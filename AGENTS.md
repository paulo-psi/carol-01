# Governança do Workspace: Carol_01

## 1. Visão Geral
- **Objetivo:** Portal web e experiência didática interativa de alto impacto, alinhada à estética, UX, tipografia e estilo pedagógico da Carol, derivada da análise multimodal de seus slides e vídeo de aula.
- **Arquétipo:** `software-app`
- **Stack Prevista:** HTML5 semântico, CSS3 moderno, JavaScript vanilla/modular, Python (suporte à extração e análise de PPTX/mídia).
- **Data de Criação:** 2026-11-13
- **Diretório Raiz dos Sites:** `../` (`C:\Users\Paulo\Antigravity\Sites`)

## 2. Fontes da Verdade (Caminhos Relativos)
- **Estado Atual e Handoff Rápido:** [`./docs/log.md`](./docs/log.md) (leia o topo ao iniciar qualquer sessão)
- **Visão e Escopo:** [`./docs/brief.md`](./docs/brief.md)
- **Plano de Execução:** [`./docs/plan.md`](./docs/plan.md)
- **Design System & Estilo da Carol:** [`./docs/design_system_carol.md`](./docs/design_system_carol.md)
- **Decisões de Arquitetura (ADRs):** [`./docs/adr/`](./docs/adr/)
- **Histórico de Versões:** [`./CHANGELOG.md`](./CHANGELOG.md)

## 3. Regras Operacionais do Projeto
- **Protocolo de Duas Fases:**
  1. *Fase de Análise & Padrão:* Analisar profundamente os slides e o vídeo da aula da Carol, registrar o Design System (paleta, fontes, contrastes, hierarquia, tom de voz e elementos gráficos) em [`./docs/design_system_carol.md`](./docs/design_system_carol.md) e validar com o usuário antes de codar.
  2. *Fase de Implementação HTML:* Codar a interface web com máxima fidelidade estética ao estilo registrado.
- **Caminhos Relativos:** Use sempre caminhos relativos à raiz deste projeto (`./src/`, `./assets/`, `./docs/`).
- **Backups Locais:** Antes de alterações destrutivas em arquivos críticos, salve cópia datada em `./_backup/` (ignorado pelo Git).
- **Diretrizes de Qualidade UI/UX:** Alinhamento estrito com as skills `ui-ux-pro-max`, `frontend-design` e `web-design-guidelines`.
- **Fechamento de Ciclo:** Ao concluir um marco ou antes de encerrar a sessão, execute `/salvar-checkpoint` para atualizar o `Handoff Rápido` em `./docs/log.md` e realizar commit seguro.
