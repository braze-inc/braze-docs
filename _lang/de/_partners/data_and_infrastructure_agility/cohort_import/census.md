---
nav_title: Volkszählung
article_title: Volkszählungs-Kohorte Import
description: "Dieser Referenzartikel beschreibt die Kohortenimportfunktion von Census, einer Datenintegrationsplattform, mit der Sie dynamisch gezielte Benutzersegmente mit Daten aus Ihrem Cloud Warehouse erstellen können."
page_type: partner
search_tag: Partner

---

# Import von Volkszählungs-Kohorten

> Dieser Artikel beschreibt, wie Sie Benutzerkohorten aus [Census][1] in Braze importieren. Weitere Informationen zur Integration der Volkszählung finden Sie im [Hauptartikel Volkszählung]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/census/).

## Integration von Kohortenimporten

### Schritt 1: Braze Serviceverbindung erstellen

Um Census in die Census-Plattform zu integrieren, navigieren Sie zur Registerkarte **Verbindungen** und wählen Sie **Neues Ziel**, um eine neue Braze-Serviceverbindung zu erstellen.

In der daraufhin angezeigten Eingabeaufforderung geben Sie dieser Verbindung einen Namen und Ihre Braze-Endpunkt-URL, den Braze REST API-Schlüssel und den Datenimportschlüssel an. Der Datenimportschlüssel ist für die Synchronisierung von Kohorten erforderlich und kann in Braze unter **Partnerintegrationen** > **Technologiepartner** > **Zählung** gefunden werden.

![][8]{: style="max-width:60%;"}

### Schritt 2: Eine Census-Synchronisation erstellen

Um Kunden mit Braze zu synchronisieren, müssen Sie eine Synchronisierung erstellen. Hier legen Sie fest, wohin die Daten synchronisiert werden sollen und wie die Felder zwischen den beiden Plattformen zugeordnet werden sollen.

1. Navigieren Sie zur Registerkarte **Syncs** und wählen Sie **Neue Sync**.<br><br> 
2. Wählen Sie im Composer das Quelldatenmodell aus Ihrem Data Warehouse.<br><br>
3. Legen Sie fest, wohin das Modell synchronisiert werden soll. Wählen Sie **Braze** als Ziel und **User & Cohort** als zu synchronisierendes Objekt.<br>![In der Eingabeaufforderung "Wählen Sie ein Ziel" wird "Braze" als Verbindung ausgewählt, und es werden verschiedene Objekte aufgelistet.][10]{: style="max-width:80%;"}<br><br>
4. Wählen Sie die **Quellspalte** aus, die die Benutzer identifiziert, die einer Kohorte hinzugefügt werden sollen, und wählen Sie als **Identifizierungstyp** **Externe Benutzer-ID**.<br><br>
5. Wählen Sie in der Dropdown-Liste **Kohortenname** eine Kohorte aus, erstellen Sie eine Kohorte oder wählen Sie eine Quellenspalte, um den Kohortennamen zu füllen.<br><br>
6. Verwenden Sie das Dropdown-Menü **Wenn ein Datensatz aus den Quelldaten entfernt wird**, um auszuwählen, was mit den Benutzern geschieht, wenn sie aus dem Quelldatensatz entfernt werden, z. B. **Nichts tun** oder **Übereinstimmenden Datensatz aus Kohorte entfernen**.<br><br>
7. Zum Schluss ordnen Sie die Census-Datenfelder den entsprechenden Braze-Feldern zu.<br>![Kartierung der Volkszählung][11]{: style="max-width:80%;"}<br><br>
8. Bestätigen Sie die Details und erstellen Sie die Synchronisierung. 

Jetzt können Sie Ihre Synchronisierung durchführen!

Bei einer Synchronisierung werden alle Felder, die Sie zuordnen, zunächst mit dem Benutzerobjekt synchronisiert, um die bereits in Braze vorhandenen Felder zu aktualisieren. Danach wird der aktualisierte Benutzer zu der angegebenen Kohorte hinzugefügt.

Nach der Synchronisierung können Sie ein Braze-Segment mit einem Census-Kohortenfilter erstellen und zu zukünftigen Braze-Kampagnen und Canvases hinzufügen, um diese Benutzer anzusprechen. 

{% alert note %}
Wenn Sie die Integration von Census und Braze verwenden, sendet Census bei jeder Synchronisierung nur die Deltas (sich ändernde Daten) an Braze.
{% endalert %}

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

[1]: https://www.getcensus.com/
[8]: {% image_buster /assets/img/census/add_service.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}