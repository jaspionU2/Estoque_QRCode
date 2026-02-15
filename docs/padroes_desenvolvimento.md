# Padrões de Desenvolvimento iDevs

## 1. Arquitetura Frontend
- **Componentes**: Devem ser funcionais, utilizando Hooks.
- **Estilização**: Uso de variáveis CSS para temas (Dark/Light).
- **Serviços**: Camada de API isolada em `src/services`.
- **Tipagem**: TypeScript obrigatório para todas as interfaces de dados.

## 2. Comunicação com Backend
- Todas as requisições devem incluir o token JWT no cabeçalho `Authorization: Bearer <token>` após o login.
- Tratamento global de erros 401 (Unauthorized) no Axios.

## 3. Experiência do Usuário (UX)
- Design Responsivo (Desktop e Mobile para leitura de QR Code).
- Micro-animações para transições de estado.
- Feedback visual imediato em ações de CRUD.

## 4. Segurança (Bernardo)
- Sanitização de inputs no frontend.
- Não armazenar senhas em cache local.
- Validar permissões de rota com base no payload do JWT.
