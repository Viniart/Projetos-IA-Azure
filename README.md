# 🧠 Azure OpenAI + Speech Services

Este repositório contém **três projetos** que demonstram uma integração entre **Azure OpenAI** e **Serviços de Fala (Speech Services)** da Azure, permitindo **reconhecimento de fala**, **síntese de voz** e **interação natural com IA**.

**Reconhecimento de Fala** - Você fala e o ChatGPT responde
**Síntese de Voz** - O ChatGPT responde e a resposta dele é falada

Os projetos foram inspirados nos repositórios oficiais da Microsoft:

* [mslearn-openai](https://github.com/MicrosoftLearning/mslearn-openai)
* [mslearn-ai-language](https://github.com/MicrosoftLearning/mslearn-ai-language)

---

## 📁 Estrutura do Repositório

```
📦 ProjetoAzureIA
 ┣ 📂 ReconhecimentoFala
 ┃ ┗ ▶️ Projeto de reconhecimento de fala + ChatGPT
 ┣ 📂 SintetizacaoFala
 ┃ ┗ ▶️ Projeto de síntese de fala (ChatGPT fala)
 ┣ 📂 ProjetoCompleto
 ┃ ┗ ▶️ Integra os dois anteriores: fala com o ChatGPT e ouve as respostas em voz
 ┗ 📄 README.md
```

---

## 🧩 Descrição dos Projetos

### 🎤 1. ReconhecimentoFala

Neste projeto, você fala com o **microfone** e o Azure Speech reconhece sua fala, transformando-a em texto.
O texto é enviado ao modelo **Azure OpenAI**, que responde diretamente no terminal.

### 🔊 2. SintetizacaoFala

Aqui, a interação ocorre por **input de texto**.
Você digita sua mensagem, o ChatGPT responde, e a resposta é **sintetizada em fala** usando uma voz neural do Azure Speech.

### 🧠 3. ProjetoCompleto

Este é o projeto principal, que **une as duas funcionalidades anteriores**.
Você pode **falar com o ChatGPT usando o microfone** e **ouvir as respostas** da IA em voz natural.

---

## 🚀 Execução do Projeto Completo

### Pré-requisitos

1. **Python 3.9+** instalado.

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # (Windows)
   ```

3. Instale as dependências:

   ```bash
   pip install python-dotenv openai azure-cognitiveservices-speech
   ```

4. Crie um arquivo **.env** na raiz do projeto com suas chaves Azure:

   ```ini
   AZURE_OAI_ENDPOINT=https://<seu-endpoint-openai>.openai.azure.com/
   AZURE_OAI_KEY=<sua-chave-openai>
   AZURE_OAI_DEPLOYMENT=<nome-do-deployment-do-modelo>
   AZURE_SPEECH_KEY=<sua-chave-speech>
   AZURE_SPEECH_REGION=<região-speech>
   ```

---

## Como Executar

1. Acesse a pasta **ProjetoCompleto**:

   ```bash
   cd ProjetoCompleto
   ```

2. Execute o script:

   ```bash
   python main.py
   ```

3. O assistente será iniciado:

   ```
   --- Chatbot IA Iniciado (fale 'sair' para sair) ---
   Serviço de reconhecimento de fala pronto.
   Testando a função de ouvir... Fale algo!
   ```

4. Fale algo no microfone 🎙️
   A IA responderá **em texto e voz**, utilizando o modelo **pt-BR-FranciscaNeural**.

---

## 🗣️ Fluxo do Projeto Completo

1. **Você fala** →
2. **Azure Speech** converte fala em texto →
3. **Azure OpenAI (ChatGPT)** responde →
4. **Azure Speech** sintetiza a resposta em voz →
5. **Você ouve a resposta** 👂

---

## 🧱 Estrutura Principal do Código

O código é dividido em funções simples e bem organizadas:

* `ouvir_do_microfone()` → Captura e reconhece o áudio do microfone.
* `falar_texto()` → Converte texto em fala com voz neural.
* `main()` → Controla o fluxo da conversa (fala → IA → voz).

---

## Tecnologias Utilizadas


**Azure OpenAI** - Geração de texto (ChatGPT)

**Azure Speech** - Reconhecimento e síntese de fala

**Python** - Linguagem principal

**dotenv** - Leitura de variáveis de ambiente

**openai SDK** - Conexão com Azure OpenAI    

**azure-cognitiveservices-speech** - Conexão com Azure Speech

---

## Exemplo de Interação

```
--- Chatbot IA Iniciado (fale 'sair' para sair) ---
Serviço de reconhecimento de fala pronto.
Testando a função de ouvir... Fale algo!
Você: "Qual a capital da França?"
IA: "A capital da França é Paris."
(síntese de voz reproduzida)
```

---

## 📘 Créditos

Inspirado nos laboratórios oficiais da Microsoft:

* [Microsoft Learn - OpenAI](https://github.com/MicrosoftLearning/mslearn-openai)
* [Microsoft Learn - AI Language](https://github.com/MicrosoftLearning/mslearn-ai-language)

Desenvolvido para fins educacionais.

---

## 🧑‍💻 Autor

**Vinicio S.**
