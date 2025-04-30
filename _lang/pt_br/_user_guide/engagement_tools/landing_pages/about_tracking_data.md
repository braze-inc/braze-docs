---
nav_title: Sobre o rastreamento de dados
article_title: Sobre os dados de rastreamento da landing page
description: "Saiba mais sobre rastreamento e dados anônimos para landing pages no Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Sobre os dados de rastreamento da landing page

> Saiba mais sobre rastreamento e dados anônimos para landing pages no Braze.

## Métodos de rastreamento

### SDK da Web

O SDK do Braze Web é inicializado somente quando um usuário envia um formulário na landing page. Antes do envio do formulário, nenhum dado pessoal é coletado e o SDK não faz o rastreamento ativo dos usuários. Após a conclusão da inicialização, o SDK não armazena nenhum dado no navegador (como cookies, armazenamento local ou outros).

Quando um formulário for enviado, o SDK coletará os seguintes dados:

- Evento de envio de formulário (nome do evento e horário de envio)
- Dados especificados pela sua equipe no formulário (como nome, e-mail e número de telefone)
- Horário de início da sessão
- ID do dispositivo (uma ID exclusiva que é gerada, mas não armazenada, para o dispositivo)
- País determinado pelo endereço IP

### Dados anônimos

Antes de um usuário enviar um formulário, os dados rastreados em uma landing page consistem apenas em informações anônimas e não identificáveis. Isso consiste em métricas agregadas padrão do site, como o número de visualizações de página (impressões) e cliques que uma landing page recebe.

Como esses dados não estão vinculados a usuários identificáveis, eles não podem ser usados para redirecionar ou rastrear o comportamento individual do usuário.

