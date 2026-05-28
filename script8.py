import pygame, sys
pygame.init()

tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Botões")
relogio = pygame.time.Clock()

fonte = pygame.font.SysFont("segoeui", 20, bold=True)

# Define os botões
btn_checkin = pygame.Rect(100, 150, 180, 50)
btn_consumo = pygame.Rect(320, 150, 180, 50)

while True:
    mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if btn_checkin.collidepoint(mouse):
                    print("✔ Check-in confirmado!")
                if btn_consumo.collidepoint(mouse):
                    print("🍽 Consumo confirmado!")

    tela.fill((30, 30, 30))

    # Botão 1
    cor1 = (80, 160, 255) if btn_checkin.collidepoint(mouse) else (50, 130, 230)
    pygame.draw.rect(tela, cor1, btn_checkin, border_radius=10)
    s1 = fonte.render("✔ Check-in", True, (255, 255, 255))
    tela.blit(s1, (btn_checkin.x + (btn_checkin.width - s1.get_width()) // 2,
                   btn_checkin.y + (btn_checkin.height - s1.get_height()) // 2))

    # Botão 2
    cor2 = (100, 210, 150) if btn_consumo.collidepoint(mouse) else (60, 180, 120)
    pygame.draw.rect(tela, cor2, btn_consumo, border_radius=10)
    s2 = fonte.render("🍽 Consumo", True, (255, 255, 255))
    tela.blit(s2, (btn_consumo.x + (btn_consumo.width - s2.get_width()) // 2,
                   btn_consumo.y + (btn_consumo.height - s2.get_height()) // 2))

    pygame.display.flip()
    relogio.tick(60)