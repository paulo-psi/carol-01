"""
Auditoria de Viewports & Responsividade com Playwright
Testa 8 resoluções críticas e captura evidências visuais completas.
"""

import pathlib
from playwright.sync_api import sync_playwright

root_dir = pathlib.Path(__file__).parent.parent
site_path = root_dir / "index.html"
site_url = site_path.as_uri()

artifact_dir = pathlib.Path(r"C:\Users\Paulo\.gemini\antigravity\brain\de041e0c-bcea-400b-b81a-f4e2df23cc7b")
screens_dir = artifact_dir / "viewport_audit"
screens_dir.mkdir(parents=True, exist_ok=True)

viewports = [
    ("desktop_1920", 1920, 1080, "Desktop Full HD"),
    ("macbook_1440", 1440, 900, "MacBook / Desktop Compacto"),
    ("laptop_1366", 1366, 768, "Laptop 1366x768"),
    ("ipad_landscape_1024", 1024, 768, "iPad Paisagem 1024x768"),
    ("ipad_portrait_768", 768, 1024, "iPad Retrato 768x1024"),
    ("iphone14_390", 390, 844, "iPhone 13/14/15 (390x844)"),
    ("galaxy_360", 360, 740, "Galaxy Padrão (360x740)"),
    ("small_320", 320, 568, "Mobile Compacto (320x568)"),
]

print("=== INICIANDO AUDITORIA DE VIEWPORTS ===")

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, w, h, desc in viewports:
        page = browser.new_page(viewport={"width": w, "height": h})
        page.goto(site_url)
        page.wait_for_timeout(500)
        
        # Testar overflow horizontal
        scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
        inner_w = page.evaluate("() => window.innerWidth")
        has_overflow = scroll_w > inner_w
        
        # Inspecionar mapa da jornada
        mapa_box = page.locator("#mapa-jornada").bounding_box()
        navbar_box = page.locator("header.navbar-sanctuary").bounding_box()
        
        # Screenshot do topo e do mapa
        top_shot = screens_dir / f"{name}_top.png"
        page.screenshot(path=str(top_shot), full_page=False)
        
        # Rolar até o mapa da jornada e capturar
        mapa_el = page.locator("#mapa-jornada")
        mapa_el.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        mapa_shot = screens_dir / f"{name}_mapa.png"
        page.screenshot(path=str(mapa_shot), full_page=False)
        
        status = "⚠️ OVERFLOW!" if has_overflow else "✅ OK"
        print(f"[{status}] {desc:28} | {w}x{h} | scrollWidth={scroll_w} innerWidth={inner_w}")
        
    browser.close()

print(f"\nScreenshots salvos em: {screens_dir}")
