import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# ---- constantes -----
G = 6.67430e-11  
M_Sol = 1.989e30  
AU = 1.496e11  # Unidade Astronômica em metros

# Dados dos planetas: [Distância ao Sol (UA), Velocidade Orbital (m/s), Cor, Tamanho]
dados_planetas = {
    "Mercúrio": [0.39, 47870, "gray", 3],
    "Vênus": [0.72, 35020, "orange", 5],
    "Terra": [1.0, 29780, "blue", 5],
    "Marte": [1.52, 24077, "red", 4],
    "Júpiter": [5.2, 13070, "brown", 10],
    "Saturno": [9.58, 9690, "gold", 9],
    "Urano": [19.2, 6810, "cyan", 7],
    "Netuno": [30.05, 5430, "blue", 7]
}

# Configuração de tempo: 1 dia por frame (aumente para acelerar a simulação)
dt = 24 * 3600 * 5  # 5 dias por frame para os planetas externos se moverem visivelmente

# Inicialização de estados (Posição e Velocidade)
estados = {}
for nome, info in dados_planetas.items():
    estados[nome] = {
        "px": info[0] * AU,
        "py": 0.0,
        "vx": 0.0,
        "vy": info[1],
        "x_lista": [],
        "y_lista": []
    }

def calcular_prox_pos(p):
    r = np.sqrt(p["px"]**2 + p["py"]**2)
    a = -G * M_Sol / r**2
    ax = a * (p["px"] / r)
    ay = a * (p["py"] / r)

    # Método de Euler-Cromer (estabilidade orbital melhorada)
    p["vx"] += ax * dt
    p["vy"] += ay * dt
    p["px"] += p["vx"] * dt
    p["py"] += p["vy"] * dt
    return p

# ---- configuração do gráfico -----
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.set_facecolor('black')

# Limite para ver até Netuno (30 UA + folga)
limite = 35 * AU
ax.set_xlim(-limite, limite)
ax.set_ylim(-limite, limite)

# Desenhar o Sol
ax.plot([0], [0], 'yo', markersize=15, label="Sol", markeredgecolor="orange")

# Criar objetos gráficos para cada planeta
graficos = {}
for nome, info in dados_planetas.items():
    dot, = ax.plot([], [], 'o', color=info[2], markersize=info[3], label=nome)
    rastro, = ax.plot([], [], '-', color=info[2], alpha=0.3, linewidth=1)
    graficos[nome] = (dot, rastro)

def animate(i):
    artistas = []
    for nome in dados_planetas:
        p = estados[nome]
        dot, rastro = graficos[nome]
        
        # Calcula física
        calcular_prox_pos(p)
        
        # Atualiza rastros (limitando tamanho para não travar a memória)
        p["x_lista"].append(p["px"])
        p["y_lista"].append(p["py"])
        if len(p["x_lista"]) > 500: # Mantém os últimos 500 pontos
            p["x_lista"].pop(0)
            p["y_lista"].pop(0)
            
        dot.set_data([p["px"]], [p["py"]])
        rastro.set_data(p["x_lista"], p["y_lista"])
        
        artistas.extend([dot, rastro])
    return artistas

ani = animation.FuncAnimation(fig, animate, frames=500, interval=20, blit=True)

plt.title("Simulação do Sistema Solar (Escala Real de Distância)")
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.grid(color='white', linestyle='--', alpha=0.1)
plt.show()
