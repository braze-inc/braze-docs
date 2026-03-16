---
nav_title: Video
article_title: Video in In-App-Nachrichten
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Videos in Ihre HTML-In-App-Nachrichten einbetten können."
channel:
  - in-app messages
---

# Video {#video}

> Um ein Video in einer HTML-In-App-Nachricht abzuspielen, fügen Sie das folgende `<video>`-Element in Ihr HTML ein und ersetzen die Videonamen durch den Namen Ihrer Datei (oder die URL des Remote-Assets). Weitere mögliche Optionen finden Sie unter `<video>` auf [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Wenn Sie ein lokales Video-Asset verwenden möchten, müssen Sie diese Datei beim Hochladen von Assets in Ihre Kampagne angeben.

{% alert note %}
Video-Content ist nur verfügbar, wenn das Gerät über eine angemessene Netzwerkgeschwindigkeit verfügt, es sei denn, das Video wird lokal vom Gerät abgerufen.
{% endalert %}

## Überlegungen zu Android

Um Videos und anderen HTML5-Content in HTML-In-App-Nachrichten auf Android einzubetten, muss die Hardwarebeschleunigung in der Aktivität aktiviert werden, in der die In-App-Nachricht angezeigt wird. Weitere Informationen finden Sie im [Android-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

**Automatische Wiedergabe**: Selbst bei aktivierter Hardwarebeschleunigung kann es vorkommen, dass Android WebViews eine Aktion der Nutzer:innen erfordern, um die Medienwiedergabe zu starten. Falls Sie die automatische Wiedergabe benötigen, konfigurieren Sie bitte das WebView, das zum Rendern von HTML-In-App-Nachrichten verwendet wird, um die erforderliche Benutzergeste zu deaktivieren, indem Sie einstellen[`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Dies erfordert eine Anpassung auf SDK-Ebene hinsichtlich der Darstellung von HTML-In-App-Nachrichten. Anleitungen zur Einrichtung finden Sie unter [„Anpassen von In-App-Nachrichten für das Braze SDK]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)“.

## Überlegungen zu iOS

Zur Unterstützung von iOS-Geräten:

- Bitte fügen Sie das`playsinline`Attribut ein, da die Vollbild-Wiedergabe nicht unterstützt wird.
- **Die automatische Wiedergabe kann unter iOS nicht garantiert werden**. Das Wiedergabeverhalten unter iOS hängt von den `WKWebView`Medienrichtlinien auf Betriebssystemebene ab und erfordert möglicherweise eine Aktion der Nutzer:innen, selbst wenn`autoplay`die entsprechenden `muted`Einstellungen aktiviert sind. Bitte testen Sie Ihre HTML-In-App-Nachricht auf den von Ihnen vorgesehenen iOS-Versionen und Geräten.

Wenn die automatische Wiedergabe erforderlich ist und Ihre Tests zeigen, dass sie standardmäßig nicht funktioniert, können Sie die von `WKWebViewConfiguration`HTML-In-App-Nachrichten verwendeten Einstellungen anpassen, um die Anforderungen an Benutzeraktionen für die Medienwiedergabe anzupassen, beispielsweise durch Festlegen der`mediaTypesRequiringUserActionForPlayback`Eigenschaft. Dies erfordert eine Anpassung auf SDK-Ebene. Informationen zu Swift-Ressourcen finden Sie unter [„Anpassen von In-App-Nachrichten für das Braze SDK]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift)“ und [„Hinzufügen der Braze-JavaScript-Schnittstelle zu WebViews für Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift)“.

## Überlegungen zum Internet

Die meisten modernen Browser machen die automatische Wiedergabe nur unter bestimmten Bedingungen zulässig (in der Regel, wenn das Video stummgeschaltet ist). Wenn Sie in einer `autoplay`In-App-Nachricht verwenden, fügen Sie hinzu`muted`und führen Sie Tests auf allen unterstützten Browsern und Geräten durch, da die Browserrichtlinien variieren und in einigen Fällen möglicherweise noch eine Benutzeraktion erforderlich ist.