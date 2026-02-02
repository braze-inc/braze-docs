---
nav_title: Konfigurieren Sie mit Salesforce Marketing Cloud
article_title: Konfigurieren Sie mit Salesforce Marketing Cloud für BrazeAI Decisioning Studio Go
page_order: 5
description: "Erfahren Sie, wie Sie eine Automatisierung von Datenabfragen und eine Journey in Salesforce Marketing Cloud für die Verwendung mit BrazeAI Decisioning <sup>StudioTM</sup> Go einrichten."
toc_headers: h2
---

# Konfigurieren Sie mit Salesforce Marketing Cloud für BrazeAI Decisioning Studio™ Go

> Richten Sie in der Salesforce Marketing Cloud (SFMC) eine Journey ein, um mit dem Triggern von Sendungen durch BrazeAI Decisioning Studio™ Go zu beginnen.

## Einrichten einer Automatisierung der Datenabfrage

### Schritt 1: Erstellen Sie eine neue Automatisierung

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

![Ein Beispiel für einen Zeitplan, der für den 25\. Januar 2024 um 12 Uhr ET festgelegt wurde und täglich wiederholt werden soll.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

### Schritt 2: Erstellen Sie Ihre SQL-Anfragen

Als nächstes erstellen wir 2 SQL-Anfragen: eine Abfrage für Abonnenten:innen und eine Abfrage für das Engagement. Diese Abfragen erlauben es BrazeAI Decisioning Studio™ Go, Daten abzurufen, um die Zielgruppe zu füllen und Engagement-Ereignisse aufzunehmen.

{% tabs %}
{% tab Subscribers query %}
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
8\. Suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go Portal im Abschnitt **Zu verwendende Ressourcen** den externen Schlüssel der Zieldatenerweiterung. Fügen Sie ihn dann in die Suchleiste ein, um zu suchen.

![Ein externer Schlüssel, der in die Suchleiste eingefügt wird]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Wählen Sie die Datenerweiterung aus, die mit dem gesuchten externen Schlüssel übereinstimmt. Der Name der Targeting-Datenerweiterung wird auch in Ihrem BrazeAI Decisioning Studio™ Go-Portal als Querverweis bereitgestellt. Die **Datenerweiterung** für die Abonnent:in-Abfrage sollte mit einem `BASE_AUDIENCE_DATA` Suffix enden.

![Der Name der Datenerweiterung, die dem externen Schlüssel des Beispiels entspricht.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Wählen Sie **Überschreiben** und dann **Weiter**.
{% endtab %}
{% tab Engagement query %}
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
Der Name der Targeting-Datenerweiterung wird auch in Ihrem BrazeAI Decisioning Studio™ Go-Portal als Querverweis bereitgestellt.  Vergewissern Sie sich, dass Sie die Ziel-Datenerweiterung für die Engagement-Abfrage betrachten. Die **Datenerweiterung** für die Abfrage des Engagements sollte mit einem Suffix ENGAGEMENT_DATA enden.
{% endalert %}

{: start="9"}
9\. Wählen Sie **Überschreiben** und dann **Weiter**.

![Der Name der Datenerweiterung, die dem externen Schlüssel des Beispiels entspricht.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### Schritt 3: Starten Sie die Automatisierung

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

## Erstellen Sie Ihre SFMC-Reise

### Schritt 1: Die Reise einrichten

1. Gehen Sie in Salesforce Marketing Cloud zu **Journey Builder** > **Journey Builder**.
2. Wählen Sie **Neue Reise erstellen**.
3. Wählen Sie für Ihre Reiseart **Mehrstufige Reise** und wählen Sie dann **Erstellen**.

![Eine API-Eingangsquelle, die mit einem Decision-Split-Knoten und mehreren E-Mail-Knoten verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### Schritt 2: Bauen Sie die Reise

#### Schritt 2.1: Eine Eingangsquelle erstellen

1. Ziehen Sie **API Event** als Eingangsquelle in den Journey Builder.

!["API Event" als Eingangsquelle ausgewählt.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. Wählen Sie im **API-Ereignis** die Option **Ein Ereignis erstellen**.

![Die Option "Ein Ereignis erstellen" in der API Ereignis.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Wählen Sie **Datenerweiterung auswählen**. Suchen Sie die Datenerweiterung, in die BrazeAI Decisioning Studio™ Go Empfehlungen schreiben wird, und wählen Sie sie aus.
4\. Wählen Sie **Zusammenfassung**, um Ihre Änderungen zu speichern.
5\. Wählen Sie **Fertig**, um das API-Ereignis zu speichern.

![Zusammenfassung der API-Ereignisse.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### Schritt 2.2: Decision-Split hinzufügen

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

#### Schritt 2.3: Fügen Sie eine E-Mail für jeden Decision-Split hinzu

1. Ziehen Sie einen Knoten **E-Mail** in jeden Pfad des **Decision-Splits**.
2. Wählen Sie **E-Mail** und wählen Sie dann die entsprechende Vorlage aus, die in jeden Pfad eingefügt werden soll (d.h. die Vorlage mit dem ID-Wert sollte der Logik in Ihrem Decision-Split entsprechen).

![Ein E-Mail-Knotenpunkt wurde der Journey hinzugefügt.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### Schritt 3: Aktivieren Sie die Reise

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
