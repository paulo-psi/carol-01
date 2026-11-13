"""
Script para baixar os binários WOFF2 oficiais do Google Fonts para:
- Caveat (700)
- Quicksand (700)
- Nunito (600, 700)
E gerar as strings Base64 prontas para embutir no SVG.
"""

import urllib.request
import re
import base64
import pathlib

root_dir = pathlib.Path(__file__).parent.parent
output_fonts_py = root_dir / "scripts" / "embedded_fonts.py"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_font_base64(font_family, weight):
    css_url = f"https://fonts.googleapis.com/css2?family={font_family}:wght@{weight}&display=swap"
    req = urllib.request.Request(css_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        css = resp.read().decode("utf-8")
    
    # Encontrar a URL do woff2 latino
    # Procurar por blocos latin
    urls = re.findall(r"url\((https://[^\)]+\.woff2)\)", css)
    if not urls:
        raise Exception(f"Não encontrou woff2 para {font_family} {weight}")
    
    # Pegar o último woff2 (que geralmente é o subset latin principal)
    woff2_url = urls[-1]
    print(f"Baixando {font_family} {weight} de: {woff2_url}")
    
    req_font = urllib.request.Request(woff2_url, headers=headers)
    with urllib.request.urlopen(req_font) as resp_font:
        font_bytes = resp_font.read()
    
    b64 = base64.b64encode(font_bytes).decode("ascii")
    print(f"  -> Concluído ({len(font_bytes)} bytes, {len(b64)} chars base64)")
    return b64

caveat_700_b64 = get_font_base64("Caveat", 700)
quicksand_700_b64 = get_font_base64("Quicksand", 700)

font_css = f"""
@font-face {{
  font-family: 'Caveat';
  font-style: normal;
  font-weight: 700;
  src: url(data:font/woff2;charset=utf-8;base64,{caveat_700_b64}) format('woff2');
}}

@font-face {{
  font-family: 'Quicksand';
  font-style: normal;
  font-weight: 700;
  src: url(data:font/woff2;charset=utf-8;base64,{quicksand_700_b64}) format('woff2');
}}
"""

output_fonts_py.write_text(f'EMBEDDED_FONT_CSS = """{font_css}"""\n', encoding="utf-8")
print(f"Fontes salvas com sucesso em: {output_fonts_py}")
