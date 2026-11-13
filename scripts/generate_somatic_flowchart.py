"""
Gerador do Fluxograma Somático da Aula 1 (Carol Langowski)
Estilo: Sketch / Hand-drawn Watercolor Sanctuary (SVG 1920x1080)
"""

import os
import pathlib
from playwright.sync_api import sync_playwright

root_dir = pathlib.Path(__file__).parent.parent
assets_img_dir = root_dir / "assets" / "img"
assets_img_dir.mkdir(parents=True, exist_ok=True)
svg_output_path = assets_img_dir / "fluxograma-jornada-fascia.svg"
png_output_path = assets_img_dir / "fluxograma-jornada-fascia.png"

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&amp;family=Nunito:wght@400;600;700&amp;family=Quicksand:wght@600;700&amp;display=swap');
      
      .bg { fill: #FAF7F0; }
      .title-main { font-family: 'Quicksand', sans-serif; font-size: 38px; font-weight: 700; fill: #234E52; }
      .title-sub { font-family: 'Caveat', cursive; font-size: 26px; font-weight: 700; fill: #9B457B; }
      .node-title { font-family: 'Quicksand', sans-serif; font-size: 20px; font-weight: 700; fill: #0F172A; }
      .node-desc { font-family: 'Nunito', sans-serif; font-size: 15px; font-weight: 600; fill: #4A5568; line-height: 1.4; }
      .hand-note { font-family: 'Caveat', cursive; font-size: 20px; font-weight: 600; fill: #735645; }
      .badge-text { font-family: 'Quicksand', sans-serif; font-size: 13px; font-weight: 700; fill: #234E52; letter-spacing: 0.05em; }

      /* Nó Dark (Santuário - Nó 8) com contraste AAA garantido */
      .node-dark .node-title { fill: #E6FFFA !important; }
      .node-dark .node-desc { fill: #F0FDFA !important; }
      .node-dark .node-highlight { fill: #A7F3D0 !important; font-weight: 700; }
      .node-dark .badge-text { fill: #FFFFFF !important; }
      .node-dark .hand-note { fill: #5EEAD4 !important; }
    </style>

    <!-- Filtro de Sombras e Textura de Papel Aquarela -->
    <filter id="soft-shadow" x="-8%" y="-8%" width="120%" height="124%">
      <feDropShadow dx="2" dy="8" stdDeviation="12" flood-color="#234E52" flood-opacity="0.06"/>
    </filter>

    <filter id="sketch-glow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#9B457B" flood-opacity="0.12"/>
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
       CABEÇALHO DO MAPA SOMÁTICO
       ====================================================================== -->
  <g transform="translate(960, 75)" text-anchor="middle">
    <rect x="-240" y="-38" width="480" height="32" rx="16" fill="#E6FFFA" stroke="#B2F5EA" stroke-width="1.2" />
    <text y="-17" class="badge-text" text-anchor="middle">🌸 CURA PELO MOVIMENTO • MAPA INTEGRAL DA AULA 1</text>
    <text y="32" class="title-main">A Jornada Somática da Fáscia: Do Suspiro à Biotensegridade</text>
    <text y="68" class="title-sub">"A fáscia precisa de carinho e relaxamento; o músculo faz força, a fáscia desliza." — Carol Langowski</text>
  </g>

  <!-- ======================================================================
       ETAPAS DA JORNADA (8 NÓS ORGÂNICOS)
       ====================================================================== -->

  <!-- NÓ 1: SINTONIZAÇÃO & SUSPIRO (X: 110, Y: 210) -->
  <g transform="translate(110, 210)" filter="url(#soft-shadow)">
    <!-- Moldura Orgânica Sketch -->
    <rect x="0" y="0" width="360" height="180" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 1</text>
    <text x="18" y="70" class="node-title">🌬️ Sintonização &amp; Suspiro</text>
    <text x="18" y="100" class="node-desc">Mãos unidas no coração e canto de</text>
    <text x="18" y="122" class="node-desc">abertura védico (Om Sahana Vavatu).</text>
    <text x="18" y="148" class="node-desc" fill="#287E7C" font-weight="700">➜ Ativa o nervo vago e a hidratação.</text>
    <text x="210" y="32" class="hand-note" transform="rotate(-3, 210, 32)">"Solte o ar com suspiro!"</text>
  </g>

  <!-- SETA 1 -> 2 -->
  <path d="M 470 300 C 510 300, 530 300, 560 300" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 2: A GRANDE TESE (X: 580, Y: 210) -->
  <g transform="translate(580, 210)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="370" height="180" rx="22" fill="#FFFDF8" stroke="#EDE1C9" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#FDF2F8" />
    <text x="53" y="30" class="badge-text" text-anchor="middle" fill="#9B457B">PASSO 2</text>
    <text x="18" y="70" class="node-title">🦴 O Fim do Músculo Isolado</text>
    <text x="18" y="100" class="node-desc">Tese do Dr. Tom Myers: não há 600</text>
    <text x="18" y="122" class="node-desc">músculos, mas 1 músculo contido em</text>
    <text x="18" y="148" class="node-desc" font-weight="700" fill="#735645">mais de 600 bolsões fasciais contínuos.</text>
    <text x="200" y="30" class="hand-note" transform="rotate(2, 200, 30)">"Tudo está conectado!"</text>
  </g>

  <!-- SETA 2 -> 3 -->
  <path d="M 950 300 C 990 300, 1010 300, 1040 300" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 3: A ROUPA INTERNA (X: 1060, Y: 210) -->
  <g transform="translate(1060, 210)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="370" height="180" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 3</text>
    <text x="18" y="70" class="node-title">👗 O Macacão Fascial (70% Água)</text>
    <text x="18" y="100" class="node-desc">Se puxar a manga no punho, repuxa a</text>
    <text x="18" y="122" class="node-desc">nuca. Metáfora da mexerica e alívio do</text>
    <text x="18" y="148" class="node-desc" font-weight="700" fill="#287E7C">ombro tratando o antebraço e abdômen.</text>
    <text x="220" y="32" class="hand-note" transform="rotate(-2, 220, 32)">"Onde dói ≠ Onde começou"</text>
  </g>

  <!-- SETA 3 -> 4 -->
  <path d="M 1430 300 C 1470 300, 1485 300, 1510 300" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 4: INTEROCEPÇÃO (X: 1530, Y: 210) -->
  <g transform="translate(1530, 210)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="340" height="180" rx="22" fill="#FFFFFF" stroke="#9B457B" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#FDF2F8" />
    <text x="53" y="30" class="badge-text" text-anchor="middle" fill="#9B457B">PASSO 4</text>
    <text x="18" y="70" class="node-title">👁️ Interocepção (8º Sentido)</text>
    <text x="18" y="100" class="node-desc">80% das terminações nervosas livres</text>
    <text x="18" y="122" class="node-desc">da fáscia sentem o corpo por dentro:</text>
    <text x="18" y="148" class="node-desc" font-weight="700" fill="#9B457B">peso, calor, respiração e conforto.</text>
    <text x="190" y="30" class="hand-note" transform="rotate(3, 190, 30)">"A escuta interna!"</text>
  </g>

  <!-- CURVA DE TRANSIÇÃO DO PASSO 4 PARA O PASSO 5 (DA LINHA 1 PARA A LINHA 2) -->
  <path d="M 1700 390 C 1700 480, 1720 530, 1660 550 C 1580 570, 480 470, 360 560 C 310 600, 300 620, 300 640" 
        fill="none" stroke="#9B457B" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-orchid)" />

  <!-- ======================================================================
       LINHA INFERIOR (PASSOS 5, 6, 7 E 8)
       ====================================================================== -->

  <!-- NÓ 5: AS TRÊS CAMADAS (X: 110, Y: 660) -->
  <g transform="translate(110, 660)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="370" height="190" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 5</text>
    <text x="18" y="70" class="node-title">🔬 As Três Camadas Fasciais</text>
    <text x="18" y="98" class="node-desc">1. Superficial (sensores térmicos e dor)</text>
    <text x="18" y="120" class="node-desc">2. Intermediária (algodão doce e orvalho)</text>
    <text x="18" y="142" class="node-desc">3. Profunda (epimísio e transmissão força)</text>
    <text x="18" y="168" class="node-desc" font-weight="700" fill="#287E7C">➜ Descoberta de Guimberteau em Bordeaux.</text>
    <text x="210" y="32" class="hand-note" transform="rotate(-2, 210, 32)">"Gotinhas de orvalho!"</text>
  </g>

  <!-- SETA 5 -> 6 -->
  <path d="M 480 755 C 520 755, 540 755, 570 755" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 6: BIOTENSEGRIDADE & ESPIRAIS (X: 590, Y: 660) -->
  <g transform="translate(590, 660)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="370" height="190" rx="22" fill="#FFFDF8" stroke="#EDE1C9" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#FEFCBF" />
    <text x="53" y="30" class="badge-text" text-anchor="middle" fill="#975A16">PASSO 6</text>
    <text x="18" y="70" class="node-title">🌀 Biotensegridade &amp; Espirais</text>
    <text x="18" y="98" class="node-desc">Ossos flutuam na rede fascial tensa.</text>
    <text x="18" y="120" class="node-desc">Cinco filamentos &amp; geometria em</text>
    <text x="18" y="142" class="node-desc">infinito (∞): movimentos em espiral</text>
    <text x="18" y="168" class="node-desc" font-weight="700" fill="#975A16">destensionam a rede em 3 dimensões.</text>
    <text x="210" y="30" class="hand-note" transform="rotate(3, 210, 30)">"Espaço em 360°!"</text>
  </g>

  <!-- SETA 6 -> 7 -->
  <path d="M 960 755 C 1000 755, 1020 755, 1050 755" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 7: TESTE DA TORÇÃO (X: 1070, Y: 660) -->
  <g transform="translate(1070, 660)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="360" height="190" rx="22" fill="#FFFFFF" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="#E6FFFA" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 7</text>
    <text x="18" y="70" class="node-title">🪑 Mini-Lab: Torção na Cadeira</text>
    <text x="18" y="98" class="node-desc">1. Teste a amplitude inicial pelo olhar.</text>
    <text x="18" y="120" class="node-desc">2. Deslize a pele do abdômen e escápulas.</text>
    <text x="18" y="142" class="node-desc">3. Reteste: ganho súbito de amplitude</text>
    <text x="18" y="168" class="node-desc" font-weight="700" fill="#287E7C">sem dor, sem alongamento mecânico!</text>
    <text x="195" y="32" class="hand-note" transform="rotate(-2, 195, 32)">"A fáscia deslizando!"</text>
  </g>

  <!-- SETA 7 -> 8 -->
  <path d="M 1430 755 C 1470 755, 1490 755, 1520 755" fill="none" stroke="#287E7C" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 8: SANTUÁRIO DA PRÁTICA (X: 1540, Y: 660) -->
  <g transform="translate(1540, 660)" filter="url(#soft-shadow)" class="node-dark">
    <rect x="0" y="0" width="340" height="190" rx="22" fill="#1A3C3F" stroke="#70D3C7" stroke-width="2" />
    <rect x="18" y="14" width="70" height="24" rx="12" fill="rgba(255,255,255,0.18)" />
    <text x="53" y="30" class="badge-text" text-anchor="middle">PASSO 8</text>
    <text x="18" y="70" class="node-title">🤍 sthiram sukham asanam</text>
    <text x="18" y="98" class="node-desc">Postura firme e simultaneamente</text>
    <text x="18" y="120" class="node-desc">doce, confortável e acolhedora.</text>
    <text x="18" y="146" class="node-desc node-highlight">📝 Registro no Diário Somático Privado</text>
    <text x="18" y="168" class="node-desc node-highlight">🖨️ Estudo em papel / Modo Tapete.</text>
    <text x="185" y="30" class="hand-note" transform="rotate(3, 185, 30)">"Durmam com os anjinhos!"</text>
  </g>

  <!-- ======================================================================
       RODAPÉ DO SKETCH
       ====================================================================== -->
  <g transform="translate(960, 1020)" text-anchor="middle">
    <text class="node-desc" fill="#735645">Design System v2.0 • Daylight Sanctuary &amp; Somatic Watercolor • Carol Langowski • Fisioterapia &amp; Yoga Fascial</text>
  </g>
</svg>
"""

svg_output_path.write_text(svg_content, encoding="utf-8")
print(f"SVG salvo em: {svg_output_path}")

# Renderizar para PNG 1920x1080 com Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.set_content(svg_content)
    page.wait_for_timeout(500)
    page.screenshot(path=str(png_output_path), full_page=True)
    browser.close()

print(f"PNG renderizado em: {png_output_path}")
