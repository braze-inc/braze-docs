---
nav_title: SmarterSends
article_title: SmarterSends
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SmarterSends, einer benutzerfreundlichen Schnittstelle, die es auch Nicht-Vermarktern ermöglicht, markenkonforme E-Mail-Kampagnen zu erstellen, zu planen und zu versenden."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends][2] fördert die Personalisierung mit Marketingkampagnen, die Unternehmen erstellen, planen und einsetzen können, um die Einhaltung von Marken- und Gesetzesvorschriften zu gewährleisten und dabei die Kontrolle über die verwendeten Inhalte und Daten zu behalten. 

Die Partnerschaft zwischen Braze und SmarterSends ermöglicht es Ihnen, die Leistungsfähigkeit von Braze mit den hyperlokalisierten Inhalten Ihrer verteilten Nutzer zu kombinieren, um Ihre Marketingkampagnen zu verbessern.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| SmarterSends-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SmarterSends-Konto][2]. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit diesen Berechtigungen: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. Für zusätzliche Sicherheit lassen Sie die IP-Adresse von SmarterSends zu (verfügbar in Ihrer Instanz). |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze API-Kampagnen-ID | Die [Braze API-Kampagnen-ID]({{site.baseurl}}/api/api_campaigns/) ist die eindeutige Kennung für alle über SmarterSends versendeten Kampagnen. Diese können Sie im Braze Dashboard unter **Messaging** > **Kampagnen** erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

## Anwendungsfälle

Mit der Integration von Braze und SmarterSends können Sie die Vorteile des verteilten Marketings nutzen, indem Sie Marketingkampagnen über mehrere Kanäle und Standorte hinweg erstellen und ausführen. Diese Vorteile umfassen:

1. **Erhöhte Reichweite:** Nutzen Sie mehrere Kanäle und Standorte, um ein breiteres Publikum zu erreichen und Kunden an verschiedenen Orten anzusprechen, was zu einer erhöhten Markenpräsenz führt.
2. **Gezielte Botschaften:** Maßgeschneiderte Botschaften über verschiedene Kanäle und an verschiedenen Standorten, um die lokalen Zielgruppen anzusprechen und die Kommunikation mit den Kunden effektiver zu gestalten. 
3. **Verbesserte Markenkonsistenz:** Abstimmung Ihrer Markenbotschaft und Ihres Markenimages über alle Kanäle und Standorte hinweg, was für den Aufbau einer starken und wiedererkennbaren Marke wichtig ist.
4. **Bessere Einblicke:** Das Sammeln von Daten aus verschiedenen Kanälen und Standorten liefert wertvolle Einblicke in das Kundenverhalten und die Vorlieben, die zur Verfeinerung von Marketingstrategien und -taktiken sowohl auf lokaler als auch auf globaler Ebene genutzt werden können.
5. **Gesteigerte Effizienz:** Nutzung der Stärken verschiedener Kanäle und Standorte, was zu einer effizienteren Nutzung von Ressourcen führen kann, während gleichzeitig die gewünschten Marketingziele erreicht werden. 

## Integration

### Schritt 1: Erstellen Sie einen REST-API-Schlüssel

1. Gehen Sie in Braze zu **Einstellungen** > **API-Schlüssel** und klicken Sie auf **Neuen API-Schlüssel erstellen**.
2. Geben Sie einen Namen für den API-Schlüssel ein.
3. Wählen Sie die folgenden Berechtigungen für diesen Schlüssel, damit SmarterSends mit Ihrem Braze-Arbeitsbereich interagieren kann.
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
6. Kopieren Sie den API-Schlüssel mit den entsprechenden Berechtigungen und fügen Sie ihn in die Einstellungen des **Braze Email Service Providers** in SmarterSends ein.

### Schritt 2: Erstellen oder Kopieren einer Anwendungs-ID

1. Gehen Sie in Ihrem Braze-Arbeitsbereich zu **Einstellungen** > **App-Einstellungen**. 
2. Richten Sie eine neue Anwendung ein oder verwenden Sie die Anwendungs-ID einer bestehenden Anwendung in Ihrem Arbeitsbereich. Beachten Sie, dass die Anwendungs-ID als **API-Schlüssel** beschriftet ist. 
3. Kopieren Sie diese ID und fügen Sie sie in das Feld **App ID** in SmarterSends ein.

### Schritt 3: Erstellen Sie eine API-Kampagne

Eine API-Kampagne ermöglicht die Verfolgung von Metriken für alle SmarterSends-Mails innerhalb von Braze und ermöglicht es SmarterSends, diese API-basierten Kampagnen auszulösen.

1. [Erstellen Sie]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign) in Braze [eine API-Kampagne]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Klicken Sie auf **E-Mail** unter **Nachrichtenkanal auswählen**, um einen Nachrichtenkanal hinzuzufügen und mit der Verfolgung von Metriken zu beginnen.
3. Als nächstes kopieren Sie die Kampagnen-ID aus Braze und fügen sie in das Feld **Kampagnen-ID** in SmarterSends ein. 
4. Kopieren Sie die Nachrichten-Varianten-ID aus Braze und fügen Sie sie in das Feld **Nachrichten-Varianten-ID** in SmarterSends ein. Dies ist die Standard-Nachrichten-ID, die verwendet wird, wenn Sie sich dafür entscheiden, nicht für jede Gruppe in SmarterSends eine Nachrichten-ID zu erstellen.
5. Für jede Gruppe, die Sie in SmarterSends erstellen, fügen Sie eine Nachrichtenvariante zu Ihrer API-Kampagne in Braze hinzu. Kopieren Sie dann die ID der Nachrichtenvariante in die ID der Nachrichtenvariante der Gruppe in SmarterSends.

{% alert tip %}
Legen Sie für jede Gruppe, die Sie in SmarterSends erstellen, eine Nachrichtenvarianten-ID an, um die Metriken für die Sendungen jeder Gruppe separat in Ihrem Braze-Arbeitsbereich anzuzeigen. Dies kann hilfreich sein, um beim Erstellen von Berichten in Braze gruppenübergreifende Trends zu erkennen.
{% endalert %}

## Anpassung

Jede SmarterSends-Instanz lässt sich vollständig an die Farben Ihres Markenlogos und Ihren eigenen Domainnamen anpassen, so dass eine vertraute Umgebung entsteht. Zur weiteren Personalisierung können Sie außerdem die Attribute und benutzerdefinierten Attribute definieren, um Benutzer in Kampagnen auf der Grundlage der Segmente in Ihrem Braze-Arbeitsbereich anzusprechen.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://smartersends.com