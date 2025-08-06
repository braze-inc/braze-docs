---
nav_title: Kubit
article_title: Kubit Kohorten Import
description: "Dieser referenzierte Artikel beschreibt die Kohortenimport-Funktionalität von Kubit, einer no-code, self-service Analytics-Plattform, die sofortige Insights zu Produkten liefert. Er erlaubt es Ihnen, Kubit-Benutzerkohorten zu importieren und sie im Messaging von Braze gezielt anzusprechen."
page_type: partner
search_tag: Partner
---

# Kubit Kohortenimport

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten aus [Kubit](https://kubit.ai/) nach Braze importieren. Weitere Informationen zur Integration von Kubit und seinen anderen Funktionalitäten finden Sie im [Hauptartikel zu Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit/).

## Integration von Datenimporten

### Schritt 1: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Kubit** aus. Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. 

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Kubit einrichten.

![Die Technologie-Partnerseite von Kubit in Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Schritt 2: Konfigurieren Sie Braze in Kubit

Geben Sie den Datenimport-Schlüssel und den Braze REST-Endpunkt an Ihren Kubit-Supportkontakt weiter. Er wird die Integration auf seiner Seite konfigurieren und Sie informieren, sobald die Integration aktiv ist.  

### Schritt 3: Kohorten nach Braze importieren

#### Erstellen Sie eine Kohorte in Kubit
[Erstellen Sie eine Kohorte](https://www.kubit.ai/doc/fundamentals#cohort) in Kubit und definieren Sie die Kriterien Ihrer Zielgruppe Nutzer:innen.<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Nutzer:innen nach Braze importieren
Sobald Sie Ihre Kohorte gespeichert haben, können Sie sie in Braze importieren, um sie in Segmenten von Braze zu verwenden. Diese Segmente können dann zur Erstellung gezielter E-Mail- oder Push-Kampagnen und Canvase verwendet werden.

Navigieren Sie dazu zu Ihrer bestehenden Kohorte und wählen Sie unter **Kohortensteuerung** **Importieren nach Braze**.

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Wählen Sie dann die gewünschte Importkadenz aus. Einmalige Importe erlauben es Ihnen jetzt, einmal zu importieren. Mit den Zeitplänen können Sie täglich, wöchentlich oder monatlich zu einer bestimmten Zeit importieren. Beachten Sie, dass jede Kohorte nur einen Zeitplan für den Live-Import haben kann. 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

#### Importstatus überprüfen
Sobald ein Import abgeschlossen ist, wird eine E-Mail-Benachrichtigung an die im Zeitplan für den Import angegebenen Empfänger:in gesendet. Sie können den Importstatus einer Kohorte auch unter **Zeitplan** in Kubit überprüfen. Im Verlauf des Zeitplans werden die Ausführungszeit des Imports, das Ergebnis und die Gesamtzahl der Nutzer:innen in der Kohorte, die in Braze importiert wurden, angezeigt.<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Sie können einen Import manuell triggern, indem Sie auf das Symbol **In Braze importieren** für diesen Zeitplan klicken.

### Schritt 4: Erstellen Sie Braze Segmente mit Kubit Kohorten
Nachdem Sie Kohorten in Braze importiert haben, können Sie diese als Filter verwenden, um Braze-Segmente zu erstellen und sie in Braze-Kampagnen oder Canvas einzubinden. Besuchen Sie unsere Dokumentation zu Segmenten, um mehr darüber zu erfahren, [wie Sie Segmente in Braze erstellen können]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![In der Segmentierung von Braze wird das Nutzer:in-Attribut "Kubit Kohorten" auf "includes_value" gesetzt und zeigt eine Liste der verfügbaren Kohorten an.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.