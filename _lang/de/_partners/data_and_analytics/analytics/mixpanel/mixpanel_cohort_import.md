---
nav_title: Mixpanel
article_title: Mixpanel Kohorten-Import
description: "Dieser Artikel referenziert die Kohortenimport-Funktionalität von Mixpanel, einer Business Analytics-Plattform, die es Ihnen erlaubt, Mixpanel Kohorten in Braze zu importieren, um Braze Segmente zu erstellen, die für das Targeting von Nutzern:innen in zukünftigen Kampagnen oder Canvase verwendet werden können."
page_type: partner
search_tag: Partner
---

# Mixpanel Kohortenimport

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten von [Mixpanel](https://mixpanel.com/) nach Braze importieren. Weitere Informationen zur Integration von Mixpanel und seinen anderen Funktionen finden Sie im [Hauptartikel über Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

## Integration von Datenimporten

Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

{% alert important %}
In Übereinstimmung mit den Richtlinien von Mixpanel zur Bindung von Daten werden Ereignisse, die vor dem 1\. Januar 2010 gesendet wurden, beim Import entfernt.
{% endalert %}

### Schritt 1: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Mixpanel** aus. Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. 

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Mixpanel einrichten.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Schritt 2: Einrichten der Integration von Braze in Mixpanel

Navigieren Sie in Mixpanel zu **Datenverwaltung > Integrationen.** Wählen Sie dann den Tab Integration von Braze aus und klicken Sie auf **Verbinden**. Geben Sie in der daraufhin angezeigten Aufforderung den Datenimport-Schlüssel und den REST-Endpunkt von Braze an und klicken Sie auf **Weiter**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Schritt 3: Exportieren Sie eine Mixpanel-Kohorte nach Braze

Navigieren Sie in Mixpanel zu **Datenverwaltung > Kohorten.** Wählen Sie die Kohorte aus, die Sie an Braze senden möchten, und wählen Sie dann **Nach Braze exportieren**. Wählen Sie schließlich eine einmalige oder dynamische Synchronisierung aus. Wenn Sie die dynamische Synchronisierung auswählen, wird Ihre Braze Kohorte alle 15 Minuten mit den Nutzer:innen in Mixpanel synchronisiert. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

### Schritt 4: Segmentierung der Nutzer:innen in Braze

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, gehen Sie zu **Zielgruppe** > **Segmente**, benennen Sie Ihr Segment und wählen Sie **Mixpanel_Cohorts** als Filter aus. Als nächstes verwenden Sie die Option "enthält" und wählen die Kohorte, die Sie in Mixpanel erstellt haben. 

![In der Segmentierung von Braze wird der Filter für die Nutzer:in-Attribute "Mixpanel Kohorten" auf "umfasst" und "Braze Kohorte" gesetzt.]({% image_buster /assets/img_archive/mixpanel1.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Targeting Nutzer:innen referenzieren.

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.