---
nav_title: Treasure Data
article_title: Schatzdaten-Kohorten-Import
description: "Dieser Referenzartikel beschreibt die Kohorten-Importfunktion von Treasure Data."
page_type: partner
search_tag: Partner

---
# Treasure Data Kohortenimport

> Dieser Artikel beschreibt, wie Sie Benutzerkohorten aus Treasure Data in Braze importieren, damit Sie gezielte Kampagnen auf der Grundlage von Daten versenden können, die möglicherweise nur in Ihrem Warehouse vorhanden sind.

{% alert important %}
Diese Funktion befindet sich derzeit in der Beta-Phase. Für weitere Informationen wenden Sie sich bitte an Ihre Treasure Data- und Braze-Vertretung.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Treasure Data Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data-Konto](https://www.treasuredata.com/). |
| Schlüssel Braze Data Import | Dies kann im Braze-Dashboard unter **Partner-Integrationen** > **Technologiepartner** und dann unter **Heap** erfasst werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Statische IP-Adresse von Treasure Data | Die statische IP-Adresse von Treasure Data ist der Zugangspunkt und die Quelle der Verknüpfung für diese Integration. Um die statische IP-Adresse zu ermitteln, wenden Sie sich an Ihren Treasure Data Customer Success Vertreter oder den technischen Support von Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Datenimporten

### Schritt 1: Holen Sie sich Ihren Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Treasure Data**. Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.

### Schritt 2: Erstellen Sie eine Datenverbindung

Bevor Sie Ihre Datenverbindung in Treasure Data erstellen, müssen Sie sich authentifizieren. Wählen Sie zunächst **Integrations Hub** und dann **Catalog**.

![Treasure Data Integrations Hub Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

Suchen Sie im **Katalog** nach der Braze-Integration, bewegen Sie dann den Mauszeiger über das Symbol und wählen Sie **Authentifizierung erstellen**. Geben Sie Ihre Anmeldedaten ein, geben Sie Ihrer Authentifizierung einen Namen und wählen Sie dann **Fertig**.

![Treasure Data Integrations Hub Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### Schritt 3: Definieren Sie Ihre Kohorte Zielgruppe

Synchronisieren Sie Ihre Kohorten mit Braze durch eine Aktivierung im **Audience Studio** oder durch Ausführen einer Abfrage in der **Data Workbench**.

{% alert important %}
Nur Benutzer, die bereits in Braze vorhanden sind, können einer Kohorte hinzugefügt oder entfernt werden. Cohort Import erstellt keine neuen Benutzer in Braze.
{% endalert %}

{% tabs local %}
{% tab Daten-Workbench %}
#### Schritt 3.1: Definieren Sie Ihre Anfrage

{% alert note %}
Abfragespalten müssen mit den genauen Spaltennamen und dem Datentyp angegeben werden. Die Abfragespalten müssen mindestens eine der Spalten enthalten: `user_ids`, `device_ids`, oder die Lötaliaspalten stimmen mit der Konfiguration auf der Benutzeroberfläche überein. Nur Benutzerprofile, die in Braze existieren, werden einer Kohorte hinzugefügt. Cohort Import erstellt keine neuen Benutzerprofile.
{% endalert %}

1. Navigieren Sie zu **Data Workbench** > **Abfragen**.
2. Wählen Sie **Neue Abfrage**.
3. Führen Sie die Abfrage aus, um die Ergebnismenge zu überprüfen.

![Treasure Data Integrations Hub Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Anwendungsfall: Kohorten nach Kennung synchronisieren

{% subtabs local %}
{% subtab Syncing External IDs %}
Hier ist eine Beispieltabelle in Treasure Data:

| external_id |	E-Mail	| geräte_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
Der Spaltenname muss `user_ids` lauten, sonst schlägt die Synchronisierung fehl.
{% endalert %}

Um Kohorten unter Verwendung der externen ID zu synchronisieren, führen Sie die folgende Abfrage aus:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Nachdem Sie die Abfrage ausgeführt haben, werden diese Benutzer-Aliase der Kohorte in Braze hinzugefügt:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Hier ist eine Beispieltabelle in Treasure Data:

| external_id |	E-Mail	| geräte_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

Um Kohorten unter Verwendung des Benutzer-Alias zu synchronisieren, führen Sie die folgende Abfrage aus:

```sql
SELECT
  email
FROM
  example_cohort_table
```

Nachdem Sie die Abfrage ausgeführt haben, werden diese Benutzer-Aliase der Kohorte in Braze hinzugefügt:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Hier ist eine Beispieltabelle in Treasure Data:

| external_id |	E-Mail	| geräte_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
Der Spaltenname muss `device_ids` lauten, sonst schlägt die Synchronisierung fehl.
{% endalert %}

Um Kohorten anhand der Geräte-ID zu synchronisieren, führen Sie die folgende Abfrage aus:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Nachdem Sie die Abfrage ausgeführt haben, werden diese Geräte-IDs der Kohorte in Braze hinzugefügt:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Schritt 3.2: Geben Sie das Ziel für den Export der Ergebnisse an

Sobald die Abfrage erstellt wurde, wählen Sie **Ergebnisse exportieren**. Sie können eine vorhandene Authentifizierung auswählen, z.B. die in den letzten Schritten erstellte, oder eine neue Authentifizierung erstellen, die für die Ausgabe verwendet werden soll. 

![Treasure Data Integrations Hub Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| Ergebniszuordnung exportieren |	Beschreibung	| 
| ----------- | ----------- |
| Kohorten-ID	| Dies ist der Backend-Kohortenidentifikator, der an Braze gesendet wird. 	|
| Name der Kohorte (optional)	| Dies ist der Name, der innerhalb des Kohortenfilters im Segmentierungstool von Braze angezeigt wird. Wenn dies nicht eingestellt ist, wird die `Cohort ID` als `Cohort Name` verwendet.	|
| Operation	| Wird verwendet, um zu bestimmen, ob die Abfrage Profile aus der Kohorte in Braze hinzufügen oder entfernen soll.	| 
| Aliasnamen (Optional) | Wenn definiert, wird der Name der entsprechenden Spalte innerhalb Ihrer Abfrage als `alias_label` gesendet und die Werte jeder Zeile in der Spalte werden als `alias_name` gesendet.	| 
| Fadenzahl | Anzahl der gleichzeitigen API-Aufrufe. |

Folgen Sie den [Schritten von Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget), um Ihren Export für Ihren Anwendungsfall zu konfigurieren.

#### Schritt 3.3: Führen Sie die Abfrage aus

Speichern Sie die Abfrage unter einem Namen und führen Sie sie aus, oder führen Sie die Abfrage einfach aus. Nach erfolgreichem Abschluss der Abfrage wird das Abfrageergebnis automatisch nach Braze exportiert.

{% endtab %}
{% tab Publikumsstudio %}
#### Schritt 3.1: Eine Aktivierung erstellen

Erstellen Sie ein neues Segment oder wählen Sie ein bestehendes Segment, um es mit Braze als Kohorte zu synchronisieren. Wählen Sie innerhalb des Segments **Aktivierung erstellen**.

#### Schritt 3.2: Füllen Sie Ihre Aktivierungsdaten aus

![Treasure Data Integrations Aktivierungsdetails]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| Einstellung der Aktivierungsdetails |	Beschreibung	| 
| ----------- | ----------- |
| Aktivierung Name	| Der Name Ihrer Aktivierung.	|
| Aktivierung Beschreibung| Eine kurze Beschreibung der Aktivierung.	|
| Authentifizierung	| Wählen Sie die in Schritt 2 erstellte Braze-Kohortenauthentifizierung.	| 
| Kohorten-ID	| Dies ist der Backend-Kohortenidentifikator, der an Braze gesendet wird. 	|
| Name der Kohorte (optional)	| Dies ist der Name, der innerhalb des Kohortenfilters im Segmentierungstool von Braze angezeigt wird. Wenn dies nicht eingestellt ist, wird die `Cohort ID` als `Cohort Name` verwendet.	|
| Operation	| Wird verwendet, um zu bestimmen, ob die Abfrage Profile aus der Kohorte in Braze hinzufügen oder entfernen soll.	| 
| Aliasnamen (Optional) | Wenn definiert, wird der Name der entsprechenden Spalte innerhalb Ihrer Abfrage als `alias_label` gesendet und die Werte jeder Zeile in der Spalte werden als `alias_name` gesendet.	| 
| Fadenzahl | Anzahl der gleichzeitigen API-Aufrufe. |

#### Schritt 3.3: Mapping der Ausgabe einrichten

![Treasure Data Integrations Aktivierung Output Mapping]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| Aktivierung Ausgang Mapping |	Beschreibung	| 
| ----------- | ----------- |
| Attribut-Spalten	| Bestimmen Sie die Spalten aus Ihrer Segmentdatenbank, die bei der Synchronisierung von Profilen mit einer Braze-Kohorte als Identifikatoren zugeordnet werden sollen.	|
| String Builder| Der String Builder ist für die Integration von Braze nicht erforderlich.	|

{% alert important %}
 - Wenn Sie `device_id` als Bezeichner verwenden, muss der **Name der Ausgabespalte** `device_ids` lauten.
 - Wenn Sie Aliase als Bezeichner verwenden, muss der **Name der Ausgabespalte** der Name der entsprechenden Spalte innerhalb Ihrer Abfrage sein, die als `alias_label` gesendet wird, und die Werte der einzelnen Zeilen in der Spalte werden als `alias_name` gesendet.
 - Wenn Sie `external_id` als Bezeichner verwenden, muss der **Name der Ausgabespalte** `user_ids` lauten.
{% endalert %}

Alle nicht relevanten oder falsch benannten Spaltennamen werden ignoriert. Sie können mehr als einen Bezeichner für Ihre Synchronisierungen verwenden.

#### Schritt 3.4: Definieren Sie Ihren Aktivierungszeitplan

Legen Sie Ihren gewünschten Synchronisierungszeitplan fest und speichern Sie Ihre Aktivierung.

![Treasure Data Integrations Aktivierungszeitplan]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Schritt 4: Erstellen Sie ein Braze-Segment aus dem Treasure Data Export

Navigieren Sie in Braze zu **Segmente**, erstellen Sie ein neues Segment und wählen Sie **Treasure Data Cohorts** als Ihren Filter. Von hier aus können Sie wählen, welche Treasure Data-Kohorte Sie einbeziehen möchten. Nachdem Sie Ihr Treasure Data-Kohortensegment erstellt haben, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.

![Treasure Data Integrations Hub Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.