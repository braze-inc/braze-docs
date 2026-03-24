---
nav_title: Hochladen eines HTML Templates für E-Mails
article_title: Hochladen eines HTML E-Mail-Templates
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie ein HTML-E-Mail-Template über das Braze-Dashboard erstellen, verwalten und Fehler beheben."
tool:
  - Templates
channel:
  - email

---

# Hochladen eines HTML Templates für E-Mails

> Über das Braze-Dashboard können Sie Ihre eigenen HTML-E-Mail-Templates hochladen und zur späteren Verwendung in Kampagnen speichern. Sie können auch [ein E-Mail-Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) mit unserem Editor erstellen.

## Voraussetzungen {#upload-requirements}

Zunächst müssen Sie Ihr HTML-E-Mail-Template erstellen. Dies muss eine ZIP-Datei sein, die Folgendes enthält:

* Eine einzelne HTML-Datei – der Textkörper Ihrer E-Mail
* Ein Ordner mit Bildern, auf die in der HTML-Datei verwiesen wird
* Weniger als 50 Bilddateien
* Weniger als 5&nbsp;MB

## Hochladen Ihres Templates

### 1. Schritt: Navigieren Sie zum Editor für E-Mail-Templates

Gehen Sie zu **Templates** > **E-Mail-Templates**.

### 2. Schritt: Öffnen Sie den Uploader

Wählen Sie unter dem Abschnitt **Template-Typ** die Option **HTML-Editor** aus und scrollen Sie nach unten zum Abschnitt **Von einem einfachen HTML-Template ausgehen**. Wählen Sie **Aus Datei**.

### 3. Schritt: Laden Sie Ihr Template hoch

Wählen Sie **Aus Datei hochladen** und wählen Sie Ihr Template von Ihrem Computer aus. Lesen Sie den Abschnitt [Voraussetzungen](#upload-requirements), um sicherzustellen, dass Ihr Template die Upload-Anforderungen erfüllt.

### 4. Schritt: Template fertigstellen und speichern

Speichern Sie Ihr Template, indem Sie **Template speichern** auswählen. Jetzt können Sie dieses Template in jeder beliebigen Kampagne oder jedem beliebigen Canvas verwenden!

{% alert note %}
Wenn Sie Änderungen an einem bestehenden Template vornehmen, werden diese Änderungen nicht in Kampagnen übernommen, die mit früheren Versionen dieses Templates erstellt wurden.
{% endalert %}

## Verwendung Ihrer Templates in API-Kampagnen {#api_for_upload_email_templates}

Um Ihre E-Mail für eine API-Kampagne zu verwenden, benötigen Sie die `email_template_id`, die Sie am Ende jedes in Braze erstellten E-Mail-Templates finden.

![Abschnitt „API-Bezeichner" eines HTML-E-Mail-Templates.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## E-Mail-Templates verwalten

Sie können E-Mail-Templates [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)! Mehr über die Erstellung und Verwaltung von Templates und kreativen Inhalten erfahren Sie unter [Templates]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Fehlerbehebung

Beim Hochladen einer HTML-Template-Datei können verschiedene E-Mail-Fehlermeldungen auftreten. Wenn Sie einen Fehler erhalten, finden Sie in der folgenden Tabelle häufige Probleme und deren empfohlene Behebung:

| Fehler | Behebung |
|------|---|
|`.zip über 5&nbsp;MB`| Verringern Sie die Dateigröße und versuchen Sie, die Datei erneut hochzuladen.|
|`.zip beschädigt`| Überprüfen Sie Ihre Datei und versuchen Sie, sie erneut hochzuladen. |
|`HTML fehlt`| Fügen Sie die HTML-Datei zu Ihrer ZIP-Datei hinzu und versuchen Sie erneut, sie hochzuladen.|
|`Mehrere HTML-Dateien`| Entfernen Sie eine der HTML-Dateien und versuchen Sie, sie erneut hochzuladen.|
|`Bilder über 5&nbsp;MB`| Verringern Sie die Anzahl der Bilder und versuchen Sie erneut hochzuladen. |
|`Zusätzliche Bilder`| Möglicherweise befinden sich in Ihrer Datei weitere Bilder, auf die in Ihrer HTML-Datei nicht verwiesen wird. Dies führt nicht zu einem Fehler, aber die zusätzlichen Bilder werden verworfen. Wenn diese Bilder in der HTML-Datei referenziert werden sollten, überprüfen Sie den Inhalt, korrigieren Sie eventuelle Fehler und versuchen Sie, die Datei erneut hochzuladen.|
|`Fehlende Bilder`| Wenn in Ihrer HTML-Datei auf Bilder verwiesen wird, diese Bilder aber nicht im Bildordner der ZIP-Datei enthalten sind, erhalten Sie einen Dateifehler. Überprüfen Sie Ihre Datei und korrigieren Sie eventuelle Fehler (z. B. Rechtschreibfehler), oder fügen Sie die fehlenden Bilder zu Ihrer ZIP-Datei hinzu und versuchen Sie, sie erneut hochzuladen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Beachten Sie, dass beim Herunterladen der Dateien für HTML-Kampagnen, Canvas-Schritte mit E-Mail-Nachrichten oder Templates auf einem Windows-Computer das Zeichen `|` (Pipe-Zeichen) nicht unterstützt wird. Möglicherweise müssen Sie eine andere Anwendung verwenden, um den Inhalt der ZIP-Datei zu extrahieren.

## Häufig gestellte Fragen

Antworten auf häufig gestellte Fragen zu E-Mail-Templates finden Sie auf unserer [FAQ-Seite zu E-Mail- und Link-Templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).