---
nav_title: Tealium para Currents
article_title: Tealium para Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a Tealium, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium para Currents

> [A Tealium](https://www.tealium.com) é uma plataforma de dados do cliente que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração da Braze e da Tealium permite que você controle perfeitamente o fluxo de informações entre os dois sistemas. Com o Currents, você também pode conectar dados à Tealium para torná-los acionáveis em todo o growth stack. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Tealium EventStream ou Tealium AudienceStream | É necessário ter uma [conta da Tealium](https://my.tealiumiq.com/) para usar a parceria. |
| Currents | Para exportar dados de volta para o Tealium, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
| URL do Tealium | Isso pode ser obtido navegando até o dashboard da Tealium e copiando o URL de ingestão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Criar uma fonte de dados para o Braze no Tealium

As instruções para a criação de uma fonte de dados podem ser encontradas no site [da Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Quando concluído, a Tealium fornecerá um URL da fonte de dados para uso na próxima etapa.

### Etapa 2: crie um Current

Na Braze, navegue até **Currents > + Criar Currents > Exportação do Tealium**. Forneça um nome de integração, e-mail de contato e o URL da Tealium. Em seguida, selecione o que deseja rastrear na lista de eventos disponíveis. Por fim, clique em **Abrir Current**.

Todos os eventos enviados ao Tealium incluirão o endereço `external_user_id` do usuário. No momento, o Braze não envia dados de eventos para a Tealium para usuários que não têm o endereço `external_user_id` definido.

{% alert important %}
É importante manter seu URL do Tealium atualizado. Se o URL de seu conector estiver incorreto, o Braze não conseguirá enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

## Detalhes da integração

A Braze oferece suporte à exportação de todos os dados listados nos [glossários de eventos do Currents]({{site.baseurl}}/user_guide/data/braze_currents/) (incluindo todas as propriedades dos eventos de [engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) e de [comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)) para a Tealium.

A estrutura de carga útil para dados exportados é a mesma que a estrutura de carga útil para conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).