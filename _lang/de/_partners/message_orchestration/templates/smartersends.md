---
nav_title: SmarterSends
article_title: SmarterSends
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und SmarterSends, einer einfach zu bedienenden Schnittstelle, die für Nicht-Marketer entwickelt wurde, um markenkonforme E-Mail Kampagnen zu erstellen, zu planen und zu versenden."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com) treibt die Personalisierung mit Marketing Kampagnen voran, die Unternehmen erstellen, zeitlich planen und einsetzen können, um die Einhaltung von Marken- und Gesetzesvorschriften durchzusetzen und dabei die Kontrolle über die verwendeten Inhalte und Daten zu behalten. 

_Diese Integration wird von SmarterSends gepflegt._

## Über die Integration

Die Partnerschaft zwischen Braze und SmarterSends erlaubt es Ihnen, die leistungsstarke Leistung von Braze mit den hyperlokalisierten Inhalten Ihrer Nutzer:innen zu kombinieren, um Ihre Kampagnen zu optimieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| SmarterSends-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SmarterSends-Konto](https://smartersends.com). |
| Braze REST API-Schlüssel | Ein REST-API-Schlüssel von Braze mit diesen Berechtigungen: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. Für zusätzliche Sicherheit lassen Sie die IP-Adresse von SmarterSends zu (verfügbar in Ihrer Instanz). |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze API Kampagnen ID | Die [API-Kampagnen-ID von Braze]({{site.baseurl}}/api/api_campaigns/) ist der eindeutige Bezeichner für alle Kampagnen, die über SmarterSends gesendet werden. Diese kann im Braze-Dashboard unter **Messaging** > **Kampagnen** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Integration von Braze und SmarterSends können Sie die Vorteile des verteilten Marketings nutzen, indem Sie Kampagnen über mehrere Kanäle und Standorte hinweg erstellen und durchführen. Diese Vorteile umfassen:

1. **Erhöhte Reichweite:** Nutzen Sie mehrere Kanäle und Standorte, um eine breitere Zielgruppe zu erreichen und Zielgruppen an verschiedenen Standorten anzusprechen, was zu einer erhöhten Markenpräsenz führt.
2. **Gezieltes Messaging:** Maßgeschneidertes Messaging über verschiedene Kanäle und Standorte hinweg, um die lokale Zielgruppe anzusprechen und die Kommunikation und das Engagement mit den Kunden effektiver zu gestalten. 
3. **Verbesserte Markenkonsistenz:** Das Messaging und Image Ihrer Marke über alle Kanäle und Standorte hinweg abzustimmen, ist wichtig für den Aufbau einer starken und wiedererkennbaren Marke.
4. **Bessere Insights:** Das Sammeln von Daten aus verschiedenen Kanälen und Standorten liefert wertvolle Insights über das Kundenverhalten und die Präferenzen der Kunden, die zur Verfeinerung von Marketing-Strategien und -Taktiken sowohl auf lokaler als auch auf globaler Ebene genutzt werden können.
5. **Gesteigerte Effizienz:** Die Stärken verschiedener Kanäle und Standorte nutzen, was zu einer effizienteren Nutzung von Ressourcen führen kann, während gleichzeitig die gewünschten Marketingziele erreicht werden. 

## Integration

### Schritt 1: Einen REST API-Schlüssel erstellen

1. Gehen Sie in Braze zu **Einstellungen** > **API-Schlüssel** und klicken Sie auf **Neuen API-Schlüssel erstellen**.
2. Geben Sie einen Namen für den API-Schlüssel ein.
3. Wählen Sie die folgenden Berechtigungen für diesen Schlüssel aus, damit SmarterSends mit Ihrem Braze Workspace interagieren kann.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Fügen Sie die SmarterSends IP-Adresse zum Abschnitt **Whislist IPs** hinzu.
5. Klicken Sie auf **API-Schlüssel speichern**.
6. Kopieren Sie den API-Schlüssel mit den entsprechenden Berechtigungen und fügen Sie ihn in die Einstellungen des **Braze E-Mail Service Providers** in SmarterSends ein.

### Schritt 2: Erstellen oder Kopieren einer Anwendungs-ID

1. Gehen Sie in Ihrem Braze Workspace zu **Einstellungen** > **App-Einstellungen**. 
2. Richten Sie eine neue App ein oder verwenden Sie die ID einer bestehenden App in Ihrem Workspace. Beachten Sie, dass die ID der Anwendung als **API-Schlüssel** gekennzeichnet ist. 
3. Kopieren Sie diese ID und fügen Sie sie in das Feld **App ID** in SmarterSends ein.

### Schritt 3: Erstellen Sie eine API-Kampagne

Eine API-Kampagne ermöglicht das Tracking von Metriken für alle SmarterSends-Mails innerhalb von Braze und erlaubt es SmarterSends, diese API-basierten Kampagnen zu triggern.

1. Erstellen Sie in Braze eine [API-Kampagne]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Klicken Sie auf **E-Mail** unter **Nachrichten-Kanal auswählen**, um einen Messaging-Kanal hinzuzufügen und mit dem Tracking von Metriken zu beginnen.
3. Kopieren Sie dann die ID der Kampagne aus Braze und fügen Sie sie in das Feld **Kampagnen ID** in SmarterSends ein. 
4. Kopieren Sie die ID der Nachrichtenvariante aus Braze und fügen Sie sie in das Feld **ID der Nachrichtenvariante** in SmarterSends ein. Dies ist die Standard ID für Nachrichten, die Sie verwenden, wenn Sie nicht für jede Gruppe in SmarterSends eine ID für Nachrichten erstellen möchten.
5. Fügen Sie für jede Gruppe, die Sie in SmarterSends erstellen, eine Variante der Nachricht zu Ihrer API-Kampagne in Braze hinzu. Kopieren Sie dann die ID der Variante der Nachricht in die ID der Variante der Nachricht der Gruppe in SmarterSends.

{% alert tip %}
Legen Sie für jede Gruppe, die Sie in SmarterSends erstellen, eine ID für eine Variante der Nachricht an, um die Metriken für die Sendungen jeder Gruppe separat in Ihrem Braze Workspace anzuzeigen. Dies kann hilfreich sein, um beim Erstellen von Berichten in Braze gruppenübergreifende Trends zu erkennen.
{% endalert %}

## Anpassung

Jede Instanz von SmarterSends lässt sich vollständig an die Farben Ihres Markenlogos und Ihren angepassten Domain-Namen anpassen, wodurch eine vertraute Umgebung geschaffen wird. Darüber hinaus können Sie zur weiteren Personalisierung die Attribute und angepassten Attribute definieren, um Nutzer:innen in Kampagnen auf der Grundlage der Segmente innerhalb Ihres Braze Arbeitsbereichs anzusprechen.


