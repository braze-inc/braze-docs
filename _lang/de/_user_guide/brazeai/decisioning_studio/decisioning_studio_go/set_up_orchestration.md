---
nav_title: Orchestrierung einrichten
article_title: Orchestrierung einrichten
page_order: 2
description: "Erfahren Sie, wie Sie BrazeAI Decisioning Studio Go mit Ihrer Customer-Engagement-Plattform verbinden, um personalisierte Kommunikation zu ermöglichen."
toc_headers: h2
---

# Orchestrierung einrichten

> BrazeAI Decisioning Studio™ Go muss mit Ihrer Customer-Engagement-Plattform (CEP) verbunden werden, um die personalisierte Kommunikation zu orchestrieren. Dieser Artikel erklärt, wie Sie die Integration für jeden unterstützten CEP einrichten.

## Unterstützte CEPs

Decisioning Studio Go unterstützt die folgenden Customer-Engagement-Plattformen:

| CEP | Integrationstyp | Wichtigste Features |
|-----|-----------------|--------------|
| **Braze** | Per API getriggerte Kampagnen | Native Integration, Triggern in Realtime |
| **Salesforce Marketing Cloud** | Journey Builder mit API-Ereignissen | Automatisierung von SQL-Abfragen, Datenerweiterungen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wählen Sie unten Ihren CEP aus, um mit der Einrichtung der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Einrichten der Braze-Integration

Um Decisioning Studio Go mit Braze zu integrieren, erstellen Sie einen API-Schlüssel, konfigurieren eine API-getriggerte Kampagne und stellen dem Decisioning Studio Go-Portal die erforderlichen Bezeichner zur Verfügung.

### Schritt 1: Einen REST API-Schlüssel erstellen

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Wählen Sie **API-Schlüssel erstellen**.
3. Geben Sie einen Namen für Ihren API-Schlüssel ein. Ein Beispiel ist "DecisioningStudioGoEmail".
4. Wählen Sie die Berechtigungen anhand der folgenden Kategorien aus:
    - **Nutzerdaten:** Wählen Sie `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Nachrichten:** auswählen `messages.send`
    - **Kampagnen:** Wählen Sie alle aufgeführten Berechtigungen aus
    - **Canvas:** alle aufgeführten Berechtigungen auswählen
    - **Segmente:** alle aufgeführten Berechtigungen auswählen
    - **Templates:** alle aufgeführten Berechtigungen auswählen

{: start="5"}
5\. Wählen Sie **API-Schlüssel erstellen**.
6\. Kopieren Sie den API-Schlüssel und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go Portal ein.

### Schritt 2: Suchen Sie den Namen Ihrer E-Mail-Anzeige

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Suchen Sie den Anzeigenamen, der mit BrazeAI Decisioning Studio™ Go verwendet werden soll.
3. Kopieren Sie den **Von-Anzeigenamen** und fügen Sie ihn in das BrazeAI Decisioning Studio™ Go-Portal als **E-Mail-Anzeigenamen** ein.
4. Kopieren Sie die zugehörige E-Mail Adresse und fügen Sie sie in Ihr BrazeAI Decisioning Studio™ Go Portal als **Absender-E-Mail Adresse** ein, die den lokalen Teil und die Domain kombiniert.

### Schritt 3: Finden Sie Ihre Braze URL und App ID

**So finden Sie Ihre Braze URL:**
1. Rufen Sie das Braze-Dashboard auf.
2. In Ihrem Browserfenster beginnt Ihre Braze-URL mit `https://` und endet mit `braze.com`. Ein Beispiel für eine Braze-URL ist `https://dashboard-01.braze.com`.

**So finden Sie Ihre App ID (API-Schlüssel):**

{% alert note %}
Braze bietet IDs für Apps (im Braze-Dashboard als API-Schlüssel bezeichnet), die Sie für das Tracking verwenden können, z. B. um Aktivitäten mit einer bestimmten App in Ihrem Workspace zu verknüpfen. Wenn Sie App IDs verwenden, unterstützt BrazeAI Decisioning Studio™ Go die Verknüpfung einer App ID mit jedem Experimentator.<br><br>Wenn Sie keine App IDs verwenden, können Sie eine beliebige Zeichenkette als Platzhalter eingeben.
{% endalert %}

1. Gehen Sie auf dem Braze-Dashboard zu **Einstellungen** > **App-Einstellungen**.
2. Gehen Sie zu der App, die Sie tracken möchten.
3. Kopieren Sie den **API-Schlüssel** und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go Portal ein.

### Schritt 4: Erstellen Sie eine API-getriggerte Kampagne

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

### Schritt 5: Kopieren Sie die IDs Ihrer Kampagnen und Nachrichten

1. Kopieren Sie in Ihrer API Kampagne die **Campaign ID**. Gehen Sie dann zum Portal BrazeAI Decisioning Studio™ Go und fügen Sie die **ID der Kampagne** ein.

![Ein Beispiel für eine ID für Nachrichtenvariationen, die Sie kopieren und einfügen können.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Kopieren Sie die **ID der Nachrichtenvariation**. Gehen Sie dann zum BrazeAI Decisioning Studio™ Go Portal und fügen Sie die **Message Variation ID** ein.

### Schritt 6: Suchen Sie eine Testnutzer:in ID

Um Ihre Integration zu testen, benötigen Sie eine Nutzer:innen ID:

1. Gehen Sie im Braze-Dashboard auf **Zielgruppe** > Nutzer:innen suchen.
2. Suchen Sie den Nutzer:innen nach seiner externen ID, seinem Nutzer-Alias, seiner E-Mail, seiner Telefonnummer oder seinem Push-Token.
3. Kopieren Sie die ID des Nutzers:innen, um sie in Ihrer Einrichtung zu referenzieren.

![Beispiel eines Nutzerprofils aus dem Auffinden eines Nutzer:innen mit seiner ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Einrichten der SFMC-Integration

Um Decisioning Studio Go in Salesforce Marketing Cloud zu integrieren, richten Sie ein App-Paket ein, erstellen eine Automatisierung der Datenabfrage und bauen eine Journey, um ausgelöste Sendungen zu verarbeiten.

### Teil 1: Ein SFMC App-Paket einrichten

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
9\. Wählen Sie nur die folgenden empfohlenen Bereiche für Ihr App-Paket aus:
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

### Teil 2: Einrichten einer Automatisierung der Datenabfrage

#### Schritt 1: Erstellen Sie eine neue Automatisierung

1. Gehen Sie von Ihrer Salesforce Marketing Cloud Startseite aus zum **Journey Builder** und wählen Sie **Automation Studio**.

![Option Automatisierung Studio in der Navigation des Journey Builders.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Wählen Sie **Neue Automatisierung**.
3\. Ziehen Sie per Drag-and-Drop einen **Zeitplan-Knoten** als **Startquelle**.

!["Zeitplan" als Startquelle einer Reise.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. Wählen Sie im Knoten **Zeitplan** die Option **Konfigurieren**.
5\. Stellen Sie für den Zeitplan Folgendes ein:
    - **Startdatum:** Der morgige Tag im Kalender
    - **Zeit:** **12:00 UHR**
    - **Zeitzone:** **(GMT-05:00) Ostküste (US & Kanada)**
6\. Für **Wiederholung** wählen Sie **Täglich**.
7\. Stellen Sie diesen Zeitplan so ein, dass er nie endet.
8\. Wählen Sie **Fertig**, um den Zeitplan zu speichern.

![Ein Beispiel für einen Zeitplan, der für den 25\. Januar 2024 um 12 Uhr ET festgelegt wurde und sich jeden Tag wiederholt.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Schritt 2: Erstellen Sie Ihre SQL-Anfragen

Als nächstes erstellen Sie 2 SQL-Anfragen: eine Abfrage für Abonnenten:innen und eine Abfrage für das Engagement. Diese Abfragen erlauben es BrazeAI Decisioning Studio™ Go, Daten abzurufen, um die Zielgruppe zu füllen und Engagement-Ereignisse aufzunehmen.

**Abonnent:innen abfragen:**

1. Ziehen Sie eine **SQL-Abfrage** per Drag-and-Drop in den Canvas.
2. Wählen Sie **Auswählen**.
3. Wählen Sie **Neue Abfrageaktivität erstellen**.
4. Geben Sie der Abfrage einen Namen und einen externen Schlüssel. Wir empfehlen Ihnen, den vorgeschlagenen Namen und den externen Schlüssel für die Abonnent:in-Abfrage zu verwenden, die Sie in Ihrem BrazeAI Decisioning Studio™ Go Portal finden.

![Ein Beispiel "OFE_Subscribers_query_Test5" und der externe Schlüssel.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Wählen Sie **Weiter**.
6\. In Ihrem BrazeAI Decisioning Studio™ Go-Portal finden Sie die SQL-Abfrage für Systemdaten unter **Abonnenten-Abfrage-Ressourcen**.
7\. Kopieren Sie die Abfrage, fügen Sie sie in das Textfeld ein und wählen Sie **Weiter**.

![Eine Beispielabfrage im Abschnitt SQL-Abfrage.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. Suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal im Abschnitt **Zu verwendende Ressourcen** den externen Schlüssel der Zieldatenerweiterung. Fügen Sie ihn dann in die Suchleiste ein, um zu suchen.

![Ein externer Schlüssel, der in die Suchleiste eingefügt wird]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Wählen Sie die Datenerweiterung aus, die mit dem gesuchten externen Schlüssel übereinstimmt. Der Name der Targeting-Datenerweiterung wird auch in Ihrem BrazeAI Decisioning Studio™ Go-Portal als Querverweis bereitgestellt. Die **Datenerweiterung** für die Abonnent:in-Abfrage sollte mit einem `BASE_AUDIENCE_DATA` Suffix enden.

![Der Name der Datenerweiterung, die dem externen Schlüssel des Beispiels entspricht.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Wählen Sie **Überschreiben** und dann **Weiter**.

**Anfrage zum Engagement:**

1. Ziehen Sie eine **SQL-Abfrage** per Drag-and-Drop in den Canvas.

!["SQL-Anfrage" als Aktivität in der Journey hinzugefügt.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Wählen Sie **Auswählen**.
3\. Wählen Sie **Neue Abfrageaktivität erstellen**.
4\. Geben Sie der Abfrage einen Namen und einen externen Schlüssel. Wir empfehlen die Verwendung des vorgeschlagenen Namens und des externen Schlüssels für die Engagement-Abfrage, die Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal finden.

![Ein Beispiel "OFE_Engagement_query" und der externe Schlüssel.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Wählen Sie **Weiter**.
6\. Suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal unter **Engagement Query Resources** die SQL-Abfrage Systemdaten.
7\. Kopieren Sie die Abfrage, fügen Sie sie in das Textfeld ein und wählen Sie **Weiter**.

![Eine Beispielabfrage im Abschnitt SQL-Abfrage.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Suchen Sie die Ziel-Datenerweiterung für die in Ihrem BrazeAI Decisioning Studio™ Go-Portal angegebene Engagement-Abfrage und wählen Sie sie aus.

{% alert tip %}
Der Name der Targeting-Datenerweiterung wird auch in Ihrem BrazeAI Decisioning Studio™ Go-Portal als Querverweis bereitgestellt. Vergewissern Sie sich, dass Sie die Ziel-Datenerweiterung für die Engagement-Abfrage betrachten. Die **Datenerweiterung** für die Abfrage des Engagements sollte mit einem Suffix ENGAGEMENT_DATA enden.
{% endalert %}

{: start="9"}
9\. Wählen Sie **Überschreiben** und dann **Weiter**.

![Der Name der Datenerweiterung, die dem externen Schlüssel des Beispiels entspricht.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Schritt 3: Starten Sie die Automatisierung

1. Geben Sie der Automatisierung einen Namen und wählen Sie **Speichern**.

![Ein Beispiel für die Automatisierung "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. Wählen Sie anschließend **Einmal ausführen**, um zu bestätigen, dass alles wie erwartet funktioniert.
3\. Wählen Sie beide Abfragen aus und wählen Sie **Ausführen**.

![Eine Automatisierung "OFE_Experimenter_Test5_Automation" mit einer Liste ausgewählter SQL-Abfrageaktivitäten, die ausgeführt werden sollen.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Wählen Sie **Jetzt ausführen**.

![Eine ausgewählte SQL-Abfrageaktivität.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Jetzt können Sie überprüfen, ob die Automatisierung erfolgreich läuft. Wenden Sie sich an den Braze Support, wenn Ihre Automatisierung nicht wie erwartet funktioniert.

### Teil 3: Erstellen Sie Ihre SFMC-Reise

#### Schritt 1: Die Reise einrichten

1. Gehen Sie in Salesforce Marketing Cloud zu **Journey Builder** > **Journey Builder**.
2. Wählen Sie **Neue Reise erstellen**.
3. Wählen Sie für Ihre Reiseart **Mehrstufige Reise** und wählen Sie dann **Erstellen**.

![Eine API-Eingangsquelle, die mit einem Decision-Split-Knoten und mehreren E-Mail-Knoten verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Schritt 2: Bauen Sie die Reise

**Erstellen Sie eine Eingangsquelle:**

1. Ziehen Sie **API Event** als Eingangsquelle in den Journey Builder.

!["API Event" als Eingangsquelle ausgewählt.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. Wählen Sie im **API-Ereignis** die Option **Ein Ereignis erstellen**.

![Die Option "Ein Ereignis erstellen" in der API Ereignis.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Wählen Sie **Datenerweiterung auswählen**. Suchen Sie die Datenerweiterung, in die BrazeAI Decisioning Studio™ Go Empfehlungen schreiben wird, und wählen Sie sie aus.
4\. Wählen Sie **Zusammenfassung**, um Ihre Änderungen zu speichern.
5\. Wählen Sie **Fertig**, um das API-Ereignis zu speichern.

![Zusammenfassung der API-Ereignisse.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Fügen Sie einen Decision-Split hinzu:**

1. Ziehen Sie einen **Decision-Split** per Drag-and-Drop nach dem **API-Eingang-Ereignis**.
2. Wählen Sie in den **Decision-Split-Details** für den ersten Pfad **Bearbeiten** aus.

![Decision-Split Details mit dem Button "Bearbeiten".]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Aktualisieren Sie den **Decision-Split**, um die Template ID zu verwenden, die von der Datenerweiterung für Empfehlungen übergeben wurde. Suchen Sie das entsprechende Feld unter **Reisedaten**.

![Der Abschnitt Journey-Daten in Pfad 1 des Decision-Splits.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Wählen Sie Ihr Eingangsereignis aus und suchen Sie das gewünschte Feld für die ID der Vorlage. Ziehen Sie es dann in den Workspace.

![Die ID der E-Mail-Vorlage, die Sie angeben müssen.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Geben Sie die Template ID Ihrer ersten E-Mail-Vorlage ein und wählen Sie dann **Fertig**.
6\. Wählen Sie **Zusammenfassung**, um diesen Pfad zu speichern.
7\. Fügen Sie einen Pfad für jede Ihrer E-Mail-Vorlagen hinzu und wiederholen Sie dann die Schritte 4-6, um die Filterkriterien so einzustellen, dass die ID der Vorlage mit dem ID-Wert der jeweiligen Vorlage übereinstimmt.
8\. Wählen Sie **Fertig**, um den **Decision-Split-Knoten** zu speichern.

![Zwei Pfade in einem Decision-Split für jede E-Mail Template ID.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Fügen Sie eine E-Mail für jeden Decision-Split hinzu:**

1. Ziehen Sie einen Knoten **E-Mail** in jeden Pfad des **Decision-Splits**.
2. Wählen Sie **E-Mail** und wählen Sie dann die entsprechende Vorlage aus, die in jeden Pfad eingefügt werden soll (d.h. die Vorlage mit dem ID-Wert sollte der Logik in Ihrem Decision-Split entsprechen).

![Ein E-Mail-Knotenpunkt wurde der Journey hinzugefügt.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Schritt 3: Aktivieren Sie die Reise

Nachdem Sie Ihre Journey eingerichtet haben, aktivieren Sie sie und teilen dem Team von BrazeAI Decisioning Studio™ Go die folgenden Details mit:

* ID der Reise
* Name der Reise
* API-Schlüssel zur Definition von Ereignissen
* Empfehlungen Datenerweiterung externer Schlüssel

{% alert note %}
Das BrazeAI Decisioning Studio™ Go-Portal zeigt Ihnen die SFMC-Automatisierung an, die einmal täglich die Daten der Abonnent:innen und des Engagements exportiert. Wenn Sie diese Automatisierung in SFMC öffnen, stellen Sie sicher, dass Sie die Pause aufheben und die Automatisierung wieder in Betrieb nehmen.
{% endalert %}

1. Kopieren Sie im BrazeAI Decisioning Studio™ Go-Portal den **Namen der Journey**.
2. Als nächstes fügen Sie im Salesforce Marketing Cloud Journey Builder den Namen der Journey in die Suchleiste ein.
3. Wählen Sie den Namen der Reise aus. Beachten Sie, dass sich die Reise derzeit im Entwurfsstatus befindet.
4. Wählen Sie **Validieren**.

![Die abgeschlossene Reise zur Aktivierung.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. Prüfen Sie dann die Validierungsergebnisse und wählen Sie **Aktivieren**.

![Empfehlungen, die im Abschnitt Validierungsregeln aufgeführt sind.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. Wählen Sie in der Zusammenfassung **Aktivieren der Reise** erneut **Aktivieren** aus.

![Zusammenfassung für die Reise.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Jetzt können Sie loslegen! Sie können jetzt damit beginnen, Sendungen über BrazeAI Decisioning Studio™ Go zu triggern.

{% endtab %}
{% endtabs %}

## Nächste Schritte

Nachdem Sie nun die Orchestrierung eingerichtet haben, fahren Sie mit der Gestaltung Ihres Agenten fort:

- [Agenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
