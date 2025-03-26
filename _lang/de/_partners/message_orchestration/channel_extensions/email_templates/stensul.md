---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Stensul, einer E-Mail-Plattform für Unternehmen, mit der Sie auf einfache Weise mobilfähige E-Mail-Vorlagen für alle Kanäle erstellen können."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) ermöglicht es E-Mail-Vermarktern, auf einfache Weise mobil ansprechende, markengerechte E-Mails in Stensul zu erstellen, bevor sie diese in Echtzeit zur Kampagnenerstellung an Braze weiterleiten.

Die Integration von Braze und Stensul ermöglicht es Ihnen, Ihre HTML-formatierten Stensul-E-Mails zu exportieren und als Vorlagen in Braze hochzuladen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Stensul-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stensul-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Vorlagenberechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster-Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Stellen Sie Ihrem Stensul-Kundenerfolgsteam Ihren Braze REST API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert important %}
Dies ist eine einmalige Einrichtung und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

### Schritt 1: Stensul E-Mail erstellen

Erstellen Sie eine Stensul-E-Mail in der Stensul-Plattform und klicken Sie auf **Fertig stellen**.

![Stensul Speicheroptionen]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Schritt 2: Vorlage nach Braze exportieren
In dem neuen Dialog, der auf der Fertigstellungsseite erscheint, wählen Sie **Hochladen in ESP**.

![Stensul Upload Optionen]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Geben Sie dann den **Namen der Vorlage**, den **Betreff** und die **Überschrift** für Ihre E-Mail ein und wählen Sie **Hochladen**. Sie erhalten dann eine Bestätigung, dass der Upload erfolgreich war, und ggf. eine Übersicht über frühere Uploads der Datei.

![Stensul Upload Success]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Nutzung

Sie finden Ihre hochgeladene Stensul-Vorlage in Ihrem Braze-Konto im Bereich **Vorlagen & Medien > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kunden zu versenden!

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
