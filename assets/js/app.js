/**
 * Cura pelo Movimento • Carol Langowski
 * Script de Interatividade Somática & Encantamento (v2.0)
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollProgress();
  initCamadasTabs();
  initTorcaoMiniLab();
  initCottonMiniLab();
  initBreathingRitual();
});

/* 1. Indicador de Progresso de Leitura */
function initScrollProgress() {
  const bar = document.getElementById('scroll-progress');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (window.scrollY / totalHeight) * 100;
    bar.style.width = `${Math.min(100, Math.max(0, progress))}%`;
  }, { passive: true });
}

/* 2. Abas das Três Camadas Fasciais */
function initCamadasTabs() {
  const tabButtons = document.querySelectorAll('[data-camada-tab]');
  const panes = document.querySelectorAll('[data-camada-pane]');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-camada-tab');

      tabButtons.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      panes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const targetPane = document.querySelector(`[data-camada-pane="${target}"]`);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    });
  });
}

/* 3. Mini-Laboratório 2: Teste Somático de Torção na Cadeira */
function initTorcaoMiniLab() {
  const stepItems = document.querySelectorAll('.torcao-step-item');
  const countDisplay = document.getElementById('torcao-progress-count');
  const completionFeedback = document.getElementById('torcao-feedback-box');

  stepItems.forEach(item => {
    item.addEventListener('click', () => {
      item.classList.toggle('checked');
      updateTorcaoProgress();
    });
  });

  function updateTorcaoProgress() {
    const checkedCount = document.querySelectorAll('.torcao-step-item.checked').length;
    if (countDisplay) {
      countDisplay.textContent = `${checkedCount} de ${stepItems.length} passos concluídos`;
    }
    if (completionFeedback) {
      if (checkedCount === stepItems.length) {
        completionFeedback.style.display = 'block';
      } else {
        completionFeedback.style.display = 'none';
      }
    }
  }
}

/* 4. Mini-Laboratório 1: O Disco de Algodão Doce */
function initCottonMiniLab() {
  const cottonSteps = document.querySelectorAll('[data-cotton-step]');
  const cottonPreview = document.getElementById('cotton-interactive-visual');

  cottonSteps.forEach((step, index) => {
    step.addEventListener('click', () => {
      cottonSteps.forEach(s => s.classList.remove('active'));
      step.classList.add('active');

      if (cottonPreview) {
        const labels = [
          "1. Disco de algodão fechado: A pele e o músculo parecem colados.",
          "2. Puxando com carinho: As fibras se afastam e revelam o algodão doce.",
          "3. A rede viva intermediária: As gotinhas de orvalho (ácido hialurônico) permitem o deslizamento sem atrito."
        ];
        cottonPreview.textContent = labels[index] || labels[0];
      }
    });
  });
}

/* 5. Ritual do Suspiro Guiado (Breathing Wave) */
function initBreathingRitual() {
  const triggerBtn = document.getElementById('btn-play-suspiro');
  const statusText = document.getElementById('suspiro-status-text');
  let breathingInterval = null;

  if (!triggerBtn || !statusText) return;

  triggerBtn.addEventListener('click', () => {
    if (breathingInterval) {
      clearInterval(breathingInterval);
      breathingInterval = null;
      triggerBtn.textContent = '🌬️ Iniciar Respiração Guiada';
      statusText.textContent = 'Clique para praticar 1 ciclo de respiração e suspiro com a Carol.';
      return;
    }

    triggerBtn.textContent = '⏸️ Pausar';
    let phase = 0; // 0: inspira (4s), 1: segura (2s), 2: suspiro (6s)

    const runCycle = () => {
      if (phase === 0) {
        statusText.innerHTML = '<strong>Inspire profundamente...</strong> preenchendo o peito com suavidade.';
        phase = 1;
      } else if (phase === 1) {
        statusText.innerHTML = '<strong>Pausa serena...</strong> sentindo o espaço interno.';
        phase = 2;
      } else {
        statusText.innerHTML = '<strong>Solte o ar com um suspiro...</strong> <em>"Ahhhh..."</em> relaxando ombros e mandíbula.';
        phase = 0;
      }
    };

    runCycle();
    breathingInterval = setInterval(runCycle, 4000);
  });
}
