---
nav_title: Konfigurieren Sie mit Braze
article_title: Konfigurieren Sie mit Braze
page_order: 1
description: "Erfahren Sie, wie Sie BrazeAI Decisioning <sup>StudioTM</sup> Go einrichten und in Braze integrieren."
---

# Konfigurieren Sie mit Braze

> Erstellen Sie eine API-Kampagne in Braze, die für BrazeAI Decisioning Studio™ Go entwickelt wurde.

## Schritt 1: Kampagne erstellen 

1. Gehen Sie auf dem Braze-Dashboard zu **Messaging** > Kampagnen.
2. Wählen Sie **Kampagne erstellen**.
3. Wählen Sie für Ihre Kampagne den Typ **API-Kampagne** aus.
4. Geben Sie einen Namen für Ihre Kampagne ein. Ein Beispiel ist "Decisioning Studio Go E-Mail".

![Eine API-Kampagne mit dem Namen "Decisioning Studio Go E-Mail".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Wählen Sie für Ihren Messaging-Kanal **E-Mail** aus.

![Option zum Auswählen Ihres Messaging-Kanals für die API-Kampagne.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Wählen Sie unter **Zusätzliche Optionen** das Kontrollkästchen **Nutzern:innen erlauben, sich erneut für Kampagnen zu qualifizieren**.
7\. Geben Sie für die Zeit bis zur erneuten Anspruchsberechtigung **1** ein und wählen Sie **Stunden** aus dem Dropdown-Menü aus.

![Wiederzulassung für die ausgewählte API Kampagne.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Wählen Sie **Kampagne speichern**.

## Schritt 2: Kopieren Sie Ihre Kampagne ID und fügen Sie sie ein

Kopieren Sie in Ihrer API Kampagne die **Campaign ID**. Gehen Sie dann zum Portal BrazeAI Decisioning Studio™ Go und fügen Sie die **ID der Kampagne** ein.

![Ein Beispiel für eine ID für Nachrichtenvariationen, die Sie kopieren und einfügen können.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

## Schritt 3: Kopieren Sie die ID Ihrer Nachrichtenvariation und fügen Sie sie ein

Kopieren Sie in Ihrer API-Kampagne die **ID der Nachrichtenvariation**. Gehen Sie dann zum BrazeAI Decisioning Studio™ Go Portal und fügen Sie die **Message Variation ID** ein.
