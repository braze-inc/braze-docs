---
nav_title: TikTok
article_title: Canvas Audience Sync mit TikTok
alias: /tiktok_audience_sync/
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync für TikTok verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
Tool:
  - Canvas
page_order: 8

---

# Audience Sync mit TikTok

Mit Braze Audience Sync to TikTok können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze-Integration zu TikTok Audiences hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Alle Kriterien, die Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas verwenden würden.

**Zu den häufigen Anwendungsfällen für Audience Syncing gehören**:

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Unterdrückungs-Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten
- Erstellen von Actalike Audiences zur effizienteren Gewinnung neuer Nutzer:innen

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit TikTok geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro – Haftungsausschluss**<br>
Braze Audience Sync to TikTok ist eine Integration von Audience Sync Pro. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager.
{% endalert %}

## Voraussetzungen

Sie müssen sicherstellen, dass die folgenden Punkte erstellt, vervollständigt und/oder akzeptiert wurden, bevor Sie Ihren TikTok-Zielgruppen-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| TikTok for Business Center Konto | [TikTok](https://business.tiktok.com/) | Ein zentrales Tool zur Verwaltung der TikTok-Assets Ihrer Marke (wie Anzeigenkonten, Seiten, Apps). |
| TikTok-Anzeigenkonto | [TikTok](https://ads.tiktok.com/) | Ein aktives TikTok-Anzeigenkonto, das mit dem Business Center-Konto Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr TikTok Business Center Manager-Admin Ihnen Administratorrechte für die TikTok-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| TikTok-Bedingungen & -Richtlinien | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von TikTok in Bezug auf Ihre Nutzung von Pinterest Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird, wie z. B.: die kommerziellen Nutzungsbedingungen, die Werbebedingungen, die Datenschutzrichtlinie, die Bedingungen für angepasste Zielgruppen, die Nutzungsbedingungen für Entwickler:innen, die Vereinbarung über die gemeinsame Nutzung von Entwicklerdaten, die Werberichtlinien, die Markenrichtlinien und die Community-Richtlinien. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### 1. Schritt: Mit TikTok verbinden

{% alert important %}
Sie müssen die [Berechtigung „Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) haben, um TikTok mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **TikTok** aus. Wählen Sie unter TikTok Audience Sync die Option **TikTok verbinden** aus.

![Die TikTok-Technologie-Seite in Braze enthält einen Übersichtsabschnitt und einen Abschnitt TikTok Audience Sync mit dem Button „Connected TikTok".]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Sie werden dann auf die TikTok-OAuth-Seite weitergeleitet, um Braze für die Verwaltung von Anzeigenkonten und Zielgruppen zu autorisieren. Nachdem Sie **Bestätigen** ausgewählt haben, werden Sie zurück zu Braze geleitet, um auszuwählen, mit welchen TikTok-Anzeigenkonten Sie synchronisieren möchten.

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Sobald die Verbindung erfolgreich hergestellt wurde, kehren Sie zur Partnerseite zurück. Hier können Sie sehen, welche Konten verbunden sind, und die Verbindung zu bestehenden Konten trennen.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Ihre TikTok-Verbindung wird auf der Ebene der Braze-App-Gruppe angewendet. Wenn Ihr TikTok-Administrator Sie aus Ihrem TikTok Business Center oder dem Zugriff auf die verbundenen TikTok-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvase, die TikTok Audience-Komponenten verwenden, Fehler anzeigen, und Braze wird die Nutzer:innen nicht synchronisieren können.

### 2. Schritt: Eine TikTok Audience-Komponente in Canvas hinzufügen

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync** aus.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3. Schritt: Sync-Einrichtung

Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **TikTok** als gewünschten Audience Sync Partner aus.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann das gewünschte TikTok-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Create a New Audience %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer:innen zur Zielgruppe hinzufügen** und wählen Sie die Felder aus, die Sie mit TikTok synchronisieren möchten. Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Zielgruppe erstellen** klicken.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze zeigt am oberen Rand des Schritteditors eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um Nutzer:innen später im Canvas-Verlauf zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie den Zielgruppen-Schritt betreten.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden TikTok-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie **Zur Zielgruppe hinzufügen**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie den TikTok Audience-Schritt betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### 4. Schritt: Canvas starten
Sobald Sie Ihre TikTok Audience-Komponente konfiguriert haben, starten Sie einfach den Canvas! Es wird eine neue Zielgruppe erstellt, und Nutzer:innen, die die TikTok Audience-Komponente durchlaufen, werden in diese Zielgruppe auf TikTok übertragen. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppe in TikTok einsehen, indem Sie Ihr **Ads Manager Konto** aufrufen und **Audiences** aus dem Dropdown-Menü **Assets** auswählen. Auf der Seite **Audience** sehen Sie die Größe jeder Zielgruppe, sobald sie &#126;1.000 erreicht hat.

![TikTok-Seite mit den folgenden Metriken für die angegebene Zielgruppe.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Realtime und respektiert dabei die Rate-Limits der Marketing-API von TikTok. Braze bündelt und verarbeitet alle 5 Sekunden so viele Nutzer:innen wie möglich, bevor sie an TikTok gesendet werden.

Das Segment-API-Rate-Limit von TikTok erlaubt nicht mehr als 50 Abfragen pro Sekunde und 10.000 Nutzer:innen pro Anfrage. Wenn eine Kund:in dieses Limit erreicht, wiederholt Braze die Synchronisierung für bis zu &#126;13 Stunden. Wenn die Synchronisierung dann immer noch nicht möglich ist, listet Braze diese Nutzer:innen in der Metrik „Fehlerhafte Nutzer:innen" auf.

## Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrik | Beschreibung |
| ------ | ----------- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit TikTok synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Anzahl der Nutzer:innen, die zur nächsten Komponente vorangebracht wurden, sofern eine vorhanden ist. Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit TikTok synchronisiert wurden. Beachten Sie, dass dies nicht gleichbedeutend mit auf TikTok gematchten Nutzer:innen ist. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit TikTok verarbeitet werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit TikTok synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges TikTok-Token sein oder die Löschung der Zielgruppe auf TikTok. |
| Canvas verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Beachten Sie, dass es bei den Metriken „Nutzer:innen synchronisiert" und „Fehlerhafte Nutzer:innen" aufgrund des Bulk-Flushers bzw. der 13-stündigen Wiederholungsversuche zu Verzögerungen bei der Berichterstattung kommen kann.
{% endalert %}

## Häufig gestellte Fragen

### Was sollte ich als Nächstes tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte?

Sie können Ihr TikTok-Konto auf der TikTok-Partnerseite trennen und erneut verbinden. Vergewissern Sie sich bei Ihrem TikTok Business Center-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, das Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden?

Bestätigen Sie, dass Ihr TikTok-Konto auf der TikTok-Partnerseite erfolgreich mit Braze verbunden ist. Stellen Sie außerdem sicher, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und die passenden Felder ausgewählt haben.

### Woher weiß ich, ob Nutzer:innen gematcht wurden, nachdem ich sie an TikTok übergeben habe?

TikTok stellt diese Informationen aufgrund seiner Datenschutzrichtlinien nicht zur Verfügung.

### Wie lange dauert es, bis meine Zielgruppen in TikTok angezeigt werden?

Die Größe der Zielgruppe wird innerhalb von 24–48 Stunden auf der Audiences-Seite im TikTok Ads Manager aktualisiert.

### Wie viele Zielgruppen kann ich maximal in meinem TikTok-Anzeigenkonto haben?

Sie können bis zu 400 Zielgruppen pro TikTok-Anzeigenkonto haben.

### Warum ist meine Zielgruppengröße oder Match-Rate in TikTok höher als die mit Audience Sync in Braze synchronisierten Nutzer:innen?

Das liegt daran, dass in TikTok eine ID mit mehreren TikTok-Nutzer:innen verknüpft sein kann. Dies tritt am häufigsten auf, wenn Clients mobile Ad-IDs (iOS IDFA und Android GAID) verwenden, da auf einem Gerät mehrere TikTok-Nutzer:innen angemeldet sein können.

Außerdem zählt TikTok auch Pangle-Nutzer:innen als gematchte Nutzer:innen, was in einigen Fällen zu einer erhöhten Match-Rate führen kann. Wenn Sie die Zielgruppe jedoch für die Zustellung von Anzeigen verwenden, ist die tatsächliche zustellbare Zielgruppengröße möglicherweise nicht so hoch wie die gematchte Nutzergröße, da sie von der Platzierung und anderen Einflussfaktoren abhängt.

### Warum erhalte ich eine E-Mail mit dem Betreff „Audience Does Not Exist For Canvas"?

Dies kann vorkommen, wenn die Zielgruppe, mit der Sie synchronisieren möchten, keine Streaming-Zielgruppe ist (z. B. wenn es sich um eine Lookalike-Zielgruppe oder eine Nutzerdatei-Zielgruppe handelt). Versuchen Sie, eine neue Zielgruppe über den Braze Audience Sync Canvas-Schritt zu erstellen.