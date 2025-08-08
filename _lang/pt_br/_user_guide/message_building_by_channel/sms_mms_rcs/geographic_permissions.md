---
nav_title: "Permissões geográficas"
article_title: Permissões geográficas
description: "Este artigo aborda a lista de permissão de países para Permissões geográficas, que permite que você escolha para quais países SMS, MMS e RCS podem ser entregues."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Permissões geográficas

> As permissões geográficas aumentam a segurança e protegem contra o tráfego fraudulento de SMS, MMS e RCS, impondo controles sobre os países para os quais você pode enviar mensagens. Você pode especificar uma lista de permissão de países para garantir que as mensagens SMS, MMS e RCS sejam enviadas apenas para regiões aprovadas. Somente os administradores podem fazer alterações na lista de permissões de países. Os usuários não administradores têm acesso a uma versão somente leitura da lista de permissões que indica para quais países um grupo de inscrições pode enviar.

Se você for um administrador, poderá configurar os países que estão na lista de permissões. A lista de permissão de países é configurada no nível do [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/). Para acessá-la, acesse **Acessar** > **Inscrições** e selecione um grupo de inscrições de SMS, MMS ou RCS. A lista de permissões está em **Geographic Permissions (Permissões geográficas**).

![A seção SMS Geographic Permissions editável para um administrador com vários países selecionados na "Country allowlist" (Lista de permissão de países).]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Seleção de países

Adicione países à lista de permissões com o menu suspenso. Os países mais comuns de SMS e RCS são mostrados na parte superior, com outros mostrados abaixo. Você também pode pesquisar países digitando no campo de texto.

![O menu suspenso "Lista de permissão de países" com os países mais comuns exibidos na parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Remova os países selecionados anteriormente, desmarcando as respectivas caixas ao lado deles.

### Salvando suas alterações

As alterações entrarão em vigor depois que você selecionar **Salvar**. A remoção de países de sua lista de permissões impedirá que todas as mensagens SMS, MMS e RCS sejam enviadas para números nesses países.

![Modal de aviso confirmando os países que serão excluídos da lista de permissões.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países de alto risco

Alguns países têm um risco maior de bombeamento de tráfego de SMS e RCS. Esses países são indicados por uma tag de **Alto risco** no menu suspenso de países.

![O menu suspenso de países com o Azerbaijão tem uma tag de "Alto risco".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Se você permitir o envio nesses países, deverá primeiro reconhecer o risco de fazê-lo antes que o país seja adicionado à sua lista de permissões.

{% alert note %}
Limite os países em sua lista de permissões apenas àqueles necessários para atender às suas necessidades comerciais. Isso minimizará seu potencial de tráfego fraudulento. Para obter mais orientações sobre como evitar o bombeamento de tráfego de SMS, consulte [as Perguntas frequentes sobre fraude de bombeamento de tráfego de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidade de envios bloqueados

As tentativas de envio para países que não estão em sua lista de permissões serão abortadas. As mensagens abortadas serão registradas no [Evento de engajamento de mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) e no [evento de engajamento com mensagem de aborto de SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

As mensagens abortadas causadas por envios bloqueados são exibidas como **Erros de mensagem abortada** e têm a mensagem "O número de telefone do destinatário está em um país bloqueado".

![Registro de abortamento mostrando vários envios de SMS que foram bloqueados porque o número de telefone está em um país bloqueado.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

