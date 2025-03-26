---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Stripo, einem Drag-and-Drop-E-Mail-Vorlagenersteller, mit dem Sie problemlos anspruchsvolle E-Mails mit interaktiven Elementen erstellen können."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) ist ein Drag-and-Drop-E-Mail-Vorlagenersteller, mit dem Sie responsive E-Mails mit interaktiven Elementen erstellen und gestalten können. Stripo-Benutzer können auch in HTML editieren und über den Stripo-Editor entscheiden, welche Elemente auf verschiedenen Geräten angezeigt oder ausgeblendet werden sollen.

Die Integration von Braze und Stripo ermöglicht es Ihnen, Ihre angepassten Stripo-E-Mails zu exportieren und sie als Vorlagen in Braze hochzuladen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Stripo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stripo-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Vorlagenberechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster-Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Stripo E-Mail erstellen

Erstellen Sie eine Stripo-E-Mail in der Stripo-Plattform und klicken Sie auf **Exportieren**. 

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### Schritt 2: Vorlage nach Braze exportieren

Wählen Sie in dem daraufhin angezeigten Dialogfeld **Braze** als Exportmethode aus. 

Als nächstes geben Sie Ihren **Kontonamen** (z.B. den Namen des Arbeitsbereichs), den **API-Schlüssel** und Ihre **Cluster-Instanz** ein.

![Stripo Formular]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Nutzung

Sie finden Ihre hochgeladene Stripo-Vorlage in Ihrem Braze-Konto im Bereich **Vorlagen & Medien > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kunden zu versenden!

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
