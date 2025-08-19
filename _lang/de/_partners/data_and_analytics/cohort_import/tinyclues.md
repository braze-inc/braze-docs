---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Tinyclues, die ein Feature zum Aufbau von Zielgruppen anbietet, mit dem Sie über eine unglaublich benutzerfreundliche UI mehr Targeting-Kampagnen versenden, neue Produkte Opportunities finden und Ihren Umsatz steigern können."
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) ist ein Feature zum Aufbau von Zielgruppen, das die Möglichkeit bietet, die Anzahl der Kampagnen und den Umsatz zu erhöhen, ohne das Kundenerlebnis zu beeinträchtigen, sowie Analytics, um die Performance von CRM-Kampagnen sowohl online als auch offline zu verfolgen.

Die Integration von Braze und Tinyclues bietet Nutzern:innen einen Weg zu einer besseren CRM-Planung und -Strategie, die es ihnen erlaubt, mit Hilfe einer unglaublich benutzerfreundlichen UI gezieltere Kampagnen zu versenden, neue Produkte Opportunities zu finden und den Umsatz zu steigern.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Tinyclues Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Tinyclues Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Datenimporten

Um Braze und Tinyclues zu integrieren, müssen Sie die Tinyclues-Plattform konfigurieren, eine bestehende Tinyclues-Kampagne exportieren und ein Kohorten-Segment in Braze erstellen, das für das Targeting von Nutzer:innen in zukünftigen Kampagnen verwendet werden kann.

### Schritt 1: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Tinyclues** aus. 

Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.<br><br>![]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"} 

Um die Integration abzuschließen, müssen Sie Ihrem Tinyclues Data Operations Team den Datenimport-Schlüssel und den REST-Endpunkt zur Verfügung stellen. Tinyclues stellt dann die Verbindung her und meldet sich bei Ihnen, sobald die Einrichtung abgeschlossen ist.

### Schritt 2: Exportieren Sie eine Kampagne von der Tinyclues Plattform

Jedes Mal, wenn Sie eine Kohorte von Tinyclues Nutzer:innen zur Verwendung in Braze erstellen möchten, müssen Sie diese zunächst aus der Tinyclues Plattform exportieren.

Wählen Sie in Tinyclues die Kampagne(n) aus, die Sie exportieren möchten, und klicken Sie auf **Kampagnen exportieren**. Beim Export wird die Zielgruppe automatisch auf Ihr Braze-Konto hochgeladen.

![]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Schritt 3: Erstellen Sie ein Segment aus der angepassten Zielgruppe von Tinyclues

Navigieren Sie in Braze zu **Segmente**, benennen Sie Ihr Tinyclues Kohorten-Segment und wählen Sie **Tinyclues Kohorten** als Filter. Von hier aus können Sie wählen, welche Tinyclues Kohorte Sie einbeziehen möchten. Nachdem Ihr Tinyclues Kohorten-Segment erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

![]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![In der Segmentierung von Braze ist der Filter für die Nutzer:innen-Attribute "Tinyclues Kohorte" auf "umfasst" und "Primärkohorte" eingestellt.]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Haben Sie Schwierigkeiten, Ihre Kohorte zu finden? In unserer Rubrik [Fehlerbehebung](#troubleshooting) finden Sie eine Anleitung. 

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

## Verwendung dieser Integration

Um Ihr Tinyclues Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas und wählen Sie das Segment als Ihre Zielgruppe aus. 

![Im Braze Kampagnen-Builder ist im Schritt Targeting der Filter "Nutzer:innen nach Segmenten zusammenstellen" auf "Tinyclues Kohorte" eingestellt.]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

## Fehlersuche

Haben Sie Probleme, die richtige Kohorte in der Liste zu finden? Sehen Sie sich in Tinyclues die Details Ihrer Kampagne an und überprüfen Sie den Namen, indem Sie die Option **Dateiname exportieren** aktivieren.

![Unten auf der Detailseite der Kampagne wird der Name Ihrer Kohorte angezeigt.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Haben Sie immer noch Probleme, Ihre Zielgruppe zu finden? Kontaktieren Sie das [Tinyclues Team](mailto:support@tinyclues.com) für weitere Unterstützung.

