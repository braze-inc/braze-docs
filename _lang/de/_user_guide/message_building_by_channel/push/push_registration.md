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

## Über Push-Token {#push-tokens}

Wenn eine App Push-Berechtigungen von einem Gerät anfragt, generiert der Anbieter des Push-Dienstes des Geräts ein Push-Token für diese App. Jede App erhält ihr eigenes eindeutiges, anonymes Push-Token, mit dem sie das Gerät und die aktuelle App-Instanz beim Senden einer Push-Benachrichtigung identifiziert.

Denken Sie daran, dass Push-Token keine statischen Bezeichner sind, die ewig halten - sie können aktualisiert werden und [ablaufen](#push-token-expire).

{% alert tip %}
Plattformspezifische Details finden Sie unter [Push-Token Registrierung](#push-token-registration).
{% endalert %}

### Push im Vordergrund vs. Hintergrund {#foreground-vs-background}

Push-Token werden verwendet, um Push-Benachrichtigungen sowohl im Vordergrund als auch im Hintergrund zu versenden.

| Typ       | Erfordert Opt-in? | Beschreibung                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Push für den Vordergrund | Ja       | Eine Benachrichtigung wird für den Nutzer:innen sichtbar angezeigt, während die App im Vordergrund ist.           |
| Hintergrund-Push | Kein:e        | Eine Benachrichtigung wird stillschweigend im Hintergrund zugestellt, ohne angezeigt zu werden. Wird oft für Funktionen wie Uninstall-Tracking verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn ein Nutzer:innen für Push-Benachrichtigungen für Ihre App optiert, wird er als "Push-registriert" betrachtet, d.h. er kann jetzt mit dem Segmentierungsfilter `Foreground Push Enabled for App` in Braze gezielt angesprochen werden.

{% alert note %}
Dies unterscheidet sich von dem Segmentierungsfilter `Foreground Push Enabled`, der dazu dient, Nutzer:innen zu identifizieren, die sich für mindestens eine Ihrer Apps entschieden haben - nicht für eine bestimmte App. Weitere Informationen finden Sie unter [Filter für die Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#foreground-push-enabled).
{% endalert %}

### Mehrere Nutzer:innen auf einem Gerät

Push-Tokens sind sowohl für das Gerät als auch für die App eindeutig. Das bedeutet, dass Push-Tokens nicht zum Targeting bestimmter Nutzer:innen verwendet werden können, wenn mehrere Nutzer:innen das gleiche Gerät verwenden.

Nehmen wir zum Beispiel an, Sie haben zwei Benutzer: Charlie und Kim. Wenn Charlie auf seinem Telefon Push-Benachrichtigungen für Ihre App aktiviert hat und Kim Charlies Telefon benutzt, um sich von Charlies Profil abzumelden und bei ihrem eigenen anzumelden, wird das Push-Token erneut Kims Profil zugewiesen. Das Push-Token bleibt dann Kims Profil auf diesem Gerät zugewiesen, bis sie sich abmeldet und Charlie sich wieder anmeldet.

Eine App oder Website kann nur ein Push-Abonnement pro Gerät haben. Wenn sich also ein Benutzer von einem Gerät oder einer Website abmeldet und sich ein neuer Benutzer anmeldet, wird das Push-Token dem neuen Benutzer neu zugewiesen. Dies wird im Profil des Benutzers im Abschnitt **Kontakteinstellungen** auf der Registerkarte **Engagement** angezeigt:

Changelog des Push-Tokens auf dem Tab \*\*Engagement** des Profils eines Nutzers, der auflistet, wann der Push-Token zu einem anderen Nutzer verschoben wurde und was der Token war.]({% image_buster /assets/img/push_token_changelog.png %})

Da es für Push-Anbieter (APNs/FCMs) keine Möglichkeit gibt, zwischen mehreren Benutzern auf einem Gerät zu unterscheiden, übergeben wir das Push-Token an den zuletzt eingeloggten Benutzer, um zu bestimmen, welcher Benutzer auf dem Gerät für Push angesprochen werden soll.

## Push-Token-Registrierung

Jede Geräteplattform handhabt die Push-Token-Registrierung anders. Im Folgenden finden Sie plattformspezifische Details:

{% tabs local %}
{% tab android %}
Bei der Installation Ihrer App wird automatisch ein Push-Token für Ihre App generiert. Dieses Token kann jedoch nur für [Push-Benachrichtigungen im Hintergrund](#foreground-vs-background) verwendet werden, bis der Nutzer:innen sich ausdrücklich dafür entscheidet. Außerdem wird die Registrierung in den verschiedenen Android-Versionen unterschiedlich gehandhabt:

| Version       | Details                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | Die Push-Erlaubnis muss vom Nutzer:innen angefragt und erteilt werden. Ihre App kann die Erlaubnis manuell anfragen, oder die Nutzer:innen werden automatisch aufgefordert, nachdem ein [Benachrichtigungskanal](https://developer.android.com/reference/android/app/NotificationChannel) erstellt wurde. |
| **Android 12 und früher** | Alle Nutzer:innen werden nach ihrer ersten Sitzung als `Subscribed` betrachtet. Braze fragt an dieser Stelle automatisch ein Push-Token an, wodurch der Nutzer:in mit einem gültigen Token und dem Standard-Abostatus `Subscribed` für Push aktiviert wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab ios %}
iOS erzeugt nicht automatisch Push-Tokens für eine App, wenn diese installiert wird. Außerdem wird die Registrierung in den verschiedenen iOS-Versionen unterschiedlich gehandhabt: 

| Version                         | Vorläufige Autorisierung? | Details                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Ja                         | Wenn ein Nutzer:in für Push-Benachrichtigungen optiert, erhalten Sie eine Standardberechtigung, die es Ihnen erlaubt, [Push-Benachrichtigungen im Vordergrund](#foreground-vs-background) zu senden. Sie können jedoch auch eine [vorläufige Autorisierung]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push) anfragen, mit der Sie [Push-Benachrichtigungen](#foreground-vs-background) im Hintergrund direkt an das Notification Center senden können. |
| **iOS 11 und höher** | Kein:e                          | Alle Nutzer:innen müssen sich ausdrücklich für den Empfang von Push-Benachrichtigungen entscheiden. Ein Push-Token wird erst generiert, nachdem die Erlaubnis erteilt wurde.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab web %}
Sie müssen das Opt-in von Nutzer:innen über das Dialogfeld für die native Browser-Berechtigung anfordern. Sie erhalten ein Token, nachdem Nutzer:innen ein Opt-in durchgeführt haben. Im Gegensatz zu iOS und Android, bei denen Ihre App die Eingabeaufforderung jederzeit anzeigen kann, zeigen einige moderne Browser die Aufforderung nur an, wenn sie durch eine "Benutzergeste" (Mausklick oder Tastendruck) ausgelöst wird. Wenn Ihre Website versucht, beim Laden der Seite eine Einwilligung in Push-Benachrichtigungen einzuholen, wird sie wahrscheinlich vom Browser ignoriert oder stummgeschaltet.
{% endtab %}
{% endtabs %}

### Überprüfung des Status des Push-Abos des Nutzers:in

Nutzerprofil für John Doe, dessen Push-Abonnement auf Abo eingestellt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, den Status des Push-Abos eines Nutzers:innen mit Braze zu überprüfen:

- **Benutzerprofil**: Sie können über das Braze-Dashboard auf der Seite [Nutzersuche]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) auf die Profile der einzelnen Nutzer:innen zugreifen. Nachdem Sie das Profil eines Benutzers gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Benutzer-ID), können Sie die Registerkarte **Engagement** auswählen, um den Abonnementstatus eines Benutzers anzuzeigen und manuell anzupassen.
- **Rest API exportieren**: Mit den Endpunkten [Benutzer:innen nach Segmenten]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) oder [Benutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) exportieren können Sie einzelne Nutzerprofile im JSON-Format exportieren. Braze gibt ein Push-Token-Objekt mit gerätespezifischen Push-Aktivierungsdaten zurück.

### Überprüfen des Push-Registrierungsstatus

Auf der Registerkarte **Engagement** im Profil eines Benutzers sehen Sie **Push registriert für** gefolgt von einem App-Namen. Wenn keine App-Informationen für dieses Gerät vorhanden sind, sehen Sie zwei Striche**(--**). Für jedes Gerät, das dem oder der Nutzer:in gehört, gibt es einen Entry.

Wenn dem App-Namen des Geräteeintrags das Präfix `Foreground:` vorangestellt ist, ist die App berechtigt, auf diesem Gerät sowohl Push-Benachrichtigungen im Vordergrund (für den Benutzer sichtbar) als auch im Hintergrund (für den Benutzer nicht sichtbar) zu empfangen.

![Push Changelog mit einem Beispiel Push-Token.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Wenn dem App-Namen des Geräteeintrags hingegen `Background:` vorangestellt ist, ist die App nur berechtigt, [Push-Nachrichten im Hintergrund]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) zu empfangen und kann keine für den Benutzer sichtbaren Benachrichtigungen auf diesem Gerät anzeigen. Dies bedeutet in der Regel, dass der Benutzer die Benachrichtigungen für die App auf diesem Gerät deaktiviert hat.

Wenn ein Push-Token auf einen anderen Benutzer auf demselben Gerät übertragen wird, wird der erste Benutzer nicht mehr für Push registriert.

## Push-Token-Verwaltung

In der folgenden Tabelle finden Sie Aktionen, die zur Änderung oder Entfernung von Push-Tokens aus Benutzerprofilen führen. 

| Aktion | Beschreibung |
| ------ | ----------- |
| `changeUser()`-Methode aufgerufen | Die `changeUser()`-Methode von Braze wechselt die Nutzer-ID, dem die SDKs Daten zum Nutzerverhalten zuordnen. Diese Methode wird normalerweise aufgerufen, wenn sich ein:e Nutzer:in bei einer Anwendung anmeldet. Wenn `changeUser()` mit einer anderen oder neuen Benutzer-ID auf einem bestimmten Gerät aufgerufen wird, wird das Push-Token dieses Geräts in das entsprechende Braze-Profil mit der entsprechenden Benutzer-ID verschoben. |
| Push-Fehler tritt auf | Einige häufige Push-Fehler, die zur Entfernung von Token führen, sind `MismatchSenderId`, `InvalidRegistration` und andere Arten von Push-Bounces. <br><br>Sehen Sie sich unsere vollständige Liste der häufigsten [Push-Fehler]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid) an. |
| Nutzer:in deinstalliert | Wenn ein Benutzer die Anwendung von einem Gerät deinstalliert, entfernt Braze das Push-Token des Benutzers aus dem Profil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Wie sieht das auf breiterer Ebene aus?

Wenn ein:e Nutzer:in eine neue Anwendung öffnet und den Push-Zugriff über eine Push-Eingabeaufforderung gewährt, wird ein Aufruf vom Braze-SDK an die Push-Anbieter getätigt. Wenn dieser Aufruf getätigt wird, überprüft der Push-Anbieter, ob alles korrekt eingerichtet ist. Wenn ja, wird ein Push-Token an Ihr Gerät übermittelt. Wenn dieses Token eintrifft, teilt das SDK dies Braze mit. Nachdem Braze das Token vom Push-Anbieter erhalten hat, aktualisieren oder erstellen wir ein neues Nutzerprofil. Diese Benutzer gelten jetzt als registriert.

Wenn wir eine Kampagne starten möchten, erstellen wir in Braze eine Kampagne, die eine Push-Nutzlast erzeugt, die an den Push-Anbieter gesendet wird. Von dort aus stellt der Anbieter die Push-Nutzdaten dem Gerät des Nutzers oder der Nutzerin zu und das SDK übergibt den Messaging-Status an Braze.

![Ein Flussdiagramm, das den oben erwähnten Push-Prozess zwischen Braze, den Kund:innen und dem Apple Push-Benachrichtigungsdienst oder Firebase Cloud Messaging abbildet.]({% image_buster /assets/img/push_process.png %})

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
