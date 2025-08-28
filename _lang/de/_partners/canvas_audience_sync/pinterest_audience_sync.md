---
nav_title: Pinterest
article_title: Canvas Zielgruppen Synchronisierung mit Pinterest
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Braze Audience Sync auf Pinterest verwenden können, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# Zielgruppen-Synchronisation auf Pinterest

Mit der Braze Audience Sync to Pinterest können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze Integration zu Pinterest Audiences hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt zum Triggern einer Anzeige für diesen Nutzer in Ihren Pinterest Audiences verwendet werden.

**Zu den üblichen Anwendungsfällen für die Synchronisierung von Zielgruppen gehören:**

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten
- Erstellen von Actalike Audiences zur effizienteren Gewinnung neuer Nutzer:innen

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Pinterest geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Richtlinie zum Datenschutz](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to Pinterest ist eine Integration von Audience Sync Pro. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze-Konto Manager:in.
{% endalert %}

## Voraussetzungen 
Sie müssen sicherstellen, dass die folgenden Artikel erstellt, vervollständigt und/oder akzeptiert wurden, bevor Sie Ihren Pinterest Audience Step in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Ein zentrales Tool zur Verwaltung der Pinterest-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten, Apps). |
| Pinterest Anzeigenkonto | [Pinterest](https://ads.pinterest.com/) | Ein aktives Pinterest-Anzeigenkonto, das mit dem Pinterest Business Hub Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Ihr Pinterest Business Hub-Administrator Ihnen Administratorrechte für die Pinterest-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| Pinterest Bedingungen & Richtlinien | Pinterest | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von Pinterest in Bezug auf Ihre Nutzung von Pinterest Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird, wie z. B.: die Allgemeinen Geschäftsbedingungen, die Geschäftsbedingungen für Serviceleistungen, die Datenschutzrichtlinien, die Servicebedingungen für Entwickler und APIs, die Bedingungen für Anzeigendaten, die Werberichtlinien, die Vereinbarung über Werbedienste, die Community-Richtlinien und die Markenrichtlinien. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit Pinterest verbinden

Gehen Sie auf dem Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Pinterest** aus. Wählen Sie unter Pinterest Audience Sync die Option **Pinterest verbinden** aus.

![Pinterest-Technologie-Seite in Braze, die eine Übersicht und einen Abschnitt Pinterest Audience Sync mit dem Button Connected Pinterest enthält.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Sie werden dann auf die Pinterest OAuth-Seite weitergeleitet, um Braze für Ad Account Management und Audience Management zu autorisieren.

Nachdem Sie **Bestätigen** gewählt haben, werden Sie wieder zu Braze zurückgeleitet, um die Pinterest-Anzeigenkonten auszuwählen, die Sie synchronisieren möchten. 

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Pinterest verbinden können.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Wenn die Verbindung erfolgreich hergestellt wurde, kehren Sie zur Partnerseite zurück, wo Sie sehen können, welche Konten verbunden sind, und wo Sie bestehende Konten trennen können.

![Eine aktualisierte Version der Technologie-Partnerseite von Pinterest, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Ihre Pinterest-Verbindung wird auf der Ebene des Braze Workspace angewendet. Wenn Ihr Pinterest-Administrator Sie aus Ihrem Pinterest Business Hub oder dem Zugriff auf die verbundenen Pinterest-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvase, die Pinterest Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann die Nutzer:innen nicht synchronisieren.

### Schritt 2: Hinzufügen eines Zielgruppen-Synchronisationsschritts mit Pinterest

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

Klicken Sie auf den Button **Angepasste Zielgruppe**, um den Komponenteneditor zu öffnen.

Wählen Sie **Pinterest** als den gewünschten Audience Sync Partner aus.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann Ihr gewünschtes Pinterest-Anzeigenkonto aus. Geben Sie in der **Dropdown-Liste Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer:innen zu Zielgruppe hinzufügen** und wählen Sie aus, welche Felder Sie mit Pinterest synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Zielgruppe erstellen** klicken.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier wird das gewünschte Anzeigenkonto ausgewählt, und eine neue Zielgruppe wird erstellt.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe auch referenzieren, um sie später in Canvas zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Eine Meldung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie den Canvas-Schritt betreten.
{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}
**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Zielgruppen auf Pinterest hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und fügen Sie sie der Zielgruppe hinzu. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie den Schritt Audience Sync betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten

Sobald Sie Ihre Audience Sync auf Pinterest konfiguriert haben, starten Sie das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Schritt Audience Sync durchlaufen, werden in diese Zielgruppe auf Pinterest weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangehen.

Sie können sich die Zielgruppen auf Pinterest ansehen, indem Sie sich in Ihrem Manager:in-Konto anmelden und Zielgruppen aus dem Dropdown-Menü für Anzeigen auswählen. Auf der Seite Zielgruppe sehen Sie die Größe jeder Zielgruppe, sobald sie ~100 erreicht hat.

![Zielgruppendetails für eine bestimmte Pinterest-Zielgruppe, einschließlich Zielgruppenname, Zielgruppen-ID, Zielgruppentyp und Zielgruppengröße.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, wird Braze diese Nutzer:innen nahezu in Realtime synchronisieren und dabei die Rate-Limits der Marketing API von Pinterest respektieren. In der Praxis wird Braze versuchen, so viele Nutzer:innen wie möglich alle 5 Sekunden zu verarbeiten, bevor diese Nutzer:innen an Pinterest weitergeleitet werden.

Das Segmente API Rate-Limits von Pinterest besagt, dass nicht mehr als sieben Abfragen pro Sekunde pro Nutzer:innen und 1.900 Nutzer:innen pro Anfrage möglich sind. Erreicht eine Braze-Kund:in dieses Rate-Limit, wird Braze-Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt.

## Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente eingegeben haben, die mit Pinterest synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Wie viele Nutzer:innen haben den Fortschritt zur nächsten Komponente vorangetrieben, falls es eine solche gibt? Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Pinterest synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Pinterest bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden nicht mit Pinterest synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Pinterest Token sein oder wenn die Zielgruppe auf Pinterest gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei der Berichterstattung über synchronisierte Nutzer:innen und fehlerhafte Metriken kommen wird.
{% endalert %}   

## Häufig gestellte Fragen

### Wie lange dauert es, bis meine Zielgruppen auf Pinterest angezeigt werden?

Die Größe der Zielgruppe wird innerhalb von 24-48 Stunden auf der Seite **Zielgruppen** im Anzeigen Manager von Pinterest aktualisiert.

### Woher weiß ich, ob Nutzer:innen übereinstimmen, nachdem ich Nutzer:innen an Pinterest weitergegeben habe?

Pinterest stellt diese Informationen nicht für seine eigenen Richtlinien zum Datenschutz zur Verfügung.

### Was sollte ich als nächstes tun, wenn ich den Fehler eines ungültigen Tokens erhalte?

Vergewissern Sie sich bei Ihrem Pinterest Business Hub-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, das Sie synchronisieren möchten. Sie können die Verbindung zu Ihrem Pinterest-Konto auch auf der Partnerseite von Pinterest trennen und wiederherstellen. 

### Warum ist es nicht zulässig, meinen Canvas zu starten?

Stellen Sie sicher, dass Ihr Pinterest-Konto erfolgreich mit Braze auf der Partnerseite von Pinterest verbunden ist. Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und die passenden Felder ausgewählt haben.

### Warum kann ich mein Anzeigenkonto nicht für meinen Audience Sync-Schritt auswählen?

Überprüfen Sie, ob Ihr Token mit den richtigen Kontoberechtigungen erstellt wurde. Beachten Sie, dass bei zu vielen Zielgruppen in Ihrem Pinterest-Anzeigenkonto das Dropdown-Menü zum Auswählen Ihres Anzeigenkontos einen Timeout verursachen kann. In diesem Fall empfehlen wir, die Anzahl der Zielgruppen in Ihrem Anzeigenkonto zu reduzieren.

