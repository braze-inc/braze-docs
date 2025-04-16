---
nav_title: Lokale in Nachrichten
article_title: Lokale in Nachrichten
page_order: 6.3
description: "In diesem Artikel erfahren Sie, wie Sie Gebietsschemata in Ihren Nachrichten verwenden können."
---

# Gebietsschemata für die Nachrichtenübermittlung

> Wenn Sie Ihrem Arbeitsbereich Gebietsschemata hinzugefügt haben, können Sie Benutzer mit E-Mails in verschiedenen Sprachen ansprechen.

## Voraussetzungen

Um die [Mehrsprachenunterstützung]({{site.baseurl}}/multi_language_support/) konfigurieren zu können, benötigen Sie die Benutzerberechtigung "Mehrsprachigkeitseinstellungen konfigurieren". Um das Gebietsschema einer Nachricht einzustellen, benötigen Sie eine Berechtigung zur Bearbeitung von Kampagnen.

## Verwendung von Gebietsschemata

Um Gebietsschemata in Ihren Nachrichten zu verwenden, erstellen Sie eine E-Mail-Kampagne oder ein Canvas. Wählen Sie entweder den HTML-Editor oder den Drag-and-Drop-Editor und folgen Sie dann den Schritten, die für Ihren Editor gelten.

{% tabs %}
{% tab HTML-Editor %}

1. Markieren Sie den Text, den Sie übersetzen möchten. Wählen Sie **Übersetzungs-Tag einfügen**. Nun wird Ihr Text mit Übersetzungs-Tags eingefasst. <br>![HTML-Editor mit einem ausgewählten Gebietsschema.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Speichern Sie die Nachricht als Entwurf.
3. Wählen Sie **Mehrsprachig** und fügen Sie über das Dropdown-Menü Ihre Gebietsschemata für die Nachricht hinzu.
4. Gehen Sie auf **Template herunterladen**, um die Übersetzungsvorlage als CSV-Datei herunterzuladen. Tragen Sie dann die Übersetzungen in die CSV-Datei ein. <br>![Beispiel für eine übersetzte CSV-Datei.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Wählen Sie **Übersetzungen hochladen**, um die CSV-Datei mit den fertigen Übersetzungen hochzuladen.

{% endtab %}
{% tab Drag-and-Drop-Editor %}

1. Fügen Sie die Übersetzungs-Tags {% raw %}`{% translation %}` und `{% endtranslation %}`{% endraw %} hinzu, um alle zu übersetzenden Texte, Bilder und Links einzufassen. 
2. Fügen Sie zu jedem Übersetzungs-Tag ein ID-Tag hinzu. Ein Beispiel ist: {% raw %}`{% translation id_1 %}`{% endraw %} <br>![Drag-and-Drop-Editor mit zwei Übersetzungs-IDs.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Wenn Sie die Tags hinzugefügt haben, speichern Sie Ihre Nachricht als Entwurf.
4. Wählen Sie **Mehrsprachig** und fügen Sie über das Dropdown-Menü Ihre Gebietsschemata für die Nachricht hinzu.
5. Gehen Sie auf **Template herunterladen**, um die Übersetzungsvorlage als CSV-Datei herunterzuladen. 
6. Füllen Sie die Übersetzungen in der CSV-Datei aus. Wenn Sie die Übersetzungstags direkt aus Schritt 1 kopiert und eingefügt haben, müssen Sie eventuell `<code>` aus der Spalte **Übersetzungstags** der CSV-Datei entfernen.
7. Wählen Sie **Übersetzungen hochladen**, um die CSV-Datei mit den fertigen Übersetzungen hochzuladen.

{% endtab %}
{% endtabs %}

Alle Änderungen an den IDs oder Lokalisierungen in der CSV-Datei werden nicht automatisch in Ihrer Nachricht aktualisiert. Um die Übersetzungen zu aktualisieren, aktualisieren Sie die CSV-Datei und laden Sie die Datei erneut hoch.

## Vorschau auf Gebietsschemata

Wählen Sie im Bereich **Vorschau & Test** die Option **Nutzer:innen in mehreren Sprachen** aus, um zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.

## 

### 

  



1. 
2. 
3. 
4. 



### 

  

### 



#### 



## Häufig gestellte Fragen

#### Ich möchte eine Änderung an der übersetzten Kopie in einer meiner Sprachversionen vornehmen. Wie kann ich das tun?
Bearbeiten Sie die CSV-Datei und laden Sie die Datei dann erneut hoch, um eine Änderung an der übersetzten Version vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln?
Nein.

#### Kann ich Gebietsschemata in meinen E-Mail Templates verwenden?
Nein, Gebietsschemata werden nur im E-Mail-Editor für Kampagnen und bei Nachrichtenschritten in Canvas unterstützt.

#### Können Übersetzungs-Tags mit HTML-Designs versehen werden?
Ja Achten Sie jedoch darauf, dass das HTML-Design nicht mitübersetzt wird.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze bei Übersetzungen durch?

| Szenario                                                                                                                                                 | Validierung in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| In einer Übersetzungsdatei fehlen die mit der jeweiligen Nachricht verbundenen Gebietsschemata.                                                                               | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| In einer Übersetzungsdatei fehlen Textblöcke etwa aus Liquid-Übersetzungs-Tags aus der jeweiligen E-Mail.                                | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| Die Übersetzungsdatei enthält den Standardtext, der nicht mit den Textblöcken der jeweiligen E-Mail übereinstimmt.                                          | Diese Übersetzungsdatei wird nicht hochgeladen. Korrigieren Sie den Fehler in der CSV-Datei, bevor Sie den Upload erneut versuchen.               |
| Die Übersetzungsdatei enthält Gebietsschemata, die in den **Mehrsprachigkeitseinstellungen** nicht vorkommen.                                                           | Diese Gebietsschemata werden nicht in Braze gespeichert.                                                                      |
| Die Übersetzungsdatei enthält Textblöcke, die in der aktuellen Nachricht nicht vorkommen (wie den Entwurfsstand beim Upload der Übersetzungen). | Textblöcke, die in der Nachricht fehlen, werden nicht aus der Übersetzungsdatei übernommen und in Braze gespeichert. |
| Ein Gebietsschema wird aus einer Nachricht entfernt, nachdem es als Teil der Übersetzungsdatei in die Nachricht übernommen worden ist.                           | Wenn Sie das Gebietsschema entfernen, werden alle damit verbundenen Übersetzungen in der Nachricht entfernt.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

