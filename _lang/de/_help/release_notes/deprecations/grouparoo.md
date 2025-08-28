---
nav_title: Grouparoo
page_order: 1
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Grouparoo, einem Open-Source Reverse ETL-Tool, mit dem Sie Ihre Marketing-, Vertriebs- und Support-Tools ganz einfach mit den Daten in Ihrem Data Warehouse betreiben können."
page_type: update

---

# Grouparoo

{% alert update %}
Die Unterstützung für Grouparoo wurde im April 2022 eingestellt.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/) ist ein quelloffenes Reverse ETL-Tool, mit dem Sie Ihre Marketing-, Vertriebs- und Support-Tools ganz einfach mit den Daten in Ihrem Warehouse betreiben können. Die Konfiguration erfolgt in einem modellzentrierten UI, so dass auch nicht-technische Teammitglieder Datenabgleiche zur Unterstützung des Betriebs konfigurieren und Zeitpläne erstellen können.

Die Integration von Braze und Grouparoo macht es einfach, die in einem Shop gespeicherten Daten zu operationalisieren, indem sie an Braze gesendet werden. Wenn Sie automatische Zeitpläne für die Synchronisierung einrichten, können Sie die Kommunikation mit Ihren Kund:in ständig mit aktuellen Informationen verbessern.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Grouparoo Konto und Projekt | Sie benötigen ein Grouparoo-Konto und ein Projekt, um die Vorteile dieser Partnerschaft zu nutzen.<br><br>Diese Integration kann sowohl mit der kostenlosen Community Edition als auch mit den Enterprise Lösungen von Grouparoo genutzt werden. Die Einrichtung erfolgt über die Benutzeroberfläche der Grouparoo-Konfiguration. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit Nutzer:innen und Tracking-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt](https://www.grouparoo.com/). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Braze App in Grouparoo

Navigieren Sie in Grouparoo zu **Apps** und wählen Sie **Braze** aus, um eine neue Braze App zu erstellen. Geben Sie in dem daraufhin angezeigten Modal Ihren Braze API-Schlüssel und den REST-Endpunkt an.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### Schritt 2: Einrichten eines Modells und einer Datenquelle

Diese Integration setzt voraus, dass Sie ein bestehendes Modell und eine Datenquelle eingerichtet haben, bevor Sie mit dem nächsten Schritt fortfahren. Wenn Sie dies noch nicht eingerichtet haben, besuchen Sie die Dokumentation von Grouparoo, um zu erfahren, wie Sie ein [Modell](https://www.grouparoo.com/docs/config/models) und eine [Datenquelle](https://www.grouparoo.com/docs/config/sources) einrichten können.

### Schritt 3: Erstellen Sie ein Braze-Ziel in Grouparoo

#### Synchronisationsmodus auswählen

Wählen Sie in Grouparoo Ihr Modell in der Navigationsleiste aus. Blättern Sie dann zum Abschnitt **Ziele** und klicken Sie auf **Neues Ziel hinzufügen**.

Wählen Sie dann die von Ihnen erstellte **Braze** App aus, benennen Sie das Ziel und wählen Sie den gewünschten Synchronisierungsmodus aus den folgenden Möglichkeiten aus:
- **Sync**: Fügen Sie bei Bedarf Nutzer:innen hinzu, aktualisieren und entfernen Sie sie. Diese Option sucht nach neuen Datensätzen, Änderungen an bestehenden Datensätzen und Löschungen.
- **Zusatzstoff**: Fügen Sie bei Bedarf Nutzer:innen hinzu und aktualisieren Sie sie, aber entfernen Sie niemanden. Diese Option sucht nach neuen Nutzer:innen, die Braze hinzugefügt werden sollen, und nach Änderungen an bestehenden Nutzer:innen, verfolgt aber nicht das Tracking von Löschungen.
- **Bereichern**: Aktualisieren Sie nur die Nutzer:innen, die bereits in Braze existieren. Nutzer:innen nicht hinzufügen oder entfernen. Mit dieser Option werden nur bestehende Nutzer:innen in Braze aktualisiert.

#### Abbildung von Eigenschaftsfeldern

Als nächstes müssen Sie Grouparoo-Eigenschaftsfelder auf Braze-Eigenschaftsfelder abbilden. 

![Beispielfelder für die Abbildung von Eigenschaften. Grouparoo userID wird so eingestellt, dass sie auf external_id abgebildet wird. email, firstName und lastName werden als äquivalente grouparoo-Felder "email", "first_name" und "last_name" eingestellt.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Stellen Sie sicher, dass das Feld Braze `external_id` dem Primärschlüssel in Ihrer Quelltabelle zugeordnet ist. Bilden Sie den Rest der Felder nach Bedarf für Ihren Anwendungsfall ab.

Abschnitt **Eigenschaften des Datensatzes senden**: Eine Liste der voreingestellten Felder des Nutzerprofils, die für die Abbildung von Daten zur Verfügung stehen. Jede dieser Eigenschaften kann mit Eigenschaften von Grouparoo synchronisiert werden.

Abschnitt **Optionale Braze Benutzerprofil Felder**: Erstellen Sie optional angepasste Braze Nutzerprofil-Felder. Wenn Sie auf **Neues Nutzerprofilfeld hinzufügen** klicken, werden alle verfügbaren Eigenschaften angezeigt, die Sie Braze zuordnen können. Der Name jedes neuen Feldes, das Sie erstellen, ist derselbe wie die Eigenschaft Grouparoo, kann aber umbenannt werden.

#### Grouparoo Gruppen

Neben der Abbildung können Sie auch Grouparoo-Gruppen zu Abo-Gruppen von Braze hinzufügen. 

![Unter "Abo-Gruppen" im Grouparoo-Zielkonfigurationsfenster wird die Grouparoo-Gruppe "Hoher Wert mit jüngstem Autokauf" der Abo-Gruppe "Hoher Wert mit jüngstem Autokauf" von Braze hinzugefügt.]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Weitere Details und Updates zu dieser Integration finden Sie in der [Dokumentation von Grouparoo.](https://www.grouparoo.com/docs/integrations/grouparoo-braze)
{% endalert %}

