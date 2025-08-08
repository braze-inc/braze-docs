---
nav_title: Snapchat
article_title: Canvas Zielgruppen Synchronisierung mit Snapchat
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Braze Audience Sync für Snapchat verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# Zielgruppen-Synchronisation auf Snapchat

Mit der Braze Audience Sync to Snapchat können Marken Nutzerdaten aus ihrer Braze-Integration zu Snapchat-Kundenlisten hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt verwendet werden, um eine Anzeige für diesen Nutzer in Ihren Snapchat-Kundenlisten zu triggern.

**Zu den üblichen Anwendungsfällen für die Synchronisierung von Zielgruppen gehören:**

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten
- Erstellen ähnlicher Zielgruppen zur effizienteren Gewinnung neuer Nutzer:innen

Mit diesem Feature können Nutzer:innen kontrollieren, welche spezifischen First-Party-Daten mit Snapchat geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Richtlinie zum Datenschutz](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to Snapchat ist eine Integration von Audience Sync Pro. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze-Konto Manager:in.
{% endalert %}

## Voraussetzungen 

Sie müssen sicherstellen, dass die folgenden Artikel erstellt, vervollständigt und/oder akzeptiert wurden, bevor Sie Ihren Snapchat-Zielgruppen-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Snapchat Business Manager:in | Snapchat | Ein zentrales Tool zur Verwaltung der Snapchat-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten, Apps). |
| Snapchat Anzeigenkonto | Snapchat | Ein aktives Snapchat-Anzeigenkonto, das mit dem Snapchat Business Manager Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr Snapchat Business Manager-Admin Ihnen Administratorrechte für die Snapchat-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| Snapchat Bedingungen & Richtlinien | [Snapchat](https://www.snap.com/en-US/policies) | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von Snapchat in Bezug auf Ihre Nutzung von Snapchat Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird, wie z. B. die Allgemeinen Geschäftsbedingungen für Dienste, die Geschäftsbedingungen für Serviceleistungen, die Bedingungen für Entwickler:in, Audience Match, die Richtlinien für Werbung, die Richtlinien für kommerzielle Inhalte, die Richtlinien für die Community und die Verantwortung der Anbieter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit Snapchat verbinden

Gehen Sie auf dem Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Snapchat** aus. Wählen Sie unter Snapchat Audience Sync die Option **Snapchat verbinden** aus.

![Snapchat-Technologie-Seite in Braze, die eine Übersicht und einen Abschnitt Snapchat Audience Sync mit dem Button Connected Snapchat enthält.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Sie werden dann auf die Snapchat OAuth-Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync Integration zu autorisieren.

Sobald Sie "Bestätigen" gewählt haben, werden Sie zurück nach Braze geleitet, um die Snapchat-Anzeigenkonten auszuwählen, die Sie synchronisieren möchten. 

![Eine Liste der verfügbaren Werbekonten, die Sie mit Snapchat verbinden können.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Nach erfolgreicher Verbindung kehren Sie zur Partnerseite zurück, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Eine aktualisierte Version der Technologie-Partnerseite von Snapchat, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Ihre Snapchat-Verbindung wird auf der Ebene des Braze Workspace angewendet. Wenn Ihr Snapchat-Administrator Sie von Ihrem Snapchat Business Manager oder dem Zugriff auf die verbundenen Snapchat-Anzeigenkonten entfernt, erkennt Braze ein ungültiges Token. Dies hat zur Folge, dass Ihre aktiven Canvase, die Snapchat verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### Schritt 2: Hinzufügen eines Zielgruppen-Synchronisationsschritts mit Snapchat

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

Klicken Sie auf den Button **Angepasste Zielgruppe**, um den Komponenteneditor zu öffnen.

Wählen Sie **TikTok** als den gewünschten Audience Sync Partner aus.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann Ihr gewünschtes Snapchat-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer:innen zur Zielgruppe hinzufügen** und wählen Sie aus, welche Felder Sie mit Snapchat synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Zielgruppe erstellen** klicken.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier wird das gewünschte Anzeigenkonto ausgewählt, und eine neue Zielgruppe wird erstellt.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe auch referenzieren, um sie später in Canvas zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Eine Meldung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie die Audience Sync Komponente betreten.

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}
**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Snapchat Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie hinzu**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten

Sobald Sie Ihre Zielgruppe mit Snapchat synchronisiert haben, starten Sie das Canvas! Es wird eine neue Zielgruppe erstellt, und Nutzer:innen, die den Schritt Audience Sync durchlaufen haben, werden in diese Zielgruppe auf Snapchat weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangehen.

Sie können die Zielgruppen in Snapchat einsehen, indem Sie Ihr Ads Manager:in-Konto aufrufen und in der Navigation im Bereich Assets die **Zielgruppen** auswählen. Auf der Seite **Zielgruppen** können Sie die Größe jeder Zielgruppe sehen, sobald sie ~1.000 erreicht hat.

![Details zur Zielgruppe einer bestimmten Snapchat-Zielgruppe, einschließlich Name der Zielgruppe, Art der Zielgruppe, Größe der Zielgruppe und Bindung der Zielgruppe in Tagen.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, synchronisiert Braze diese Nutzer:innen nahezu in Realtime und respektiert dabei die Rate-Limits der Snapchat API. In der Praxis wird Braze versuchen, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese Nutzer:innen an Snapchat weitergeleitet werden.

Das Rate-Limits der API von Snapchat besagt, dass nicht mehr als zehn Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage möglich sind. Erreicht eine Braze-Kund:in dieses Rate-Limit, wird Braze-Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt.

### Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente eingegeben haben, um mit Snapchat synchronisiert zu werden. |
| Fortgefahren mit nächstem Schritt | Wie viele Nutzer:innen haben den Fortschritt zur nächsten Komponente vorangetrieben, falls es eine solche gibt? Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Snapchat synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Snapchat verarbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden nicht mit Snapchat synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiger Snapchat-Token sein oder wenn die Zielgruppe auf Snapchat gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei der Berichterstattung über synchronisierte Nutzer:innen und fehlerhafte Metriken kommen wird.
{% endalert %}   

## Häufig gestellte Fragen

### Wie viele Zielgruppen kann Snapchat unterstützen?

Zurzeit können Sie nur 1.000 Zielgruppen in Ihrem Snapchat-Konto haben. 

Wenn Sie dieses Limit überschreiten, wird Braze Sie darüber informieren, dass wir keine neuen Zielgruppen erstellen können. Sie müssen Zielgruppen, die Sie nicht mehr verwenden, aus Ihrem Snapchat-Anzeigenkonto entfernen.

### Woher weiß ich, ob Nutzer:innen übereinstimmen, nachdem ich Nutzer:innen an Snapchat weitergegeben habe?

Snapchat stellt diese Informationen für seine Richtlinien zum Datenschutz nicht zur Verfügung.

### Was sollte ich als nächstes tun, wenn ich den Fehler eines ungültigen Tokens erhalte?

Sie können die Verbindung zu Ihrem Snapchat-Konto auf der Partnerseite von Snapchat trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Snapchat Business Manager-Administrator, dass Sie die entsprechenden Berechtigungen für das Werbekonto haben, mit dem Sie synchronisieren möchten.

### Warum ist es nicht zulässig, meinen Canvas zu starten?

Stellen Sie sicher, dass Ihr Snapchat-Anzeigenkonto erfolgreich mit Braze auf der Snapchat Partnerseite verbunden ist. Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und die passenden Felder ausgewählt haben.


