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

**Automatisch spielen**: Selbst bei aktiviertem Enablement der Hardware-Beschleunigung benötigen Android WebViews möglicherweise eine Nutzer:innen-Geste, um die Medienwiedergabe zu starten. Wenn Sie die automatische Wiedergabe benötigen, konfigurieren Sie die WebView, die zum Rendern von In-App-Nachrichten im HTML-Format verwendet wird, so, dass die Anforderung der Nutzer:innen-Geste deaktiviert wird. [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Dazu müssen Sie auf SDK-Ebene anpassen, wie die HTML In-App-Nachrichten angezeigt werden. Eine Anleitung zur Einrichtung finden Sie unter [Anpassen von In-App-Nachrichten für das Braze SDK]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## Überlegungen zu iOS

Zur Unterstützung von iOS-Geräten:

- Sie müssen das Attribut `playsinline` einfügen, da die Wiedergabe im Vollbildmodus nicht unterstützt wird.
- **Die automatische Wiedergabe wird unter iOS nicht garantiert**. Das Wiedergabeverhalten von iOS hängt von den Richtlinien auf `WKWebView` und OS-Ebene ab und erfordert möglicherweise eine Benutzer:in, auch wenn `autoplay` und `muted` eingestellt sind. Testen Sie Ihre HTML In-App-Nachricht auf Ihren iOS-Zielversionen und -Geräten.

Wenn die automatische Wiedergabe erforderlich ist und Ihre Tests zeigen, dass sie standardmäßig nicht funktioniert, können Sie die von HTML In-App-Nachrichten verwendete `WKWebViewConfiguration` anpassen, um die Anforderung an die Medienwiedergabe durch den Benutzer anzupassen, z.B. indem Sie die Eigenschaft `mediaTypesRequiringUserActionForPlayback` einstellen. Dies erfordert eine Anpassung auf SDK-Ebene. Ressourcen zu Swift finden Sie unter [In-App-Nachrichten für das Braze SDK anpassen]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) und [Hinzufügen der Braze JavaScript-Schnittstelle zu WebViews für Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Internet-Überlegungen

Die meisten modernen Browser lassen die automatische Wiedergabe nur unter bestimmten Bedingungen zu (in der Regel, wenn das Video stummgeschaltet ist). Wenn Sie `autoplay` in einer In-App-Nachricht verwenden, fügen Sie `muted` ein und testen Sie die unterstützten Browser und Geräte, da die Richtlinien für Browser variieren und in einigen Fällen immer noch eine Geste des Benutzers erforderlich sein kann.