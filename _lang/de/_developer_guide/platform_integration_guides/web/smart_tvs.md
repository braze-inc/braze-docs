---
nav_title: Smart TV-Integrationen
article_title: Smart TV-Integration für das Web
platform: Web
page_order: 20
description: "Dieser Artikel beschreibt, wie Sie das Braze Web SDK für die Integration mit Smart-TVs (Samsung und LG) verwenden."

---

# Smart TV-Integration

> Mit dem Braze Web SDK können Sie Analysen erfassen und den Nutzern von Smart-TVs, einschließlich [Samsung Tizen-TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) und [LG-Vs (webOS](https://webostv.developer.lge.com/discover)) In-App-Nachrichten und Content-Card-Nachrichten anzeigen. Dieser Artikel beschreibt, wie Sie das Braze Web SDK für die Integration mit Smart-TVs verwenden.

Eine vollständige technische Referenz finden Sie in unserer [JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) oder in unseren [Beispielanwendungen](https://github.com/Appboy/smart-tv-sample-apps), um zu sehen, wie das Web SDK auf einem Fernseher läuft.

## Installieren Sie das Braze SDK

Folgen Sie zunächst unserer Anleitung [SDK-Ersteinrichtung]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) für das Web-SDK.

Für die Integration mit Smart TVs sind zwei Änderungen erforderlich:

1. Achten Sie beim Herunterladen oder Importieren des Web SDK darauf, dass Sie das "core"-Bundle verwenden (verfügbar unter https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js, wobei x.y die gewünschte Version ist). Wir empfehlen die Verwendung der CDN-Version unseres Web SDK, da die NPM-Version in nativen ES-Modulen geschrieben ist, während die CDN-Version in ES5 transpiliert ist. Wenn Sie die [NPM-Version](https://www.npmjs.com/package/@braze/web-sdk) bevorzugen, stellen Sie sicher, dass Sie einen Bundler wie Webpack verwenden, der ungenutzten Code entfernt, und dass der Code in ES5 transpiliert wird.
2. Bei der Initialisierung des Web SDK müssen Sie die Initialisierungsoptionen `disablePushTokenMaintenance` und `manageServiceWorkerExternally` auf `true` setzen.

## Analytics

Alle Analytics-Methoden des Web SDK können auch bei Smart-TVs verwendet werden.

Eine vollständige Anleitung zur Verfolgung benutzerdefinierter Ereignisse, benutzerdefinierter Attribute und mehr finden Sie in unserer [Analytics-Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/).

## In-App-Nachrichten und Inhaltskarten

Das Braze Web SDK unterstützt sowohl [In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/) als auch [Content-Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/) auf Smart-TVs. Beachten Sie, dass Sie das ["Core"-Web-SDK](https://www.npmjs.com/package/@braze/web-sdk) verwenden müssen, da das Rendern von In-App-Nachrichten und Content Cards von unserer Standard-UI-Anzeige nicht unterstützt wird und stattdessen von Ihrer App angepasst werden sollte, um sich in das Erlebnis Ihrer TV-App einzufügen.

Unter [Manuelle Anzeige von In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display) finden Sie weitere Informationen darüber, wie Ihre Smart TV App In-App-Nachrichten empfangen und anzeigen kann.


