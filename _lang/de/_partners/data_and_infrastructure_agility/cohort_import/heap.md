---
nav_title: Heap
article_title: Heap
description: "Dieser Referenzartikel beschreibt die Integration zwischen Braze und Heap, einer Plattform für digitale Einblicke, die es Ihnen ermöglicht, Heap-Daten in Braze zu importieren, Benutzerkohorten zu erstellen und Braze-Daten in Heap zu exportieren, um Segmente zu erstellen."
alias: /partners/heap/
page_type: partner
search_tag: Partner

---

# Heap

> [Heap](https://heap.io/), eine Plattform für digitale Einblicke, fokussiert Sie auf die Möglichkeiten, die Ihr digitales Erlebnis am meisten beeinflussen, um Reibungsverluste zu beseitigen, Ihre Kunden zu begeistern und Ihren Umsatz zu steigern.

Mit der Integration von Braze und Heap können Sie [Heap-Daten in Braze importieren](#data-import-integration), Benutzerkohorten erstellen und [Braze-Daten in Heap exportieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/heap/), um Segmente zu erstellen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Heap-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Heap-Konto](https://heap.io/about). |
| Schlüssel Braze Data Import | Dies kann im Braze-Dashboard unter **Partner-Integrationen** > **Technologiepartner** und dann unter **Heap** erfasst werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Lötende Ströme | Um Daten von Braze nach Heap zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) in Ihrem Konto aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle
- Binden Sie Nutzer, die einen Trichter verlassen haben, wieder ein: Lösen Sie Re-Engagement-Nachrichten aus, wenn Benutzer den Kauf- oder Abonnementtrichter verlassen.
- Personalisieren Sie das Erlebnis der Studie: Identifizieren Sie Reibungspunkte in der Testphase und senden Sie rechtzeitig Erinnerungen, um die Nutzer während der Testphase wieder einzubinden und ihnen zu helfen, den Wert zu erkennen.
- Erhöhen Sie das Engagement für Ankündigungen und Angebote: Richten Sie Werbeaktionen, Aktualisierungen und Ankündigungen neuer Dienste an die entsprechenden Zielgruppen.

## Integration von Datenimporten

Verwenden Sie die Heap to Braze-Integration, um die in Heap definierten Kohorten automatisch mit Braze zu synchronisieren.

### Schritt 1: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie dann **Heap**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Auf dieser Seite finden Sie Ihren Datenimportschlüssel und einen REST-Endpunkt. Notieren Sie sich diese beiden Werte und teilen Sie sie Ihrem Heap-Kundenbetreuer mit, um die Einrichtung der Integration abzuschließen.

![][3]{: style="max-width:90%;"}

### Schritt 2: Segmentieren Sie importierte Benutzer in Braze

Navigieren Sie in Braze zu **Segmente**, benennen Sie Ihr Heap-Kohortensegment und wählen Sie **Heap-Kohorten** als Filter. Von hier aus können Sie wählen, welche Heap-Kohorte Sie einbeziehen möchten. Nachdem Sie Ihr Heap-Kohortensegment erstellt haben, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.

![Im Braze Segment Builder ist der Benutzerattributfilter "Heap-Kohorte" auf "enthält" und "Heap-Test-Kohorte" eingestellt.][2]{: style="max-width:90%;"}

### Mit dieser Integration

Um Ihr Heap-Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Canvas und wählen das Segment als Ihre Zielgruppe aus.

![Im Braze-Kampagnen-Builder ist im Schritt "Targeting" der Filter "Zielbenutzer nach Segment" auf "Heap cohort" eingestellt.][4]{: style="max-width:90%;"}

## Details zur Integration

Die Payload-Struktur für exportierte Daten ist die gleiche wie die Payload-Struktur für benutzerdefinierte HTTP-Konnektoren, die Sie im [Repository für Beispiele für benutzerdefinierte HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %}
[3]: {% image_buster /assets/img/heap/heap2.png %}
[4]: {% image_buster /assets/img/heap/heap3.png %} 
