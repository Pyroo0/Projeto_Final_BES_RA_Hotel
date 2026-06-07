import pygame
import sys
import random
import datetime
import ComoJogar

pygame.init()
tela = pygame.display.set_mode((1400, 1020))
pygame.display.set_caption("Hotel Incremental")

relogio = pygame.time.Clock()
mouse = pygame.mouse.get_pos()

fonte_media = pygame.font.SysFont("segoeui", 28)
fonte_mediabold = pygame.font.SysFont("segoeui", 28, bold=True)
fonte_pequena = pygame.font.SysFont("segoeui", 18)
fonte_pequenabold = pygame.font.SysFont("segoeui", 18, bold=True)
fonte_tiny = pygame.font.SysFont("segoeui", 14)
fonte_tinybold = pygame.font.SysFont("segoeui", 14, bold=True)

filtro = pygame.Surface((685, 330))
filtro.set_alpha(180)
filtro.fill((160, 160, 160))

btn_upgquarto = pygame.Rect(250, 760, 200, 50)
btn_morequarto = pygame.Rect(250, 840, 200, 50)
btn_upghotel = pygame.Rect(250, 920, 200, 50)
btn_ajuda = pygame.Rect(1340, 25, 40, 40)

img_hotel = pygame.transform.scale(pygame.image.load("hotel1estrela.png"), (1380, 324))
img_recepcao = pygame.transform.scale(pygame.image.load("recepcao1estrela.png"), (685, 330))
img_restaurante = pygame.transform.scale(pygame.image.load("restaurante1estrela.png"), (685, 330))
img_quarto = pygame.transform.scale(pygame.image.load("quarto1estrela.png"), (685, 330))

lvlhotel = 1
lvlhoteldisplay = 1

mostrar_aviso = False
mensagem_aviso = ""
mostrar_tutorial = True

NIVEL_CONFIG = {
    1: {"preco_hotel": 3_000, "preco_upgq": 100, "preco_moreq": 300, "receita": 10, "max_upg": 10},
    2: {"preco_hotel": 10_000, "preco_upgq": 400, "preco_moreq": 800, "receita": 30, "max_upg": 10},
    3: {"preco_hotel": 15_000, "preco_upgq": 1_200, "preco_moreq": 2_000, "receita": 80, "max_upg": 10},
    }

def cfg():
    return NIVEL_CONFIG[lvlhoteldisplay]


dinheiro = 0.00
MS_POR_MINUTO_JOGO = 6000
acumulador_receita = 0

MS_POR_HORA_JOGO = 2000
hora_jogo = 8
dia_jogo = 1
acumulador_horario = 0

upgrades_quarto = 0

NOMES = [
    "Ana Silva", "Bruno Costa", "Carla Dias", "Diego Melo", "Elisa Ramos",
    "Felipe Nunes", "Gabriela Sá", "Henrique Luz", "Isabela Forte", "João Pedro",
    "Karen Lima", "Lucas Souza", "Marina Faro", "Nicolas Pais", "Olivia Braga",
    "Paulo Teixeira", "Quintina Ávila", "Rafael Torres", "Sofia Cunha", "Thiago Rego",
    "Ursula Viana", "Victor Hugo", "Wendy Sales", "Xerxes Leal", "Yasmin Brito",
]

acumulador_hospede = 0
MS_ENTRE_HOSPEDES = random.randint(12000, 20000)
MAX_FILA_HOSPEDES = 6

fila_hospedes = []
hospede_selecionado = None
quarto_selecionado = None

quartos = [
    {"id": 1, "status": "livre", "hospede": None, "tempo_saida": 0},
    {"id": 2, "status": "livre", "hospede": None, "tempo_saida": 0},
    {"id": 3, "status": "bloqueado", "hospede": None, "tempo_saida": 0},
    {"id": 4, "status": "bloqueado", "hospede": None, "tempo_saida": 0},
]
quartos2 = [{"id": i + 1, "status": "livre" if i < 4 else "bloqueado", "hospede": None, "tempo_saida": 0} for i in
            range(7)]
quartos3 = [{"id": i + 1, "status": "livre" if i < 7 else "bloqueado", "hospede": None, "tempo_saida": 0} for i in
            range(10)]

ITENS_CONSUMO = [
    {"item": "Água Mineral", "preco": 6.00},
    {"item": "Refrigerante", "preco": 8.00},
    {"item": "Café Express", "preco": 7.00},
    {"item": "Sanduíche", "preco": 18.00},
    {"item": "Batata Frita", "preco": 15.00},
    {"item": "Suco Natural", "preco": 10.00},
    {"item": "Sobremesa", "preco": 14.00}
]

lista_consumos = []
consumo_selecionado = None
acumulador_consumo = 0
MS_ENTRE_CONSUMOS = random.randint(8000, 12000)
MAX_LISTA_CONSUMOS = 6


def todos_desbloqueados(lista):
    return all(q["status"] != "bloqueado" for q in lista)

def contar_ocupados(lista):
    return sum(1 for q in lista if q["status"] == "ocupado")

def quartos_livres(lista):
    return [q for q in lista if q["status"] == "livre"]

def atualizar_saidas():
    global consumo_selecionado
    agora = pygame.time.get_ticks()
    for q in quartos:
        if q["status"] == "ocupado" and q["tempo_saida"] > 0:
            if agora >= q["tempo_saida"]:
                for c in lista_consumos[:]:
                    if c["quarto_id"] == q["id"] and c["hospede"] == q["hospede"]:
                        if consumo_selecionado == c:
                            consumo_selecionado = None
                        lista_consumos.remove(c)
                q["status"] = "livre"
                q["hospede"] = None
                q["tempo_saida"] = 0

def fazer_checkin(nome, quarto):
    duracao_ms = random.randint(30000, 90000)
    quarto["status"] = "ocupado"
    quarto["hospede"] = nome
    quarto["tempo_saida"] = pygame.time.get_ticks() + duracao_ms

def desenhar_checkin(mouse):
    pygame.draw.line(tela, (80, 120, 180), (360, 410), (360, 668), 1)

    s = fonte_pequenabold.render("Fila de hóspedes:", True, (0, 51, 102))
    tela.blit(s, (28, 378))

    if not fila_hospedes:
        s = fonte_pequena.render("Nenhum hóspede aguardando", True, (64, 64, 64))
        tela.blit(s, (28, 408))
    else:
        for i, nome in enumerate(fila_hospedes):
            card = pygame.Rect(28, 405 + i * 40, 318, 34)
            selecionado = (hospede_selecionado == nome)
            if selecionado:
                cor_card = (50, 130, 230)
                cor_txt = (255, 255, 255)
            elif card.collidepoint(mouse):
                cor_card = (180, 210, 255)
                cor_txt = (0, 30, 80)
            else:
                cor_card = (220, 230, 245)
                cor_txt = (20, 20, 60)
            pygame.draw.rect(tela, cor_card, card, border_radius=8)
            pygame.draw.rect(tela, (100, 140, 200), card, 1, border_radius=8)
            ns = fonte_pequena.render(nome, True, cor_txt)
            tela.blit(ns, (card.x + 10, card.y + (card.height - ns.get_height()) // 2))

    rx = 372

    if hospede_selecionado is None:
        hint = fonte_pequena.render("Selecione um hóspede", True, (64, 64, 64))
        tela.blit(hint, (rx, 410))
        return None

    nome_label = fonte_pequenabold.render(f"Hóspede: {hospede_selecionado}", True, (0, 51, 102))
    tela.blit(nome_label, (rx, 378))

    dica = fonte_pequenabold.render("Escolha o quarto livre:", True, (0, 51, 102))
    tela.blit(dica, (rx, 415))

    livres = quartos_livres(quartos)
    if not livres:
        s = fonte_pequena.render("Nenhum quarto livre!", True, (180, 60, 60))
        tela.blit(s, (rx, 445))
    else:
        cols_q = 4
        for i, q in enumerate(livres):
            col_q = i % cols_q
            lin_q = i // cols_q
            qrect = pygame.Rect(rx + col_q * 72, 443 + lin_q * 42, 64, 34)
            sel = quarto_selecionado == q["id"]
            cor = (50, 130, 230) if sel else ((80, 160, 255) if qrect.collidepoint(mouse) else (200, 215, 235))
            cor_t = (255, 255, 255) if sel or qrect.collidepoint(mouse) else (20, 20, 60)
            pygame.draw.rect(tela, cor, qrect, border_radius=7)
            pygame.draw.rect(tela, (50, 130, 230), qrect, 1, border_radius=7)
            ts = fonte_tiny.render(f"Q{q['id']}", True, cor_t)
            tela.blit(ts, (qrect.x + (qrect.width - ts.get_width()) // 2,
                           qrect.y + (qrect.height - ts.get_height()) // 2))

    checkin_ok = quarto_selecionado is not None
    btn_conf = pygame.Rect(rx, 620, 285, 38)
    cor_btn = (50, 190, 90) if (checkin_ok and btn_conf.collidepoint(mouse)) else \
        (30, 160, 70) if checkin_ok else (120, 120, 120)
    pygame.draw.rect(tela, cor_btn, btn_conf, border_radius=9)
    bs = fonte_pequenabold.render("Confirmar Check-In", True, (255, 255, 255))
    tela.blit(bs, (btn_conf.x + (btn_conf.width - bs.get_width()) // 2,
                   btn_conf.y + (btn_conf.height - bs.get_height()) // 2))
    return btn_conf

def desenhar_consumos(mouse):
    pygame.draw.line(tela, (80, 120, 180), (1055, 410), (1055, 668), 1)

    s = fonte_pequenabold.render("Pedidos de consumo:", True, (0, 51, 102))
    tela.blit(s, (723, 378))

    if not lista_consumos:
        s = fonte_pequena.render("Nenhum pedido pendente", True, (64, 64, 64))
        tela.blit(s, (723, 408))
    else:
        for i, pedido in enumerate(lista_consumos):
            card = pygame.Rect(723, 405 + i * 40, 318, 34)
            selecionado = (consumo_selecionado == pedido)
            if selecionado:
                cor_card = (50, 130, 230)
                cor_txt = (255, 255, 255)
            elif card.collidepoint(mouse):
                cor_card = (180, 210, 255)
                cor_txt = (0, 30, 80)
            else:
                cor_card = (220, 230, 245)
                cor_txt = (20, 20, 60)
            pygame.draw.rect(tela, cor_card, card, border_radius=8)
            pygame.draw.rect(tela, (100, 140, 200), card, 1, border_radius=8)

            txt_pedido = f"Q{pedido['quarto_id']} - {pedido['item']} (R$ {pedido['preco']:.2f})"
            ns = fonte_tinybold.render(txt_pedido, True, cor_txt)
            tela.blit(ns, (card.x + 10, card.y + (card.height - ns.get_height()) // 2))

    rx = 1067
    if consumo_selecionado is None:
        hint = fonte_pequena.render("Selecione um pedido", True, (64, 64, 64))
        tela.blit(hint, (rx, 410))
        return None

    nome_lbl = fonte_pequenabold.render(f"Hóspede: {consumo_selecionado['hospede']}", True, (0, 51, 102))
    tela.blit(nome_lbl, (rx, 378))

    q_lbl = fonte_pequena.render(f"Quarto: {consumo_selecionado['quarto_id']}", True, (20, 20, 60))
    tela.blit(q_lbl, (rx, 415))

    item_lbl = fonte_pequena.render(f"Item: {consumo_selecionado['item']}", True, (20, 20, 60))
    tela.blit(item_lbl, (rx, 445))

    val_str = f"Valor: R$ {consumo_selecionado['preco']:.2f}".replace(".", ",")
    p_lbl = fonte_pequenabold.render(val_str, True, (0, 140, 60))
    tela.blit(p_lbl, (rx, 475))

    btn_reg = pygame.Rect(rx, 620, 285, 38)
    cor_btn = (50, 190, 90) if btn_reg.collidepoint(mouse) else (30, 160, 70)
    pygame.draw.rect(tela, cor_btn, btn_reg, border_radius=9)
    bs = fonte_pequenabold.render("Registrar Consumo", True, (255, 255, 255))
    tela.blit(bs, (btn_reg.x + (btn_reg.width - bs.get_width()) // 2,
                   btn_reg.y + (btn_reg.height - bs.get_height()) // 2))
    return btn_reg

def desenhar_quartos(quartos, mouse):
    painel_x, painel_y = 705, 690
    margem = 8
    cols = 5
    card_w = (685 - margem * (cols + 1)) // cols
    card_h = (280 - margem * 3) // 2
    agora = pygame.time.get_ticks()

    for i, quarto in enumerate(quartos):
        col = i % cols
        lin = i // cols
        x = painel_x + margem + col * (card_w + margem)
        y = painel_y + 40 + margem + lin * (card_h + margem)

        rect = pygame.Rect(x, y, card_w, card_h)

        if hospede_selecionado and quarto["status"] == "livre" and rect.collidepoint(mouse):
            cor = (120, 200, 120)
        elif quarto["status"] == "ocupado":
            cor = (220, 80, 80) if rect.collidepoint(mouse) else (180, 50, 50)
        elif quarto["status"] == "livre":
            cor = (80, 200, 110) if rect.collidepoint(mouse) else (50, 160, 80)
        else:
            cor = (80, 80, 80)

        pygame.draw.rect(tela, cor, rect, border_radius=10)
        pygame.draw.rect(tela, (255, 255, 255), rect, 2, border_radius=10)

        s = fonte_pequenabold.render(f"Q{quarto['id']}", True, (255, 255, 255))
        tela.blit(s, (x + 8, y + 6))

        status_txt = fonte_tiny.render(quarto["status"].upper(), True, (255, 255, 255))
        tela.blit(status_txt, (x + 8, y + 28))

        if quarto["hospede"]:
            nome_s = fonte_tiny.render(quarto["hospede"], True, (255, 230, 180))
            tela.blit(nome_s, (x + 8, y + 48))

            if quarto["tempo_saida"] > 0:
                rest = max(0, quarto["tempo_saida"] - agora) // 1000
                ts = fonte_tiny.render(f"{rest}s", True, (255, 210, 80))
                tela.blit(ts, (x + 8, y + 68))

def desenhar_painel_status(dinheiro, hora, dia):
    pygame.draw.rect(tela, (255, 255, 255), (13, 13, 200, 100), border_radius=12)
    pygame.draw.rect(tela, (0, 0, 0), (13, 13, 200, 100), 3, border_radius=12)
    surf = fonte_pequenabold.render(f"{hora:02d}:00  Dia {dia}", True, (0, 51, 102))
    tela.blit(surf, (24, 22))
    pygame.draw.line(tela, (200, 200, 200), (24, 50), (203, 50), 1)
    texto_din = f"R$ {dinheiro:,.2f}".replace(",", ".")
    cor_din = (0, 140, 60) if dinheiro >= 0 else (200, 40, 40)
    tela.blit(fonte_pequenabold.render(texto_din, True, cor_din), (24, 58))
    cor_btn_ajuda = (80, 160, 255) if btn_ajuda.collidepoint(mouse) else (50, 130, 230)
    pygame.draw.rect(tela, cor_btn_ajuda, btn_ajuda, border_radius=8)
    pygame.draw.rect(tela, (255, 255, 255), btn_ajuda, 2, border_radius=8)
    txt_ajuda = fonte_mediabold.render("?", True, (255, 255, 255))
    tela.blit(txt_ajuda, (btn_ajuda.x + (btn_ajuda.width - txt_ajuda.get_width()) // 2,
                          btn_ajuda.y + (btn_ajuda.height - txt_ajuda.get_height()) // 2 - 2))

def desenhar_badge(cx, cy, texto, cor_fundo=(50, 130, 230), cor_texto=(255, 255, 255)):
    surf = fonte_tinybold.render(texto, True, cor_texto)
    pad_x, pad_y = 10, 4
    w = surf.get_width() + pad_x * 2
    h = surf.get_height() + pad_y * 2
    rect = pygame.Rect(cx - w // 2, cy - h // 2, w, h)
    pygame.draw.rect(tela, cor_fundo, rect, border_radius=8)
    tela.blit(surf, (rect.x + pad_x, rect.y + pad_y))

def desenhar_btn(rect, label, sublabel, maxed, mouse):
    if maxed:
        cor = (110, 110, 110)
    elif rect.collidepoint(mouse):
        cor = (80, 160, 255)
    else:
        cor = (50, 130, 230)
    pygame.draw.rect(tela, cor, rect, border_radius=10)
    if maxed:
        s = fonte_pequena.render("Nível máximo", True, (255, 255, 255))
        tela.blit(s, (rect.x + (rect.width - s.get_width()) // 2,
                      rect.y + (rect.height - s.get_height()) // 2))
    else:
        s1 = fonte_pequena.render(label, True, (255, 255, 255))
        s2 = fonte_tiny.render(sublabel, True, (200, 240, 180))
        tela.blit(s1, (rect.x + (rect.width - s1.get_width()) // 2, rect.y + 7))
        tela.blit(s2, (rect.x + (rect.width - s2.get_width()) // 2, rect.y + 28))

def desenhar_aviso(tela, mensagem, fonte):
    overlay = pygame.Surface((1400, 1020))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    caixa = pygame.Rect(450, 360, 500, 200)
    pygame.draw.rect(tela, (255, 255, 255), caixa, border_radius=12)
    pygame.draw.rect(tela, (50, 130, 230), caixa, 3, border_radius=12)

    s = fonte.render(mensagem, True, (0, 0, 0))
    tela.blit(s, (caixa.x + (caixa.width - s.get_width()) // 2,
                  caixa.y + 40))

    btn_ok = pygame.Rect(caixa.x + 175, caixa.y + 120, 150, 45)
    pygame.draw.rect(tela, (50, 130, 230), btn_ok, border_radius=8)
    tok = fonte.render("OK", True, (255, 255, 255))
    tela.blit(tok, (btn_ok.x + (btn_ok.width - tok.get_width()) // 2,
                    btn_ok.y + (btn_ok.height - tok.get_height()) // 2))
    return btn_ok

def salvar_relatorio(dinheiro, dia, hora, quartos, lista_consumos, lvlhoteldisplay):
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_arquivo = f"relatorio_dia{dia}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("   RELATÓRIO DE ENCERRAMENTO - HOTEL\n")
        f.write("=" * 40 + "\n")
        f.write(f"Gerado em: {agora}\n")
        f.write(f"Nível do hotel: {lvlhoteldisplay} estrela(s)\n")
        f.write(f"Dia do jogo: {dia} | Hora de encerramento: {hora:02d}:00\n")
        f.write(f"Faturamento total: R$ {dinheiro:,.2f}\n".replace(",", "."))
        f.write("\n--- QUARTOS ---\n")
        for q in quartos:
            hospede = q["hospede"] if q["hospede"] else "-"
            f.write(f"  Quarto {q['id']:02d}: {q['status'].upper():<10} | Hóspede: {hospede}\n")
        f.write("\n--- CONSUMOS PENDENTES ---\n")
        if lista_consumos:
            for c in lista_consumos:
                f.write(f"  Q{c['quarto_id']} | {c['hospede']} | {c['item']} - R$ {c['preco']:.2f}\n")
        else:
            f.write("  Nenhum consumo pendente.\n")
        f.write("\n" + "=" * 40 + "\n")
        f.write("Expediente encerrado. Até amanhã!\n")

while True:
    dt = relogio.tick(60)
    mouse = pygame.mouse.get_pos()

    acumulador_horario += dt
    while acumulador_horario >= MS_POR_HORA_JOGO:
        acumulador_horario -= MS_POR_HORA_JOGO
        hora_jogo += 1
        if hora_jogo >= 24:
            hora_jogo = 0
            dia_jogo += 1

    acumulador_receita += dt
    while acumulador_receita >= MS_POR_MINUTO_JOGO:
        acumulador_receita -= MS_POR_MINUTO_JOGO
        multiplicador = 1.0 + upgrades_quarto * 0.2
        ganho = contar_ocupados(quartos) * cfg()["receita"] * multiplicador
        dinheiro += ganho

    atualizar_saidas()

    acumulador_hospede += dt
    if acumulador_hospede >= MS_ENTRE_HOSPEDES:
        acumulador_hospede = 0
        if len(fila_hospedes) < MAX_FILA_HOSPEDES:
            nomes_na_fila = set(fila_hospedes)
            candidatos = [n for n in NOMES if n not in nomes_na_fila]
            if candidatos:
                fila_hospedes.append(random.choice(candidatos))

    acumulador_consumo += dt
    if acumulador_consumo >= MS_ENTRE_CONSUMOS:
        acumulador_consumo = 0
        if len(lista_consumos) < MAX_LISTA_CONSUMOS:
            quartos_ocupados = [q for q in quartos if q["status"] == "ocupado"]
            if quartos_ocupados:
                q_escolhido = random.choice(quartos_ocupados)
                item_escolhido = random.choice(ITENS_CONSUMO)
                novo_pedido = {
                    "quarto_id": q_escolhido["id"],
                    "hospede": q_escolhido["hospede"],
                    "item": item_escolhido["item"],
                    "preco": item_escolhido["preco"]
                }
                lista_consumos.append(novo_pedido)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvar_relatorio(dinheiro, dia_jogo, hora_jogo, quartos, lista_consumos, lvlhoteldisplay)
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not mostrar_aviso and not mostrar_tutorial:

            clicou_algo = False

            if btn_ajuda.collidepoint(mouse) and not mostrar_tutorial:
                mostrar_tutorial = True
                clicou_algo = True

            for i, nome in enumerate(fila_hospedes):
                card = pygame.Rect(28, 405 + i * 40, 318, 34)
                if card.collidepoint(mouse):
                    hospede_selecionado = nome
                    quarto_selecionado = None
                    clicou_algo = True
                    break

            if hospede_selecionado is not None and not clicou_algo:
                livres = quartos_livres(quartos)
                cols_q = 4
                for i, q in enumerate(livres):
                    col_q = i % cols_q
                    lin_q = i // cols_q
                    qrect = pygame.Rect(372 + col_q * 72, 443 + lin_q * 42, 64, 34)
                    if qrect.collidepoint(mouse):
                        quarto_selecionado = q["id"]
                        clicou_algo = True
                        break

                btn_conf = pygame.Rect(372, 620, 285, 38)
                if btn_conf.collidepoint(mouse) and quarto_selecionado is not None:
                    for q in quartos:
                        if q["id"] == quarto_selecionado and q["status"] == "livre":
                            fazer_checkin(hospede_selecionado, q)
                            if hospede_selecionado in fila_hospedes:
                                fila_hospedes.remove(hospede_selecionado)
                            hospede_selecionado = None
                            quarto_selecionado = None
                            break
                    clicou_algo = True

            if not clicou_algo:
                hospede_selecionado = None
                quarto_selecionado = None

            clicou_consumo = False
            for i, pedido in enumerate(lista_consumos):
                card = pygame.Rect(723, 405 + i * 40, 318, 34)
                if card.collidepoint(mouse):
                    consumo_selecionado = pedido
                    clicou_consumo = True
                    break

            if consumo_selecionado is not None and not clicou_consumo:
                btn_reg = pygame.Rect(1067, 620, 285, 38)
                if btn_reg.collidepoint(mouse):
                    dinheiro += consumo_selecionado["preco"]
                    lista_consumos.remove(consumo_selecionado)
                    consumo_selecionado = None
                    clicou_consumo = True

            if not clicou_consumo:
                consumo_selecionado = None

            if btn_upgquarto.collidepoint(mouse):
                max_upg = cfg()["max_upg"]
                preco = cfg()["preco_upgq"]
                if upgrades_quarto >= max_upg:
                    mostrar_aviso = True
                    mensagem_aviso = "Nível máximo de quarto atingido!"
                elif dinheiro >= preco:
                    dinheiro -= preco
                    upgrades_quarto += 1
                else:
                    mostrar_aviso = True
                    mensagem_aviso = "Dinheiro insuficiente!"

            if btn_morequarto.collidepoint(mouse):
                preco = cfg()["preco_moreq"]
                if todos_desbloqueados(quartos):
                    mostrar_aviso = True
                    mensagem_aviso = "Todos os quartos já estão desbloqueados!"
                elif dinheiro >= preco:
                    dinheiro -= preco
                    for q in quartos:
                        if q["status"] == "bloqueado":
                            q["status"] = "livre"
                            break
                else:
                    mostrar_aviso = True
                    mensagem_aviso = "Dinheiro insuficiente!"

            if btn_upghotel.collidepoint(mouse):
                preco = cfg()["preco_hotel"]
                if lvlhotel >= 5:
                    mostrar_aviso = True
                    mensagem_aviso = "Nível máximo de Hotel atingido!"
                elif dinheiro >= preco:
                    dinheiro -= preco
                    lvlhotel += 2
                    lvlhoteldisplay += 1
                    upgrades_quarto = 0
                    hospede_selecionado = None
                    quarto_selecionado = None
                    consumo_selecionado = None
                    lista_consumos.clear()

                    img_hotel = pygame.transform.scale(pygame.image.load(f"hotel{lvlhotel}estrela.png"), (1380, 324))
                    img_recepcao = pygame.transform.scale(pygame.image.load(f"recepcao{lvlhotel}estrela.png"),
                                                          (685, 330))
                    img_restaurante = pygame.transform.scale(pygame.image.load(f"restaurante{lvlhotel}estrela.png"),
                                                             (685, 330))
                    img_quarto = pygame.transform.scale(pygame.image.load(f"quarto{lvlhotel}estrela.png"), (685, 330))

                    if lvlhoteldisplay == 2:
                        quartos = quartos2
                    elif lvlhoteldisplay == 3:
                        quartos = quartos3
                else:
                    mostrar_aviso = True
                    mensagem_aviso = "Dinheiro insuficiente!"

    tela.fill((40, 40, 40))

    pygame.draw.rect(tela, (0, 51, 102), (10, 10, 1380, 330), border_radius=12)
    tela.blit(img_hotel, (10, 13))
    pygame.draw.rect(tela, (50, 130, 230), (10, 10, 1380, 330), 3, border_radius=12)

    pygame.draw.rect(tela, (0, 51, 102), (10, 350, 685, 330), border_radius=12)
    tela.blit(img_recepcao, (10, 350))
    tela.blit(filtro, (10, 350))
    pygame.draw.rect(tela, (50, 130, 230), (10, 350, 685, 330), 3, border_radius=12)

    pygame.draw.rect(tela, (0, 51, 102), (705, 350, 685, 330), border_radius=12)
    tela.blit(img_restaurante, (705, 350))
    tela.blit(filtro, (705, 350))
    pygame.draw.rect(tela, (50, 130, 230), (705, 350, 685, 330), 3, border_radius=12)

    pygame.draw.rect(tela, (0, 51, 102), (10, 690, 685, 330), border_radius=12)
    pygame.draw.rect(tela, (50, 130, 230), (10, 690, 685, 330), 3, border_radius=12)

    pygame.draw.rect(tela, (0, 51, 102), (705, 690, 685, 330), border_radius=12)
    tela.blit(img_quarto, (705, 690))
    tela.blit(filtro, (705, 690))
    pygame.draw.rect(tela, (50, 130, 230), (705, 690, 685, 330), 3, border_radius=12)

    desenhar_painel_status(dinheiro, hora_jogo, dia_jogo)

    tela.blit(fonte_mediabold.render("Check-In", True, (0, 51, 102)), (290, 360))
    tela.blit(fonte_mediabold.render("Consumos", True, (0, 51, 102)), (985, 360))
    tela.blit(fonte_mediabold.render("Upgrades", True, (50, 130, 230)), (290, 700))
    tela.blit(fonte_mediabold.render("Quartos", True, (0, 51, 102)), (985, 700))

    desenhar_checkin(mouse)
    desenhar_consumos(mouse)

    max_upg = cfg()["max_upg"]
    preco_upgq = cfg()["preco_upgq"]
    upg_max = upgrades_quarto >= max_upg
    badge_upgq_cor = (100, 100, 100) if upg_max else (0, 51, 102)
    mult_str = f"{upgrades_quarto}/{max_upg}  x{1.0 + upgrades_quarto * 0.2:.1f}"
    desenhar_badge(btn_upgquarto.centerx, btn_upgquarto.y - 14, mult_str, badge_upgq_cor)
    desenhar_btn(btn_upgquarto, "Upg. Quarto", f"R$ {preco_upgq:,.0f}", upg_max, mouse)

    total_q = len(quartos)
    desbloqueados = sum(1 for q in quartos if q["status"] != "bloqueado")
    quartos_cheios = todos_desbloqueados(quartos)
    preco_moreq = cfg()["preco_moreq"]
    badge_moreq_cor = (100, 100, 100) if quartos_cheios else (0, 51, 102)
    desenhar_badge(btn_morequarto.centerx, btn_morequarto.y - 14,
                   f"{desbloqueados}/{total_q}", badge_moreq_cor)
    desenhar_btn(btn_morequarto, "+1 Quarto", f"R$ {preco_moreq:,.0f}", quartos_cheios, mouse)

    hotel_max = lvlhotel >= 5
    preco_hotel = cfg()["preco_hotel"]
    badge_hotel_cor = (100, 100, 100) if hotel_max else (0, 51, 102)
    desenhar_badge(btn_upghotel.centerx, btn_upghotel.y - 14,
                   f"Hotel {lvlhoteldisplay}/3", badge_hotel_cor)
    desenhar_btn(btn_upghotel, "Upg. Hotel",
                 "Nível máx." if hotel_max else f"R$ {preco_hotel:,.0f}",
                 hotel_max, mouse)

    desenhar_quartos(quartos, mouse)

    if mostrar_aviso:
        btn_ok = desenhar_aviso(tela, mensagem_aviso, fonte_media)
        if pygame.mouse.get_pressed()[0] and btn_ok.collidepoint(mouse):
            mostrar_aviso = False

    if mostrar_tutorial and not mostrar_aviso:
        mostrar_tutorial = ComoJogar.exibir_tutorial(tela, fonte_mediabold, fonte_pequenabold, fonte_pequena,
                                                     fonte_tiny, mouse)

    pygame.display.flip()