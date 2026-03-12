---
nav_title: Lokalisierungen in Nachrichten
article_title: Lokalisierungen übersetzen
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Dieser Artikel enthält Anweisungen zur Verwendung von Locales in Ihren Nachrichten."
---

# Lokalisierungen übersetzen

> Nachdem Sie Ihrem Workspace Sprachversionen hinzugefügt haben, können Sie Zielgruppen in verschiedenen Sprachen mit einem einzigen Push, einer E-Mail, einem Banner, einer In-App-Nachricht oder einem Content-Block ansprechen.

{% multi_lang_include locales.md section="Prerequisites" %}

## Verwendung von Gebietsschemata

### Schritt 1: Bitte richten Sie die Locales in Ihrem Workspace ein. {#workspace-setup}

Bevor Sie Locales und Übersetzungstags verwenden können, müssen Sie zunächst [Locales zu Ihrem Workspace hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Schritt 2: Fügen Sie Ihrer Nachricht Liquid-Tags hinzu. {#add-translation-tags}

Fügen Sie die Übersetzungstags{% raw %}`{% translation your_id_here %}`  und  `{% endtranslation %}`{% endraw %}hinzu, um den gesamten Text, alle Bilder oder Link-URLs, die Sie übersetzen möchten, einzuschließen.

Jede Übersetzung sollte eine eindeutige Kennung aufweisen`id`. Wenn Sie beispielsweise eine einfache Begrüßung übersetzen, können Sie die ID „greeting” benennen:

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Lokalisierung von HTML-Blöcken

Ein komplexerer Absatz kann mehrere Übersetzungstags enthalten("offer_text". "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Das Einfügen großer HTML-Blöcke in Übersetzungstags kann zu Problemen mit Stylesheets oder der Formatierung führen. Bitte fassen Sie die Textabschnitte so kurz wie möglich.
{% endalert %}

#### Lokalisierung von Links

Um Anker-Tag-Links zu lokalisieren, stellen Sie bitte sicher, dass Sie **nur die sprachspezifischen Teile** umschließen und nicht das gesamte`href`URL-Attribut. Wenn Sie die gesamte URL einfügen, funktioniert das Template möglicherweise nicht korrekt.

##### Korrekte Verwendung

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### Falsche Verwendung

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### Schritt 3: Bitte wählen Sie die Spracheinstellungen für die Nachrichten aus. {#choose-locales}

Nachdem Sie die Übersetzungstags in die Nachricht eingefügt haben, gehen Sie zu den Mehrspracheinstellungen der Nachricht und wählen Sie eine oder mehrere Sprachversionen aus, in die diese Nachricht übersetzt werden soll.

![Mehrsprachige Einstellungen mit einem Dropdown-Feld zum Auswählen der Sprachumgebung.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Wählen Sie beim Bearbeiten Ihrer Nachricht im Menü „Inhalt“ **die Option „Mehrsprachig“** aus.

![Mehrsprachige Einstellungen für E-Mails.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Bitte wählen Sie beim Bearbeiten Ihrer Nachricht die Option **„Sprachen verwalten**”.

![Mehrsprachige Einstellungen für Push-Benachrichtigungen.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Bitte wählen Sie **„Sprachen verwalten“** unten im Abschnitt **„Build**“.

![Mehrsprachige Einstellungen für Drag-and-Drop-In-App-Nachrichten.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Bitte wählen Sie beim Bearbeiten Ihrer Nachricht die Option **„Sprachen verwalten**”.

![Mehrsprachige Einstellungen für HTML-Nachrichten innerhalb der App.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Bitte wählen Sie beim Bearbeiten Ihrer Nachricht die Option **„Sprachen verwalten**”.

![Mehrsprachige Einstellungen für Banner.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}

{% tab Content Block %}
Wählen Sie beim Bearbeiten Ihres Content-Blocks die Option **„Sprachen verwalten**”.

{% alert important %}
Content-Blöcke, für die Übersetzungen hochgeladen wurden, können nicht durch eine einzelne Kampagne oder eine Canvas-Nachricht überschrieben werden.
{% endalert %}

![Mehrsprachige Einstellungen für Content-Blöcke.]({% image_buster /assets/img/multi-language_support/content_block_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: CSV-Template herunterladen {#download-csv}

Nachdem Sie Ihre Sprachversionen ausgewählt haben, klicken Sie auf **„Template herunterladen“,** um ein CSV-Template herunterzuladen, das eine Matrix Ihrer ausgewählten Übersetzungs-IDs und Sprachversionen enthält.

![Beispiel-CSV für die Sprachumgebungen en, fr und es im Rahmen der Lokalisierung.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Schritt 5: Bitte laden Sie eine vollständig ausgefüllte CSV-Datei hoch. {#upload-csv}

{% alert important %}
Alle Änderungen an den IDs oder Lokalisierungen in der CSV-Datei werden nicht automatisch in Ihrer Nachricht aktualisiert. Um die Übersetzungen zu aktualisieren, aktualisieren Sie die CSV-Datei und laden Sie die Datei erneut hoch.
{% endalert %}

Nachfolgend finden Sie das Format für eine vollständig ausgefüllte CSV-Datei:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Schritt 6: Vorschau der Lokalisierungen {#preview-locales}

Wählen Sie bei der Vorschau Ihrer Nachricht die Option **„Mehrsprachiger Nutzer“** aus dem Dropdown-Menü **„Vorschau als Nutzer:in“** aus. Auf diese Weise können Sie zwischen verschiedenen Gebietsschema-Definitionen wechseln, um eine Vorschau aller Übersetzungen Ihrer Nachricht anzuzeigen.

![Lokale Vorschau]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Sehen Sie sich unsere [Translation API]({{site.baseurl}}/api/endpoints/translations) an, um Übersetzungen in Ihren Kampagnen und Canvase zu verwalten und zu aktualisieren.
{% endalert %}

## Nachrichten von rechts nach links

Beim Ausfüllen der Übersetzungsdatei für Sprachen, die von rechts nach links geschrieben werden (wie Arabisch), umschließen Sie die Übersetzung bitte mit`span`, damit sie korrekt formatiert wird:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Übersetzungen verwalten

### Bearbeitung von Übersetzungen für gestartete Kampagnen und Canvase

Nachdem eine Kampagne oder ein Canvas gestartet wurde, können Sie auch im Entwurfsmodus noch Übersetzungen ändern. Dies gilt unabhängig davon, ob Sie die Übersetzungen direkt im Composer, per CSV-Upload oder über die API bearbeiten. 

Weitere Einzelheiten zur Verwaltung von Kampagnen und Canvase nach dem Einführen finden Sie unter [Bearbeiten von gestarteten Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) und [Canvas-Entwürfen und Bearbeiten nach dem Einführen]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplizieren von Canvas-Schritten oder Kampagnen und Übersetzungen

Übersetzungen werden zusammen mit einem Canvas-Schritt, einer Kampagne oder einer Kampagnenvariante kopiert. Dies gilt auch für das Kopieren zwischen Workspaces, sofern die Gebietsschemata im Ziel-Workspace definiert sind. Achten Sie darauf, die Übersetzungen zu überprüfen und entsprechend zu aktualisieren, wenn Sie Änderungen an Ihrem Canvas oder Ihrer Kampagne vornehmen.

### Verwendung der Multi-Language-API mit Canvases

Um die [Multi-Language-API mit Canvases]({{site.baseurl}}/api/endpoints/translations/) zu verwenden, müssen Sie die Parameter `workflow_id`,`step_id` und`message_variation_id`in die Parameterliste aufnehmen.

#### Canvas-Schritte zu Entwürfen nach der Markteinführung hinzugefügt

Bei der Verwendung der Multi-Language-API mit Canvas-Schritten, die nach dem Start von Canvas erstellt wurden, ist der Parameter`message_variation_id`, den Sie an die API übergeben, leer oder unbeschrieben.

## Häufig gestellte Fragen

#### Kann ich eine Änderung an der übersetzten Kopie in einer meiner Lokalisationen vornehmen?
Ja Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung an der übersetzten Kopie vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln?
Nein.

#### Unterstützen Übersetzungen HTML für die Formatierung?
Ja, aber achten Sie darauf, dass das HTML-Styling nicht mit dem Inhalt übersetzt wird.

#### Ist es möglich, vollständige HTML-Nachrichten in einen Übersetzungstag einzubinden?
Nein, Ihre Übersetzungstags sollten so klein wie möglich sein, um Performance- oder Größenbeschränkungen zu vermeiden.

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
