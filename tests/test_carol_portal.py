import os
import threading
import http.server
import socketserver
import pytest
from playwright.sync_api import sync_playwright

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # Silenciar logs normais de requisição

@pytest.fixture(scope="module")
def local_server():
    handler = CustomHTTPHandler
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as httpd:
        port = httpd.server_address[1]
        server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        server_thread.start()
        yield f"http://127.0.0.1:{port}"
        httpd.shutdown()

def test_portal_carol_full_experience(local_server):
    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        page.goto(f"{local_server}/index.html", wait_until="networkidle")

        # 1. Título e Identidade
        title = page.title()
        assert "Carol Langowski" in title
        assert "Cura pelo Movimento" in title

        # 2. Imagens Oficiais Carregadas
        images = [
            "./assets/img/logo-cura-pelo-movimento.png",
            "./assets/img/sistema-fascial-corpo-luminoso.png",
            "./assets/img/aquarela-interocepcao.png",
            "./assets/img/diagrama-tres-camadas-fasciais.png",
            "./assets/img/aquarela-trikonasana-expansao.png"
        ]
        for img_src in images:
            width = page.evaluate(
                """(src) => {
                    const el = document.querySelector(`img[src="${src}"]`);
                    return el ? el.naturalWidth : 0;
                }""",
                img_src
            )
            assert width > 0, f"Imagem não carregou corretamente: {img_src}"

        # 3. Interação das Abas das 3 Camadas
        tab_interm = page.locator('[data-camada-tab="intermediaria"]')
        tab_interm.click()
        assert tab_interm.get_attribute("aria-selected") == "true"
        pane_interm = page.locator('[data-camada-pane="intermediaria"]')
        assert pane_interm.is_visible()
        assert "Espreguiçar" in pane_interm.inner_text()

        # 4. Mini-Laboratório 1: Disco de Algodão
        btn_cotton = page.locator('[data-cotton-step="2"]')
        btn_cotton.click()
        visual_text = page.locator("#cotton-interactive-visual").inner_text()
        assert "gotinhas de orvalho" in visual_text

        # 5. Mini-Laboratório 2: Teste da Torção na Cadeira
        steps = page.locator(".torcao-step-item")
        assert steps.count() == 5
        for i in range(5):
            steps.nth(i).click()

        feedback = page.locator("#torcao-feedback-box")
        assert feedback.is_visible()
        assert "Incrível" in feedback.inner_text()

        # 6. Ritual do Suspiro
        btn_suspiro = page.locator("#btn-play-suspiro")
        btn_suspiro.click()
        assert "Pausar" in btn_suspiro.inner_text()

        # 7. Responsividade & Imunidade a Overflow Horizontal em 4 Viewports (1440, 768, 390, 320)
        viewports = [
            {"width": 1440, "height": 900},
            {"width": 768, "height": 1024},
            {"width": 390, "height": 844},
            {"width": 320, "height": 568}
        ]
        for vp in viewports:
            page.set_viewport_size(vp)
            overflow = page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
            assert not overflow, f"Overflow horizontal detectado no viewport {vp}"

        # 8. Zero erros de console
        assert len(console_errors) == 0, f"Erros de console detectados: {console_errors}"
        assert len(page_errors) == 0, f"Erros de página detectados: {page_errors}"

        browser.close()
