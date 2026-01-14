---
nav_title: Übersicht über die Plattform
article_title: Übersicht über die Plattform
page_order: 1
description: "Dieser Artikel beschreibt die grundlegenden Komponenten und Funktionen der Braze-Plattform. Links in diesem Artikel führen zu wichtigen Themen von Braze."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}Erste Schritte: Übersicht über die Plattform

> Dieser Artikel beschreibt die grundlegenden Komponenten und Funktionen der Braze-Plattform. Links in diesem Artikel führen zu wichtigen Themen von Braze. 

{% alert tip %}
Schauen Sie sich unseren kostenlosen Kurs [Developer Learning Path](https://learning.braze.com/path/developer) zusammen mit diesen Artikeln an.
{% endalert %}

## Was ist Braze?

Braze ist eine Plattform zur Kundenbindung. Das bedeutet ganz einfach, dass Braze Ihnen dabei hilft, Ihren Benutzern zuzuhören, ihre Handlungen und ihr Verhalten zu verstehen und dann entsprechend zu handeln. Die Braze-Plattform weist drei Hauptkomponenten auf: das SDK, das Dashboard und die REST API.

Für Marketer, die einen allgemeinen Überblick über Braze suchen, empfiehlt sich stattdessen der Abschnitt [Erste Schritte für Marketer]({{site.baseurl}}/user_guide/getting_started/overview/).

![Braze hat verschiedene Schichten. Insgesamt besteht es aus dem SDK, der API, dem Dashboard und den Partnerintegrationen. Diese tragen jeweils zu einem Datenaufnahme-Layer, einem Klassifizierungs-Layer, einem Orchestrierungs-Layer, einem Personalisierungs-Layer und einem Aktions-Layer bei. Der Aktions-Layer verfügt über verschiedene Kanäle, darunter Push, In-App-Nachrichten, verbundener Katalog, Webhook, SMS und E-Mail.]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

Die [Braze SDKs](#integrating-braze) können in Ihre Mobil- und Webanwendungen integriert werden, um leistungsstarke Tools für das Marketing, die Nutzerverwaltung und die Analyse bereitzustellen.

Kurz gesagt, wenn das SDK vollständig integriert ist, weist es folgende Eigenschaften auf:

* Sammelt und synchronisiert Benutzerdaten in einem konsolidierten Benutzerprofil
* Sammelt automatisch Sitzungsdaten, Geräteinformationen und Push-Tokens
* Es erfasst Marketing-Engagement-Daten und angepasste Daten speziell für Ihr Unternehmen
* Ist auf Sicherheit ausgelegt und wird von Dritten auf Penetration getestet
* Ist optimiert für Geräte mit niedrigem Batteriestand oder langsamem Netzwerk
* Unterstützt serverseitige JWT-Signaturen für zusätzliche Sicherheit
* Hat schreibgeschützten Zugriff auf Ihre Systeme (kann keine Benutzerdaten abrufen)
* Unterstützt Push-Benachrichtigungen, In-App-Nachrichten und Content-Card-Nachrichtenkanäle

### Dashboard Benutzeroberfläche

Das Dashboard ist die UI, die alle Daten und Interaktionen im Zentrum der Braze-Plattform steuert. Marketer nutzen das Dashboard, um ihre Arbeit zu erledigen und Inhalte zu erstellen. Entwickler nutzen das Dashboard, um Einstellungen für die Integration von Apps zu verwalten, wie z. B. API-Schlüssel und Zugangsdaten für Push-Benachrichtigungen.

Wenn Sie gerade erst anfangen, sollte Ihr Teamadministrator Sie (und alle anderen Teammitglieder, die Zugriff auf Braze benötigen) als [Benutzer in Ihrem Dashboard]({{site.baseurl}}/user_guide/administrative/access_braze) hinzufügen.

### REST API

Mit der Braze-API können Sie Daten in großem Umfang in und aus Braze verschieben. Verwenden Sie die API, um Updates aus dem Backend, aus Data Warehouses sowie aus anderen Erst- und Drittanbieterquellen einzubringen. Darüber hinaus können Sie die API nutzen, um angepasste Events zu Segmentierungszwecken direkt aus webbasierten Anwendungen hinzuzufügen. Sie können Nachrichten über die API triggern und versenden, sodass technische Ressourcen komplexe JSON-Metadaten in Ihre Kampagnen aufnehmen können.

Die API stellt zudem einen Webdienst bereit, mit dem Sie Aktionen Ihrer Nutzer direkt über HTTP aufzeichnen können, anstatt über die SDKs für Mobilgeräte und Web. In Kombination mit Webhooks bedeutet dies, dass Sie Aktionen verfolgen und Aktivitäten für Nutzer innerhalb und außerhalb Ihrer App triggern können. Der [API-Leitfaden]({{site.baseurl}}/api/home) enthält eine Liste der verfügbaren Braze-API-Endpunkte und ihrer Verwendungsmöglichkeiten.

Mehr über die Teile und Komponenten von Braze finden Sie hier: [Erste Schritte: Überblick über die Architektur]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Datenanalyse und Maßnahmen

Die in Braze gespeicherten Daten bleiben erhalten und können für Segmentierung, Personalisierung und Targeting verwendet werden, solange Sie Kunde bei Braze sind. So können Sie auf Nutzerprofildaten (z. B. Sitzungsaktivitäten oder Käufe) zugreifen, bis Sie sich entscheiden, diese Informationen zu löschen. Ein Streaming-Dienst könnte zum Beispiel die angesehenen Inhalte jedes Abonnenten vom ersten Tag an verfolgen (auch wenn das schon viele Jahre her ist) und diese Daten nutzen, um relevante Nachrichten zu versenden.

![Segment im Braze-Dashboard mit der Bezeichnung "Aktuelle Käufer" neben einem Telefonbildschirm, auf dem eine E-Mail mit "Top-Empfehlungen für Linda" angezeigt wird.]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### App-Analysen

Das Braze-Dashboard zeigt Diagramme an, die in Echtzeit auf der Grundlage von Analytics-Metriken und angepassten Events, die Sie in Ihrer Anwendung instrumentieren, aktualisiert werden. Die konsequente Messung und Optimierung Ihrer Kampagnen mit A/B-Tests, benutzerdefinierten Berichten und Analysen sowie automatisierten Informationen hilft Ihnen, Ihre Kunden zu binden und sich von den Wettbewerbern in Ihrem Bereich abzuheben.

### Benutzer-Segmentierung

Mit der Segmentierung können Sie Nutzergruppen auf der Grundlage von leistungsstarken Filtern ihres In-App-Verhaltens, demografischen Daten und Ähnlichem erstellen. Außerdem haben Sie in Braze die Möglichkeit, jede In-App-Nutzeraktion als "angepasstes Event" zu definieren, wenn die gewünschte Aktion nicht standardmäßig erfasst wird. Dasselbe gilt für Benutzermerkmale über "benutzerdefinierte Attribute". Nachdem ein Benutzersegment auf dem Dashboard erstellt wurde, bewegen sich Ihre Benutzer in das Segment hinein und aus ihm heraus, wenn sie die definierten Kriterien erfüllen (oder nicht erfüllen). Sie können z.B. ein Segment erstellen, das alle Nutzer umfasst, die in der App Geld ausgegeben haben und die App zuletzt vor mehr als zwei Wochen genutzt haben.

Mehr über unsere Datenmodelle erfahren Sie hier: [Erste Schritte: Übersicht über Analysen]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Multichannel-Messaging

Nachdem Sie ein Segment definiert haben, können Sie mit den Messaging-Tools von Braze auf dynamische, personalisierte Weise mit Ihren Benutzern in Kontakt treten. Braze wurde mit einem kanalunabhängigen, nutzerzentrierten Datenmodell entwickelt. Die Nachrichtenübermittlung erfolgt innerhalb Ihrer App oder Website (z. B. durch das Versenden von In-App-Nachrichten oder durch grafische Elemente wie Content Card-Karusselle und Banner) oder außerhalb Ihrer App (z. B. durch das Versenden von Push-Benachrichtigungen oder E-Mails). So können Ihre Marketingexperten beispielsweise eine Push-Benachrichtigung und eine E-Mail an das im vorherigen Abschnitt definierte Beispielsegment senden.

![Erstellen und triggern Sie personalisierte Nachrichten auf jedem Kanal – sowohl außerhalb als auch innerhalb Ihrer App oder Website.]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| Kanal                                                                                              | Beschreibung                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Content-Cards*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) | Senden Sie zielgerichtete und dynamische In-App-Benachrichtigungen, ohne den Kunden zu unterbrechen. |
| [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | Versenden Sie Rich-HTML-Nachrichten, indem Sie Ihre E-Mail mit dem Rich-Text-Editor, unserem Drag-and-Drop-Editor oder durch Hochladen einer Ihrer vorhandenen HTML-Vorlagen erstellen. |
| [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Senden Sie unaufdringliche In-App-Benachrichtigungen über die speziell entwickelte, native Benutzeroberfläche von Braze. |
| [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | Triggern Sie automatisch Push-Benachrichtigungen von Messaging-Kampagnen oder Newsfeed-Elementen, indem Sie den Apple Push Notification Service (APNs) für iOS oder Firebase Cloud Messaging (FCM) für Android verwenden. |
| [SMS, MMS und RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs) | Nutzen Sie SMS, MMS oder RCS, um Transaktionsbenachrichtigungen zu versenden, Aktionen zu teilen, Erinnerungen zu senden und vieles mehr. |
| [Web-Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | Senden Sie Webbrowser-Benachrichtigungen, auch wenn Ihre Nutzer gerade nicht auf Ihrer Website aktiv sind. |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Verwenden Sie Webhooks, um Aktionen außerhalb der App zu triggern und andere Systeme und Anwendungen mit Echtzeitdaten zu versorgen. |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | Stellen Sie eine direkte Verbindung zu Ihren Nutzern und Kunden her, indem Sie die beliebte Peer-to-Peer-Messaging-Plattform nutzen: WhatsApp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Als Add-on-Feature erhältlich\*\*.</sup>

### Anpassbare Komponenten

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> Alle Komponenten von Braze sind barrierefrei, anpassungsfähig und individuell gestaltbar. Sie können mit Braze beginnen, indem Sie die Standardkomponenten der `BrazeUI` verwenden und sie an Ihre Marke und Ihren Anwendungsfall anpassen.
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> Um über die Standardoptionen hinauszugehen, können Sie benutzerdefinierten Code schreiben, um das Aussehen eines Nachrichtenkanals zu aktualisieren, damit er besser zu Ihrer Marke passt. So können Sie beispielsweise die Schriftart, die Schriftgröße und die Farbe der Komponenten ändern. Marketer behalten direkt im Braze-Dashboard die Kontrolle über die Zielgruppe, den Inhalt, das On-Click-Verhalten und den Ablauf von Kampagnen.
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> Sie können auch vollständig angepasste Komponenten erstellen, um zu steuern, wie Ihre Nachrichten aussehen, wie sie sich verhalten und wie sie mit anderen Messaging-Kanälen interagieren (z. B. Triggern einer Content-Card auf der Grundlage einer Push-Benachrichtigung). Braze bietet SDK-Methoden, mit denen Sie Metriken wie Impressionen, Klicks und Ausblendungen im Braze-Dashboard protokollieren können. Für jeden Messaging-Kanal gibt es einen Analyse-Artikel mit hilfreichen Informationen.
{% endgallery %}

<br>
<br>

## Integration von Braze

Braze ist so konzipiert, dass Sie es schnell und einfach in Betrieb nehmen können. Unsere durchschnittliche Time-to-Value beträgt sechs Wochen bei unserem Kundenstamm von Hunderten von Marken. Mehr über den Integrationsprozess erfahren Sie hier: [Erste Schritte: Übersicht über die Integration]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

## Ressourcen als Lesezeichen

Als technische Ressource werden Sie an vielen Details von Braze beteiligt sein. Hier finden Sie gute Quellen, die Sie sich außerhalb unserer Dokumentation merken sollten. Halten Sie unser Glossar mit [den wichtigsten Begriffen]({{site.baseurl}}/user_guide/getting_started/terms_to_know/) für den Fall bereit, dass Sie Fragen zu den Begriffen von Braze haben.

| Ressource | Was Sie lernen werden|
|---|---|
| [Fehlersuche im SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | Bei der Fehlerbehebung Ihrer Integration ist das Debugging-Tool des SDK ein hilfreiches Tool. Stellen Sie sicher, dass Sie es zur Hand haben! |
| [Öffentliches GitHub von Braze](https://github.com/braze-inc/) | In unserem GitHub-Repository finden Sie ausführliche Informationen zur Integration und Beispielcode. |
| [GitHub-Repository für Android SDK](https://github.com/braze-inc/braze-android-sdk/) | Das Android SDK GitHub-Repository. |
| [Android SDK-Referenz](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Klassendokumentation für das Android SDK. |
| [iOS (Swift) SDK GitHub Repository](https://github.com/braze-inc/braze-swift-sdk) | Das Swift SDK GitHub-Repository. |
| [iOS (Swift) SDK Referenz](https://braze-inc.github.io/braze-swift-sdk/) | Klassendokumentation für das iOS SDK. |
| [GitHub-Repository für Web SDK](https://github.com/braze-inc/braze-web-sdk) | GitHub Repository für das Web-SDK. |
| [Web SDK-Referenz](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | Klassendokumentation für das iOS SDK. |
| [SDK-Changelogs]({{site.baseurl}}/developer_guide/changelogs) | Braze bietet zusätzlich zu den Releases für kritische Probleme und größere Betriebssystem-Updates auch monatliche Releases an. |
| [Braze API Postman-Kollektion](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Laden Sie hier unsere Postmann-Kollektion herunter.  |
| [Braze Systemstatus-Monitor](https://braze.statuspage.io/) | Unsere Statusseite wird immer dann aktualisiert, wenn es zu Zwischenfällen oder Ausfällen kommt. Gehen Sie auf diese Seite, um die Benachrichtigungen zu abonnieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

