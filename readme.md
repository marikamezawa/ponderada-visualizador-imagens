# Visualizador de Filtros em Imagens e Webcam

&emsp; Este é um visualizador de imagens e vídeo desenvolvido em Python com Streamlit, que permite aplicar filtros em imagens carregadas ou diretamente da webcam. A aplicação utiliza OpenCV para a aplicação de filtros  e streamlit-webrtc para o streaming em tempo real da câmera.


## Funcionalidades
Aplicação de múltiplos filtros (na ordem escolhida pelo usuário):

- Escala de cinza
- Inversão de cores
- Desfoque (blur)
- Realce de nitidez (sharpen)
- Detecção de bordas (Canny)

Visualização lado a lado da imagem original e da imagem modificada, download da imagem processada (no modo de upload) e interface interativa e simples via navegador, com resposta imediata.

## Modos de Entradas

O aplicativo oferece duas opções para entrada para a visualização de filtros:

- Upload de Imagem  

&emsp; Aqui, o usuário pode carregar uma imagem armazenada localmente por meio de um diálogo de seleção de arquivo, suportando formatos JPG, JPEG e PNG. Após o upload, a aplicação aplica os filtros escolhidos e exibe lado a lado a imagem original e a imagem processada. Além disso, oferece a opção de baixar a imagem filtrada em formato PNG para salvar no dispositivo. Esse modo é indicado para editar imagens estáticas e obter resultados finais para armazenamento.

- Webcam 

&emsp; Neste modo, o usuário pode utilizar a câmera do computador para capturar vídeo em tempo real. A aplicação acessa a webcam via navegador, aplica os filtros selecionados diretamente nos frames do vídeo e exibe o resultado na interface. É necessário conceder permissão para o acesso à câmera. Esse modo é útil para visualizar os efeitos dos filtros ao vivo, sem precisar carregar imagens do computador.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/marikamezawa/ponderada-visualizador-imagens.git
cd ponderada-visualizador-imagens
```

### 2. Crie um ambiente virtual para instalar as dependências do projeto

```bash
python3 -m venv venv
```

### 3. Ative o ambiente virtual


No Linux ou macOS:
```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```
### 4. Instale as bibliotecas necessárias

```bash
pip install -r requirements.txt
```

### 5. Execute o código

```bash
streamlit run main.py
```


## referências:

**ALVES, Thiago.** Building webcam streaming applications with Streamlit and OpenCV. 2023. Disponível em: https://thiagoalves.ai/pt/building-webcam-streaming-applications-with-streamlit-and-opencv/. Acesso em: 12 maio 2025.

**STREAMLIT.** st.file_uploader. Documentação oficial. Disponível em: https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader. Acesso em: 12 maio 2025.

**SANTOS, Diogo.** Streamlit com OpenCV: app com webcam, upload e filtros. YouTube, 2023. Disponível em: https://youtu.be/groftMCwSR0?feature=shared. Acesso em: 12 maio 2025.




