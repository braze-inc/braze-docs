---
nav_title: Hightouch
article_title: Hightouch Cohort Import
description: "Dieser Referenzartikel beschreibt die Kohorten-Importfunktion von Hightouch, einer Plattform zur Synchronisierung Ihrer Kundendaten aus Ihrem Lager mit Business-Tools."
page_type: partner
search_tag: Partner

---
# Hightouch-Kohorte importieren

> Dieser Artikel beschreibt, wie Sie Benutzerkohorten aus [Hightouch][1] in Braze importieren, damit Sie gezielte Kampagnen auf der Grundlage von Daten versenden können, die möglicherweise nur in Ihrem Warehouse vorhanden sind. Weitere Informationen zur Integration von Hightouch und seinen anderen Funktionen finden Sie im [Hauptartikel zu Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/hightouch/).

## Integration von Datenimporten

### Schritt 1: Holen Sie sich den Braze-Datenimportschlüssel
Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Hightouch**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.<br><br>![][6]{: style="max-width:90%;"} 

### Schritt 2: Braze-Kohorten als Ziel in Hightouch hinzufügen
Navigieren Sie zur Seite **Ziel** in Ihrem Hightouch-Arbeitsbereich, suchen Sie nach **Braze Cohorts** und klicken Sie auf **Weiter**. Übernehmen Sie dort Ihren REST-Endpunkt und Ihren Datenimportschlüssel und klicken Sie auf **Weiter**.<br><br>![][7]{: style="max-width:90%;"}

### Schritt 3: Synchronisieren Sie ein Modell (oder eine Zielgruppe) in Braze Cohorts
Erstellen Sie in Hightouch mit Ihrem erstellten [Modell](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) oder Ihrer [Zielgruppe](https://hightouch.io/docs/audiences/usage/) eine neue Synchronisierung. Als nächstes wählen Sie das Ziel Braze Cohorts, das Sie im vorherigen Schritt erstellt haben. Schließlich wählen Sie in der Zielkonfiguration von Braze Cohorts den Identifikator aus, den Sie abgleichen möchten, und entscheiden, ob Sie möchten, dass Hightouch eine neue Braze Cohort erstellt oder eine bestehende aktualisiert.<br><br>![][8]{: style="max-width:90%;"}

### Schritt 4: Erstellen Sie ein Braze-Segment aus der benutzerdefinierten Hightouch-Zielgruppe
Navigieren Sie in Braze zu **Segmente**, erstellen Sie ein neues Segment und wählen Sie **Hightouch Cohorts** als Filter. Von hier aus können Sie wählen, welche Hightouch-Kohorte Sie einbeziehen möchten. Nachdem Sie Ihr Hightouch-Kohortensegment erstellt haben, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.<br><br>![][9]{: style="max-width:90%;"}

### Mit dieser Integration
Um Ihr Hightouch-Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Canvas und wählen das Segment als Ihre Zielgruppe aus.<br><br>![][10]{: style="max-width:90%;"}

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

[1]: https://hightouch.io
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %}
[7]: {% image_buster /assets/img/hightouch/cohort1.png %}
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  