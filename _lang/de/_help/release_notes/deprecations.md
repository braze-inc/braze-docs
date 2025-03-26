---
nav_title: Abwertungen
article_title: Abwertungen
page_order: 9
page_type: reference
description: "Diese Seite enthält Verweise auf veraltete Artikel und bietet eine Liste veralteter und nicht unterstützter Funktionen."
---

# Abwertungen

Technologie ist immer in Bewegung - innerhalb und außerhalb von Braze! Und wir tun unser Bestes, um mit ihr Schritt zu halten. Hier finden Sie die Ursprünge von Braze und seiner Technologie, wie wir die Menschen in der "vorigen Zeit" unterstützt haben - vor der heutigen Zeit jedenfalls...

Vielleicht sind Sie hierher gelangt, weil Sie nach einem Begriff für eine Integration oder Funktion gesucht haben, die nicht mehr existiert. Dies ist unser Versuch, Sie über unsere Fortschritte und Bewegungen in der Technologiebranche auf dem Laufenden zu halten. Unter den folgenden Links finden Sie eine Liste der veralteten und nicht mehr unterstützten Funktionen und können veraltete Artikel lesen.

## Veraltete Artikel

- [Benutzerdefinierter Push-Broadcast-Empfänger für Android]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Eclipse SDK Einrichtung]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [Ablehnung von TLS 1.0 und 1.1]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Twilio Webhook-Integration]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [Apptimize Partnerschaft]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Grouparoo Partnerschaft]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)
- [Shopify `checkout.liquid` Verwerfung]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout/)

## Protokoll der Verwerfungen

### Shopify `checkout.liquid`

**Unterstützung zurückgezogen**: August 2024 (Phase 1), August 2025 (Phase 2)

Die Unterstützung für Shopify `checkout.liquid` wird im August 2024 auslaufen und im August 2025 enden. Shopify wird auf [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) umsteigen, das sicherer, leistungsfähiger und anpassbarer ist.

### Benutzerdefinierter Push-Broadcast-Empfänger für Android

**Unterstützung zurückgezogen**: Oktober 2022

Die Verwendung eines benutzerdefinierten `BroadcastReceiver` für Push-Benachrichtigungen ist nicht mehr sinnvoll. Verwenden Sie stattdessen [` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/) stattdessen.

### Grouparoo Partnerschaft

**Unterstützung zurückgezogen**: April 2022

Die Unterstützung für Grouparoo wurde im April 2022 eingestellt.

### Braze Windows SDK

**März 24, 2022**: Das Braze Windows SDK ist veraltet und es können keine neuen Windows-Apps im Braze Dashboard erstellt werden.<br>
**September 15, 2022**: Es können keine neuen Nachrichten an Windows-Anwendungen gesendet werden. Bestehende Nachrichten und Datenerfassung sind davon nicht betroffen.<br>
**11\. Januar 2024**: Braze wird keine Nachrichten mehr übermitteln oder Daten von Windows-Anwendungen sammeln.

### Baidu Push-Integration

**März 24, 2022**: Die Baidu-Push-Integration von Braze ist veraltet, und es können keine neuen Baidu-Apps im Braze-Dashboard erstellt werden. <br>
**September 15, 2022**: Es können keine neuen Baidu-Push-Nachrichten erstellt werden. Bestehende Nachrichten und Datenerfassung sind davon nicht betroffen.<br>
**11\. Januar 2024**: Braze wird keine Nachrichten mehr versenden oder Daten von Baidu-Apps sammeln.

### appboyBridge globale Variable

**Unterstützung zurückgezogen**: Mai 2021<br>
**Ersetzt durch**: `brazeBridge`

Die globale Variable `appboyBridge` ist veraltet und wird durch `brazeBridge` ersetzt. `appboyBridge` wird für bestehende Kunden weiterhin funktionieren, aber wir empfehlen Ihnen, auf `brazeBridge` zu migrieren, wenn Sie `appboyBridge` verwenden.

### Amazon Moments Partnerschaft

**Unterstützung zurückgezogen**: Juni 2020

Die Unterstützung für Amazon Moments wurde im Juni 2020 eingestellt. Amazon Moments wird mit Amazon Advertising zusammengelegt und hat seine APIs und unsere Integration veraltet.

### Faktische Partnerschaft

**Unterstützung zurückgezogen**: Juni 2020

Die Unterstützung für Factual wurde im Juni 2020 eingestellt. Factual wurde kürzlich von Foursquare übernommen und ist nicht mehr mit der Braze-Plattform integriert.

### Twilio Webhook-Integration

**Unterstützung zurückgezogen**: Januar 2020

Die Unterstützung für die [Twilio Webhook-Integration]({{site.baseurl}}/partners/twilio/) wurde zum 31\. Januar 2020 eingestellt. Wenn Sie mit Braze weiterhin auf SMS-Dienste zugreifen möchten, lesen Sie unsere [SMS-Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).

### Apptimize Partnerschaft

**Unterstützung zurückgezogen**: August 2019

Wenn Sie derzeit [Apptimize mit Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize) verwenden, werden Sie keine Unterbrechung des Dienstes erleben. Sie können weiterhin benutzerdefinierte Apptimize-Attribute für Braze Benutzerprofile festlegen. Es wird jedoch keine formale Eskalationsunterstützung mit dem Partner angeboten.

### Originelle In-App-Nachrichten

**Unterstützung zurückgezogen:** Februar 2019<br>
**Ersetzt durch**: [In-App-Messaging]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message)

Braze hat das Aussehen der In-App-Nachrichten verbessert, um den neuesten UX- und UI-Best Practices zu entsprechen, und unterstützt die ursprünglichen In-App-Nachrichten nicht mehr.

Mit den folgenden SDK-Versionen ist Braze zu einer neuen Form von In-App-Nachrichten übergegangen:
- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

Vor diesen Versionen unterstützte Braze "originale In-App-Nachrichten". Zuvor wurde die Unterstützung für ursprüngliche In-App-Nachrichten für alle Kunden angeboten, die vor der neuen Version eine In-App-Kampagne durchgeführt haben. Alle Kampagnenstatistiken waren von der Änderung nicht betroffen, und diejenigen, die ursprüngliche In-App-Nachrichten verschickt hatten, hatten die Möglichkeit, über die Schaltfläche **Kampagne erstellen** auf der **Kampagnenseite** weitere zu versenden.

### Feedback-Widget

**Unterstützung zurückgezogen**: 1\. Juli 2019.

Das Braze SDK stellte ein Feedback-Widget zur Verfügung, das zu Ihrer App hinzugefügt werden konnte, um Benutzern die Möglichkeit zu geben, mit der Methode `submitfeedback` Feedback zu hinterlassen und es entweder an Desk.com oder Zendesk weiterzuleiten und auf dem Dashboard zu verwalten.

### Google Cloud Messaging (GCM)

**Unterstützung zurückgezogen**: Löten Sie die Stütze ab: Juli 2018, Google stellt die Unterstützung ein: Mai 29, 2019<br>
**Ersetzt durch**: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google hat [die Unterstützung für GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) ab dem 29\. Mai 2019 [eingestellt](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html). Braze hat die Unterstützung für GCM in den Android SDKs im Juli 2018 eingestellt, was in unseren [Android SDK Changelogs](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) vermerkt wurde. Das bedeutet, dass bestehende GCM-Tokens weiterhin funktionieren und Sie Ihren bestehenden Benutzern Nachrichten schicken können. Allerdings können Sie neuen Benutzern keine Nachrichten schicken.

Kunden, die noch nicht auf [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) migriert sind, können von dieser Änderung betroffen sein.

Wenn Sie nicht auf FCM umgestellt haben, schlagen alle Registrierungen von GCM-Push-Tokens fehl. Wenn Ihre Anwendungen derzeit GCM unterstützen, müssen Sie mit Ihren Entwicklungsteams an der [Umstellung von GCM auf Firebase Cloud Messaging (FCM](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)) arbeiten.

### Eclipse

**Unterstützung zurückgezogen**: 2014-2015<br>
**Ersetzt durch**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze hat die Unterstützung für die Eclipse IDE eingestellt, da Google [die Unterstützung](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) für das Eclipse Android Developer Tools (ADT) Plugin [eingestellt hat](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). 

Wenn Sie vor der Migration Hilfe bei der Eclipse-Integration benötigen, wenden Sie sich bitte an den [Support]({{site.baseurl}}/support_contact/).

### Der Raw Event Stream (RES)

**Unterstützung zurückgezogen**: Juli 2018<br>
**Ersetzt durch**: [Currents]({{site.baseurl}}/partners/braze_currents/about/)

Der Raw Event Stream war der Vorgänger von [Currents]({{site.baseurl}}/partners/braze_currents/about/) und wurde veraltet, um Platz für die Zukunft der Braze-Daten zu schaffen.

### Verzögerung im Leerlauf - GCM-Funktion

**Unterstützung zurückgezogen**: November 2016

Der Parameter Verzögerung im Leerlauf war früher Teil der [GCM-Push-Optionen](https://developers.google.com/cloud-messaging/http-server-ref). Google hat die Unterstützung für diese Option am 15\. November 2016 zurückgezogen. Zuvor bedeutete die Einstellung **true**, dass die Nachricht erst gesendet werden sollte, wenn das Gerät aktiv wird.

### Benutzerdefinierte Endpunkte

**Unterstützung zurückgezogen**: Dezember 2019

Entfernen von benutzerdefinierten Endpunkten. Wenn Sie einen benutzerdefinierten Endpunkt haben, können Sie diesen weiterhin verwenden, aber Braze gibt ihn nicht mehr heraus.


[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
