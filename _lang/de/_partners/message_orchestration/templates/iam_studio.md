---
nav_title: IAM Studio
article_title: IAM Studio
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und IAM Studio, einer Plattform zur Personalisierung von Nachrichten, die es Ihnen erlaubt, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) ist eine Plattform zur Personalisierung von Nachrichten ohne Code, die es Ihnen erlaubt, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen.

_Diese Integration wird von IAM Studio.\*s gepflegt._

## Über die Integration

Mit der Integration von Braze und IAM Studio können Sie ganz einfach anpassbare In-App-Nachrichtentemplates in Ihre Braze In-App-Nachrichten einfügen. Sie bieten Bildersatz, Textänderung, Deeplink-Einstellungen, angepasste Attribute und Ereigniseinstellungen. Mit IAM Studio können Sie die Produktionszeit für Nachrichten reduzieren und mehr Zeit für die Planung von Inhalten aufwenden. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| IAM Studio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [IAM Studio-Konto](https://www.inappmessage.com/register). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

- Anregung zum Kauf von Waren
- Sammlung von Nutzer:innen-Informationen
- Steigende Mitgliederzahlen
- Informationen zur Ausgabe von Kupons

## Integration

### Schritt 1: Template auswählen

Wählen Sie ein Template für In-App-Nachrichten aus der Galerie der In-App-Nachrichten-Templates aus, das Sie verwenden möchten.

![In der IAM Studio Template-Galerie finden Sie verschiedene Templates wie "Carousel Slide Modal", "Simple Icon Modal", "Modal Full Image" und mehr.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Schritt 2: Anpassen des Templates

Passen Sie zunächst das Bild, den Text und den Button für Ihren Inhalt an. Stellen Sie sicher, dass Sie **Deeplink** für das Bild und den Button verbinden.

{% tabs local %}
{% tab Bild %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen des Bildes an. Diese Optionen umfassen das Bild, den Bildradius und das abgeblendete Bild.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen des Titels und des Untertitels Ihrer Nachricht an. Diese Optionen umfassen Text, Formatierung und Schriftart.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen des Haupt-, linken und rechten Buttons. Diese Optionen umfassen Farbe, Deeplinks, Text und Formatierung.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Als nächstes erstellen Sie Ihre personalisierte In-App-Nachricht, indem Sie angepasste Schriftarten hinzufügen und Liquid-Tags verwenden. Um die Protokollierung und das Tracking zu aktivieren, wählen Sie **Daten protokollieren und das Verhalten der Nutzer:innen verfolgen**.

{% tabs local %}
{% tab Schriftarten %}
![Das UI von IAM Studio zeigt die Optionen zum Hinzufügen von Liquid. Zu diesen Optionen gehört die Personalisierung von Sätzen.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![Das IAM Studio UI mit den Optionen zur Anpassung der Ereignis-/Attribut-Protokollierung. Diese Optionen beinhalten das Protokoll des Nutzer:in-Verhaltens.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Protokollierung und Tracking %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen der Schriftart an. Diese Optionen beinhalten, dass Nutzer:in den Schriftstil anpassen können.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png %})
{% endtab %}
{% endtabs %}

### Schritt 3: Exportieren Sie die Vorlage

Wenn Sie alle Bearbeitungen abgeschlossen haben, exportieren Sie das Template, indem Sie auf **Exportieren** klicken. Nach dem Exportieren wird der HTML Code für In-App-Nachricht generiert. Kopieren Sie diesen Code, indem Sie auf den Button **Code kopieren** klicken. 

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Schritt 4: Code in Braze verwenden 

Navigieren Sie zu Braze, und fügen Sie in Ihrer In-App-Nachricht den angepassten Code in das **HTML-Eingabefeld** ein. Testen Sie Ihre Nachricht, um sicherzustellen, dass sie korrekt angezeigt wird.

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}


