---
nav_title: Crowdin
article_title: Crowdin
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Crowdin, einer cloudbasierten Softwareplattform, die es Ihnen erlaubt, die Übersetzung Ihrer E-Mail-Templates und Content-Blöcke in Braze zu automatisieren."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin ist eine cloudbasierte Software zur Verwaltung der Lokalisierung. Mit Crowdin können Sie Ihre Android- und iOS-Apps, Ihre Website, Shop-Screenshots und andere Inhalte übersetzen. Die Übersetzung kann durch Ihr internes Team, eine Übersetzungsagentur oder mit Hilfe von maschinellen Übersetzungsprogrammen erfolgen.

_Diese Integration wird von Crowdin gepflegt._

## Über die Integration

Die Integration von Braze und Crowdin erlaubt Ihnen die Übersetzung von E-Mail Templates und Content-Blöcken. Sie können auch Inhalte aus Ihrem Braze-Konto mit Ihrem Crowdin-Projekt synchronisieren und Übersetzungen zurück zu Braze hinzufügen.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| Crowdin Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Crowdin-Konto](https://accounts.crowdin.com/register). |
| Crowdin Übersetzungsprojekt | Um Ihr Braze-Konto mit Crowdin oder Crowdin Enterprise zu verbinden, müssen Sie sich zunächst registrieren und ein Übersetzungsprojekt erstellen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen für Templates und Content-Blöcke. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze SDK-Endpunkt | Die URL Ihres SDK-Endpunkts hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Einrichten der Braze App in Crowdin/Crowdin Enterprise

#### Crowdin
Um die Braze App in Crowdin einzurichten, gehen Sie folgendermaßen vor:

1. Rufen Sie die [Braze App auf dem Marktplatz](https://store.crowdin.com/braze-app) auf.
2. Klicken Sie auf **Installieren**, um es zu Ihrem Konto hinzuzufügen.
3. Öffnen Sie das Projekt, das Sie für die Lokalisierung Ihrer Braze-Inhalte erstellt haben.
4. Gehen Sie zu **Einstellungen > Tab Integrationen.** 
5. Klicken Sie im Bereich **Anwendungen** auf die App Braze.
6. Geben Sie im Dialogfeld Ihre Braze-Zugangsdaten an (REST-API-Schlüssel und SDK-Endpunkt von Braze).
7. Klicken Sie auf **Mit Braze Connector anmelden**. 

#### Crowdin Unternehmen
Um die Braze App in Crowdin Enterprise einzurichten, gehen Sie folgendermaßen vor:

1. Gehen Sie auf die **Workspace-Homepage** > **Marketplace**.
2. Klicken Sie auf **Installieren** in der Braze App, um sie zu Ihrer Organisation hinzuzufügen.
3. Öffnen Sie das Projekt, das Sie für die Lokalisierung Ihrer Braze-Inhalte erstellt haben.
4. Gehen Sie zu **Anwendungen > Anpassen.**
5. Klicken Sie auf die Braze App.
6. Geben Sie im Dialogfeld Ihre Braze-Zugangsdaten an (REST-API-Schlüssel und SDK-Endpunkt von Braze).
7. Klicken Sie auf **Mit Braze Connector anmelden**.

### Schritt 2: Fügen Sie Ihre Inhalte zu Crowdin/Crowdin Enterprise hinzu

Sobald Sie Ihre Zugangsdaten für Braze eingegeben haben, sehen Sie zwei Panels. Wählen Sie den gewünschten Inhalt aus, um die Dateien für die Übersetzung aus Ihrem Braze-Konto zu synchronisieren, und klicken Sie auf **Mit Crowdin synchronisieren**.

Im Editor-Modus in Crowdin können die von Ihrem Braze-Konto synchronisierten Inhalte Ihren Übersetzern als String-Liste oder als Dateivorschau angezeigt werden.

![Ein Bild davon, wie der E-Mail Composer von Crowdin Editor aussieht, dem einige grundlegende Übersetzungen hinzugefügt wurden.]({% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %})

### Schritt 3: Übersetzungen hinzufügen zu Braze

Sobald die Übersetzungen abgeschlossen sind, öffnen Sie die App Braze in Crowdin, wählen Sie die übersetzten Dateien (für jede Datei können Sie entweder alle Zielsprachen oder nur bestimmte auswählen) im linken Panel aus und klicken Sie auf **Sync to Braze**.

![Ein Bild eines Nutzers, der seine Übersetzungsdateien auswählt und mit Braze synchronisiert.]({% image_buster /assets/img/crowdin/sync_translations.png %})


