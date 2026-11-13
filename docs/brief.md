# Brief do Projeto: Carol_01 — Experiência Didática & Portal da Carol

## 1. Visão Geral e Posicionamento
Criação de um portal web interativo e experiência digital de aprendizagem fundamentada no conteúdo, estilo, design e didática da professora Carol.

- **Diferencial Crítico:** O design visual, layout, tipografia, paleta de cores e tom de voz do produto não serão genéricos; serão derivados diretamente da análise estética e funcional dos **slides** e do **vídeo** da sua aula.
- **Protocolo de Qualidade:** Registro rigoroso do padrão visual em [`./docs/design_system_carol.md`](./docs/design_system_carol.md) antes da codificação da interface final.

## 2. Metodologia em 2 Etapas Estratégicas

### Etapa 1: Análise Multimodal & Registro de Padrão (Prioridade Imediata)
1. **Inspeção dos Slides (`assets/slides/`):**
   - Extração da paleta de cores oficial (hex codes primários, secundários, fundos, acentos).
   - Mapeamento tipográfico (famílias de fontes para títulos, corpo, destaques e espaçamentos).
   - Padrão de diagramação (espaço em branco, proporção dos cards, ícones, molduras e alinhamentos).
   - Linguagem visual (minimalista, ilustrada, corporativa, acolhedora, acadêmica).
2. **Inspeção do Vídeo da Aula (`assets/video/`):**
   - Didática, ritmo e tom de voz (acolhedor, direto, dinâmico, reflexivo).
   - Pontos de ênfase e ganchos de aprendizagem.
   - Recursos visuais adicionais exibidos ou enfatizados em tela.
3. **Entregável da Etapa 1:** [`./docs/design_system_carol.md`](./docs/design_system_carol.md) — Documento completo de padrão com paleta, regras de layout e componentes visuais.

### Etapa 2: Desenvolvimento da Interface Web (HTML/CSS/JS)
1. Proposta de arquitetura de informação e wireframe/seções.
2. Construção de HTML5 semântico com CSS3 customizado e JavaScript modular.
3. Design 100% responsivo (mobile, tablet, desktop) com zero overflow horizontal.
4. Recursos interativos alinhados à didática da Carol (ex.: abas, modais, checklists, resumos dinâmicos).
5. Auditoria independente de qualidade via `revisor-qualidade` e testes automatizados.

## 3. Critérios de Sucesso
- [ ] Materiais de aula (slides e vídeo) recebidos e analisados.
- [ ] Padrão de design e UX documentado e aprovado pelo usuário.
- [ ] Interface HTML implementada com fidelidade estética absoluta ao padrão da Carol.
- [ ] Pontuação de qualidade máxima no Glance Test e nos testes de conformidade.
