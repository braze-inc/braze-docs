---
nav_title: Heap - Kohortenimport
article_title: Heap - Kohortenimport
description: "Dieser referenzierte Artikel beschreibt die Integration zwischen Braze und Heap, einer Plattform für digitale Insights, die es Ihnen erlaubt, Heap-Daten in Braze zu importieren, Nutzer:innen-Kohorten zu erstellen sowie Braze-Daten in Heap zu exportieren, um Segmente zu erstellen."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Heap - Kohortenimport

> [Heap](https://heap.io/), eine Plattform für digitale Insights, konzentriert sich auf die Opportunitäten in Ihrem digitalen Erlebnis, die sich am stärksten auf Ihr Geschäft auswirken, indem sie Reibungsverluste beseitigen, Ihre Kunden begeistern und Ihren Umsatz beschleunigen.

Die Integration von Braze und Heap ermöglicht Ihnen den [Import von Heap-Daten in Braze](#data-import-integration), die Erstellung von Nutzer:innen-Kohorten sowie den [Export von Nutzer:innen-Daten in Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/), um Segmente zu erstellen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Heap-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Heap-Konto](https://heap.io/about). |
| Braze Datenimport-Schlüssel | Dies kann im Braze-Dashboard unter **Partnerintegrationen** > **Technologiepartner** erfasst werden, und wählen Sie dann **Heap** aus. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze-Currents | Um Daten von Braze nach Heap zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) in Ihrem Konto aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle
- Erneute Interaktion mit Nutzer:innen, die einen Funnel verlassen haben: Triggern Sie eine erneute Interaktion mit Nachrichten, wenn Nutzer:innen den Kauf- oder Abo-Funnel abbrechen.
- Personalisieren Sie das Testerlebnis: Identifizieren Sie Reibungspunkte in Ihrer Testphase und senden Sie zeitlich korrekt getimte Erinnerungen, um Nutzer:innen während einer Testphase erneut zu interagieren und ihnen zu helfen, einen Mehrwert zu erzielen.
- Erhöhen Sie das Engagement für Ankündigungen und Angebote: Targeting von Aktionen, Updates und Ankündigungen neuer Dienste für die relevanten Zielgruppen.

## Integration von Datenimporten

Verwenden Sie die Heap to Braze Integration, um Kohorten, die in Heap definiert sind, automatisch mit Braze zu synchronisieren.

### Schritt 1: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie dann **Heap** aus. 

Auf dieser Seite finden Sie Ihren Datenimport-Schlüssel und einen REST-Endpunkt. Notieren Sie sich diese beiden Werte und geben Sie sie Ihrem Heap Account Manager:in, um die Integration fertigzustellen.

![]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Schritt 2: Segmentierung importierter Nutzer:in in Braze

Navigieren Sie in Braze zu **Segmente**, benennen Sie Ihr Heap-Kohorten-Segment und wählen Sie **Heap-Kohorten** als Filter. Von hier aus können Sie wählen, welche Heap-Kohorte Sie einbeziehen möchten. Nachdem Sie Ihr Kohorten-Segment erstellt haben, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

![In der Segmentierung von Braze ist der Filter für die Nutzer:innen Attribute "Heap Kohorte" auf "includes" und "Heap Test Kohorte" gesetzt.]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Verwendung dieser Integration

Um Ihr Heap-Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas und wählen das Segment als Ihre Zielgruppe aus.

![Im Braze-Kampagnen-Builder ist im Schritt Targeting der Filter "Nutzer:innen nach Segmenten zusammenstellen" auf "Kohorte horten" eingestellt.]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

## Details zur Integration

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

