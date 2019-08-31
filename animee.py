import requests

def carregar_arquivo(anime):
    arquivo=open('anime.txt','r')

    for linha in arquivo:
        dado=linha.split()
        anime.append(dado[0])
        anime.append(dado[1])

    arquivo.close()

    return anime


def anime_verificar(anime):

    try:
        for i in range(0,len(anime),2):
            if int(anime[i+1])<9:
                requisicao=requests.get('https://www.animesvision.com.br/animes/%s/episodio-0%s/legendado'%(anime[i],anime[i+1]))
            else:
                requisicao=requests.get('https://www.animesvision.com.br/animes/%s/episodio-%s/legendado'%(anime[i],anime[i+1])) 
            if requisicao.status_code==200:
                print('O episódio %s do anime %s está ONLINE'%(anime[i+1],anime[i]))
            else:
                print('O episódio %s do anime %s NÃO está ONLINE'%(anime[i+1],anime[i]))        
    except ConnectionError as e:
        print('ERRO DE REDE:',e)
    except HTTPError as e:
        print('ERRRO HTTP',e)
    except Timeout as e:
        print('TEMPO EXCEDIDO',e)
        
def add_anime(anime):
    
    arquivo=open('anime.txt','a')
    print('Digite o nome do anime, por favor:')     
    nome=input()
    print('Digite o episodio:')
    episodio=int(input())
    nome=converter_string(nome)
    anime.append(nome)
    anime.append(episodio)
    arquivo.write('%s %s\n'%(nome,episodio))
    arquivo.close()
    return anime

def anime_online():

    try:        
        print('Digite o nome do anime, por favor:') 
        nome=input()
        nome=converter_string(nome)
        print('Digite o episodio:')
        episodio=int(input())
        if(episodio<9):
            requisicao=requests.get('https://www.animesvision.com.br/animes/%s/episodio-0%s/legendado'%(nome,episodio))
        else:
            requisicao=requests.get('https://www.animesvision.com.br/animes/%s/episodio-%s/legendado'%(nome,episodio))
        if(requisicao.status_code==200):
            print('EPISÓDIO ONLINE\n')
            print(requisicao.url)
        else:
            print('ANIME OU EPISODIO NÃO ENCONTRADO')
    except ConnectionError as e:
        print('ERRO DE REDE:',e)
    except HTTPError as e:
        print('ERRRO HTTP',e)
    except Timeout as e:
        print('TEMPO EXCEDIDO',e)

def remover_anime(anime):
    
    print('Digite o nome do anime que deseja remover')
    nome=input()
    print(anime)

    nome=converter_string(nome)
    posicao=buscar(anime,nome)
                                          #arrumar essa função
    if(posicao==-1):
        print('ANIME NÃO ENCONTRADO!\n')
        return anime
    anime.pop(posicao)
    anime.pop(posicao)

    arquivo=open('anime.txt','w')

    for i in range(0,len(anime),2):
        arquivo.write('%s %s\n'%(anime[i],anime[i+1]))

    arquivo.close()
    return anime
    
def buscar(anime,nome):
    contador=0
    for i in anime:
        if(i==nome):
            print('achei!!')
            return contador
        contador+=1
    return -1

def converter_string(string):
    texto=""
    contador=0
    ultimo=0

    string=str(string)+' '

    for i in string:
        if(i==' '):
            if(ultimo==0):
                texto=str(string[ultimo:contador])
            else:
                texto=str(texto[:])+'-'+str(string[ultimo+1:contador])
            ultimo=contador
        contador+=1
    return texto

anime=[]
anime=carregar_arquivo(anime)
quantidade=len(anime)
anime_verificar(anime)

print('\n########BEM-VINDO AO PROGRAMA VERIFICADOR DE ANIME########\n')

#print(anime)

while True:
    print('\nDigite 1 para adicionar um novo anime\nDigite 2 para fazer uma verificação rápida de um anime especifico\nDigite 3 para verificar todos os animes salvos no arquivo\nDigite 4 para remover um anime listado\nDigite 5 para sair')
    x=int(input())
    if x==1:
        anime=add_anime(anime)        
    elif x==2:
        anime_online()
    elif x==3:
        anime_verificar(anime)
    elif x==4:
        anime=remover_anime(anime)
    elif x==5:
        exit(1)
    elif x==6:
        print(anime)
        print(len(anime))
        

    




