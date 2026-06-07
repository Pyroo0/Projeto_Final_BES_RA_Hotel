Hotel Incremental

Jogo de gerenciamento de hotel desenvolvido em Python com Pygame, como projeto final da disciplina de Raciocínio Algorítmico — PUCPR 2026/1.



Descrição

Você é o administrador de um hotel e precisa gerenciar o estabelecimento em tempo real. Faça check-in de hóspedes, registre consumos, desbloqueie quartos e faça upgrades para evoluir seu hotel de 1 a 3 estrelas. Ao encerrar o expediente, um relatório completo é salvo automaticamente.



Como jogar

Check-in
1. Aguarde um hóspede aparecer na fila (painel esquerdo)
2. Clique no nome do hóspede para selecioná-lo
3. Escolha um quarto livre disponível
4. Clique em **Confirmar Check-In**

Consumos
1. Hóspedes fazem pedidos automaticamente (painel direito)
2. Clique no pedido para selecioná-lo
3. Clique em **Registrar Consumo** para receber o valor

Upgrades (painel inferior esquerdo)
- **Upg. Quarto** — aumenta a receita por minuto de cada quarto ocupado
- **+1 Quarto** — desbloqueia um novo quarto
- **Upg. Hotel** — evolui o hotel para o próximo nível de estrelas



Requisitos

- Python 3.8 ou superior
- Pygame

Instalação do Pygame

```bash
pip install pygame
```



Como executar

```bash
python JogoHotelLisiane.py
```

> As imagens do jogo já estão incluídas na pasta do projeto e são carregadas automaticamente.



Estrutura do projeto

```
Projeto Final
 ├── JogoHotelLisiane.py       # Arquivo principal
 ├── ComoJogar.py              # Módulo da tela de tutorial
 ├── hotel1estrela.png         # Imagens do hotel nível 1
 ├── recepcao1estrela.png
 ├── restaurante1estrela.png
 ├── quarto1estrela.png
 ├── hotel3estrela.png         # Imagens do hotel nível 2
 ├── recepcao3estrela.png
 ├── restaurante3estrela.png
 ├── quarto3estrela.png
 ├── hotel5estrela.png         # Imagens do hotel nível 3
 ├── recepcao5estrela.png
 ├── restaurante5estrela.png
 ├── quarto5estrela.png
 └── README.md
```



Relatório de encerramento

Ao fechar o jogo, um arquivo `relatorio_dia{N}.txt` é gerado automaticamente na pasta do projeto com:

- Data e hora real do encerramento
- Nível do hotel e dia/hora do jogo
- Faturamento total acumulado
- Status de todos os quartos
- Consumos pendentes não registrados



Tecnologias utilizadas

| Biblioteca | Uso |
|---|---|
| `pygame` | Interface gráfica e loop do jogo |
| `random` | Geração de hóspedes e pedidos aleatórios |
| `datetime` | Registro da hora real no relatório |
| `os` | Manipulação de caminhos de arquivo |
| `math` | Cálculo dinâmico do layout de quartos |
| `sys` | Encerramento do sistema |



Autor

Pedro — Engenharia de Software, PUCPR  
GitHub: [@Pyroo0](https://github.com/Pyroo0)
