# Changelog — Sites/Carol_01

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

## [1.2.8] - 2026-11-13
### Corrigido
- **Causa Raiz do Vazamento de Textos nos Balões Solucionada:** Diagnóstico forense comprovou que navegadores bloqueiam `@import` de fontes externas do Google Fonts quando SVGs são carregados em tags `<img>` (Sandbox de Segurança do W3C). Como consequência, o navegador do usuário recorria à fonte cursiva padrão do sistema (Comic Sans / Segoe), cujos glifos são de 30% a 45% mais largos que o Caveat, fazendo as aspas e letras vazarem pelas bordas de balões estreitos.
- **Fontes Oficiais WOFF2 Embutidas em Base64 no SVG:** Inclusão direta dos binários oficiais de `Caveat 700` e `Quicksand 700` dentro do `<defs><style>` do arquivo `fluxograma-jornada-fascia.svg` em formato Base64 (`data:font/woff2;base64,...`). O arquivo agora é 100% autossuficiente e universal, dispensando qualquer requisição de rede e garantindo renderização idêntica em qualquer navegador e dispositivo.
- **Largura dos Balões com Blindagem Anti-Transbordamento:** As larguras dos 8 balões de fala da Carol foram redimensionadas para `240px` a `290px` (com folga de segurança lateral de até 50px de cada lado), perfeitamente contidas dentro dos cards de `330px`. Nenhuma letra ou pontuação vaza ou encosta nas bordas, mesmo sob variações extremas de renderização.

## [1.2.7] - 2026-11-13
### Adicionado
- **Passe-Partout e Ampla Área de Respiro no Mapa Somático:** Inclusão de moldura interna cremoso-aquarela (`#FAF7F0`) com padding respirável `clamp(16px, 2.5vw, 36px)` em volta do fluxograma vetorial, conferindo acabamento de galeria de arte e impedindo qualquer sensação de compressão visual contra as bordas do card.
- **Pílulas de Navegação Rápida para Mobile/Tablet:** Nova sub-barra horizontal de atalhos táteis (`.navbar-mobile-nav`) com rolagem suave (`overflow-x: auto`) para que alunas em smartphones e tablets acessem instantaneamente qualquer seção da aula com um toque leve, mantendo o design limpo e arejado.
- **Auditoria Automatizada em 8 Viewports com Playwright:** Bateria de testes que valida sistematicamente ausência total de overflow horizontal (`scrollWidth === innerWidth`) em Full HD (1920x1080), MacBook (1440x900), Laptop (1366x768), iPad Paisagem (1024x768), iPad Retrato (768x1024), iPhone (390x844), Galaxy (360x740) e Mobile Compacto (320x568).

### Modificado
- **Área de Respiro e Espaçamento Periférico em Toda a Página:** Aumento dos paddings verticais das seções (`clamp(72px, 8.5vw, 112px) 0`), gaps generosos nos grids (`clamp(24px, 3vw, 36px)`) e margens laterais seguras no `.container` (`width: min(100% - 48px, 1200px)`), proporcionando ritmo visual calmo, sereno e condizente com a experiência somática do Yoga.
- **Refinamento do Fluxograma Vetorial (SVG/PNG 1920x1080):** Cabeçalho redesenhado com 85px de respiro vertical livre até os cards, subtítulo de citação calibrado para fonte 20px suave, balões de fala da Carol refinados com cauda e bordas delicadas, e traçado fluido de retorno do Passo 4 ao 5.

## [1.2.6] - 2026-11-13
### Removido
- **Termo Técnico de Design System nos Rodapés:** Remoção de *"Design System v2.0 • Daylight Sanctuary & Somatic Watercolor"* do rodapé do portal e do fluxograma somático, substituído pela assinatura institucional *"Cura pelo Movimento • Carol Langowski • Fisioterapia Integrativa & Yoga Fascial"*.

## [1.2.5] - 2026-11-13
### Modificado
- **Balões de Fala Somáticos (Speech Bubbles) no Fluxograma:** Redesenho completo das falas da Carol no fluxograma em SVG/PNG 1920x1080. Todas as 8 anotações manuscritas agora residem em balões de fala orgânicos com caudas apontando para seus respectivos cards, com textos perfeitamente centralizados e contidos (zero cortes ou sobreposições).
- **Fluxo Orgânico Contínuo:** Curva de retorno do Passo 4 para o Passo 5 redesenhada para contornar suavemente e entrar pela lateral esquerda do Passo 5, desimpedindo completamente o topo do card.

## [1.2.4] - 2026-11-13
### Adicionado
- **Orbe Somático de Respiração Guiada (Daylight Sanctuary):** Componente interativo de respiração com anéis concêntricos em aquarela, expansão e retração fluida acelerada por hardware na GPU, aura translúcida pulsante e timer circular vetorial SVG (`stroke-dashoffset`).
- **Ritmo Somático de 12 Segundos & 3 Ciclos:** Sincronização da contagem regressiva em segundos com as 3 fases do método da Carol (Inspiração 4s, Sustentação serena 2s e Suspiro Somático 6s) e pérolas indicadoras de progresso.
- **Acessibilidade e Controle:** Suporte para pausar/retomar o exercício e conformidade com `@media (prefers-reduced-motion: reduce)`.

## [1.2.3] - 2026-11-13
### Removido
- **Botões Supérfluos da Barra de Navegação:** Remoção definitiva dos botões "Modo Tapete" e "Ir para o Tapetinho", atendendo ao feedback de clareza do usuário.
- **Classes e Lógica de Modo Tapete:** Limpeza completa de regras CSS órfãs (`body.tapete-mode`), remoção de handlers em JavaScript e sanitização do fluxograma somático para foco em práticas guiadas.

### Modificado
- **Barra de Navegação Ultra-Clean:** Layout de alta elegância composto exclusivamente pelo Brand oficial à esquerda e os 6 links temáticos essenciais à direita, com respiração visual e zero distrações.

## [1.2.2] - 2026-11-13
### Adicionado
- **Fluxograma Somático em Sketch / Aquarela:** Mapa mental de síntese da Aula 1 gerado em SVG vetorial e PNG renderizado em alta definição (1920x1080), contendo os 8 passos somáticos interconectados, botões de ação para download em PNG e visualização em tela cheia com SVG nativo.
- **Seção 9 (Mapa Somático):** Integrada ao `index.html` e `src/index.html` com container responsivo com proteção contra overflow horizontal em todas as larguras de tela.

### Modificado
- **Barra de Navegação (Navbar) Blindada:** Redesenho completo para eliminar quebras de linha e colapso de botões espremidos (conforme print da aluna). Links consolidados em 6 itens objetivos (`A Tese`, `Roupa Interna`, `3 Camadas`, `Biotensegridade`, `Glossário`, `Mapa Somático`) e ação primária limpa (`🧘‍♀️ Modo Tapete`).
- **Áudio Somático Reeditado & Masterizado (58s):** Captura do trecho correto (`00:00:46` a `00:01:44`) com suspiro duplo profundo e mantra védico completo (*Om Sahana Vavatu*) cantado pela Carol, masterizado acusticamente a 192 kbps com EBU R128 (-16 LUFS).
- **Responsividade e Testes:** Bateria de testes Pytest ampliada cobrindo o mapa somático e testando imunidade a overflow em 1440, 768, 480, 390, 360 e 320px.

## [1.2.1] - 2026-11-13
### Modificado
- **Acessibilidade & Hierarquia Semântica (WCAG AA):** Hierarquia de headings corrigida para fluxo contínuo (`h1 -> h2 -> h3`), eliminação completa de inversão de escala tipográfica (`heading_scale_issues = 0`).
- **Contraste de Cores Reforçado:** Tokens `--carol-terracotta` (#735645, 5.2:1) e `--carol-amber` (#975A16, 4.8:1) escurecidos cirurgicamente para texto sobre branco.
- **Ergonomia Tátil:** Alvos dos links da barra superior ampliados para $\ge 40\text{px}$ (`small_tap_targets = 0`).
- **Design Editorial Anti-Slop:** Remoção da tarja vertical de 5px no card de suspiro substituída por borda translúcida perimétrica orgânica; ícones dos cards bento integrados ao fluxo tipográfico editorial.

## [1.2.0] - 2026-11-13
### Adicionado
- **Pílula de Áudio Real com a Voz da Carol:** Trecho autêntico de 51s com fade-in/out (`assets/audio/sintonizacao-carol.mp3`, 407 KB) com o suspiro somático e o mantra védico *Om Sahana Vavatu*.
- **Modo Ao Lado do Tapete (`.tapete-mode`):** Aumento de 20% na escala tipográfica, espaçamento e realce visual dos blocos práticos para leitura confortável a distância no tapete, com persistência no `localStorage`.
- **Glossário Vivo do Corpo:** Acordeão nativo HTML5 (`<details>` e `<summary>`) com 8 termos fundamentais da ciência fascial traduzidos em tom afetuoso.
- **Diário Somático da Aluna:** Área de anotações no Santuário da Prática com salvamento automático e local no navegador via `localStorage` (100% privado).
- **Modo Impressão / Folha de Estudos (@media print):** Estilização para impressão e geração de PDF limpo com economia de tinta e diagramação equilibrada.
- **Suíte de Testes Playwright & Pytest:** 13 testes cobrindo áudio, modo tapete, glossário, diário somático, responsividade em 4 viewports e imunidade a erros.

## [1.1.0] - 2026-11-13
### Adicionado
- Enriquecimento epistêmico e conceitual a partir da transcrição dos 190 minutos de aula da Carol Langowski (Dr. Guimberteau, Metáfora da Mexerica, Aluno do Tênis, Ciência do Bocejo/Suspiro, Cicatrizes & Miofibroblastos, Método das Espirais).
- Teste somático interativo de torção na cadeira (Mini-Laboratório 2) com checklist e reteste.

## [1.0.0] - 2026-11-13
### Adicionado
- Portal digital completo de apoio à turma com 8 seções, alinhado ao Design System v2.0 (Daylight Sanctuary & Somatic Watercolor).
- 11 ilustrações oficiais aquarelas da Carol em alta resolução.

## [0.1.0] - 2026-11-13
### Adicionado
- Estrutura inicial do projeto (`software-app`) criada com Governança V4.5.
