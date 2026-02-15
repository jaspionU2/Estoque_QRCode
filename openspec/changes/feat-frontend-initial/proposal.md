# Proposal: Implementação do Frontend do sistema de Estoque QRCode

**ID:** feat-frontend-initial  
**Author:** Ricardo (iDevs)  
**Status:** DRAFT  
**Date:** 2026-02-15  

## 1. Problem Statement
O backend do sistema de estoque de Chromebooks está funcional, mas os usuários não possuem uma interface para realizar operações de login, cadastro de equipamentos, empréstimos e leitura de QRCode portável.

## 2. Proposed Solution
Criar uma Single Page Application (SPA) usando Vite+React+TS que consuma a API FastAPI existente. O design será focado em usabilidade móvel (para escaneamento) e dashboard administrativo.

## 3. Scope
- [ ] Setup do projeto Vite + React + TS.
- [ ] Sistema de Autenticação (Login/Logout) integrado ao JWT do Backend.
- [ ] Dashboard de resumo de estoque.
- [ ] CRUD de Equipamentos (Chromebooks).
- [ ] Fluxo de Empréstimo/Devolução com Leitor de QRCode.
- [ ] Gerenciamento de Usuários e Atribuições.

## 4. Requirements (Deltas)

### Requirement: AUTH-001
#### Scenario: Autenticação de Usuário
O sistema **SHALL** permitir login via email e senha consumindo `/conta/doLogin`.

### Requirement: EQUIP-001
#### Scenario: Cadastro de Equipamento
O sistema **SHALL** permitir adicionar novos chromebooks via `/equipamento/createEquipmanento`.

### Requirement: SCAN-001
#### Scenario: Leitura de QRCode
O sistema **MUST** utilizar a câmera do dispositivo para ler IDs de equipamentos via QRCode.

## 5. Security Review (Bernardo)
- Validação de expiração de token.
- Proteção de rotas privadas.

## 6. QA Review (Beatriz)
- Testes de integração de fluxo de empréstimo.
- Validação visual responsiva.
