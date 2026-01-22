---
nav_title: Hochladen einer HTML-E-Mail-Vorlage
article_title: Hochladen einer HTML-E-Mail-Vorlage
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie eine HTML-E-Mail-Template mit dem Braze-Dashboard erstellen, verwalten und Fehler beheben."
tool:
  - Templates
channel:
  - email

---

# Hochladen einer HTML-E-Mail-Vorlage

> Über das Braze-Dashboard können Sie Ihre eigenen HTML-E-Mail-Templates hochladen und zur späteren Verwendung in Kampagnen speichern. Sie können auch [eine E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) mit unserem Editor [erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/).

## Voraussetzungen {#upload-requirements}

Zunächst müssen Sie Ihre HTML-E-Mail-Vorlage erstellen. Dies muss eine ZIP-Datei sein, die Folgendes enthält:

* Eine einzelne HTML-Datei - der Textkörper Ihrer E-Mail
* Ein Ordner mit Bildern, auf die in der HTML-Datei verwiesen wird
* Weniger als 50 Bilddateien
* Weniger als 5 MB

## Hochladen Ihrer Template

### Schritt 1: Navigieren Sie zum Editor für E-Mail-Vorlagen

Gehen Sie zu **Vorlagen** > **E-Mail-Vorlagen**.

### Schritt 2: Öffnen Sie den Uploader

Wählen Sie unter dem Abschnitt **Vorlagentyp** die Option **HTML-Editor** und scrollen Sie nach unten zum Abschnitt **Von einer einfachen HTML-Vorlage ausgehen**. Wählen Sie **Aus Datei**.

### Schritt 3: Laden Sie Ihre Vorlage hoch

Wählen Sie **Aus Datei hochladen** und wählen Sie Ihr Template von Ihrem Computer aus. Lesen Sie den Abschnitt [Voraussetzungen](#upload-requirements), um sicherzustellen, dass Ihre Template die Upload-Anforderungen erfüllt.

#### Fehler beim Hochladen von Vorlagen beheben

Beim Hochladen einer HTML-Vorlagendatei können Sie mehrere E-Mail-Fehlermeldungen erhalten. Wenn Sie einen Fehler erhalten, finden Sie in der folgenden Tabelle häufige Probleme und deren empfohlene Behebung:

| Fehler | Behebung |
|------|---|
|.zip über 5 MB| Verringern Sie die Dateigröße und versuchen Sie, die Datei erneut hochzuladen.|
|.zip beschädigt| Überprüfen Sie Ihre Datei und versuchen Sie, sie erneut hochzuladen. |
|HTML fehlt| Fügen Sie die HTML-Datei zu Ihrer ZIP-Datei hinzu und versuchen Sie erneut, sie hochzuladen.|
|Mehrere HTML-Dateien| Entfernen Sie eine der HTML-Dateien und versuchen Sie, sie erneut hochzuladen.|
|Bilder über 5 MB| Verringern Sie die Anzahl der Bilder und versuchen Sie erneut hochzuladen. |
|Extra Bilder| Möglicherweise befinden sich in Ihrer Datei weitere Bilder, auf die in Ihrer HTML-Datei nicht verwiesen wird. Dies führt nicht zu einem Fehler, aber die zusätzlichen Bilder werden verworfen. Wenn diese Bilder in der HTML-Datei referenziert werden sollten, überprüfen Sie den Inhalt, korrigieren Sie eventuelle Fehler und versuchen Sie, die Datei erneut hochzuladen.|
|Fehlende Bilder| Wenn in Ihrer HTML-Datei auf Bilder verwiesen wird, diese Bilder aber nicht im Bildordner der ZIP-Datei enthalten sind, erhalten Sie einen Dateifehler. Überprüfen Sie Ihre Datei und korrigieren Sie eventuelle Fehler (z.B. Rechtschreibfehler), oder fügen Sie die fehlenden Bilder zu Ihrer ZIP-Datei hinzu und versuchen Sie, sie erneut hochzuladen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 4: Template fertigstellen und speichern

Speichern Sie Ihr Template, indem Sie **Template speichern** auswählen. Jetzt können Sie diese Vorlage in jeder beliebigen Kampagne oder jedem beliebigen Canvas verwenden!

{% alert note %}
Wenn Sie Änderungen an einer bestehenden Vorlage vornehmen, werden diese Änderungen nicht in Kampagnen übernommen, die mit früheren Versionen dieser Vorlage erstellt wurden.
{% endalert %}

## Verwendung Ihrer Vorlagen in API-Kampagnen {#api_for_upload_email_templates}

Um Ihre E-Mail für eine API-Kampagne zu verwenden, benötigen Sie die `email_template_id`, die Sie am Ende jeder in Braze erstellten E-Mail-Template finden.

![API Bezeichner Abschnitt einer HTML E-Mail Vorlage.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## E-Mail-Vorlagen verwalten

Sie können E-Mail-Templates [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)! Erfahren Sie mehr über die Erstellung und Verwaltung von Vorlagen und kreativen Inhalten unter [Vorlagen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Häufig gestellte Fragen

Antworten auf häufig gestellte Fragen zu E-Mail Templates finden Sie auf unserer [FAQ-Seite zu E-Mail- und Link-Templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).


