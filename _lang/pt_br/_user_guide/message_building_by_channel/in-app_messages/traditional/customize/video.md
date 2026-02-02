---
nav_title: Vídeo
article_title: Vídeo em mensagens no app
page_order: 4
page_type: reference
description: "Este artigo descreve como incorporar vídeos em suas mensagens no app em HTML."
channel:
  - in-app messages
---

# Vídeo {#video}

> Para reproduzir um vídeo em uma mensagem no app em HTML, inclua o seguinte elemento `<video>` no HTML e substitua os nomes dos vídeos pelo nome do arquivo (ou o URL do ativo remoto). Você pode encontrar outras opções possíveis em `<video>` nos [documentos da Web da MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Para usar um ativo de vídeo local, inclua esse arquivo ao fazer upload de ativos para sua campanha.

{% alert note %}
O conteúdo de vídeo só está disponível quando o dispositivo tem uma velocidade de rede razoável, a menos que o vídeo seja obtido do dispositivo localmente.
{% endalert %}

## Considerações sobre o Android

Para incorporar vídeo e outros conteúdos HTML5 em mensagens HTML no app no Android, é necessário ativar a aceleração de hardware na atividade em que a mensagem no app é exibida. Para saber mais, consulte o [guia do desenvolvedor do Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

## Considerações sobre o iOS

Para oferecer suporte a dispositivos iOS:

- É necessário incluir a atribuição `playsinline` porque a reprodução em tela inteira não é suportada no momento.
- O iOS não oferece suporte à reprodução automática por padrão. Para atualizar essa opção padrão, você pode modificar o [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)


