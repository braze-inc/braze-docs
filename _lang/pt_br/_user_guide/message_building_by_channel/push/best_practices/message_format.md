---
nav_title: Formatos de mensagem
article_title: Formatos de mensagem e imagem de push
page_order: 5
page_type: reference
description: "Este artigo descreve formatos de mensagem e imagem para notificações push."
channel: push

---

# Formatos de mensagem e imagem de push

> Este artigo de referência descreve formatos de mensagem e imagem para notificações push.

Para melhores resultados, consulte as seguintes diretrizes de tamanho de imagem e comprimento de mensagem ao criar suas mensagens de push. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação (iOS) e da configuração de exibição do dispositivo do usuário, bem como do tamanho do dispositivo. Quando em dúvida, mantenha seu texto curto e doce.

## Push iOS e Android

{% tabs local %}
{% tab Images %}

**Tipo de Imagem** | **Tamanho de Imagem Recomendado** | **Tamanho Máximo da Imagem** | **Tipos de Arquivos**
--- | --- | --- | ---
(iOS) 2:1 *Recomendado* | 500 KB | 5 MB | PNG, JPEG, GIF
(Android) Ícone de push | 500 KB | 5 MB | PNG, JPEG
(Android) Notificação expandida | 500 KB | 5 MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Text %}

| Tipo de mensagem | Comprimento recomendado da mensagem (apenas texto) | Comprimento recomendado da mensagem (rich)
--- | ---
(iOS) Tela de bloqueio | 160 caracteres | 130 caracteres
(iOS) Central de notificações | 160 caracteres | 130 caracteres
(iOS) Alerta de banner | 80 caracteres | 65 caracteres
(Android) Tela de bloqueio | 49 caracteres | N/A
(Android) Gaveta de notificações | 597 caracteres | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Se perguntando quantos caracteres você pode usar em uma notificação push do iOS sem que ela seja truncada? Confira nossas [diretrizes de contagem de caracteres do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Payload Size %}

**Plataforma** | **Tamanho**
--- | ---
pré iOS 8 | 0,256 KB
pós iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image Example %}
{% subtabs %}
{% subtab iOS %}

\![notificação push do iOS com texto que diz: "Oi! Esta é uma Push do iOS com uma imagem" com um emoji. Há uma pequena imagem ao lado do texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
\![notificação push do iOS em um push forte com o mesmo texto da mensagem anterior com uma imagem expandida precedendo o texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

\![notificação push do Android com uma imagem grande abaixo do texto da mensagem.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Notificações com imagens grandes são exibidas melhor quando se usa uma imagem de pelo menos 600x300 pixels.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Text Example %}
{% subtabs %}
{% subtab iOS %}

\![notificação push do iOS com texto que diz: "Oi! Esta é uma Push do iOS".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
\![notificação push do Android exibida na tela inicial.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Notificações web

{% tabs local %}
{% tab Images %}

| ** Navegador ** | ** Tamanho de Ícone Recomendado **
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Os ícones são configuráveis por campanha com Safari 16 no macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| ** Navegador ** | **Plataforma** | ** Tamanho da Imagem Grande **
| --- | --- | ---
Chrome | Android | proporção 2:1
Firefox | Android | N/A
Chrome | Windows | proporção 2:1
Edge | Windows | proporção 2:1
Firefox | Windows | N/A
Firefox | Windows | proporção 2:1
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| ** Navegador ** | **Plataforma** | ** Comprimento Máximo do Título **  | ** Comprimento Máximo do Corpo da Mensagem **
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | duzent
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


