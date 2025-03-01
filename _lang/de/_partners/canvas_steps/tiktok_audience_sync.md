---
nav_title: TikTok
article_title: Canvas Audience Sync zu TikTok
alias: /tiktok_audience_sync/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für TikTok verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
Tool:
  - Canvas
page_order: 7

---

# Publikumssynchronisation zu TikTok

Mit der Braze Audience Sync to TikTok können Marken Benutzerdaten aus ihrer eigenen Braze-Integration zu TikTok Audiences hinzufügen, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu liefern. Alle Kriterien, die Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze Canvas verwenden würden. 

**Häufige Anwendungsfälle für Audience Syncing sind**:

- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut ansprechen
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind
- Erstellen von Actalike Audiences zur effizienteren Gewinnung neuer Benutzer

Mit dieser Funktion können Marken kontrollieren, welche spezifischen Daten von Erstanbietern mit TikTok geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to TikTok ist eine Audience Sync Pro Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager.
{% endalert %}

## Voraussetzungen

Sie müssen sicherstellen, dass die folgenden Punkte erstellt, ausgefüllt und/oder akzeptiert wurden, bevor Sie Ihren TikTok Audience Step in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| TikTok für Business Center Konto | [TikTok](https://business.tiktok.com/) | Ein zentrales Tool zur Verwaltung der TikTok-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten, Apps). |
| TikTok Anzeigenkonto | [TikTok](https://ads.tiktok.com/) | Ein aktives TikTok-Anzeigenkonto, das mit dem Business Center-Konto Ihrer Marke verbunden ist.<br><br>Vergewissern Sie sich, dass Ihr TikTok Business Center Manager Ihnen Administratorrechte für die TikTok-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| TikToK Bedingungen & Richtlinien | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von TikTok in Bezug auf Ihre Nutzung von Pinterest Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird, darunter: die kommerziellen Nutzungsbedingungen, die Werbebedingungen, die Datenschutzrichtlinie, die Bedingungen für Custom Audience, die Nutzungsbedingungen für Entwickler, die Vereinbarung über die gemeinsame Nutzung von Entwicklerdaten, die Werberichtlinien, die Markenrichtlinien und die Community-Richtlinien. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit TikTok verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **TikTok** aus. Wählen Sie unter TikTok Audience Sync die Option **TikTok verbinden**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

![Die TikTok-Technologie-Seite in Braze enthält einen Abschnitt Übersicht und einen Abschnitt TikTok Audience Sync mit der Schaltfläche Connected TikTok.][1]{: style="max-width:75%;"}

Sie werden dann auf die TikTok OAuth-Seite weitergeleitet, um Braze für die Verwaltung von Anzeigenkonten und Audience Management zu autorisieren. Nachdem Sie **Bestätigen** gewählt haben, werden Sie wieder zu Braze zurückgeleitet, um auszuwählen, mit welchen TikTok-Anzeigenkonten Sie synchronisieren möchten. 

![][2]{: style="max-width:75%;"}

Sobald die Verbindung erfolgreich hergestellt wurde, kehren Sie zur Partnerseite zurück. Hier können Sie sehen, welche Konten verbunden sind und die Verbindung zu bestehenden Konten trennen.

![][3]{: style="max-width:75%;"}

Ihre TikTok-Verbindung wird auf der Ebene der Braze-App-Gruppe angewendet. Wenn Ihr TikTok-Administrator Sie aus Ihrem TikTok Business Center oder dem Zugriff auf die verbundenen TikTok-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die TikTok Audience-Komponenten verwenden, Fehler anzeigen und Braze wird nicht in der Lage sein, Benutzer zu synchronisieren.

### Schritt 2: Hinzufügen einer TikTok Audience-Komponente in Canvas Flow

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**. 

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

Klicken Sie auf die Schaltfläche **Benutzerdefinierte Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **TikTok** als den gewünschten Audience Sync-Partner.

![][19]{: style="max-width:80%;"}

Wählen Sie dann das gewünschte TikTok-Anzeigenkonto. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

![][11]

{% tabs %}
{% tab Ein neues Publikum schaffen %}

**Ein neues Publikum schaffen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Benutzer zur Zielgruppe hinzufügen** und wählen Sie die Felder, die Sie mit TikTok synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche **Zielgruppe erstellen** klicken.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auch später in der Canvas-Reise auf diese Zielgruppe verweisen, um sie zu entfernen.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Benutzer nahezu in Echtzeit, sobald sie den Schritt der Zielgruppe betreten.

{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}

**Synchronisieren Sie mit einer bestehenden Zielgruppe**<br>
Braze bietet auch die Möglichkeit, Benutzer zu bestehenden TikTok-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie der Zielgruppe hinzu**. Braze fügt dann nahezu in Echtzeit Nutzer hinzu, sobald diese den TikTok Audience-Schritt betreten.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die vorhandene Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten
Sobald Sie Ihre TikTok Audience-Komponente konfiguriert haben, starten Sie einfach die Canvas! Es wird eine neue Audience erstellt und Nutzer, die durch die TikTok Audience-Komponente fließen, werden in diese Audience auf TikTok weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Benutzer zum nächsten Schritt in ihrer User Journey übergehen.

Sie können die Zielgruppe in TikTok einsehen, indem Sie Ihr **Ads Manager-Konto** aufrufen und im Dropdown-Menü **Assets** die Option **Zielgruppen** auswählen. Auf der Seite **Publikum** können Sie die Größe jedes Publikums sehen, sobald es ~1.000 erreicht hat.

![TikTok-Seite mit den folgenden Metriken für das angegebene Publikum.][5]

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung

Wenn Benutzer die Stufe Audience Sync erreichen, synchronisiert Braze diese Benutzer nahezu in Echtzeit und respektiert dabei die Ratenbeschränkungen der Marketing API von TikTok. Das bedeutet, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer wie möglich zu verarbeiten, bevor diese Nutzer an TikTok weitergeleitet werden.

TikToks Segment-API-Ratenlimit besagt, dass nicht mehr als 50 Abfragen pro Sekunde und 10k Benutzer pro Anfrage möglich sind. Wenn ein Braze-Kunde dieses Ratenlimit erreicht, wird der Canvas die Synchronisierung bis zu ~13 Stunden lang wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

## Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| Metrisch | Beschreibung |
| ------ | ----------- |
| Aufgenommen | Anzahl der Benutzer, die diese Komponente eingegeben haben, die mit TikTok synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Anzahl der Benutzer, die zur nächsten Komponente vorgerückt sind, falls eine solche existiert. Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Benutzer, die erfolgreich mit TikTok synchronisiert wurden. Beachten Sie, dass dies nicht gleichbedeutend ist mit Nutzern, die auf TikTok gematcht werden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit TikTok bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Benutzer, die aufgrund eines API-Fehlers nach ca. 13 Stunden Wiederholungsversuchen nicht mit TikTok synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges TikTok-Token sein oder wenn die Audience auf TikTok gelöscht wurde. |
| Canvas verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience-Synchronisationskomponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei den Berichten über synchronisierte Benutzer und fehlerhafte Benutzer kommen wird.
{% endalert %}

## Fehlersuche

{% details Was sollte ich als nächstes tun, wenn ich einen ungültigen Token-Fehler erhalte? %}
Sie können die Verbindung zu Ihrem TikTok-Konto auf der TikTok-Partnerseite trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem TikTok Business Center-Administrator, dass Sie die entsprechenden Berechtigungen für das zu synchronisierende Anzeigenkonto haben.
{% enddetails %}

{% details Warum kann mein Canvas nicht gestartet werden? %}
Stellen Sie sicher, dass Ihr TikTok-Konto erfolgreich mit Braze auf der TikTok-Partnerseite verbunden ist.
Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben.
{% enddetails %}

{% details Woher weiß ich, ob die Benutzer übereinstimmen, nachdem ich sie an TikTok weitergegeben habe? %}
TikTok stellt diese Informationen für seine Datenschutzrichtlinien nicht zur Verfügung.
{% enddetails %}

{% details Wie lange dauert es, bis meine Zielgruppen in TikTok angezeigt werden? %}
Die Größe der Zielgruppe wird innerhalb von 24-48 Stunden auf der Seite Zielgruppen im TikTok Ads Manager aktualisiert.
{% enddetails %}

{% details Wie viele Zielgruppen kann ich maximal in meinem TikTok-Anzeigenkonto haben? %}
400
{% enddetails %}

[1]: {% image_buster /assets/img/tiktok/tiktok1.png %}
[2]: {% image_buster /assets/img/tiktok/tiktok2.png %}
[3]: {% image_buster /assets/img/tiktok/tiktok3.png %}
[4]: {% image_buster /assets/img/tiktok/tiktok4.png %}
[5]: {% image_buster /assets/img/tiktok/tiktok5.png %}
[6]: {% image_buster /assets/img/tiktok/tiktok6.png %}
[7]: {% image_buster /assets/img/tiktok/tiktok7.png %}
[8]: {% image_buster /assets/img/tiktok/tiktok8.png %}
[11]: {% image_buster /assets/img/tiktok/tiktok11.png %}
[12]: {% image_buster /assets/img/tiktok/tiktok12.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[14]: {% image_buster /assets/img/tiktok/tiktok14.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok15.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
