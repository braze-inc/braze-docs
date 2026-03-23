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
| **Braze** | Per API getriggerte Kampagnen | Native Integration, Triggern in Realtime |
| **Salesforce Marketing Cloud** | Journey Builder mit API-Ereignissen | Automatisierung von SQL-Abfragen, Datenerweiterungen |
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

![Ein Beispiel für Automatisierung "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

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
{% endtabs %}

## Nächste Schritte

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit der Gestaltung Ihres Agenten fort:

- [Agenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
