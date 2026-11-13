# Plano de Melhorias & Encantamento: Carol_01 (v2.0)
## *Cura pelo Movimento — Guia Digital de Apoio (Aula 1)*

> **Objetivo:** Elevar o encantamento, a experiência sensorial e a utilidade prática do guia digital para as alunas do curso, mantendo o site leve, acessível e sem excessos.

---

## 1. As 5 Propostas de Melhoria

### 🌟 Melhoria 1: Pílula de Áudio Real com a Voz da Carol (Sintonização Afetuosa)
- **Problema/Oportunidade:** Hoje, o "Ritual do Suspiro" no Hero é um timer visual com texto. Ouvir a voz serena da Carol cantando o mantra de abertura (*Om Sahana Vavatu*) ou guiando o suspiro cria uma conexão somática e afetiva imediata.
- **Implementação:**
  - Extrair um trecho limpo de 45 segundos do áudio original (`cura_1.mp4`, minutos 01:55–02:40).
  - Converter para MP3 otimizado leve (~350 KB) em `assets/audio/sintonizacao-carol.mp3`.
  - Integrar um botão discreto no Hero: *"▶ Ouvir Sintonização com a Carol"*, com player minimalista nativo em HTML5 (`<audio>`), carregado sob demanda (sem autoplay).

---

### 🧘‍♀️ Melhoria 2: Modo "Ao Lado do Tapete" (Tapete Mode / Leitura Confortável)
- **Problema/Oportunidade:** Muitas alunas praticam com o celular ou tablet apoiado no chão ou em um bloquinho de Yoga a 1 ou 2 metros de distância. O tamanho padrão de fonte de leitura pode ficar pequeno nessa distância.
- **Implementação:**
  - Botão seletor na barra de navegação: `🧘‍♀️ Modo Tapete`.
  - Quando ativado, aumenta a tipografia base em 20%, eleva o espaçamento entre linhas e destaca com foco visual os blocos práticos (o Teste da Torção e a Respiração com Suspiro).
  - Persiste a preferência no navegador via `localStorage`.

---

### 📖 Melhoria 3: Glossário Vivo do Corpo (Dicionário de Fáscia em `<details>`)
- **Problema/Oportunidade:** Para alunas leigas de primeira viagem, termos técnicos como *Biotensegridade*, *Miofibroblastos*, *Pandiculação*, *Fasciacytes* e *Trilhos Anatômicos* podem gerar pequenas dúvidas.
- **Implementação:**
  - Seção sanfonada em acordeão nativo HTML5 (`<details>` e `<summary>`), com 8 termos explicados em 2 frases simples com o tom acolhedor da Carol.
  - Ocupa zero espaço visual quando fechado e serve de consulta rápida durante os estudos.

---

### 📝 Melhoria 4: Diário Somático da Aluna (Anotação Local Privada)
- **Problema/Oportunidade:** Ao final da aula e após o Teste da Torção na Cadeira, a aluna quer registrar as sensações do seu corpo para comparar nas próximas semanas.
- **Implementação:**
  - Campo de texto simples e intimista no Santuário da Prática: *"Meu diário somático da Aula 1: O que meu corpo sentiu hoje?"*.
  - Salva instantaneamente no `localStorage` do navegador da aluna.
  - Zero necessidade de login, contas ou servidores (privacidade 100% no dispositivo dela).

---

### 🖨️ Melhoria 5: Folha de Estudo para Impressão (Modo Apostila em Papel)
- **Problema/Oportunidade:** Várias alunas gostam de levar anotações em papel para o tapete ou colar na parede da sala de prática.
- **Implementação:**
  - Folha de estilo de impressão (`@media print`):
    - Converte o layout para fundo branco puro sem fundos escuros (economiza tinta).
    - Diagrama a Grande Tese, o Raio-X das 3 Camadas e o Teste da Torção em 2 páginas elegantes e legíveis.
    - Botão sutil no rodapé: *"🖨️ Imprimir / Salvar em PDF"*.

---

## 2. Cronograma de Execução Proposto

| Etapa | Ação | Arquivos Afetados | Verificação |
| :---: | :--- | :--- | :--- |
| **Etapa 1** | Extração e compressão do áudio da Carol | `assets/audio/sintonizacao-carol.mp3` | Teste de áudio e tamanho < 400 KB |
| **Etapa 2** | Modo Tapete (`styles.css` e `app.js`) | `assets/css/styles.css`, `assets/js/app.js` | Teste de alternância e tamanho de fonte |
| **Etapa 3** | Glossário Vivo em `<details>` | `index.html`, `src/index.html` | Validação semântica e acessibilidade |
| **Etapa 4** | Diário Somático com `localStorage` | `index.html`, `assets/js/app.js` | Teste de persistência de texto |
| **Etapa 5** | CSS de Impressão (`@media print`) | `assets/css/styles.css` | Teste de print layout em Chromium |
| **Etapa 6** | Bateria Pytest & Playwright | `tests/test_carol_portal.py` | 100% aprovado nos 4 viewports |
