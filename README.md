# learning-langchain 🦜🔗

Repositório de estudos onde acompanho o curso [**LangChain - Develop AI Agents with LangChain & LangGraph**](https://www.udemy.com/course/langchain/?couponCode=MT260907G1B) (Udemy, por Eden Marco).

Aqui ficam meus códigos, anotações e experimentos feitos ao longo das aulas — normalmente adaptando os exemplos do curso para rodar com modelos locais via **Ollama** em vez de depender só de APIs pagas.

O material oficial do curso está em [langchain-course/](langchain-course/).

## 🧰 Stack

- **LangChain v1** + **LangGraph** — construção de chains e agentes
- **Ollama** (`langchain-ollama`) — LLMs rodando localmente
- **OpenAI** (`langchain-openai`) — alternativa em nuvem
- **Tavily** (`langchain-tavily`, `tavily-python`) — busca na web como tool
- **LangSmith** — tracing e observabilidade
- **rich** — output formatado no terminal
- **uv** — gerenciamento de dependências e ambiente virtual

## 📁 Estrutura

```
src/
├── session 2/              # Chains: PromptTemplate + LLM (resumo de texto)
└── session 3 (agents)/     # Agente com create_agent + tool de busca (Tavily)
```

## ▶️ Como rodar

1. **Instale as dependências** (o projeto usa [uv](https://docs.astral.sh/uv/)):

   ```bash
   uv sync
   ```

   Ou, com pip tradicional:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure o `.env`** na raiz do projeto:

   ```env
   OPENAI_API_KEY=...
   TAVILY_API_KEY=...
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_API_KEY=...
   LANGSMITH_PROJECT=learning-langchain
   ```

3. **Baixe os modelos do Ollama** usados nos exemplos:**
   Obs: Eu optei em utilizar modelos locais por conta que não quero ter custo. Porém caso você queria utilizar outro modelo que não seja local eu recomendo o da Groq, pois não tem custo alto (https://groq.com/)
   ```bash
   ollama pull phi3
   ollama pull qwen3:1.7b
   ```

4. **Execute uma das sessões**:

   ```bash
   uv run python "src/session 3 (agents)/main.py"
   ```

## 📌 Progresso

- [x] **Session 2** — primeira chain: `PromptTemplate | ChatOllama`
- [x] **Session 3** — primeiro agente com `create_agent` e tool customizada de busca
- [ ] RAG e vector stores
- [ ] LangGraph (reflection / reflexion agents)
