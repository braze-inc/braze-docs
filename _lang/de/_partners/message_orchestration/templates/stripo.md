---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und Stripo, einem E-Mail-Builder per Drag-and-Drop, mit dem Sie auf einfache Weise anspruchsvolle E-Mails mit interaktiven Elementen erstellen können."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) ist ein E-Mail-Builder per Drag-and-Drop, mit dem Sie responsive E-Mails mit interaktiven Elementen erstellen und gestalten können. Nutzer:innen von Stripo können mit dem Stripo-Editor auch HTML bearbeiten und entscheiden, welche Elemente auf verschiedenen Geräten angezeigt oder ausgeblendet werden sollen.

_Diese Integration wird von Stripo gepflegt._

## Über die Integration

Die Integration von Braze und Stripo ermöglicht es Ihnen, Ihre angepassten E-Mails von Stripo zu exportieren und als Templates in Braze hochzuladen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Stripo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stripo-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Stripo E-Mail erstellen

Erstellen Sie eine Stripo E-Mail in der Stripo-Plattform und klicken Sie auf **Exportieren**. 

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### Schritt 2: Template nach Braze exportieren

Wählen Sie in dem nun erscheinenden Dialog **Braze** als Exportmethode aus 

Als nächstes geben Sie Ihren **Kontonamen** (z.B. den Namen des Workspace), den **API-Schlüssel** und Ihre **Instanz** ein.

![Stripo Formular]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Nutzung

Ihre hochgeladene Stripo-Vorlage finden Sie in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende Nachrichten an Ihre Kund:in zu versenden!


