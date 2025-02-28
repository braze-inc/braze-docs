---
nav_title: Grouparoo
page_order: 1
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Grouparoo, einem Open-Source-Reverse-ETL-Tool, mit dem Sie Ihre Marketing-, Vertriebs- und Support-Tools ganz einfach mit den Daten in Ihrem Data Warehouse betreiben können."
page_type: update

---

# Grouparoo

{% alert update %}
Die Unterstützung für Grouparoo wurde im April 2022 eingestellt.
{% endalert %}

> [Grouparoo][1] ist ein Open-Source-Reverse-ETL-Tool, mit dem Sie Ihre Marketing-, Vertriebs- und Support-Tools ganz einfach mit den Daten in Ihrem Warehouse betreiben können. Die Konfiguration erfolgt über eine modellzentrierte Benutzeroberfläche, so dass auch nicht-technische Teammitglieder Datenabgleiche zur Unterstützung des Betriebs konfigurieren und planen können.

Die Integration von Braze und Grouparoo macht es einfach, die in einem Warehouse gespeicherten Daten zu operationalisieren, indem Sie sie an Braze senden. Wenn Sie automatische Synchronisierungszeitpläne einrichten, können Sie die Kommunikation mit Ihren Kunden ständig mit aktuellen Informationen verbessern.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Grouparoo Konto und Projekt | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Grouparoo-Konto und ein Projekt.<br><br>Diese Integration kann mit der kostenlosen Community Edition und den Unternehmenslösungen von Grouparoo genutzt werden. Die Einrichtung erfolgt über die Grouparoo Konfigurationsoberfläche. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit Benutzer- und Track-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1 Erstellen Sie eine Braze-App in Grouparoo

Navigieren Sie in Grouparoo zu **Apps** und wählen Sie **Braze**, um eine neue Braze-App zu erstellen. Geben Sie in dem angezeigten Modal Ihren Braze-API-Schlüssel und den REST-Endpunkt an.

![][2]

### Schritt 2 Ein Modell und eine Datenquelle einrichten

Diese Integration setzt voraus, dass Sie ein bestehendes Modell und eine Datenquelle eingerichtet haben, bevor Sie mit dem nächsten Schritt fortfahren. Wenn Sie dies noch nicht eingerichtet haben, besuchen Sie die Grouparoo-Dokumentation, um zu erfahren, wie Sie ein [Modell](https://www.grouparoo.com/docs/config/models) und eine [Datenquelle](https://www.grouparoo.com/docs/config/sources) einrichten können.

### Schritt 3: Erstellen Sie ein Braze-Ziel in Grouparoo

#### Sync-Modus auswählen

Wählen Sie in Grouparoo Ihr Modell in der Navigationsleiste aus. Blättern Sie dann zum Abschnitt **Ziele** und klicken Sie auf **Neues Ziel hinzufügen**.

Wählen Sie dann die von Ihnen erstellte **Braze-App** aus, benennen Sie das Ziel und wählen Sie den gewünschten Synchronisierungsmodus aus:
- **Sync**: Fügen Sie bei Bedarf Braze-Benutzer hinzu, aktualisieren und entfernen Sie sie. Diese Option sucht nach neuen Datensätzen, Änderungen an bestehenden Datensätzen und Löschungen.
- **Zusatzstoff**: Fügen Sie bei Bedarf Braze-Benutzer hinzu und aktualisieren Sie sie, aber entfernen Sie niemanden. Diese Option sucht nach neuen Benutzern, die zu Braze hinzugefügt werden sollen, und nach Änderungen an bestehenden Braze-Benutzern, verfolgt aber nicht die Löschungen.
- **Bereichern**: Aktualisieren Sie nur die Benutzer, die bereits in Braze existieren. Sie können keine Benutzer hinzufügen oder entfernen. Mit dieser Option werden nur bestehende Benutzer in Braze aktualisiert.

#### Zuordnung von Eigenschaftsfeldern

Als nächstes müssen Sie Grouparoo-Eigenschaftsfelder den Braze-Eigenschaftsfeldern zuordnen. 

![Beispielfelder für die Zuordnung von Eigenschaften. Grouparoo userID wird so eingestellt, dass sie auf external_id abgebildet wird. email, firstName und lastName werden als entsprechende grouparoo-Felder "email", "first_name" und "last_name" eingestellt.][3]{: style="max-width:80%;"}

Stellen Sie sicher, dass das Feld Braze `external_id` dem Primärschlüssel in Ihrer Quelltabelle zugeordnet ist. Ordnen Sie die übrigen Felder nach Bedarf für Ihren Anwendungsfall zu.

Abschnitt **Datensatzeigenschaften senden**: Eine Liste der voreingestellten Benutzerprofilfelder, die für die Zuordnung von Daten zur Verfügung stehen. Jedes dieser Objekte kann mit den Grouparoo-Eigenschaften synchronisiert werden.

**Optionaler** Abschnitt **Braze Benutzerprofilfelder**: Erstellen Sie optionale benutzerdefinierte Braze-Benutzerprofilfelder. Wenn Sie auf **Neues Braze-Benutzerprofilfeld hinzufügen** klicken, werden alle verfügbaren Eigenschaften angezeigt, die Sie Braze zuordnen können. Der Name jedes neuen Feldes, das Sie erstellen, ist derselbe wie die Eigenschaft Grouparoo, kann aber umbenannt werden.

#### Grouparoo Gruppen

Zusätzlich zum Mapping können Sie auch Grouparoo-Gruppen zu Braze-Abonnementgruppen hinzufügen. 

![Unter "Braze-Abonnementgruppen" im Grouparoo-Zielkonfigurationsfenster wird die Grouparoo-Gruppe "Hoher Wert mit kürzlich erfolgtem Autokauf" zur Braze-Abonnementgruppe "Hoher Wert mit kürzlich erfolgtem Autokauf" hinzugefügt.][4]{: style="max-width:80%;"}

{% alert important %}
Weitere Details und Aktualisierungen zu dieser Integration finden Sie in der [Dokumentation von Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

[1]: https://www.grouparoo.com/
[2]: {% image_buster /assets/img/grouparoo/add-app.png %}
[3]: {% image_buster /assets/img/grouparoo/mapping.png %}
[4]: {% image_buster /assets/img/grouparoo/lists.png %}