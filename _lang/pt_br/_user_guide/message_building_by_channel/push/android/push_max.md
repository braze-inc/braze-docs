---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Para melhorar as notificações por push no Android, o Push Max rastreia as que não foram entregues e reenvia o push quando há mais probabilidade de o usuário ver as notificações."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Saiba mais sobre o Push Max e como você pode usar esse recurso para melhorar potencialmente a entregabilidade das notificações por push do Android para [dispositivos OEM chineses]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/).

## O que é o Push Max?

Para melhorar as notificações por push no Android, o Push Max rastreia as que não foram entregues e reenvia o push quando há mais probabilidade de o usuário ver as notificações.

Alguns dispositivos Android fabricados por fabricantes de equipamentos originais (OEMs) chineses, como Xiaomi, OPPO e Vivo, empregam um esquema robusto de otimização de bateria para aumentar a vida útil da bateria. Esse comportamento pode ter a consequência não intencional de encerrar o processamento do aplicativo em segundo plano, o que reduz a entregabilidade das notificações por push nesses dispositivos se o aplicativo não estiver em primeiro plano. Essa circunstância ocorre com mais frequência nos mercados da Ásia-Pacífico (APAC).

## Disponibilidade

- Disponível apenas para notificações por push no Android
- Não há suporte para mensagens baseadas em ações ou disparadas por API
- Não há suporte quando a opção de [enviar apenas para o último dispositivo usado pelo usuário]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options) está selecionada

## Pré-requisitos

As notificações por push enviadas usando o Push Max só serão entregues a dispositivos que tenham pelo menos a seguinte [versão mínima do SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Usando o Push Max

{% tabs %}
{% tab Campanhas %}

Para usar o Push Max em sua campanha:

1. Crie uma campanha push.
2. Selecione **Android Push** como sua plataforma.
3. Acesse a etapa **Schedule Delivery**.
4. Selecione **Enviar usando Push Max**.

![Seção de entregabilidade de Android Push da etapa Agendar entrega com a opção "Enviar usando Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Para usar o Push Max em seu Canva:

1. Adicione uma etapa de Mensagens ao seu canvas.
2. Selecione **Android Push** como sua plataforma.
3. Acesse a guia **Configurações de entrega**.
4. Selecione **Enviar usando Push Max**.

![Guia Configurações de entrega de uma etapa de Mensagem push do Android com a opção "Enviar usando Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Os dois recursos a seguir, Intelligent Timing e Time to Live, podem ser usados em conjunto com o Push Max para aumentar potencialmente a entregabilidade de suas notificações por push no Android.

### Intelligent Timing

O Push Max funciona melhor quando [o Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) está ativado. O Intelligent Timing pode calcular e enviar a notificação por push no momento em que é mais provável que o usuário esteja usando o app e que o push tenha maior probabilidade de ser entregue.

### TTL (Time to Live)

O TTL (Time to Live) pode rastrear notificações por push com falha para o Firebase Cloud Messaging (FCM) e tentar novamente a notificação quando for provável que o usuário a receba.

Por padrão, o TTL é definido como 28 dias, que é o máximo. Você pode diminuir o TTL padrão para todas as novas mensagens push do Android em **Configurações** > **Configurações do espaço de trabalho** > **Push Time to Live (TTL)** ou pode configurar o número de dias por mensagem na guia **Configurações** ao criar uma notificação por push do Android.

![Campo TTL definido como 28 dias.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Coisas para saber

### Códigos promocionais

Recomendamos que você não use [códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) do Braze em mensagens em que o Push Max esteja ativado.

Isso ocorre porque os códigos promocionais são exclusivos. Se uma notificação por push que contém um código promocional não for entregue, quando essa notificação for reenviada devido ao Push Max, um novo código promocional será enviado. Isso pode fazer com que você consuma os códigos promocionais mais rapidamente do que o esperado.

### Propriedades do evento da tela e propriedades de entrada

O Push Max pode não funcionar como esperado se você incluir referências Liquid às [propriedades de entrada do Canva ou às propriedades do evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em sua mensagem. Isso ocorre porque as propriedades de entrada e evento não estão disponíveis quando o Push Max está tentando reenviar a mensagem.
