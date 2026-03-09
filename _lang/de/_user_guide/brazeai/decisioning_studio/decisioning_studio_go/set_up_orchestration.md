---
nav_title: Orchestrierung einrichten
article_title: Orchestrierung einrichten
page_order: 2
description: "Erfahren Sie, wie Sie BrazeAI Decisioning Studio mit Ihrer Customer-Engagement-Plattform verbinden, um personalisierte Kommunikation zu ermöglichen."
toc_headers: h2
---

# Orchestrierung einrichten

> BrazeAI Decisioning Studio™ Go muss mit Ihrer Customer-Engagement-Plattform (CEP) verbunden sein, um personalisierte Kommunikation zu ermöglichen. Dieser Artikel erläutert, wie Sie die Integration für jedes unterstützte CEP einrichten.

## Unterstützte CEPs

Decisioning Studio Go unterstützt die folgenden Customer-Engagement-Plattformen:

| CEP | Integrationstyp | Wichtigste Features |
|-----|-----------------|--------------|
| **Braze** | Per API getriggerte Kampagnen | Native Integration, Realtime-Triggern |
| **Salesforce Marketing Cloud** | Journey Builder mit API-Ereignissen | Automatisierung von SQL-Anfragen, Datenerweiterungen |
| **Klaviyo** | Flows mit metrischen Triggern | Vorlagenbasierte Trigger-Aufteilungen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Bitte wählen Sie unten Ihren CEP aus, um mit der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Einrichtung der Braze-Integration

Um Decisioning Studio Go in Braze zu integrieren, erstellen Sie einen API-Schlüssel, konfigurieren eine API-gesteuerte Kampagne und stellen die erforderlichen Bezeichner für das Decisioning Studio Go-Portal bereit.

### Schritt 1: Einen REST API-Schlüssel erstellen

1. Bitte navigieren Sie im Braze-Dashboard zu **„Einstellungen“** > **„APIs und Bezeichner“** > **„API-Schlüssel**“.
2. Wählen Sie **API-Schlüssel erstellen**.
3. Bitte geben Sie einen Namen für Ihren API-Schlüssel ein. Ein Beispiel hierfür ist „DecisioningStudioGoEmail“.
4. Bitte wählen Sie die Berechtigungen anhand der folgenden Kategorien aus:
    - **Nutzerdaten:** Bitte wählen Sie `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Nachrichten:** auswählen `messages.send`
    - **Kampagnen:** Bitte wählen Sie alle aufgeführten Berechtigungen aus.
    - **Canvas:** Bitte wählen Sie alle aufgeführten Berechtigungen aus.
    - **Segmente:** Bitte wählen Sie alle aufgeführten Berechtigungen aus.
    - **Templates:** Bitte wählen Sie alle aufgeführten Berechtigungen aus.

{: start="5"}
5\. Wählen Sie **API-Schlüssel erstellen**.
6\. Bitte kopieren Sie den API-Schlüssel und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go-Portal ein.

### Schritt 2: Bitte suchen Sie Ihren E-Mail-Anzeigenamen.

1. Bitte navigieren Sie im Braze-Dashboard zu **„Einstellungen“** > **„E-Mail-Einstellungen**“.
2. Bitte suchen Sie den Anzeigenamen, der mit BrazeAI Decisioning Studio™ Go verwendet werden soll.
3. Bitte kopieren Sie den **Anzeigenamen** und fügen Sie ihn als **Anzeigenamen** **für E-Mails** in das BrazeAI Decisioning Studio™ Go-Portal ein.
4. Bitte kopieren Sie die zugehörige E-Mail-Adresse und fügen Sie sie in Ihr BrazeAI Decisioning Studio™ Go-Portal als **Absender-E-Mail-Adresse** ein, wobei der lokale Teil und die Domain kombiniert werden.

### Schritt 3: Bitte suchen Sie Ihre Braze-URL und App-ID.

**Um Ihre Braze-URL zu finden:**
1. Bitte gehen Sie zum Braze-Dashboard.
2. In Ihrem Browserfenster beginnt Ihre Braze-URL mit`https://`und endet mit`braze.com`. Ein Beispiel für eine Braze-URL lautet`https://dashboard-01.braze.com`: .

**Um Ihre App-ID (API-Schlüssel) zu ermitteln:**

{% alert note %}
Braze stellt App-IDs (im Braze-Dashboard als API-Schlüssel bezeichnet) zur Verfügung, die Sie für Tracking-Zwecke verwenden können, beispielsweise um Aktivitäten mit einer bestimmten App in Ihrem Workspace zu verknüpfen. Bei Verwendung von App-IDs unterstützt BrazeAI Decisioning Studio™ Go die Zuordnung einer App-ID zu jedem Experimentator.<br><br>Wenn Sie keine App-IDs verwenden, können Sie einen beliebigen String als Platzhalter eingeben.
{% endalert %}

1. Bitte gehen Sie im Braze-Dashboard zu **„Einstellungen“** > **„App-Einstellungen**“.
2. Bitte gehen Sie zu der App, die Sie für das Tracking verwenden möchten.
3. Bitte kopieren Sie den **API-Schlüssel** und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go-Portal ein.

### Schritt 4: Erstellen Sie eine API-gesteuerte Kampagne

1. Bitte gehen Sie im Braze-Dashboard zu **„Messaging“** > **„Kampagnen**“.
2. Bitte wählen Sie **„Kampagne erstellen**“.
3. Bitte wählen Sie für Ihren Kampagnentyp **„API-Kampagne**“ aus.
4. Bitte geben Sie einen Namen für Ihre Kampagne ein. Ein Beispiel hierfür ist „Decisioning Studio Go E-Mail“.

![Eine API-Kampagne mit dem Namen „Decisioning Studio Go E-Mail”.]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Bitte wählen Sie für Ihren Messaging-Kanal **„E-Mail“** aus.

![Option zum Auswählen Ihres Messaging-Kanals für die API-Kampagne.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Wählen Sie unter **„Zusätzliche Optionen**“ das Kontrollkästchen **„Nutzer:innen erlauben, erneut für Kampagnen in Frage zu kommen**“.
7\. Um die Zeit für die erneute Berechtigung einzugeben, geben Sie **bitte 1** ein und wählen Sie **„Stunden”** aus dem Dropdown-Menü aus.

![Wiederwahlberechtigung für die ausgewählte API-Kampagne.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Bitte wählen Sie **„Kampagne speichern**“.

### Schritt 5: Bitte kopieren Sie Ihre Kampagnen- und Nachrichten-IDs.

1. Bitte kopieren Sie in Ihrer API-Kampagne die **Kampagnen-ID**. Begeben Sie sich anschließend zum Portal „BrazeAI Decisioning Studio™ Go“ und fügen Sie die **ID der Kampagne** ein.

![Ein Beispiel für eine ID für eine Nachrichtsvariation, die kopiert und eingefügt werden soll.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Bitte kopieren Sie die **ID der Nachrichtenvariation**. Begeben Sie sich anschließend zum Portal „BrazeAI Decisioning Studio™ Go“ und fügen Sie die **ID der Nachrichtenvariante** ein.

### Schritt 6: Bitte suchen Sie eine ID für einen Testnutzer:in.

Um Ihre Integration zu testen, benötigen Sie eine Benutzer-ID:

1. Bitte gehen Sie im Braze-Dashboard zu **„Zielgruppe“** > **„Nutzersuche**“.
2. Suchen Sie den Nutzer anhand seiner externen ID, seines Nutzer-Alias, seiner E-Mail-Adresse, seiner Telefonnummer oder seines Push-Tokens.
3. Bitte kopieren Sie die ID des Nutzers, um sie in Ihrer Konfiguration zu referenzieren.

![Beispiel für ein Nutzerprofil, das einen Nutzer anhand seiner ID identifiziert.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Einrichtung der SFMC-Integration

Um Decisioning Studio Go in die Salesforce Marketing Cloud zu integrieren, richten Sie ein App-Paket ein, erstellen eine Automatisierung für Datenabfragen und entwickeln eine Journey zur Verarbeitung ausgelöster Sendungen.

### Teil 1: Einrichten einer SFMC-App-App-Paket

1. Bitte gehen Sie zu Ihrer Marketing Cloud-Startseite.
2. Öffnen Sie das Menü in der globalen Kopfzeile und wählen Sie **„Einstellungen**“.
3. Bitte navigieren Sie im Panel zu **„Apps“** unter **„Plattform-Tools“** und wählen Sie anschließend **„Installierte Pakete“** aus.
4. Bitte wählen Sie **„Neu“,** um ein App-Paket zu erstellen.
5. Bitte geben Sie der App-App einen Namen und eine Beschreibung.

![Ein App-Paket mit dem Namen „Experimenter 1 – Test 5”.]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Bitte wählen Sie **„Komponente hinzufügen**”.
7\. Wählen Sie für den **Komponententyp** **„API-Integration**“ aus. Wählen Sie anschließend **„Weiter**“.
8\. Auswählen Sie für den **Integrationstyp** **„Server-zu-Server**“. Wählen Sie anschließend **„Weiter**“.
9\. Bitte wählen Sie ausschließlich die folgenden empfohlenen Bereiche für Ihr App-Paket aus:
    \- Kanäle > E-Mail > Lesen, Schreiben, Senden
    \- Kanäle > OTT > Lesen
    \- Kanäle > Push > Lesen
    \- Kanäle > SMS > Lesen
    \- Kanäle > Soziales > Lesen
    \- Kanäle > Internet > Lesen
    \- Assets > Dokumente und Bilder > Lesen, Schreiben
    \- Assets > Gespeicherte Inhalte > Lesen, Schreiben
    \- Automatisierung > Automatisierungen > Lesen, Schreiben, Ausführen
    \- Automatisierung > Journeys > Lesen, Schreiben, Ausführen, Aktivieren/Stoppen/Pausieren/Senden/Zeitplan
    \- Kontakte > Zielgruppen > Lesen
    \- Kontakte > Liste und Abonnent:innen > Lesen, Schreiben
    \- Cross Cloud-Plattform > Zielgruppe des Marktes > Ansicht
    \- Cross Cloud-Plattform > Zielgruppe des Marktes > Ansicht
    \- Cross Cloud-Plattform > Marketing Cloud Connect > Lesen
    \- Daten > Datenerweiterungen > Lesen, Schreiben
    \- Daten > Dateistandorte > Lesen
    \- Daten > Tracking-Ereignisse > Lesen, Schreiben
    \- Ereignisbenachrichtigungen > Callbacks > Lesen
    \- Ereignisbenachrichtigungen > Abonnements > Lesen

{% details Show image of recommended scopes %}

![Die empfohlenen Bereiche für das Salesforce Marketing Cloud-App-Paket.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Wählen Sie **Speichern**.
11\. Bitte kopieren Sie die folgenden Felder und fügen Sie sie in das BrazeAI Decisioning Studio™ Go-Portal ein: **Client-ID**, **Client-Geheimnis**, **Authentifizierungs-Basis-URI**, **REST-Basis-URI**, **SOAP-Basis-URI**.

### Teil 2: Richten Sie eine Automatisierung für Datenabfragen ein.

#### Schritt 1: Erstellen Sie eine neue Automatisierung

1. Bitte gehen Sie von Ihrer Salesforce Marketing Cloud-Startseite aus zu **Journey Builder** und wählen Sie **Automation Studio** aus.

![Option „Automatisierung“ in der Navigation des Journey Builders.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Bitte wählen Sie **„Neue Automatisierung**“.
3\. Ziehen Sie einen **Zeitplan**-Knoten per Drag-and-Drop als **Startquelle**.

![„Zeitplan“ als Ausgangspunkt einer Reise.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. Auswählen Sie im Knoten **„Zeitplan**“ **die Option „Konfigurieren**“.
5\. Bitte stellen Sie für den Zeitplan Folgendes ein:
    - **Startdatum:** Der morgige Tag im Kalender
    - **Zeit:** **12:00 UHR**
    - **Zeitzone:** **(GMT-05:00) Ostküste (USA, &Kanada)**
6\. Wählen Sie für **„Wiederholen“** **die Option „Täglich**“.
7\. Bitte stellen Sie diesen Zeitplan so ein, dass er niemals endet.
8\. Bitte wählen Sie **„Fertig“,** um den Zeitplan zu speichern.

![Ein Beispiel für einen Zeitplan, der für den 25\. Januar 2024 um 12 Uhr ET definiert wurde und sich täglich wiederholt.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Schritt 2: Erstellen Sie Ihre SQL-Anfragen

Erstellen Sie anschließend zwei SQL-Anfragen: eine Anfrage für Abonnent:innen und eine Anfrage für Engagement. Diese Abfragen ermöglichen es BrazeAI Decisioning Studio™ Go, Daten abzurufen, um die Zielgruppen zu füllen und Engagement-Ereignisse zu erfassen.

**Anfrage der Abonnent:innen:**

1. Ziehen Sie eine **SQL-Anfrage** per Drag-and-Drop auf das Canvas.
2. **Bitte wählen Sie „Auswählen**“.
3. Bitte wählen Sie **„Neue Abfrageaktivität erstellen**“.
4. Bitte geben Sie der Abfrage einen Namen und einen externen Schlüssel. Wir empfehlen, den vorgeschlagenen Namen und den externen Schlüssel für die Abonnentenabfrage zu verwenden, die in Ihrem BrazeAI Decisioning Studio™ Go-Portal angegeben sind.

![Ein Beispiel"OFE_Subscribers_query_Test5"und der externe Schlüssel.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Wählen Sie **Weiter**.
6\. Bitte suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal die SQL-Anfrage „Systemdaten“ unter **„Abonnentenabfrage-Ressourcen**“.
7\. Bitte kopieren Sie die Abfrage in das Textfeld und wählen Sie **„Weiter**“.

![Ein Beispiel für eine Abfrage im Abschnitt „SQL-Anfragen“.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. Bitte suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal im Abschnitt **„Zu verwendende Ressourcen**“ den externen Schlüssel der Zieldatenerweiterung. Bitte fügen Sie es anschließend in die Suchleiste ein, um die Suche durchzuführen.

![Ein externer Schlüssel, der in die Suchleiste eingefügt wurde]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Auswählen Sie die Erweiterung der Daten, die mit dem von Ihnen gesuchten externen Schlüssel übereinstimmt. Der Name der Zieldaten-Erweiterung wird ebenfalls in Ihrem BrazeAI Decisioning Studio™ Go-Portal zur Querverweisung angegeben, um die Daten zu referenzieren. Die **Datenerweiterung** für die Abonnent:innen-Abfrage sollte mit einem`BASE_AUDIENCE_DATA`Suffix enden.

![Der Name der Erweiterung für die Daten, der mit dem Beispiel für den externen Schlüssel übereinstimmt.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Bitte wählen Sie **„Überschreiben“** und anschließend **„Weiter**“.

**Anfrage zum Engagement:**

1. Ziehen Sie eine **SQL-Anfrage** per Drag-and-Drop auf das Canvas.

![„SQL-Anfrage“ wurde als Aktivität in die Journey aufgenommen.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. **Bitte wählen Sie „Auswählen**“.
3\. Bitte wählen Sie **„Neue Abfrageaktivität erstellen**“.
4\. Bitte geben Sie der Abfrage einen Namen und einen externen Schlüssel. Wir empfehlen, den vorgeschlagenen Namen und den externen Schlüssel für die Abfrage zum Engagement zu verwenden, die in Ihrem BrazeAI Decisioning Studio™ Go-Portal bereitgestellt werden.

![Ein Beispiel"OFE_Engagement_query"und der externe Schlüssel.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Wählen Sie **Weiter**.
6\. Bitte suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal die SQL-Anfrage „Systemdaten“ unter **„Engagement-Abfrage-Ressourcen**“.
7\. Bitte kopieren Sie die Abfrage in das Textfeld und wählen Sie **„Weiter**“.

![Ein Beispiel für eine Abfrage im Abschnitt „SQL-Anfragen“.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Suchen und auswählen Sie die gewünschte Datenerweiterung für die in Ihrem BrazeAI Decisioning Studio™ Go-Portal angegebene Engagement-Abfrage aus.

{% alert tip %}
Der Name der Zieldaten-Erweiterung wird ebenfalls in Ihrem BrazeAI Decisioning Studio™ Go-Portal zur Querverweisung angegeben, um die Daten zu referenzieren. Bitte stellen Sie sicher, dass Sie die richtige Datenerweiterung für die Engagement-Abfrage betrachten. Die **Datenerweiterung** für die Engagement-Abfrage sollte mit demENGAGEMENT_DATASuffix „.suffix“ enden.
{% endalert %}

{: start="9"}
9\. Bitte wählen Sie **„Überschreiben“** und anschließend **„Weiter**“.

![Der Name der Erweiterung für die Daten, der mit dem Beispiel für den externen Schlüssel übereinstimmt.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Schritt 3: Führen Sie die Automatisierung aus.

1. Bitte geben Sie der Automatisierung einen Namen und wählen Sie **„Speichern**“.

![Ein Beispiel für Automatisierung/assets/img/decisioning_studio_go/query3.pngimage_buster"OFE_Experimenter_Test5_Automation".]({%    %})

{: start="2"}
2\. Wählen Sie anschließend **„Einmal ausführen“**, um zu bestätigen, dass alles wie erwartet funktioniert.
3\. Bitte wählen Sie beide Abfragen aus und klicken Sie auf **„Ausführen**“.

![Eine Automatisierung"OFE_Experimenter_Test5_Automation"mit einer Liste ausgewählter SQL-Anfragen, die ausgeführt werden sollen.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Bitte wählen Sie **„Jetzt ausführen**“.

![Eine ausgewählte SQL-Anfrage-Aktivität.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Nun können Sie überprüfen, ob die Automatisierung erfolgreich ausgeführt wird. Bitte wenden Sie sich an den Braze-Support, wenn Ihre Automatisierung nicht wie erwartet funktioniert.

### Teil 3: Gestalten Sie Ihre SFMC-Reise

#### Schritt 1: Die Reise vorbereiten

1. Bitte gehen Sie in Salesforce Marketing Cloud zu **Journey Builder** > **Journey Builder**.
2. Auswählen **„Neue Reise erstellen**“.
3. Wählen Sie für Ihre Reiseart **„Mehrstufige Reise**“ aus und wählen Sie anschließend **„Erstellen**“.

![Eine API-Ereignis-Eingangsquelle, die mit einem Decision-Split-Knoten und mehreren E-Mail-Knoten verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Schritt 2: Die Reise gestalten

**Erstellen Sie einen Eingang:**

1. Ziehen Sie für Ihren Eingang **„API Event**“ in den Journey Builder.

![„API-Ereignis“ wurde als Eingabequelle ausgewählt.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. Wählen Sie im **API-Ereignis** **die Option „Ereignis erstellen“** aus.

![Die Option „Ereignis erstellen“ in der API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Bitte **wählen Sie „Datenerweiterung“ aus**. Bitte suchen und auswählen Sie die Datenerweiterung aus, in die BrazeAI Decisioning Studio™ Go Empfehlungen schreiben soll.
4\. Bitte wählen Sie **„Zusammenfassung“,** um Ihre Änderungen zu speichern.
5\. Auswählen Sie **„Fertig“,** um das API-Ereignis zu speichern.

![Zusammenfassung der API-Ereignisse.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Fügen Sie eine Decision-Split hinzu:**

1. Ziehen Sie eine **Decision-Split** per Drag-and-Drop hinter das **API-Eingabeereignis.**
2. Auswählen Sie in den Details **zum Decision-Split** für den ersten Pfad **die Option „Bearbeiten**“.

![Decision-Split mit dem Button „Bearbeiten“ aufteilen.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Bitte aktualisieren Sie die **Decision-Split,** um die von der Empfehlungsdatenerweiterung übergebene Template-ID zu verwenden. Bitte suchen Sie das entsprechende Feld unter **„Reisedaten**“.

![Der Abschnitt „Reisedaten“ in Pfad 1 der Decision-Split.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Bitte wählen Sie Ihr Eingangsereignis aus und suchen Sie das gewünschte Template-ID-Feld. Ziehen Sie es anschließend in die Workspace.

![Die ID des E-Mail-Templates, die eingefügt werden soll.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Geben Sie bitte die ID Ihres ersten Templates für E-Mails ein und wählen Sie anschließend **„Fertig**“.
6\. Bitte wählen Sie **„Zusammenfassung“,** um diesen Pfad zu speichern.
7\. Fügen Sie für jedes Ihrer Templates einen Pfad hinzu und wiederholen Sie anschließend die Schritte 4 bis 6, um die Filterkriterien so festzulegen, dass die Template-ID mit dem ID-Wert jedes Templates übereinstimmt.
8\. Auswählen Sie **„Fertig“,** um den Knoten **„Decision-Split“** zu speichern.

![Zwei Pfade in einem Decision-Split für jedes E-Mail-Template.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Fügen Sie für jede Decision-Split eine E-Mail hinzu:**

1. Ziehen Sie einen **E-Mail**-Knoten in jeden Pfad des **Decision-Split**.
2. Wählen Sie **„E-Mail“** und anschließend das entsprechende Template aus, das in jeden Pfad eingefügt werden soll (d. h. das Template mit dem ID-Wert sollte mit der Logik in Ihrem Decision-Split übereinstimmen).

![Ein E-Mail-Knoten wurde zur Customer Journey hinzugefügt.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Schritt 3: Die Reise aktivieren

Nachdem Sie Ihre Journey eingerichtet haben, aktivieren Sie diese bitte und teilen Sie dem BrazeAI Decisioning Studio™ Go-Team die folgenden Details mit:

* Reise-ID
* Name der Reise
* API-Ereignisdefinitionsschlüssel
* Empfehlungen zur Erweiterung der Daten um einen externen Schlüssel

{% alert note %}
Das BrazeAI Decisioning Studio™ Go-Portal zeigt Ihnen die von SFMC bereitgestellte Automatisierung, mit der einmal täglich die Daten zu Abonnent:innen und Engagement exportiert werden. Wenn Sie diese Automatisierung in SFMC öffnen, stellen Sie bitte sicher, dass Sie die Pause beenden und sie wieder live schalten.
{% endalert %}

1. Bitte kopieren Sie im BrazeAI Decisioning Studio™ Go-Portal den **Namen der Customer Journey**.
2. Fügen Sie anschließend im Salesforce Marketing Cloud Journey Builder den Namen der Journey in die Suchleiste ein.
3. Bitte wählen Sie den Namen der Reise aus. Bitte beachten Sie, dass sich die Reise derzeit im Entwurfsstadium befindet.
4. Bitte wählen Sie **„Validieren**“.

![Die abgeschlossene Reise zur Aktivierung.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. Überprüfen Sie anschließend die Validierungsergebnisse und wählen Sie **„Aktivieren**“.

![Empfehlungen sind im Abschnitt „Validierungsregeln“ aufgeführt.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. Wählen Sie in der Zusammenfassung **„Reise aktivieren**“ erneut **„Aktivieren**“.

![Zusammenfassung der Reise.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Jetzt können Sie loslegen! Sie können nun damit beginnen, Sendungen über BrazeAI Decisioning Studio™ Go zu triggern.

{% endtab %}
{% tab Klaviyo %}

## Einrichtung der Klaviyo-Integration

Um Decisioning Studio Go in Klaviyo zu integrieren, richten Sie einen API-Schlüssel ein, erstellen Sie ein Platzhalter-Template und entwickeln Sie einen Ablauf zur Verarbeitung ausgelöster Sendungen.

### Teil 1: Klaviyo-API-Schlüssel einrichten

1. Bitte gehen Sie in Klaviyo zu **„Einstellungen“** > **„API-Schlüssel**“.
2. Bitte wählen Sie **„Privaten API-Schlüssel auswählen**“.
3. Geben Sie einen Namen für den API-Schlüssel ein. Ein Beispiel hierfür sind „Entscheidungsträger im Experimentierstudio“.
4. Bitte wählen Sie die folgenden Berechtigungen für den API-Schlüssel aus:
    - Kampagnen: Lesezugriff
    - Datenschutz: Vollzugriff
    - Veranstaltungen: Vollzugriff
    - Ströme: Vollzugriff
    - Bilder: Lesezugriff
    - Liste: Vollzugriff
    - Metriken: Vollzugriff
    - Profil: Vollzugriff
    - Segmente: Lesezugriff
    - Vorlagen: Vollzugriff
    - Webhooks: Lesezugriff

![Ein Klaviyo-API-Schlüssel mit ausgewählten Berechtigungen.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Wählen Sie **Erstellen**.
6\. Bitte kopieren Sie diesen API-Schlüssel und fügen Sie ihn in das BrazeAI Decisioning Studio™ Go-Portal ein, wenn Sie dazu aufgefordert werden.

### Teil 2: Erstellen Sie ein Platzhalter-Template in Klaviyo.

BrazeAI Decisioning Studio™ Go importiert Templates, die mit bestehenden Abläufen in Ihrem Klaviyo-Konto verknüpft sind. Um ein Template zu verwenden, das mit keinem Ablauf verknüpft ist, können Sie einen Platzhalterablauf erstellen, der die gewünschten Templates enthält. Der Ablauf kann als Entwurf verbleiben; er muss nicht veröffentlicht werden.

{% alert note %}
Der Zweck dieses Platzhalter-Ablaufs besteht darin, die von Ihnen gewünschten Inhalte in BrazeAI Decisioning Studio™ Go zu importieren. Sie müssen in einem späteren Schritt einen separaten Ablauf erstellen, den BrazeAI Decisioning Studio™ Go verwendet, um Aktivierungen zu triggern, sobald Ihr Experimentator live ist.
{% endalert %}

**Schritt 1: Richten Sie Ihren Ablauf ein**

1. Wählen Sie in Klaviyo **„Flows“** aus.
2. Auswählen Sie **„Flow erstellen“** > **„Von Grund auf neu erstellen**“.
3. Bitte geben Sie dem Platzhalter „Flow“ einen aussagekräftigen Namen und wählen Sie anschließend **„Flow erstellen**“.

![Ein Flow mit dem Namen „OFE-Platzhalter-Flow“.]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Bitte wählen Sie einen beliebigen Auslöser aus und speichern Sie anschließend den Ablauf.
5\. Bitte wählen Sie **„Bestätigen und speichern**“.

**Schritt 2: Erstellen Sie das Platzhalter-Template.**

1. Ziehen Sie einen **E-Mail**-Knoten per Drag-and-Drop hinter den **Trigger**.

![Ein Ablauf mit einem Trigger-Knoten, gefolgt von einem E-Mail-Knoten.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. Wählen Sie im Knoten **„E-Mail“** **die Option „Template auswählen“** aus.
3\. Wählen Sie anschließend das gewünschte Template aus und wählen Sie **„Template verwenden**“.
4\. Bitte wählen Sie **„Speichern“** > **„Fertig**“.
5\. (Optional) Um weitere Templates hinzuzufügen, die in BrazeAI Decisioning Studio™ Go verwendet werden sollen, fügen Sie einen weiteren Knoten **für E-Mails** hinzu und wiederholen Sie die Schritte 2 bis 4.
6\. Bitte belassen Sie alle E-Mails im Entwurfsmodus und verlassen Sie den Flow.

Im BrazeAI Decisioning Studio™ Go-Portal sollten Ihre Templates unter Ihrem Platzhalter-Flow ausgewählt werden können.

![Ein Beispiel für ein Platzhalter-Template von Klaviyo im Decisioning Studio Go-Portal.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

### Teil 3: Erstellen Sie einen Ablauf in Klaviyo

{% alert important %}
Für jeden neuen Experimentator, den Sie einrichten, müssen Sie in Klaviyo einen neuen Ablauf erstellen. Wenn Sie zuvor einen Platzhalter-Flow zum Importieren Ihrer Templates erstellt haben, müssen Sie einen neuen Flow erstellen und können den vorherigen Platzhalter-Flow nicht wiederverwenden.
{% endalert %}

Bevor Sie einen Ablauf in Klaviyo erstellen, müssen Sie die folgenden Angaben aus Ihrem BrazeAI Decisioning Studio™ Go-Portal referenzieren:

- Flussname
- Name des Ereignisses, das triggert

#### Schritt 1: Richten Sie den Ablauf ein

1. Wählen Sie in Klaviyo **„Flows“** > **„Flow erstellen**“.
2. Auswählen Sie **„Selbst zusammenstellen**“.
3. Geben Sie unter **„Name**“ den Namen des Ablaufs aus Ihrem BrazeAI Decisioning Studio™ Go-Portal ein. Wählen Sie anschließend **„Manuell erstellen**“.

![Die Option „Manuell erstellen“ wurde für einen Beispielablauf ausgewählt.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Bitte wählen Sie den Auslöser aus.
5\. Ordnen Sie den Namen einer Metrik dem Namen eines Trigger-Ereignisses aus Ihrem BrazeAI Decisioning Studio™ Go-Portal zu.

![Ein Beispiel für einen Metriknamen, der mit dem Namen des Auslöseereignisses"OFE_TEST_CASE_API_EVENT_TRIGGER".]({%image_buster/assets/img/decisioning_studio_go/flow2.png übereinstimmt    %})

{: start="6"}
6\. Wählen Sie **Speichern**.

{% alert note %}
Wenn Ihr Experimentator über ein Template verfügt, fahren Sie bitte mit Schritt 2 fort. Wenn Ihr Experimentator über zwei oder mehr Templates verfügt, fahren Sie bitte mit [Schritt 3 fort: Fügen Sie Ihrem Ablauf eine ](#step-3-add-a-trigger-split-to-your-flow)Trigger-Aufteilung hinzu.
{% endalert %}

#### Schritt 2: Fügen Sie eine E-Mail zu Ihrem Ablauf hinzu (einzelnes Template)

1. Ziehen Sie einen **E-Mail**-Knoten per Drag-and-Drop hinter den **Trigger**-Knoten.
2. Wählen Sie in den **E-Mail-Details** **die Option „Template auswählen“** aus.

![Option „Template auswählen“ im Abschnitt „E-Mail-Details“.]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Bitte suchen und auswählen Sie Ihre Basis-Template. Sie können Ihr Template anhand des Template-Namens im Abschnitt **„Zu verwendende Ressourcen“** des BrazeAI Decisioning Studio™ Go-Portals suchen.

![Ein Beispiel-Template in Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Auswählen **„Template verwenden“** > **„Speichern**“.
5\. Bitte geben Sie in die **Betreffzeile **„“ ein{% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. Geben Sie für **den Namen des Absenders** und **die Absender-E-Mail-Adresse** die gewünschten Angaben ein.

![Beispiel für Betreffzeile, Absendername und Absender-E-Mail-Adresse für „E-Mail 1”.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Wählen Sie **Erledigt**.
8\. Deaktivieren Sie das Kontrollkästchen **„Zuletzt per E-Mail versendete Profile überspringen**“ und wählen Sie anschließend **„Speichern**“.
9\. Bitte führen Sie im E-Mail-Knoten ein Update durch und ändern Sie den Modus von **„Entwurf“** in **„Live**“.

![Der Klaviyo-Flow-Editor zeigt einen Trigger-Knoten, der mit einem E-Mail-Knoten verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

Jetzt können Sie loslegen! Sie können nun Aktivierungen über BrazeAI Decisioning Studio™ Go triggern.

#### Schritt 3: Fügen Sie Ihrem Ablauf eine Trigger-Aufteilung hinzu (mehrere Templates)

1. Ziehen Sie einen **Trigger-Split**-Knoten per Drag-and-Drop hinter den **Trigger-Knoten**.
2. Wählen Sie den Knoten **„Trigger split“** aus und legen Sie die **Dimension** auf **„EmailTemplateID“** fest.

![Klaviyo-Flussdiagramm, das einen Trigger-Knoten zeigt, der einen Trigger-Split speist, der mit der Dimension „EmailTemplateID“ konfiguriert ist.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

**Bitte fügen Sie Ihr E-Mail-Template hinzu:**

1. Bitte suchen Sie im BrazeAI Decisioning Studio™ Go-Portal die **ID** für** das** **Template** für Ihre erste Vorlage im Abschnitt **„Zu verwendende Ressourcen**“. Geben Sie die **ID des Templates** für das Feld **„Dimension“** ein und wählen Sie anschließend **„Auswählen**“.
2. Ziehen Sie einen **E-Mail**-Knoten per Drag-and-Drop auf den Zweig **„Ja“** der **Trigger-Aufteilung**.

![Ein Klaviyo-Flow mit einem Trigger-Split-Knoten, der einen Ja-Zweig hat, der zu einem E-Mail-Knoten führt, und einen Nein-Zweig, der mit einem weiteren Trigger-Split verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. Wählen Sie in den **E-Mail-Details** **die Option „Template auswählen“** aus.
4\. Bitte suchen und auswählen Sie Ihre Basis-Template. Sie können Ihr Template anhand des Basisvorlagennamens im Abschnitt **„Zu verwendende Ressourcen“** des BrazeAI Decisioning Studio™ Go-Portals suchen.
5\. Auswählen **„Template verwenden“** > **„Speichern**“.
6\. Bitte geben Sie in die **Betreffzeile **„“ ein{% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. Geben Sie für **den Namen des Absenders** und **die Absender-E-Mail-Adresse** die gewünschten Angaben ein.

![Ein ausgewähltes Template für E-Mails sowie Felder für die Betreffzeile, den Namen des Absenders und die E-Mail-Adresse des Absenders.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Wählen Sie **Erledigt**.
9\. Deaktivieren Sie das Kontrollkästchen **„Zuletzt per E-Mail versendete Profile überspringen**“ und wählen Sie anschließend **„Speichern**“.
10\. Bitte führen Sie im E-Mail-Knoten ein Update durch und ändern Sie den Modus von **„Entwurf“** in **„Live**“.

**Fügen Sie für jedes zusätzliche Template einen neuen Trigger-Split hinzu:**

1. Ziehen Sie einen weiteren **Trigger-Split**-Knoten per Drag-and-Drop in den Zweig **„No“** des vorherigen **Trigger-Split**-Knotens.
2. Legen Sie die **Dimension** auf **„EmailTemplateID“** fest und geben Sie als **D**imensionswert die **ID** der** E-Mail-Vorlage** der Basisvorlage ein, die Sie einrichten.
3. Wählen Sie **Speichern**.

![Diagramm eines Klaviyo-Flow-Editors, das einen Trigger-Knoten zeigt, der zu einer Trigger-Aufteilung führt. Die Trigger-Aufteilung verfügt über einen Ja-Zweig, der zu einem E-Mail-Knoten führt, und einen Nein-Zweig, der mit einer weiteren Trigger-Aufteilung verbunden ist, die zu zusätzlichen E-Mail-Knoten führt.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Ziehen Sie einen **E-Mail**-Knoten per Drag-and-Drop in den **Ja**-Zweig Ihrer neuen Trigger-Aufteilung.
5\. Bitte wiederholen Sie die oben genannten Schritte zur Einrichtung des Templates für E-Mails, um das entsprechende Template auszuwählen.
6\. Setzen Sie die **Betreffzeile** auf {% raw %}`{{event.SubjectLine}}`{% endraw %}und deaktivieren Sie das Kontrollkästchen **„Zuletzt per E-Mail versendete Profile überspringen**“.
7\. Wiederholen Sie diesen Vorgang, bis Sie für jedes Basis-Template, das Ihr Experimentator verwendet, einen **Trigger-Split**-Knoten und einen Knoten **für E-Mails** haben. Ihr letzter Trigger-Split sollte im Branch „Nein“ keine Einträge enthalten.

![Ein Klaviyo-Flow mit mehreren Trigger-Split-Knoten, die zu mehreren E-Mail-Knoten verzweigen.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="8"}
8\. Bitte führen Sie in jedem Ihrer **E-Mail**-Knoten ein Update durch, um den Modus von **„Entwurf“** in **„Live“** zu ändern.

![Die Option zum Update des Knotenstatus auf „Live“.]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

Jetzt können Sie loslegen! Sie können nun Aktivierungen über BrazeAI Decisioning Studio™ Go triggern.

{% endtab %}
{% endtabs %}

## Nächste Schritte

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit der Gestaltung Ihres Agenten fort:

- [Agenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
