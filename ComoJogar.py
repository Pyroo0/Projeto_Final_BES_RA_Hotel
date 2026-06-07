import pygame

def exibir_tutorial(tela, fonte_mediabold, fonte_pequenabold, fonte_pequena, fonte_tiny, mouse):
    largura_janela, altura_janela = 800, 580
    jx = (tela.get_width() - largura_janela) // 2
    jy = (tela.get_height() - altura_janela) // 2

    filtro = pygame.Surface((tela.get_width(), tela.get_height()))
    filtro.set_alpha(150)
    filtro.fill((20, 20, 20))
    tela.blit(filtro, (0, 0))

    pygame.draw.rect(tela, (245, 247, 250), (jx, jy, largura_janela, altura_janela), border_radius=14)
    pygame.draw.rect(tela, (0, 51, 102), (jx, jy, largura_janela, altura_janela), 4, border_radius=14)

    pygame.draw.rect(tela, (0, 51, 102), (jx, jy, largura_janela, 60), border_radius=12)
    tit = fonte_mediabold.render("COMO JOGAR - HOTEL INCREMENTAL", True, (255, 255, 255))
    tela.blit(tit, (jx + (largura_janela - tit.get_width()) // 2, jy + 14))

    if not hasattr(exibir_tutorial, "aba_atual"):
        exibir_tutorial.aba_atual = 0

    abas = ["1. Objetivo", "2. Check-In", "3. Consumos", "4. Upgrades"]
    btn_abas = []

    largura_aba = 150
    espacamento = 15
    inicio_x = jx + (largura_janela - (largura_aba * 4 + espacamento * 3)) // 2

    for i, nome_aba in enumerate(abas):
        bx = inicio_x + i * (largura_aba + espacamento)
        by = jy + 80
        rect_aba = pygame.Rect(bx, by, largura_aba, 35)
        btn_abas.append(rect_aba)

        if exibir_tutorial.aba_atual == i:
            cor_fundo = (50, 130, 230)
            cor_texto = (255, 255, 255)
        elif rect_aba.collidepoint(mouse):
            cor_fundo = (180, 210, 255)
            cor_texto = (0, 30, 80)
        else:
            cor_fundo = (210, 220, 235)
            cor_texto = (50, 50, 80)

        pygame.draw.rect(tela, cor_fundo, rect_aba, border_radius=6)
        pygame.draw.rect(tela, (100, 140, 200), rect_aba, 1, border_radius=6)
        txt_aba = fonte_tiny.render(nome_aba, True, cor_texto)
        tela.blit(txt_aba, (rect_aba.x + (rect_aba.width - txt_aba.get_width()) // 2, rect_aba.y + 8))

    pygame.draw.rect(tela, (255, 255, 255), (jx + 30, jy + 135, largura_janela - 60, 350), border_radius=10)
    pygame.draw.rect(tela, (200, 210, 225), (jx + 30, jy + 135, largura_janela - 60, 350), 1, border_radius=10)

    linhas_texto = []
    if exibir_tutorial.aba_atual == 0:
        linhas_texto = [
            ("BEM-VINDO AO SEU NOVO EMPREENDIMENTO!", fonte_pequenabold, (0, 51, 102)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Seu objetivo é gerenciar e expandir o Hotel Incremental, transformando", fonte_pequena, (40, 40, 40)),
            ("uma pequena hospedagem de 1 estrela em um resort de luxo de 3 estrelas.", fonte_pequena, (40, 40, 40)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Para crescer, você precisará administrar o fluxo de caixa baseado em:", fonte_pequena, (40, 40, 40)),
            ("  * Hospedar clientes vindos da fila de espera.", fonte_pequena, (0, 102, 204)),
            ("  * Atender pedidos de serviço de quarto no painel de consumos.", fonte_pequena, (0, 102, 204)),
            ("  * Reinvestir o lucro acumulado em melhorias de quartos e expansão.", fonte_pequena, (0, 102, 204)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Fique atento ao relógio do jogo no topo esquerdo. O tempo não para!", fonte_pequenabold, (180, 50, 50))
        ]
    elif exibir_tutorial.aba_atual == 1:
        linhas_texto = [
            ("COMO HOSPEDAR NOVOS CLIENTES:", fonte_pequenabold, (0, 51, 102)),
            ("", fonte_pequena, (0, 0, 0)),
            ("1. No painel Recepção, novos hóspedes surgem na 'Fila de hóspedes'.", fonte_pequena, (40, 40, 40)),
            ("2. Clique no nome do hóspede desejado para selecioná-lo.", fonte_pequena, (40, 40, 40)),
            ("3. Escolha um quarto com o status 'LIVRE' (botões azuis na recepção).", fonte_pequena, (40, 40, 40)),
            ("4. Clique no botão verde 'Confirmar Check-In' para concluir.", fonte_pequena, (40, 40, 40)),
            ("", fonte_pequena, (0, 0, 0)),
            ("O quarto ficará ocupado (vermelho) no painel de Quartos à direita.", fonte_pequena, (40, 40, 40)),
            ("A cada 6 segundos de jogo, os quartos ocupados geram lucro automático.", fonte_pequena, (0, 120, 50)),
            ("Quando o cronômetro do quarto zera, o hóspede sai automaticamente.", fonte_pequena, (40, 40, 40))
        ]
    elif exibir_tutorial.aba_atual == 2:
        linhas_texto = [
            ("SERVIÇO DE QUARTO E FATURAMENTO EXTRA:", fonte_pequenabold, (0, 51, 102)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Enquanto estão hospedados, os clientes fazem pedidos na aba 'Consumos'.", fonte_pequena, (40, 40, 40)),
            ("A lista suporta no máximo 6 pedidos simultâneos no hotel.", fonte_pequena, (40, 40, 40)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Para faturar:", fonte_pequenabold, (40, 40, 40)),
            ("1. Clique no pedido dentro da lista para inspecionar os detalhes.", fonte_pequena, (40, 40, 40)),
            ("2. Veja o nome do hóspede, número do quarto e preço do produto.", fonte_pequena, (40, 40, 40)),
            ("3. Clique no botão verde 'Registrar Consumo' para coletar o dinheiro.", fonte_pequena, (40, 40, 40)),
            ("", fonte_pequena, (0, 0, 0)),
            ("ATENÇÃO: Se a estadia do hóspede acabar e ele for embora do hotel,", fonte_pequenabold, (180, 50, 50)),
            ("o pedido dele sumirá da lista e você perderá essa receita!", fonte_pequenabold, (180, 50, 50))
        ]
    elif exibir_tutorial.aba_atual == 3:
        linhas_texto = [
            ("EVOLUINDO SEU PATRIMÔNIO:", fonte_pequenabold, (0, 51, 102)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Gerencie suas estratégias através do painel de Upgrades:", fonte_pequena, (40, 40, 40)),
            ("", fonte_pequena, (0, 0, 0)),
            ("* Upg. Quarto: Aumenta o valor das diárias em +20% por nível (Máx. 10).", fonte_pequena, (40, 40, 40)),
            ("* +1 Quarto: Desbloqueia novas acomodações que estão bloqueadas.", fonte_pequena, (40, 40, 40)),
            ("* Upg. Hotel: Redefine sua estrutura para o próximo nível visual.", fonte_pequena, (40, 40, 40)),
            ("", fonte_pequena, (0, 0, 0)),
            ("Ao evoluir o Hotel, a receita base salta drasticamente e o número máximo", fonte_pequena, (0, 51, 102)),
            ("de quartos expande (permitindo até 10 quartos no nível final do resort).", fonte_pequena, (0, 51, 102))
        ]

    pos_y = jy + 155
    for texto, fonte, cor in linhas_texto:
        surf_linha = fonte.render(texto, True, cor)
        tela.blit(surf_linha, (jx + 50, pos_y))
        pos_y += 26

    btn_fechar = pygame.Rect(jx + (largura_janela - 180) // 2, jy + 505, 180, 45)
    cor_fechar = (210, 50, 50) if btn_fechar.collidepoint(mouse) else (170, 30, 30)
    pygame.draw.rect(tela, cor_fechar, btn_fechar, border_radius=10)
    pygame.draw.rect(tela, (255, 255, 255), btn_fechar, 1, border_radius=10)

    txt_fechar = fonte_pequenabold.render("Entendido!", True, (255, 255, 255))
    tela.blit(txt_fechar, (btn_fechar.x + (btn_fechar.width - txt_fechar.get_width()) // 2, btn_fechar.y + 11))

    if pygame.mouse.get_pressed()[0]:
        for i, rect_aba in enumerate(btn_abas):
            if rect_aba.collidepoint(mouse):
                exibir_tutorial.aba_atual = i
        if btn_fechar.collidepoint(mouse):
            return False

    return True