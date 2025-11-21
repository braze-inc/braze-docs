---
nav_title: Einen Katalog erstellen
article_title: Einen Katalog erstellen
alias: "/catalogs/"
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie Kataloge erstellen, die über Liquid auf benutzerfremde Daten in Braze-Kampagnen verweisen."
---

# Einen Katalog erstellen

> Um einen Katalog zu erstellen, importieren Sie eine CSV-Datei mit benutzerfremden Daten in Braze. Anschließend können Sie auf diese Informationen zugreifen, um Ihre Nachrichten zu ergänzen. Sie können jede Art von Daten in einen Katalog einbringen. Bei diesen Daten handelt es sich in der Regel um eine Art von Metadaten Ihres Unternehmens, z. B. Produktinformationen für ein E-Commerce-Unternehmen oder Kursinformationen für einen Bildungsanbieter.

## Anwendungsfälle

Anwendungsfälle für Commons-Kataloge sind unter anderem:

- Produkte
- Dienste
- Lebensmittel
- Anstehende Ereignisse
- Musik
- Pakete

Nachdem diese Informationen importiert wurden, können Sie in Nachrichten darauf zugreifen, ähnlich wie auf angepasste Attribute oder Event-Eigenschaften über Liquid.

## Einen Katalog erstellen

Um einen Katalog zu erstellen, gehen Sie zu **Dateneinstellungen** > **Kataloge**, wählen Sie dann **Neuen Katalog erstellen** und wählen Sie eine der folgenden Optionen:

{% tabs local %}
{% tab Upload CSV %}
### Schritt 1: Überprüfen Sie Ihre CSV-Datei

Bevor Sie Ihre CSV-Datei hochladen, stellen Sie sicher, dass Ihre CSV-Datei die folgenden Anforderungen erfüllt:

| CSV-Anforderung | Details |
|-----------------|---------|
| Kopfzeilen | Die erste Spalte in der CSV-Datei muss `id` heißen, und jede Zeile muss einen eindeutigen `id` Wert haben. |
| Spalten | Eine CSV-Datei kann maximal 1.000 Felder (Spalten) enthalten, und jeder Spaltenname kann bis zu 250 Zeichen lang sein. |
| Dateigröße | Bei den kostenlosen Tarifen ist die Gesamtgröße aller CSV-Dateien in einem Unternehmen auf 100 MB begrenzt. Bei den Pro-Tarifen beträgt die maximale Dateigröße für eine einzelne CSV-Datei 2 GB. |
| Feldwerte | Jede Zelle (Feldwert) kann bis zu 5.000 Zeichen enthalten. |
| Gültige Zeichen | Die Spalte `id` und alle Kopfwerte dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| Daten-Typen | Zu den unterstützten Datentypen für das Hochladen einer CSV-Datei gehören String, Integer, Gleitkommazahl, Boolean oder Datetime. |
| Formatieren | Formatieren Sie den gesamten Text in Kleinbuchstaben, um die Konsistenz zu wahren. |
| Kodierung | Speichern und laden Sie die CSV-Datei in der Kodierung UTF-8 hoch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Benötigen Sie mehr Platz für Ihre CSV-Dateien? Wenden Sie sich an Ihren Account Manager bei Braze, um weitere Informationen über Katalog-Upgrades zu erhalten.
{% endalert %}

### Schritt 2: CSV hochladen

Ziehen Sie Ihre Datei per Drag-and-Drop in die Upload-Zone, oder wählen Sie **CSV hochladen** und wählen Sie Ihre Datei aus.

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Wählen Sie für jede Spalte einen Datentyp aus.

{% alert note %}
Dieser Datentyp kann nicht mehr bearbeitet werden, nachdem Sie Ihren Katalog eingerichtet haben. Auch ein `NULL`-Wert wird beim CSV-Upload nicht unterstützt und wird als String behandelt.
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Geben Sie einen Namen und eine optionale Beschreibung für Ihren Katalog ein. Beachten Sie die folgenden Anforderungen, wenn Sie Ihren Katalog benennen:

  - Muss einzigartig sein
  - Maximal 250 Zeichen
  - Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten

{% alert tip %}
Sie können auch [Templates in einem Katalognamen verwenden](#template-catalog-names), mit denen Sie dynamisch Katalognamen auf der Grundlage von Variablen wie Sprache oder Kampagne erzeugen können.
{% endalert %}

![Ein Katalog namens "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Wählen Sie **Prozesskatalog**, um den Katalog zu erstellen.

{% alert important %}
Ihre CSV-Datei kann abgelehnt werden, wenn Sie Ihre [Tarifstufe](#tiers) überschreiten.
{% endalert %}

### Anleitung: Erstellen eines Katalogs aus einer CSV-Datei

Die Anleitung basiert auf einem Katalog, der zwei Spiele mit Preisangaben und einem Bildlink enthält.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">Titel</th>
    <th class="tg-0pky">Preis</th>
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

Der Katalog wird erstellt, wenn man eine CSV-Datei hochlädt. Die Datentypen für `id`, `title`, `price` und `image_link` sind String, String, Zahl und String. 

{% alert note %}
Dieser Datentyp kann nicht mehr bearbeitet werden, nachdem Sie Ihren Katalog eingerichtet haben.
{% endalert %}

![Vier Katalogspaltennamen: "ID", "Titel", "Preis", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Als nächstes geben wir diesem Katalog den Namen "games_catalog" und wählen den Button **Katalog verarbeiten**. Dann prüft Braze den Katalog vor der Katalogerstellung auf eventuelle Fehler.

![Ein Katalog namens "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Beachten Sie, dass Sie diesen Namen nicht mehr ändern können, wenn der Katalog bereits erstellt worden ist. Sie können einen Katalog löschen und eine aktualisierte Version unter demselben Katalognamen erneut hochladen.

Wenn Sie den Katalog erstellt haben, können Sie ihn [in Kampagnen nennen]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Voraussetzungen

Bevor Sie Kataloge im Browser bearbeiten oder erstellen können, benötigen Sie die Berechtigung **Kataloge verwalten Dashboard**.

### Schritt 1: Katalogdetails eingeben

Geben Sie einen Namen und eine optionale Beschreibung für Ihren Katalog ein. Beachten Sie die folgenden Anforderungen, wenn Sie Ihren Katalog benennen:

- Muss einzigartig sein
- Maximal 250 Zeichen
- Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten

{% alert tip %}
Sie können auch [Templates in einem Katalognamen verwenden](#template-catalog-names), mit denen Sie dynamisch Katalognamen auf der Grundlage von Variablen wie Sprache oder Kampagne erzeugen können.
{% endalert %}

![Ein Katalog namens "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Schritt 2: Erstellen Sie Ihren Katalog

Wählen Sie Ihren Katalog aus der Liste aus und wählen Sie dann **Katalog aktualisieren** > **Felder hinzufügen**. Geben Sie den **Feldnamen** ein und wählen Sie über das Dropdown-Menü den Datentyp aus. Wiederholen Sie den Vorgang nach Bedarf.

![Zwei Beispielfelder "Bewertung" und "Name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Wählen Sie **Katalog aktualisieren** > **Artikel hinzufügen**, um einen Artikel zu Ihrem Katalog hinzuzufügen, indem Sie die Informationen auf der Grundlage der Felder eingeben, die Sie zuvor hinzugefügt haben. Wählen Sie dann **Artikel speichern** oder **Speichern und weiteren hinzufügen**, um mit dem Hinzufügen Ihrer Artikel fortzufahren.

![Fügen Sie einen Katalogartikel hinzu.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze verarbeitet Zeitwerte basierend auf dem Zeitstempel des Dashboards. Wenn eine Spalte z. B. den Wert "13.03.2024" aufweist und Sie die pazifische Zeitzone verwenden, wird in Braze "12\. März 2024, 17:00 Uhr" importiert.
{% endalert %}
{% endtab %}
{% endtabs %}

## Verwendung von Templates in Katalognamen {#template-catalog-names}

Wenn Sie Ihren Katalog benennen, können Sie auch Templates in einem Katalognamen verwenden. Damit können Sie dynamisch Katalognamen auf der Grundlage von Variablen wie Sprache oder Kampagne erzeugen. Sie können zum Beispiel Folgendes verwenden:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Kataloge verwalten

### Auf dem Dashboard

Um Ihren Katalog zu aktualisieren, nachdem Sie eine CSV-Datei hochgeladen oder einen Katalog im Browser erstellt haben, wählen Sie **Katalog aktualisieren > CSV hochladen** und wählen dann aus, ob Sie Artikel in Ihrem Katalog aktualisieren, hinzufügen oder löschen möchten.

### Verwendung der REST API

Wenn Sie mehr Kataloge erstellen, können Sie auch den [Endpunkt Kataloge auflisten]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) verwenden, um eine Liste der Kataloge in einem Arbeitsbereich anzuzeigen.

Unterstützte Datentypen für die Verwendung der API sind: String, Ganzzahl, Gleitkommazahl, Boolescher Wert oder Datetime. Sie können auch Arrays und Objekte hochladen, wenn Sie Ihre Kataloge mit der API verwalten.

## Katalogartikel konfigurieren

Neben der Verwaltung Ihrer Kataloge können Sie auch asynchrone und synchrone Endpunkte zur Verwaltung der Katalogartikel verwenden. So können Sie Katalogartikel bearbeiten, löschen und nähere Details zu ihnen auflisten. 

Wenn Sie zum Beispiel einen einzelnen Katalogartikel bearbeiten möchten, können Sie dazu den [Endpunkt`/catalogs/catalog_name/items/item_id` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/) verwenden.

## Katalogspeicher {#tiers}

Die kostenlose Version von Catalogs unterstützt CSV-Dateien mit einer Größe von bis zu 100 MB für alle CSV-Dateien in Ihrem Unternehmen, während die Pro-Version von Catalogs CSV-Dateien mit einer Größe von bis zu 2 GB für eine einzelne CSV-Datei unterstützt.

{% alert important %}
Der im Braze Dashboard angezeigte Paketanspruch wird aus optischen Gründen auf die nächste Einheit gerundet; Sie haben jedoch weiterhin Anspruch auf den vollen erworbenen Anspruch. Um ein Upgrade für Katalogspeicher anzufordern, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}

#### Kostenlose Version

Die Speichergröße kostenloser Katalogversionen beträgt max. 100 MB. Sie können eine unbegrenzte Anzahl von Artikeln haben, solange sie weniger als 100 MB groß sind. 

#### Catalogs Pro

Auf Unternehmensebene richtet sich der maximale Speicherplatz für Catalogs Pro nach der Größe der Katalogdaten. Mögliche Speichergrößen sind: 5 GB, 10 GB, oder 15 GB. Beachten Sie, dass der Speicherplatz der kostenlosen Version (100 MB) in jedem dieser Tarife enthalten ist.
