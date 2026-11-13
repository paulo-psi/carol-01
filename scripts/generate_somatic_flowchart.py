"""
Gerador do Fluxograma Somático da Aula 1 (Carol Langowski)
Estilo: Minimalista, Clean, Daylight Sanctuary com Balões Orgânicos e Amplo Respiro Periférico
Resolução: 1920x1080 Vetorial (SVG e PNG)
"""

import pathlib
import sys
from playwright.sync_api import sync_playwright

root_dir = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(root_dir / "scripts"))
try:
    from embedded_fonts import EMBEDDED_FONT_CSS
except ImportError:
    EMBEDDED_FONT_CSS = ""

assets_img_dir = root_dir / "assets" / "img"
assets_img_dir.mkdir(parents=True, exist_ok=True)
svg_output_path = assets_img_dir / "fluxograma-jornada-fascia.svg"
png_output_path = assets_img_dir / "fluxograma-jornada-fascia.png"

def make_bubble(center_x, y, w, text, bg_color="#FFFFFF", border_color="#287E7C", text_color="#134E4A", h=34, r=17):
    """Gera um balão de fala somático unificado com cauda central apontando para o card."""
    x = center_x - (w / 2)
    hw = w / 2
    tail_w = 14
    tail_h = 7
    thw = tail_w / 2
    path_d = f"M {r} 0 L {w - r} 0 A {r} {r} 0 0 1 {w} {r} A {r} {r} 0 0 1 {w - r} {h} L {hw + thw:.1f} {h} L {hw:.1f} {h + tail_h} L {hw - thw:.1f} {h} L {r} {h} A {r} {r} 0 0 1 0 {r} A {r} {r} 0 0 1 {r} 0 Z"
    return f"""
    <!-- Balão de Fala da Carol -->
    <g transform="translate({x:.1f}, {y})" filter="url(#bubble-shadow)">
      <path d="{path_d}" fill="{bg_color}" stroke="{border_color}" stroke-width="1.4" />
      <text x="{hw:.1f}" y="18" dominant-baseline="middle" class="bubble-text" fill="{text_color}" text-anchor="middle">{text}</text>
    </g>"""

# Centros exatos dos cards:
# Card 1: 325.0 | Card 2: 748.3 | Card 3: 1171.7 | Card 4: 1595.0
# Larguras ampliadas com folga de segurança total contra transbordamento:
bubble_1 = make_bubble(center_x=325.0, y=172, w=260, text='"Solte o ar com suspiro!"', bg_color="#F0FDFA", border_color="#319795", text_color="#0F766E")
bubble_2 = make_bubble(center_x=748.3, y=172, w=260, text='"Tudo está conectado!"', bg_color="#FFFDF8", border_color="#D97706", text_color="#92400E")
bubble_3 = make_bubble(center_x=1171.7, y=172, w=290, text='"Onde dói ≠ Onde começou"', bg_color="#F0FDFA", border_color="#319795", text_color="#0F766E")
bubble_4 = make_bubble(center_x=1595.0, y=172, w=240, text='"A escuta interna!"', bg_color="#FDF2F8", border_color="#DB2777", text_color="#9D174D")

bubble_5 = make_bubble(center_x=325.0, y=612, w=260, text='"Gotinhas de orvalho!"', bg_color="#F0FDFA", border_color="#319795", text_color="#0F766E")
bubble_6 = make_bubble(center_x=748.3, y=612, w=240, text='"Espaço em 360°!"', bg_color="#FFFDF8", border_color="#D97706", text_color="#92400E")
bubble_7 = make_bubble(center_x=1171.7, y=612, w=260, text='"A fáscia deslizando!"', bg_color="#F0FDFA", border_color="#319795", text_color="#0F766E")
bubble_8 = make_bubble(center_x=1595.0, y=612, w=270, text='"Durmam com os anjinhos!"', bg_color="#1A3C3F", border_color="#5EEAD4", text_color="#E6FFFA")

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&amp;family=Nunito:wght@400;600;700&amp;family=Quicksand:wght@600;700&amp;display=swap');
      
      {EMBEDDED_FONT_CSS}
      
      .bg {{ fill: #FAF7F0; }}
      .title-main {{ font-family: 'Quicksand', system-ui, sans-serif; font-size: 34px; font-weight: 700; fill: #234E52; }}
      .title-sub {{ font-family: 'Caveat', cursive, sans-serif; font-size: 20px; font-weight: 700; fill: #823866; }}
      .node-title {{ font-family: 'Quicksand', system-ui, sans-serif; font-size: 18px; font-weight: 700; fill: #0F172A; }}
      .node-desc {{ font-family: 'Nunito', system-ui, sans-serif; font-size: 13.5px; font-weight: 600; fill: #4A5568; line-height: 1.45; }}
      .bubble-text {{ font-family: 'Caveat', cursive, sans-serif; font-size: 19px; font-weight: 700; }}
      .badge-text {{ font-family: 'Quicksand', system-ui, sans-serif; font-size: 11.5px; font-weight: 700; fill: #234E52; letter-spacing: 0.06em; }}

      /* Nó Dark (Santuário - Nó 8) com contraste AAA */
      .node-dark .node-title {{ fill: #E6FFFA !important; }}
      .node-dark .node-desc {{ fill: #F0FDFA !important; }}
      .node-dark .node-highlight {{ fill: #A7F3D0 !important; font-weight: 700; }}
      .node-dark .badge-text {{ fill: #FFFFFF !important; }}
    </style>

    <!-- Filtro de Sombras e Textura de Papel Aquarela -->
    <filter id="soft-shadow" x="-8%" y="-8%" width="120%" height="124%">
      <feDropShadow dx="2" dy="6" stdDeviation="10" flood-color="#234E52" flood-opacity="0.05"/>
    </filter>

    <filter id="bubble-shadow" x="-8%" y="-8%" width="120%" height="130%">
      <feDropShadow dx="1" dy="3" stdDeviation="4" flood-color="#234E52" flood-opacity="0.07"/>
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

  <!-- Formas Orgânicas de Fundo (Aquarela Suave & Minimalista) -->
  <path d="M -80 120 C 180 -40, 420 80, 520 280 C 620 480, 240 680, 40 620 C -120 580, -200 320, -80 120 Z" fill="#E6FFFA" opacity="0.45" />
  <path d="M 1520 720 C 1720 580, 1980 640, 2020 860 C 2060 1080, 1820 1180, 1640 1120 C 1460 1060, 1380 840, 1520 720 Z" fill="#FDF2F8" opacity="0.5" />
  <circle cx="960" cy="540" r="460" fill="#FFFDF8" opacity="0.75" />

  <!-- ======================================================================
       CABEÇALHO DO MAPA SOMÁTICO (COM RESPIRO VERTICAL REFORÇADO)
       ====================================================================== -->
  <g transform="translate(960, 40)" text-anchor="middle">
    <rect x="-230" y="0" width="460" height="28" rx="14" fill="#E6FFFA" stroke="#B2F5EA" stroke-width="1.2" />
    <text y="19" class="badge-text" text-anchor="middle">🌸 CURA PELO MOVIMENTO • MAPA INTEGRAL DA AULA 1</text>
    <text y="58" class="title-main">A Jornada Somática da Fáscia: Do Suspiro à Biotensegridade</text>
    <text y="90" class="title-sub">"A fáscia precisa de carinho e relaxamento; o músculo faz força, a fáscia desliza." — Carol Langowski</text>
  </g>

  <!-- ======================================================================
       BALÕES DE FALA DA CAROL (LINHA 1)
       ====================================================================== -->
  {bubble_1}
  {bubble_2}
  {bubble_3}
  {bubble_4}

  <!-- ======================================================================
       ETAPAS DA JORNADA (LINHA 1: PASSOS 1 A 4 - LARGURA: 330px, GAPS: 93px)
       ====================================================================== -->

  <!-- NÓ 1: SINTONIZAÇÃO & SUSPIRO (X: 160, Y: 220) -->
  <g transform="translate(160, 220)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFFFF" stroke="#70D3C7" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#E6FFFA" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle">PASSO 1</text>
    <text x="18" y="66" class="node-title">🌬️ Sintonização &amp; Suspiro</text>
    <text x="18" y="94" class="node-desc">Mãos unidas no coração e canto de</text>
    <text x="18" y="115" class="node-desc">abertura védico (Om Sahana Vavatu).</text>
    <text x="18" y="144" class="node-desc" font-weight="700" fill="#287E7C">➔ Ativa o nervo vago e a hidratação.</text>
  </g>

  <!-- SETA 1 -> 2 (Comprimento: 88px) -->
  <path d="M 490 307.5 L 575 307.5" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-dasharray="5,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 2: O FIM DO MÚSCULO ISOLADO (X: 583.3, Y: 220) -->
  <g transform="translate(583.3, 220)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#F1F5F9" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle" fill="#475569">PASSO 2</text>
    <text x="18" y="66" class="node-title">🦴 O Fim do Músculo Isolado</text>
    <text x="18" y="94" class="node-desc">Tese do Dr. Tom Myers: não há 600</text>
    <text x="18" y="115" class="node-desc">músculos, mas 1 músculo contido em</text>
    <text x="18" y="136" class="node-desc">mais de 600 bolsões fasciais contínuos.</text>
  </g>

  <!-- SETA 2 -> 3 (Comprimento: 88px) -->
  <path d="M 913.3 307.5 L 998.7 307.5" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-dasharray="5,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 3: O MACACÃO FASCIAL (X: 1006.7, Y: 220) -->
  <g transform="translate(1006.7, 220)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFFFF" stroke="#70D3C7" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#E6FFFA" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle">PASSO 3</text>
    <text x="18" y="66" class="node-title">👗 O Macacão Fascial (70% Água)</text>
    <text x="18" y="94" class="node-desc">Se puxar a manga no punho, repuxa a</text>
    <text x="18" y="115" class="node-desc">nuca. Metáfora da mexerica e alívio do</text>
    <text x="18" y="136" class="node-desc">ombro tratando o antebraço e abdômen.</text>
  </g>

  <!-- SETA 3 -> 4 (Comprimento: 88px) -->
  <path d="M 1336.7 307.5 L 1422 307.5" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-dasharray="5,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 4: INTEROCEPÇÃO (X: 1430, Y: 220) -->
  <g transform="translate(1430, 220)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFFFF" stroke="#F472B6" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#FDF2F8" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle" fill="#9B457B">PASSO 4</text>
    <text x="18" y="66" class="node-title">👁️ Interocepção (8º Sentido)</text>
    <text x="18" y="94" class="node-desc">80% das terminações nervosas livres</text>
    <text x="18" y="115" class="node-desc">da fáscia sentem o corpo por dentro:</text>
    <text x="18" y="136" class="node-desc">peso, calor, respiração e conforto.</text>
  </g>

  <!-- SETA CURVA RETORNO: 4 -> 5 (Fluxo Curvo com Respiro Amplo) -->
  <path d="M 1595 395 C 1595 530, 80 500, 80 747.5 L 150 747.5" fill="none" stroke="#9B457B" stroke-width="2.2" stroke-dasharray="6,4" marker-end="url(#arrow-orchid)" />

  <!-- ======================================================================
       BALÕES DE FALA DA CAROL (LINHA 2)
       ====================================================================== -->
  {bubble_5}
  {bubble_6}
  {bubble_7}
  {bubble_8}

  <!-- ======================================================================
       LINHA INFERIOR (PASSOS 5 A 8 - LARGURA: 330px, GAPS: 93px)
       ====================================================================== -->

  <!-- NÓ 5: AS TRÊS CAMADAS FASCIAIS (X: 160, Y: 660) -->
  <g transform="translate(160, 660)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFFFF" stroke="#70D3C7" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#E6FFFA" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle">PASSO 5</text>
    <text x="18" y="66" class="node-title">🔬 As Três Camadas Fasciais</text>
    <text x="18" y="92" class="node-desc">1. Superficial (sensores térmicos e dor)</text>
    <text x="18" y="113" class="node-desc">2. Intermediária (algodão doce e orvalho)</text>
    <text x="18" y="134" class="node-desc">3. Profunda (epimísio e transmissão força)</text>
    <text x="18" y="156" class="node-desc" font-weight="700" fill="#287E7C">➔ Descoberta de Guimberteau.</text>
  </g>

  <!-- SETA 5 -> 6 (Comprimento: 88px) -->
  <path d="M 490 747.5 L 575 747.5" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-dasharray="5,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 6: BIOTENSEGRIDADE & ESPIRAIS (X: 583.3, Y: 660) -->
  <g transform="translate(583.3, 660)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFDF8" stroke="#EDE1C9" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#FEFCBF" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle" fill="#975A16">PASSO 6</text>
    <text x="18" y="66" class="node-title">🌀 Biotensegridade &amp; Espirais</text>
    <text x="18" y="92" class="node-desc">Ossos flutuam na rede fascial tensa.</text>
    <text x="18" y="113" class="node-desc">Cinco filamentos &amp; geometria em</text>
    <text x="18" y="134" class="node-desc">infinito (∞): movimentos em espiral</text>
    <text x="18" y="156" class="node-desc" font-weight="700" fill="#975A16">destensionam em 3 dimensões.</text>
  </g>

  <!-- SETA 6 -> 7 (Comprimento: 88px) -->
  <path d="M 913.3 747.5 L 998.7 747.5" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-dasharray="5,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 7: TESTE DA TORÇÃO (X: 1006.7, Y: 660) -->
  <g transform="translate(1006.7, 660)" filter="url(#soft-shadow)">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#FFFFFF" stroke="#70D3C7" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="#E6FFFA" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle">PASSO 7</text>
    <text x="18" y="66" class="node-title">🪑 Mini-Lab: Torção na Cadeira</text>
    <text x="18" y="92" class="node-desc">1. Teste a amplitude inicial pelo olhar.</text>
    <text x="18" y="113" class="node-desc">2. Deslize a pele do abdômen e escápulas.</text>
    <text x="18" y="134" class="node-desc">3. Reteste: ganho súbito de amplitude</text>
    <text x="18" y="156" class="node-desc" font-weight="700" fill="#287E7C">sem dor, sem forçar o músculo!</text>
  </g>

  <!-- SETA 7 -> 8 (Comprimento: 88px) -->
  <path d="M 1336.7 747.5 L 1422 747.5" fill="none" stroke="#287E7C" stroke-width="2.2" stroke-dasharray="5,4" marker-end="url(#arrow-sketch)" />

  <!-- NÓ 8: SANTUÁRIO DA PRÁTICA (X: 1430, Y: 660) -->
  <g transform="translate(1430, 660)" filter="url(#soft-shadow)" class="node-dark">
    <rect x="0" y="0" width="330" height="175" rx="20" fill="#1A3C3F" stroke="#70D3C7" stroke-width="1.8" />
    <rect x="18" y="14" width="65" height="22" rx="11" fill="rgba(255,255,255,0.18)" />
    <text x="50.5" y="29" class="badge-text" text-anchor="middle">PASSO 8</text>
    <text x="18" y="66" class="node-title">🤍 sthiram sukham asanam</text>
    <text x="18" y="92" class="node-desc">Postura firme e simultaneamente</text>
    <text x="18" y="113" class="node-desc">doce, confortável e acolhedora.</text>
    <text x="18" y="136" class="node-desc node-highlight">📝 Registro no Diário Somático Privado</text>
    <text x="18" y="156" class="node-desc node-highlight">🖨️ Estudo em papel &amp; Práticas guiadas.</text>
  </g>

  <!-- ======================================================================
       RODAPÉ DO SKETCH (COM RESPIRO VERTICAL)
       ====================================================================== -->
  <g transform="translate(960, 995)" text-anchor="middle">
    <text class="node-desc" fill="#735645" font-size="15px">Cura pelo Movimento • Carol Langowski • Fisioterapia Integrativa &amp; Yoga Fascial</text>
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
