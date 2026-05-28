import pygame
import sys

pygame.init()
tela = pygame.display.set_mode((1400, 1020))
pygame.display.set_caption("Hotel Incremental")

relogio = pygame.time.Clock()

fonte_grandebold = pygame.font.SysFont("segoeui", 48, bold=True)
fonte_media  = pygame.font.SysFont("segoeui", 28)
fonte_mediabold  = pygame.font.SysFont("segoeui", 28, bold=True)
fonte_pequena= pygame.font.SysFont("segoeui", 18)
fonte_pequenabold= pygame.font.SysFont("segoeui", 18, bold=True)
filtro = pygame.Surface((685, 330))
filtro.set_alpha(180)
filtro.fill((160, 160, 160))

while True:
    mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if btn_upgquarto.collidepoint(mouse):
                    print("✔ Check-in confirmado!")

    tela.fill((40, 40, 40))
    #tela principal com imagem do hotel
    pygame.draw.rect(tela, (0, 51, 102), (10, 10, 1380, 330), border_radius=12)
    imagemhotel = pygame.image.load("hotel5estrela.png")
    imagemhotel = pygame.transform.scale(imagemhotel, (1380, 324))
    tela.blit(imagemhotel, (10, 13), )
    pygame.draw.rect(tela, (50, 130, 230), (10, 10, 1380, 330), 3, border_radius=12)
    #tela de cadastros
    pygame.draw.rect(tela, (0, 51, 102), (10, 350, 685, 330), border_radius=12)
    imagemhotel = pygame.image.load("recepcao5estrela.png")
    imagemhotel = pygame.transform.scale(imagemhotel, (685, 330))
    tela.blit(imagemhotel, (10, 350), )
    tela.blit(filtro, (10, 350))
    pygame.draw.rect(tela, (50, 130, 230), (10, 350, 685, 330), 3, border_radius=12)
    #tela de consumos
    pygame.draw.rect(tela, (0, 51, 102), (705,350, 685, 330), border_radius=12)
    imagemhotel = pygame.image.load("restaurante5estrela.png")
    imagemhotel = pygame.transform.scale(imagemhotel, (685, 330))
    tela.blit(imagemhotel, (705, 350), )
    tela.blit(filtro, (705, 350))
    pygame.draw.rect(tela, (50, 130, 230), (705,350, 685, 330), 3, border_radius=12)
    #tela de upgrades
    pygame.draw.rect(tela, (0, 51, 102), (10, 690, 685, 330), border_radius=12)
    pygame.draw.rect(tela, (50, 130, 230), (10, 690, 685, 330), 3, border_radius=12)
    #tela de quartos
    pygame.draw.rect(tela, (0, 51, 102), (705,690, 685, 330), border_radius=12)
    imagemhotel = pygame.image.load("quarto5estrela.png")
    imagemhotel = pygame.transform.scale(imagemhotel, (685, 330))
    tela.blit(imagemhotel, (705, 690))
    tela.blit(filtro, (705, 690))

    pygame.draw.rect(tela, (50, 130, 230), (705, 690, 685, 330), 3, border_radius=12)

    #tela de horario
    pygame.draw.rect(tela, (255, 255, 255), (13, 13, 150, 80), border_radius=12)
    pygame.draw.rect(tela, (0, 0, 0), (13, 13, 150, 80), 3, border_radius=12)
    #tela de nivel do hotel
    pygame.draw.rect(tela, (255, 255, 255), (1237, 13, 150, 80), border_radius=12)
    pygame.draw.rect(tela, (0, 0, 0), (1237, 13, 150, 80), 3, border_radius=12)

    h1 = fonte_pequenabold.render("Nível do hotel:", True, (0, 51, 102))
    tela.blit(h1, (1250, 17))
    lvlhotel = "5"
    nh1 = fonte_mediabold.render(lvlhotel, True, (0, 51, 102))
    tela.blit(nh1, (1305, 45))
    c1 = fonte_mediabold.render("Check-In", True, (0, 51, 102))
    xc1 = (700 - c1.get_width()) // 2
    tela.blit(c1,(xc1,360 ))
    co1 = fonte_mediabold.render("Consumos", True, (0, 51, 102))
    xco1 = (2100 - co1.get_width()) // 2
    tela.blit(co1, (xco1, 360))
    u1 = fonte_mediabold.render("Upgrades", True, (50, 130, 230))
    xu1 = (700 - u1.get_width()) // 2
    tela.blit(u1, (xc1, 700))
    q1 = fonte_mediabold.render("Quartos", True, (0, 51, 102))
    xq1 = (2100 - q1.get_width()) // 2
    tela.blit(q1, (xco1, 700))

    btn_upgquarto = pygame.Rect(100, 150, 180, 50)
    cor1 = (80, 160, 255) if btn_upgquarto.collidepoint(mouse) else (50, 130, 230)
    pygame.draw.rect(tela, cor1, btn_upgquarto, border_radius=10)
    s1 = fonte_pequena.render("✔ Check-in", True, (255, 255, 255))
    tela.blit(s1, (btn_upgquarto.x + (btn_upgquarto.width - s1.get_width()) // 2,
                   btn_upgquarto.y + (btn_upgquarto.height - s1.get_height()) // 2))

    pygame.display.flip()
    relogio.tick(60)