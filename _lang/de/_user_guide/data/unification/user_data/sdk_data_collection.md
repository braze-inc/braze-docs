---
nav_title: SDK Datenerfassung
article_title: SDK Datenerfassung
page_order: 1
page_type: reference
description: "Dieser Artikel befasst sich mit den Daten, die vom SDK über personalisierte Integrationen, automatisch erfasste Integrationen und minimale Integrationen gesammelt werden."

---

# SDK Datenerfassung

> Wenn Sie das Braze SDK in Ihre App oder Website integrieren, sammelt Braze automatisch bestimmte Arten von Daten. Einige dieser Daten sind für unsere Prozesse unerlässlich, und einige dieser Daten können je nach Ihren Bedürfnissen ein- oder ausgeschaltet werden. Sie können Braze auch so konfigurieren, dass es weitere Datentypen erfasst, um Segmentierung und Kommunikation zu verbessern.

Braze ist auf eine flexible Datenerfassung ausgelegt. Daher können Sie das Braze SDK auf folgende Weise integrieren:

- **[Minimale Integration](#minimum-integration):** Braze sammelt automatisch Daten, die für die Kommunikation mit den Braze-Diensten erforderlich sind.
- **[Optionale Daten, die standardmäßig erfasst werden](#optional-data-collected-by-default):** Braze erfasst automatisch bestimmte Daten, die für die meisten Anwendungsfälle nützlich sind. Sie können die automatische Erfassung dieser Daten deaktivieren, wenn sie für die Kommunikation mit den Serviceleistungen; Diensten von Braze nicht erforderlich sind.
- **[Optionale Daten, die standardmäßig nicht erfasst werden](#data-not-collected-by-default):** Braze erfasst bestimmte Daten, die für einzelne Anwendungsfälle nützlich sind, tut dies aber aufgrund von Regulierungsvorschriften nicht automatisch. Sie können diese Daten in den Fällen erfassen lassen, in denen dies zweckdienlich ist.
- **[Personalisierte Integration](#personalized-integration):** Braze bietet Ihnen die Möglichkeit, zusätzlich zu den standardmäßigen optionalen Daten weitere Daten zu erfassen.

## Minimale Integration

Hier finden Sie die zwingend erforderlichen Daten, die Braze bei der Initialisierung des SDK erzeugt und empfängt. Diese Daten sind nicht konfigurierbar und für die Kernfunktionen der Plattform unerlässlich. Mit Ausnahme des Sitzungsbeginns und des Sitzungsendes werden alle anderen automatisch getrackten Daten nicht auf die Datenpunkt-Nutzung angerechnet.

| Attribut | Beschreibung | Hintergründe der Datenerfassung |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | Die aktuellste Version der App | Dieses Attribut wird verwendet, um Nachrichten über die Kompatibilität der App-Version an die richtigen Geräte zu senden. Es kann verwendet werden, um Benutzer über Dienstunterbrechungen und Fehler zu informieren. |
| Land | Durch Geolocation der IP-Adresse identifiziertes Land. Wenn die Geolocation der IP-Adresse nicht verfügbar ist, wird diese durch die [Lokalisierung des Geräts](#optional-data-collected-by-default) identifiziert. Der Wert könnte alternativ auch das sein, was die SDKs direkt mit `setCountry` festlegen. Beachten Sie jedoch, dass die Übergabe eines Attribut-Wertes durch ein SDK oder eine API Datenpunkte protokollieren wird.| Dieses Attribut wird verwendet, um Nachrichten auf der Grundlage des Standorts zu versenden. |
| Geräte-ID | Bezeichner des Geräts, ein zufällig generierter String | Dieses Attribut wird verwendet, um die Geräte der Nutzer:innen zu unterscheiden und Nachrichten an das richtige Gerät zu senden. |
| OS und OS-Version | Aktuell gemeldetes Gerät oder Browser und Geräte- oder Browserversion | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden. Es kann auch im Rahmen der Segmentierung verwendet werden, um Nutzer:innen für Upgrades von App-Versionen anzusprechen. |
| Sitzungsbeginn und Sitzungsende | Wenn der Nutzer:innen beginnt, Ihre integrierte App oder Website zu nutzen | Das Braze SDK meldet die vom Braze-Dashboard verwendeten Sitzungsdaten, um das Benutzerengagement und andere Zahlen zu berechnen, die für Benutzeranalysen wichtig sind. Wann genau Sitzungsbeginn und -ende von Ihrer App bzw. Website gemeldet werden, kann konfiguriert werden [(Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). |
| SDK-Daten zur Nachrichteninteraktion | Direkte Push-Öffnungen, In-App-Nachricht-Interaktionen, Content-Card-Interaktionen | Dieses Attribut wird zur Qualitätskontrolle verwendet, z.B. um zu überprüfen, ob eine Nachricht eingegangen ist und ob sie nicht doppelt gesendet wurde. |
| SDK-Version | Aktuelle SDK-Version | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden und Dienstunterbrechungen zu vermeiden. |
| Sitzungs-ID und -Zeitstempel | Sitzungskennung: zufällige Zeichenfolge und Zeitstempel | Wird verwendet, um festzustellen, ob der Nutzer:in eine neue oder eine bestehende Sitzung eintritt und um zu bestimmen, ob Nachrichten, die für diesen Nutzer:innen bestimmt sind, erneut zugestellt werden können.<br><br>Bestimmte Nachrichtenkanäle wie In-App-Nachrichten und Content-Cards werden zu Beginn der Sitzung mit dem Gerät synchronisiert. Unser Backend verwendet dann die Daten des letzten Kontakts mit den Servern von Braze (die das Gerät speichert und zurücksendet), um festzustellen, ob der Nutzer:innen für neue Nachrichten berechtigt ist.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Berechnete Metriken

Braze erstellt Kennzahlen anhand von SDK-Daten, Interaktionsdaten zu Nicht-SDK-Nachrichten und daraus abgeleiteten Informationen. Zur Verdeutlichung: Die errechneten Daten werden nicht vom SDK erfasst, sondern von Braze generiert. Benutzerprofile enthalten sowohl erfasste als auch generierte Daten. 

Die berechneten Metriken umfassen die folgenden Attribute.

| Attribut                                      | Beschreibung                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| Zuerst verwendete App                                 | Uhrzeit                                                                 |
| Zuletzt verwendete App                                  | Uhrzeit                                                                 |
| Sitzungsanzahl insgesamt                            | Zahl                                                               |
| Geklickte Karte                                   | Zahl                                                               |
| Zuletzt empfangene Nachricht                     | Uhrzeit                                                                 |
| Zuletzt erhaltene E-Mail Kampagne                   | Uhrzeit                                                                 |
| Zuletzt eingegangene Push-Kampagne                    | Uhrzeit                                                                 |
| Anzahl der Artikel im Feedback                       | Zahl                                                               |
| Anzahl der Sitzungen in den letzten Y Tagen          | Nummer und Uhrzeit                                                      |
| Empfangene Nachricht der Kampagne                  | Boolesch. Dieser Filter gibt Benutzer aus, denen eine frühere Kampagnen zugestellt worden ist.                               |
| Empfangene Nachricht von Kampagne mit Tag        | Boolesch. Dieser Filter gibt Benutzer aus, denen eine frühere Kampagnen zugestellt worden ist, die derzeit mit einem Tag versehen ist.                  |
| Retarget-Kampagne                              | Boolesch. Dieser Filter stellt Nutzer:innen darauf ab, ob sie in der Vergangenheit eine bestimmte E-Mail, Push- oder In-App-Nachricht geöffnet oder angeklickt haben. |
| Deinstalliert                                    | Boolesch und Zeit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Wenn Sie nur an der minimalen Integration interessiert sind und Sie mParticle, Segment, Tealium oder GTM verwenden, beachten Sie Folgendes:
- **Mobile Plattformen**: Sie müssen den Code für derartige Konfigurationen manuell anpassen. mParticle und Segment bieten keine Möglichkeit, dies über ihre Plattform zu tun. 
- **Web**: Die Braze-Integration muss nativ erfolgen, um eine minimale Integration zu ermöglichen. Tag-Manager bieten keine Möglichkeit, dies über ihre Plattform zu tun.
{% endalert %} 

## Standardmäßig erfasste optionale Daten

Zusätzlich zu den Daten für die minimale Integration werden die folgenden Attribute automatisch von Braze erfasst, wenn Sie die SDK-Integration initialisieren. Sie können sich [gegen die Erfassung dieser Attribute entscheiden]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection), um eine minimale Integration zu ermöglichen.

| Attribut               | Plattform          | Beschreibung                                                                        | Hintergründe der Datenerfassung                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Browsername            | Internet               | Name des Browsers                                                                | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Browser zu senden. Es kann auch für die browserbasierte Segmentierung verwendet werden.                                     |
| Gerätegebietsschema           | Android, iOS      | Das Standardgebietsschema des Geräts                                                   | Dieses Attribut wird verwendet, um Nachrichten in die vom Benutzer bevorzugte Sprache zu übersetzen.                                                                                            |
| Neueste Lokalisierung des Geräts           | Android, iOS      | Die letzte Standard Lokalisierung des Geräts                                                   | Dieses Attribut stammt aus den Geräteeinstellungen des Nutzers und wird verwendet, um Nachrichten in die bevorzugte Sprache des Nutzers:innen zu übersetzen. Sie ist unabhängig von dem Attribut `Most Recent Location`.                                                                                            |
| Gerät Modell            | Android, iOS      | Die spezifische Hardware des Geräts                                                | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden. Er kann auch im Rahmen der Segmentierung verwendet werden.                                                 |
| Gerätemarke            | Android           | Die Marke des Geräts (z. B. Samsung)                                         | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden.                                                                                          |
| Mobilfunkanbieter | Android, iOS      | Der Mobilfunkanbieter                                                                 | Dieses Attribut wird optional für das Targeting von Nachrichten verwendet.<br><br>**Hinweis:** Dieses Feld ist seit iOS 16 veraltet und wird in einer zukünftigen iOS-Version standardmäßig auf `--` gesetzt. |
| Sprache                | Android, iOS, Internet | Geräte- oder Browsersprache, entnommen aus dem Gebietsschema des Geräts                                                            | Dieses Attribut wird verwendet, um Nachrichten in die bevorzugte Sprache eines Nutzers:in zu übersetzen. Sie basiert auf dem Gebietsschema des Geräts.                                                                                            |
| Einstellungen für Benachrichtigungen   | Android, iOS, Internet | Ob in dieser App Push-Benachrichtigungen aktiviert sind.                                   | Dieses Attribut wird verwendet, um Push-Benachrichtigungen zu aktivieren.                                                                                                                    |
| Auflösung              | Android, iOS, Internet | Gerät oder Browser-Auflösung                                                          | Wird optional für gerätebasiertes Messaging Targeting verwendet. Das Format dieses Wertes ist "`<width>`x`<height>`".                                                                 |
| Zeitzone               | Android, iOS, Internet | Zeitzone des Geräts oder des Browsers                                                           | Dieses Attribut wird verwendet, um Nachrichten je nach Zeitzone des Benutzers zum richtigen Zeitpunkt zu versenden.                                                   |
| Benutzer-Agent              | Internet               | [Benutzer-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden. Er kann auch im Rahmen der Segmentierung verwendet werden.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Wenn Sie mehr über Geräteeigenschaften (wie Mobilfunkanbieter, Zeitzone, Auflösung etc.) erfahren möchten, lesen Sie die Dokumentation zur jeweiligen Plattform: [Android]({{site.baseurl}}/developer_guide/storage/?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage/?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage/#cookies).

## Standardmäßig nicht erfasste Daten

Standardmäßig werden die folgenden Attribute nicht erfasst. Jedes Attribut muss manuell integriert werden.

| Attribut                  | Plattform     | Beschreibung                                                                                                                                                                                                                                                                                                               | Warum es nicht gesammelt wird                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ad-Tracking auf Gerät aktiviert | Android, iOS | Auf iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Auf Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Diese Eigenschaft erfordert zusätzliche App-Berechtigungen durch den Integrator.                                                                                                                                                                                      |
| Geräte-IDFA                | iOS          | Gerätekennung für Werbetreibende                                                                                                                                                                                                                                                                                         | Erfordert das Ad Tracking Transparency Framework, das eine zusätzliche Datenschutzprüfung durch den App Store veranlasst. Weitere Informationen finden Sie unter [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| Google Advertising ID      | Android      | Bezeichner für Werbung in Google Play Apps                                                                                                                                                                                                                                                                        | Dazu muss die App die GAID abrufen und sie an Braze weitergeben. Weitere Einzelheiten finden Sie unter [Optionale Google Advertising ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Jüngster Standort | Android, iOS | Dies ist der letzte bekannte GPS-Standort des Nutzer:innen-Geräts. Diese wird beim Start der Sitzung aktualisiert und im Profil des Nutzers:innen gespeichert. | Dazu muss der Nutzer:innen Ihrer App die Erlaubnis zum Standort erteilen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Das Braze SDK speichert keine IP-Adressen lokal.
{% endalert %}

## Personalisierte Integration

Um das Beste aus Braze herauszuholen, implementieren unsere SDK-Integratoren häufig die SDKs von Braze und protokollieren zusätzlich zu den automatisch erfassten Daten [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) und [Kauf-Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events), die für ihr Geschäft relevant sind.

Eine personalisierte Integration ermöglicht eine angepasste Kommunikation, die auf die Erfahrungen Ihrer Nutzer:innen abgestimmt ist.

{% alert important %}
Braze sperrt bzw. blockiert Benutzer mit mehr als 5.000.000 Sitzungen ("Dummy-Benutzer") und lässt ihre SDK-Ereignisse außer Acht. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}


