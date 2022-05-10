import random

# conversro de texto para ASCII: https://patorjk.com/software/taag/#p=display&f=Crazy&t=Subnaotica
# conversor de imagem para ASCII: https://www.text-image.com/convert/result.cgi

# código cortesia de Enzo Quental
import sys,time
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

# Fonte: Crazy     Texto: Subnaotica     O "~" foi adicionado posteriormente, já que o site não reconhece acentos 
# Criando e dando print na logo do jogo
def logo():
    print("")
    logo = print('''                                                      .-''-.                     _..._               
                                                    '   _    \                .-'_..._''.            
                     /|           _..._           /   /` '.   \       .--.  .' .'      '.\           
                     ||         .'     '.        .   |     \  '       |__| / .'                      
                     ||        .   .-.   .  /\/  |   '      |  '  .|  .--.. '                        
                     ||  __    |  '   '  |    __ \    \     / / .' |_ |  || |                 __     
       _     _    _  ||/'__ '. |  |   |  | .:--.'.`.   ` ..' /.'     ||  || |              .:--.'.   
     .' |   | '  / | |:/`  '. '|  |   |  |/ |   \ |  '-...-'`'--.  .-'|  |. '             / |   \ |  
    .   | /.' | .' | ||     | ||  |   |  |`" __ | |             |  |  |  | \ '.          .`" __ | |  
  .'.'| |///  | /  | ||\    / '|  |   |  | .'.''| |             |  |  |__|  '. `._____.-'/ .'.''| |  
.'.'.-'  /|   `'.  | |/\ ..' / |  |   |  |/ /   | |_            |  '.'        `-.______ / / /   | |_ 
.'   \_.' '   .'|  '/'  `'-'`  |  |   |  |\ \._,\ '/            |   /                  `  \ \._,\ '/ 
           `-'  `--'           '--'   '--' `--'  `"             `'-'                       `--'  `"  ''')

# print na tela de morte, quando o oxigênio atinge um número menor ou igual a 0
# imagem: https://www.pinterest.com/pin/283937951496139285/  : fonte da imagem do Cacodemon, inimigo do DOOM (1993)
def cacodemon():
    print(''' 
                               ~5.                                       .~                  ^.        
           .?.                !P5.                                       :G!                :P.        
           .YP7.             :5JJ                                        .Y5!             .7PP.        
            :P55~           .JJ77                                        ^7Y?            ^J5G~         
             !PYY?^         !P?!~^                                      :!!JP~         ^?Y5G?          
              JG5JJ?^       7BY7~?!              .~~~~~~.              ^7!7YB7       ^?JY5GY.          
               ~G5JJJ?~^    .PGJ!!7!:    :^^: ~YGBBBBBBBBGYJ^        :!7!7JG#?    .^?JJY5GG.           
                ~GPYJ????^.  P&BGGGGGP?5B####G####BBGGBB#####GGGGJ^!PGGGGGB&B: .^77??J5PBG:            
                ^GGP5J?77!!~5B#&&##########BBBBBBG5JJPGBBBBBB#&########&&#BJ~!!77?Y5PG#G:             
    :             ^BBP55Y?!~~^::~YB####BB####BBBBBBG5PGBBBBBB###BB#####G?~::^~~!?Y55PB#J.            ..
    ^?!^.          .YBPPP5Y?7~^:...?#####B##########BBB##B#####B##B###7. .:^~7JY55PGBG7        ....^7?.
      ^JY7~^. :75PB&#GP55555YJ7!^~G#BB####&&##########B###&#####BB#G^~!7JY55555GB##B5P~     .^~??YY?:  
        ^JY?!!~7YGGB#####GP5555555JJGBBB#########BB###BBB#########BB#B?JY55555PPG#####BGPJ77!7?Y57.    
        :YPJ?7777JPGB###BGGGGGPPPGBB#####B####&&######&####BB#####BBBPPPPGGBB####BG5J?777?YPP?.      
        .PBBGP5YJY5PB#&&######BB##############&&&&&&&&&&#####################&&&#BP5YYY5PG#?.                                     ▄█▀█▄
        G#BB###BGGBBB##&&&&&&&&#######BBB#####&&&&&&&&&&#####BB########&&&&&&&###BBBGBBB##BBP~        
        .5&##BBB###########&&#&&&&######BBBBBBB###&&&&&&###BBBBBBB#####&&&&&##############BBB#&##P^     ██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
    .JB#################&###&&&&&&&&&#######BBB###&&###BB#######&&&&&#&&&&&##&###################:      ▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
    G&#############BBB##########BGGB##&&&#&################&#&&&#BBBGB##########BBB######&######&P       ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
    J&&&&&&&&##B#&######BGGGB##B#BPGGBB&&&###&&&&&&&&&&&&&&##&&&#BGGPGBBB##GPBBB######&#B#&&&&&&&&P       ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
    !&&&&&&&&&&&&&&&&BGGGP5PPGB##BPPPGB#&&#&&&&#BGPB##BB#&&&&#&&#BP55GB##BGP55PGGG#&&&&&#&&&&&&&&&G.       ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
    .Y###&&&&&&&&&#BGPPGP5YJY55GBB##BBGPPB#&B##B5YJY#&BYYP#&B#&#GPGGB###BBP55YJ5PGGPGB#&&&&&&&&&&###B?     ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
    .PBBB###&&&&&&&BBGBPY?JYJJ?JY5PGBBB#BGGBGBGG##GBB##GGB#BGGBGBGGB#BBBGP5YJ?JYYJ?5PPGBB&&&&&&&###BB##!   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
    B#B####&&&&&&&&&##B5JYPP5YJ???7JYPPGGB##GG#####BBGGBB####BGG##BGGP5Y?77??JY5PPYYPB##&&&&&&&&&###B##P     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
    #####&&#GGB#&&B#&&#PPBBG555YJJJJ?!!7Y55PPGGB###&&&&&&##BBGGP555J7!7?JJJYY55PGBGGG#&&##&&&&&&&&&#####                         
    &&#&&#GP55G#&&J?P#&&&##BGP55PPJ7!7?Y55JJJJ????YPB&#B5J77?JJJJJ55J7!!7YPPY5PGB##&&#B5?P&&&&&&&&&&&#&&
    G&&&#GPPGB#&&@#5BPYG&&#BBGPGPYJJY5PP5Y55YYJ?7!~~J#B7~~!7?JY55YY5PP5JJJ5PGGGB#&&#PJGGP#&@&&&&&&&&&&&&
    Y&&&####&&&&&@@&&G?!5#&&##BGPPGP5YJ?77!7JYJ!!~~^7GG~^!!!!JYJ77!7JY5PGGPPB###&#GJ7JB&@@@@@&&&&&&&&&&#
    &&&&&&&&&###&&@&&&BY?YGBGG#&###BP55YJ?7~7J?!~~^7GJPP~^~!!??!~7?JY5PGB####BGGGPYJYB@@@@@&#&&&&&&&&&&&
    #&&&######Y:5&&&&&&BP5P##J7Y#&#&#BBGP5JJ?77YJ7~JB!?B?^7YJ77JJY5GBBB###&BJ75BG55PB&@&&&&?:P&#&###&&&#
    :G#######B5?P#&&&&&&BB#&@BYJGG7JB######BP55P5Y?PBPGB57YPP55PB######G??BGJ5#@&&BB&&&#&&#G?5########G:
    ~#####BBBB##&#&&&&&&&@@@@#GGGY?P###########BGGBGGGGBGBB##########GYJYGBG#@@@@&&&########BBBB#####~ 
    !G###BBBGBBGJ5B&?~5&@@@@@&&&B5B&GP##GY5GBB###BGPPGB###BBPYYB&GPB#BGB&&&&@&&&&5^J&GYYGBBGBBB####J  
    7#######BBB?!G&?:7B&&@@@@@@@&@#7!5##JJP#&#5J5PYYGYJP#&B5JJ##J~5&&&&&&&&##&#G7:7&5~YGBB########?  
    P####&&##BB#B##P5#&&&#&&&@@@@@G!:7P#&B#&&&BPBGJJGBGB&&&##&#5~^?B&&&###&&##&&B5G&###B###&#####P^  
    :###&&###B##BBB#BB###B#&&&&&&@G7~!JG&&&&&##B##GG#&#BB#&&&#GJ~!JG&###&&&#B###B##BBB##########B.   
        7#&#BPYYY5G####BGGPBBBPYB###&GY7!7YG#&#PJ?5####&#Y??B&##PY7!7Y#####GYPBBGGBBB##&##########&B    
        ^&&&#GPYJ?5GB#&##BGPGBBGBPJB##GY77JP#&#57!7B&##&P!!!G&##5J775P##PYG#GBBBGG###GP#&#B##&&&&&&#!   
    ~#&P?5BBGP5PGBB##&&#BGGBBGGBB#&&#BBB####BGPG#BBBBBGGG#####BGB#&&#BBBGBBBB###G5Y5B&##&&&&55&&&G   
    J&&5:  ^B#BBBB#&##&&&##BBBBBBB#&&&&&###B###BBBBBBBB##BBB##&&&&&#BBBBGBB###G55PG#&&&&&B!: ^#&&J   
        .Y#&BBB&&##B##BB##&&&&#######BB###BB######BB#B#BBBB###BBB###BBB######&&&#BBBBB####&&&BBB&&5.    
        .?JJJYGG577P#BBB###&###&&&###############BB##BB####&####BB#####&####&&##BB##Y~7PG5JJJJJ!      
                ?Y7!7Y#&BBB##BBB#&&&&&#####&&##&####B##BB###&##&&#####&&&&##BBB##BB#&GJ~!?YY            
                P5Y5GB#&BB##BB#&###&#&&##&&#BBB#&&&##B###&&##BB##&###&&#&&##&#BB##BB&#BPYY5P.           
                ~BPGBGBB&&&&###&BY#&&&&&###B#G?P&&&&&##&&&&G?P#B####&&&&&#YB&###&&&&&PYBGPB?            
                .PG?.   ^^:~P##&&&&G^:^P&###J^5&&##&&&##&&#&#P#GP#&#&#7~G&&&##P~!#B!:  .PB?             
                ^:          :5##&&&P^.:G&&&#&&Y5?G&BPG###?Y@&&#P#&J^B#B&#B&&BJ?J^      ^7              
                            ...:7?P&&&&&&@@#^:G&P..?55###&&@@@&&&B#&B#5GY:...                        
                                    :^^^^^^Y&&&&Y~??^  ^P&&&P7J#7^?#7 .^.                            ''')


# coloquei o início do jogo como uma função separada do jogo principal, pois fica mais fácil de separar o tutorial do resto do 
def inicio():
    logo()
    print("")
    print_slow("Bem vindo ao jogo, espero que sobreviva...")
    print("")
    nome = 0

    # se o jogador não responder a pergunta adequadamente, o programa continua fazendo ela até que ele responda algo válido
    while nome == 0:
        nome_jogador = input("Gostaria de escolher um nome? Digite [S] para SIM ou [N] para NÃO: ")
        if nome_jogador == "S" or nome_jogador=="s" or nome_jogador == "N" or nome_jogador=="n":
            nome = 1
    print("")
    # se o jogador escolher ter um nome, a variável de entrada é substituída pelo nome do jogador
    if nome_jogador == "S" or nome_jogador=="s":
        nome_jogador = input("Me diga seu nome: ")
    else:
        nome_jogador = ""
    
    continuar_rodando_while = 1
    print("")
    print("")
    # se o jogador não responder a pergunta adequadamente, o programa continua fazendo ela, mas o programa não guarda a resposta do usuário
    # 
    while continuar_rodando_while == 1:
        print_slow("É sua primeira vez jogando o jogo? Digite [S] para SIM ou [N] para NÃO:")
        print("")
        resposta_jogooun = input("Digite aqui sua resposta: ")
        if resposta_jogooun == "S" or resposta_jogooun == "s" or resposta_jogooun == "N" or resposta_jogooun == "n":
            continuar_rodando_while = 0
    
    # valida sua entrada de tutorial, o continuar_rodando_while 1 é equivalente e TRUE e o 0 é equivalente a FALSE, apenas uma maneira diferente de representar a operação booleana
    continuar_rodando_while = 1
    while continuar_rodando_while == 1:
        print_slow("Gostaria de realizar o tutorial do jogo? Digite [S] para SIM ou [N] para NÃO ")
        print("")
        resposta_jogooun = input("Digite aqui sua resposta: ")
        if resposta_jogooun == "S" or resposta_jogooun=="s" or resposta_jogooun == "N" or resposta_jogooun=="n":
            continuar_rodando_while = 0

    # esse código roda o tutorial, ou seja, apenas é lido se a resposta do usuário for "S" ou "s"
    if resposta_jogooun == "S" or resposta_jogooun=="s":
        print_slow("'SUBNÃOTICA' tem base no jogo Deep Sea Adventure, um jogo onde você, o jogador, terá a oportunidade de se aventurar por um mapa cheio de tesouros, mas tome cuidado com seu oxigênio, ele tende a acabar mais cedo do que muitos gostariam...")
        print("")
        print("")
        print("Seu nível de oxigênio começa com 25 pontos. Cada rodada é uma nova necessidade de seu personagem respirar. O número de tesouros carregados será subtraído do seu nível de oxigênio.")
        print("")
        print("")
        print_slow("Exemplo: você está carregando 3 tesouros (o valor deles não importa) e decide prosseguir com sua descida ao fundo do mar. Seu nível de oxigênio antes da rodada era de 19 pontos, agora, ele tem o valor de 16 pontos.")
        print("")
        print("")
        print("EXEMPLO: você está na posição 27")
        print("")
        posição(27)
        print("")
        print("")
        print_slow("O mapa será exposto dessa exata maneira cada vez que você rodar o dado, preste atenção na sua posição, pois tesouros maiores sempre se encontram nas maiores profundezas do mar...")
        print("")
        print("")
        print_slow("Tome cuidado com as posições, se você passar da última casa não há volta...")
        print("")
        print("")
        print_slow("VALORES DOS TESOUROS: ")
        print("")
        print_slow("posições 1 a 8 = 1 a 3 ")
        print("")
        print_slow("posições 9 a 16 = 4 a 7")
        print("")
        print_slow("posições 17 a 24 = 8 a 11")
        print("")
        print_slow("posições 25 a 32")
        print("")
        print("")
        print_slow("Tome muito cuidado com a sua direção, uma vez que você optar por voltar ao submarino não há como retornar as profundezas")
        print("")
        print("")
        print_slow("outra coisa a levar em conta são os tesouros, já que você não consegue retornar ao submarino sem pelo menos 1")

    print("")
    print("")
    print_slow("Pressione ENTER, sabe, aquela tecla do seu teclado, pra começar a gameplay de alto nível")
    print("")
    print("")

    entre = 0
    while entre==0:
        entre = input("Por favor, pressione apenas ENTER para continuar, qualquer outra tecla ou combinação de teclas vai fazer com que você volte para essa mensagem: ")
        if entre == "":
            entre = 1
        else:
            entre = 0

    player_position = 0
    while player_position == 0:
        posição(0)
        print_slow("Para começar a aventura, saia do submarino")
        print("")
        print("")
        sair = input("Pressione ENTER para sair do submarino: ")
        if sair == "":
            player_position = 1

    return nome_jogador


# Essa função roda os dados e retorna a soma deles, para que o número de casa seja calculado
def roda_dado():
    dado1 = random.randint(1,3)
    dado2 = random.randint(1,3)
    dado = dado1 + dado2
    return dado



def rodar_tesouros(tesouros,position):
    escolha_certa = 0
    # Esse while roda a mesma pergunta se o 
    while escolha_certa==0:
        print_slow("Deseja se livrar de algum tesouro ou vasculhar por novos? Pressione [v] para VASCULHAR ou [l] para LARGAR" )
        print("")
        print("")
        player_input = input("Nos diga sua escolha, ó corajoso mergulhador: ")
        if player_input=="v" or player_input=="l" or player_input=="L" or player_input=="V":
            escolha_certa = 1
        else:
            print_slow("Responda a pergunta adequadamente, se não voltará para essa mensagem")
            print("")
    
    # se o jogador decidir vasculhar por tesouros ele cai dentro desse if
    if player_input == "v" or player_input == "V":
        
        # esse é o if que calcula o tesouro baseado na posição do jogador
        if position<9:
            tesouro_vasculhado = random.randint(0,3)
        elif position<16:
            tesouro_vasculhado = random.randint(4,7)
        elif position<24:
            tesouro_vasculhado = random.randint(8,11)
        elif position<=32:
            tesouro_vasculhado = random.randint(12,15)

        num_tesouros = len(tesouros)
        # Se o número de tesouros for maior que 3, ou seja, se ele fo 4, o jogador precisa se despedir de um de seus preciosos tesouros, para que ele seja substituído pela novo que foi vasculhado
        if num_tesouros>3:
            print("Suas forças permitem apenas 4 tesouros, e você deseja adicionar mais um? Escolha um para ser despejado")
            print("")
            print(tesouros)
            print("^   ^   ^   ^")
            print("|   |   |   |")
            print("1   2   3   4")
            print("escolha uma das posições:  1   2   3   4")
            escolha_despejar = int(input("Escolha aqui qual tesouro deverá ser despejado no Oceano, seu maníaco: "))
            del tesouros[escolha_despejar-1]

        print(f"Tesouro descoberto: {tesouro_vasculhado}")

        # Se o tesouro vasculhado for igual a 0, o programa humilha o jogador e não adiciona o tesouro a lista
        if tesouro_vasculhado==0:
            print_slow("Otário, kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk n pegou tesouro nenhum kkkkkkkkkkkkkkk")
            
        
        # O jogador agora tem a opção de adicionar o tesouro a lista, se ele for maior que 0
        continuar_rodando_while = 1
        while continuar_rodando_while == 1 and tesouro_vasculhado>0:
            print("")
            print_slow("Deseja adicionar ele aos seus tesouros? Digite [S] para SIM ou [N] para NÃO")
            print("")
            escolha_tesouros = input("Digite aqui sua escolha: ")
            print("")
            if escolha_tesouros == "S" or escolha_tesouros=="s" or escolha_tesouros == "N" or escolha_tesouros=="n":
                continuar_rodando_while = 0
            if escolha_tesouros == "S" or escolha_tesouros=="s":
                tesouros.append(tesouro_vasculhado)
    

    else:
        if len(tesouros)>0:
            print("")
            print_slow("Escolha um para ser despejado")
            print("")
            print(tesouros)
            print("^  ^  ^  ^")
            print("|  |  |  |")
            print("1  2  3  4")
            escolha_despejar = int(input("Escolha aqui qual tesouro deverá ser despejado no Oceano, seu maníaco (coloque apenas o número): "))
            del tesouros[escolha_despejar-1] 
        else:
            print_slow("Você não possui nada, miserável")
            print("")
            escolha_certa = 0
    print("Estes são seu tesouros atuais, grande guerreiro dos sete mares: ")
    print(tesouros)
    return tesouros


# Essa função recebe a posição do jogador e dá print no mapa junto com a posição dele 
def posição(posição):
    if posição>0 and posição<=32:
        print("")
        print("")
        # https://www.gratispng.com/png-1pggiu/  link da imagem do submarino, ela foi convertida utilizando o site no início desse documento
        print("--------------------------------------------------------------------------------------")
        print('''
                                ::.                                                                    
                                !5PPJ7                                                                  
                                !PGB7Y!                                                                 
                                :^?5J?                                                                 
                                    PY?                                                                 
                                ..YY!:::::^7?~::::...                                                 
                            .:::::.......:G5##Y....::::::.                                            
                            .~.............Y5BG?..........:~.                       ^~.                
                            7:^^~~!!77777??7JJ?!!!~~^:::....!:                    :G###^               
                        ..^~!?????????????????????JJJJJJJ??7!~J.                   5#BB#5               
                    ..^J77???????????????????????????????????JJJ?J!:..             PBBB#G               
                :^:..~5?????????????????????????????????????????5~:^^^::.        ?#BB#P               
            .^:....~J757?????????????????????JJJJJ??????????????5^J:..:^~^:.    .BBB#7               
            ^^.........5?J5PPPP5Y???????????55PGGGP55J??????????75!........:^~^.  ~###.               
            !. .........JP5PYJYBGPP?????????PYG5?75#B5G???????????Y?::.........~?!. ?&7                
            ~: ........~?JG55^^^Y&JBJ????????G5P~^^:5&PPY7?????????JJ!?..........~!J!7BJ?.              
            7............?G5PYJ5GY5BJ????????PGPJ!!?BBYB???????????J?...........:!~JYYBJY:              
            ^^.........:.Y?5PPPPPGGY??????????PGGPPPPPGY??????????75!!!........:~7?^ P#:                
            ~~........?~57??JYYYJ??????????????Y5555Y?????????????5:^^......:^77~. !##P                
            :~^.......JJ????????????????????????77?????????????7Y7.......^!7!:    PBB&~               
                :~^:.:~~5???????????????????????????????????????7JP!J^:^~!7~:      .BBB#G               
                .:^~?PJ???????????????????????????????????????YG77?77!^.         :BBB##               
                    .^~7?JJJJ???????????????????????????JJY555P7~^.               G###5               
                            .:^~!77??JJYYYYYYYYYYYYJJJJ??7!~^:.                     .5GY                
                                    ............                                                     
                                                                                                        
                                                                                                        ''')
        print("")
        print("[1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]   [10]")
        print("")
        print("")
        print("[11]   [12]   [13]   [14]   [15]   [16]   [17]   [18]   [19]   [20]  [21]")
        print("")
        print("")
        print("[22]   [23]   [24]   [25]   [26]   [27]   [28]   [29]   [30]   [31]  [32]")
        print("")
        print("")
        print_slow("NUNCA se esqueça de onde está, a profundidade máxima é 32, e ter consciência da sua direção pode ser a diferença entre a vida e a morte...")
        print("")
        print("")
        print(f"Sua posição atual é {posição}")
        print("--------------------------------------------------------------------------------------")
    else:
        print("")
        print("")
        print_slow("não há como retornar...")
        print("")
        print("")


# essa função calcula o oxigênio consumido em cada rodada
def calcula_oxigenio(tesouros,oxigenio):
    oximenos = len(tesouros)
    oxigenio-=oximenos
    print("")
    if oxigenio>0:
        # fonte: DOOM   texto: oxigenio     o "^" foi adicionado posteriormente
        print('''
             _         _        _       
            (_)       / \      (_)      
    _____  ___  __ _  ___ _ __  _  ___  
    / _ \ \/ / |/ _` |/ _ \ '_ \| |/ _ \ 
   | (_) >  <| | (_| |  __/ | | | | (_) |
    \___/_/\_\_|\__, |\___|_| |_|_|\___/ 
                __/ |                   
               |___/                    ''')
        print("")
        print(f"Seu nível de oxigênio atual é {oxigenio}")
        print("")
    elif oxigenio>-24:
        print("")
        print("")
        print_slow("o oxigênio acabou...")
    print("--------------------------------------------------------------------------------------")
    return oxigenio

def se_perdeu():
    print("")
    print_slow('''                                                                                                    
                                                                                                    
                                                .7?^                                                
                                               ^5JYB!                                               
                                              !Y!7YPB:     ..                                       
                                 .    .5:    ~J~^JY5GP    ^G5                                       
                                :B7   :#B.  :?^^!5YYGB7   5#G                                       
                                ~P5^  .G#G. ?~:^7Y5J5GG. .G#P   .                                   
                                :5J5: .P##PJ!::~????J5B^ ?##J  !B:                                  
                                .J??7.:GBB#G^::^77!!?YGGPB##! .5B!                                  
                                 ?7!7?P#BB#5^^:~777!7YGGBB##: ?PB7      ~^                          
                                 !?!!!?5BBB5^^^7??7!!?PGBBBB.~JYB7     !B?                          
                                 .J77!7?5B#P!^~J7?J7!?PBBBBBY??5B!    ~GB~                          
                        !P7.      :J??77J5BB?7?YYYJ77?5BB#B577?PB~   !PGG.                          
                        ~BGGY^     ^YJ?7YPGBY7?5P5YJ?J5B#BJ!7?JGG: .?55GJ                           
                        .55YPBP~    YPYJ5GGGGJ7YPP55YPPBP?7???5GP .JJJPG:                           
                         .?Y?JPGGY!^PGPPGGGBBPJYPGGGGGG577?JYPGGG7?JJ5G!                            
                           !J??JPB####GGGBBBBBGPPGGBGPJ?J5PGBBBGYJJYPP~                             você se perdeu.......
                            :?YJYPGBB#BBGBBBBBBBGGBGGPGGGBBBBGPYJ5GG!.                              
                              ~YPGGGBBBBBBB#####BBBB###BBBBBGGGGGG?:                                
                                ^?BBBBBBBBGGGGGBB#########BBBBGY!.                                  
                                 .Y5YYJ??777??JJYYYPP555PPGG#?.                                     
                               .!?7!!!7J?J???777??YJY555YYYYPG!                                     
                              !J7!!777????7!!!!7?JPJ???5PPPP5YG5~                                   
                            :JJ??77!!~~~~~!?7!~!77???YYYJJY5PP5PB?        ..!^!~                    
                          .7G?7!~^^^~~~^~^^~!7!!~7?JJJJJJYYYYYY5P#J        :!7Y^                    
                         :??JJ~~^^^^^77^^^^^^!7YJJ7~!!7?JJJYPYYYYY#?       .!?J.                    
                        .7!!!7J?!~:::^~:^^!!?7!~^!Y?7!!?JJYY5YYYPPPG^      :JY5^                    
                       .~~~~~^^^~??::^!7?7~~^::::^~7JYJ?JJJJJ5PPP5555.... .^!7J~                    
                       ^~7!~::...:YY??!~^:.:::^!:^^~~7JY55YY555YYY5PPJ7!!~??!!.                     
                      .~~J!::..:!7??J?~^^:::..^?:^^~~!!7JPGG5J?JY5555G^                             
                      ~~~~:.:^!!~::.:!J?!^^::::^:^^~~!?55YJ?YPPYY5Y55PJ                             
                     !!~~:^!!!~~!~!!~^^!7J7^^:::^^~77JJJ?JJJJJ5PPP555YP~                            
                    :5?!7!~!?YY55J?75GY^^~7JJ!^^!??!!77??JJYYJJ55PPPGGBG.                           
                    .?P?~:7?JGP5J?557P&5^^:^~?5J7~^~!77?JJJYPYY5555PGPPG!                           
                    .!7Y7^Y!JB5JJY5P?5#B~::~7?JY7!!!!7?JJJJJYYY55PGP5Y5P5                           
                    .~~~J?!J?JY55YYJYB#G~!J?!^:^!?JJ???JJYYYYYJ5PGP5555PG.                          
                    ^!!~~Y?!777J5Y5PB##5JJ~^^^7^:^^!?5YYYYYYYYPP5Y55P55PG.                          
                    ~7Y^^~?J~^^~J555GGJ!~^:^^^?^^^~~^!?555555PPJ5555BP5PP.                          
                    !7J^^^^~?7^:::7J7^:^~!!!!!~~^^^~~~~7?5GGP5YYY555P55P5                           
                    !!~~^^^^:^????!::^!7!!!~~~!!7??7~7?YP5YJJY5PP5Y5Y5PB5                           
                    ^~~~^^^^~!?7?7^:~7~!7!~~~~!777!?JY5PYJJJJ5Y55GP55GBB7                           
                    .^~~^~!!!~:::~7~J!77~~!~!!!~!?~^7GYJJJYGPJJJYJYGGPPG^                           
                     ?7!?7^^^^^::::77~J^7!^:^^~7!!J^~5JJJ5BY!JYY5PJJP5PG^                           
                     7G5?~~^^^^^:::?~?!!!^^!~^^~J^Y7~YJJJGG~JYYYJGG7PGPB:                           
                     .7YY?!~~7!^^:^?7J~?7!!5?~~~J~7J75JJJPG??Y55PPJYGPG5                            
                      !!?YY7~!7^^^~?^?!??JJJJ5?~77!J~5JJJYB#Y?J5YYG#GP?.                            
                      Y7!!?YY~~~~~!J~?7?!YJ??57^7J!J~YYJJYYPB#BBBBBBPP.                             
                      !?~7!!YY?!7JJY!7?J??!5Y!7~?7!Y?5PYJJY5P5555Y5PP~                              
                       J5Y?77?YJJ?7Y~77J~~~7!^^~7J7?~YY55Y5P5Y55YYJJ~                               
                       .JGGPJJ?!77!J?77J!~~~^^^~!Y7Y7?7??YYPPPP5Y!:.                                
                         :^:^~~7^^^777?!?77777??J!YJ!J7J7~!7!~..                                    
                                   .5P?7?J55555YJJYYY: .                                            
                                  :G#5Y5GGBGGBYJJJJJG:                                              
                                 .G#GB###B5Y5BBBBGGB#5                                              
                                 5BGGPGGGGBBBBPJJ?JY5G?                                             
                                !#J7???77?5BBGYJJJYYJ5#J                                            
                               !#BPYJJYJ?JYPPPGGGGBBB###5.                                          
                              ~#G5PPGGGGBBGYJJJGBG5??JY5BG7                                         
                             :BBG555G#BBBBGPGGGGBGY?J??7?5#J                                        
                            .?YJ???7!!77??~^^^~~7JJ77!77?JY5:                                       
                                                                                                    
                                                                                                    ''')
    print("")

def rodada():
    print("")
    print('''                     _                                 _           _       
                    (_)                               | |         | |      
 _ __  _ __ _____  ___ _ __ ___   __ _   _ __ ___   __| | __ _  __| | __ _ 
| '_ \| '__/ _ \ \/ / | '_ ` _ \ / _` | | '__/ _ \ / _` |/ _` |/ _` |/ _` |
| |_) | | | (_) >  <| | | | | | | (_| | | | | (_) | (_| | (_| | (_| | (_| |
| .__/|_|  \___/_/\_\_|_| |_| |_|\__,_| |_|  \___/ \__,_|\__,_|\__,_|\__,_|
| |                                                                        
|_|                                                                        ''')
    print


querjogar = 0
while querjogar == 0:
    # as variáveis de entrada 
    escolha_prog_volta = 0
    oxigenio = 50
    tesouros = []
    nome = inicio()
    player_position = 1
    # enquanto o oxigênio é maior que 0, o programa principal roda, se não ele para
    
    while oxigenio>0 and player_position>0 and player_position<=32:
        # continua pedindo para o jogador respirar até ele parar de ser cabeça-dura e só apertar enter
        while oxigenio == 50:
            print("")
            print("")
            pressione = input("Pressione ENTER para respirar: ")
            if pressione == "":
                oxigenio = 25
        
        # se você escolher um nome, o jogo se refere a você usando ele
        if nome != "n" and nome!="N" and nome!="":
            print("")
            rodada()
            print("")
            print(f"Olá {nome}, seja bem-vindo a próxima rodada")
            print("")
        else:
            print("")
            rodada()
            print("")
            print("Iniciando uma próxima rodada. ")


        # O programa continua validando sua entrada até você escolher uma das opções da maneira correta
        while escolha_prog_volta == 0:
            print("")
            print_slow("Você pretende progredir ou retorceder? Pressione [P] para PROGREDIR AO FUNDO DO MAR ou [V] para começar sua VOLTA AO SUBMARINO")
            print("")
            input_progressão_jogador = input("")
            if input_progressão_jogador == "P" or input_progressão_jogador == "p" or input_progressão_jogador == "v" or input_progressão_jogador == "V":
                escolha_prog_volta = 1
            if (input_progressão_jogador == "v" or input_progressão_jogador == "V") and len(tesouros)==0:
                print("")
                print_slow("não há como retornar sem tesouros, pressione [P], não tenha medo...")
                input_progressão_jogador = ""
                escolha_prog_volta = 0

        # se o jogador escolhe progredir, ele roda o dado e decide avançar, 
        if input_progressão_jogador == "p" or input_progressão_jogador == "P":
            player_position += roda_dado()
            if player_position<=32:
                posição(player_position)
                oxigenio = calcula_oxigenio(tesouros,oxigenio)
                print("")
                tesouros = rodar_tesouros(tesouros, player_position)
                escolha_prog_volta = 0
            else: 
                print("")
                se_perdeu()
                print("")
                oxigenio = -25
    
            


        # o jogador não pode retornar ao submarino sem possuir pelo menos algum tesouro
        elif (input_progressão_jogador == "v" or input_progressão_jogador == "V") and len(tesouros)==0:
            print("")
            print("Você não pode voltar sem tesouros, pare de ter medo")
            escolha_prog_volta = 0
        
        

        # se o jogador optar por voltar, ele não tem como progredir novamente
        while input_progressão_jogador == "v" or input_progressão_jogador == "V" and player_position>0:
            if player_position<=0 and len(tesouros) == 0:
                print("")

                ("Você não pode retornar ao submarino sem tesouros")
            else:
                player_position -= roda_dado()
            posição(player_position)
            oxigenio = calcula_oxigenio(tesouros,oxigenio)
            tesouros = rodar_tesouros(tesouros, player_position)
            # essa condição quebra o ciclo do while se o jogador retornar ao submarino e ainda possuir oxigênio, o -100 é um número arbitrário que também quebra o while do oxigênio
            if player_position<=0:
                input_progressão_jogador = ""
                oxigenio = -100
        


    # o número da condição que quebra o while do oxigênio dentro do while do VOLTA AO SUBMARINO (linha 377) também serve para reconhecer se o jogador conseguiu retornar ao submarino sem morrer, e com tesouros
    if oxigenio == -100:
        print("")
        print_slow('''                                                                                       .---.    .-' '-.               .-' '-.     
                                        _______                                        |   |   '   _    \            '   _    \   
          .--. __  __   ___             \  ___ `'.         __.....__                   '---' /   /` '.   \         /   /` '.   \  
     _.._ |__||  |/  `.'   `.            ' |--.\  \    .-''         '.                 .---..   |     \  '  .--./).   |     \  '  
   .' .._|.--.|   .-.  .-.   '           | |    \  '  /     .-''"'-.  `.               |   ||   '      |  '/.''\\ |   '      |  ' 
   | '    |  ||  |  |  |  |  |           | |     |  '/     /________\   \              |   |\    \     / /| |  | |\    \     / /  
 __| |__  |  ||  |  |  |  |  |           | |     |  ||                  |              |   | `.   ` ..' /  \`-' /  `.   ` ..' /   
|__   __| |  ||  |  |  |  |  |           | |     ' .'\    .-------------'              |   |    '-...-'`   /("'`      '-...-'`    
   | |    |  ||  |  |  |  |  |           | |___.' /'  \    '-.____...---.              |   |               \ '---.                
   | |    |__||__|  |__|  |__|          /_______.'/    `.             .'               |   |                /'""'.\               
   | |                                  \_______|/       `''-...... -'              __.'   '               ||     ||              
   | |                                                                             |      '                \'. __//               
   |_|                                                                             |____.'                  `'---'                ''')
        print("")
        print_slow("Parabéns! Você terminou o jogo ainda vivo, e trouxe consigo um belo cachê")
        print("")
        print_slow(f"Seus tesouros: {sum(tesouros)}")
    else:
        print("")
        print("")
        cacodemon()
        print("")

    i = 0
    while i == 0:
        print("")
        print("")
        logo()
        print("")
        print_slow("Você gostaria de jogar novamente? Pressione [S] para SIM e [N] para NÃO")
        print("")
        querjogar = input("")
        if querjogar == "S" or querjogar == "s":
            querjogar = 0
            i = 1
        elif querjogar == "n" or querjogar == "N":
            querjogar = 1
            i = 1
        else:
            print_slow("Digite apenas a letra [S] ou [N], por favor")
            print("")
            print("")


