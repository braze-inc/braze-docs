---
nav_title: LinkedIn
article_title: Canvas Audience Sync mit LinkedIn
alias: /linkedin_audience_sync/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync auf LinkedIn verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
Tool:
  - Canvas
page_order: 4

---

# Audience Sync mit LinkedIn

Mit der Braze Audience Sync to LinkedIn können Marken Benutzerdaten aus ihrer Braze-Integration zu LinkedIn-Kundenlisten hinzufügen, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu liefern. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze Canvas auf der Grundlage Ihrer Benutzerdaten verwenden würden, kann jetzt eine Anzeige für diesen Benutzer in Ihren LinkedIn-Kundenlisten auslösen.

**Häufige Anwendungsfälle für Audience Syncing sind**:

- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut ansprechen
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind

Mit dieser Funktion können Marken kontrollieren, welche spezifischen Erstanbieterdaten mit LinkedIn geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
Audience Sync to LinkedIn befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Beta teilnehmen möchten.
{% endalert %}

## Voraussetzungen

Sie müssen sicherstellen, dass Sie die folgenden Elemente erstellt, abgeschlossen oder akzeptiert haben, bevor Sie Ihren LinkedIn Audience Sync-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| LinkedIn Anzeigenkonto | [LinkedIn](https://www.linkedin.com/campaignmanager) | Ein aktives LinkedIn-Anzeigenkonto, das mit Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Sie alle relevanten LinkedIn-Bedingungen für den Zugriff und die Nutzung dieses Kontos akzeptiert haben und dass Ihr LinkedIn-Administrator Ihnen die entsprechenden Berechtigungen für die Verwaltung von Audiences erteilt hat. |
| LinkedIn Bedingungen und Richtlinien | LinkedIn | Sie erklären sich damit einverstanden, alle von LinkedIn geforderten Bedingungen, Richtlinien und Dokumentationen in Bezug auf Ihre Nutzung von LinkedIn Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird und zu denen auch die von LinkedIn gehören können: Dienstleistungsbedingungen, Anzeigenvereinbarung, Datenverarbeitungsvereinbarung und Richtlinien der professionellen Gemeinschaft. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Mit LinkedIn verbinden

Gehen Sie im Dashboard von Braze zu **Technologiepartner** und wählen Sie **LinkedIn**. Wählen Sie im Bereich **LinkedIn Audience Sync** die Option **LinkedIn verbinden**.

![Die LinkedIn Technologieseite in Braze enthält einen Abschnitt Übersicht und einen Abschnitt LinkedIn Audience Sync mit der Schaltfläche Verbundenes LinkedIn.][3]{: style="max-width:75%;"}

Sie werden dann auf die LinkedIn OAuth-Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync-Integration zu autorisieren. Nachdem Sie **Bestätigen** gewählt haben, werden Sie wieder zu Braze zurückgeleitet, um auszuwählen, mit welchen LinkedIn-Anzeigenkonten Sie synchronisieren möchten. 

!["Braze Self Service" ist als Anzeigenkonto für die Verbindung ausgewählt.][7]{: style="max-width:75%;"}

Sobald Sie sich erfolgreich verbunden haben, werden Sie zur Partnerseite zurückgebracht, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Ein erfolgreich verbundenes LinkedIn-Konto.][6]{: style="max-width:75%;"}

Ihre LinkedIn-Verbindung wird auf der Ebene des Braze-Arbeitsbereichs angewendet. Wenn Ihr LinkedIn-Administrator Sie aus Ihrem LinkedIn-Anzeigenkonto entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die LinkedIn verwenden, Fehler anzeigen, und Braze kann die Benutzer nicht synchronisieren.

### Schritt 2: Konfigurieren Sie Ihre Canvas-Eingabekriterien

Wenn Sie Zielgruppen für das Ad Tracking aufbauen, möchten Sie vielleicht bestimmte Nutzer auf der Grundlage ihrer Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z. B. das Recht "Nicht verkaufen oder weitergeben" gemäß [CCPA](https://oag.ca.gov/privacy/ccpa). Vermarkter sollten die entsprechenden Filter für die Eignung der Nutzer in ihre Canvas-Eingabekriterien integrieren. Nachfolgend finden Sie einige Optionen. 

Wenn Sie die [iOS IDFA über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection) gesammelt haben, können Sie den Filter " **Ads Tracking Enabled** " verwenden. Wählen Sie den Wert `true`, um Benutzer nur an Audience Sync-Ziele zu senden, für die sie sich angemeldet haben. 

![Ein Eintrag Publikum mit dem Filter "Ad Tracking Enabled is true".][5]{: style="max-width:75%;"}

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante benutzerdefinierte Attribute sammeln, sollten Sie diese als Filter in Ihre Canvas-Eingabekriterien aufnehmen:

![Ein Canvas mit einem Eintrag Publikum von "opted_in_marketing" ist gleich "true".][4]{: style="max-width:75%;"}

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance/).

### Schritt 3: Fügen Sie einen Schritt zur Publikums-Synchronisierung mit LinkedIn hinzu

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie Audience Sync. Klicken Sie auf die Schaltfläche **Benutzerdefinierte Audience**, um den Komponenteneditor zu öffnen.

![Der Canvas-Editor mit der Liste der verfügbaren Komponenten.][2]{: style="max-width:35%;"} ![Die ausgewählte Audience Sync-Komponente.][1]{: style="max-width:29%;"}

### Schritt 4: Sync-Einrichtung

Wählen Sie **LinkedIn** als den gewünschten Audience Sync-Partner.

![Die Details zu "Audience Sync einrichten" mit den verschiedenen Partnern, aus denen Sie wählen können.][9]{: style="max-width:70%;"}

Wählen Sie dann das gewünschte LinkedIn-Anzeigenkonto. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

![Audience Sync mit LinkedIn, wobei Braze als Anzeigenkonto ausgewählt ist.][11]

{% tabs %}
{% tab Ein neues Publikum schaffen %}

**Ein neues Publikum schaffen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Benutzer zur Zielgruppe hinzufügen** und wählen Sie die Felder aus, die Sie mit LinkedIn synchronisieren möchten. Für diese Integration unterstützen wir derzeit Folgendes: 
- E-Mail
- Vor- und Nachname
- Android-GAID

Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche **Zielgruppe erstellen** klicken.

![Ein Beispiel für eine "Leads"-Zielgruppe mit dem ausgewählten Braze-Anzeigenkonto, der "Leads"-Zielgruppe, der Aktion zum Hinzufügen von Benutzern zur Zielgruppe und den Feldern E-Mail, Android-GAID sowie Vor- und Nachname, die abgeglichen werden sollen.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auch später in der Canvas-Reise auf diese Zielgruppe verweisen, um sie zu entfernen.

![Bestätigung, dass die Zielgruppe "Leads" erstellt wurde.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Benutzer nahezu in Echtzeit, sobald sie die Komponente Audience Sync betreten.

{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}

**Synchronisieren Sie mit einer bestehenden Zielgruppe**<br>
Braze bietet auch die Möglichkeit, Benutzer zu bestehenden LinkedIn Zielgruppen hinzuzufügen, um zu bestätigen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie der Zielgruppe hinzu**. Braze fügt dann nahezu in Echtzeit Benutzer hinzu, sobald diese die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die vorhandene Zielgruppe ausgewählt.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

Sobald Sie Ihre Audience Sync auf LinkedIn konfiguriert haben, starten Sie einfach die Canvas! Die neue Zielgruppe wird erstellt, und Benutzer, die den Schritt Audience Sync durchlaufen, werden in diese Zielgruppe auf LinkedIn weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Benutzer zum nächsten Schritt in ihrer User Journey übergehen.

Sie können die Zielgruppe auf LinkedIn einsehen, indem Sie in Ihr Anzeigenkonto gehen und unter dem Abschnitt **Assets** in der Navigation die Option **Zielgruppen** auswählen. Auf der Seite **Zielgruppen** können Sie die Größe der einzelnen Zielgruppen sehen, nachdem Sie mehr als 300 Mitglieder erreicht haben.

![LinkedIn-Seite, die die folgenden Metriken für die angegebene Zielgruppe auflistet.][8]

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung

Wenn Benutzer die Audience Sync-Stufe erreichen, wird Braze diese Benutzer nahezu in Echtzeit synchronisieren und dabei die API-Ratenlimits von LinkedIn respektieren. In der Praxis wird Braze versuchen, alle 5 Sekunden so viele Benutzer wie möglich zu verarbeiten, bevor es diese Benutzer an LinkedIn weiterleitet.

Das API-Limit von LinkedIn besagt, dass nicht mehr als zehn Abfragen pro Sekunde und 100.000 Benutzer pro Anfrage möglich sind. Wenn ein Braze-Kunde dieses Limit erreicht, wird Braze the Canvas die Synchronisierung für bis zu 13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

## Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| METRISCH | BESCHREIBUNG |
| ------ | ----------- | 
| Aufgenommen | Anzahl der Benutzer, die diese Komponente eingegeben haben, die mit LinkedIn synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Wie viele Benutzer sind zur nächsten Komponente übergegangen, falls es eine gibt? Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Benutzer, die erfolgreich mit LinkedIn synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit LinkedIn bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Benutzer, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit LinkedIn synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges LinkedIn-Token sein oder wenn die Zielgruppe auf LinkedIn gelöscht wurde. |
| Canvas verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei den Berichten über synchronisierte Benutzer und fehlerhafte Benutzer kommen wird.
{% endalert %}

{% alert important %}
LinkedIn bietet zusätzliche Metriken zu den Trefferquoten auf seiner Plattform. Um die Übereinstimmung Ihrer spezifischen Audience Sync zu überprüfen, wählen Sie die Audience Sync-Schritt-Metriken aus, um die Seite **Canvas-Schritt-Details** aufzurufen.
<br><br>
Wählen Sie als Partner **LinkedIn**, Ihr Anzeigenkonto und die Zielgruppe, um die Größe der Zielgruppe und die Trefferquote von LinkedIn zu sehen.

![Ein Beispiel für Audience Sync-Schrittmetriken mit 10.000 eingegebenen Benutzern.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Fehlersuche

{% details Wie lange wird es dauern, bis die Zielgruppengrößen in LinkedIn angezeigt werden? %}
Es kann bis zu 48 Stunden dauern, bis Sie die Zielgruppen in Ihrem LinkedIn-Konto sehen können.
{% enddetails %}

{% details Wie groß muss die Zielgruppe mindestens sein, damit LinkedIn sie in Ihrem Anzeigenkonto auffüllt?  %}
Die Zielgruppe muss mindestens 300 Mitglieder umfassen, um die Größe der Zielgruppe in Ihrem LinkedIn-Konto aufzufüllen.
{% enddetails %}

{% details Was sollte ich als nächstes tun, wenn ich einen ungültigen Token-Fehler erhalte? %}
Sie können die Verbindung zu Ihrem LinkedIn-Konto auf der LinkedIn-Partnerseite trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem LinkedIn-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.
{% enddetails %}

{% details Warum kann mein Canvas nicht gestartet werden? %}
Bitte bestätigen Sie, dass Ihr LinkedIn-Anzeigenkonto erfolgreich mit Braze auf der LinkedIn-Partnerseite verbunden wurde.
Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben.
{% enddetails %}

{% details Woher weiß ich, ob die Benutzer übereinstimmen, nachdem ich sie an LinkedIn weitergegeben habe? %}
- Woher weiß ich, ob die Benutzer übereinstimmen, nachdem ich sie an LinkedIn weitergegeben habe?
LinkedIn bietet in seinem Dashboard Informationen zu den Trefferquoten. Sie können es auf LinkedIn unter der Rubrik **Audiences** einsehen. 
- Darüber hinaus können Sie die Trefferquote für Ihre LinkedIn Audience auf der Seite Canvas Step Details Ihres Audience Sync-Schritts überprüfen.
{% enddetails %} 

{% details Wie viele Zielgruppen kann LinkedIn unterstützen? %}
Derzeit gibt es keine Begrenzung für die Anzahl der Zielgruppen in Ihrem LinkedIn-Anzeigenkonto.
{% enddetails %}

{% details Warum bleibt ein Segment im Status GEBÄUDE stecken und wird nicht aktualisiert? %}
Ein Segment gilt als ungenutzt und wird auf ARCHIVIERT gesetzt, wenn es 30 Tage lang nicht kontinuierlich in einem Entwurf oder einer aktiven Kampagne verwendet wurde. Aus diesem Grund kann es vorkommen, dass ein Segment im Zustand BUILDING "feststeckt", wenn Aktualisierungen in ein ARCHIVIERTES Segment gestreamt werden, wodurch es in den Zustand BUILDING versetzt wird, und kurz bevor es wieder archiviert wird, neue Aktualisierungen in das unbenutzte Segment gestreamt werden.
{% enddetails %}

[1]: {% image_buster /assets/img/linkedin/linkedin1.png %}
[2]: {% image_buster /assets/img/linkedin/linkedin2.png %}
[3]: {% image_buster /assets/img/linkedin/linkedin3.png %}
[4]: {% image_buster /assets/img/linkedin/linkedin4.png %}
[5]: {% image_buster /assets/img/linkedin/linkedin5.png %}
[6]: {% image_buster /assets/img/linkedin/linkedin6.png %}
[7]: {% image_buster /assets/img/linkedin/linkedin7.png %}
[8]: {% image_buster /assets/img/linkedin/linkedin8.png %}
[9]: {% image_buster /assets/img/linkedin/linkedin.png %}
[11]: {% image_buster /assets/img/linkedin/linkedin20.png %}