---
nav_title: Architektonische Übersicht
article_title: Architektonische Übersicht
page_order: 3
description: "Dieser Artikel beschreibt die verschiedenen Teile des Technologie-Stacks von Braze und enthält Links zu relevanten Artikeln."
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

# Die ersten Schritte: Architektonische Übersicht

> Dieser Artikel beschreibt die verschiedenen Teile des Technologie-Stacks von Braze und enthält Links zu relevanten Artikeln. 

Bei Braze geht es in erster Linie um Daten. Die Braze-Plattform, unterstützt durch das SDK, die REST API und Partnerintegrationen, erlaubt Ihnen, Daten zu aggregieren und darauf zu reagieren. 

![Braze hat verschiedene Schichten. Insgesamt besteht es aus dem SDK, der API, dem Dashboard und den Partnerintegrationen. Diese tragen jeweils zu einem Datenaufnahme-Layer, einem Klassifizierungs-Layer, einem Orchestrierungs-Layer, einem Personalisierungs-Layer und einem Aktions-Layer bei. Der Aktions-Layer verfügt über verschiedene Kanäle, darunter Push, In-App-Nachrichten, verbundener Katalog, Webhook, SMS und E-Mail.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Datenaufnahme](#ingestion): Braze bezieht Daten aus einer Vielzahl von Quellen.
* [Klassifizierung](#classification): Ihr Marketing Team segmentiert Ihre Nutzer:innen dynamisch anhand dieser Metriken. 
* [Orchestrierung](#orchestration): Braze koordiniert auf intelligente Weise Nachrichten an verschiedene Segmente der Zielgruppe zum idealen Zeitpunkt.
* [Aktion](#action): Ihr Marketing Team arbeitet mit den Daten und erstellt Inhalte über eine Vielzahl von Messaging-Kanälen wie SMS und E-Mail.
* [Personalisierung](#personalization): Die Daten werden in Realtime mit personalisierten Informationen über Ihre Zielgruppe transformiert. 
* [Export](#exporting-data): Anschließend verfolgt Braze das Engagement Ihrer Nutzer:innen für diese Nachrichten und speist es in die Plattform ein, wodurch ein Kreislauf entsteht. Sie erhalten Insights in diese Daten durch Realtime-Berichte und Analytics.

All dies zusammen sorgt für erfolgreiche Interaktionen zwischen Ihrer Nutzerbasis und Ihrer Marke. Braze bietet das alles im Rahmen eines vertikal integrierten Stacks. Lassen Sie uns jede Schicht einzeln untersuchen.

## Datenaufnahme {#ingestion}

Braze basiert auf einer Streaming-Daten-Architektur, die Snowflake, Kafka, MongoDB und Redis nutzt. Daten aus vielen Quellen können über SDK und API in Braze geladen werden. Die Plattform kann alle Daten in Realtime verarbeiten, unabhängig davon, wie verschachtelt oder strukturiert sie sind. Die Daten in Braze werden im Benutzerprofil gespeichert. 

{% alert tip %}
Braze kann die Daten eines Nutzers während seiner gesamten Reise zu Ihnen verfolgen, von dem Zeitpunkt, an dem er anonym ist, bis zu dem Zeitpunkt, an dem er in Ihrer App angemeldet und bekannt ist. Für jeden Ihrer Nutzer:innen sollten Sie eine ID festlegen, die in Braze `external_id`heißt. Diese sollten sich nicht ändern und zugänglich sein, wenn ein Benutzer die App öffnet. So können Sie Ihre Benutzer über verschiedene Geräte und Plattformen hinweg verfolgen. Lesen Sie den [Artikel Nutzer:innen Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) für bewährte Verfahren.
{% endalert %}

![Braze importiert Backend-Datenquellen aus der API, Frontend-Datenquellen aus dem SDK, Data Warehouse-Daten aus Braze Cloud Data Ingestion und aus Partnerintegrationen. Diese Daten werden über die Braze API ]({% image_buster /assets/img/getting-started/import-export.png %}) exportiert.{: style="display:block;margin:auto;" }

{% alert note %}
Diese personenbezogene Datenbank mit Nutzerprofilen ermöglicht eine interaktive Geschwindigkeit in Realtime. Braze berechnet Werte vor, wenn Daten eintreffen, und speichert die Ergebnisse in einem leichtgewichtigen Dokumentenformat, um schnell abrufbar zu sein. Und weil die Plattform von Anfang an so konzipiert wurde, ist sie ideal für die meisten Messaging-Anwendungsfälle – insbesondere in Kombination mit anderen Datenkonzepten wie Connected-Content, Produktkatalogen und verschachtelten Attributen.
{% endalert %}

### Backend-Datenquellen über die Braze API
Braze kann über unsere [REST API]({{site.baseurl}}/api/endpoints/user_data) Daten aus Nutzer:innen-Datenbanken, Offline-Transaktionen und Data Warehouses abrufen. 

### Frontend-Datenquellen über Braze SDK
Braze erfasst über das [Braze SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/) automatisch First-Party-Daten aus Frontend-Datenquellen, z. B. aus Nutzergeräten. Das SDK behandelt neue (anonyme) Nutzer und verwaltet die Daten ihres Nutzerprofils während ihres gesamten Lebenszyklus. 

### Partnerintegrationen
Braze hat über 150 Technologie-Partner, die wir "Alloys" nennen. Sie können Ihre Daten-Feeds durch ein sinnvolles, robustes Netzwerk [interoperabler Technologien und Daten-APIs]({{site.baseurl}}/partners/home) ergänzen. 

### Direkte Data Warehouse-Anbindung über Braze Cloud Data Ingestion
Sie können Daten von Ihrem Data Warehouse über [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) in wenigen Minuten in die Plattform streamen und so relevante Benutzerattribute, Events und Käufe synchronisieren. Die Integration von Cloud Data Ingestion unterstützt komplexe Datenstrukturen, einschließlich verschachtelter JSON und Arrays von Objekten.

Cloud Data Ingestion kann Daten von Snowflake, Amazon Redshift, Databricks und Google BigQuery synchronisieren.

## Klassifizierung {#classification}
Die Klassifizierungsschicht ermöglicht es Ihrem Team, Zielgruppen, so genannte [Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments), auf der Grundlage von Daten, die Braze durchlaufen, dynamisch zu klassifizieren und aufzubauen. 

{% alert note %}
Die Klassifizierung, Orchestrierung und Personalisierung sind die Ebenen, auf denen Ihr Marketing Team einen Großteil seiner Arbeit erledigen wird. Die Schnittstelle zu diesen Ebenen erfolgt meist über das Braze-Dashboard, unsere Weboberfläche. Entwickler spielen eine Rolle beim Einrichten und Anpassen dieser Ebenen.
{% endalert %}

Viele gängige Arten von Nutzerattributen wie Name, E-Mail, Geburtsdatum, Land und andere werden vom SDK standardmäßig automatisch getrackt. Als Entwickler arbeiten Sie mit Ihrem Team zusammen, um zu definieren, welche zusätzlichen, angepassten Daten für Ihren Anwendungsfall sinnvoll zu tracken sind. Ihre benutzerdefinierten Daten haben Einfluss darauf, wie Ihre Nutzerbasis klassifiziert und segmentiert wird. Sie werden dieses Datenmodell während des Implementierungsprozesses einrichten. 

Erfahren Sie mehr über [automatisch erfasste Daten und benutzerdefinierte Daten]({{site.baseurl}}/developer_guide/analytics/).

## Orchestrierung {#orchestration}
Die Orchestrierung erlaubt es Ihrem Marketing Team, die Nutzer auf der Grundlage ihrer Nutzerdaten und ihres früheren Engagements zu betreuen. Diese Arbeit wird hauptsächlich über unsere Dashboard-Schnittstelle erledigt, aber Sie haben auch die Möglichkeit, [Kampagnen über die API]({{site.baseurl}}/api/api_campaigns#api-campaigns) einzuführen. Sie können Braze beispielsweise über Ihr Backend mitteilen, wann die Nachrichten und Kampagnen, die Ihre Marketer im Dashboard entworfen haben, versendet werden sollen, und sie gemäß Ihrer Backend-Logik triggern. Ein Beispiel für eine durch APIs getriggerte Nachricht könnte das Zurücksetzen von Passwörtern oder Versandbestätigungen sein. 

{% alert note %}
Von APIs getriggerte Kampagnen sind ideal für erweiterte transaktionale Anwendungsfälle. Sie erlauben Marketern die Verwaltung von Kampagnen-Texten, multivariaten Tests und Wiederzulassungsregeln im Braze-Dashboard und triggern gleichzeitig die Zustellung dieser Inhalte von Ihren Servern und Systemen. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Echtzeit in die Nachricht eingefügt werden.
{% endalert %}


### Feature-Flags
Braze ermöglicht Ihnen, Funktionen für eine Auswahl von Nutzer über [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/) aus der Ferne zu aktivieren oder zu deaktivieren. So können Ihre Marketer mit Messaging für Features, die Sie noch nicht für die gesamte Zielgruppe eingeführt haben, das richtige Segment Ihrer Nutzerbasis ansprechen. Darüber hinaus können Feature-Flags dazu verwendet werden, ein Feature in der Produktion ein- und auszuschalten, ohne zusätzliche Code-Bereitstellung oder Updates im App Shop. So können Sie neue Features sicher und zuverlässig einführen.

## Personalisierung {#personalization}
Die Personalisierungsebene bietet Ihnen die Möglichkeit, dynamische Inhalte in Ihren Nachrichten zuzustellen. Durch den Einsatz von Liquid, einer weit verbreiteten Sprache für die Personalisierung, kann Ihr Team dynamisch auf vorhandene Daten zurückgreifen, um die auf jeden Empfänger:in zugeschnittene Nachricht anzuzeigen. Darüber hinaus können Sie mit [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) alle Informationen, auf die Sie auf Ihrem Webserver oder über API zugreifen können, direkt in die Nachrichten einfügen, die Sie versenden, z. B. Push-Benachrichtigungen oder E-Mails. Connected-Content baut auf Liquid auf und verwendet eine vertraute Syntax.

Und da dieser dynamische Content programmierbar ist, können Marketer berechnete Werte, Antworten aus anderen Aufrufen oder Artikel aus dem Produktkatalog einbeziehen. Nachdem Sie diese Systeme während der Implementierung eingerichtet haben, kann Ihr Marketing Team dies mit wenig bis gar keiner Unterstützung durch technische Teams tun. 

## Aktion {#action}
Die Aktionsschicht ermöglicht das eigentliche Messaging für Ihre Nutzer:innen. Der Zweck der Aktionsschicht ist es, die richtige Nachricht zum richtigen Zeitpunkt an den richtigen Nutzer:innen zu senden, und zwar auf der Grundlage der Daten, die über alle zuvor besprochenen Schichten verfügbar sind. Die Nachrichtenübermittlung erfolgt innerhalb Ihrer App oder Website (z. B. durch das Versenden von In-App-Nachrichten oder durch grafische Elemente wie Content Card-Karusselle und Banner) oder außerhalb Ihrer App (z. B. durch das Versenden von Push-Benachrichtigungen oder E-Mails).

### Messaging-Kanäle
Braze wurde entwickelt, um mit seinem kanalagnostischen, nutzerzentrierten Datenmodell eine sich entwickelnde technologische Landschaft zu bewältigen. Das Dashboard verwaltet die Zustellung von Nachrichten und die Auslöser für Transaktionen. So können Ihre Marketer beispielsweise eine SMS Nachricht triggern, die einen Gutschein für einen Ihrer neu eröffneten Standorte anbietet, wenn ein Nutzer:innen den Geofence in der Nähe dieses Standorts betritt, oder einem Nutzer:innen eine E-Mail schicken, um ihn über die neue Staffel seiner Lieblingssendung zu informieren.

Das [Braze SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/) ermöglicht zusätzliche Messaging-Kanäle: Push, In-App-Nachrichten und Content-Cards. Sie integrieren das SDK in Ihre App oder Website, damit Ihr Marketing-Team das Braze-Dashboard nutzen kann, um seine Kampagnen über alle unterstützten Messaging-Kanäle zu koordinieren.

![]({% image_buster /assets/img/getting_started/channels.png %})

## Daten exportieren
Alle Interaktionen der Endnutzer mit Braze werden getrackt, sodass Sie Ihre Interaktionen und Reichweite messen können. Und nachdem Braze Ihre Daten aus all diesen Quellen zusammengetragen hat, können Sie sie mit einer Vielzahl von Tools zurück in Ihren Tech Stack exportieren und so den Kreislauf schließen.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) ist ein optionales Add-on für Braze, das einen granularen Streaming-Export ermöglicht, der kontinuierlich andere Ziele Ihres Stacks speist. Currents ist ein Rohdaten-Feed pro Nutzer und Event, der alle fünf Minuten oder alle 15.000 Ereignisse Daten exportiert, je nachdem, was zuerst eintritt. Beispiele für einige nachgelagerte Ziele für Currents sind u. a. Segment, S3, Redshift und Mixpanel. 

### Snowflake Daten gemeinsam nutzen
Die Snowflake-Funktionalität für [die sichere gemeinsame Nutzung von Daten]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) erlaubt es Braze, Ihnen einen sicheren Zugriff auf die Daten in unserem Snowflake-Portal zu gewähren, ohne dass Sie sich über Reibungsverluste im Arbeitsablauf, Fehlerpunkte und unnötige Kosten sorgen müssen, die mit den typischen Beziehungen zu Datenanbietern verbunden sind. Die gemeinsame Nutzung erfolgt über die eindeutige Ebene der Dienste und den Shop von Snowflake: Es werden keine Daten zwischen Konten kopiert oder übertragen. Das ist ein wichtiges Konzept, da gemeinsam genutzte Daten keinen Speicherplatz in einem Verbraucherkonto beanspruchen und daher nicht zu Ihren monatlichen Gebühren für den Datenspeicher beitragen. Den Verbrauchern werden nur die Computer-Ressourcen (d. h. virtuelle Warehouses) berechnet, die zur Abfrage der gemeinsam genutzten Daten verwendet werden.

### Braze Export APIs
Die Braze API stellt [Endpunkte]({{site.baseurl}}/api/endpoints/export) zur Verfügung, die es Ihnen erlauben, sowohl aggregierte Analytics als auch einzelne Nutzerdaten programmatisch zu exportieren. Diese Daten können für Zielgruppen und Segmente beliebiger Größe exportiert werden. 

### CSVs
Schließlich haben Sie die Möglichkeit, Ihre Daten auf aggregierter Ebene direkt vom Dashboard als [CSV-Datei]({{site.baseurl}}/user_guide/data/export_braze_data/) herunterzuladen. Die CSV-Option erlaubt es Ihren Team-Mitgliedern, Daten aus Braze zu exportieren.

{% alert tip %}
Während der CSV-Export ein Basislimit von 500.000 Zeilen hat, gibt es für die APIs diesbezüglich kein Limit.
{% endalert %}

## Praxisbeispiel 
Einer Ihrer Nutzer:innen, nennen wir ihn Mel, hat gerade Ihre Produktankündigung erhalten. Hinter den Kulissen haben alle Ebenen der Braze-Plattform zusammengearbeitet, um sicherzustellen, dass dieser Prozess reibungslos abläuft. 

Die Informationen von Mel wurden über einen CSV-Import von Ihrer Legacy-Plattform für Customer-Engagement in Braze übernommen. Jedes Mal, wenn Mel nach der Integration mit Ihrer App interagierte, wurden weitere Daten zu ihrem Kundenprofil hinzugefügt. 

Ihre Produktankündigung wurde an alle Kunden gesendet, denen ein ähnlicher Artikel in Ihrer App gefallen hat. Sie haben diese Daten als angepasstes Event definiert. Das SDK hat dieses Ereignis getrackt und Ihre Nutzer entsprechend segmentiert. Braze orchestrierte die beste Tageszeit, um diese Ankündigung zu versenden, und personalisierte die Ankündigung, indem er Mel mit ihrem Wunschnamen ansprach. 

Wenn Mel die Ankündigung öffnet, fügt sie Ihr neues Produkt zu ihrer Wunschliste hinzu. Braze trackt, dass sie die E-Mail automatisch angeklickt hat. Das SDK verfolgt, dass sie Ihr neues Produkt auf die Wunschliste gesetzt hat. Jedes Mal, wenn sie mit Ihrer Marke interagieren, erfahren Sie und Ihre Nutzer mehr übereinander.

![]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})



