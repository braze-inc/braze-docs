---
nav_title: Hightouch Kohorten Import
article_title: Hightouch Kohorten Import
description: "Dieser referenzierte Artikel beschreibt die Kohortenimport-Funktionalität von Hightouch, einer Plattform zur Synchronisierung Ihrer Kundendaten aus Ihrem Data Warehouse mit Business Tools."
page_type: partner
search_tag: Partner

---
# Hightouch Kohortenimport

> Dieser Artikel beschreibt, wie Sie Kohorten von Nutzern:in aus [Hightouch](https://hightouch.io) nach Braze importieren, damit Sie gezielte Kampagnen auf der Grundlage von Daten versenden können, die möglicherweise nur in Ihrem Warehouse vorhanden sind. Weitere Informationen zur Integration von Hightouch und seinen anderen Funktionen finden Sie im [Hauptartikel zu Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch/).

## Integration von Datenimporten

### Schritt 1: Holen Sie sich den Braze Datenimport-Schlüssel
Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Hightouch** aus. 

Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.<br><br>![]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"} 

### Schritt 2: Braze Kohorten als Ziel in Hightouch hinzufügen
Navigieren Sie zu der Seite **Ziele** in Ihrem Hightouch Workspace, suchen Sie nach **Braze Kohorten** und klicken Sie auf **Weiter**. Nehmen Sie von dort Ihren REST-Endpunkt und Ihren Datenimport-Schlüssel und klicken Sie auf **Weiter**.<br><br>![]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Schritt 3: Synchronisieren Sie ein Modell (oder eine Zielgruppe) mit Braze Kohorten
Erstellen Sie in Hightouch unter Verwendung Ihrer erstellten [Modelle](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) oder [Zielgruppen](https://hightouch.io/docs/audiences/usage/) eine neue Synchronisierung. Wählen Sie dann das Ziel Braze Kohorten aus, das Sie im vorherigen Schritt erstellt haben. Schließlich wählen Sie in der Zielkonfiguration für Braze Kohorten den Bezeichner aus, den Sie abgleichen möchten, und entscheiden, ob Hightouch eine neue Braze Kohorte erstellen oder eine bestehende aktualisieren soll.<br><br>![]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

### Schritt 4: Erstellen Sie ein Braze-Segment aus der angepassten Zielgruppe von Hightouch
Navigieren Sie in Braze zu **Segmente**, erstellen Sie ein neues Segment, und wählen Sie **Hightouch Kohorten** als Filter. Von hier aus können Sie wählen, welche Hightouch Kohorte Sie einbeziehen möchten. Nachdem Ihr Hightouch Kohorten-Segment erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.<br><br>![]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Verwendung dieser Integration
Um Ihr Hightouch-Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas und wählen Sie das Segment als Ihre Zielgruppe aus.<br><br>![]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

