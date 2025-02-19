---
nav_title: "Push-Registrierung"
article_title: Push-Registrierung
page_order: 2
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was es bedeutet, für Push registriert zu sein und wie wir bei Braze Push-Nachrichten versenden und mit Push-Tokens und Push-Registrierung umgehen."
channel:
  - push

---

# Push-Registrierung

> In diesem Artikel erfahren Sie, wie einem Benutzer ein Push-Token zugewiesen wird und wie Braze Push-Nachrichten an Ihre Benutzer sendet.

## Push-Token

Um zu verstehen, wie wir hier bei Braze Push-Nachrichten versenden, ist es wichtig zu wissen, was Push-Token sind. Push-Tokens sind eine eindeutige anonyme Kennung, die vom Gerät eines Benutzers generiert und an Braze gesendet wird, um zu ermitteln, wohin die Benachrichtigung des jeweiligen Empfängers zu senden ist. Wenn ein Gerät keinen Push-Token hat, können Sie keinen Push an das Gerät senden.

Push-Tokens werden von Push-Dienstanbietern generiert. Braze stellt eine Verbindung zu Anbietern von Push-Diensten wie Firebase Cloud Messaging Service (FCMs) für Android und Apple Push Notification Service (APNs) für iOS her. Diese Anbieter senden eindeutige Geräte-Token, die Ihre App identifizieren. Jedes Gerät verfügt über einen eindeutigen Token, der für Messaging verwendet wird. Token können [ablaufen](#push-token-expire) oder aktualisiert werden.

Es gibt zwei Möglichkeiten, wie [ein Push-Token][Push-Token]] klassifiziert werden. Diese sind wichtig, um zu verstehen, wie eine Push-Benachrichtigung an Ihre Benutzer gesendet werden kann.

1. **Foreground Push** bietet die Möglichkeit, regelmäßig sichtbare Push-Benachrichtigungen in den Vordergrund des Geräts eines Benutzers zu senden.
2. **Push-Benachrichtigungen im Hintergrund** sind unabhängig davon verfügbar, ob sich ein bestimmtes Gerät für den Empfang von Push-Benachrichtigungen der jeweiligen Marke entschieden hat. Mit dem Hintergrund-Push können Marken stille Push-Benachrichtigungen – also Benachrichtigungen, die absichtlich nicht angezeigt werden – an Geräte senden, um wichtige Funktionen wie das Tracking der Deinstallation zu unterstützen.

Wenn ein Nutzerprofil über ein gültiges Vordergrund-Push-Token verfügt, das mit einer App verknüpft ist, betrachtet Braze den Nutzer als „Push-registriert“ für die jeweilige App. Braze bietet daher einen speziellen Filter für die Segmentierung, `Push enabled for App,`, um diese Nutzer:innen zu identifizieren.

{% alert note %}
Der Filter `Push enabled for App` berücksichtigt nur das Vorhandensein eines gültigen Vordergrund- oder Hintergrund-Push-Tokens für die jeweilige App. Der allgemeinere Filter `Push Enabled` hingegen segmentiert Benutzer, die explizit Push-Benachrichtigungen für beliebige Apps in Ihrem Arbeitsbereich aktiviert haben. Diese Zählung umfasst nur den Vordergrund-Push und schließt Nutzer:innen, die sich abgemeldet haben, nicht mit ein. Mehr über diese und andere Filter erfahren Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Mehrere Benutzer auf einem Gerät

Push-Token sind sowohl für ein Gerät als auch für eine App spezifisch. Es ist also nicht möglich, mit Push-Token zwischen mehreren Nutzer:innen zu unterscheiden, die dasselbe Gerät verwenden.

Nehmen wir zum Beispiel an, Sie haben zwei Benutzer: Charlie und Kim. Wenn Charlie auf seinem Telefon Push-Benachrichtigungen für Ihre App aktiviert hat und Kim Charlies Telefon benutzt, um sich von Charlies Profil abzumelden und bei ihrem eigenen anzumelden, wird das Push-Token erneut Kims Profil zugewiesen. Das Push-Token bleibt dann Kims Profil auf diesem Gerät zugewiesen, bis sie sich abmeldet und Charlie sich wieder anmeldet.

Eine App oder Website kann nur ein Push-Abonnement pro Gerät haben. Wenn sich also ein Benutzer von einem Gerät oder einer Website abmeldet und sich ein neuer Benutzer anmeldet, wird das Push-Token dem neuen Benutzer neu zugewiesen. Dies wird im Profil des Benutzers im Abschnitt **Kontakteinstellungen** auf der Registerkarte **Engagement** angezeigt:

![Push-Token-Changelog auf dem Tab \*\*Engagement** des Profils eines Nutzers oder einer Nutzerin. Hier wird aufgeführt, wann der Push-Token an eine:n andere:n Nutzer:in weitergegeben wurde und um welchen Token es sich handelte.][4]

Da es für Push-Anbieter (APNs/FCMs) keine Möglichkeit gibt, zwischen mehreren Benutzern auf einem Gerät zu unterscheiden, übergeben wir das Push-Token an den zuletzt eingeloggten Benutzer, um zu bestimmen, welcher Benutzer auf dem Gerät für Push angesprochen werden soll.

## Push-Token-Registrierung

Plattformen handhaben die Registrierung von Push-Token und Push-Berechtigungen auf unterschiedliche Weise:

- **Android**:
  - **Android 13**:<br>Die Push-Erlaubnis muss vom Nutzer oder von der Nutzerin angefordert und erteilt werden. Erhält ein Token, nachdem der oder die Nutzer:in die Genehmigung erteilt hat. Ihre App kann den Benutzer zu gegebener Zeit manuell um Erlaubnis bitten, aber wenn nicht, werden die Benutzer automatisch gefragt, nachdem Ihre App einen [Benachrichtigungskanal](https://developer.android.com/reference/android/app/NotificationChannel) erstellt hat.
  - **Android 12 und früher**:<br>Alle Nutzer:innen werden bei ihrer ersten Sitzung als `Subscribed` betrachtet, wenn Braze automatisch ein Push-Token anfordert. Zu diesem Zeitpunkt ist der oder die Nutzer:in mit einem gültigen Push-Token für dieses Gerät und einem Standard Abo-Status von `Subscribed`**aktiviert**.<br><br>
- **iOS**: Nicht automatisch für Push registriert.
    - **iOS 12 (mit vorläufiger Autorisierung)**: <br>Ihre App kann eine [vorläufige Autorisierung]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push) oder einen autorisierten Push anfordern. Autorisiertes Push erfordert die explizite Erlaubnis eines Benutzers, bevor er eine Benachrichtigung senden kann (er erhält ein Token, nachdem der Benutzer die Erlaubnis erteilt hat), während [provisional push][provisional-blog] ] es Ihnen ermöglicht, Benachrichtigungen __unauffällig__ direkt an die Benachrichtigungszentrale zu senden, ohne dass ein Ton oder eine Warnung ausgegeben wird.
    - **iOS 11 und höher & iOS 12 (ohne vorläufige Autorisierung)**: <br>Alle Nutzer:innen müssen sich ausdrücklich für den Empfang von Push-Benachrichtigungen entscheiden. Nachdem sich die Nutzer:innen angemeldet haben, erhalten sie einen Token.<br><br>
- **Internet:** Sie müssen das Opt-in von Nutzer:innen über das Dialogfeld für die native Browser-Berechtigung anfordern. Sie erhalten ein Token, nachdem Nutzer:innen ein Opt-in durchgeführt haben.  Im Gegensatz zu iOS und Android, bei denen Ihre App die Eingabeaufforderung jederzeit anzeigen kann, zeigen einige moderne Browser die Aufforderung nur an, wenn sie durch eine "Benutzergeste" (Mausklick oder Tastendruck) ausgelöst wird. Wenn Ihre Website versucht, beim Laden der Seite die Berechtigung für Push-Benachrichtigungen anzufordern, wird dies wahrscheinlich vom Browser ignoriert oder unterdrückt.

| Push-Token erhalten | Push-Token senden |
| ---------------- | ----------------- |
| Anwendungen müssen sich bei einem Push-Anbieter registrieren, um ein Push-Token für ein Gerät zu erhalten. | Entwickler:innen können dann das Gerät mithilfe des von FCM/APNs generierten Push-Tokens erreichen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Überprüfen Sie den Status des Push-Abonnements des Benutzers

![Benutzerprofil von John Doe, dessen Push-Abonnementstatus auf Abonniert gesetzt ist.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, den Status des Push-Abos eines Nutzers:innen mit Braze zu überprüfen:

1. **Benutzerprofil**: Sie können über das Braze-Dashboard auf der Seite [Nutzersuche][5] ] auf einzelne Nutzerprofile zugreifen. Nachdem Sie das Profil eines Benutzers gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Benutzer-ID), können Sie die Registerkarte **Engagement** auswählen, um den Abonnementstatus eines Benutzers anzuzeigen und manuell anzupassen. 
<br>
2. **Rest API Export**: Sie können einzelne Nutzerprofile im JSON-Format exportieren, indem Sie die Endpunkte [Nutzer:innen nach Segmenten][Segment] oder [Nutzer:innen nach Bezeichner][Bezeichner] verwenden. Braze gibt ein Push-Token-Objekt zurück, das Push-Enablement-Informationen pro Gerät enthält.

### Überprüfen des Push-Registrierungsstatus

Auf der Registerkarte **Engagement** im Profil eines Benutzers sehen Sie **Push registriert für** gefolgt von einem App-Namen. Wenn keine App-Informationen für dieses Gerät vorhanden sind, sehen Sie zwei Striche**(--**). Für jedes Gerät, das dem oder der Nutzer:in gehört, gibt es einen Entry.

Wenn dem App-Namen des Geräteeintrags das Präfix `Foreground:` vorangestellt ist, ist die App berechtigt, auf diesem Gerät sowohl Push-Benachrichtigungen im Vordergrund (für den Benutzer sichtbar) als auch im Hintergrund (für den Benutzer nicht sichtbar) zu empfangen.

![Push-Changelog mit einem Beispiel für ein Push-Token.][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Wenn dem App-Namen des Geräteeintrags hingegen `Background:` vorangestellt ist, ist die App nur berechtigt, [Push-Nachrichten im Hintergrund]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) zu empfangen und kann keine für den Benutzer sichtbaren Benachrichtigungen auf diesem Gerät anzeigen. Dies bedeutet in der Regel, dass der Benutzer die Benachrichtigungen für die App auf diesem Gerät deaktiviert hat.

Wenn ein Push-Token auf einen anderen Benutzer auf demselben Gerät übertragen wird, wird der erste Benutzer nicht mehr für Push registriert.

## Push-Token-Verwaltung

In der folgenden Tabelle finden Sie Aktionen, die zur Änderung oder Entfernung von Push-Tokens aus Benutzerprofilen führen. 

| Aktion | Beschreibung |
| ------ | ----------- |
| `changeUser()`-Methode aufgerufen | Die `changeUser()`-Methode von Braze wechselt die Nutzer-ID, dem die SDKs Daten zum Nutzerverhalten zuordnen. Diese Methode wird normalerweise aufgerufen, wenn sich ein:e Nutzer:in bei einer Anwendung anmeldet. Wenn `changeUser()` mit einer anderen oder neuen Benutzer-ID auf einem bestimmten Gerät aufgerufen wird, wird das Push-Token dieses Geräts in das entsprechende Braze-Profil mit der entsprechenden Benutzer-ID verschoben. |
| Push-Fehler tritt auf | Einige häufige Push-Fehler, die zur Entfernung von Token führen, sind `MismatchSenderId`, `InvalidRegistration` und andere Arten von Push-Bounces. <br><br>Sehen Sie sich unsere vollständige Liste der häufigsten [Push-Fehler][errors] an. |
| Nutzer:in deinstalliert | Wenn ein Benutzer die Anwendung von einem Gerät deinstalliert, entfernt Braze das Push-Token des Benutzers aus dem Profil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Wie sieht das auf breiterer Ebene aus?

Wenn ein:e Nutzer:in eine neue Anwendung öffnet und den Push-Zugriff über eine Push-Eingabeaufforderung gewährt, wird ein Aufruf vom Braze-SDK an die Push-Anbieter getätigt. Wenn dieser Aufruf getätigt wird, überprüft der Push-Anbieter, ob alles korrekt eingerichtet ist. Wenn ja, wird ein Push-Token an Ihr Gerät übermittelt. Wenn dieses Token eintrifft, teilt das SDK dies Braze mit. Nachdem Braze das Token vom Push-Anbieter erhalten hat, aktualisieren oder erstellen wir ein neues Nutzerprofil. Diese Benutzer gelten jetzt als registriert.

Wenn wir eine Kampagne starten möchten, erstellen wir in Braze eine Kampagne, die eine Push-Nutzlast erzeugt, die an den Push-Anbieter gesendet wird. Von dort aus stellt der Anbieter die Push-Nutzdaten dem Gerät des Nutzers oder der Nutzerin zu und das SDK übergibt den Messaging-Status an Braze.

![Ein Flussdiagramm, das den oben genannten Push-Prozess zwischen Braze, dem oder der Kund:in und dem Apple Push Notification Service oder Firebase Cloud Messaging abbildet.][push-process]

| Registrierungsschritte | Messaging-Schritte |
| ------------------ | --------------- |
| 1\. Kund:in (Gerät) registriert sich beim Push-Anbieter<br>2\. Anbieter erzeugt und liefert Push-Token<br>3\. Flush-Token in Braze |1\. Braze sendet Push-Nutzdaten an Anbieter<br>2\. Anbieter liefert die Push-Nutzdaten an das Gerät<br>3\. SDK übergibt Messaging-Statistiken an Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Was passiert, wenn ein angemeldeter Benutzer meine App löscht und dann erneut herunterlädt?

Angenommen, ein Benutzer entscheidet sich für Push, erhält einige Push-Nachrichten und löscht die App später. Dadurch wird die Push-Einwilligung auf der Geräteebene entfernt. Von hier aus wird die erste abgelehnte Push-Nachricht nach der Deinstallation automatisch dazu führen, dass diese:r Nutzer:in von zukünftigen Push-Nachrichten ausgeschlossen wird. Wenn ein Benutzer danach die App neu installiert, aber nicht startet, kann Braze keine Push-Nachrichten an den Benutzer senden, da die Push-Tokens für Ihre App nicht erneut vergeben wurden.

Wenn ein Benutzer die Vordergrund-Push-Funktion wieder aktivieren würde, müsste er außerdem eine Sitzung starten, um diese Informationen in seinem Benutzerprofil zu aktualisieren, damit er Push-Nachrichten empfangen kann.
 
### Wann laufen Push-Tokens ab? {#push-token-expire}

Leider ist dies in den APNs und FCM nicht wirklich definiert. Push-Tokens können ablaufen, wenn eine App aktualisiert wird, wenn Benutzer ihre Daten auf ein neues Gerät übertragen oder wenn sie ein Betriebssystem neu installieren. Im Großen und Ganzen haben wir keine Insights darüber, warum Push-Anbieter bestimmte Push-Token ablaufen lassen.

Um dieser Unklarheit Rechnung zu tragen, werden bei unseren SDK-Push-Integrationen Token immer bei Sitzungsbeginn registriert und gelöscht, um sicherzustellen, dass wir über das aktuellste Token verfügen.

[errors]: {{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[push-process]: {% image_buster /assets/img/push_process.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[2]: {% image_buster /assets/img/push_changelog.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {% image_buster /assets/img/push_token_changelog.png %}


