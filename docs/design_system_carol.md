# Design System & Manual de Estilo: Carol Langowski (Cura pelo Movimento)

> **Documento Canônico de Identidade Visual, UX e Tom de Voz**  
> *Extraído da análise forense dos slides da Aula 1 ("Fáscia e Yoga") e das gravações em áudio de Carol Langowski.*

---

## 1. Identidade, Filosofia & Atmosfera

### 1.1 O Conceito Central
- **Nome do Programa:** *Cura pelo Movimento*
- **Professora:** **Carol Langowski** — Fisioterapeuta de formação, professora de Yoga, com mentoria de Ana Otsubo e especialização internacional de 2 anos com Karen Kirkness (*Five Filaments* / Espirais Fasciais).
- **Atmosfera (The Vibe):** **"Daylight Sanctuary / Holistic Scientific"**  
  Um equilíbrio refinado entre a **precisão científica da anatomia/fisioterapia** e o **calor, fluidez e serenidade acolhedora do Yoga**. Não é uma estética médica fria de hospital nem um visual místico genérico; é uma estética de bem-estar baseado em evidências, com respeito à biologia do corpo e à sabedoria ancestral.
- **Princípio Motor Chave:**
  > *"A forma segue a função. A função altera-se com a forma."*  
  > *"Comandos no ásana: gerar expansão, não contração."*  
  > *"sthiram sukham asanam"* (Postura firme e confortável).

---

## 2. Paleta de Cores Oficial (Extraída dos Slides)

```
┌────────────────────────────────────────────────────────────────────────┐
│  #234E52        #319795        #EFF8F7        #FFFFFF        #D69E2E   │
│  Deep Teal      Vibrant Teal   Ice Mint Mist  Pure White     Golden    │
│  (Primária)     (Acentos)      (Fundo Claro)  (Cards)        (Métricas)│
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Cores Principais e Semântica

| Papel | Hex | Amostra | Descrição e Aplicação |
| :--- | :--- | :---: | :--- |
| **Primária (Deep Teal)** | `#234E52` | 🟢 | Cor institucional da Carol. Usada em títulos principais, cabeçalhos de destaque, bordas estruturais e contraste nobre. |
| **Secundária (Vibrant Teal)** | `#319795` | 🟢 | Cor de ação, vida e movimento. Usada em botões primários, ícones ativos, badges de status, links e sublinhados. |
| **Destaque Solar (Golden Ochre)** | `#D69E2E` | 🟡 | Cor de calor e atenção sutil. Usada em números de destaque (estatísticas, idade do colágeno, prazos) e marcadores solares. |
| **Destaque Terra (Warm Bronze)** | `#744210` | 🟤 | Texto de alto contraste sobre cartões solares ou alertas pedagógicos gentis. |
| **Acento Claro (Soft Mint)** | `#B2F5EA` | 🟢 | Fundo de pills, badges e destaques secundários com texto em `#234E52`. |
| **Ice Seafoam (Wash)** | `#E6FFFA` | ⚪ | Cartões de destaque com efeito de frescor e respiro visual. |

### 2.2 Fundo e Superfícies (Daylight Clean)

| Superfície | Hex | Aplicação |
| :--- | :--- | :--- |
| **Fundo Geral da Página** | `#EFF8F7` / `#F0F7F7` | Gradiente ou sólido ultra-suave com toque de menta claro, reduzindo fadiga ocular e gerando sensação de ar puro. |
| **Superfície de Cards** | `#FFFFFF` | Branco puro com cantos arredondados generosos (`border-radius: 16px` a `24px`) e sombra suave em dispersão (`box-shadow: 0 4px 20px rgba(35, 78, 82, 0.06)`). |
| **Superfície Escura (Night / Deep)** | `#1D4044` / `#234E52` | Usada apenas no slide/seção final de convite à prática ("sthiram sukham asanam / Vamos praticar?") e rodapé imersivo. |

### 2.3 Tipografia e Cores de Texto

| Nível | Hex | Aplicação |
| :--- | :--- | :--- |
| **Texto de Título (Dark Slate)** | `#0F172A` | Títulos H1, H2 e termos fundamentais. Contraste WCAG AAA (13.5:1). |
| **Texto de Subtítulo (Deep Teal)** | `#234E52` | Subtítulos H3, H4, nomes de seções e tags. Contraste WCAG AAA (8.2:1). |
| **Texto de Corpo (Cool Slate)** | `#4A5568` | Parágrafos, explicações e legendas. Contraste WCAG AA (5.4:1). |
| **Texto Suave / Muted** | `#718096` | Metadados, tempo de leitura e notas de rodapé. |

---

## 3. Tipografia Oficial

A tipografia da Carol é **humanista arredondada** (*rounded*), refletindo a ausência de quinas duras, a maleabilidade fascial e a suavidade corporal:

- **Fonte de Títulos (Headings):** `'Nunito'`, sans-serif  
  - Pesos: `700` (Bold) e `800` (ExtraBold)  
  - Características: Terminações arredondadas, proporções amigáveis, tom caloroso e moderno.
- **Fonte de Apoio / Subtítulos Elegantes:** `'Quicksand'`, sans-serif  
  - Pesos: `500` (Medium) e `600` (SemiBold)  
  - Características: Leve, arejada, geométrica suave.
- **Fonte de Corpo (Body):** `'Nunito'` ou `system-ui, -apple-system, sans-serif`  
  - Peso: `400` (Regular) e `600` (SemiBold)  
  - Espaçamento: `line-height: 1.65`, `letter-spacing: -0.01em`

```css
/* Definição de Tokens Tipográficos */
--font-heading: 'Nunito', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-subheading: 'Quicksand', 'Nunito', sans-serif;
--font-body: 'Nunito', system-ui, -apple-system, sans-serif;
```

---

## 4. Iconografia & Simbolismo Visual

Apresentação baseada nos ícones do **Material Symbols** com traço limpo e sem preenchimento excessivo:

- `water_drop` 💧 — O oceano interno (70% líquida / hidratação celular).
- `grid_view` / `layers` 🕸️ — Rede tridimensional contínua e as 3 camadas da fáscia.
- `waves` 🌊 — Viscoelasticidade, fluidez e movimentos ondulatórios/somáticos.
- `favorite` 🤍 — Interocepção, morada das emoções e acolhimento somático.
- `hub` 🌿 — Conectividade sistêmica e tensegridade.
- `spa` / `self_improvement` 🧘 — Ásanas conscientes e Yoga integrativo.

---

## 5. Padrões de Layout e Componentes UI (Design dos Slides)

### 5.1 Anatomia dos Cards nos Slides
1. **Pill de Contexto (Eyebrow Tag):**  
   Caixa alta suave (`font-size: 0.75rem`, `letter-spacing: 0.08em`, cor `#319795` sobre pill `#E6FFFA`).  
   *Exemplo:* `DEFINIÇÃO CIENTÍFICA`, `ORGANIZAÇÃO ANATÔMICA`, `COMPOSIÇÃO FASCIAL`.
2. **Título da Seção:**  
   Fonte Nunito ExtraBold (`#0F172A` ou `#234E52`), tamanho expressivo.
3. **Cartões Modulares em Grid:**  
   Divididos em 2, 3 ou 4 colunas horizontais com cantos arredondados (`16px`), ícone no topo esquerdo com círculo de fundo suave, título em negrito e descrição limpa.
4. **Pill de Abordagem / Ação Prática:**  
   Em cada camada fascial (Slide 8), Carol inclui uma indicação de ação concreta:  
   - *Superficial:* "Abordagem: Rolo e massagem suave"
   - *Intermediária:* "Abordagem: Espreguiçar"
   - *Profunda:* "Abordagem: Balanceio, movimento multidirecional e alongamento dinâmico"
5. **Painel de Métricas de Destaque (Data Callout - Slide 12):**  
   Números grandes (`font-size: 3rem`, cor `#D69E2E`), subtítulo em negrito e parágrafo explicativo sobre a produção de colágeno aos 35 e aos 50 anos.
6. **Tabela de Fluidez Térmica e Mental (Slide 13):**  
   Contraste entre pares biológicos:  
   - *Frio* (aumenta viscosidade / densidade) $\leftrightarrow$ *Calor* (liquefaz a matriz / deslizamento)  
   - *Movimento* (evita congestionamento neural) $\leftrightarrow$ *Meditação* (libera óxido nítrico / relaxamento)

---

## 6. Tom de Voz e Didática (Voz da Carol)

1. **Acolhimento Íntimo:** Começa conectando com o momento presente ("solte o ar com um suspiro", "mãos unidas em frente ao coração", mantra védico de abertura), usa linguagem afetuosa ("mulheres lindas", "gente"), mas sem perder a autoridade científica.
2. **Desmistificação Médica:** Traduz termos anatômicos densos em metáforas intuitivas:  
   - *"A nossa roupa interna"*  
   - *"O sexto órgão dos sentidos: interocepção"*  
   - *"Onde moram as dores e as lesões"*  
   - *"A rede neural como um cristal líquido"*
3. **Regra de Ouro do Movimento:**  
   - Não buscar a rigidez ou a dor.  
   - No ásana: **gerar expansão, nunca contração**.  
   - O corpo é uma teia contínua: mexer o pé afeta a nuca; respirar afeta o quadril.
4. **Respeito ao Tempo do Tecido:**  
   - Fáscia não responde ao impacto rápido; responde à deformação lenta, contínua e consciente (viscoelasticidade e movimentos somáticos).

---

## 7. Tokens CSS Recomendados para a Interface Web

```css
:root {
  /* Cores Principais */
  --carol-deep-teal: #234E52;
  --carol-vibrant-teal: #319795;
  --carol-soft-mint: #B2F5EA;
  --carol-ice-mint: #E6FFFA;
  --carol-bg-mist: #EFF8F7;
  --carol-bg-alt: #F0F7F7;
  --carol-white: #FFFFFF;

  /* Cores de Acento */
  --carol-amber: #D69E2E;
  --carol-amber-dark: #744210;

  /* Texto */
  --carol-text-title: #0F172A;
  --carol-text-sub: #234E52;
  --carol-text-body: #4A5568;
  --carol-text-muted: #718096;

  /* Tipografia */
  --font-heading: 'Nunito', -apple-system, sans-serif;
  --font-sub: 'Quicksand', 'Nunito', sans-serif;
  --font-body: 'Nunito', system-ui, sans-serif;

  /* Formas & Sombras */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-pill: 9999px;
  --shadow-soft: 0 4px 20px rgba(35, 78, 82, 0.06);
  --shadow-hover: 0 8px 30px rgba(35, 78, 82, 0.12);
  --border-glass: 1px solid rgba(49, 151, 149, 0.15);
}
```
