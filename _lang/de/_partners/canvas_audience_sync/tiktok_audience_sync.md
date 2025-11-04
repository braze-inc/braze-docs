---
nav_title: TikTok
article_title: Canvas Zielgruppen Synchronisierung mit TikTok
alias: /tiktok_audience_sync/
description: "Dieser Artikel referenziert, wie Sie Braze Audience Sync für TikTok verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
Tool:
  - Canvas
page_order: 7

---

# Zielgruppen Synchronisierung mit TikTok

Mit der Braze Audience Sync to TikTok können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze Integration zu TikTok Audiences hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Alle Kriterien, die Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas verwenden würden. 

**Zu den häufigen Anwendungsfällen für Audience Syncing gehören**:

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten
- Erstellen von Actalike Audiences zur effizienteren Gewinnung neuer Nutzer:innen

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit TikTok geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Richtlinie zum Datenschutz](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to TikTok ist eine Integration von Audience Sync Pro. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze-Konto Manager:in.
{% endalert %}

## Voraussetzungen

Sie müssen sicherstellen, dass die folgenden Artikel erstellt, vervollständigt und/oder akzeptiert wurden, bevor Sie Ihren TikTok-Zielgruppen-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| TikTok für Business Center Konto | [TikTok](https://business.tiktok.com/) | Ein zentrales Tool zur Verwaltung der TikTok-Assets Ihrer Marke (wie Anzeigenkonten, Seiten, Apps). |
| TikTok Anzeigenkonto | [TikTok](https://ads.tiktok.com/) | Ein aktives TikTok-Anzeigenkonto, das mit dem Business Center-Konto Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr TikTok Business Center Manager Ihnen Administratorrechte für die TikTok-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| TikToK Bedingungen & Richtlinien | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von TikTok in Bezug auf Ihre Nutzung von Pinterest Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird, wie z.B.: die kommerziellen Serviceleistungen, die Werbebedingungen, die Datenschutzrichtlinien, die Bedingungen für angepasste Zielgruppen, die Servicebedingungen für Entwickler, die Vereinbarung über die gemeinsame Nutzung von Entwickler:in, die Werberichtlinien, die Markenrichtlinien und die Richtlinien der Community. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit TikTok verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **TikTok** aus. Wählen Sie unter TikTok Audience Sync **TikTok verbinden** aus.

![Die TikTok-Technologie-Seite in Braze enthält eine Übersicht und einen Abschnitt TikTok Audience Sync mit dem Button Connected TikTok.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Sie werden dann auf die TikTok OAuth-Seite weitergeleitet, um Braze für die Verwaltung von Anzeigenkonten und Zielgruppen zu autorisieren. Nachdem Sie **Bestätigen** gewählt haben, werden Sie wieder zu Braze zurückgeleitet, um auszuwählen, mit welchen TikTok-Anzeigenkonten Sie synchronisieren möchten. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Sobald die Verbindung erfolgreich hergestellt wurde, kehren Sie zur Partnerseite zurück. Hier können Sie sehen, welche Konten verbunden sind und die Verbindung zu bestehenden Konten trennen.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Ihre TikTok-Verbindung wird auf der Ebene der App-Gruppe von Braze angewendet. Wenn Ihr TikTok-Administrator Sie aus Ihrem TikTok Business Center oder dem Zugriff auf die verbundenen TikTok-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvase, die TikTok Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann die Nutzer:innen nicht synchronisieren.

### Schritt 2: Hinzufügen einer TikTok Audience-Komponente in Canvas Flow

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

Klicken Sie auf den Button **Angepasste Zielgruppe**, um den Komponenteneditor zu öffnen.

Wählen Sie **TikTok** als den gewünschten Audience Sync Partner aus.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann das gewünschte TikTok-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer:innen hinzufügen** und wählen Sie die Felder aus, die Sie mit TikTok synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Zielgruppe erstellen** klicken.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe auch referenzieren, um sie später in Canvas zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie den Canvas-Schritt betreten.

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}

**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Zielgruppen von TikTok hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie hinzu**. Braze fügt dann Nutzer:innen in nahezu Realtime hinzu, sobald sie den Schritt TikTok Audience betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten
Sobald Sie Ihre TikTok Audience-Komponente konfiguriert haben, starten Sie einfach den Canvas! Es wird eine neue Zielgruppe erstellt, und Nutzer:innen, die die TikTok Audience-Komponente durchlaufen, werden zu dieser Zielgruppe auf TikTok weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangehen.

Sie können die Zielgruppen in TikTok einsehen, indem Sie Ihr **Ads Manager:in Konto** eingeben und **Zielgruppen** aus dem Dropdown-Menü **Assets** auswählen. Auf der Seite **Zielgruppe** sehen Sie die Größe jeder Zielgruppe, sobald sie ~1.000 erreicht hat.

![TikTok-Seite mit den folgenden Metriken für die angegebene Zielgruppe.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, wird Braze diese Nutzer:innen nahezu in Realtime synchronisieren und dabei die Rate-Limits der Marketing API von TikTok respektieren. Das bedeutet, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese Nutzer:innen an TikTok weitergeleitet werden.

Das Segmente API Rate-Limits von TikTok besagt, dass nicht mehr als 50 Abfragen pro Sekunde und 10k Nutzer:innen pro Anfrage möglich sind. Erreicht eine Braze Kund:in dieses Rate-Limit, wird der Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt.

## Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrisch | Beschreibung |
| ------ | ----------- |
| Eingetreten | Anzahl der Nutzer:in, die diese Komponente eingegeben haben, die mit TikTok synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Anzahl der Nutzer:innen, die zur nächsten Komponente vorgebracht wurden, sofern eine solche existiert. Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit TikTok synchronisiert wurden. Beachten Sie, dass dies nicht gleichbedeutend ist mit Nutzer:innen, die auf TikTok gefunden wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit TikTok bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden nicht mit TikTok synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges TikTok-Token sein oder wenn die Zielgruppe auf TikTok gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas eine Audience-Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es bei den Metriken Nutzer:innen synchronisiert und Nutzer:innen fehlerhaft aufgrund des Bulk Flush und der 13-stündigen Wiederholung zu einer Verzögerung bei der Berichterstattung kommt.
{% endalert %}

## Häufig gestellte Fragen

### Was sollte ich als nächstes tun, wenn ich den Fehler eines ungültigen Tokens erhalte?

Sie können Ihr TikTok-Konto auf der Partnerseite von TikTok trennen und wieder verbinden. Vergewissern Sie sich bei Ihrem TikTok Business Center-Administrator, dass Sie die entsprechenden Berechtigungen für das zu synchronisierende Anzeigenkonto haben.

### Warum ist es nicht zulässig, meinen Canvas zu starten?

Bestätigen Sie, dass Ihr TikTok-Konto erfolgreich mit Braze auf der TikTok Partnerseite verbunden ist. Vergewissern Sie sich als nächstes, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und die passenden Felder ausgewählt haben.

### Woher weiß ich, ob Nutzer:innen zueinander gefunden haben, nachdem ich Nutzer:innen an TikTok weitergegeben habe?

TikTok stellt diese Informationen nicht für seine Richtlinien zum Datenschutz zur Verfügung.

### Wie lange wird es dauern, bis meine Zielgruppen in TikTok angezeigt werden?

Die Größe der Zielgruppe wird innerhalb von 24-48 Stunden auf der Seite Zielgruppen im TikTok Ads Manager:in aktualisiert.

### Wie viele Zielgruppen kann ich maximal in meinem TikTok-Anzeigenkonto haben?

Sie können bis zu 400 Zielgruppen pro TikTok-Anzeigenkonto haben.

### Warum ist meine Zielgruppe oder die Trefferquote in TikTok höher als die Nutzer:innen, die in Braze mit Audience Sync synchronisiert wurden?

Das liegt daran, dass in TikTok eine ID mit mehreren Nutzer:innen verbunden sein kann. Dies tritt am häufigsten auf, wenn Clients mobile Ad-IDs (iOS IDFA und Android GAID) verwenden, da auf einem Gerät mehrere Nutzer:innen von TikTok angemeldet sein können. 

Außerdem zählt TikTok auch Nutzer:innen von Pangle als gematchte Nutzer:innen, was in einigen Fällen zu einer erhöhten Match-Rate führen kann. Wenn Sie die Zielgruppe jedoch für die Zustellung von Anzeigen verwenden, ist die tatsächliche Größe der zustellbaren Zielgruppe möglicherweise nicht so hoch wie die Größe der zugeordneten Nutzer:innen, da sie von der Platzierung und anderen Einflussfaktoren abhängt.


