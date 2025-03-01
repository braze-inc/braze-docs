---
nav_title: IAM Studio
article_title: IAM Studio
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und IAM Studio, einer Plattform zur Personalisierung von Nachrichten, die es Ihnen ermöglicht, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze bereitzustellen."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) ist eine Plattform zur Personalisierung von Nachrichten ohne Code, mit der Sie personalisierte, reichhaltige In-App-Erlebnisse erstellen und diese über Braze bereitstellen können.

Mit der Integration von Braze und IAM Studio können Sie ganz einfach anpassbare In-App-Nachrichtenvorlagen in Ihre In-App-Nachrichten von Braze einfügen, die Bilder ersetzen, Text ändern, Deep-Link-Einstellungen, benutzerdefinierte Attribute und Ereigniseinstellungen bieten. Mit IAM Studio können Sie die Produktionszeit für Nachrichten reduzieren und mehr Zeit für die Planung von Inhalten aufwenden. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| IAM Studio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [IAM Studio-Konto](https://www.inappmessage.com/register). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

- Förderung des Kaufs von Waren
- Sammlung von Benutzerinformationen
- Steigende Mitgliederzahlen
- Informationen zur Ausgabe von Kupons

## Integration

### Schritt 1: Template auswählen

Wählen Sie eine In-App-Nachrichtenvorlage aus der Galerie der In-App-Nachrichtenvorlagen aus, die Sie verwenden möchten.

![In der IAM Studio Vorlagengalerie finden Sie verschiedene Vorlagen wie "Karussell-Schiebe-Modal", "Einfaches Symbol-Modal", "Modal Vollbild" und mehr.][1]

### Schritt 2: Anpassen der Vorlage

Passen Sie zunächst das Bild, den Text und die Schaltfläche für Ihren Inhalt an. Stellen Sie sicher, dass Sie **Deeplink** für das Bild und die Schaltfläche verbinden.

{% tabs local %}
{% tab Bild %}
![Die IAM Studio-Benutzeroberfläche mit den Optionen zum Anpassen des Bildes. Diese Optionen umfassen das Bild, den Bildradius und das abgeblendete Bild.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![Die IAM Studio-Benutzeroberfläche zeigt die Optionen zum Anpassen des Titels und des Untertitels Ihrer Nachricht. Diese Optionen umfassen Text, Formatierung und Schriftart.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Schaltfläche %}
![Die IAM Studio-Benutzeroberfläche zeigt die Optionen zur Anpassung der Haupt-, linken und rechten Taste. Diese Optionen umfassen Farbe, Deep Link, Text und Formatierung.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Als nächstes erstellen Sie Ihre persönliche In-App-Nachricht, indem Sie benutzerdefinierte Schriftarten hinzufügen und Liquid-Tags verwenden. Um die Protokollierung und Verfolgung zu aktivieren, wählen Sie **Daten protokollieren und Benutzerverhalten verfolgen**.

{% tabs local %}
{% tab Schriftarten %}
![Die Benutzeroberfläche von IAM Studio zeigt die Optionen zum Hinzufügen von Liquid. Zu diesen Optionen gehört die Erstellung eines personalisierten Satzes.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Flüssigkeit %}
![Die Benutzeroberfläche von IAM Studio mit den Optionen zur Anpassung der Ereignis-/Attributprotokollierung. Diese Optionen beinhalten, dass das Benutzerverhalten protokolliert wird.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Protokollierung und Verfolgung %}
![Die IAM Studio-Benutzeroberfläche zeigt die Optionen zur Anpassung der Schriftart. Diese Optionen beinhalten, dass der Benutzer den Schriftstil anpassen kann.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Schritt 3: Exportieren Sie die Vorlage

Wenn Sie alle Bearbeitungen abgeschlossen haben, exportieren Sie die Vorlage, indem Sie auf **Exportieren** klicken. Nach dem Exportieren wird der HTML-Code für die In-App-Nachricht generiert. Kopieren Sie diesen Code, indem Sie auf die Schaltfläche **Code kopieren** klicken. 

![][2]{: style="max-width:45%;"}

### Schritt 4: Code in Braze verwenden 

Navigieren Sie zu Braze, und fügen Sie in Ihrer In-App-Nachricht den benutzerdefinierten Code in das **HTML-Eingabefeld** ein. Testen Sie Ihre Nachricht, um sicherzustellen, dass sie korrekt angezeigt wird.

![][3]{: style="max-width:85%;"}

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}
