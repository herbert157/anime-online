import requests

def carregar_arquivo(anime):
    arquivo=open('anime.txt','r')

    for linha in arquivo:
        dado=linha.split()
        anime.append(dado[0])
        anime.append(dado[1])

    arquivo.close()

    return anime


def anime_verificar(anime,quantidade):

    try:
        for i in range(0,quantidade,2):
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
    print('Digite o nome do anime, por favor:')      #criar uma verificação para caso o anime não for encontrado!!
    nome=input()
    print('Digite o episodio:')
    episodio=int(input())
    anime.append(nome)
    anime.append(episodio)
    arquivo.write('%s %s\n'%(nome,episodio))
    arquivo.close()
    return anime

def anime_online():

    try:        
        print('Digite o nome do anime, por favor:') 
        nome=input()
        print('Digite o episodio:')
        episodio=int(input())
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

    for i in  range(0,len(anime)):
        if anime[i]==nome:                                    ##arrumar essa função
            anime[i]=anime[len(anime)-2]
            anime[i+1]=anime[len(anime)-1]
            anime.remove(anime[len(anime)-2])
            anime.remove(anime[len(anime)-1])

    print(anime)

    return anime
    

anime=[]
anime=carregar_arquivo(anime)
quantidade=len(anime)
anime_verificar(anime,quantidade)

print('\n########BEM-VINDO AO PROGRAMA VERIFICADOR DE ANIME########\n')

#print(anime)

while True:
    print('\nDigite 1 para adicionar um novo anime\nDigite 2 para fazer uma verificação rápida de um anime especifico\nDigite 3 para verificar todos os animes salvos no arquivo\nDigite 4 para remover um anime listado\nDigite 5 para sair')
    x=int(input())
    if x==1:
        anime=add_anime(anime)        
        quantidade=len(anime)
    elif x==2:
        anime_online()
    elif x==3:
        anime_verificar(anime,quantidade)
    elif x==4:
        anime=remover_anime(anime)
    elif x==5:
        exit(1)
        

    




