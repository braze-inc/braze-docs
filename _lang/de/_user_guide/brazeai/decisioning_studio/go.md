---
nav_title: Entscheidungsfindung Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 0
description: "Erfahren Sie, wie Sie BrazeAI Decisioning <sup>StudioTM</sup> Go einrichten und in Braze integrieren."
---

# BrazeAI Decisioning Studio™ Go

> Suchen Sie die wichtigsten Informationen in Braze, um die Integration mit BrazeAI Decisioning Studio™ Go zu beginnen.

## Grundlegendes

### Erstellen eines REST API-Schlüssels in Braze

So erstellen Sie einen neuen REST-API-Schlüssel:

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Wählen Sie **API-Schlüssel erstellen**.
3. Geben Sie einen Namen für Ihren API-Schlüssel ein. Ein Beispiel ist "DecisioningStudioGoEmail".
4. Wählen Sie die Berechtigungen anhand der folgenden Kategorien aus:
    - **Nutzerdaten:** Wählen Sie `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Nachrichten:** auswählen `messages.send`
    - **Kampagnen:** Wählen Sie alle aufgeführten Berechtigungen aus
    - **Canvas:** alle aufgeführten Berechtigungen auswählen
    - **Segmente:** alle aufgeführten Berechtigungen auswählen
    - **Templates:** Wählen Sie alle aufgelisteten Berechtigungen aus

{: start="5"}
5\. Wählen Sie **API-Schlüssel erstellen**.
6\. Kopieren Sie dann den API-Schlüssel und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go Portal ein.

### Lokalisierung Ihres Braze E-Mail Anzeigenamens

So finden Sie Ihren Braze E-Mail Anzeigenamen:

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Suchen Sie den Anzeigenamen, der mit BrazeAI Decisioning Studio™ Go verwendet werden soll.
3. Kopieren Sie den **Von-Anzeigenamen** und fügen Sie ihn in das BrazeAI Decisioning Studio™ Go-Portal als **E-Mail-Anzeigenamen** ein.
4. Kopieren Sie die zugehörige E-Mail Adresse und fügen Sie sie in Ihr BrazeAI Decisioning Studio™ Go Portal als **Absender-E-Mail Adresse** ein, die den lokalen Teil und die Domain kombiniert.

### Finden Sie Ihre Nutzer:in ID

So finden Sie Ihre Nutzer:innen ID:

1. Gehen Sie im Braze-Dashboard auf **Zielgruppe** > Nutzer:innen suchen.
2. Suchen Sie den Nutzer:innen nach seiner externen ID, seinem Nutzer-Alias, seiner E-Mail, seiner Telefonnummer oder seinem Push-Token.
3. Kopieren Sie die ID des Nutzers:innen, um sie in Ihrer Einrichtung zu referenzieren.

![Beispiel eines Nutzerprofils aus dem Auffinden eines Nutzer:innen mit seiner ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Finden Sie Ihre Braze URL

Zur Identifizierung Ihrer Braze URL:

1. Rufen Sie das Braze-Dashboard auf.
2. In Ihrem Browserfenster beginnt die URL von Braze mit `https://` und endet mit `braze.com`. Ein Beispiel für eine Braze-URL ist `https://dashboard-01.braze.com`.

### Finden Sie Ihren Braze API-Schlüssel

{% alert note %}
Braze bietet IDs für Apps (im Braze-Dashboard als API-Schlüssel bezeichnet), die Sie für das Tracking verwenden können, z. B. um Aktivitäten mit einer bestimmten App in Ihrem Workspace zu verknüpfen. Wenn Sie App IDs verwenden, unterstützt BrazeAI Decisioning Studio™ Go die Verknüpfung einer App ID mit jedem Experimentator.<br><br>Wenn Sie keine App IDs verwenden, können Sie eine beliebige Zeichenkette als Platzhalter eingeben.
{% endalert %}

1. Gehen Sie auf dem Braze-Dashboard zu **Einstellungen** > **App-Einstellungen**.
2. Gehen Sie zu der App, die Sie tracken möchten.
3. Kopieren Sie den **API-Schlüssel** und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go Portal ein.

### Einrichten von Klaviyo API-Schlüsseln

Sie müssen einen API-Schlüssel einrichten, um Klaviyo für BrazeAI Decisioning Studio™ Go zu verwenden.

1. Gehen Sie in Klaviyo zu **Einstellungen** > **API-Schlüssel**.
2. Wählen Sie **Privaten API-Schlüssel erstellen**. 
3. Geben Sie einen Namen für den API-Schlüssel ein. Ein Beispiel ist "Decisioning Studio Experimenters".
4. Wählen Sie die folgenden Berechtigungen für den API-Schlüssel aus:
    - Kampagnen: Zugang lesen
    - Datenschutz: Vollzugriff
    - Ereignisse: Vollzugriff
    - Ströme: Vollzugriff
    - Bilder: Zugang lesen
    - Liste: Vollzugriff
    - Metriken: Vollzugriff
    - Profile: Vollzugriff
    - Segmente: Zugang lesen
    - Templates: Vollzugriff
    - Webhooks: Zugang lesen

![Ein Klaviyo API-Schlüssel mit ausgewählten Rechten.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Wählen Sie **Erstellen**.
6\. Kopieren Sie diesen API-Schlüssel und fügen Sie ihn in das BrazeAI Decisioning Studio™ Go Portal ein, wenn Sie dazu aufgefordert werden.

### Einrichten eines SFMC App-Pakets

Um Salesforce Marketing Cloud für BrazeAI Decisioning Studio™ Go zu nutzen, müssen Sie ein App-Paket in Salesforce Marketing Cloud einrichten. 

1. Gehen Sie zur Startseite Ihrer Marketing Cloud. 
2. Öffnen Sie das Menü in der globalen Kopfzeile und wählen Sie **Einstellungen**.
3. Gehen Sie in der Navigation des seitlichen Panels unter **Plattform-Tools** auf **Apps** und wählen Sie dann **Installierte Pakete**.
4. Wählen Sie **Neu**, um ein App-Paket zu erstellen.
5. Geben Sie dem App-Paket einen Namen und eine Beschreibung.

![Ein App-Paket mit dem Namen "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Wählen Sie **Komponente hinzufügen**.
7\. Wählen Sie als **Komponententyp** **API Integration** aus. Wählen Sie dann **Weiter**.
8\. Als **Integrationstyp** wählen Sie **Server-zu-Server**. Wählen Sie dann **Weiter**.
9\. Wählen Sie dann die folgenden empfohlenen Bereiche nur für Ihr App-Paket aus:
    \- Kanäle > E-Mail > Lesen, Schreiben, Senden
    \- Kanäle > OTT > Lesen
    \- Kanäle > Push > Lesen
    \- Kanäle > SMS > Lesen
    \- Kanäle > Soziale Netzwerke > Lesen
    \- Kanäle > Internet > Lesen
    \- Assets > Dokumente und Bilder > Lesen, Schreiben
    \- Assets > Gespeicherte Inhalte > Lesen, Schreiben
    \- Automatisierung > Automatisierungen > Lesen, Schreiben, Ausführen
    \- Automatisierung > Journeys > Lesen, Schreiben, Ausführen, Aktivieren/Stop/Pause/Senden/Zeitplan
    \- Kontakte > Zielgruppen > Lesen
    \- Kontakte > Liste und Abonnent:innen > Lesen, Schreiben
    \- Cross Cloud Platform > Market Zielgruppe > Ansicht
    \- Cross Cloud Platform > Market Zielgruppe Mitglied > Ansicht
    \- Cross Cloud Platform > Marketing Cloud Connect > Lesen
    \- Daten > Datenerweiterungen > Lesen, Schreiben
    \- Daten > Standorte der Dateien > Lesen
    \- Daten > Tracking-Ereignisse > Lesen, Schreiben
    \- Ereignisbenachrichtigungen > Callbacks > Lesen
    \- Ereignisbenachrichtigungen > Abonnements > Lesen

{% details Show image of recommended scopes %}

![Die empfohlenen Geltungsbereiche für das Salesforce Marketing Cloud App-Paket.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Wählen Sie **Speichern**.
11\. Kopieren Sie die folgenden Felder und fügen Sie sie in das BrazeAI Decisioning Studio™ Go Portal ein: **Client-ID**, **Client-Geheimnis**, **Authentifizierungs-Basis-URI**, **REST-Basis-URI**, **SOAP-Basis-URI**.