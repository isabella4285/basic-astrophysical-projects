import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#---- constantes -----
G = 6.67430e-11  # Constante de gravitação universal (m^3 kg^-1 s^-2)
M_Sol = 1.989e30  # Massa do Sol (kg)
#acho q nao será necessário usar a massa da Terra
V_terra = 29780  # Velocidade orbital média da Terra (m/s)
d_terra_sol = 1.496e11  # Distância média da Terra ao Sol (m)
d_mercurio_sol = 0.39*d_terra_sol #distancia de mercurio ao sol, 0.39 vezes a distancia da terra ao sol
V_mercurio = 47.87*1000 #velocidade orbital média de
d_venus_sol = 0.72*d_terra_sol #distancia de venus ao sol, 0.72 vezes a distancia da terra ao sol
V_venus = 35.02*1000 #velocidade orbital média de venus 
d_marte_sol = 1.52*d_terra_sol #distancia de marte ao sol, 1.52 vezes a distancia da terra ao sol
V_marte = 24.077*1000 #velocidade orbital média de marte
d_jupiter_sol = 5.2*d_terra_sol #distancia de jupiter
V_jupiter = 13.07*1000 #velocidade orbital média de jupiter
d_saturno_sol = 9.58*d_terra_sol #distancia de saturno
V_saturno = 9.69*1000 #velocidade orbital média de saturno
d_urano_sol = 19.2*d_terra_sol #distancia de urano
V_urano = 6.81*1000 #velocidade orbital média de urano
d_netuno_sol = 30.05*d_terra_sol #distancia de netuno
V_netuno = 5.43*1000 #velocidade
#e = 10^x

#listas
planetas = ["mercurio", "venus", "terra", "marte", "jupiter", "saturno", "urano", "netuno"]
distancias = [0.39, 0.72, 1, 1.52, 5.2, 9.58, 19.2, 30.05] #distancia dos planetas ao sol em UA
velocidades = [47.87, 35.02, 29.78, 24.077, 13.07, 9.69, 6.81, 5.43] #velocidade orbital média dos planetas em km/s
cores = ["ro", "yo", "bo", "go", "co", "mo", "wo", "ko"] #cores para cada planeta, ro = red orbit, yo = yellow orbit,



#---- condições iniciais -----
pos_x, pos_y = d_terra_sol, 0.0  # Posição inicial da Terra (m)
vel_x, vel_y = 0.0, V_terra  # Velocidade inicial da terra,, no inicio, fazer ela se mover apenas em y, o que cria a órbita
vel_x_mercurio, vel_y_mercurio = 0.0, V_mercurio
vel_x_venus, vel_y_venus = 0.0, V_venus
vel_x_marte, vel_y_marte = 0.0, V_marte
vel_x_jupiter, vel_y_jupiter = 0.0, V_jupiter
vel_x_saturno, vel_y_saturno = 0.0, V_saturno
vel_x_urano, vel_y_urano = 0.0, V_urano
vel_x_netuno, vel_y_netuno = 0.0, V_netuno

dt = 24*3600 #delta t, 1 dia
x_lista, y_lista = [], [] #listas para armazenar as posições da terra ao longo do tempo, usadas para desenhar o rastro
def calcular_prox_pos(px, py, vx, vy):
    #usar pitagoras
    r = np.sqrt(px**2+py**2)
    #aceleracao, F = m*a, F = G*M_Sol*m/r^2, a = F/m
    a = (-1)*G*M_Sol/r**2
    ax = a*(px/r) #decomposicao vetorial de a, para saber quanto dessa aceleracao é em x e quanto é em y
    ay = a*(py/r)

    #usar o metodo de Euler para atualizar a posição e velocidade -> v = v0 + a*dt
    vx += ax*dt
    vy += ay*dt
    px += vx*dt
    py += vy*dt
    return px, py, vx, vy
#---- configuração do gráfico -----
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal') # para ficar mais homogeneo, sem distorção
ax.set_facecolor('black') #cor de fundo do gráfico
ax.set_xlim(-2e11, 2e11) #limites do gráfico em x
ax.set_ylim(-2e11, 2e11) #limites do gráfico em y

#desenhar o sol
sol, = ax.plot([0], [0], 'yo', markersize=12, label = "Sol") #sol no centro do gráfico, 'yo' = yellow orbit, markersize = tamanho do marcador
#objetos
terra, = ax.plot([], [], "bo", markersize=5, label = "Terra") #terra, 'bo' = blue orbit
mercurio, = ax.plot([], [], "ro", markersize=3, label = "Mercúrio") #mercurio, 'ro' = red orbit
venus, = ax.plot([], [], "yo", markersize=3, label = "Vênus") #venus, 'yo' = yellow orbit
marte, = ax.plot([], [], "ro", markersize=3, label = "Marte") #marte, 'ro' = red orbit
jupiter, = ax.plot([], [], "co", markersize=3, label = "Júpiter") #jupiter, 'co' = cyan orbit
saturno, = ax.plot([], [], "mo", markersize=3, label = "Saturno") #saturno, 'mo' = magenta orbit
urano, = ax.plot([], [], "wo", markersize=3, label = "Urano") #urano, 'wo' = white orbit
netuno, = ax.plot([], [], "ko", markersize=3, label = "Netuno") #netuno, 'ko' = black orbit
rastro_t, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro da terra, 'w-' = white line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_me, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de mercurio, 'r-' = red line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_ve, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de venus, 'y-' = yellow line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_ma, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de marte, 'r-' = red line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_ju, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de jupiter, 'c-' = cyan line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_sa, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de saturno, 'm-' = magenta line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_ur, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de urano, 'w-' = white line, alpha = transparencia da linha, linewidth = espessura da linha
rastro_ne, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro de netuno, 'k-' = black line, alpha = transparencia da linha, linewidth = espessura da linha

#terra_dot e rastro são os objetos que serão atualizados a cada frame da animação, por isso são definidos como variáveis e estao vazios
#animacao
def animate(i):
    global pos_x, pos_y, vel_x, vel_y
    pos_x, pos_y, vel_x, vel_y = calcular_prox_pos(pos_x, pos_y, vel_x, vel_y)
    x_lista.append(pos_x)
    y_lista.append(pos_y)
    terra.set_data([pos_x], [pos_y])
    mercurio.set_data([pos_x/2], [pos_y/2]) #posição de mercurio, metade da distancia da terra ao sol
    rastro_t.set_data(x_lista, y_lista)
    rastro_me.set_data([x/2 for x in x_lista], [y/2 for y in y_lista]) #rastro de mercurio, metade da distancia da terra ao sol
    return terra, mercurio, rastro_t, rastro_me   

ani = animation.FuncAnimation(fig, animate, frames=365, interval=30, blit=True) #365 frames para um ano, intervalo de 50ms entre cada frame
plt.title("Simulação da órbita da Terra ao redor do Sol")
plt.legend(loc='upper right')
plt.show()
