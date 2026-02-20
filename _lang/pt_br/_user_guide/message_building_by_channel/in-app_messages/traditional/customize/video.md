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

**auto-play**: Mesmo com a aceleração de hardware ativada, os WebViews do Android podem exigir um gesto do usuário para iniciar a reprodução de mídia. Se você precisar de auto-play, configure o WebView usado para renderizar mensagens HTML no app para desativar a exigência de gesto do usuário definindo [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Isso requer personalização em nível de SDK de como as mensagens HTML no app são exibidas. Para orientações de configuração, veja [Personalizar mensagens no app para o SDK Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## Considerações sobre o iOS

Para oferecer suporte a dispositivos iOS:

- Você deve incluir o atributo `playsinline` porque a reprodução em tela cheia não é suportada.
- **auto-play não é garantido no iOS**. O comportamento de reprodução no iOS depende de `WKWebView` e políticas de mídia em nível de OS, e pode exigir um gesto do usuário mesmo quando `autoplay` e `muted` estão definidos. Teste sua mensagem HTML no app nas versões e dispositivos iOS alvo.

Se o auto-play for necessário e seus testes mostrarem que não funciona por padrão, você pode personalizar o `WKWebViewConfiguration` usado por mensagens HTML no app para ajustar a exigência de ação do usuário para reprodução de mídia, por exemplo, definindo a propriedade `mediaTypesRequiringUserActionForPlayback`. Isso requer personalização em nível de SDK. Para recursos Swift, veja [Personalizar mensagens no app para o SDK Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) e [Adicionando a interface JavaScript do Braze aos WebViews para Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Considerações sobre a web

A maioria dos navegadores modernos permite auto-play apenas sob certas condições (comumente quando o vídeo está mudo). Se você usar `autoplay` em uma mensagem HTML no app, inclua `muted` e teste em seus navegadores e dispositivos suportados, pois as políticas dos navegadores variam e podem ainda exigir um gesto do usuário em alguns casos.