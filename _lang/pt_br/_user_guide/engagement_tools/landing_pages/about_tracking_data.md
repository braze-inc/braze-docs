---
nav_title: Sobre dados de rastreamento
article_title: Sobre dados de rastreamento de página de destino
description: "Saiba sobre rastreamento e dados anonimizados para páginas de destino no Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Sobre dados de rastreamento de página de destino

> Saiba sobre rastreamento e dados anonimizados para páginas de destino no Braze.

## Métodos de rastreamento

### Web SDK

O SDK da web do Braze é inicializado apenas quando um usuário envia um formulário na página de destino. Antes do envio do formulário, nenhum dado pessoal é coletado e o SDK não rastreia ativamente os usuários. Após a conclusão da inicialização, o SDK não armazena nenhum dado no navegador (como cookies, armazenamento local ou outros).

Quando um formulário é enviado, o SDK coletará os seguintes dados:

- Evento de envio de formulário (nome do evento e hora do envio)
- Dados especificados pela sua equipe no formulário (como nome, e-mail e número de telefone)
- Hora de início da sessão
- ID do dispositivo (um ID único que é gerado, mas não armazenado, para o dispositivo)
- País determinado pelo endereço IP

### Dados anonimizados

Antes que um usuário envie um formulário, os dados rastreados em uma página de destino consistem apenas em informações anonimizadas e não identificáveis. Isso consiste em métricas agregadas padrão de sites, como o número de visualizações de página (impressões) e cliques que uma página de destino recebe.

Como esses dados não estão vinculados a usuários identificáveis, não podem ser usados para redirecionar ou rastrear o comportamento de usuários individuais.

