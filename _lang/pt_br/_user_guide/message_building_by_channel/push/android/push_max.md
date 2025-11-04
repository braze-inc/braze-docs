---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "O Push Max amplia as notificações push do Android rastreando as notificações push que falharam e reenviando o push quando for mais provável que o usuário o receba."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Saiba mais sobre o Push Max e como você pode usar esse recurso para melhorar potencialmente a capacidade de entrega de notificações push do Android para [dispositivos OEM chineses]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/).

## O que é o Push Max?

O Push Max amplia as notificações push do Android rastreando as notificações push que falharam e reenviando o push quando for mais provável que o usuário o receba.

Alguns dispositivos Android fabricados por fabricantes de equipamentos originais (OEMs) chineses, como Xiaomi, OPPO e Vivo, empregam um esquema robusto de otimização da bateria para aumentar a vida útil da bateria. Esse comportamento pode ter a consequência não intencional de encerrar o processamento de aplicativos em segundo plano, o que reduz a capacidade de entrega de notificações por push nesses dispositivos se o aplicativo não estiver em primeiro plano. Essa circunstância ocorre com mais frequência nos mercados da Ásia-Pacífico (APAC).

## Disponibilidade

- Disponível apenas para notificações por push do Android
- Não há suporte para mensagens baseadas em ações ou acionadas por API
- Não há suporte quando a opção de [enviar apenas para o último dispositivo usado pelo usuário]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options) está selecionada

## Pré-requisitos

As notificações por push enviadas usando o Push Max só serão entregues a dispositivos que tenham pelo menos a seguinte [versão mínima do SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Usando o Push Max

{% tabs %}
{% tab Campaigns %}

Para usar o Push Max em sua campanha:

1. Crie uma campanha de envio.
2. Selecione **Android Push** como sua plataforma.
3. Vá para a etapa **Schedule Delivery**.
4. Selecione **Enviar usando Push Max**.

Seção Android Push Deliverability da etapa Schedule Delivery com a opção "Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Para usar o Push Max em seu Canvas:

1. Adicione uma etapa de Mensagem ao seu Canvas.
2. Selecione **Android Push** como sua plataforma.
3. Vá para a guia **Delivery Settings (Configurações de entrega** ).
4. Selecione **Enviar usando Push Max**.

Aba Delivery Settings (Configurações de entrega) de uma etapa de mensagem push do Android com a opção "Send using Push Max" (Enviar usando Push Max).]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Os dois recursos a seguir, Intelligent Timing e Time to Live, podem ser usados em conjunto com o Push Max para aumentar potencialmente a capacidade de entrega de suas notificações por push do Android.

### Cronograma inteligente

O Push Max funciona melhor quando [o Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) está ativado. O Intelligent Timing pode calcular e enviar a notificação push em um momento em que o usuário provavelmente estará usando o aplicativo e o push terá maior probabilidade de ser entregue.

### Tempo de vida (TTL)

O Time to Live (TTL) pode rastrear notificações push com falha para o Firebase Cloud Messaging (FCM) e tentar novamente a notificação quando for provável que o usuário a receba.

Por padrão, o Time to Live é definido como 28 dias, que é o máximo. Você pode diminuir o TTL padrão para todas as novas mensagens push do Android em **Configurações** > **Configurações do espaço de trabalho** > **Configurações de push**, ou pode configurar o número de dias por mensagem na guia **Configurações** ao compor uma notificação push do Android.

\![Campo Time to Live definido como 28 dias.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Coisas para saber

### Códigos promocionais

Recomendamos que você não use [códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) do Braze em mensagens em que o Push Max esteja ativado.

Isso ocorre porque os códigos promocionais são exclusivos. Se uma notificação push que contém um código promocional não for entregue, quando essa notificação for reenviada devido ao Push Max, um novo código promocional será enviado. Isso pode fazer com que você consuma os códigos promocionais mais rapidamente do que o esperado.

### Propriedades do evento Canvas e propriedades de entrada

O Push Max pode não funcionar como esperado se você incluir referências Liquid às [propriedades de entrada do Canvas ou às propriedades do evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em sua mensagem. Isso ocorre porque as propriedades de entrada e evento não estão disponíveis quando o Push Max está tentando reenviar a mensagem.
