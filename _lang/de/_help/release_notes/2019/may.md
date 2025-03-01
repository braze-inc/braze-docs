---
nav_title: Mai
page_order: 8
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Mai 2019."
---

# Mai 2019

## Inhaltskarten

Content Cards sind dauerhafte Inhalte, die in der App und im Web der Kunden erscheinen.

Mit Content Cards können Sie einen gezielten, dynamischen Strom reichhaltiger Inhalte an Ihre Kunden senden, und zwar direkt in den von ihnen geliebten Apps, ohne ihr Erlebnis zu unterbrechen. Oder Sie können Content Cards mit anderen Kanälen wie E-Mail oder Push-Benachrichtigungen kombinieren, um kohärente Marketingstrategien zu ermöglichen.

![Inhalt Karten Feed]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

Darüber hinaus unterstützen Content Cards mehr personalisierte Funktionen, wie z. B. das Anheften von Karten, das Ablegen von Karten, die API-basierte Bereitstellung, benutzerdefinierte Ablaufzeiten für Karten und Kartenanalysen.

Verwenden Sie es, um Benachrichtigungszentren, Homepage-Feeds und Promotion-Feeds zu erstellen.

Sie müssen auf eine unterstützte Braze SDK-Version aktualisieren:
- iOS: 3.8.0 oder höher
- Android: 2.6.0 oder höher
- Web: 2.2.0 oder höher

[Erfahren Sie hier mehr über Content Cards!]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/)

{% alert update %}
Content Cards für Currents und unsere API-Dokumentation für Content Cards werden im Laufe dieser Woche veröffentlicht. Stay tuned!
{% endalert %}

## Erweiterung der Roku Plattform

Braze hat einen neuen Kanal zu unseren Möglichkeiten hinzugefügt! Durch die Expansion in neue Kanäle können wir es unseren Kunden ermöglichen, ihre Daten durch ein besseres Verständnis des Sehverhaltens anzureichern oder ihren Kunden auf allen relevanten Kanälen sinnvolle Erlebnisse zu bieten.

Sie können jetzt [Daten von Roku-Geräten]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) zur Datenanreicherung und benutzerdefinierten Ereignisverfolgung [abrufen]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/).

## Benachrichtigungseinstellungen für Canvas- oder Kampagnen-Updates

Diese [neue Benachrichtigung]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences) informiert Sie per E-Mail, wenn eine Kampagne oder ein Canvas aktiviert, aktualisiert, reaktiviert oder deaktiviert wird. Aktivieren Sie dies in den **Einstellungen für Benachrichtigungen** in Ihrem Braze-Konto.

## Dokumentation für Technologiepartner von Jampp

Jampp ist eine Performance-Marketing-Plattform für die Akquise und das Retargeting von mobilen Kunden. Es kombiniert Verhaltensdaten mit prädiktiver und programmatischer Technologie, um Einnahmen für Werbetreibende zu generieren, indem persönliche, relevante Anzeigen geschaltet werden, die die Verbraucher zum ersten oder häufigeren Kauf anregen.

Braze-Kunden können [Jampp integrieren]({{site.baseurl}}/partners/advertising_technologies/retargeting/jampp/), indem sie den Braze-Webhook-Kanal so konfigurieren, dass er Ereignisse in Jampp streamt. Dadurch haben Kunden die Möglichkeit, ihre Retargeting-Initiativen mit Jampp innerhalb des Ökosystems der mobilen Werbung um umfangreichere Datensätze zu erweitern.

## Plattform-Auswahl für In-App-Nachrichten

Mit unserer Plattformauswahl, die diesen Schritt bei der Kampagnenerstellung hervorhebt, können Sie leichter auswählen, wohin Ihre In-App-Nachrichten gesendet werden und für welche Plattformen sie gedacht sind.

![Plattform Picker][1]

## Versand-ID Aktuelles Feld für E-Mail

{% alert update %}
Das Verhalten von `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Einstiegsschritten, die geplant werden können) als ausgelöste Ereignisse behandelt, selbst wenn sie "geplant" sind. Erfahren Sie mehr über [`dispatch_id` Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas und Kampagnen.

_Aktualisierung im August 2019 vermerkt._
{% endalert %}

Um unsere Currents-Funktionen weiter zu verbessern, fügen wir `dispatch_id` als Feld zu den Currents-E-Mail-Ereignissen für alle Verbindungsarten hinzu.

Die `dispatch_id` ist die eindeutige ID, die für jede von der Braze-Plattform gesendete Übertragung oder Sendung generiert wird.

Während alle Kunden, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` erhalten, erhalten Kunden, die entweder aktionsbasierte oder API-ausgelöste Nachrichten erhalten, eine eindeutige `dispatch_id` pro Nachricht. Mit dem Feld `dispatch_id` können Sie feststellen, welche Instanz einer wiederkehrenden Kampagne für die Konversion verantwortlich ist. So erhalten Sie mehr Einblicke und Informationen darüber, welche Arten von Kampagnen dazu beitragen, Ihre Geschäftsziele zu erreichen.

## "Sortierfunktion der Kampagne "Nur meine anzeigen

Wenn ein Benutzer das Kontrollkästchen `Only Show Mine` in der Kampagnentabelle aktiviert, werden die Ergebnisse nach Kampagnen gefiltert, die nur von dem eingeloggten Benutzer erstellt wurden. Außerdem kann der Benutzer die Suchleiste verwenden, indem er `created_by_me:true` eingibt.

Außerdem ist die Seitenleiste des Kampagnenrasters jetzt in der Größe veränderbar!

## Benutzer nach Alias löschen

Sie können jetzt den Endpunkt `users/delete` verwenden, um [Benutzer nach Alias zu löschen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)!

## Einzigartige Berechnung für E-Mail-Klicks und Öffnungen

Einmalige Klicks und einmalige Öffnungen für E-Mails werden jetzt in einem 7-Tage-Zeitfenster pro Benutzer erfasst und angezeigt und innerhalb dieses 7-Tage-Fensters um 1 erhöht, und zwar für jedes `dispatch_id`.

Die Verwendung von `dispatch_id` ermöglicht es, dass wiederkehrende Nachrichten die tatsächliche Anzahl der einmaligen Öffnungen oder Klicks jeder einzelnen Nachricht widerspiegeln. Jetzt, wo `dispatch_id` in Currents verfügbar ist, wird es für die Kunden einfach sein, diese Daten abzugleichen.

Alle Benutzer, die auch Mailjet verwenden, werden einen Anstieg dieser Zahlen feststellen, da der bisherige Zeitrahmen für die Einzigartigkeit über 30 Tage betrug. Sie hätten vor drei (3) Wochen auf diese Änderung aufmerksam gemacht werden müssen.  SendGrid-Kunden sollten keinen Unterschied bemerken.

Sie können nach diesen aktualisierten Begriffen in unserem [Glossar zu den Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) suchen.

{% alert update %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Einstiegsschritten, die geplant werden können) als ausgelöste Ereignisse behandelt, selbst wenn sie "geplant" sind. [Erfahren Sie mehr über das [Verhalten von`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas und Kampagnen.

_Aktualisierung im August 2019 vermerkt._
{% endalert %}


## Meist genutzter Kanal

{% alert update %}
Ab der [Produktversion vom November 2019]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite) wurde "Most Engaged Channel" in ["Intelligent Channel"]({{site.baseurl}}/user_guide/intelligence/intelligent_channel/) umbenannt [.]({{site.baseurl}}/user_guide/intelligence/intelligent_channel/)
{% endalert %}

Der Filter "Engagiertester Kanal" wählt den Teil Ihrer Zielgruppe aus, für den der ausgewählte Nachrichtenkanal der "beste" Kanal ist. In diesem Fall bedeutet "am besten", dass die Wahrscheinlichkeit eines Engagements angesichts der Historie des Nutzers am höchsten ist. Sie können E-Mail, Web-Push oder Mobile-Push (das jedes verfügbare mobile Betriebssystem oder Gerät einschließt) als Kanal auswählen.

Testen Sie diesen neuen Filter in unserer [Segmentierungsfilter-Bibliothek]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

[1]: {% image_buster /assets/img/iam_platforms.gif %}
