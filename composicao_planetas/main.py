import csv
import matplotlib.pyplot as plt
import numpy as np
import os

#tentar fazer outro que tenha a relacao entre distancia e frequencia de elementos, ou seja, quais elementos aparecem mais nos planetas mais proximos do sol e quais aparecem mais nos planetas mais distantes do sol
elementos = ['co2','n2','o2','ar','he','na','k','h2']
densidade = [1.98, 1.25, 1.43, 1.78, 0.179, 0.97, 0.86, 0.09]
tamanho = [2.3, 1.9, 2.0, 1.9, 1.4, 1.9,2.3, 1.2]#raio molecular em Å 0,23nm=2,3Å, conferir depois
colors = np.array(['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown'])
planetas = ('mercurio', 'venus', 'terra', 'marte', 'jupiter', 'saturno', 'urano', 'netuno')

def funcao(elementos, colors):
    porc = []
    planeta = input("Digite o nome do planeta: ")

    if planeta not in planetas:
        print("Planeta inválido. Tente novamente.")
        return

    d = [] #y, distancia do sol
    t = []

    def composicao(planeta):
        with open('composicao_hea.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['planeta'] == planeta:
                    for elemento in elementos:        
                        #print(f"{elemento}: {row[elemento]}%")
                        porc.append(float(row[elemento]))

    with open('composicao_hea.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #pegar todas as distancias do sol
                d.append(float(row['dist_sol']))
                #pegar as temperaturas
                t.append(float(row['temp']))
            
    composicao(planeta)
    #print(porc)

    #desenhar o grafico
    d_a = np.array(densidade)
    t_a = np.array(tamanho)
    sizes = np.array(porc)
    
    print("--------------------------------------------------------")
    for i in range(len(elementos)):
        if porc[i] != 0:
            print(f"{colors[i].ljust(8)} | {elementos[i].ljust(3)}: {porc[i]}%")

    print("\n\n\n")
            
    plt.scatter(d_a, t_a, c=colors, s=sizes*10, alpha=0.8, cmap='nipy_spectral')

    plt.title(f"Composição de {planeta}")
    plt.xlabel("Densidade dos elementos")
    plt.ylabel("Tamanho do raio atômico (Å)")

    plt.colorbar()

    plt.show()


while True:
    os.system('clrt' if os.name == 'nt' else 'clear')
    funcao(elementos, colors)



