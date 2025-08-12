---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artigo contém notas de versão para abril de 2019."
---

# Abril de 2019

## Eventos e campos da New Currents

Além de algumas correções na seção, um novo [Evento de inscrição]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) foi adicionado à página Eventos de engajamento com mensagens. 

Agora você pode exportar os dados de alteração de estado do grupo de inscrições da Braze para o [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) e [o mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mParticle/mparticle_for_currents/), bem como para os eventos de atribuição de instalação no [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

Além disso, a propriedade `canvas_step_id` foi adicionada aos [eventos de conversão]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) disponíveis.

{% alert important %}
Para aproveitar essas atualizações, será necessário editar as configurações do conector do Currents e ativar os eventos que deseja usar. Entre em contato com seu gerente de conta se tiver alguma dúvida.
{% endalert %}

## Arquivamento de grupos de inscrições

Agora você pode [arquivar grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Os grupos de inscrições arquivados não podem ser editados e não aparecerão mais nos filtros de segmentos.  Se tentar arquivar um grupo que esteja sendo usado como Filtro de segmento em qualquer e-mail, campanha ou Canva, você receberá uma mensagem de erro que o impedirá de arquivar o grupo até que remova todos os usos dele.
