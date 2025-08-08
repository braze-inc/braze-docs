---
nav_title: Abwertungen
article_title: Abwertungen
page_order: 9
page_type: reference
description: "Diese Seite enthält Referenzen zu veralteten Artikeln und eine Liste veralteter und nicht mehr unterstützter Features."
---

# Abwertungen

Die Technologie ist immer in Bewegung - innerhalb und außerhalb von Braze! Und wir tun unser Bestes, um mit ihr Schritt zu halten. Hier finden Sie die Herkunft von Braze und seiner Technologie, wie wir die Menschen in der Zeit 'vor der Zeit' unterstützt haben - vor der Zeit jedenfalls...

Möglicherweise sind Sie hierher gelangt, weil Sie nach einem Begriff für eine Integration oder ein Feature gesucht haben, das nicht mehr existiert. Dies ist unser Versuch, Sie über unsere Fortschritte und Bewegungen in der Technologiebranche auf dem Laufenden zu halten. Unter den folgenden Links finden Sie eine Liste der veralteten und nicht mehr unterstützten Features und können veraltete Artikel lesen.

## Veraltete Artikel

- [Angepasster Push-Empfänger für Android]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Eclipse SDK Einrichtung]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0 und 1.1 veraltet]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Twilio (Twilio) Webhook Integration]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [Apptimize Partnerschaft]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Grouparoo Partnerschaft]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)
- [Shopify `checkout.liquid` Verwerfung]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout/)

## Protokoll der Verwerfungen

### Shopify `checkout.liquid`

**Unterstützung zurückgezogen**: August 2024 (Phase 1), August 2025 (Phase 2)

Die Unterstützung für Shopify `checkout.liquid` wird im August 2024 auslaufen und im August 2025 enden. Shopify wird auf [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) umsteigen, das sicherer, performanter und anpassbarer ist.

### Angepasster Push-Empfänger für Android

**Unterstützung zurückgezogen**: Oktober 2022

Die Verwendung eines angepassten `BroadcastReceiver` für Push-Benachrichtigungen ist nicht mehr zeitgemäß. Verwenden Sie stattdessen [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) stattdessen.

### Grouparoo Partnerschaft

**Unterstützung zurückgezogen**: April 2022

Die Unterstützung für Grouparoo wurde im April 2022 eingestellt.

### Braze Windows SDK

**März 24, 2022**: Das Braze Windows SDK ist veraltet, und im Braze-Dashboard können keine neuen Windows-Apps erstellt werden.<br>
**September 15, 2022**: Es können keine neuen Nachrichten an Windows-Anwendungen gesendet werden. Bestehende Nachrichten und Datenerfassung sind davon nicht betroffen.<br>
**11\. Januar 2024**: Braze wird keine Nachrichten mehr übermitteln oder Daten von Windows-Anwendungen sammeln.

### Baidu Push-Integration

**März 24, 2022**: Die Braze Baidu Push Integration ist veraltet, und es können keine neuen Baidu Apps im Braze-Dashboard erstellt werden. <br>
**September 15, 2022**: Es können keine neuen Baidu-Push-Nachrichten erstellt werden. Bestehende Nachrichten und Datenerfassung sind davon nicht betroffen.<br>
**11\. Januar 2024**: Braze wird keine Nachrichten mehr versenden oder Daten von Baidu-Apps sammeln.

### appboyBridge globale Variable

**Unterstützung zurückgezogen**: Mai 2021<br>
**Ersetzt durch**: `brazeBridge`

Die globale Variable `appboyBridge` ist veraltet und wird durch `brazeBridge` ersetzt. `appboyBridge` wird für bestehende Kund:inen weiterhin funktionieren, aber wir empfehlen Ihnen, auf `brazeBridge` zu migrieren, wenn Sie `appboyBridge` verwenden.

### Amazon Moments Partnerschaft

**Unterstützung zurückgezogen**: Juni 2020

Die Unterstützung für Amazon Moments wurde im Juni 2020 eingestellt. Amazon Moments wird in Amazon Advertising aufgehen und hat seine APIs und unsere Integration veraltet.

### Faktische Partnerschaft

**Unterstützung zurückgezogen**: Juni 2020

Die Unterstützung für Factual wurde im Juni 2020 eingestellt. Factual wurde kürzlich von Foursquare übernommen und ist nicht mehr in die Braze Plattform integriert.

### Twilio (Twilio) Webhook Integration

**Unterstützung zurückgezogen**: Januar 2020

Die Unterstützung für die [Twilio Webhook Integration]({{site.baseurl}}/partners/twilio/) wurde zum 31\. Januar 2020 eingestellt. Wenn Sie mit Braze weiterhin auf SMS Dienste zugreifen möchten, lesen Sie unsere [SMS Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).

### Apptimize Partnerschaft

**Unterstützung zurückgezogen**: August 2019

Wenn Sie derzeit [Apptimize mit Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize) verwenden, wird der Dienst nicht unterbrochen. Sie können die angepassten Attribute von Apptimize immer noch an Nutzerprofile von Braze anpassen. Es wird jedoch keine formale Eskalationsunterstützung mit dem Partner angeboten.

### In-App-Nachrichten im Original

**Unterstützung zurückgezogen:** Februar 2019<br>
**Ersetzt durch**: [In-App-Messaging]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)

Braze hat das Aussehen der In-App-Nachrichten verbessert, um den neuesten UX- und UI-Best Practices zu entsprechen, und unterstützt die ursprünglichen In-App-Nachrichten nicht mehr.

Mit den folgenden SDK-Versionen ist Braze zu einer neuen Form von In-App-Nachrichten übergegangen:
- iOS: `2.19.0`
- Android: `1.13.0`
- Internet: `1.3.0`

Vor diesen Versionen unterstützte Braze "originale In-App-Nachrichten". Zuvor wurde die Unterstützung für originale In-App-Nachrichten für alle Kunden angeboten, die vor der neuen Version eine In-App-Kampagne durchgeführt haben. Alle Statistiken der Kampagnen waren von der Änderung nicht betroffen, und diejenigen, die ursprüngliche In-App-Nachrichten gesendet hatten, hatten die Opportunity, weitere Nachrichten über den Button **Kampagne erstellen** auf der **Kampagnen-Seite** zu senden.

### Feedback-Widget

**Unterstützung zurückgezogen**: 1\. Juli 2019.

Das Braze SDK stellte ein Feedback-Widget zur Verfügung, das zu Ihrer App hinzugefügt werden konnte, um Nutzern:innen die Möglichkeit zu geben, mit der Methode `submitfeedback` ein Feedback zu hinterlassen, das entweder an Desk.com oder an Zendesk weitergeleitet und auf dem Dashboard verwaltet wurde.

### Google Cloud Messaging (GCM)

**Unterstützung zurückgezogen**: Entfernen Sie die Stütze mit Braze: Juli 2018, Google stellt die Unterstützung ein: Mai 29, 2019<br>
**Ersetzt durch**: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Ab dem 29\. Mai 2019 hat Google hat [die Unterstützung für GCM eingestellt](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html). Braze hat die Unterstützung für GCM in den Android SDKs im Juli 2018 eingestellt, was in unseren [SDK Changelogs für Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) vermerkt wurde. Das bedeutet, dass bestehende GCM Token weiterhin funktionieren und Sie Ihren bestehenden Nutzer:innen Nachrichten schicken können. Allerdings können Sie neuen Nutzer:innen keine Nachrichten schicken.

Kunden:in, die noch nicht auf [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) migriert sind, können von dieser Änderung betroffen sein.

Wenn Sie nicht auf FCM umgestellt haben, werden alle Registrierungen von GCM Push-Tokens fehlschlagen. Wenn Ihre Apps derzeit GCM unterstützen, müssen Sie mit Ihren Entwicklerteams an der [Umstellung von GCM auf Firebase Cloud Messaging (FCM](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)) arbeiten.

### Eclipse

**Unterstützung zurückgezogen**: 2014-2015<br>
**Ersetzt durch**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze hat die Unterstützung für die Eclipse IDE eingestellt, da Google für das Eclipse Android Developer Tools (ADT) Plugin [den Support schrittweise beendet](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). 

Wenn Sie vor der Migration Unterstützung bei Ihrer Eclipse Integration benötigen, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

### Der Raw Event Stream (RES)

**Unterstützung zurückgezogen**: Juli 2018<br>
**Ersetzt durch**: [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)

Der Raw Event Stream war der Vorgänger von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) und wurde veraltet, um Platz für die Zukunft der Braze-Daten zu schaffen.

### Verzögerung im Leerlauf - GCM Feature

**Unterstützung zurückgezogen**: November 2016

Der Parameter Verzögerung im Leerlauf war früher Teil der [GCM Push-Optionen](https://developers.google.com/cloud-messaging/http-server-ref). Google hat die Unterstützung für diese Option am 15\. November 2016 zurückgezogen. Zuvor zeigte die Einstellung **true** an, dass die Nachricht erst gesendet werden sollte, wenn das Gerät aktiv wird.

### Angepasste Endpunkte

**Unterstützung zurückgezogen**: Dezember 2019

Entfernen von angepassten Endpunkten. Wenn Sie einen angepassten Endpunkt haben, können Sie diesen weiterhin verwenden, aber Braze gibt ihn nicht mehr heraus.


