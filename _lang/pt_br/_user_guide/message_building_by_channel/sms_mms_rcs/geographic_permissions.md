---
nav_title: "Permissões geográficas"
article_title: Permissões Geográficas
description: "Este artigo cobre a lista de permissões de países para Permissões Geográficas, que permite escolher quais países SMS, MMS e RCS podem ser entregues."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Permissões Geográficas

> As Permissões Geográficas aumentam a segurança e protegem contra tráfego fraudulento de SMS, MMS e RCS, aplicando controles nos países para os quais você pode enviar mensagens. Você pode especificar uma lista de permissões de países para garantir que mensagens SMS, MMS e RCS sejam enviadas apenas para regiões aprovadas. Apenas administradores podem fazer alterações na lista de permissões de países. Usuários não administradores têm acesso a uma versão somente leitura da lista de permissões que indica quais países um grupo de assinatura pode enviar.

Se você é um administrador, pode configurar os países que estão na lista de permissões. A lista de permissões de países é configurada no nível do [grupo de assinatura]({{site.baseurl}}/sms_rcs_subscription_groups/). Você pode acessá-la indo para **Público** > **Assinaturas** e selecionando um grupo de assinatura SMS, MMS ou RCS. A lista de permissões está sob **Permissões Geográficas**.

\![A seção editável de Permissões Geográficas de SMS para um administrador com vários países selecionados na "Lista de permissões de países".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Selecionando países

Adicione países à lista de permissões com o menu suspenso. Os países mais comuns de SMS e RCS são mostrados no topo, com outros mostrados abaixo. Você também pode pesquisar países digitando no campo de texto.

\![O menu suspenso "Lista de permissões de países" com os países mais comuns exibidos no topo.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Remova países selecionados anteriormente desmarcando as caixas respectivas ao lado deles.

### Salvando suas alterações

As alterações entrarão em vigor após você selecionar **Salvar**. Remover países da sua lista de permissões impedirá que todas as mensagens SMS, MMS e RCS sejam enviadas para números nesses países.

\![Modal de aviso confirmando os países que serão excluídos da lista de permissões.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países de alto risco

Certos países têm um risco maior de aumento de tráfego de SMS e RCS. Esses países são indicados por uma tag **Alto Risco** no menu suspenso de países.

\![O menu suspenso de países com o Azerbaijão tendo uma tag "Alto Risco".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Se você permitir o envio nesses países, deve primeiro reconhecer o risco de fazê-lo antes que o país seja adicionado à sua lista de permissões.

{% alert note %}
Limite os países na sua lista de permissões apenas àqueles necessários para atender às suas necessidades comerciais. Isso minimizará seu potencial para tráfego fraudulento. Para mais orientações sobre como prevenir o aumento de tráfego de SMS, veja [FAQs sobre fraudes de aumento de tráfego de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidade de envios bloqueados

Envios tentados para países que não estão na sua lista de permissões serão abortados. Mensagens abortadas serão registradas no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) e dentro do [evento de engajamento de mensagem de abortar SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Mensagens abortadas causadas por envios bloqueados aparecem como **Erros de Mensagem Abortada** e têm a mensagem "O número de telefone do destinatário está em um país bloqueado".

\![Registro de abortos mostrando vários envios de SMS que foram bloqueados porque o número de telefone está em um país bloqueado.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

