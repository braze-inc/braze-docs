---
nav_title: Eventos personalizados efêmeros
permalink: /ephemeral_custom_events/
hidden: true
page_type: reference
---

# Eventos personalizados efêmeros

- Os eventos personalizados efêmeros não devem incluir eventos de compra ou de início e fim de sessão (conforme descrito na documentação do Braze).
- O Braze não transmitirá e armazenará os eventos personalizados como pontos de dados no Braze para até 12 posicionamentos/nomes de eventos por implementação do SDK.
- A solução Eventos efêmeros será implementada nos SDKs de produção da Braze para iOS e Android, e em quaisquer SDKs de produção futuros da Braze para plataformas para as quais a Braze tenha ativado a solução de Eventos personalizados efêmeros. Isso garante que o cliente possa usar esses SDKs de produção e não perca a sincronização com futuros recursos e correções de bugs. Isso também garante que o cliente possa aproveitar as futuras atualizações do SDK sem a necessidade de outros processos personalizados.
<!--
Keep this doc available on the docs site with the above permalink until 1/21/2026. This feature was built as a one-off page for a customer. Reach out to Rod Amies with questions, if needed.
-->
