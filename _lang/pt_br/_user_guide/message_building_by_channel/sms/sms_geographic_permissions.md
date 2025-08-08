---
nav_title: "Permissões geográficas de SMS"
article_title: Permissões geográficas de SMS
description: "Este artigo aborda a lista de permissão de países para SMS Geographic Permissions, que permite que você escolha para quais países o SMS pode ser entregue."
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# Permissões geográficas de SMS

> As permissões geográficas de SMS aumentam a segurança e protegem contra o tráfego fraudulento de SMS, impondo controles sobre os países para os quais você pode enviar mensagens SMS. Você pode especificar uma lista de permissão de países para garantir que as mensagens SMS sejam enviadas apenas para regiões aprovadas. Somente os administradores podem fazer alterações na lista de permissões de países. Os usuários não administradores têm acesso a uma versão somente leitura da lista de permissões que indica para quais países um grupo de inscrições pode enviar.

![A seção de permissões geográficas de SMS somente leitura para um usuário não administrador com os Estados Unidos e o Reino Unido selecionados na "Lista de permissão de países".][6]{: style="max-width:80%;"}

## Configuração da lista de permissões de países para SMS

Se você for um administrador, poderá configurar os países que estão na lista de permissões. A lista de permissão de países é configurada no nível do [grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/). Para acessá-la, acesse **Público** > **Inscrições** e selecione um grupo de inscrições de SMS. A lista de **permissões** está em **SMS Geographic Permissions (Permissões geográficas de SMS**).

![A seção editável de permissões geográficas de SMS para um administrador com a Austrália, o Canadá e os Estados Unidos selecionados na "Lista de permissão de países".][1]{: style="max-width:80%;"}

### Seleção de países

Adicione países à lista de permissões com o menu suspenso. Os países mais comuns de SMS são mostrados na parte superior, e outros são mostrados abaixo. Você também pode pesquisar países digitando no campo de texto.

![O menu suspenso "Lista de permissão de países" com os países mais comuns exibidos na parte superior.][2]{: style="max-width:80%;"}

Remova os países selecionados anteriormente, desmarcando as respectivas caixas ao lado deles.

### Salvando suas alterações

As alterações entrarão em vigor depois que você selecionar **Salvar**. A remoção de países de sua lista de permissões impedirá que todas as mensagens SMS e MMS sejam enviadas para números nesses países.

![Modal de aviso confirmando os países que serão excluídos da lista de permissões.][3]{: style="max-width:70%;"}

## Países de alto risco

Certos países têm um risco maior de bombeamento de tráfego de SMS. Esses países são indicados por uma tag de **Alto risco** no menu suspenso de países.

![O menu suspenso do país com o Azerbaijão tendo uma tag de "Alto Risco".][4]{: style="max-width:80%;"}

Se você permitir o envio nesses países, deverá primeiro reconhecer o risco de fazê-lo antes que o país seja adicionado à sua lista de permissões.

{% alert note %}
Limite os países em sua lista de permissões apenas àqueles necessários para atender às suas necessidades comerciais. Isso minimizará seu potencial de tráfego fraudulento. Para obter mais orientações sobre como evitar o bombeamento de tráfego de SMS, consulte [as Perguntas frequentes sobre fraude de bombeamento de tráfego de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidade de envios bloqueados

As tentativas de envio para países que não estão em sua lista de permissões serão abortadas. As mensagens abortadas serão registradas no [Evento de engajamento de mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) e no [evento de engajamento com mensagem de aborto de SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

As mensagens abortadas causadas por envios bloqueados serão exibidas como `Abort_Type = "blocked_recipient_country"` com o registro de aborto detalhando o país bloqueado.

![Registro de abortamento mostrando o abort_type de blocked_recipient_country e as iniciais do país do número de telefone bloqueado.][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}