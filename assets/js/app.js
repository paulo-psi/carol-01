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
  initAudioCarol();
  initDiarioSomatico();
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

/* 5. Ritual do Suspiro Guiado com Orbe Somático e Timer Circular (Daylight Sanctuary) */
function initBreathingRitual() {
  const triggerBtn = document.getElementById('btn-play-suspiro');
  const widget = document.getElementById('respiracao-widget');
  const ringProgress = document.getElementById('respiracao-ring-progress');
  const badgeEl = document.getElementById('respiracao-fase-badge');
  const timerSecEl = document.getElementById('respiracao-timer-seconds');
  const cicloTextEl = document.getElementById('respiracao-ciclo-text');
  const instrucaoTextEl = document.getElementById('respiracao-instrucao-texto');
  const perolas = document.querySelectorAll('.perola-item');

  if (!triggerBtn || !widget || !ringProgress || !timerSecEl) return;

  const RING_CIRCUMFERENCE = 440;
  const PHASES = [
    {
      name: 'Inspire',
      duration: 4,
      className: 'fase-inspire',
      text: 'Inspira grande pelas narinas... sentindo as costelas se abrirem em 360°.'
    },
    {
      name: 'Sustente',
      duration: 2,
      className: 'fase-sustente',
      text: 'Pausa serena... sinta o espaço e o calor interno acolhedor.'
    },
    {
      name: 'Suspire & Solte',
      duration: 6,
      className: 'fase-suspire',
      text: 'Solta o ar com um longo suspiro... "Ahhh" relaxando peito, ombros e mandíbula.'
    }
  ];

  const TOTAL_CYCLES = 3;
  let isRunning = false;
  let isPaused = false;
  let currentCycle = 1;
  let currentPhaseIndex = 0;
  let remainingSecondsInPhase = 0;
  let tickerTimer = null;

  function updatePerolas(cycle) {
    perolas.forEach((p, idx) => {
      const pCycle = idx + 1;
      p.classList.remove('active', 'completed');
      if (pCycle < cycle) {
        p.classList.add('completed');
      } else if (pCycle === cycle) {
        p.classList.add('active');
      }
    });
  }

  function setPhase(phaseIdx, startFromRemaining = null) {
    currentPhaseIndex = phaseIdx;
    const phase = PHASES[phaseIdx];
    remainingSecondsInPhase = startFromRemaining !== null ? startFromRemaining : phase.duration;

    // Atualizar classes visuais do orbe
    widget.classList.remove('fase-inspire', 'fase-sustente', 'fase-suspire');
    widget.classList.add(phase.className);

    badgeEl.textContent = phase.name;
    timerSecEl.textContent = `${remainingSecondsInPhase}s`;
    cicloTextEl.textContent = `Ciclo ${currentCycle} de ${TOTAL_CYCLES}`;

    instrucaoTextEl.style.opacity = '0';
    setTimeout(() => {
      instrucaoTextEl.textContent = phase.text;
      instrucaoTextEl.style.opacity = '1';
    }, 150);

    updateRingOffset(remainingSecondsInPhase, phase.duration);
  }

  function updateRingOffset(remaining, total) {
    const elapsedRatio = (total - remaining) / total;
    const offset = RING_CIRCUMFERENCE * (1 - elapsedRatio);
    ringProgress.style.strokeDashoffset = offset.toFixed(1);
  }

  function tick() {
    remainingSecondsInPhase--;

    if (remainingSecondsInPhase > 0) {
      timerSecEl.textContent = `${remainingSecondsInPhase}s`;
      const currentPhase = PHASES[currentPhaseIndex];
      updateRingOffset(remainingSecondsInPhase, currentPhase.duration);
    } else {
      // Transição para a próxima fase do ciclo
      const nextPhaseIndex = currentPhaseIndex + 1;
      if (nextPhaseIndex < PHASES.length) {
        setPhase(nextPhaseIndex);
      } else {
        // Concluiu um ciclo de 12s
        if (currentCycle < TOTAL_CYCLES) {
          currentCycle++;
          updatePerolas(currentCycle);
          setPhase(0);
        } else {
          // Concluiu os 3 ciclos com sucesso
          finishBreathing();
        }
      }
    }
  }

  function startBreathing() {
    isRunning = true;
    isPaused = false;
    widget.style.display = 'block';
    widget.setAttribute('aria-hidden', 'false');
    triggerBtn.textContent = '⏸️ Pausar Exercício';
    triggerBtn.setAttribute('aria-pressed', 'true');

    if (currentCycle > TOTAL_CYCLES) {
      currentCycle = 1;
    }
    updatePerolas(currentCycle);
    setPhase(currentPhaseIndex, remainingSecondsInPhase > 0 ? remainingSecondsInPhase : null);

    clearInterval(tickerTimer);
    tickerTimer = setInterval(tick, 1000);
  }

  function pauseBreathing() {
    isPaused = true;
    isRunning = false;
    clearInterval(tickerTimer);
    tickerTimer = null;
    triggerBtn.textContent = '▶ Continuar Exercício';
    triggerBtn.setAttribute('aria-pressed', 'false');
  }

  function finishBreathing() {
    clearInterval(tickerTimer);
    tickerTimer = null;
    isRunning = false;
    isPaused = false;

    widget.classList.remove('fase-inspire', 'fase-sustente', 'fase-suspire');
    badgeEl.textContent = 'Feito com Amor';
    timerSecEl.innerHTML = '🌸';
    cicloTextEl.textContent = '3 Ciclos Concluídos';
    ringProgress.style.strokeDashoffset = '0';
    ringProgress.style.stroke = 'var(--carol-orchid)';

    instrucaoTextEl.innerHTML = '<strong>Muito bem!</strong> Sua rede fascial agradece pelo carinho, relaxamento e hidratação profunda.';
    perolas.forEach(p => {
      p.classList.remove('active');
      p.classList.add('completed');
    });

    triggerBtn.textContent = '🌬️ Praticar Novamente';
    triggerBtn.setAttribute('aria-pressed', 'false');
    currentCycle = 1;
    currentPhaseIndex = 0;
    remainingSecondsInPhase = 0;
  }

  triggerBtn.addEventListener('click', () => {
    if (!isRunning && !isPaused) {
      currentCycle = 1;
      currentPhaseIndex = 0;
      remainingSecondsInPhase = 0;
      startBreathing();
    } else if (isRunning) {
      pauseBreathing();
    } else if (isPaused) {
      startBreathing();
    }
  });
}

/* 6. Pílula de Áudio da Carol (Sintonização Afetuosa) */
function initAudioCarol() {
  const audioEl = document.getElementById('audio-sintonizacao');
  const audioBtn = document.getElementById('btn-audio-carol');
  if (!audioEl || !audioBtn) return;

  audioBtn.addEventListener('click', () => {
    if (audioEl.paused) {
      audioEl.play().then(() => {
        audioBtn.innerHTML = '⏸️ Pausar Voz da Carol';
        audioBtn.setAttribute('aria-pressed', 'true');
      }).catch(err => {
        console.warn('Reprodução de áudio prevenida pelo navegador:', err);
      });
    } else {
      audioEl.pause();
      audioBtn.innerHTML = '▶ Ouvir Sintonização &amp; Mantra (58s)';
      audioBtn.setAttribute('aria-pressed', 'false');
    }
  });

  audioEl.addEventListener('ended', () => {
    audioBtn.innerHTML = '▶ Ouvir Sintonização &amp; Mantra (58s)';
    audioBtn.setAttribute('aria-pressed', 'false');
  });
}

/* 7. Diário Somático da Aluna (Persistência Local) */
function initDiarioSomatico() {
  const textarea = document.getElementById('diario-textarea');
  const statusBadge = document.getElementById('diario-status');
  const btnLimpar = document.getElementById('btn-limpar-diario');
  if (!textarea) return;

  const savedText = localStorage.getItem('carol_diario_aula1');
  if (savedText) {
    textarea.value = savedText;
    if (statusBadge) {
      statusBadge.textContent = '✓ Anotações restauradas';
      statusBadge.classList.add('saved');
    }
  }

  let saveTimeout = null;
  textarea.addEventListener('input', () => {
    if (statusBadge) {
      statusBadge.textContent = 'Salvando...';
      statusBadge.classList.remove('saved');
    }
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(() => {
      localStorage.setItem('carol_diario_aula1', textarea.value);
      if (statusBadge) {
        statusBadge.textContent = '✓ Salvo no seu aparelho';
        statusBadge.classList.add('saved');
      }
    }, 400);
  });

  if (btnLimpar) {
    btnLimpar.addEventListener('click', () => {
      if (window.confirm('Deseja limpar suas anotações deste diário?')) {
        textarea.value = '';
        localStorage.removeItem('carol_diario_aula1');
        if (statusBadge) {
          statusBadge.textContent = 'Anotação limpa';
          statusBadge.classList.remove('saved');
        }
      }
    });
  }
}
