---
nav_title: Lokalisierungen in Nachrichten
article_title: Lokalisierung übersetzen
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie in Ihren Nachrichten Gebietsschemata verwenden können."
---

# Lokalisierung übersetzen

> Nachdem Sie Ihrem Workspace Lokalisierungen hinzugefügt haben, können Sie Nutzer:innen in verschiedenen Sprachen mit einer einzigen Push-, E-Mail-, Banner- oder In-App-Nachricht zusammenstellen.

{% multi_lang_include locales.md section="Prerequisites" %}

## Verwendung von Gebietsschemata

### Schritt 1: Lokalisierung in Ihrem Workspace einrichten {#workspace-setup}

Bevor Sie Lokalisierungen und Tags für die Übersetzung verwenden können, müssen Sie [Ihrem Workspace]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings) zunächst [Lokalisierungen hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Schritt 2: Fügen Sie Ihrer Nachricht Liquid-Tags für die Übersetzung hinzu {#add-translation-tags}

Fügen Sie die Übersetzungstags {% raw %}`{% translation your_id_here %}` und `{% endtranslation %}`{% endraw %} hinzu, um alle Text-, Bild- oder Link-URLs, die Sie übersetzen werden, zu umschließen.

Jede Übersetzung sollte eine eindeutige `id` haben. Wenn Sie zum Beispiel eine einfache Begrüßung übersetzen, können Sie die ID "Begrüßung" nennen:

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Lokalisierung von HTML-Blöcken

Ein komplizierterer Absatz kann mehrere Übersetzungstags haben ("offer_text" und "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Wenn Sie große HTML-Blöcke in Übersetzungstags einpacken, kann dies zu Problemen mit Stylesheets oder Styling führen. Bringen Sie die kleinstmöglichen Textabschnitte unter.
{% endalert %}

#### Lokalisierung von Links

Achten Sie bei der Lokalisierung von Anker-Tag-Links darauf, dass Sie **nur die sprachspezifischen Teile** und nicht das gesamte Attribut `href` URL einschließen. Wenn Sie die gesamte URL umbrechen, funktioniert das Link-Template möglicherweise nicht richtig.

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

### Schritt 3: Wählen Sie die Lokalisierung für Nachrichten {#choose-locales}

Nachdem Sie Ihre Tags in die Nachricht eingefügt haben, wählen Sie in den Einstellungen für die Mehrsprachigkeit der Nachricht eine oder mehrere Lokalisierungen aus, die für diese Nachricht übersetzt werden sollen.

![Mehrsprachige Einstellungen mit einem Dropdown-Feld zum Auswählen von Lokalisierungen.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Wählen Sie bei der Bearbeitung Ihrer Nachricht im Menü Contentful die Option **Multi-Language** aus.

![Mehrsprachige Einstellungen für E-Mails.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Wählen Sie **Sprachen verwalten**, wenn Sie Ihre Nachricht bearbeiten.

![Mehrsprachige Einstellungen für Push.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Wählen Sie **Sprachen verwalten** am Ende des Abschnitts **Build**.

![Mehrsprachige Einstellungen für In-App-Nachrichten per Drag-and-Drop.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Wählen Sie **Sprachen verwalten**, wenn Sie Ihre Nachricht bearbeiten.

![Mehrsprachige Einstellungen für In-App-Nachrichten im HTML-Format.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Wählen Sie **Sprachen verwalten**, wenn Sie Ihre Nachricht bearbeiten.

![Mehrsprachige Einstellungen für Werbebanner.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: CSV-Vorlage herunterladen {#download-csv}

Nachdem Sie Ihre Lokalisierungen ausgewählt haben, wählen Sie **Vorlage herunterladen**, um eine CSV-Vorlage mit einer Matrix Ihrer ausgewählten Übersetzungs-IDs und Lokalisierungen herunterzuladen.

![Beispiel-CSV für die Lokalisierungen en, fr, und es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Schritt 5: Eine ausgefüllte CSV hochladen {#upload-csv}

{% alert important %}
Alle Änderungen an den IDs oder Lokalisierungen in der CSV-Datei werden nicht automatisch in Ihrer Nachricht aktualisiert. Um die Übersetzungen zu aktualisieren, aktualisieren Sie die CSV-Datei und laden Sie die Datei erneut hoch.
{% endalert %}

Hier ist das Format für ein Beispiel für eine ausgefüllte CSV-Datei:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Schritt 6: Vorschau der Lokalisierungen {#preview-locales}

Wählen Sie bei der Vorschau Ihrer Nachricht die Option **Mehrsprachiger Nutzer:innen** aus dem Dropdown-Menü **Vorschau als Nutzer**:innen. Damit können Sie zwischen verschiedenen Lokalisierungen wechseln, um eine Vorschau auf alle Übersetzungen Ihrer Nachricht zu erhalten.

![Lokalisierungs-Vorschauen]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Sehen Sie sich unsere [Translation API]({{site.baseurl}}/api/endpoints/translations) an, um Übersetzungen in Ihren Kampagnen und Canvase zu verwalten und zu aktualisieren.
{% endalert %}

## Nachrichten von rechts nach links

Wenn Sie die Übersetzungsdatei für Sprachen ausfüllen, die von rechts nach links geschrieben werden (wie Arabisch), umschließen Sie die Übersetzung mit `span`, damit sie richtig formatiert ist:

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

Übersetzungen werden zusammen mit einem Canvas-Schritt, einer Kampagne oder einer Kampagnenvariante kopiert. Dies gilt auch für das Kopieren zwischen Workspaces, sofern die Lokalisierungen in dem Ziel-Workspace definiert sind. Achten Sie darauf, die Übersetzungen zu überprüfen und entsprechend zu aktualisieren, wenn Sie Änderungen an Ihrem Canvas oder Ihrer Kampagne vornehmen.

### Verwendung der Multi-Language API mit Canvase

Um die [Multi-Language API mit Canvase]({{site.baseurl}}/api/endpoints/translations/) zu verwenden, müssen Sie die `workflow_id`, `step_id` und `message_variation_id` in die Parameterliste aufnehmen.

#### Canvas-Schritte zu Entwürfen nach der Markteinführung hinzugefügt

Wenn Sie die Multi-Language API mit Canvas-Schritten verwenden, die nach dem Start des Canvas erstellt wurden, ist die `message_variation_id`, die Sie an die API übergeben, leer oder leer.

## Häufig gestellte Fragen

#### Kann ich eine Änderung an der übersetzten Kopie in einer meiner Lokalisationen vornehmen?
Ja Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung an der übersetzten Kopie vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln?
Nein.

#### Unterstützen die Übersetzungen HTML für das Styling?
Ja, aber achten Sie darauf, dass das HTML-Styling nicht mit dem Inhalt übersetzt wird.

#### Kann ich ganze HTML-Nachrichten in einen Tag zur Übersetzung einpacken?
Nein, Ihre Tags zur Übersetzung sollten so klein wie möglich sein, um Performance- oder Größenbeschränkungen zu vermeiden.

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
