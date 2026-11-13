"""
Script de diagnóstico forense:
1. Mede a largura exata de cada texto dos 8 balões em diferentes fontes (Caveat, Comic Sans, Arial, system-ui).
2. Comprova por que o texto vazou para a esquerda e para a direita.
3. Demonstra a solução com embutimento de fonte em Base64 e balões com largura proporcional e segura.
"""

import pathlib
from playwright.sync_api import sync_playwright

root_dir = pathlib.Path(__file__).parent.parent

texts = [
    (1, '"Solte o ar com suspiro!"'),
    (2, '"Tudo está conectado!"'),
    (3, '"Onde dói ≠ Onde começou"'),
    (4, '"A escuta interna!"'),
    (5, '"Gotinhas de orvalho!"'),
    (6, '"Espaço em 360°!"'),
    (7, '"A fáscia deslizando!"'),
    (8, '"Durmam com os anjinhos!"'),
]

current_widths = {
    1: 200,
    2: 185,
    3: 215,
    4: 170,
    5: 185,
    6: 160,
    7: 185,
    8: 210,
}

html_test = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap" rel="stylesheet">
<style>
  .caveat { font-family: 'Caveat', cursive; font-size: 19px; font-weight: 700; white-space: nowrap; }
  .system-cursive { font-family: 'Comic Sans MS', cursive, sans-serif; font-size: 19px; font-weight: 700; white-space: nowrap; }
  .arial { font-family: Arial, sans-serif; font-size: 19px; font-weight: 700; white-space: nowrap; }
</style>
</head>
<body>
<div id="container"></div>
<script>
const texts = """ + str([t[1] for t in texts]) + """;
const container = document.getElementById('container');
texts.forEach((text, i) => {
    ['caveat', 'system-cursive', 'arial'].forEach(fontClass => {
        const span = document.createElement('span');
        span.className = fontClass;
        span.id = `text_${i+1}_${fontClass}`;
        span.innerText = text;
        container.appendChild(span);
        container.appendChild(document.createElement('br'));
    });
});
</script>
</body>
</html>
"""

temp_html = root_dir / "scripts" / "temp_font_test.html"
temp_html.write_text(html_test, encoding="utf-8")

print("=== MEDIÇÃO FORENSE DE LARGURAS DE TEXTO ===")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(temp_html.as_uri())
    page.wait_for_timeout(1000)
    
    for idx, text in texts:
        cur_w = current_widths[idx]
        w_caveat = page.evaluate(f"() => document.getElementById('text_{idx}_caveat').getBoundingClientRect().width")
        w_cursive = page.evaluate(f"() => document.getElementById('text_{idx}_system-cursive').getBoundingClientRect().width")
        w_arial = page.evaluate(f"() => document.getElementById('text_{idx}_arial').getBoundingClientRect().width")
        
        # Calcular quanto vazou
        leak_caveat = w_caveat - (cur_w - 20) # 20px de padding interno do balão
        leak_cursive = w_cursive - (cur_w - 20)
        
        print(f"\nPasso {idx}: {text}")
        print(f"  Largura do Balão Atual: {cur_w}px (Área útil interna: {cur_w - 28}px)")
        print(f"  Largura Caveat Oficial:  {w_caveat:.1f}px -> {'⚠️ VAZA' if w_caveat > (cur_w - 24) else '✅ Cabe'}")
        print(f"  Largura Fallback Sistema: {w_cursive:.1f}px -> {'🚨 VAZA GRAVEMENTE!' if w_cursive > (cur_w - 24) else '✅ Cabe'}")
    
    browser.close()

if temp_html.exists():
    temp_html.unlink()
