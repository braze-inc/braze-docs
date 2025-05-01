---
nav_title: Smart-TV Unterstützung
article_title: Smart-TV-Unterstützung für das Internet Braze SDK
platform: Web
page_order: 30
description: "Dieser Artikel beschreibt, wie Sie das Braze Web SDK für die Integration mit Smart-TVs (Samsung und LG) verwenden."

---

# Smart-TV Unterstützung

> Mit dem Braze Web SDK können Sie Analysen erfassen und den Nutzern von Smart-TVs, einschließlich [Samsung Tizen-TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) und [LG-Vs (webOS](https://webostv.developer.lge.com/discover)) In-App-Nachrichten und Content-Card-Nachrichten anzeigen. Dieser Artikel beschreibt, wie Sie das Braze Web SDK für die Integration mit Smart-TVs verwenden.

{% alert tip %}
Eine vollständige technische Referenz finden Sie in unserer [JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) oder in unseren [Beispielanwendungen](https://github.com/Appboy/smart-tv-sample-apps), um zu sehen, wie das Web SDK auf einem Fernseher läuft.
{% endalert %}

{% multi_lang_include Entwickler_guide/prerequisites/web.md %}

## Konfigurieren des Internet Braze SDK

Für die Integration mit Smart TVs sind zwei Änderungen erforderlich:

1. Achten Sie beim Herunterladen oder Importieren des Web SDK darauf, dass Sie das "core"-Bundle verwenden (verfügbar unter `https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`, wobei `x.y` die gewünschte Version ist). Wir empfehlen die Verwendung der CDN-Version unseres Web SDK, da die NPM-Version in nativen ES-Modulen geschrieben ist, während die CDN-Version in ES5 transpiliert ist. Wenn Sie die [NPM-Version](https://www.npmjs.com/package/@braze/web-sdk) bevorzugen, stellen Sie sicher, dass Sie einen Bundler wie Webpack verwenden, der ungenutzten Code entfernt, und dass der Code in ES5 transpiliert wird.
2. Bei der Initialisierung des Web SDK müssen Sie die Initialisierungsoptionen `disablePushTokenMaintenance` und `manageServiceWorkerExternally` auf `true` setzen.

## Analytics

Alle Analytics-Methoden des Web SDK können auch bei Smart-TVs verwendet werden. Eine vollständige Übersicht über das Tracking angepasster Events, angepasster Attribute und mehr finden Sie unter [Analytics]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

## In-App-Nachrichten und Inhaltskarten

Das Braze Web SDK unterstützt sowohl [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web) als auch [Content-Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web) auf Smart-TVs. Beachten Sie, dass Sie das ["Core"-Web-SDK](https://www.npmjs.com/package/@braze/web-sdk) verwenden müssen, da das Rendern von In-App-Nachrichten und Content Cards von unserer Standard-UI-Anzeige nicht unterstützt wird und stattdessen von Ihrer App angepasst werden sollte, um sich in das Erlebnis Ihrer TV-App einzufügen.

Weitere Informationen darüber, wie Ihre Smart-TV App In-App-Nachrichten empfangen und anzeigen kann, finden Sie unter [Triggern von Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).
