# Jogo de Encontrar a Nota

## Descrição do Projeto

Este é um jogo simples onde o jogador deve encontrar a nota de R$ 50 ou R$ 100 em diferentes rodadas. O jogo é dividido em duas fases, cada uma com suas próprias regras.

## Funcionalidades

### Fase 1:
- O jogador deve inserir o percentual de vezes que a nota de R$ 50 aparecerá do lado esquerdo.
- Após inserir o número de rodadas, o jogador inicia o jogo clicando no botão "Iniciar Jogo".
- Cada rodada apresenta duas opções de botões: esquerda e direita.
- O jogador deve escolher a opção correta para ganhar pontos.
- Se o jogador demorar muito para escolher, volta para o início do jogo.

### Fase 2:
- Similar à Fase 1, mas com algumas variações.
- O jogador também deve inserir o percentual de vezes que a nota de R$ 50 aparecerá do lado esquerdo.
- As pontuações podem variar dependendo do tempo de resposta em relação à média.

## Estrutura do Código

O código está dividido em três partes principais:

1. **Configuração da Interface Gráfica:**
   - Utiliza a biblioteca customtkinter para a criação de elementos gráficos personalizados.
   - Define a aparência visual do aplicativo.

2. **Funções do Jogo:**
   - `MostrarInformaçao()`: Exibe informações sobre a aplicação.
   - `InfosJogo()`: Apresenta informações específicas sobre as regras do jogo.
   - `IniciarJogo()`: Configura e inicia a Fase 1 do jogo.
   - `iniciarSegundoJogo()`: Configura e inicia a Fase 2 do jogo.

3. **Interface Gráfica e Interação do Usuário:**
   - Utiliza entradas, rótulos e botões para interação com o usuário.
   - Manipula eventos de entrada para validar as informações inseridas.

## Dependências

- customtkinter
- CTkMessagebox
- PIL (Pillow)

## Como Executar

1. Instale as dependências:
   ```
   pip install customtkinter Pillow
   ```

2. Execute o script `app.py`.

## Observações

- Certifique-se de ter as imagens das notas na pasta "assets" no mesmo diretório do script.
- O código possui algumas funcionalidades que podem ser ajustadas conforme necessário.
