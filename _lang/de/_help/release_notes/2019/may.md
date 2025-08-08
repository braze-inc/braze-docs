---
nav_title: Mai
page_order: 8
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Mai 2019."
---

# Mai 2019

## Content-Cards

Content-Cards sind persistente Inhalte, die in den App- und Internet-Erlebnissen der Kund:in erscheinen.

Mit Content-Cards können Sie einen zielgerichteten, dynamischen Stream mit reichhaltigen Inhalten an Ihre Kund:in senden, und zwar direkt in den Apps, die sie lieben, ohne ihr Erlebnis zu unterbrechen. Oder Sie können Content-Cards mit anderen Kanälen wie E-Mail oder Push-Benachrichtigungen kombinieren, um kohärente Marketing-Strategien zu ermöglichen.

![Content-Cards Feed]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

Darüber hinaus unterstützen Content-Cards mehr personalisierte Features, einschließlich Karten-Anheftung, Karten-Ausblendung, API-basierte Zustellung, angepasste Karten-Ablaufzeiten und Kartenanalysen.

Verwenden Sie es, um Benachrichtigungszentren, Homepage-Feeds und Feeds für Aktionen zu erstellen.

Sie müssen ein Update auf eine unterstützte Braze SDK-Version durchführen:
- iOS: 3.8.0 oder höher
- Android: 2.6.0 oder höher
- Web: 2.2.0 oder höher

[Erfahren Sie hier mehr über Content-Cards!]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)

{% alert update %}
Content-Cards für Currents und unsere API-Dokumentation für Content-Cards werden im Laufe dieser Woche veröffentlicht. Stay tuned!
{% endalert %}

## Erweiterung der Roku Plattform

Braze hat einen neuen Kanal zu unseren Möglichkeiten hinzugefügt! Durch die Expansion in neue Kanäle können wir unsere Kunden in die Lage versetzen, ihre Daten durch das Verständnis des Sehverhaltens anzureichern oder ihren Verbraucher:in über alle relevanten Kanäle hinweg sinnvolle Erlebnisse zu bieten.

Sie können jetzt [Daten von Roku-Geräten abrufen]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) und zur Datenanreicherung sowie zum angepassten Event Tracking nutzen.

## Benachrichtigungseinstellungen für Canvas- oder Kampagnen-Updates

Diese [neue Benachrichtigung]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences) informiert Sie per E-Mail, wenn eine Kampagne oder ein Canvas aktiviert, aktualisiert, reaktiviert oder deaktiviert wird. Aktivieren Sie dies in den **Einstellungen für Benachrichtigungen** in Ihrem Braze-Konto.

## Jampp Technologie Partner Dokumentation

Jampp ist eine Performance-Marketing-Plattform für die Akquisition und das Retargeting von Mobile-Kund:in. Es kombiniert Verhaltensdaten mit prognostischer und programmatischer Technologie, um Einnahmen für Werbetreibende zu generieren, indem es persönliche, relevante Anzeigen schaltet, die Verbraucher:in zum ersten Mal oder häufiger zum Kauf anregen.

Kunden:in von Braze können [sich mit Jampp integrieren]({{site.baseurl}}/partners/jampp/), indem sie den Braze-Webhook-Kanal so konfigurieren, dass er Events in Jampp streamt. Dadurch haben Kunden die Möglichkeit, ihre Retargeting-Initiativen mit Jampp innerhalb des Ökosystems für mobile Werbung um umfangreichere Datensätze zu erweitern.

## Plattformauswahl für In-App-Nachrichten

Mit unserem Plattform-Picker, der diesen Schritt bei der Erstellung von Kampagnen hervorhebt, können Sie leichter auswählen, wohin Ihre In-App-Nachrichten gesendet werden und für welche Plattformen sie bestimmt sind.

![Platform Picker]({% image_buster /assets/img/iam_platforms.gif %})

## Versand ID Currents Feld für E-Mail

{% alert update %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie "geplant" sind. Erfahren Sie mehr über [`dispatch_id` Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas und Kampagnen.

_Update im August 2019 vermerkt._
{% endalert %}

In dem Bestreben, unsere Currents-Funktionen weiter zu verbessern, fügen wir `dispatch_id` als Feld zu den E-Mail-Ereignissen von Currents für alle Konnektoren hinzu.

Die `dispatch_id` ist die eindeutige ID, die für jede von der Braze-Plattform gesendete Übertragung bzw. Sendung generiert wird.

Während alle Kund:innen, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` erhalten, bekommen Kunden, die entweder aktionsbasierte oder API-getriggerte Nachrichten erhalten, eine eindeutige `dispatch_id` pro Nachricht. Mit dem Feld `dispatch_id` können Sie feststellen, welche Instanz einer wiederkehrenden Kampagne für die Konversion verantwortlich ist. So erhalten Sie mehr Insights und Informationen darüber, welche Arten von Kampagnen dazu beitragen, Ihre Geschäftsziele zu erreichen.

## Feature zur Sortierung der Kampagne "Nur meine anzeigen"

Wenn ein Nutzer:in der Kampagnentabelle das Kontrollkästchen `Only Show Mine` aktiviert, werden die Ergebnisse nach Kampagnen gefiltert, die nur von dem angemeldeten Nutzer:in erstellt wurden. Zusätzlich kann der Nutzer:innen die Suchleiste nutzen, indem er `created_by_me:true` eingibt.

Außerdem ist die Seitenleiste des Kampagnen-Rasters jetzt in der Größe veränderbar!

## Nutzer:innen nach Alias löschen

Sie können jetzt den Endpunkt `users/delete` verwenden, um [Nutzer:innen nach Alias zu löschen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)!

## Eindeutige Berechnung für Klicks und Öffnungen von E-Mails

Eindeutige Klicks und eindeutige Öffnungen für E-Mails werden jetzt in einem 7-Tage-Zeitfenster pro Nutzer:in erfasst und angezeigt und innerhalb dieses 7-Tage-Fensters um 1 erhöht, und zwar für jede `dispatch_id`.

Mit `dispatch_id` ist es zulässig, dass wiederkehrende Nachrichten die tatsächliche eindeutige Öffnung oder die eindeutige Anzahl der Klicks jeder Nachricht widerspiegeln. Jetzt, da `dispatch_id` in Currents verfügbar ist, wird es für Kund:in einfach sein, diese Daten abzugleichen.

Alle Nutzer:innen, die auch Mailjet verwenden, werden einen Anstieg dieser Zahlen feststellen, da der bisherige Zeitrahmen für die Eindeutigkeit über 30 Tage betrug. Sie hätten vor drei (3) Wochen auf diese Änderung aufmerksam gemacht werden müssen.  Für SendGrid Kund:in sollte es keinen Unterschied geben.

Sie können nach diesen aktualisierten Begriffen in unserem [Glossar zu den Metriken des Berichts]({{site.baseurl}}/user_guide/data/report_metrics/) suchen.

{% alert update %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie "geplant" sind. [Erfahren Sie mehr über das [Verhalten von`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas und Kampagnen.

_Update im August 2019 vermerkt._
{% endalert %}


## Kanal mit dem größten Engagement

{% alert update %}
Ab der [Produktversion im November 2019]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite) wurde "Most Engaged Channel" in ["Intelligent Channel"]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) umbenannt.
{% endalert %}

Der Filter Most Engaged Channel wählt den Teil Ihrer Zielgruppe aus, für den der ausgewählte Messaging-Kanal der "beste" Kanal ist. In diesem Fall bedeutet "am besten" "hat die höchste Wahrscheinlichkeit eines Engagements, wenn man den Verlauf des Nutzers:in betrachtet". Sie können E-Mail, Web-Push oder Mobile-Push (das jedes verfügbare mobile Betriebssystem oder Gerät einschließt) als Kanal auswählen.

Testen Sie diesen neuen Filter in unserer Bibliothek [Segmentierungsfilter]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

