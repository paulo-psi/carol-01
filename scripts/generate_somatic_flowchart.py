"""
Gerador do Fluxograma Somático da Aula 1 (Carol Langowski)
Estilo: Sketch / Hand-drawn Watercolor Sanctuary com Balões de Fala da Carol
Resolução: 1920x1080 Vetorial (SVG e PNG)
"""

import pathlib
from playwright.sync_api import sync_playwright

root_dir = pathlib.Path(__file__).parent.parent
assets_img_dir = root_dir / "assets" / "img"
assets_img_dir.mkdir(parents=True, exist_ok=True)
svg_output_path = assets_img_dir / "fluxograma-jornada-fascia.svg"
png_output_path = assets_img_dir / "fluxograma-jornada-fascia.png"

def make_bubble(x, y, w, text, bg_color="#FFFFFF", border_color="#287E7C", text_color="#134E4A", h=34, r=17):
    """Gera um balão de fala somático unificado com cauda central apontando para o card."""
    hw = w / 2
    tail_w = 16
    tail_h = 8
    thw = tail_w / 2
    path_d = f"M {r} 0 L {w - r} 0 A {r} {r} 0 0 1 {w} {r} A {r} {r} 0 0 1 {w - r} {h} L {hw + thw:.1f} {h} L {hw:.1f} {h + tail_h} L {hw - thw:.1f} {h} L {r} {h} A {r} {r} 0 0 1 0 {r} A {r} {r} 0 0 1 {r} 0 Z"
    return f"""
    <!-- Balão de Fala da Carol -->
    <g transform="translate({x}, {y})" filter="url(#bubble-shadow)">
      <path d="{path_d}" fill="{bg_color}" stroke="{border_color}" stroke-width="1.8" />
      <text x="{hw:.1f}" y="22" class="bubble-text" fill="{text_color}" text-anchor="middle">{text}</text>
    </g>"""

# Gerar balões para os 8 nós
# Linha 1 (Cards em Y=215, Balões em Y=162)
bubble_1 = make_bubble(x=175, y=162, w=230, text='"Solte o ar com suspiro!"', bg_color="#F0FDFA", border_color="#287E7C", text_color="#0F766E")
bubble_2 = make_bubble(x=665, y=162, w=215, text='"Tudo está conectado!"', bg_color="#FFFDF8", border_color="#D97706", text_color="#92400E")
bubble_3 = make_bubble(x=1120, y=162, w=260, text='"Onde dói ≠ Onde começou"', bg_color="#F0FDFA", border_color="#287E7C", text_color="#0F766E")
bubble_4 = make_bubble(x=1615, y=162, w=200, text='"A escuta interna!"', bg_color="#FDF2F8", border_color="#DB2777", text_color="#9D174D")

# Linha 2 (Cards em Y=665, Balões em Y=612)
bubble_5 = make_bubble(x=185, y=612, w=220, text='"Gotinhas de orvalho!"', bg_color="#F0FDFA", border_color="#287E7C", text_color="#0F766E")
bubble_6 = make_bubble(x=685, y=612, w=180, text='"Espaço em 360°!"', bg_color="#FFFDF8", border_color="#D97706", text_color="#92400E")
bubble_7 = make_bubble(x=1140, y=612, w=220, text='"A fáscia deslizando!"', bg_color="#F0FDFA", border_color="#287E7C", text_color="#0F766E")
bubble_8 = make_bubble(x=1590, y=612, w=240, text='"Durmam com os anjinhos!"', bg_color="#1A3C3F", border_color="#70D3C7", text_color="#5EEAD4")

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&amp;family=Nunito:wght@400;600;700&amp;family=Quicksand:wght@600;700&amp;display=swap');
      
      .bg {{ fill: #FAF7F0; }}
      .title-main {{ font-family: 'Quicksand', sans-serif; font-size: 38px; font-weight: 700; fill: #234E52; }}
      .title-sub {{ font-family: 'Caveat', cursive; font-size: 26px; font-weight: 700; fill: #9B457B; }}
      .node-title {{ font-family: 'Quicksand', sans-serif; font-size: 20px; font-weight: 700; fill: #0F172A; }}
      .node-desc {{ font-family: 'Nunito', sans-serif; font-size: 15px; font-weight: 600; fill: #4A5568; line-height: 1.4; }}
      .bubble-text {{ font-family: 'Caveat', cursive; font-size: 21px; font-weight: 700; }}
      .badge-text {{ font-family: 'Quicksand', sans-serif; font-size: 13px; font-weight: 700; fill: #234E52; letter-spacing: 0.05em; }}

      /* Nó Dark (Santuário - Nó 8) com contraste AAA */
      .node-dark .node-title {{ fill: #E6FFFA !important; }}
      .node-dark .node-desc {{ fill: #F0FDFA !important; }}
      .node-dark .node-highlight {{ fill: #A7F3D0 !important; font-weight: 700; }}
      .node-dark .badge-text {{ fill: #FFFFFF !important; }}
    </style>

    <!-- Filtro de Sombras e Textura de Papel Aquarela -->
    <filter id="soft-shadow" x="-8%" y="-8%" width="120%" height="124%">
      <feDropShadow dx="2" dy="8" stdDeviation="12" flood-color="#234E52" flood-opacity="0.06"/>
    </filter>

    <filter id="bubble-shadow" x="-8%" y="-8%" width="120%" height="130%">
      <feDropShadow dx="1" dy="4" stdDeviation="5" flood-color="#234E52" flood-opacity="0.08"/>
    </filter>

    <!-- Marcador de Seta Desenhada à Mão -->
    <marker id="arrow-sketch" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 1 2 C 4 5, 8 6, 11 6 C 8 6, 4 7, 1 10" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>

    <marker id="arrow-orchid" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 1 2 C 4 5, 8 6, 11 6 C 8 6, 4 7, 1 10" fill="none" stroke="#9B457B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <!-- Fundo Texturizado Daylight Sanctuary -->
  <rect width="100%" height="100%" class="bg" />

  <!-- Formas Orgânicas de Fundo (Aquarela Abstrata) -->
  <path d="M -80 120 C 180 -40, 420 80, 520 280 C 620 480, 240 680, 40 620 C -120 580, -200 320, -80 120 Z" fill="#E6FFFA" opacity="0.65" />
  <path d="M 1520 720 C 1720 580, 1980 640, 2020 860 C 2060 1080, 1820 1180, 1640 1120 C 1460 1060, 1380 840, 1520 720 Z" fill="#FDF2F8" opacity="0.75" />
  <circle cx="960" cy="540" r="460" fill="#FFFDF8" opacity="0.9" />

  <!-- ======================================================================
       CABEÇALHO DO MAPA SOMÁTICO (COM RESPIRO VERTICAL REFORÇADO)
       ====================================================================== -->
  <g transform="translate(960, 40)" text-anchor="middle">
    <rect x="-240" y="0" width="480" height="32" rx="16" fill="#E6FFFA" stroke="#B2F5EA" stroke-width="1.2" />
    <text y="21" class="badge-text" text-anchor="middle">🌸 CURA PELO MOVIMENTO • MAPA INTEGRAL DA AULA 1</text>
    <text y="68" class="title-main">A Jornada Somática da Fáscia: Do Suspiro à Biotensegridade</text>
    <text y="104" class="title-sub">"A fáscia precisa de carinho e relaxamento; o músculo faz força, a fáscia desliza." — Carol Langowski</text>
  </g>

  <!-- ======================================================================
       BALÕES DE FALA DA CAROL (LINHA 1)
       ====================================================================== -->
  {bubble_1}
  {bubble_2}
  {bubble_3}
  {bubble_4}

  <!-- ======================================================================
       ETAPAS DA JORNADA (LINHA 1: PASSOS 1 A 4)
       ====================================================================== -->

  <!-- NÓ 1: SINTONIZAÇÃO & SUSPIRO (X: 110, Y: 215) -->
  <g transform="translate(110, 215)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="360" height="185" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 1</text>
    <text x="18" y="68" class="node-title">🌬️ Sintonização &amp; Suspiro</text>
    <text x="18" y="98" class="node-desc">Mãos unidas no coração e canto de</text>
    <text x="18" y="120" class="node-desc">abertura védico (Om Sahana Vavatu).</text>
    <text x="18" y="150" class="node-desc" font-weight="700" fill="#287E7C">➔ Ativa o nervo vago e a hidratação.</text>
  </g>

  <!-- SETA 1 -> 2 -->
  <path d="M 470 305 C 510 305, 530 305, 570 305" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 2: O FIM DO MÚSCULO ISOLADO (X: 590, Y: 215) -->
  <g transform="translate(590, 215)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="365" height="185" rx="22" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#F1F5F9" />
    <text x="53" y="30" class="badge-text" text-anchor="middle" fill="#475569">PASSO 2</text>
    <text x="18" y="68" class="node-title">🦴 O Fim do Músculo Isolado</text>
    <text x="18" y="98" class="node-desc">Tese do Dr. Tom Myers: não há 600</text>
    <text x="18" y="120" class="node-desc">músculos, mas 1 músculo contido em</text>
    <text x="18" y="142" class="node-desc">mais de 600 bolsões fasciais contínuos.</text>
  </g>

  <!-- SETA 2 -> 3 -->
  <path d="M 955 305 C 995 305, 1015 305, 1050 305" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 3: O MACACÃO FASCIAL (X: 1070, Y: 215) -->
  <g transform="translate(1070, 215)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="360" height="185" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 3</text>
    <text x="18" y="68" class="node-title">👗 O Macacão Fascial (70% Água)</text>
    <text x="18" y="98" class="node-desc">Se puxar a manga no punho, repuxa a</text>
    <text x="18" y="120" class="node-desc">nuca. Metáfora da mexerica e alívio do</text>
    <text x="18" y="142" class="node-desc">ombro tratando o antebraço e abdômen.</text>
  </g>

  <!-- SETA 3 -> 4 -->
  <path d="M 1430 305 C 1470 305, 1490 305, 1530 305" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 4: INTEROCEPÇÃO (X: 1550, Y: 215) -->
  <g transform="translate(1550, 215)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="185" rx="22" fill="#FFFFFF" stroke="#F472B6" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#FDF2F8" />
    <text x="53" y="30" class="badge-text" text-anchor="middle" fill="#9B457B">PASSO 4</text>
    <text x="18" y="68" class="node-title">👁️ Interocepção (8º Sentido)</text>
    <text x="18" y="98" class="node-desc">80% das terminações nervosas livres</text>
    <text x="18" y="120" class="node-desc">da fáscia sentem o corpo por dentro:</text>
    <text x="18" y="142" class="node-desc">peso, calor, respiração e conforto.</text>
  </g>

  <!-- SETA CURVA RETORNO: 4 -> 5 (Fluxo Orgânico contornando e entrando na lateral do Passo 5) -->
  <path d="M 1715 400 C 1715 550, 50 510, 50 755 L 100 755" fill="none" stroke="#9B457B" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-orchid)" />

  <!-- ======================================================================
       BALÕES DE FALA DA CAROL (LINHA 2)
       ====================================================================== -->
  {bubble_5}
  {bubble_6}
  {bubble_7}
  {bubble_8}

  <!-- ======================================================================
       LINHA INFERIOR (PASSOS 5 A 8)
       ====================================================================== -->

  <!-- NÓ 5: AS TRÊS CAMADAS FASCIAIS (X: 110, Y: 665) -->
  <g transform="translate(110, 665)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="370" height="190" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 5</text>
    <text x="18" y="68" class="node-title">🔬 As Três Camadas Fasciais</text>
    <text x="18" y="96" class="node-desc">1. Superficial (sensores térmicos e dor)</text>
    <text x="18" y="118" class="node-desc">2. Intermediária (algodão doce e orvalho)</text>
    <text x="18" y="140" class="node-desc">3. Profunda (epimísio e transmissão força)</text>
    <text x="18" y="166" class="node-desc" font-weight="700" fill="#287E7C">➔ Descoberta de Guimberteau em Bordeaux.</text>
  </g>

  <!-- SETA 5 -> 6 -->
  <path d="M 480 760 C 520 760, 540 760, 570 760" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 6: BIOTENSEGRIDADE & ESPIRAIS (X: 590, Y: 665) -->
  <g transform="translate(590, 665)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="370" height="190" rx="22" fill="#FFFDF8" stroke="#EDE1C9" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#FEFCBF" />
    <text x="53" y="30" class="badge-text" text-anchor="middle" fill="#975A16">PASSO 6</text>
    <text x="18" y="68" class="node-title">🌀 Biotensegridade &amp; Espirais</text>
    <text x="18" y="96" class="node-desc">Ossos flutuam na rede fascial tensa.</text>
    <text x="18" y="118" class="node-desc">Cinco filamentos &amp; geometria em</text>
    <text x="18" y="140" class="node-desc">infinito (∞): movimentos em espiral</text>
    <text x="18" y="166" class="node-desc" font-weight="700" fill="#975A16">destensionam a rede em 3 dimensões.</text>
  </g>

  <!-- SETA 6 -> 7 -->
  <path d="M 960 760 C 1000 760, 1020 760, 1050 760" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 7: TESTE DA TORÇÃO (X: 1070, Y: 665) -->
  <g transform="translate(1070, 665)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="360" height="190" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 7</text>
    <text x="18" y="68" class="node-title">🪑 Mini-Lab: Torção na Cadeira</text>
    <text x="18" y="96" class="node-desc">1. Teste a amplitude inicial pelo olhar.</text>
    <text x="18" y="118" class="node-desc">2. Deslize a pele do abdômen e escápulas.</text>
    <text x="18" y="140" class="node-desc">3. Reteste: ganho súbito de amplitude</text>
    <text x="18" y="166" class="node-desc" font-weight="700" fill="#287E7C">sem dor, sem alongamento mecânico!</text>
  </g>

  <!-- SETA 7 -> 8 -->
  <path d="M 1430 760 C 1470 760, 1490 760, 1520 760" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 8: SANTUÁRIO DA PRÁTICA (X: 1540, Y: 665) -->
  <g transform="translate(1540, 665)" filter="url(#soft-shadow)" class="node-dark">
    <rect x="0" y="0" width="340" height="190" rx="22" fill="#1A3C3F" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="rgba(255,255,255,0.18)" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 8</text>
    <text x="18" y="68" class="node-title">🤍 sthiram sukham asanam</text>
    <text x="18" y="96" class="node-desc">Postura firme e simultaneamente</text>
    <text x="18" y="118" class="node-desc">doce, confortável e acolhedora.</text>
    <text x="18" y="144" class="node-desc node-highlight">📝 Registro no Diário Somático Privado</text>
    <text x="18" y="166" class="node-desc node-highlight">🖨️ Estudo em papel &amp; Práticas guiadas.</text>
  </g>

  <!-- ======================================================================
       RODAPÉ DO SKETCH
       ====================================================================== -->
  <g transform="translate(960, 1030)" text-anchor="middle">
    <text class="node-desc" fill="#735645">Cura pelo Movimento • Carol Langowski • Fisioterapia Integrativa &amp; Yoga Fascial</text>
  </g>
</svg>"""

svg_output_path.write_text(svg_content, encoding="utf-8")
print(f"SVG salvo em: {svg_output_path}")

# Renderizar para PNG 1920x1080 com Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.set_content(svg_content)
    page.wait_for_timeout(600)
    page.screenshot(path=str(png_output_path), full_page=True)
    browser.close()

print(f"PNG renderizado em: {png_output_path}")
