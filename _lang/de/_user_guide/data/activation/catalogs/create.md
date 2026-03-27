---
nav_title: Katalog erstellen
article_title: Erstellen Sie einen Katalog
alias: "/catalogs/"
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie Kataloge erstellen, die über Liquid auf Nicht-Nutzerdaten in Braze-Kampagnen verweisen."
---

# Katalog erstellen

> Um einen Katalog zu erstellen, importieren Sie eine CSV-Datei mit Nicht-Nutzerdaten in Braze. Anschließend können Sie auf diese Informationen zugreifen, um Ihre Nachrichten anzureichern. Sie können jede Art von Daten in einen Katalog einbringen. Bei diesen Daten handelt es sich in der Regel um Metadaten Ihres Unternehmens, z. B. Produktinformationen für ein E-Commerce-Unternehmen oder Kursinformationen für einen Bildungsanbieter.

## Anwendungsfälle

Häufige Anwendungsfälle für Kataloge sind unter anderem:

- Produkte
- Dienste
- Lebensmittel
- Anstehende Ereignisse
- Musik
- Pakete

Nachdem diese Informationen importiert wurden, können Sie in Nachrichten darauf zugreifen – ähnlich wie auf angepasste Attribute oder Event-Eigenschaften über Liquid.

## Unterstützte Datentypen {#supported-data-types}

Die folgende Tabelle listet die unterstützten Katalogdatentypen auf und beschreibt, wie sie erstellt oder aktualisiert werden können.

| Datentyp    | Beschreibung                                   | Verfügbar über CSV-Upload | Verfügbar über API und CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| String       | Eine Folge von Zeichen.                     | ✅ Ja                    | ✅ Ja                     |
| Zahl       | Ein numerischer Wert, entweder eine ganze Zahl oder eine Gleitkommazahl.     | ✅ Ja                    | ✅ Ja                     |
| Boolescher Wert      | Ein `true`- oder `false`-Wert.                    | ✅ Ja                    | ✅ Ja                     |
| Uhrzeit         | Ein im [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-Format formatierter String.                        | ✅ Ja                    | ✅ Ja                     |
| JSON-Objekt  | Ein verschachteltes Objekt mit Schlüssel-Wert-Paaren. Kann auf der Plattform angezeigt werden, kann jedoch nur über die API oder CDI erstellt oder aktualisiert werden.         | ⛔ Nein                     | ✅ Ja                     |
| String-Array | Eine Liste von Strings. Kann auf der Plattform angezeigt werden, kann jedoch nur über die API oder CDI erstellt oder aktualisiert werden. Maximal 100 Elemente. | ⛔ Nein                     | ✅ Ja                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Einen Katalog erstellen

Um einen Katalog zu erstellen, navigieren Sie zu **Dateneinstellungen** > **Kataloge**, wählen Sie **Neuen Katalog erstellen** und wählen Sie eine der folgenden Optionen aus:

{% tabs local %}
{% tab Upload CSV %}
### 1. Schritt: Überprüfen Sie Ihre CSV-Datei

Bevor Sie Ihre CSV-Datei hochladen, stellen Sie sicher, dass sie die folgenden Anforderungen erfüllt:

| CSV-Anforderung | Details |
|-----------------|---------|
| Kopfzeilen | Die erste Spalte in der CSV-Datei muss den Namen `id` tragen, und jede Zeile muss einen eindeutigen `id`-Wert enthalten. |
| Spalten | Eine CSV-Datei kann maximal 1.000 Felder (Spalten) enthalten, und jeder Spaltenname kann bis zu 250 Zeichen lang sein. |
| Dateigröße | Bei kostenlosen Tarifen ist die Gesamtgröße aller CSV-Dateien eines Unternehmens auf 100 MB begrenzt. Für Pro-Tarife beträgt die maximale Dateigröße für eine einzelne CSV-Datei 2 GB. |
| Feldwerte | Jede Zelle (Feldwert) kann bis zu 5.000 Zeichen enthalten. |
| Zulässige Zeichen | Die `id`-Spalte und alle Kopfzeilenwerte dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| Datentypen | Unterstützte Datentypen für CSV-Uploads umfassen Strings, Zahlen, Boolesche Werte und Zeitangaben. Die vollständige Liste der Datentypen, einschließlich derjenigen, die nur über die API und CDI verfügbar sind, finden Sie unter [Unterstützte Datentypen](#supported-data-types). |
| Formatierung | Formatieren Sie den gesamten Text in Kleinbuchstaben, um die Einheitlichkeit zu gewährleisten. |
| Kodierung | Speichern und laden Sie die CSV-Datei mit UTF-8-Kodierung hoch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Benötigen Sie mehr Platz für Ihre CSV-Dateien? Wenden Sie sich an Ihren Braze Account Manager, um weitere Informationen über Katalog-Upgrades zu erhalten.
{% endalert %}

### 2. Schritt: CSV hochladen

Ziehen Sie Ihre Datei per Drag-and-Drop in die Upload-Zone, oder wählen Sie **CSV hochladen** und wählen Sie Ihre Datei aus.

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Wählen Sie für jede Spalte einen Datentyp aus.

{% alert note %}
Dieser Datentyp kann nicht mehr bearbeitet werden, nachdem Sie Ihren Katalog eingerichtet haben. Außerdem wird ein `NULL`-Wert beim CSV-Upload nicht unterstützt und als String behandelt.
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Geben Sie einen Namen und optional eine Beschreibung für Ihren Katalog ein. Beachten Sie bei der Benennung Ihres Katalogs die folgenden Anforderungen:

  - Muss eindeutig sein
  - Maximal 250 Zeichen
  - Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten

{% alert tip %}
Sie können auch [Templates in einem Katalognamen verwenden](#template-catalog-names), um Katalognamen basierend auf Variablen wie Sprache oder Kampagne dynamisch zu generieren.
{% endalert %}

![Ein Katalog mit dem Namen "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Wählen Sie **Katalog verarbeiten**, um den Katalog zu erstellen.

{% alert important %}
Ihre CSV-Datei kann abgelehnt werden, wenn Sie Ihre [Tarifstufe](#tiers) überschreiten. 
{% endalert %}

### Anleitung: Erstellen eines Katalogs aus einer CSV-Datei

Diese Anleitung basiert auf einem Katalog, der zwei Spiele mit Preisangaben und einem Bildlink enthält.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Der Katalog wird erstellt, indem eine CSV-Datei hochgeladen wird. Die Datentypen für `id`, `title`, `price` und `image_link` sind String, String, Zahl und String. 

{% alert note %}
Dieser Datentyp kann nicht mehr bearbeitet werden, nachdem Sie Ihren Katalog eingerichtet haben.
{% endalert %}

![Vier Katalogspaltennamen: „id", „title", „price", „image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Als Nächstes benennen wir diesen Katalog „games_catalog" und wählen den Button **Katalog verarbeiten**. Anschließend prüft Braze den Katalog vor der Erstellung auf eventuelle Fehler.

![Ein Katalog mit dem Namen "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Beachten Sie, dass Sie diesen Namen nicht mehr ändern können, nachdem der Katalog erstellt wurde. Sie können einen Katalog löschen und eine aktualisierte Version unter demselben Katalognamen erneut hochladen.

Nachdem Sie den Katalog erstellt haben, können Sie damit beginnen, den [Katalog in einer Kampagne zu referenzieren]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Voraussetzungen

Bevor Sie Kataloge im Browser bearbeiten oder erstellen können, benötigen Sie die folgenden [Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) für Ihren Workspace:

- Kataloge anzeigen
- Kataloge bearbeiten
- Kataloge exportieren
- Kataloge löschen

{% multi_lang_include deprecations/user_permissions.md %}

### 1. Schritt: Katalogdetails eingeben

Geben Sie einen Namen und optional eine Beschreibung für Ihren Katalog ein. Beachten Sie bei der Benennung Ihres Katalogs die folgenden Anforderungen:

- Muss eindeutig sein
- Maximal 250 Zeichen
- Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten

{% alert tip %}
Sie können auch [Templates in einem Katalognamen verwenden](#template-catalog-names), um Katalognamen basierend auf Variablen wie Sprache oder Kampagne dynamisch zu generieren.
{% endalert %}

![Ein Katalog mit dem Namen "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### 2. Schritt: Ihren Katalog erstellen

Wählen Sie Ihren Katalog aus der Liste aus und wählen Sie anschließend **Katalog aktualisieren** > **Felder hinzufügen**. Geben Sie den **Feldnamen** ein und wählen Sie den Datentyp aus dem Dropdown-Menü aus. Wiederholen Sie den Vorgang nach Bedarf.

![Zwei Beispielfelder „rating" und „name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Wählen Sie **Katalog aktualisieren** > **Artikel hinzufügen**, um einen Artikel zu Ihrem Katalog hinzuzufügen, indem Sie die Informationen auf der Grundlage der zuvor hinzugefügten Felder eingeben. Wählen Sie dann **Artikel speichern** oder **Speichern und weiteren hinzufügen**, um mit dem Hinzufügen Ihrer Artikel fortzufahren.

![Einen Katalogartikel hinzufügen.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze verarbeitet Zeitwerte basierend auf dem Zeitstempel des Dashboards. Wenn eine Spalte z. B. den Wert „03/13/2024" aufweist und Ihre Zeitzone die pazifische Zeitzone ist, wird dieser Zeitwert in Braze als „12. März 2024, 17:00 Uhr" importiert.
{% endalert %}
{% endtab %}
{% endtabs %}

## Katalogdatentypen

Kataloge unterstützen verschiedene Datentypen, um Ihnen bei der effektiven Organisation und Strukturierung Ihrer Daten zu helfen. Die folgende Tabelle beschreibt jeden unterstützten Datentyp und seine Zuordnung zu CSV- und API-Typnamen:

| Datentyp | Format | Beispiel | Beschreibung |
|-----------|--------|---------|-------------|
| String | Text | `"Hello World"` | Jede Folge von Zeichen, die für Textdaten wie Namen, Beschreibungen und IDs verwendet wird. Entspricht dem `string`-Typ in CSV- und API-Importen. |
| Uhrzeit | ISO 8601 oder Unix-Zeitstempel (Sekunden) | `"2024-03-15T14:30:00Z"` | Datums- und Zeitwerte im Format ISO 8601 oder Unix-Zeitstempel in Sekunden. Entspricht dem `time`-Typ in der API und dem `datetime`-Typ in CSV-Importen. |
| Boolescher Wert | `true` oder `false` | `true` | Logische Werte, die wahre oder falsche Zustände darstellen. Entspricht dem `boolean`-Typ in CSV- und API-Importen. |
| Zahl | Ganzzahl oder Dezimalzahl | `42` oder `19.99` | Numerische Werte, einschließlich Ganzzahlen und Gleitkommazahlen für Preise, Mengen, Bewertungen und mehr. Entspricht den Typen `integer` und `float` in CSV-Importen und dem `number`-Typ in der API. |
| Objekt | JSON-Objekt | `{"key": "value", "price": 10}` | Komplexe verschachtelte Datenstrukturen. Der API-`type`-Wert ist `object`. Wird als JSON-Objekt im Dashboard angezeigt. Nur über API oder Cloud-Datenaufnahme (CDI) verfügbar. |
| Array | String-Array | `["red", "blue", "green"]` | Listen von String-Werten. Der API-`type`-Wert ist `array`. Wird im Dashboard als String-Array angezeigt. Nur über die API oder CDI verfügbar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Verwendung von Templates in Katalognamen {#template-catalog-names}

Bei der Benennung Ihres Katalogs können Sie auch Templates in einem Katalognamen verwenden. Auf diese Weise können Sie Katalognamen dynamisch auf der Grundlage von Variablen wie Sprache oder Kampagne generieren. Sie können zum Beispiel Folgendes verwenden:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Verwaltung von Katalogen

### Im Dashboard

Um Ihren Katalog nach dem Hochladen einer CSV-Datei oder dem Erstellen eines Katalogs im Browser zu aktualisieren, wählen Sie **Katalog aktualisieren** > **CSV hochladen** und legen Sie anschließend fest, ob Sie Artikel in Ihrem Katalog aktualisieren, hinzufügen oder löschen möchten.

### Verwendung der REST API

Wenn Sie mehr Kataloge erstellen, können Sie auch den [Endpunkt „Kataloge auflisten"]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) verwenden, um eine Liste der Kataloge in einem Workspace abzurufen.

Die REST API unterstützt alle [Katalogdatentypen](#supported-data-types), einschließlich JSON-Objekte und String-Arrays. JSON-Objekte und String-Arrays können ausschließlich über die REST API erstellt oder aktualisiert werden.

### Nutzung der Cloud-Datenaufnahme

Sie können Kataloge über die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) verwalten, indem Sie Katalogdaten direkt aus Ihrem Data Warehouse (wie Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric oder S3) nach einem festgelegten Zeitplan synchronisieren.

## Katalogartikel verwalten

Neben der Verwaltung Ihrer Kataloge können Sie auch asynchrone und synchrone Endpunkte zur Verwaltung der Katalogartikel verwenden. Dazu gehört die Möglichkeit, Katalogartikel zu bearbeiten und zu löschen sowie Details zu Katalogartikeln aufzulisten. 

Wenn Sie zum Beispiel einen einzelnen Katalogartikel bearbeiten möchten, können Sie den [`/catalogs/catalog_name/items/item_id`-Endpunkt]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/) verwenden.

## Katalogspeicher {#tiers}

Die kostenlose Version von Catalogs unterstützt CSV-Dateien mit einer Gesamtgröße von bis zu 100 MB für alle CSV-Dateien in Ihrem Unternehmen, während die Catalogs Pro-Version CSV-Dateien mit einer Größe von bis zu 2 GB für eine einzelne CSV-Datei unterstützt.

{% alert important %}
Der im Braze-Dashboard angezeigte Paketanspruch wird aus optischen Gründen auf die nächste Einheit gerundet; Sie haben jedoch weiterhin Anspruch auf den vollen erworbenen Umfang. Um ein Upgrade für den Katalogspeicher anzufordern, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}

#### Kostenlose Version

Die Speichergröße der kostenlosen Version von Catalogs beträgt bis zu 100&nbsp;MB. Sie können eine unbegrenzte Anzahl von Artikeln haben, solange sie unter 100&nbsp;MB bleiben. 

#### Catalogs Pro

Auf Unternehmensebene richtet sich der maximale Speicherplatz für Catalogs Pro nach der Größe der Katalogdaten. Die verfügbaren Speichergrößen sind: 5&nbsp;GB, 10&nbsp;GB oder 15&nbsp;GB. Beachten Sie, dass der Speicherplatz der kostenlosen Version (100&nbsp;MB) in jedem dieser Tarife enthalten ist.

## Spezifikationen

Die folgende Tabelle fasst die Spezifikationen zusammen, die für Kataloge gelten.

| Bereich | Spezifikationen |
|------|-----------|
| Zeichen pro Artikelwert | Bis zu 5.000 Zeichen in einem einzelnen Wert. Wenn Sie beispielsweise ein Feld mit der Bezeichnung `description` haben, beträgt die maximale Zeichenanzahl innerhalb des Feldes 5.000. |
| Zeichen pro Artikelspaltenname | Bis zu 250 Zeichen |
| Auswahlen pro Katalog | Bis zu 30 Auswahlen pro Katalog |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Katalog-Liquid-Tags können nicht rekursiv verwendet werden. Das bedeutet, dass Sie keinen Katalogartikel referenzieren können, der dann innerhalb derselben Liquid-Auswertung einen zweiten Katalogartikel aufruft.
{% endalert %}