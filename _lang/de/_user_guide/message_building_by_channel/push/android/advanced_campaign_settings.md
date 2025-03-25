---
nav_title: "Erweiterte Einstellungen für Push-Kampagnen"
article_title: Erweiterte Einstellungen für Push-Kampagnen
page_order: 5
page_layout: reference
description: "Dieser Referenzartikel behandelt einige erweiterte Einstellungen für Push-Kampagnen wie Priorität, benutzerdefinierte URLs, Zustelloptionen und mehr."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Erweiterte Einstellungen für Push-Kampagnen

> Für die Push-Benachrichtigungen von Android und Fire OS, die über das Braze Dashboard gesendet werden, sind viele erweiterte Einstellungen verfügbar. Dieser Artikel beschreibt diese Funktionen und wie Sie sie erfolgreich nutzen können.

## Benachrichtigungs-ID {#notification-id}

Eine Benachrichtigungs-ID ist eine eindeutige Kennung für eine von Ihnen gewählte Nachrichtenkategorie, die dem Nachrichtendienst mitteilt, dass er nur die jüngste Nachricht mit dieser ID berücksichtigen soll. Wenn Sie eine Benachrichtigungs-ID festlegen, können Sie nur die aktuellste und relevanteste Nachricht versenden, anstatt einen Stapel veralteter, irrelevanter Nachrichten.

Um eine Benachrichtigungs-ID zuzuweisen, navigieren Sie zur Kompositionsseite des Push, dem Sie die ID hinzufügen möchten, und wählen Sie die Registerkarte **Einstellungen**. Geben Sie eine ganze Zahl in den Abschnitt **Benachrichtigungs-ID** ein. Um diese Benachrichtigung zu aktualisieren, nachdem Sie sie herausgegeben haben, senden Sie eine weitere Benachrichtigung mit der gleichen ID, die Sie zuvor verwendet haben.

![]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:80%;" }

## Lebenszeit (TTL) {#ttl}

Mit dem Feld Time-to-live (TTL) können Sie eine benutzerdefinierte Zeitspanne für die Speicherung von Nachrichten mit dem Push-Messaging-Dienst festlegen. Die Time-To-Live-Standardwerte  sind 4 Wochen für Firebase Cloud Messaging (FCM) und 31 Tage für Amazon Device Messaging (ADM).

Nehmen wir an, Ihre App ist ein Spiel und Sie bieten Ihren Nutzern einen Bonus in Form einer Spielwährung, wenn sie das Spiel täglich spielen. Sie könnten eine Push-Nachricht senden, die den Benutzer darauf hinweist, dass seine Serie zu brechen droht, wenn er eine bestimmte Anzahl von Tagen überschritten hat. Wenn ein Benutzer jedoch sein Gerät 4 Wochen später erneut mit der Spiele-App verbindet und die Zeit bis zum Start auf die Standardeinstellung setzt, sind diese Nachrichten im Nachrichtendienst bereits abgelaufen und werden nicht zugestellt.

## Priorität der Firebase-Nachrichtenzustellung {#fcm-priority}

Mit dem Feld **Priorität der Firebase-Nachrichtenzustellung** können Sie festlegen, ob ein Push mit „normaler“ oder „hoher“ Priorität an Firebase Cloud Messaging gesendet wird. Lesen Sie die [FCM Dokumentation](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message), um mehr zu erfahren.

## Textzusammenfassung

Mit dem Zusammenfassungstext können Sie zusätzlichen Text in der **erweiterten Benachrichtigungsansicht** einstellen. Der Zusammenfassungstext wird in der erweiterten Ansicht unter dem Text der Nachricht angezeigt. Es dient auch als Beschriftung für Benachrichtigungen mit Bildern.

![][9]

Bei Push-Benachrichtigungen, die Bilder enthalten, wird der Nachrichtentext in der eingeklappten Ansicht angezeigt, während der Zusammenfassungstext als Bildunterschrift angezeigt wird, wenn die Benachrichtigung erweitert wird. Sehen Sie sich die folgende Animation an, um ein Beispiel für dieses Verhalten zu sehen.

![Zusammenfassung Text Verhalten][15]

## Benutzerdefinierte URIs

Mit der Funktion **Benutzerdefinierte URI** können Sie eine Web-URL oder eine Android-Ressource angeben, zu der navigiert werden soll, wenn die Benachrichtigung angeklickt wird. Wenn kein benutzerdefinierter URI angegeben ist, gelangen Benutzer durch Klicken auf die Benachrichtigung zu Ihrer App. Sie können die angepasste URI verwenden, um Deeplinks innerhalb Ihrer App zu setzen und Nutzer:innen auf Ressourcen zu verweisen, die auch außerhalb Ihrer App existieren. Dies kann über unsere [Messaging API][13] oder in den **Einstellungen** im Push Composer festgelegt werden.

![Benutzerdefinierte URI][12]

## Benachrichtigungs-Anzeigepriorität

{% alert important %}
Die Einstellung für die Priorität der Benachrichtigungsanzeige wird auf Geräten mit Android O oder neuer nicht mehr verwendet. Bei neueren Geräten legen Sie die Priorität über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) fest.
{% endalert %}

Die Prioritätsstufe einer Push-Benachrichtigung wirkt sich darauf aus, wie Ihre Benachrichtigung im Vergleich zu anderen Benachrichtigungen in der Benachrichtigungsleiste angezeigt wird. Sie kann sich auch auf die Geschwindigkeit und die Art der Zustellung auswirken, da normale Nachrichten und Nachrichten mit geringerer Priorität mit etwas höherer Latenz oder in Stapeln gesendet werden können, um den Akku zu schonen, während Nachrichten mit hoher Priorität immer sofort gesendet werden.

Dieses Feature ist nützlich, um Ihre Nachrichten danach zu unterscheiden, wie kritisch oder zeitkritisch sie sind. Zum Beispiel wäre eine Benachrichtigung über gefährliche Straßenverhältnisse ein guter Kandidat für eine hohe Priorität, während eine Benachrichtigung über einen laufenden Verkauf eine niedrigere Priorität erhalten sollte. Sie sollten abwägen, ob die Verwendung einer störenden Priorität für die von Ihnen gesendete Benachrichtigung wirklich notwendig ist, da es sich negativ auswirken kann, wenn sie ständig an erster Stelle im Posteingang Ihrer Benutzer steht oder deren andere Aktivitäten unterbricht.

In Android O wurde die Benachrichtigungspriorität eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um die Priorität für einen Kanal während seiner Konfiguration festzulegen und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungstöne senden. Für Geräte mit Android-Versionen vor O können Sie über das Braze Dashboard und die Messaging API eine Prioritätsstufe für Android- und Fire OS-Benachrichtigungen festlegen.

Um Ihre gesamte Nutzerbasis mit einer bestimmten Priorität zu benachrichtigen, empfehlen wir Ihnen, die Priorität indirekt über die [Konfiguration des Benachrichtigungskanals][17] ] festzulegen (um O+-Geräte anzusprechen) und die individuelle Priorität über das Dashboard zu senden (um <O-Geräte anzusprechen).

In der folgenden Tabelle finden Sie die Prioritätsstufen, die Sie für Android- oder Fire OS-Push-Benachrichtigungen festlegen können:

| Priorität | Beschreibung| `priority` Wert (für API-Nachrichten) |
|------|-----------|----------------------------|
| Max. | Dringende oder zeitkritische Nachrichten. | `2` |
| Hoch | Wichtige Mitteilungen, wie z.B. eine neue Nachricht von einem Freund. | `1` |
| Standard | Die meisten Benachrichtigungen. Verwenden Sie diese Option, wenn Ihre Nachricht nicht ausdrücklich unter eine der anderen Prioritätsarten fällt. | `0` |
| Niedrig | Informationen, die Sie Ihren Benutzern mitteilen möchten, die aber keine sofortige Aktion erfordern. | `-1`|
| Min. | Kontextuelle oder Hintergrundinformationen. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen finden Sie in der Dokumentation von Google zu [Android-Benachrichtigungen][2].

## Kategorie Push

Android-Push-Benachrichtigungen bieten die Möglichkeit, anzugeben, ob Ihre Benachrichtigung in eine vordefinierte Kategorie fällt. Die Android-Benutzeroberfläche kann diese Kategorie verwenden, um zu entscheiden, wo die Benachrichtigung in der Benachrichtigungsleiste des Benutzers platziert werden soll.

![Tab „Einstellungen“, wobei die Kategorie auf „Keine“ eingestellt ist, was der Standardeinstellung entspricht.][52]

| Kategorie | Beschreibung |
|---|-------|
| Keine | Standardoption. |
| Alarm | Alarm oder Timer. |
| Anruf | Eingehender Anruf (Sprache oder Video) oder eine ähnliche Anfrage für synchrone Kommunikation. |
| E-Mail | Asynchrone Massennachrichten (E-Mail). |
| Fehler | Fehler im Hintergrundbetrieb oder Authentifizierungsstatus. |
| Event | Kalender-Event. |
| Nachricht | Eingehende Direktnachricht (SMS, Sofortnachricht, etc.). |
| Fortschritt | Fortschritt einer lang andauernden Hintergrundoperation. |
| Aktion | Promotion oder Werbung. |
| Empfehlung | Eine konkrete, zeitnahe Empfehlung für eine einzige Sache. |
| Erinnerung | Benutzergesteuerte Erinnerung. |
| Dienst | Anzeige des laufenden Hintergrunddienstes. |
| Social | Soziales Netzwerk oder Update zum Teilen. |
| Status | Laufende Informationen zum Gerät oder zum kontextuellen Status. |
| System | Aktualisierung des System- oder Gerätestatus. Reserviert für die Systemnutzung. |
| Transport | Medientransportsteuerung für die Wiedergabe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Push-Sichtbarkeit

Android-Push-Benachrichtigungen bieten ein optionales Feld, mit dem Sie festlegen können, wie eine Benachrichtigung auf dem Sperrbildschirm des Benutzers erscheint. In der folgenden Tabelle finden Sie die Sichtbarkeitsoptionen und Beschreibungen.

| Sichtbarkeit | Beschreibung |
|---|-----|
| Public | Benachrichtigung erscheint auf dem Sperrbildschirm |
| Private | Die Benachrichtigung wird mit der Meldung "Inhalt verborgen" angezeigt |
| Geheim | Die Benachrichtigung wird nicht auf dem Sperrbildschirm angezeigt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Außerdem können Android-Nutzer die Anzeige von Push-Benachrichtigungen auf dem Sperrbildschirm deaktivieren, indem sie die Datenschutzeinstellungen für Benachrichtigungen auf ihrem Gerät ändern. Diese Einstellung setzt die Sichtbarkeit der Push-Benachrichtigung außer Kraft.

![Dashboard Push-Prioritätsort mit aktivierter Sichtbarkeit und der Einstellung Privat.][53]{: style="float:right;max-width:60%;margin-left:15px;"}

Unabhängig von der Sichtbarkeit werden alle Benachrichtigungen auf dem Sperrbildschirm des Benutzers angezeigt, wenn die Datenschutzeinstellung für Benachrichtigungen auf dem Gerät **Alle Inhalte anzeigen** lautet (Standardeinstellung). Ebenso werden Benachrichtigungen nicht auf dem Sperrbildschirm angezeigt, wenn der Datenschutz für Benachrichtigungen auf **Nicht anzeigen** eingestellt ist. Die Sichtbarkeit wirkt sich nur aus, wenn der Datenschutz für Ihre Benachrichtigungen auf **Sensible Inhalte ausblenden** eingestellt ist.

Die Sichtbarkeit hat keine Auswirkungen auf Geräte vor Android Lollipop 5.0.0, d.h. alle Benachrichtigungen werden auf diesen Geräten angezeigt.

Weitere Informationen finden Sie in unserer [Android-Dokumentation][51] ].

## Benachrichtigungstöne

In Android O wurden die Benachrichtigungstöne eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um den Ton für einen Kanal während seiner Konfiguration zu definieren und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungen senden.

Für Geräte mit Android-Versionen vor Android O können Sie mit Braze den Ton einer einzelnen Push-Nachricht über den Dashboard Composer einstellen. Hierzu können Sie eine lokale Tonressource auf dem Gerät angeben (z. B. `android.resource://com.mycompany.myapp/raw/mysound`). 

Wenn Sie in diesem Feld **Standard** wählen, wird der Standard-Benachrichtigungston auf dem Gerät abgespielt. Dies kann über unsere [Messaging API][13] oder in den **Einstellungen** im Push Composer festgelegt werden.

![][11]

Als nächstes geben Sie die vollständige URI der Ton-Ressource (z. B. `android.resource://com.mycompany.myapp/raw/mysound`) in das Dashboard-Prompt ein.

Wenn Sie Ihre gesamte Nutzerbasis mit einem bestimmten Ton benachrichtigen möchten, empfehlen wir Ihnen, den Ton indirekt über die [Konfiguration des Benachrichtigungskanals][16] festzulegen (um O+ Geräte zu adressieren) und den individuellen Ton über das Dashboard zu senden (um <O Geräte zu adressieren).

[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
[17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels
[51]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
