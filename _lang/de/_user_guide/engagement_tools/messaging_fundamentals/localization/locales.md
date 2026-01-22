---
nav_title: Lokalisierungen in Nachrichten
article_title: Lokalisierungen in Nachrichten
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie in Ihren Nachrichten Gebietsschemata verwenden können."
---

# Lokalisierungen in Nachrichten

> Nachdem Sie Ihrem Workspace Gebietsschemata hinzugefügt haben, können Sie Nutzer:innen mit einer einzigen Push-, E-Mail- oder In-App-Nachricht in verschiedenen Sprachen zusammenstellen.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
Die Unterstützung mehrerer Sprachen und Lokalisierungen in Nachrichten sind derzeit in der frühen Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Verwendung von Gebietsschemata

{% tabs %}
{% tab In-app message %}

Um Lokalisierungen in Ihren Messaging-Nachrichten zu verwenden, erstellen Sie eine In-App-Nachricht-Kampagne oder ein Canvas. Wählen Sie entweder den Drag-and-Drop-Editor oder den traditionellen Editor aus und folgen Sie dann den Schritten, die für Ihren Editor gelten.

{% subtabs %}
{% subtab traditional editor %}

1. Fügen Sie die Übersetzungs-Tags {% raw %}`{% translation %}` und `{% endtranslation %}`{% endraw %} hinzu, um alle zu übersetzenden Texte, Bilder und Links einzufassen. 
2. Fügen Sie zu jedem Übersetzungs-Tag ein ID-Tag hinzu. Ein Beispiel ist: {% raw %}`{% translation id_1 %}`{% endraw %}

![Traditioneller Editor mit Übersetzungs-IDs.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Wenn Sie die Tags hinzugefügt haben, speichern Sie Ihre Nachricht als Entwurf.
4\. Wählen Sie **Sprachen verwalten** und fügen Sie über das Dropdown-Menü Ihre Lokalisierungen für die Nachricht hinzu.

!["Sprachen verwalten"-Modal mit einer ausgewählten Lokalisierung.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Gehen Sie auf **Template herunterladen**, um die Übersetzungsvorlage als CSV-Datei herunterzuladen. Tragen Sie dann die Übersetzungen in die CSV-Datei ein.

![Ein Beispiel für eine CSV-Datei zur Übersetzung.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Wählen Sie **Übersetzungen hochladen**, um die CSV-Datei mit den fertigen Übersetzungen hochzuladen.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Fügen Sie die Übersetzungs-Tags {% raw %}`{% translation %}` und `{% endtranslation %}`{% endraw %} hinzu, um alle zu übersetzenden Texte, Bilder und Links einzufassen. 
2. Fügen Sie zu jedem Übersetzungs-Tag ein ID-Tag hinzu. Ein Beispiel ist: {% raw %}`{% translation id_1 %}`{% endraw %} 

![Drag-and-Drop-Editor mit zwei Übersetzungs-IDs.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Nachdem Sie die Tags hinzugefügt haben, speichern Sie Ihre Nachricht als Entwurf, und öffnen Sie den Editor erneut.
4\. Wählen Sie im Panel **Aufbauen** die Option **Mehrsprachig** aus und fügen Sie über das Dropdown-Menü Ihre Lokalisierungen für die Nachricht hinzu.
5\. Gehen Sie auf **Template herunterladen**, um die Übersetzungsvorlage als CSV-Datei herunterzuladen. 

!["Mehrsprachiges" Panel mit Button zum Herunterladen des Templates.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Füllen Sie die Übersetzungen in der CSV-Datei aus. Wenn Sie die Übersetzungstags direkt aus Schritt 1 kopiert und eingefügt haben, müssen Sie eventuell `<code>` aus der Spalte **Übersetzungstags** der CSV-Datei entfernen.
7\. Wählen Sie **Übersetzungen hochladen**, um die CSV-Datei mit den fertigen Übersetzungen hochzuladen.

!["Mehrsprachiges" Panel mit Buttons zum Herunterladen des Templates und Hochladen von Übersetzungen.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Email %}

Um Gebietsschemata in Ihren Nachrichten zu verwenden, erstellen Sie eine E-Mail-Kampagne oder ein Canvas. Wählen Sie entweder den HTML-Editor oder den Drag-and-Drop-Editor und folgen Sie dann den Schritten, die für Ihren Editor gelten.

{% subtabs %}
{% subtab HTML editor %}

1. Markieren Sie den Text, den Sie übersetzen möchten. Wählen Sie **Übersetzungs-Tag einfügen**. Nun wird Ihr Text mit Übersetzungs-Tags eingefasst. <br>![HTML-Editor mit einer ausgewählten Lokalisierung.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Speichern Sie die Nachricht als Entwurf.
3. Wählen Sie **Mehrsprachig** und fügen Sie über das Dropdown-Menü Ihre Gebietsschemata für die Nachricht hinzu.
4. Gehen Sie auf **Template herunterladen**, um die Übersetzungsvorlage als CSV-Datei herunterzuladen. Tragen Sie dann die Übersetzungen in die CSV-Datei ein. <br>![Ein Beispiel für eine CSV-Datei zur Übersetzung.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Wählen Sie **Übersetzungen hochladen**, um die CSV-Datei mit den fertigen Übersetzungen hochzuladen.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Fügen Sie die Übersetzungs-Tags {% raw %}`{% translation %}` und `{% endtranslation %}`{% endraw %} hinzu, um alle zu übersetzenden Texte, Bilder und Links einzufassen. 
2. Fügen Sie zu jedem Übersetzungs-Tag ein ID-Tag hinzu. Ein Beispiel ist: {% raw %}`{% translation id_1 %}`{% endraw %} <br>![Drag-and-Drop-Editor mit zwei Übersetzungs-IDs.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Wenn Sie die Tags hinzugefügt haben, speichern Sie Ihre Nachricht als Entwurf.
4. Wählen Sie **Mehrsprachig** und fügen Sie über das Dropdown-Menü Ihre Gebietsschemata für die Nachricht hinzu.
5. Gehen Sie auf **Template herunterladen**, um die Übersetzungsvorlage als CSV-Datei herunterzuladen. 
6. Füllen Sie die Übersetzungen in der CSV-Datei aus. Wenn Sie die Übersetzungstags direkt aus Schritt 1 kopiert und eingefügt haben, müssen Sie eventuell `<code>` aus der Spalte **Übersetzungstags** der CSV-Datei entfernen.
7. Wählen Sie **Übersetzungen hochladen**, um die CSV-Datei mit den fertigen Übersetzungen hochzuladen.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Push %}

Um Lokalisierungen in Ihren Messaging-Nachrichten zu verwenden, erstellen Sie eine Push-Kampagne oder ein Canvas und führen dann die folgenden Schritte aus:

1. Fügen Sie die Übersetzungstags {% raw %}`{% translation id1%}` und `{% endtranslation %}`{% endraw %} hinzu, um alle zu übersetzenden Text-, Bild- oder Link-URLs einzuschließen. Jede Übersetzungs-ID (`id1`) muss eindeutig sein.

![Push-Benachrichtigung-Editor mit Übersetzungs-Tags in den Feldern für Titel und Nachrichten.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Speichern Sie Ihre Nachricht als Entwurf.
3\. Wählen Sie **Sprache verwalten** und fügen Sie über das Dropdown-Menü Ihre Lokalisierungen für die Nachricht hinzu.
4\. Wählen Sie **Template herunterladen** aus und geben Sie die Übersetzungen in das CSV Template ein.

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Um die fertige CSV-Vorlage hochzuladen, wählen Sie **Übersetzungen hochladen**. 

![Das Fenster "Mehrsprachige Nachrichten" mit zwei ausgewählten Lokalisierungen und Buttons zum Herunterladen eines Templates oder Hochladen von Übersetzungen.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

{% endtab %}
{% endtabs %}

Alle Änderungen an den IDs oder Lokalisierungen in der CSV-Datei werden nicht automatisch in Ihrer Nachricht aktualisiert. Um die Übersetzungen zu aktualisieren, aktualisieren Sie die CSV-Datei und laden Sie die Datei erneut hoch.

{% alert tip %}
Sehen Sie sich unsere [Translation API]({{site.baseurl}}/api/endpoints/translations) an, um Übersetzungen in Ihren Kampagnen und Canvase zu verwalten und zu aktualisieren.
{% endalert %}

## Vorschau auf Gebietsschemata

{% tabs %}
{% tab In-app message %}

Wählen Sie im Dropdown-Menü **Vorschau der Nachricht als Nutzer:** in auf dem Tab **Test** die Option **Benutzer:innen** aus und geben Sie verschiedene Sprachen ein, um eine Vorschau der Nachricht anzuzeigen und zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.


{% endtab %}
{% tab Email %}

Wählen Sie im Bereich **Vorschau & Test** **mehrsprachige Nutzer:innen** aus, um zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.

{% endtab %}
{% tab Push %}

Wählen Sie im Dropdown-Menü **Vorschau der Nachricht als Nutzer:** in auf dem Tab **Test** die Option **Benutzer:innen** aus und geben Sie verschiedene Sprachen ein, um eine Vorschau der Nachricht anzuzeigen und zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.

{% endtab %}
{% endtabs %}

## Übersetzungen verwalten

### Bearbeitung von Übersetzungen für gestartete Kampagnen und Canvase

Nachdem eine Kampagne oder ein Canvas gestartet wurde, können Sie auch im Entwurfsmodus noch Übersetzungen ändern. Dies gilt unabhängig davon, ob Sie die Übersetzungen direkt im Composer, per CSV-Upload oder über die API bearbeiten. 

Bevor Sie ein Update der Übersetzung vornehmen, müssen Sie die Kampagne oder das Canvas zunächst als Entwurf speichern.

1. Wählen Sie **Kampagne/Canvas bearbeiten** und nehmen Sie dann Ihre Änderungen im Composer vor.
2. Wählen Sie **Als Entwurf speichern** und wählen Sie dann im Modal **Ja**.
3. Gehen Sie zum Schritt **Review Summary** und wählen Sie **Update campaign/Canvas**.
4. Wählen Sie im Modal **Kampagne/Canvas aktualisieren** aus.

Weitere Einzelheiten zur Verwaltung von Kampagnen und Canvase nach dem Einführen finden Sie unter [Bearbeiten von gestarteten Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) und [Canvas-Entwürfen und Bearbeiten nach dem Einführen]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplizieren von Canvas-Schritten oder Kampagnen und Übersetzungen

Wenn Sie einen Canvas-Schritt oder eine Kampagne duplizieren, egal ob im Entwurfsmodus nach dem Start oder während der ursprünglichen Erstellung, werden die mit diesem Schritt verbundenen Übersetzungen nicht übernommen. Alle notwendigen Übersetzungen müssen dem neuen Schritt oder der Kampagne hinzugefügt werden. Achten Sie darauf, die Übersetzungen zu überprüfen und entsprechend zu aktualisieren, wenn Sie Änderungen an Ihrem Canvas oder Ihrer Kampagne vornehmen.

### Verwendung der mehrsprachigen API mit Canvase

Um die [mehrsprachige API mit Canvase]({{site.baseurl}}/api/endpoints/translations/) zu verwenden, müssen Sie die Parameter `workflow_id`, `step_id` und `message_variation_id` in die Parameterliste aufnehmen.

#### Canvas-Schritte zu Entwürfen nach der Markteinführung hinzugefügt

Wenn Sie die mehrsprachige API mit Canvas-Schritten verwenden, die nach dem Start des Canvas erstellt wurden, ist die `message_variation_id`, die Sie an die API übergeben, leer oder leer.

## Häufig gestellte Fragen

#### Kann ich eine Änderung an der übersetzten Kopie in einer meiner Lokalisationen vornehmen?
Ja Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung an der übersetzten Kopie vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln?
Nein.

#### Können Übersetzungs-Tags mit HTML-Designs versehen werden?
Ja, aber achten Sie darauf, dass das HTML-Styling nicht mit dem Inhalt übersetzt wird.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?

| Szenario                                                                                                                                                 | Validierung in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| In einer Übersetzungsdatei fehlen die mit der jeweiligen Nachricht verbundenen Gebietsschemata.                                                                               | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| In einer Übersetzungsdatei fehlen Textblöcke etwa aus Liquid-Übersetzungs-Tags aus der jeweiligen E-Mail.                                | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| Die Übersetzungsdatei enthält den Standardtext, der nicht mit den Textblöcken der jeweiligen E-Mail übereinstimmt.                                          | Diese Übersetzungsdatei wird nicht hochgeladen. Korrigieren Sie den Fehler in der CSV-Datei, bevor Sie den Upload erneut versuchen.               |
| Die Übersetzungsdatei enthält Gebietsschemata, die in den **Mehrsprachigkeitseinstellungen** nicht vorkommen.                                                           | Diese Gebietsschemata werden nicht in Braze gespeichert.                                                                      |
| Die Übersetzungsdatei enthält Textblöcke, die in der aktuellen Nachricht nicht vorkommen (wie den Entwurfsstand beim Upload der Übersetzungen). | Textblöcke, die in der Nachricht fehlen, werden nicht aus der Übersetzungsdatei übernommen und in Braze gespeichert. |
| Ein Gebietsschema wird aus einer Nachricht entfernt, nachdem es als Teil der Übersetzungsdatei in die Nachricht übernommen worden ist.                           | Wenn Sie das Gebietsschema entfernen, werden alle damit verbundenen Übersetzungen in der Nachricht entfernt.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }