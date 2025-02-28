---
nav_title: Pinterest
article_title: Canvas Audience Sync zu Pinterest
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync auf Pinterest verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# Publikumssynchronisation auf Pinterest

Mit der Braze Audience Sync to Pinterest können Marken Nutzerdaten aus ihrer eigenen Braze-Integration zu Pinterest Audiences hinzufügen, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, kann jetzt zum Auslösen einer Anzeige für diesen Benutzer in Ihren Pinterest Audiences verwendet werden.

**Häufige Anwendungsfälle für die Synchronisierung von Zielgruppen sind:**

- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut ansprechen
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind
- Erstellen von Actalike Audiences zur effizienteren Gewinnung neuer Benutzer

Mit dieser Funktion können Marken kontrollieren, welche spezifischen Erstanbieterdaten mit Pinterest geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to Pinterest ist eine Audience Sync Pro-Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager.
{% endalert %}

## Voraussetzungen 
Sie müssen sicherstellen, dass die folgenden Elemente erstellt, vervollständigt und/oder akzeptiert wurden, bevor Sie Ihren Pinterest Audience Step in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Ein zentrales Tool zur Verwaltung der Pinterest-Assets Ihrer Marke (wie Anzeigenkonten, Seiten, Apps). |
| Pinterest Anzeigenkonto | [Pinterest](https://ads.pinterest.com/) | Ein aktives Pinterest-Anzeigenkonto, das mit dem Pinterest Business Hub Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Ihr Pinterest Business Hub-Administrator Ihnen Administratorrechte für die Pinterest-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| Pinterest Bedingungen & Richtlinien | Pinterest | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von Pinterest in Bezug auf Ihre Nutzung von Pinterest Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird. Dazu können gehören: die Nutzungsbedingungen, die Geschäftsbedingungen, die Datenschutzrichtlinien, die Entwickler- und API-Nutzungsbedingungen, die Bedingungen für Anzeigendaten, die Werberichtlinien, die Vereinbarung über Werbedienstleistungen, die Community-Richtlinien und die Markenrichtlinien. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit Pinterest verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Pinterest**. Wählen Sie unter Pinterest Audience Sync die Option **Pinterest verbinden**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

![Pinterest-Technologie-Seite in Braze, die einen Übersichtsbereich und einen Bereich Pinterest Audience Sync mit der Schaltfläche Connected Pinterest enthält.][1]{: style="max-width:80%;"}

Sie werden dann auf die Pinterest OAuth-Seite weitergeleitet, um Braze für Ad Account Management und Audience Management zu autorisieren.

Sobald Sie Bestätigen gewählt haben, werden Sie zurück zu Braze weitergeleitet, um die Pinterest-Anzeigenkonten auszuwählen, die Sie synchronisieren möchten. 

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Pinterest verbinden können.][2]{: style="max-width:80%;"}

Nach erfolgreicher Verbindung kehren Sie zur Partnerseite zurück, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Eine aktualisierte Version der Pinterest-Technologiepartnerseite, auf der die erfolgreich verbundenen Anzeigenkonten angezeigt werden.][3]{: style="max-width:80%;"}

Ihre Pinterest-Verbindung wird auf der Ebene des Braze-Arbeitsbereichs angewendet. Wenn Ihr Pinterest-Administrator Sie aus Ihrem Pinterest Business Hub oder dem Zugriff auf die verbundenen Pinterest-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die Pinterest Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann keine Benutzer synchronisieren.

### Schritt 2: Fügen Sie einen Schritt zur Publikums-Synchronisierung mit Pinterest hinzu

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

Klicken Sie auf die Schaltfläche **Benutzerdefinierte Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **Pinterest** als den gewünschten Audience Sync-Partner.

![][19]{: style="max-width:80%;"}

Wählen Sie dann Ihr gewünschtes Pinterest-Anzeigenkonto aus. Geben Sie in der **Dropdown-Liste Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Ein neues Publikum schaffen %}

**Ein neues Publikum schaffen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Benutzer zur Zielgruppe hinzufügen** und wählen Sie die Felder aus, die Sie mit Pinterest synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche **Zielgruppe erstellen** klicken.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier wird das gewünschte Anzeigenkonto ausgewählt und eine neue Zielgruppe erstellt.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auch später in der Canvas-Reise auf diese Zielgruppe verweisen, um sie zu entfernen.

![Eine Warnung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Benutzer nahezu in Echtzeit, sobald sie den Schritt Audience Sync betreten.
{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}
**Synchronisieren Sie mit einer bestehenden Zielgruppe**<br>
Braze bietet auch die Möglichkeit, Nutzer zu bestehenden Pinterest-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und fügen Sie sie der Zielgruppe hinzu. Braze fügt dann nahezu in Echtzeit Benutzer hinzu, sobald sie den Audience Sync-Schritt betreten.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten

Sobald Sie Ihre Audience Sync auf Pinterest konfiguriert haben, starten Sie die Canvas! Die neue Zielgruppe wird erstellt und Nutzer, die den Schritt Audience Sync durchlaufen, werden in diese Zielgruppe auf Pinterest weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Benutzer zum nächsten Schritt in ihrer User Journey übergehen.

Sie können sich die Zielgruppe auf Pinterest ansehen, indem Sie Ihr Ads Manager-Konto aufrufen und im Dropdown-Menü Anzeigen die Option Zielgruppen auswählen. Auf der Seite Publikum können Sie die Größe jedes Publikums sehen, sobald es ~100 erreicht hat.

![Audience-Details für eine bestimmte Pinterest Audience mit Audience-Name, Audience-ID, Audience-Typ und Audience-Größe.][11]

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung

Wenn Nutzer den Schritt zur Audience Sync erreichen, synchronisiert Braze diese Nutzer nahezu in Echtzeit und respektiert dabei die Ratenbeschränkungen der Marketing API von Pinterest. In der Praxis wird Braze versuchen, alle 5 Sekunden so viele Benutzer wie möglich zu verarbeiten, bevor es diese Benutzer an Pinterest weiterleitet.

Pinterests Segment-API-Ratenbeschränkung besagt, dass nicht mehr als sieben Abfragen pro Sekunde pro Benutzer und 1.900 Benutzer pro Anfrage möglich sind. Wenn ein Braze-Kunde dieses Ratenlimit erreicht, wird Braze the Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

## Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Aufgenommen | Anzahl der Benutzer, die diese Komponente eingegeben haben, die mit Pinterest synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Wie viele Benutzer sind zur nächsten Komponente übergegangen, falls es eine gibt? Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Benutzer, die erfolgreich mit Pinterest synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit Pinterest bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Benutzer, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Pinterest synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Pinterest-Token sein oder wenn die Zielgruppe auf Pinterest gelöscht wurde. |
| Canvas verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei den Berichten für synchronisierte Benutzer und fehlerhafte Metriken kommen wird.
{% endalert %}   

## Fehlersuche
{% details Was sollte ich als nächstes tun, wenn ich einen ungültigen Token-Fehler erhalte? %}
Sie können die Verbindung zu Ihrem Pinterest-Konto auf der Pinterest-Partnerseite einfach trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Pinterest Business Hub-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, das Sie synchronisieren möchten.
{% enddetails %}

{% details Warum kann mein Canvas nicht gestartet werden? %}
Stellen Sie sicher, dass Ihr Pinterest-Konto erfolgreich mit Braze auf der Pinterest-Partnerseite verbunden ist.
Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben
{% enddetails %}

{% details Woher weiß ich, ob die Benutzer übereinstimmen, nachdem ich sie an Pinterest weitergegeben habe? %}
Pinterest stellt diese Informationen nicht für seine eigenen Datenschutzrichtlinien zur Verfügung.
{% enddetails %}

{% details Wie lange dauert es, bis meine Zielgruppen auf Pinterest angezeigt werden? %}
Die Größe der Zielgruppe wird innerhalb von 24-48 Stunden auf der Seite "Zielgruppen" im Anzeigenmanager von Pinterest aktualisiert.
{% enddetails %}

[1]: {% image_buster /assets/img/pinterest/pinterest1.png %}
[2]: {% image_buster /assets/img/pinterest/pinterest2.png %}
[3]: {% image_buster /assets/img/pinterest/pinterest3.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[6]: {% image_buster /assets/img/pinterest/pinterest6.png %}
[7]: {% image_buster /assets/img/pinterest/pinterest7.png %}
[8]: {% image_buster /assets/img/pinterest/pinterest8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[9]: {% image_buster /assets/img/pinterest/pinterest9.png %}
[10]: {% image_buster /assets/img/pinterest/pinterest10.png %}
[11]: {% image_buster /assets/img/pinterest/pinterest11.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}