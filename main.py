import banner
import time
import numpy as np
from termcolor import colored
from ping3 import ping
import matplotlib.pyplot as plt
banner.banner()
site = input(colored('[+] Insira o IP/Dominio do site que quer verificar : ','green'))

down = ping(site)
if down == int('0'):
    print(colored(f'[-] Não foi possivel alcançar {site}','red'))
    time.sleep(0.5)
    input(colored('[!] Pressione ENTER para sair...','red'))
    exit()
else:
    print(colored(f'[+] A iniciar...','green'))
    pass

f = open("testes.pings","w+")
for i in range(20):
    teste = ping(f'{site}')
    teste = float(teste)
    teste = teste * 1000
    teste = int(teste)
    f.write(f'{teste}\n')
    i = i + 1
f.close()

print(colored(f'[+] Teste finalizado com sucesso!','green'))

dados = np.loadtxt("testes.pings")
y1 = np.array(dados)
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

plt.plot(x1, y1, label="Oscilação do Ping")
plt.xlabel('Tempo (s)')
plt.ylabel('Ping (ms)')
plt.title('Variação do Ping')
plt.legend()
plt.show()
input()