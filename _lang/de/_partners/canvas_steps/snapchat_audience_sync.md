---
nav_title: Snapchat
article_title: Canvas Audience Sync zu Snapchat
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Snapchat verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# Publikums-Synchronisation mit Snapchat

Mit dem Braze Audience Sync to Snapchat können Marken Nutzerdaten aus ihrer Braze-Integration zu Snapchat-Kundenlisten hinzufügen, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu liefern. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, kann jetzt zum Auslösen einer Anzeige für diesen Benutzer in Ihren Snapchat-Kundenlisten verwendet werden.

**Häufige Anwendungsfälle für die Synchronisierung von Zielgruppen sind:**

- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut ansprechen
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind
- Erstellen von Lookalike Audiences zur effizienteren Gewinnung neuer Benutzer

Mit dieser Funktion können Nutzer kontrollieren, welche spezifischen Daten von Erstanbietern mit Snapchat geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to Snapchat ist eine Audience Sync Pro Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager.
{% endalert %}

## Voraussetzungen 

Sie müssen sicherstellen, dass die folgenden Punkte erstellt, ausgefüllt und/oder akzeptiert wurden, bevor Sie Ihren Snapchat Audience Step in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | Ein zentrales Tool zur Verwaltung der Snapchat-Assets Ihrer Marke (z. B. Werbekonten, Seiten, Apps). |
| Snapchat Anzeigenkonto | Snapchat | Ein aktives Snapchat-Anzeigenkonto, das mit dem Snapchat Business Manager Ihrer Marke verbunden ist.<br><br>Stellen Sie sicher, dass Ihr Snapchat Business Manager-Administrator Ihnen Administratorrechte für die Snapchat-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| Snapchat Bedingungen & Richtlinien | [Snapchat](https://www.snap.com/en-US/policies) | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien und Dokumentationen von Snapchat in Bezug auf Ihre Nutzung von Snapchat Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien und Dokumentationen, auf die darin verwiesen wird, wie z. B.: die Nutzungsbedingungen, die Geschäftsbedingungen, die Bedingungen für Entwickler, Audience Match, die Werberichtlinien, die Richtlinie für kommerzielle Inhalte, die Community-Richtlinien und die Verantwortung der Anbieter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit Snapchat verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Snapchat**. Wählen Sie unter Snapchat Audience Sync die Option **Snapchat verbinden**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

![Snapchat-Technologie-Seite in Braze, die einen Abschnitt Übersicht und einen Abschnitt Snapchat Audience Sync mit der Schaltfläche Verbundenes Snapchat enthält.][1]{: style="max-width:80%;"}

Sie werden dann auf die Snapchat OAuth Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync Integration zu autorisieren.

Sobald Sie Bestätigen gewählt haben, werden Sie zurück zu Braze geleitet, um die Snapchat-Anzeigenkonten auszuwählen, die Sie synchronisieren möchten. 

![Eine Liste der verfügbaren Werbekonten, die Sie mit Snapchat verbinden können.][2]{: style="max-width:80%;"}

Nach erfolgreicher Verbindung kehren Sie zur Partnerseite zurück, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Eine aktualisierte Version der Seite der Snapchat-Technologiepartner, die die erfolgreich verbundenen Werbekonten zeigt.][3]{: style="max-width:80%;"}

Ihre Snapchat-Verbindung wird auf der Ebene des Braze-Arbeitsbereichs angewendet. Wenn Ihr Snapchat-Administrator Sie aus Ihrem Snapchat Business Manager oder dem Zugriff auf die verbundenen Snapchat-Anzeigenkonten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die Snapchat verwenden, Fehler anzeigen und Braze kann die Benutzer nicht synchronisieren.

### Schritt 2: Schritt zur Publikums-Synchronisation mit Snapchat hinzufügen

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

Klicken Sie auf die Schaltfläche **Benutzerdefinierte Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **TikTok** als den gewünschten Audience Sync-Partner.

![][19]{: style="max-width:80%;"}

Wählen Sie dann Ihr gewünschtes Snapchat-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Ein neues Publikum schaffen %}

**Ein neues Publikum schaffen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Nutzer zur Zielgruppe hinzufügen** und wählen Sie die Felder aus, die Sie mit Snapchat synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche **Zielgruppe erstellen** klicken.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier wird das gewünschte Anzeigenkonto ausgewählt und eine neue Zielgruppe erstellt.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auch später in der Canvas-Reise auf diese Zielgruppe verweisen, um sie zu entfernen.

![Eine Warnung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Benutzer nahezu in Echtzeit, sobald sie die Komponente Audience Sync betreten.

{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}
**Synchronisieren Sie mit einer bestehenden Zielgruppe**<br>
Braze bietet auch die Möglichkeit, Nutzer zu bestehenden Snapchat-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie der Zielgruppe hinzu**. Braze fügt dann nahezu in Echtzeit Benutzer hinzu, sobald diese die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten

Sobald Sie Ihre Audience Sync für Snapchat konfiguriert haben, starten Sie die Canvas! Es wird eine neue Zielgruppe erstellt und Nutzer, die den Schritt Audience Sync durchlaufen haben, werden in diese Zielgruppe auf Snapchat weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Benutzer zum nächsten Schritt in ihrer User Journey übergehen.

Sie können die Zielgruppe in Snapchat anzeigen, indem Sie Ihr Ads Manager-Konto aufrufen und in der Navigation im Bereich Assets die Option **Zielgruppen** auswählen. Auf der Seite **Zielgruppen** können Sie die Größe der einzelnen Zielgruppen sehen, sobald sie ~1.000 erreicht haben.

![Publikumsdetails für ein bestimmtes Snapchat-Publikum, einschließlich Publikumsname, Publikumsart, Publikumsgröße und Publikumsdauer in Tagen.][9]

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung

Wenn Nutzer den Audience Sync-Schritt erreichen, wird Braze diese Nutzer nahezu in Echtzeit synchronisieren und dabei die API-Ratenlimits von Snapchat respektieren. In der Praxis wird Braze versuchen, alle 5 Sekunden so viele Nutzer wie möglich zu verarbeiten, bevor es diese Nutzer an Snapchat weiterleitet.

Das API-Limit von Snapchat besagt, dass nicht mehr als zehn Abfragen pro Sekunde und 100.000 Nutzer pro Anfrage möglich sind. Wenn ein Braze-Kunde dieses Ratenlimit erreicht, wird Braze the Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

### Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Aufgenommen | Anzahl der Benutzer, die diese Komponente eingegeben haben, um mit Snapchat synchronisiert zu werden. |
| Fortgefahren mit nächstem Schritt | Wie viele Benutzer sind zur nächsten Komponente übergegangen, falls es eine gibt? Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer, die erfolgreich mit Snapchat synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit Snapchat verarbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Snapchat synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Snapchat-Token sein oder wenn die Zielgruppe auf Snapchat gelöscht wurde. |
| Canvas verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei den Berichten für synchronisierte Benutzer und fehlerhafte Metriken kommen wird.
{% endalert %}   

## Fehlersuche

{% details Was sollte ich als nächstes tun, wenn ich einen ungültigen Token-Fehler erhalte? %}
Sie können die Verbindung zu Ihrem Snapchat-Konto auf der Snapchat-Partnerseite trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Snapchat Business Manager-Administrator, dass Sie die entsprechenden Berechtigungen für das Werbekonto haben, mit dem Sie synchronisieren möchten.
{% enddetails %}

{% details Warum kann mein Canvas nicht gestartet werden? %}
Stellen Sie sicher, dass Ihr Snapchat-Anzeigenkonto erfolgreich mit Braze auf der Snapchat-Partnerseite verbunden ist. Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben
{% enddetails %}

{% details Woher weiß ich, ob sich Nutzer gefunden haben, nachdem ich sie an Snapchat weitergegeben habe? %}
Snapchat stellt diese Informationen für seine Datenschutzrichtlinien nicht zur Verfügung.
{% enddetails %}

{% details Wie viele Zielgruppen kann Snapchat unterstützen? %}
Zurzeit können Sie nur 1.000 Zielgruppen in Ihrem Snapchat-Konto haben.
Wenn Sie dieses Limit überschreiten, wird Braze Sie benachrichtigen, dass wir keine neuen Audiences erstellen können.
Sie müssen in Ihr Snapchat-Anzeigenkonto gehen und Zielgruppen entfernen, die Sie nicht mehr verwenden.
{% enddetails %}

[1]: {% image_buster /assets/img/snapchat/snapchat1.png %}
[2]: {% image_buster /assets/img/snapchat/snapchat2.png %}
[3]: {% image_buster /assets/img/snapchat/snapchat3.png %}
[6]: {% image_buster /assets/img/snapchat/snapchat4.png %}
[7]: {% image_buster /assets/img/snapchat/snapchat5.png %}
[8]: {% image_buster /assets/img/snapchat/snapchat6.png %}
[9]: {% image_buster /assets/img/snapchat/snapchat7.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}