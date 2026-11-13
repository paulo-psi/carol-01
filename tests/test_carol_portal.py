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

        # 7. Melhoria 1: Pílula de Áudio da Carol (Sintonização Afetuosa)
        audio_el = page.locator("#audio-sintonizacao")
        assert audio_el.count() == 1
        assert "sintonizacao-carol.mp3" in audio_el.get_attribute("src")
        btn_audio = page.locator("#btn-audio-carol")
        assert btn_audio.is_visible()
        btn_audio.click()
        page.wait_for_timeout(300)
        assert btn_audio.get_attribute("aria-pressed") == "true"
        btn_audio.click()
        page.wait_for_timeout(200)
        assert btn_audio.get_attribute("aria-pressed") == "false"

        # 8. Melhoria 2: Modo Ao Lado do Tapete (Tapete Mode & Persistência)
        btn_tapete = page.locator("#btn-toggle-tapete")
        assert btn_tapete.is_visible()
        btn_tapete.click()
        page.wait_for_timeout(200)
        assert page.evaluate("() => document.body.classList.contains('tapete-mode')")
        assert page.evaluate("() => localStorage.getItem('carol_tapete_mode') === 'active'")
        # Desativar e verificar retorno
        btn_tapete.click()
        page.wait_for_timeout(200)
        assert not page.evaluate("() => document.body.classList.contains('tapete-mode')")
        assert page.evaluate("() => localStorage.getItem('carol_tapete_mode') === 'inactive'")

        # 9. Melhoria 3: Glossário Vivo do Corpo (Acordeão <details>)
        glossario_sec = page.locator("#glossario")
        assert glossario_sec.is_visible()
        glossario_items = page.locator(".glossario-item")
        assert glossario_items.count() == 8
        first_item = glossario_items.first
        first_item.locator("summary").click()
        page.wait_for_timeout(200)
        assert first_item.get_attribute("open") is not None
        assert "Biotensegridade" in first_item.locator("summary").inner_text()
        assert "espaçadores flutuantes" in first_item.locator(".glossario-content").inner_text()

        # 9.1 Mapa Somático da Jornada (Fluxograma Sketch em Aquarela)
        mapa_sec = page.locator("#mapa-jornada")
        mapa_sec.scroll_into_view_if_needed()
        assert mapa_sec.is_visible()
        mapa_img = page.locator("#mapa-jornada img")
        assert mapa_img.is_visible()
        assert "fluxograma-jornada-fascia.svg" in mapa_img.get_attribute("src")

        # 10. Melhoria 4: Diário Somático da Aluna (Persistência Local)
        diario_input = page.locator("#diario-textarea")
        assert diario_input.is_visible()
        diario_input.fill("Hoje senti a fáscia do meu pescoço deslizar suavemente após o suspiro!")
        page.wait_for_timeout(600)  # aguardar debounce de 400ms
        status_text = page.locator("#diario-status").inner_text()
        assert "Salvo" in status_text
        saved_storage = page.evaluate("() => localStorage.getItem('carol_diario_aula1')")
        assert "pescoço deslizar" in saved_storage

        # 11. Melhoria 5: Botão de Impressão de Folha de Estudos
        btn_print = page.locator("#btn-print-page")
        assert btn_print.is_visible()

        # 12. Responsividade & Imunidade a Overflow Horizontal em 4 Viewports (1440, 768, 390, 320)
        viewports = [
            {"width": 1440, "height": 900},
            {"width": 768, "height": 1024},
            {"width": 390, "height": 844},
            {"width": 320, "height": 568}
        ]
        for vp in viewports:
            page.set_viewport_size(vp)
            page.wait_for_timeout(200)
            overflow = page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
            assert not overflow, f"Overflow horizontal detectado no viewport {vp}"

        # 13. Zero erros de console
        assert len(console_errors) == 0, f"Erros de console detectados: {console_errors}"
        assert len(page_errors) == 0, f"Erros de página detectados: {page_errors}"

        browser.close()
