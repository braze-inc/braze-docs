---
nav_title: Kubit
article_title: Kubit Cohort Import
description: "Dieser Referenzartikel beschreibt die Kohorten-Importfunktionalität von Kubit, einer codefreien Self-Service-Analyseplattform, die sofortige Produkteinblicke liefert. Sie können Kubit-Benutzerkohorten importieren und sie im Braze-Messaging ansprechen."
page_type: partner
search_tag: Partner
---

# Kubit-Kohorte importieren

> Dieser Artikel beschreibt, wie Sie Benutzerkohorten von [Kubit](https://kubit.ai/) nach Braze importieren. Weitere Informationen zur Integration von Kubit und seinen anderen Funktionalitäten finden Sie im [Hauptartikel zu Kubit]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/).

## Integration von Datenimporten

### Schritt 1: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Kubit**. Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Kubit einrichten.

![Die Kubit-Technologiepartnerseite in Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Schritt 2: Konfigurieren Sie Braze in Kubit

Geben Sie den Braze-Datenimportschlüssel und den Braze-REST-Endpunkt an Ihren Kubit-Supportkontakt weiter. Er wird die Integration auf seiner Seite konfigurieren und Sie benachrichtigen, sobald die Integration aktiv ist.  

### Schritt 3: Kohorten zum Hartlöten importieren

#### Erstellen Sie eine Kohorte in Kubit
[Erstellen Sie eine Kohorte](https://www.kubit.ai/doc/fundamentals#cohort) in Kubit und definieren Sie die Kriterien Ihrer Zielnutzer.<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Benutzer in Braze importieren
Sobald Sie Ihre Kohorte gespeichert haben, können Sie sie in Braze importieren, um sie in Braze-Segmenten zu verwenden. Diese Segmente können dann verwendet werden, um gezielte E-Mail- oder Push-Kampagnen und Canvases zu erstellen.

Navigieren Sie dazu zu Ihrer bestehenden Kohorte und wählen Sie unter **Kohortensteuerung** die Option **In Braze importieren**.

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Wählen Sie dann die gewünschte Importkadenz. Einmalige Importe ermöglichen es Ihnen jetzt, einmal zu importieren. Geplante Importe ermöglichen es Ihnen, täglich, wöchentlich oder monatlich zu einem bestimmten Zeitpunkt zu importieren. Beachten Sie, dass jede Kohorte nur einen Live-Importplan haben kann. 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

#### Überprüfen Sie den Importstatus
Sobald ein Import abgeschlossen ist, wird eine E-Mail-Benachrichtigung an den/die im Importplan angegebenen Empfänger gesendet. Sie können den Importstatus einer Kohorte auch unter **Zeitplan** in Kubit überprüfen. Der Zeitplanverlauf zeigt die Ausführungszeit des Imports, das Ergebnis und die Gesamtzahl der Benutzer in der Kohorte, die in Braze importiert wurden.<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Sie können einen Import manuell auslösen, indem Sie auf das Symbol **In Braze importieren** für diesen Importplan klicken.

### Schritt 4: Erstellen Sie Braze-Segmente mit Kubit-Kohorten
Nachdem Sie Kohorten in Braze importiert haben, können Sie diese als Filter verwenden, um Braze-Segmente zu erstellen und sie in Braze-Kampagnen oder Canvas einzubeziehen. Besuchen Sie unsere Segmentdokumentation, um mehr darüber zu erfahren, [wie Sie Braze-Segmente erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![Im Braze Segment Builder wird das Benutzerattribut "Kubit-Kohorten" auf "includes_value" gesetzt und zeigt eine Liste der verfügbaren Kohorten an.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.