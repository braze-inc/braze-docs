---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und Stensul, einer E-Mail-Plattform für Unternehmen zur Erstellung mobiler, responsiver E-Mail-Templates für verschiedene Kanäle."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) stellt E-Mail Marketern Tools zur Verfügung, mit denen sie in Stensul responsive, markengerechte E-Mails erstellen können, bevor sie diese zur Erstellung von Kampagnen in Realtime an Braze weiterleiten.

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

![Stensul Optionen speichern]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Schritt 2: Template nach Braze exportieren
In dem neuen Dialog, der auf der Fertigstellungsseite erscheint, wählen Sie **Hochladen in ESP**.

![Stensul Upload Optionen]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Geben Sie dann den **Namen des Templates**, den **Betreff** und den **Preheader** für Ihre E-Mail ein und wählen Sie **Hochladen**. Sie erhalten dann eine Bestätigung, dass der Upload erfolgreich war und ggf. einen Verlauf früherer Uploads der Datei.

![Stensul Upload Erfolg]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Nutzung

Sie finden Ihre hochgeladene Stensul-Vorlage in Ihrem Braze-Konto im Bereich **Templates & Media > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende Nachrichten an Ihre Kund:in zu versenden!


