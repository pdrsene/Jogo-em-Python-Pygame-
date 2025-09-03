import pygame #blibioteca de criação de jogos
import random #blibioteca para funcoes de aleatoriedade

pygame.init()

largura, altura = 400, 600
tela = pygame.display.set_mode((largura, altura)) #tamanho da tela
clock = pygame.time.Clock() #fps

# jogador
jogador = pygame.Rect(180, 500, 40, 40)
velocidade = 5

# obstaculos
obstaculos = []

def criar_obstaculo():
    x = random.randint(0, largura - 40)
    return pygame.Rect(x, -40, 40, 40)

rodando = True

while rodando: #funcao looping, dentro do parenteses a cor
    tela.fill((40, 40, 40))  # limpa a tela
    
    teclas = pygame.key.get_pressed()#contar cada tecla pressionada

    for evento in pygame.event.get():#definir X para finalizar o jogo
        if evento.type == pygame.QUIT:
            rodando = False

    if teclas[pygame.K_LEFT] and jogador.left > 0:#limitador o jogador sempre dentro da tela
        jogador.x -= velocidade

    if teclas[pygame.K_RIGHT] and jogador.right < largura:#limitador o jogador sempre dentro da tela
        jogador.x += velocidade

    if random.randint(1, 30) == 1:
        obstaculos.append(criar_obstaculo())

    for obstaculo in obstaculos:
        obstaculo.y += 5
        if obstaculo.colliderect(jogador):
            rodando = False
        pygame.draw.rect(tela, (255, 0, 0), obstaculo)  # desenhar obstaculo

    obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo.y < altura]

    pygame.draw.rect(tela, (0, 255, 0), jogador)  # desenhar jogador

    pygame.display.flip()
    clock.tick(60) #fps definido

pygame.quit()

