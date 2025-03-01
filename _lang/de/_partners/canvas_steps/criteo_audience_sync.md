---
nav_title: Criteo
article_title: Canvas Audience Sync mit Criteo
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync mit Criteo verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
page_order: 1
alias: "/audience_sync_criteo/"

Tool:
  - Canvas
---

# Audience Sync mit Criteo

Mit der Braze Audience Sync to Criteo können Marken Benutzerdaten aus ihrer eigenen Braze-Integration zu Criteo-Kundenlisten hinzufügen, um Werbung auf der Grundlage von Verhaltensauslösern, Segmentierung und mehr zu liefern. Alle Kriterien, die Sie normalerweise verwenden, um eine Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze Canvas auf der Grundlage Ihrer Benutzerdaten auszulösen, können jetzt verwendet werden, um eine Anzeige für diesen Benutzer in Ihren Criteo-Kundenlisten auszulösen.

**Häufige Anwendungsfälle für die Synchronisierung von Zielgruppen sind:**

- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut ansprechen
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind
- Erstellen von Lookalike Audiences zur effizienteren Gewinnung neuer Benutzer

Diese Funktion gibt Marken die Möglichkeit, zu kontrollieren, welche spezifischen First-Party-Daten mit Criteo geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro Haftungsausschluss**<br>
Braze Audience Sync to Criteo ist eine Audience Sync Pro Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager. <br> 
{% endalert %}

## Voraussetzungen 

Sie müssen sicherstellen, dass Sie die folgenden Elemente erstellt und/oder abgeschlossen haben, bevor Sie Ihre Audience Sync mit Criteo einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Criteo Werbekonto | [Criteo](https://marketing.criteo.com/) | Ein aktives Criteo-Anzeigenkonto, das mit Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr Criteo-Administrator Ihnen die entsprechenden Berechtigungen für den Zugriff auf Audiences erteilt hat. |
| [Criteo Werberichtlinien](https://www.criteo.com/advertising-guidelines/)<br>und<br>[Criteo Richtlinien zur Markensicherheit](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Als aktiver Kunde von Criteo müssen Sie sicherstellen, dass Sie die Richtlinien für Werbung und Markensicherheit von Criteo einhalten können, bevor Sie Kampagnen von Criteo starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Schritt 1: Mit Criteo verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Criteo**. Wählen Sie unter Criteo Audience Export die Option **Connect Criteo**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

![Criteo-Technologie-Seite in Braze, die einen Übersichtsbereich und einen Criteo-Bereich mit der Schaltfläche Connected Criteo enthält.][5]{: style="max-width:80%;"}

Es erscheint eine Criteo oAuth-Seite, auf der Sie Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync-Integration autorisieren.

Nachdem Sie bestätigt haben, werden Sie zurück zu Braze geleitet, um die Criteo-Anzeigenkonten auszuwählen, mit denen Sie synchronisieren möchten. 

![Eine Liste der verfügbaren Werbekonten, die Sie mit Criteo verbinden können.][7]{: style="max-width:80%;"}

Sobald Sie sich erfolgreich verbunden haben, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Eine aktualisierte Version der Seite für Criteo-Technologiepartner, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.][4]{: style="max-width:80%;"}

Ihre Criteo-Verbindung wird auf der Ebene des Braze-Arbeitsbereichs angewendet. Wenn Ihr Criteo-Administrator Sie aus Ihrem Criteo-Anzeigenkonto entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die Criteo verwenden, Fehler anzeigen, und Braze kann die Benutzer nicht synchronisieren.

### Schritt 2: Konfigurieren Sie Ihre Canvas-Eingabekriterien

Wenn Sie Zielgruppen für das Ad-Tracking aufbauen, möchten Sie möglicherweise bestimmte Nutzer auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, z. B. das Recht "Nicht verkaufen oder weitergeben" gemäß [CCPA](https://oag.ca.gov/privacy/ccpa). Vermarkter sollten die entsprechenden Filter für die Eignung der Nutzer in ihre Canvas-Eingabekriterien integrieren. Nachfolgend finden Sie einige Optionen.

Wenn Sie die [iOS IDFA über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) gesammelt haben, können Sie den Filter "Ads Tracking Enabled" verwenden. Wählen Sie den Wert true, um Benutzer nur an Audience Sync-Ziele zu senden, für die sie sich angemeldet haben.

![][11]

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante benutzerdefinierte Attribute sammeln, sollten Sie diese als Filter in Ihre Canvas-Eingabekriterien aufnehmen:

![][12]

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance/).

### Schritt 3: Hinzufügen eines Audience Sync-Schrittes mit Criteo

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![Arbeitsablauf der vorherigen Schritte zum Hinzufügen einer Criteo Audience Komponente in Canvas Flow.][9]{: style="max-width:35%;"} ![Arbeitsablauf der vorherigen Schritte zum Hinzufügen einer Criteo Audience Komponente in Canvas Flow.][10]{: style="max-width:28%;"}

### Schritt 4: Sync-Einrichtung

Klicken Sie auf die Schaltfläche **Benutzerdefinierte Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **Criteo** als den gewünschten Audience Sync-Partner. 

![][6]

Wählen Sie dann Ihr gewünschtes Criteo-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Ein neues Publikum schaffen %}
**Ein neues Publikum schaffen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Benutzer zur Zielgruppe hinzufügen** und wählen Sie die Felder, die Sie mit Criteo synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche **Zielgruppe erstellen** klicken.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier wird das gewünschte Anzeigenkonto ausgewählt und eine neue Zielgruppe erstellt.]({% image_buster /assets/img/criteo/criteo3.png %})

Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auch später in der Canvas-Reise auf diese Zielgruppe verweisen, um sie zu entfernen.

![Eine Warnung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/criteo/criteo1.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Benutzer nahezu in Echtzeit, sobald sie die Komponente Audience Sync betreten.
{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}
**Synchronisieren Sie mit einer bestehenden Zielgruppe**<br>
Braze bietet auch die Möglichkeit, Nutzer zu bestehenden Criteo Audiences hinzuzufügen, um sicherzustellen, dass diese Audiences aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und **fügen Sie sie der Zielgruppe hinzu**. Braze fügt dann entweder Benutzer in nahezu Echtzeit hinzu, wenn sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Schritts Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

Sobald Sie Ihre Audience Sync mit Criteo konfiguriert haben, starten Sie einfach die Canvas! Die neue Zielgruppe wird erstellt und die Nutzer, die den Schritt Audience Sync durchlaufen, werden in diese Zielgruppe auf Criteo weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Benutzer zum nächsten Schritt in ihrer User Journey übergehen.

Sie können die Zielgruppe in Criteo einsehen, indem Sie in Ihr Ads Manager-Konto gehen und dann Segmente aus der **Zielgruppenbibliothek** in der Navigation auswählen. Auf der Seite **Segmente** sehen Sie die Größe der einzelnen Zielgruppen, sobald sie ~1.000 erreicht haben.

![Die Hörerbibliothek zeigt das Segment, die ID, die Quelle, den Typ, die Größe, die aktuelle Verwendung und die letzte Aktualisierung an.][0]

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung

Wenn Benutzer die Stufe Audience Sync erreichen, synchronisiert Braze diese Benutzer nahezu in Echtzeit und respektiert dabei auch die API-Ratenbeschränkungen von Criteo. In der Praxis bedeutet dies, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer wie möglich zu verarbeiten, bevor diese Nutzer an Snapchat weitergeleitet werden.

Die API-Rate von Criteo ist auf maximal 250 Anfragen pro Minute begrenzt. Wenn ein Braze-Kunde dieses Ratenlimit erreicht, wird Braze the Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt. 

## Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Aufgenommen | Anzahl der Benutzer, die diese Komponente eingegeben haben, die mit Criteo synchronisiert werden soll. |
| Fortgefahren mit nächstem Schritt | Wie viele Benutzer sind zur nächsten Komponente weitergegangen, falls es eine gibt. Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Benutzer, die erfolgreich mit Criteo synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit Criteo bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Benutzer, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Criteo synchronisiert wurden. Mögliche Fehlerursachen sind z.B. ein ungültiges Criteo-Token oder wenn die Zielgruppe auf Criteo gelöscht wurde. |
| Canvas verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei den Berichten über synchronisierte Benutzer und fehlerhafte Benutzer kommen wird.
{% endalert %}

## Fehlersuche

{% details Was sollte ich als nächstes tun, wenn ich einen ungültigen Token-Fehler erhalte? %}
Sie können die Verbindung zu Ihrem Criteo-Konto auf der Criteo-Partnerseite einfach trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Criteo-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.
{% enddetails %}

{% details Warum kann mein Canvas nicht gestartet werden? %}
Stellen Sie sicher, dass Ihr Criteo-Anzeigenkonto auf der Criteo-Partnerseite erfolgreich mit Braze verbunden wurde.

Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben
{% enddetails %}

{% details Woher weiß ich, ob die Benutzer übereinstimmen, nachdem ich sie an Criteo weitergegeben habe? %}
Criteo stellt diese Informationen nicht für seine eigenen Datenschutzrichtlinien zur Verfügung.
{% enddetails %}

{% details Wie viele Zielgruppen kann Criteo unterstützen? %}
Zurzeit können Sie nur 1.000 Zielgruppen in Ihrem Criteo-Konto haben. 

Wenn Sie dieses Limit überschreiten, wird Braze Sie darüber informieren, dass wir keine neuen Zielgruppen erstellen können. 

Sie müssen in Ihr Criteo-Anzeigenkonto gehen und Zielgruppen entfernen, die Sie nicht mehr verwenden.
{% enddetails %} 

[0]: {% image_buster /assets/img/criteo/criteo.png %}
[1]: {% image_buster /assets/img/criteo/criteo1.png %}
[2]: {% image_buster /assets/img/criteo/criteo2.png %}
[3]: {% image_buster /assets/img/criteo/criteo3.png %}
[4]: {% image_buster /assets/img/criteo/criteo4.png %}
[5]: {% image_buster /assets/img/criteo/criteo5.png %}
[6]: {% image_buster /assets/img/criteo/criteo6.png %}
[7]: {% image_buster /assets/img/criteo/criteo7.png %}
[8]: {% image_buster /assets/img/criteo/criteo8.png %}
[9]: {% image_buster /assets/img/criteo/criteo9.png %}
[10]: {% image_buster /assets/img/criteo/criteo10.png %}
[11]: {% image_buster /assets/img/criteo/criteo11.png %}
[12]: {% image_buster /assets/img/criteo/criteo12.png %}
