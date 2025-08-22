---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Stensul, einer E-Mail-Plattform für Unternehmen, die es Ihnen erlaubt, auf allen Kanälen einfach mobile, responsive E-Mail-Templates zu erstellen."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) versetzt Marketer in die Lage, in Stensul responsive, markengerechte E-Mails zu erstellen, bevor sie diese zur Erstellung von Kampagnen in Realtime an Braze weiterleiten.

_Diese Integration wird von Stensul gepflegt._

## Über die Integration

Die Integration von Braze und Stensul ermöglicht es Ihnen, Ihre HTML-formatierten E-Mails aus Stensul zu exportieren und sie als Templates in Braze hochzuladen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Stensul Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stensul-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Stellen Sie Ihrem Stensul Customer-Success-Team Ihren Braze REST API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert important %}
Dies ist eine einmalige Einrichtung und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

### Schritt 1: Stensul E-Mail erstellen

Erstellen Sie eine Stensul E-Mail in der Stensul Plattform und klicken Sie auf **Fertig stellen**.

![Stensul Speicheroptionen]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Schritt 2: Template nach Braze exportieren
In dem neuen Dialog, der auf der Fertigstellungsseite erscheint, wählen Sie **Hochladen in ESP**.

![Stensul Upload Optionen]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Geben Sie dann den **Namen des Templates**, den **Betreff** und den **Preheader** für Ihre E-Mail ein und wählen Sie **Hochladen**. Sie erhalten dann eine Bestätigung, dass der Upload erfolgreich war und ggf. einen Verlauf früherer Uploads der Datei.

![Stensul Upload Success]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Nutzung

Sie finden Ihr hochgeladenes Template für Stensul in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail Templates**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende Nachrichten an Ihre Kund:in zu versenden!


