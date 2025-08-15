---
nav_title: Deaktivieren des SDK-Trackings für iOS
article_title: SDK Tracking für iOS deaktivieren
platform: iOS
page_order: 8
description: "Dieser Artikel zeigt, wie Sie die Datenerfassung für Ihre iOS-Anwendung deaktivieren können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Deaktivieren der Datenerfassung für iOS

Um den Datenschutzbestimmungen zu entsprechen, kann das Tracking von Daten im iOS SDK mit der Methode [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733) gänzlich unterbunden werden. Diese Methode führt dazu, dass alle Netzwerkverbindungen abgebrochen werden und das Braze SDK keine Daten an unsere Server weitergibt. Wenn Sie die Datenerfassung später wieder aufnehmen möchten, können Sie [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) verwenden, um die Datenerfassung fortzusetzen.

Außerdem können Sie mit der Methode [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) verwenden, um alle auf dem Gerät gespeicherten clientseitigen Daten vollständig zu löschen.

Sofern ein Nutzer nicht alle Apps eines Anbieters auf einem bestimmten Gerät deinstalliert, führt die nächste Ausführung von Braze SDK und Apps nach dem Aufruf von `wipeDataAndDisableForAppRun()` dazu, dass unser Server diesen Nutzer:innen über seinen Identifier for Vendors (IDFV) erneut identifiziert. Um alle Nutzerdaten vollständig zu löschen, sollten Sie einen Aufruf an `wipeDataAndDisableForAppRun` mit einer Anfrage zum Löschen von Daten auf dem Server über die Braze [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint) kombinieren.

## iOS SDK v5.7.0+
Bei Geräten, die iOS SDK v5.7.0 und höher verwenden, führt die [Deaktivierung der IDFV-Erfassung]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfv-collection---swift/) dazu, dass der Aufruf von [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) nicht dazu führt, dass unser Server Nutzer über ihren Identifier for Vendors (IDFV) wiedererkennt.