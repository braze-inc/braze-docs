---
nav_title: Einen Katalog erstellen
article_title: Einen Katalog erstellen
alias: "/catalogs/"
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie Kataloge erstellen, die über Liquid auf benutzerfremde Daten in Braze-Kampagnen verweisen."
---

# Einen Katalog erstellen

> Um einen Katalog zu erstellen, importieren Sie eine CSV-Datei mit benutzerfremden Daten in Braze. Anschließend können Sie auf diese Informationen zugreifen, um Ihre Nachrichten zu ergänzen. Sie können jede Art von Daten in einen Katalog einbringen. Bei diesen Daten handelt es sich in der Regel um eine Art von Metadaten Ihres Unternehmens, z. B. Produktinformationen für ein E-Commerce-Unternehmen oder Kursinformationen für einen Bildungsanbieter.<br><br>Auf dieser Seite erfahren Sie, wie Sie eine CSV-Datei vorbereiten und hochladen, um einen Katalog zu erstellen, wie Sie Kataloge verwalten und vieles mehr.

Anwendungsfälle für Commons-Kataloge sind unter anderem:

- Produkte
- Dienste
- Lebensmittel
- Anstehende Ereignisse
- Musik
- Pakete

Nachdem diese Informationen importiert wurden, können Sie in Nachrichten darauf zugreifen, ähnlich wie auf angepasste Attribute oder Event-Eigenschaften über Liquid.

## Vorbereiten Ihrer CSV-Datei

Bevor Sie einen Katalog erstellen, sollten Sie Ihre CSV-Datei bereithalten, wenn Sie den Katalog per Upload erstellen möchten.

{% alert note %}
Benötigen Sie mehr Platz für Ihre CSV-Dateien? Wenden Sie sich an Ihren Account Manager bei Braze, um weitere Informationen über Katalog-Upgrades zu erhalten.
{% endalert %}

### Richtlinien für CSV-Dateien

Beachten Sie diese Richtlinien bei der Erstellung Ihrer CSV-Datei. Die erste Spalte der CSV-Datei muss die Kopfzeile `id` sein, und alle Artikel-`id`s muss eindeutig sein. Alle anderen Spaltennamen müssen eindeutig sein. Außerdem gelten die folgenden Einschränkungen für Katalog-CSV-Dateien:

- Maximal 1.000 Felder (Spalten)
- Maximale Feld- (Spalten-) Bezeichnung von 250 Zeichen
- Maximal 100 MB für alle CSV-Dateien Ihres Unternehmens (kostenlos)
- Maximale CSV-Dateigröße von 2 GB (Pro)
- Maximaler Feldwert (Zelle) von 5.000 Zeichen
- Nur Buchstaben, Zahlen, Bindestriche und Unterstriche für `id` und Kopfwerte

Wir empfehlen außerdem, den gesamten Text Ihrer CSV-Dateien in Kleinbuchstaben zu schreiben. Vergewissern Sie sich, dass Sie Ihre CSV-Datei im UTF-8-Format kodieren, damit Sie sie im nächsten Schritt hochladen können.

## Methode festlegen

Um einen Katalog zu erstellen, gehen Sie zu **Dateneinstellungen** > **Kataloge**.

Wählen Sie **Neuen Katalog erstellen** und wählen Sie dann entweder **CSV hochladen** oder **Im Browser erstellen**.

### Methode 1: CSV hochladen

1. Ziehen Sie Ihre Datei per Drag-and-Drop in die Upload-Zone, oder wählen Sie **CSV hochladen** und wählen Sie Ihre Datei aus. <br>![][1]{: style="max-width:80%;"} <br><br>
2. Wählen Sie für jede Spalte einen der folgenden Datentypen: Boolescher Wert, Zahl, String oder Zeit.
<br> ![][9]{: style="max-width:80%;"} <br><br>
3. Geben Sie Ihrem Katalog einen Namen. Beachten Sie die folgenden Anforderungen an einen Katalognamen:
- Muss einzigartig sein
- Maximal 250 Zeichen
- Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten<br><br>
4. (optional) Fügen Sie eine Beschreibung für den Katalog hinzu.
5. Wählen Sie **Prozesskatalog**, um den Katalog zu erstellen.

{% alert note %}
Dieser Datentyp kann nicht mehr bearbeitet werden, nachdem Sie Ihren Katalog eingerichtet haben. Auch ein `NULL`-Wert wird beim CSV-Upload nicht unterstützt und wird als String behandelt.
{% endalert %}

Sie können auch Vorlagen in einem Katalognamen verwenden. Sie können zum Beispiel Folgendes verwenden:
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
Ihre CSV-Datei kann abgelehnt werden, wenn Sie Ihre [Tarifstufe](#tiers) überschreiten.
{% endalert %}

Sie können die CSV-Datei auch aktualisieren, wenn Sie einen Katalog im Browser erstellen. Wählen Sie **Katalog aktualisieren > CSV hochladen** und wählen Sie dann aus, ob Sie Artikel in Ihrem Katalog aktualisieren, hinzufügen oder löschen möchten.

### Methode 2: Im Browser erstellen

Um Kataloge im Browser zu bearbeiten oder zu erstellen, benötigen Sie die Berechtigung "Kataloge verwalten Dashboard".

1. Geben Sie einen Namen für Ihren Katalog ein. Beachten Sie die folgenden Anforderungen für Ihren Katalognamen:
- Muss einzigartig sein
- Bis zu 250 Zeichen
- Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten <br> ![Ein Katalog mit dem Namen "my_catalog".][14]{: style="max-width:80%;"} <br><br>
2. (optional) Geben Sie eine Beschreibung für Ihren Katalog ein.
3. Wählen Sie den Katalog, den Sie gerade erstellt haben, auf der Seite **Kataloge** auflisten aus, um Ihren Katalog zu aktualisieren.
4. Wählen Sie **Katalog aktualisieren** > **Felder hinzufügen**, um Ihre Felder hinzuzufügen. Geben Sie dann den **Feldnamen** ein und verwenden Sie das Dropdown-Menü, um den Datentyp auszuwählen. Wiederholen Sie den Vorgang nach Bedarf.<br> ![Zwei Beispielfelder "Bewertung" und "Name".][12]{: style="max-width:50%;"}<br><br>
5. Wählen Sie **Katalog aktualisieren** > **Artikel hinzufügen**, um einen Artikel zu Ihrem Katalog hinzuzufügen, indem Sie die Informationen auf der Grundlage der Felder eingeben, die Sie zuvor hinzugefügt haben. Wählen Sie dann **Artikel speichern** oder **Speichern und weiteren hinzufügen**, um mit dem Hinzufügen Ihrer Artikel fortzufahren. <br> ![Fügen Sie einen Artikel hinzu.][13]{: style="max-width:50%;"}

Sie können auch eine CSV-Datei hochladen, wenn Sie einen Katalog im Browser erstellen.

{% alert note %}
Braze verarbeitet Zeitwerte basierend auf dem Zeitstempel des Dashboards. Wenn eine Spalte z. B. den Wert "13.03.2024" aufweist und Sie die pazifische Zeitzone verwenden, wird in Braze "12\. März 2024, 17:00 Uhr" importiert.
{% endalert %}

#### Anleitung: Erstellen eines Katalogs aus einer CSV-Datei

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

![Vier Katalogspaltennamen: "id", "title", "price", "image_link".][9]{: style="max-width:85%;"}

Als nächstes geben wir diesem Katalog den Namen "games_catalog" und wählen den Button **Katalog verarbeiten**. Dann prüft Braze den Katalog vor der Katalogerstellung auf eventuelle Fehler.

![Ein Katalog namens "games_catalog".][11]{: style="max-width:85%;"}

Beachten Sie, dass Sie diesen Namen nicht mehr ändern können, wenn der Katalog bereits erstellt worden ist. Sie können einen Katalog löschen und eine aktualisierte Version unter demselben Katalognamen erneut hochladen.

Wenn Sie den Katalog erstellt haben, können Sie ihn [in Kampagnen nennen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/).

## Kataloge über API verwalten

Wenn Sie mehr Kataloge erstellen, können Sie auch den [Endpunkt Kataloge auflisten]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) verwenden, um eine Liste der Kataloge in einem Arbeitsbereich anzuzeigen.

### Katalogartikel konfigurieren

Neben der Verwaltung Ihrer Kataloge können Sie auch asynchrone und synchrone Endpunkte zur Verwaltung der Katalogartikel verwenden. So können Sie Katalogartikel bearbeiten, löschen und nähere Details zu ihnen auflisten. 

Wenn Sie zum Beispiel einen einzelnen Katalogartikel bearbeiten möchten, können Sie dazu den [Endpunkt`/catalogs/catalog_name/items/item_id` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/) verwenden.

## Katalogebenen {#tiers}

Die kostenlose Version von Catalogs unterstützt CSV-Dateien mit einer Größe von bis zu 100 MB für alle CSV-Dateien in Ihrem Unternehmen, während die Pro-Version von Catalogs CSV-Dateien mit einer Größe von bis zu 2 GB für eine einzelne CSV-Datei unterstützt.

### Katalogspeicher

{% alert important %}
Der im Braze Dashboard angezeigte Paketanspruch wird aus optischen Gründen auf die nächste Einheit gerundet; Sie haben jedoch weiterhin Anspruch auf den vollen erworbenen Anspruch. Um ein Upgrade für Katalogspeicher anzufordern, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}

#### Kostenlose Version

Die Speichergröße kostenloser Katalogversionen beträgt max. 100 MB. Sie können beliebig viele Artikel enthalten, solange die Größe unter 100 MB liegt. Auswahlen werden bei der Speichergröße berücksichtigt. Je komplexer sie sind, desto mehr Speicherplatz belegen sie. Außerdem gibt es eine Größenabweichung zwischen den CSV-Katalogdaten und der Darstellung dieser Daten in unserem Datenspeicher.

#### Catalogs Pro

Auf Unternehmensebene richtet sich der maximale Speicherplatz für Catalogs Pro nach der Größe der Katalogdaten. Mögliche Speichergrößen sind: 5 GB, 10 GB, oder 15 GB. Beachten Sie, dass der Speicherplatz der kostenlosen Version (100 MB) in jedem dieser Tarife enthalten ist.

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[7]: {% image_buster /assets/img_archive/create_catalog_option.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[12]: {% image_buster /assets/img_archive/add_catalog_fields.png %}
[13]: {% image_buster /assets/img_archive/add_catalog_items.png %}
[14]: {% image_buster /assets/img_archive/in_browser_catalog.png %}
