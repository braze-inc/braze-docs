---
nav_title: Crowdin
article_title: Crowdin
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Crowdin, einer cloudbasierten Softwareplattform, die es Ihnen ermöglicht, die Übersetzung Ihrer E-Mail-Vorlagen und Content Blocks in Braze zu automatisieren."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin ist eine cloudbasierte Software für das Lokalisierungsmanagement. Mit Crowdin können Sie Ihre Android- und iOS-Apps, Ihre Website, Shop-Screenshots und andere Inhalte übersetzen. Die Übersetzung kann durch Ihr internes Team, ein Übersetzungsbüro oder mit Hilfe von maschinellen Übersetzungsprogrammen erfolgen.

Die Integration von Braze und Crowdin ermöglicht Ihnen die Übersetzung von E-Mail-Vorlagen und Inhaltsblöcken. Sie können auch Inhalte aus Ihrem Braze-Konto mit Ihrem Crowdin-Projekt synchronisieren und Übersetzungen zurück zu Braze hinzufügen.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| Crowdin-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Crowdin-Konto](https://accounts.crowdin.com/register). |
| Crowdin Übersetzungsprojekt | Um Ihr Braze-Konto mit Crowdin oder Crowdin Enterprise zu verbinden, müssen Sie sich zunächst anmelden und ein Übersetzungsprojekt erstellen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen für Vorlagen und Inhaltsblöcke. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze SDK Endpunkt | Die URL Ihres SDK-Endpunkts hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Einrichten der Braze-App in Crowdin/Crowdin Enterprise

#### Crowdin
Um die Braze-App in Crowdin einzurichten, folgen Sie diesen Schritten:

1. Rufen Sie die [Braze-App auf dem Marktplatz](https://store.crowdin.com/braze-app) auf.
2. Klicken Sie auf **Installieren**, um es zu Ihrem Konto hinzuzufügen.
3. Öffnen Sie das Projekt, das Sie für die Lokalisierung Ihrer Braze-Inhalte erstellt haben.
4. Gehen Sie zu **Einstellungen >** Registerkarte **Integrationen**.
5. Klicken Sie im Bereich **Anwendungen** auf die App Braze.
6. Geben Sie im Dialog Ihre Braze-Anmeldedaten ein (Braze REST API-Schlüssel und Braze SDK-Endpunkt).
7. Klicken Sie auf **Mit Braze Connector anmelden**. 

#### Crowdin Unternehmen
Um die Braze-App in Crowdin Enterprise einzurichten, folgen Sie diesen Schritten:

1. Gehen Sie zur Startseite von **Workspace** > **Marktplatz**.
2. Klicken Sie auf **Installieren** in der Braze-App, um sie Ihrer Organisation hinzuzufügen.
3. Öffnen Sie das Projekt, das Sie für die Lokalisierung Ihrer Braze-Inhalte erstellt haben.
4. Gehen Sie zu **Anwendungen > Benutzerdefiniert**.
5. Klicken Sie auf die Braze-App.
6. Geben Sie im Dialog Ihre Braze-Anmeldedaten ein (Braze REST API-Schlüssel und Braze SDK-Endpunkt).
7. Klicken Sie auf **Mit Braze Connector anmelden**.

### Schritt 2: Fügen Sie Ihre Inhalte zu Crowdin/Crowdin Enterprise hinzu

Sobald Sie Ihre Braze-Zugangsdaten eingegeben haben, sehen Sie zwei Felder. Wählen Sie den gewünschten Inhalt, um die Dateien für die Übersetzung von Ihrem Braze-Konto zu synchronisieren, und klicken Sie auf **Mit Crowdin synchronisieren**.

Im Editor-Modus von Crowdin können die von Ihrem Braze-Konto synchronisierten Inhalte Ihren Übersetzern als Stringliste oder als Dateivorschau angezeigt werden.

![Ein Bild davon, wie der E-Mail-Composer von Crowdin Editor aussieht, dem einige grundlegende Übersetzungen hinzugefügt wurden.][2]

### Schritt 3: Übersetzungen hinzufügen zu Braze

Sobald die Übersetzungen abgeschlossen sind, öffnen Sie die Braze-App in Crowdin, wählen Sie die übersetzten Dateien (für jede Datei können Sie entweder alle Zielsprachen oder nur bestimmte auswählen) auf der linken Seite aus und klicken Sie auf **Mit Braze synchronisieren**.

![Ein Bild eines Benutzers, der seine Übersetzungsdateien auswählt und sie mit Braze synchronisiert.][3]

[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
