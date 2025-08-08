---
nav_title: LinkedIn
article_title: Canvas Zielgruppen Synchronisierung mit LinkedIn
alias: /linkedin_audience_sync/
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Braze Audience Sync auf LinkedIn verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
Tool:
  - Canvas
page_order: 4

---

# Zielgruppen-Synchronisierung mit LinkedIn

Mit der Braze Audience Sync to LinkedIn können Marken Nutzerdaten aus ihrer Braze-Integration zu LinkedIn-Kundenlisten hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, kann jetzt eine Anzeige an diesen Benutzer in Ihren LinkedIn-Kundenlisten triggern.

**Zu den häufigen Anwendungsfällen für Audience Syncing gehören**:

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit LinkedIn geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Richtlinie zum Datenschutz](https://www.braze.com/privacy).

{% alert important %}
Audience Sync to LinkedIn befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze-Konto Manager:in, wenn Sie an der Beta teilnehmen möchten.
{% endalert %}

## Voraussetzungen

Sie müssen sicherstellen, dass Sie die folgenden Artikel erstellt, abgeschlossen oder akzeptiert haben, bevor Sie Ihren LinkedIn Audience Sync-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| LinkedIn Anzeigenkonto | [LinkedIn](https://www.linkedin.com/campaignmanager) | Ein aktives LinkedIn-Anzeigenkonto, das mit Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Sie alle relevanten LinkedIn-Bedingungen für den Zugriff und die Nutzung dieses Kontos akzeptiert haben und dass Ihr LinkedIn-Administrator Ihnen die entsprechenden Berechtigungen zur Verwaltung von Zielgruppen erteilt hat. |
| LinkedIn Bedingungen und Richtlinien | LinkedIn | Sie erklären sich damit einverstanden, alle von LinkedIn geforderten Bedingungen, Richtlinien und Dokumentationen in Bezug auf Ihre Nutzung von LinkedIn Audience Sync einzuhalten, einschließlich aller darin referenzierten Bedingungen, Richtlinien und Dokumentationen, zu denen auch die von LinkedIn gehören können: Bedingungen für Serviceleistungen; Dienste, Anzeigenvereinbarung, Datenverarbeitungsvereinbarung und Richtlinien der Professional Community. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Mit LinkedIn verbinden

Gehen Sie im Braze-Dashboard zu **Technologiepartner** und wählen Sie **LinkedIn** aus. Wählen Sie im Bereich **LinkedIn Audience Sync** die Option **LinkedIn verbinden** aus.

![Die LinkedIn Technologieseite in Braze enthält eine Übersicht und einen Abschnitt LinkedIn Audience Sync mit dem Button Connected LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Sie werden dann auf die LinkedIn OAuth-Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync Integration zu autorisieren. Nachdem Sie **Bestätigen** gewählt haben, werden Sie wieder zu Braze zurückgeleitet, um auszuwählen, mit welchen LinkedIn-Anzeigenkonten Sie synchronisieren möchten. 

!["Braze Self Service" ist als das zu verbindende Anzeigenkonto ausgewählt.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Sobald Sie sich erfolgreich verbunden haben, werden Sie auf die Partnerseite zurückgebracht, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Ein erfolgreich verbundenes LinkedIn-Konto.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Ihre LinkedIn-Verbindung wird auf der Ebene des Braze Workspace angewendet. Wenn Ihr LinkedIn-Administrator Sie aus Ihrem LinkedIn-Anzeigenkonto entfernt, erkennt Braze ein ungültiges Token. Dies hat zur Folge, dass Ihre aktiven Canvase, die LinkedIn verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### Schritt 2: Konfigurieren Sie Ihre Canvas Eingangskriterien

Beim Aufbau von Zielgruppen für das Ad Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z.B. das Recht "Nicht verkaufen oder weitergeben" gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen. 

Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection) erfasst haben, können Sie den Filter **Ads Tracking Enablement** verwenden. Wählen Sie den Wert `true` aus, um Nutzer:innen nur in Zielgruppen zu schicken, für die sie ein Opt-in gesetzt haben. 

![Ein Eingang Zielgruppe mit dem Filter "Ad Tracking Enablement ist wahr".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute sammeln, sollten Sie diese in Ihre Canvas-Eingangskriterien als Filter einbeziehen:

![Ein Canvas mit einem Eingang Zielgruppe "opted_in_marketing" ist gleich "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance/).

### Schritt 3: Fügen Sie einen Schritt zur Synchronisierung der Zielgruppe mit LinkedIn hinzu

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie Audience Sync. Klicken Sie auf den Button **Angepasste Zielgruppe**, um den Komponenteneditor zu öffnen.

![Der Canvas Editor mit der Liste der verfügbaren Komponenten.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![Die ausgewählte Audience Sync Komponente.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Schritt 4: Sync-Einrichtung

Wählen Sie **LinkedIn** als den gewünschten Audience Sync Partner aus.

![Die Details zu "Audience Sync einrichten" mit den verschiedenen Partnern, aus denen Sie wählen können.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Wählen Sie dann das gewünschte LinkedIn-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

![Synchronisierung der Zielgruppe mit LinkedIn, wobei Braze als Anzeigenkonto ausgewählt ist.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer:innen zur Zielgruppe hinzufügen** und wählen Sie aus, welche Felder Sie mit LinkedIn synchronisieren möchten. Für diese Integration unterstützen wir derzeit Folgendes: 
- E-Mail
- Vor- und Nachname
- Android-GAID

Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Zielgruppe erstellen** klicken.

![Ein Beispiel für eine "Leads"-Zielgruppe mit dem ausgewählten Braze-Konto, der "Leads"-Zielgruppe, der Aktion zum Hinzufügen von Nutzer:innen zur Zielgruppe und E-Mail, Android GAID sowie Vor- und Nachname als abzugleichende Felder.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe auch referenzieren, um sie später in Canvas zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Bestätigung, dass die Zielgruppe "Leads" erstellt wurde.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie die Audience Sync Komponente betreten.

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}

**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden LinkedIn Zielgruppen hinzuzufügen, um zu bestätigen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie hinzu**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

Sobald Sie Ihre Audience Sync auf LinkedIn konfiguriert haben, starten Sie einfach das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Schritt Audience Sync durchlaufen, werden in diese Zielgruppe auf LinkedIn weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangehen.

Sie können die Zielgruppen auf LinkedIn einsehen, indem Sie in Ihr Anzeigenkonto gehen und **Zielgruppen** unter dem Abschnitt **Assets** in der Navigation auswählen. Auf der Seite **Zielgruppen** können Sie sehen, wie groß die einzelnen Zielgruppen sind, wenn sie mehr als 300 Mitglieder erreicht haben.

![LinkedIn-Seite mit den folgenden Metriken für die angegebene Zielgruppe.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, wird Braze diese Nutzer:innen nahezu in Realtime synchronisieren und dabei die Rate-Limits der LinkedIn API beachten. In der Praxis wird Braze versuchen, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese an LinkedIn weitergeleitet werden.

LinkedIns API Rate-Limits besagen, dass nicht mehr als zehn Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage möglich sind. Erreicht eine Braze-Kund:in dieses Rate-Limit, wird Braze-Canvas die Synchronisierung für bis zu 13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt.

## Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| METRIC | BESCHREIBUNG |
| ------ | ----------- | 
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente eingegeben haben, die mit LinkedIn synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Wie viele Nutzer:innen haben den Fortschritt zur nächsten Komponente vorangetrieben, falls es eine solche gibt? Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit LinkedIn synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit LinkedIn bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden nicht mit LinkedIn synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges LinkedIn Token sein oder wenn die Zielgruppe auf LinkedIn gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es bei den Metriken Nutzer:innen synchronisiert und Nutzer:innen fehlerhaft aufgrund des Bulk Flush und der 13-stündigen Wiederholung zu einer Verzögerung bei der Berichterstattung kommt.
{% endalert %}

{% alert important %}
LinkedIn bietet zusätzliche Metriken zu den Trefferquoten auf seiner Plattform. Um die Übereinstimmung Ihrer spezifischen Zielgruppe zu überprüfen, wählen Sie die Metriken des Audience Sync-Schrittes aus, um die Seite **Canvas-Schritt-Details** aufzurufen.
<br><br>
Wählen Sie als Partner **LinkedIn**, Ihr Anzeigenkonto und die Zielgruppe aus, um die Größe der Zielgruppe und die Trefferquote von LinkedIn zu sehen.

![Ein Beispiel für die Metriken der Audience Sync-Schritte mit 10.000 eingegebenen Nutzer:innen.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Häufig gestellte Fragen

### Wie lange dauert es, bis die Zielgruppengrößen in LinkedIn angezeigt werden?

Es kann bis zu 48 Stunden dauern, bis Sie die Zielgruppen in Ihrem LinkedIn-Konto einsehen können.

### Wie groß muss die Zielgruppe mindestens sein, damit LinkedIn sie in Ihrem Anzeigenkonto auffüllt?

Die Zielgruppe muss mindestens 300 Mitglieder umfassen, um die Größe der Zielgruppe in Ihrem LinkedIn-Konto aufzufüllen.

### Was sollte ich als nächstes tun, wenn ich den Fehler eines ungültigen Tokens erhalte?

Sie können die Verbindung zu Ihrem LinkedIn-Konto auf der LinkedIn Partnerseite trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem LinkedIn-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.

### Warum ist es nicht zulässig, meinen Canvas zu starten?

Bestätigen Sie, dass Ihr LinkedIn-Anzeigenkonto erfolgreich mit Braze auf der LinkedIn Partnerseite verbunden wurde. Vergewissern Sie sich als nächstes, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und die passenden Felder ausgewählt haben.

### Woher weiß ich, ob Nutzer:innen übereinstimmen, nachdem ich Nutzer:innen an LinkedIn weitergegeben habe?

LinkedIn bietet in seinem Dashboard Informationen zu den Trefferquoten. Sie können sie auf LinkedIn unter der Rubrik **Zielgruppen** einsehen. Sie können die Trefferquote für Ihre LinkedIn Zielgruppe in den Canvas-Schritt-Details Ihres Audience Sync-Schrittes überprüfen.

### Wie viele Zielgruppen kann LinkedIn unterstützen?

Derzeit gibt es keine Begrenzung für die Anzahl der Zielgruppen in Ihrem LinkedIn-Anzeigenkonto.

### Warum bleibt ein Segment im Status GEBÄUDE stecken und wird nicht aktualisiert?

Ein Segment gilt als ungenutzt und wird auf ARCHIVIERT gesetzt, wenn es 30 Tage lang nicht kontinuierlich in einer Entwurfs- oder aktiven Kampagne verwendet wurde. Aus diesem Grund kann es vorkommen, dass ein Segment im Zustand BUILDING "feststeckt", wenn Updates zu einem ARCHIVIERTEN Segment gestreamt werden, wodurch es in den Zustand BUILDING gepusht wird, und kurz bevor es wieder archiviert wird, neue Updates zu dem unbenutzten Segment gestreamt werden.


