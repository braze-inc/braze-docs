---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Splio, die es Ihnen ermöglicht, gezieltere Kampagnen zu versenden, neue Produkte zu finden und den Umsatz zu steigern."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/) ist ein Tool zum Aufbau von Zielgruppen, mit dem Sie die Anzahl der Kampagnen und den Umsatz steigern können, ohne das Kundenerlebnis zu beeinträchtigen, und das Analytics zur Verfügung stellt, um die Performance von CRM-Kampagnen sowohl online als auch offline zu verfolgen.

Mit der Integration von Braze und Splio können Sie bessere CRM-Strategien planen und durchführen, gezieltere Kampagnen versenden, neue Produkt Opportunitäten finden und Ihren Umsatz steigern.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Splio-Konto | Für diese Partnerschaft benötigen Sie ein Splio-Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Datenimporten

Um Braze und Splio zu integrieren, müssen Sie die Splio-Plattform konfigurieren, eine bestehende Splio-Kampagne exportieren und ein Kohorten-Segment in Braze erstellen, um Nutzer:innen in zukünftigen Kampagnen zu targetieren.

### Schritt 1: Holen Sie sich den Datenimport-Schlüssel für Braze

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Splio**.

Suchen Sie Ihren REST-Endpunkt und generieren Sie Ihren Datenimport-Schlüssel für Braze. Nachdem Sie den Schlüssel generiert haben, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.<br><br>![Die Technologie-Partnerseite von Splio mit dem REST-Endpunkt und dem Datenimport-Schlüssel.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

Um die Integration abzuschließen, geben Sie den Datenimport-Schlüssel und den REST-Endpunkt an Ihr Splio Data Operations Team weiter. Splio stellt die Verbindung her und kontaktiert Sie, nachdem die Einrichtung abgeschlossen ist.

### Schritt 2: Exportieren Sie eine Kampagne aus der Splio-Plattform

Jedes Mal, wenn Sie in Braze eine Kohorte von Nutzer:innen aus Splio erstellen möchten, müssen Sie diese zunächst aus der Splio-Plattform exportieren.

Wählen Sie in Splio die Kampagnen aus, die Sie exportieren möchten, und klicken Sie auf **Kampagnen exportieren**. Nachdem Sie exportiert haben, wird die Zielgruppe automatisch auf Ihr Braze-Konto hochgeladen.

![Exportieren von Kampagnen aus der Splio-Plattform.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Schritt 3: Erstellen Sie ein Segment aus der angepassten Zielgruppe von Splio

Navigieren Sie in Braze zu **Segmente**, benennen Sie Ihr Splio-Kohorten-Segment und wählen Sie **Splio-Kohorten** als Filter. Wählen Sie von hier aus, welche Kohorte von Splio Sie einbeziehen möchten. Nachdem Sie Ihr Splio Kohorten-Segment erstellt haben, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

![Erstellen eines Segmentes der Kohorte Splio in Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![In der Segmentierung von Braze ist der Filter für die Nutzer:innen Attribute "Splio Kohorte" auf "includes" und "Primary Kohorte" eingestellt.]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Haben Sie Schwierigkeiten, Ihre Kohorte zu finden? Schauen Sie in der Rubrik [Fehlerbehebung](#troubleshooting) nach.

{% alert important %}
Es werden nur Nutzer:innen aus einer Kohorte hinzugefügt oder entfernt, die bereits in Braze existieren. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

## Verwendung dieser Integration

Um Ihr Splio-Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas und wählen das Segment als Ihre Zielgruppe aus.

![Im Braze-Kampagnen-Builder ist im Schritt Targeting der Filter "Nutzer:innen nach Segmenten zusammenstellen" auf "Kohorte Splio" eingestellt.]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Nutzer:in

Braze vergleicht Nutzer:innen anhand ihrer `external_id` oder `alias`. Anonyme Nutzer:innen werden anhand ihrer `device_id` gefunden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` abgeglichen werden, sondern müssen über ihre `external_id` oder `alias` abgeglichen werden.

## Fehlersuche

Wenn Sie die richtige Kohorte in der Liste nicht finden können, sehen Sie sich die Details Ihrer Kampagne in Splio an und überprüfen Sie den Namen, indem Sie den **Dateinamen exportieren**.

![Unten auf der Detailseite der Kampagne wird der Name Ihrer Kohorte angezeigt.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Wenn Sie Probleme haben, Ihre Zielgruppe abzurufen, wenden Sie sich an das [Team von Splio](mailto:support-team@splio.com), um Unterstützung zu erhalten.