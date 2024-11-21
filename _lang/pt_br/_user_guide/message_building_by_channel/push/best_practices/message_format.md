---
nav_title: Formatos de mensagens
article_title: Formatos de mensagens push e imagens
page_order: 5
page_type: reference
description: "Este artigo descreve os formatos de mensagem e imagem para notificações por push."
channel: push

---

# Formatos de mensagens e imagens push

> Este artigo de referência descreve os formatos de mensagem e imagem para notificações por push.

Para obter melhores resultados, consulte as seguintes diretrizes de tamanho de imagem e duração de mensagem ao criar suas mensagens push. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação (iOS) e da configuração de exibição do dispositivo do usuário, bem como do tamanho do dispositivo. Em caso de dúvida, mantenha seu texto curto e agradável.

## Push para iOS e Android

{% tabs local %}
{% tab Imagens %}

**Tipo de imagem** | **Tamanho de imagem recomendado** | **Tamanho máximo da imagem** | **Tipos de arquivos**
--- | --- | --- | ---
(iOS) 2:1 *Recomendado* | 500 KB | 5 MB | PNG, JPEG, GIF
(Android) Ícone push | 500 KB | 5 MB | PNG, JPEG
(Android) Notificação expandida | 500 KB | 5 MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Texto %}

| Tipo de mensagem | Comprimento recomendado da mensagem (somente texto) | Comprimento recomendado de mensagens (Rich)
--- | ---
(iOS) Tela de bloqueio | 160 caracteres | 130 caracteres
(iOS) Central de notificações | 160 caracteres | 130 caracteres
(iOS) Alerta de banner | 80 caracteres | 65 caracteres
(Android) Tela de bloqueio | 49 caracteres | N/D
(Android) Gaveta de notificação | 597 caracteres | N/D
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Quer saber quantos caracteres você pode usar em uma notificação por push do iOS sem que ela seja truncada? Confira nossas [diretrizes de contagem de caracteres do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Tamanho da carga útil %}

**Plataforma** | **Tamanho**
--- | ---
pré iOS 8 | 0,256 KB
pós iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Exemplo de imagem %}
{% subtabs %}
{% subtab iOS %}

![Notificação por push do iOS com texto que diz: "Oi! Este é um push do iOS com uma imagem" com um emoji. Há uma pequena imagem ao lado do texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificações por push do iOS em um hard push com o mesmo texto da mensagem anterior, com uma imagem expandida precedendo o texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Notificações por push do Android com uma imagem grande sob o texto da mensagem.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
As notificações de imagens grandes são mais bem exibidas quando se usa uma imagem de pelo menos 600x300 pixels.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Exemplo de texto %}
{% subtabs %}
{% subtab iOS %}

![Notificação por push do iOS com texto que diz: "Oi! Este é um iOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Notificações por push do Android exibidas na tela inicial.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web push

{% tabs local %}
{% tab Imagens %}

| **Navegador** | **Tamanho recomendado do ícone**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (os ícones podem ser configurados por campanha com o Safari 16 no MacOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **Navegador** | **Plataforma** | **Tamanho da imagem grande**
| --- | --- | ---
Chrome | Android | Relação de aspecto 2:1
Firefox | Android | N/D
Chrome | Windows | Relação de aspecto 2:1
Edge | Windows | Relação de aspecto 2:1
Firefox | Windows | N/D
Firefox | Windows | Relação de aspecto 2:1
Safari | MacOS | N/D
Chrome | MacOS | N/D
Firefox | MacOS | N/D
Opera | MacOS | N/D
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Texto %}

| **Navegador** | **Plataforma** | **Comprimento máximo do título**  | **Comprimento máximo do corpo da mensagem**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | MacOS | 35 | 50
Safari | MacOS | 38 | 84
Firefox | MacOS | 38 | 42
Opera | MacOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


