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

img_hotel    = pygame.image.load(f"hotel1estrela.png")
img_hotel    = pygame.transform.scale(img_hotel, (1380, 324))

img_recepcao = pygame.image.load(f"recepcao1estrela.png")
img_recepcao = pygame.transform.scale(img_recepcao, (685, 330))

img_restaurante = pygame.image.load(f"restaurante1estrela.png")
img_restaurante = pygame.transform.scale(img_restaurante, (685, 330))

img_quarto   = pygame.image.load(f"quarto1estrela.png")
img_quarto   = pygame.transform.scale(img_quarto, (685, 330))

lvlhotel = 1

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
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if btn_upghotel.collidepoint(mouse):
                lvlhotel += 2
                img_hotel = pygame.image.load("hotel" + str(lvlhotel) + "estrela.png")
                img_hotel = pygame.transform.scale(img_hotel, (1380, 324))

                img_recepcao = pygame.image.load("recepcao" + str(lvlhotel) + "estrela.png")
                img_recepcao = pygame.transform.scale(img_recepcao, (685, 330))

                img_restaurante = pygame.image.load("restaurante" + str(lvlhotel) + "estrela.png")
                img_restaurante = pygame.transform.scale(img_restaurante, (685, 330))

                img_quarto = pygame.image.load("quarto" + str(lvlhotel) + "estrela.png")
                img_quarto = pygame.transform.scale(img_quarto, (685, 330))

    tela.fill((40, 40, 40))
    #tela principal com imagem do hotel
    pygame.draw.rect(tela, (0, 51, 102), (10, 10, 1380, 330), border_radius=12)
    tela.blit(img_hotel, (10, 13), )
    pygame.draw.rect(tela, (50, 130, 230), (10, 10, 1380, 330), 3, border_radius=12)
    #tela de cadastros
    pygame.draw.rect(tela, (0, 51, 102), (10, 350, 685, 330), border_radius=12)
    tela.blit(img_recepcao, (10, 350), )
    tela.blit(filtro, (10, 350))
    pygame.draw.rect(tela, (50, 130, 230), (10, 350, 685, 330), 3, border_radius=12)
    #tela de consumos
    pygame.draw.rect(tela, (0, 51, 102), (705,350, 685, 330), border_radius=12)
    tela.blit(img_restaurante, (705, 350), )
    tela.blit(filtro, (705, 350))
    pygame.draw.rect(tela, (50, 130, 230), (705,350, 685, 330), 3, border_radius=12)
    #tela de upgrades
    pygame.draw.rect(tela, (0, 51, 102), (10, 690, 685, 330), border_radius=12)
    pygame.draw.rect(tela, (50, 130, 230), (10, 690, 685, 330), 3, border_radius=12)
    #tela de quartos
    pygame.draw.rect(tela, (0, 51, 102), (705,690, 685, 330), border_radius=12)
    tela.blit(img_quarto, (705, 690))
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
    nh1 = fonte_mediabold.render(str(lvlhotel), True, (0, 51, 102))
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

    #boato de upgrade do quarto
    preco_upgquarto = 100.00
    btn_upgquarto = pygame.Rect(400, 760, 180, 50)
    cor1 = (80, 160, 255) if btn_upgquarto.collidepoint(mouse) else (50, 130, 230)
    pygame.draw.rect(tela, cor1, btn_upgquarto, border_radius=10)
    s1 = fonte_pequena.render(f"{preco_upgquarto} R$", True, (255, 255, 255))
    tela.blit(s1, (btn_upgquarto.x + (btn_upgquarto.width - s1.get_width()) // 2,
                   btn_upgquarto.y + (btn_upgquarto.height - s1.get_height()) // 2))

    #botao de comprar mais um quarto
    preco_morequarto = 300.00
    btn_morequarto = pygame.Rect(400, 840, 180, 50)
    cor1 = (80, 160, 255) if btn_morequarto.collidepoint(mouse) else (50, 130, 230)
    pygame.draw.rect(tela, cor1, btn_morequarto, border_radius=10)
    s1 = fonte_pequena.render(f"{preco_morequarto} R$", True, (255, 255, 255))
    tela.blit(s1, (btn_morequarto.x + (btn_morequarto.width - s1.get_width()) // 2,
                   btn_morequarto.y + (btn_morequarto.height - s1.get_height()) // 2))
    #melhorar hotel
    preco_upghotel = 5000.00
    btn_upghotel = pygame.Rect(400, 920, 180, 50)
    cor1 = (80, 160, 255) if btn_upghotel.collidepoint(mouse) else (50, 130, 230)
    pygame.draw.rect(tela, cor1, btn_upghotel, border_radius=10)
    s1 = fonte_pequena.render(f"{preco_upghotel} R$", True, (255, 255, 255))
    tela.blit(s1, (btn_upghotel.x + (btn_upghotel.width - s1.get_width()) // 2,
                   btn_upghotel.y + (btn_upghotel.height - s1.get_height()) // 2))


    pygame.display.flip()
    relogio.tick(60)