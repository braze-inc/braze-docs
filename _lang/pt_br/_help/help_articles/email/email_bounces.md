---
nav_title: Envios de e-mail
article_title: Envios de e-mail
page_order: 0
page_type: solution
description: "Este artigo de ajuda esclarece a diferença entre hard bounce e soft bounce."
channel: email
---

# Envios de e-mail

O que fazer quando uma mensagem da sua campanha de mensagens é devolvida pelos endereços de e-mail dos seus usuários? Primeiro, vamos definir e solucionar os problemas dos dois tipos de envios de e-mail: hard bounce e soft bounce. 

## Hard bounce

{% multi_lang_include metrics.md metric='Hard Bounce' %}

Para saber mais, consulte [Hard bounce]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce).

## Soft bounces

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

Se um e-mail receber um soft bounce, geralmente tentaremos novamente dentro de 72 horas, mas o número de tentativas varia de acordo com o destinatário.

Embora os soft bounces não sejam rastreados na análise de dados da campanha, é possível monitorar os soft bounces no [Message Activity Log][3]. Aqui, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" de suas campanhas de e-mail.

Para saber mais sobre como gerenciar suas inscrições e campanhas de e-mail, consulte [Práticas recomendadas para e-mail][2].

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 2 de maio de 2024_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
