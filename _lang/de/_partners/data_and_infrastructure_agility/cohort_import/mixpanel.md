---
nav_title: Mixpanel
article_title: Mixpanel-Kohorten-Import
description: "Dieser Referenzartikel beschreibt die Kohorten-Importfunktion von Mixpanel, einer Business Analytics-Plattform, die es Ihnen ermöglicht, Mixpanel-Kohorten in Braze zu importieren, um Braze-Segmente zu erstellen, die für die Ausrichtung von Benutzern in zukünftigen Braze-Kampagnen oder Canvases verwendet werden können."
page_type: partner
search_tag: Partner
---

# Mixpanel-Kohorte importieren

> Dieser Artikel beschreibt, wie Sie Benutzerkohorten aus [Mixpanel](https://mixpanel.com/) in Braze importieren. Weitere Informationen zur Integration von Mixpanel und seinen anderen Funktionen finden Sie im [Hauptartikel über Mixpanel]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/mixpanel_for_currents/).

## Integration von Datenimporten

Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

{% alert important %}
In Übereinstimmung mit den Datenaufbewahrungsrichtlinien von Mixpanel werden Ereignisse, die vor dem 1\. Januar 2010 gesendet wurden, beim Import entfernt.
{% endalert %}

### Schritt 1: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Mixpanel**. Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Mixpanel einrichten.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Schritt 2: Einrichten der Braze-Integration in Mixpanel

Navigieren Sie in Mixpanel zu **Datenverwaltung > Integrationen.** Wählen Sie dann die Registerkarte Braze-Integration und klicken Sie auf **Verbinden**. Geben Sie in der daraufhin angezeigten Aufforderung den Braze-Datenimportschlüssel und den REST-Endpunkt an und klicken Sie auf **Weiter**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Schritt 3: Exportieren Sie eine Mixpanel-Kohorte nach Braze

Navigieren Sie in Mixpanel zu **Datenverwaltung > Kohorten**. Wählen Sie die Kohorte aus, die Sie an Braze senden möchten, und wählen Sie dann **Nach Braze exportieren**. Wählen Sie schließlich eine einmalige Synchronisierung oder eine dynamische Synchronisierung. Wenn Sie die dynamische Synchronisierung wählen, wird Ihre Braze-Kohorte alle 15 Minuten mit den Benutzern in Mixpanel synchronisiert. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### Schritt 4: Segmentierte Benutzer in Braze

Um in Braze ein Segment für diese Benutzer zu erstellen, gehen Sie zu **Zielgruppe** > **Segmente**, benennen Sie Ihr Segment und wählen Sie **Mixpanel_Cohorts** als Filter. Als nächstes verwenden Sie die Option "Includes" und wählen die Kohorte, die Sie in Mixpanel erstellt haben. 

![In der Braze-Segmenterstellung wird der Benutzerattributfilter "Mixpanel-Kohorten" auf "umfasst" und "Braze-Kohorte" gesetzt.]({% image_buster /assets/img_archive/mixpanel1.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Nutzer ansprechen verwenden.

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.