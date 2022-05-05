from cgitb import text
import pygame
import constantes

pygame.font.init()
fontP = pygame.font.get_default_font()
fontE = pygame.font.match_font('Verdana',0,1)
fontI = pygame.font.SysFont(fontP,45)
fontMenor = pygame.font.SysFont(fontP,25)
fonteTextoE = pygame.font.SysFont(fontE,30)
#ret = pygame.Rect(200,40,200,80)

screen = pygame.display.set_mode((0,0))

texto = fontI.render('Bem-vindo ao InterPY',32,constantes.cWhite,)
texto2 = fontMenor.render('Pressione qualquer tecla para começar a jogar',32,constantes.cWhite)
#INSTRUÇÕES
textoReal = fonteTextoE.render('InterPY é um jogo que consiste em você(jogador) ser um agente da interpol, o qual é contratado por uma',32,constantes.cWhite)
screen.blit(textoReal,(140,250))
pygame.display.flip()
textoReal = fonteTextoE.render('agência estrangeira e você deve passar as características dos indivíduos suspeitos, para seu superior que apenas entende',32,constantes.cWhite)
screen.blit(textoReal,(70,280))
pygame.display.flip()
textoReal = fonteTextoE.render('a lingua inglesa. Mas não se preocupe,o jogo estará lhes fornecendo dicas constantemente para formular frases',32,constantes.cWhite)
screen.blit(textoReal,(140,310))
pygame.display.flip()
textoReal = fonteTextoE.render('A medida em que o jogador vai avançando de nível, novos desafios vão surgindo e será necessário se reinventar.',32,constantes.cWhite)
screen.blit(textoReal,(70,340))
pygame.display.flip()
textoReal = fonteTextoE.render('para continuar avançando.',32,constantes.cWhite)
screen.blit(textoReal,(500,370))
pygame.display.flip()

#Bem-vindo
screen.blit(texto,(500,100))
pygame.display.flip()
#Pressione
screen.blit(texto2,(500,700))
pygame.display.flip()
pygame.display.flip()


esperando = True
while esperando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esperando = False
        if event.type == pygame.KEYUP:
            esperando = False


pygame.init()
#x = 1280
#y = 720


pygame.display.set_caption('Investigation')

rodando = True
while rodando:

    pygame.time.delay(40)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    criminoso = pygame.image.load('i1_jogo_720p.png')
    screen.blit(criminoso,(0,0))
    
    pygame.display.update()

pygame.quit