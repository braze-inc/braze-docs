---
nav_title: Criteo
article_title: Canvas Zielgruppen Synchronisierung mit Criteo
description: "Dieser Artikel referenziert, wie Sie Braze Audience Sync für Criteo verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
page_order: 1
alias: /audience_sync_criteo/

Tool:
  - Canvas
---

# Zielgruppen-Synchronisation mit Criteo

Mit der Braze Audience Sync to Criteo können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze-Integration zu Criteo-Kundenlisten hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, kann jetzt verwendet werden, um eine Anzeige für diesen Benutzer in Ihren Criteo-Kundenlisten zu triggern.

**Zu den üblichen Anwendungsfällen für die Synchronisierung von Zielgruppen gehören:**

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten
- Erstellen von Lookalike Audiences zur effizienteren Gewinnung neuer Nutzer:innen

Dieses Feature gibt Marken die Möglichkeit zu kontrollieren, welche spezifischen First-Party-Daten mit Criteo geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Richtlinie zum Datenschutz](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to Criteo ist eine Integration von Audience Sync Pro. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze-Konto Manager:in. <br> 
{% endalert %}

## Voraussetzungen 

Sie müssen sicherstellen, dass Sie die folgenden Artikel erstellt und/oder vervollständigt haben, bevor Sie die Synchronisierung Ihrer Zielgruppe mit Criteo einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Criteo Werbekonto | [Criteo](https://marketing.criteo.com/) | Ein aktives Criteo-Anzeigenkonto, das mit Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr Criteo-Administrator Ihnen die entsprechenden Berechtigungen für den Zugriff auf Zielgruppen erteilt hat. |
| [Criteo Werberichtlinien](https://www.criteo.com/advertising-guidelines/)<br>und<br>[Criteo Richtlinien zur Markensicherheit](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Als aktiver Kunde von Criteo müssen Sie sicherstellen, dass Sie die Criteo-Richtlinien für Werbung und Markensicherheit einhalten können, bevor Sie Kampagnen von Criteo starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit Criteo verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Criteo** aus. Wählen Sie unter Criteo Zielgruppen-Export die Option **Criteo verbinden** aus.

![Criteo Technologieseite in Braze, die eine Übersicht und einen Criteo Bereich mit dem Connected Criteo Button enthält.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Es wird eine Criteo oAuth-Seite angezeigt, auf der Sie Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync Integration autorisieren können.

Nachdem Sie bestätigt haben, werden Sie zurück nach Braze geleitet, um die Criteo-Anzeigenkonten auszuwählen, mit denen Sie synchronisieren möchten. 

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Criteo verbinden können.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Nach erfolgreicher Verbindung gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Eine aktualisierte Version der Technologie-Partnerseite von Criteo, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Ihre Criteo-Verbindung wird auf der Ebene des Braze Workspace angewendet. Wenn Ihr Criteo-Administrator Sie aus Ihrem Criteo-Anzeigenkonto entfernt, erkennt Braze ein ungültiges Token. Dies hat zur Folge, dass Ihre aktiven Canvase, die Criteo verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### Schritt 2: Konfigurieren Sie Ihre Canvas Eingangskriterien

Beim Aufbau von Zielgruppen für das Ad Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen einbeziehen oder ausschließen, um Datenschutzgesetze einzuhalten, wie z.B. das Recht "Nicht verkaufen oder weitergeben" gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen.

Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) erfasst haben, können Sie den Filter Ads Tracking Enablement verwenden. Wählen Sie den Wert true aus, um Nutzer:innen nur in Zielgruppen zu schicken, für die sie ein Opt-in gesetzt haben.

![]({% image_buster /assets/img/criteo/criteo11.png %})

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute sammeln, sollten Sie diese in Ihre Canvas-Eingangskriterien als Filter einbeziehen:

![]({% image_buster /assets/img/criteo/criteo12.png %})

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance/).

### Schritt 3: Hinzufügen eines Zielgruppen-Synchronisationsschritts mit Criteo

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![Workflow der vorherigen Schritte zum Hinzufügen einer Criteo Zielgruppen-Komponente in Canvas Flow.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Workflow der vorherigen Schritte zum Hinzufügen einer Criteo Zielgruppen-Komponente in Canvas Flow.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Schritt 4: Sync-Einrichtung

Klicken Sie auf den Button **Angepasste Zielgruppe**, um den Komponenteneditor zu öffnen.

Wählen Sie **Criteo** als den gewünschten Audience Sync Partner aus. 

![]({% image_buster /assets/img/criteo/criteo6.png %})

Wählen Sie dann Ihr gewünschtes Criteo-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}
**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer:innen hinzufügen**, und wählen Sie aus, welche Felder Sie mit Criteo synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Zielgruppe erstellen** klicken.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier wird das gewünschte Anzeigenkonto ausgewählt, und eine neue Zielgruppe wird erstellt.]({% image_buster /assets/img/criteo/criteo3.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe auch referenzieren, um sie später in Canvas zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Eine Meldung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/criteo/criteo1.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie die Audience Sync Komponente betreten.
{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}
**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Zielgruppen von Criteo hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie hinzu**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

Sobald Sie Ihre Zielgruppe mit Criteo synchronisiert haben, starten Sie einfach das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Schritt Audience Sync durchlaufen, werden in diese Zielgruppe auf Criteo weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey voranbringen.

Sie können sich die Zielgruppe in Criteo ansehen, indem Sie in Ihr Ads Manager-Konto gehen und dann Segmente aus der **Bibliothek der Zielgruppe** in der Navigation auswählen. Auf der Seite **Segmente** sehen Sie die Größe der einzelnen Zielgruppen, nachdem sie ~1.000 erreicht haben.

![Die Bibliothek der Zielgruppe mit Segment, ID, Quelle, Typ, Größe, aktueller Verwendung und letztem Update.]({% image_buster /assets/img/criteo/criteo.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen den Schritt Audience Sync erreichen, wird Braze diese Nutzer:innen nahezu in Realtime synchronisieren und dabei die Rate-Limits der Criteo APIs respektieren. In der Praxis bedeutet dies, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese Nutzer:innen an Criteo weitergeleitet werden.

Das Rate-Limits für die API von Criteo besagt, dass nicht mehr als 250 Anfragen pro Minute gestellt werden dürfen. Erreicht eine Braze-Kund:in dieses Rate-Limit, wird Braze-Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt. 

## Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente eingegeben haben, die mit Criteo synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Wie viele Nutzer:innen wurden zur nächsten Komponente vorgebracht, falls es eine gibt. Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Criteo synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Criteo verarbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden nicht mit Criteo synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Criteo Token sein oder wenn die Zielgruppe auf Criteo gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es bei den Metriken Nutzer:innen synchronisiert und Nutzer:innen fehlerhaft aufgrund des Bulk Flush und der 13-stündigen Wiederholung zu einer Verzögerung bei der Berichterstattung kommt.
{% endalert %}

## Häufig gestellte Fragen

### Was sollte ich als nächstes tun, wenn ich den Fehler eines ungültigen Tokens erhalte?
Sie können die Verbindung zu Ihrem Criteo-Konto auf der Partnerseite von Criteo einfach trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Criteo-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.

### Warum ist es nicht zulässig, meinen Canvas zu starten?

Bestätigen Sie auf der Partnerseite von Criteo, dass Ihr Criteo-Anzeigenkonto erfolgreich mit Braze verbunden wurde. Überprüfen Sie als nächstes, ob Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben.

### Woher weiß ich, ob Nutzer:innen übereinstimmen, nachdem ich Nutzer:innen an Criteo weitergegeben habe?

Criteo stellt diese Informationen nicht für seine eigenen Richtlinien zum Datenschutz zur Verfügung.

### Wie viele Zielgruppen kann Criteo unterstützen?

Zurzeit können Sie nur 1.000 Zielgruppen in Ihrem Criteo-Konto haben. Wenn Sie dieses Limit überschreiten, werden Sie von Braze benachrichtigt, dass wir keine neuen Zielgruppen erstellen können. Sie müssen Zielgruppen, die Sie nicht mehr verwenden, aus Ihrem Criteo-Anzeigenkonto entfernen.


