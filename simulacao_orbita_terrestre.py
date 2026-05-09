import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#---- constantes -----
G = 6.67430e-11  # Constante de gravitação universal (m^3 kg^-1 s^-2)
M_Sol = 1.989e30  # Massa do Sol (kg)
#acho q nao será necessário usar a massa da Terra
V_terra = 29780  # Velocidade orbital média da Terra (m/s)
d_terra_sol = 1.496e11  # Distância média da Terra ao Sol (m)
#e = 10^x
#---- condições iniciais -----
pos_x, pos_y = d_terra_sol, 0.0  # Posição inicial da Terra (m)
vel_x, vel_y = 0.0, V_terra  # Velocidade inicial da terra,, no inicio, fazer ela se mover apenas em y, o que cria a órbita
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
#objeto da terra que sera animado
terra, = ax.plot([], [], "bo", markersize=5, label = "Terra") #terra, 'bo' = blue orbit
rastro, = ax.plot([], [], "w-", alpha=0.3, linewidth=1) #rastro da terra, 'w-' = white line, alpha = transparencia da linha, linewidth = espessura da linha
#terra_dot e rastro são os objetos que serão atualizados a cada frame da animação, por isso são definidos como variáveis e estao vazios
#animacao
def animate(i):
    global pos_x, pos_y, vel_x, vel_y
    pos_x, pos_y, vel_x, vel_y = calcular_prox_pos(pos_x, pos_y, vel_x, vel_y)
    x_lista.append(pos_x)
    y_lista.append(pos_y)
    terra.set_data([pos_x], [pos_y])
    rastro.set_data(x_lista, y_lista)
    return terra, rastro   
ani = animation.FuncAnimation(fig, animate, frames=365, interval=30, blit=True) #365 frames para um ano, intervalo de 50ms entre cada frame
plt.title("Simulação da órbita da Terra ao redor do Sol")
plt.legend(loc='upper right')
plt.show()
