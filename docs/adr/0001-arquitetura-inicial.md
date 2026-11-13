# ADR 0001: Estrutura e Arquitetura Inicial do Projeto

- **Data:** 2026-11-13
- **Status:** Aceito

## Contexto
O projeto **Sites/Carol_01** foi iniciado com o objetivo: *Portal web e experiencia didatica interativa alinhada ao design, UX e estilo da Carol a partir da analise de slides e video*.

## Decisão
Adotar o arquétipo `software-app` dentro do padrão Governança V4.5 do Antigravity 2.0, utilizando a stack `HTML5, CSS3, JavaScript, Python`.

## Consequências
- Memória persistente concentrada em `./docs/log.md` (seção Handoff Rápido).
- Snapshots locais isolados em `./_backup/` (fora do controle de versão Git).
