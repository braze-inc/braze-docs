---
nav_title: "Push Enablement und Abo"
article_title: Push-Aktivierung und Abonnement
page_order: 3
page_type: reference
description: "Dieser Artikel erläutert Push-Aktivierung und Push-Abonnement in Braze sowie grundlegende Unterschiede zwischen iOS, Android und Web."
channel:
  - push

---

# Push-Aktivierung und Push-Abonnement

> Dieser Artikel erläutert Push-Aktivierung und Push-Abostatus in Braze sowie grundlegende Unterschiede zwischen iOS, Android und Web.

## Push-Abostatus {#push-sub-states}

Ein "Push-Abonnement-Status" in Braze identifiziert die globale Präferenz eines **Benutzers** für seinen Wunsch, Push-Benachrichtigungen zu erhalten. Da der Abostatus nutzerabhängig ist, ist er nicht auf eine bestimmte App begrenzt. Die Abo-Status werden zu hilfreichen Flaggen, wenn Sie entscheiden, welche Nutzer:innen Sie für Push-Benachrichtigungen ansprechen wollen.

{% alert note %}
Der Status des Push-Abonnements eines Benutzers gilt für sein gesamtes Benutzerprofil, das alle Geräte des Benutzers umfasst.
{% endalert %}

Es gibt drei Statusoptionen für Push-Abos: `Subscribed`, `Opted-In`, und `Unsubscribed`.

Damit Ihr Benutzer Ihre Nachrichten über Push empfangen kann, muss sein Push-Abonnementstatus entweder `Subscribed` oder `Opted-In` sein und er muss [Push aktiviert haben](#foreground-push-enabled). Sie können diese Einstellung bei Bedarf beim Verfassen einer Nachricht außer Kraft setzen.

|Einwilligungsstatus|Beschreibung|
|---|---|
|`Subscribed`| Standard-Push-Abonnementstatus, wenn ein Benutzerprofil in Braze erstellt wird. |
|`Opted-In`| Ein Benutzer hat sich ausdrücklich für den Erhalt von Push-Benachrichtigungen entschieden. Braze ändert den nutzerspezifischen Opt-in-Status automatisch auf `Opted-In`, wenn eine Opt-in-Anfrage auf Betriebssystemebene angenommen wird.<br><br>Dies gilt nicht für Nutzer:innen von Android 12 oder darunter.|
|`Unsubscribed`| Ein Nutzer hat sich über Ihre Anwendung oder andere von Ihrer Marke angebotene Methoden explizit von Push abgemeldet. Standardmäßig stellen die Push Kampagnen von Braze nur Nutzer:innen zusammen, die `Subscribed` oder `Opted-in` für Push sind.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze ändert den Status des Push-Abonnements eines Benutzers nicht automatisch in `Unsubscribed`. Wenn der nutzerspezifische Push-Abostatus `Unsubscribed` lautet, wird der Filter `Foreground Push Enabled` in der Segmentierung auf `false` gestellt.
{% endalert %}

### Push-Abostatus ändern {#update-push-subscription-state}

Es gibt drei Möglichkeiten, den Status des Push-Abos eines Nutzers:innen zu aktualisieren:

#### Automatisches Opt-in (Standard)

Braze setzt den Push-Abonnement-Status eines Benutzers standardmäßig auf `Opted-In`, wenn er zum ersten Mal Push-Benachrichtigungen für Ihre App autorisiert. Braze tut dies auch, wenn ein Nutzer:innen die Push-Berechtigungen in seinen Systemeinstellungen wieder aktiviert, nachdem er sie zuvor deaktiviert hatte.

{% tabs local %}
{% tab android %}
Um dieses Standardverhalten zu deaktivieren, fügen Sie die folgende Eigenschaft in die Datei `braze.xml` Ihres Android Studio-Projekts ein:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
Ab [Braze Swift SDK Version 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0) können Sie dieses Verhalten deaktivieren oder weiter anpassen, indem Sie die Konfiguration `optInWhenPushAuthorized` zur Datei `AppDelegate.swift` Ihres Xcode-Projekts hinzufügen:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK-Integration

Sie können den Abonnementstatus eines Benutzers mit dem Braze SDK über die Methode `setPushNotificationSubscriptionType` im [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [unter Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) oder [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) aktualisieren. Sie können diese Methode zum Beispiel verwenden, um eine Einstellungsseite in Ihrer App zu erstellen, auf der Benutzer Push-Benachrichtigungen manuell aktivieren oder deaktivieren können.

#### REST API

Sie können den Status des Abos eines Nutzers:innen mit der Braze REST API aktualisieren, indem Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) verwenden, um das [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) Attribut zu aktualisieren.

### Status des Push-Abonnements prüfen

Nutzerprofil für John Doe, dessen Push-Abonnement auf Abo eingestellt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, den Status des Push-Abos eines Nutzers:innen mit Braze zu überprüfen:

1. **Nutzerprofil** Sie können über das Braze-Dashboard auf dem **[Nutzer:innen-Suche]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** Seite. Nachdem Sie das Profil eines Benutzers gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Benutzer-ID), können Sie die Registerkarte **Engagement** auswählen, um den Abonnementstatus eines Benutzers anzuzeigen und manuell anzupassen.
2. **REST API Export:** Mit den Endpunkten [Benutzer:innen nach Segmenten]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) oder [Benutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) exportieren können Sie einzelne Nutzerprofile im JSON-Format exportieren. Braze gibt ein Push-Token-Objekt mit gerätespezifischen Push-Aktivierungsdaten zurück.

## Push-Erlaubnis

Alle Push-fähigen Plattformen (iOS, Internet und Android) erfordern ein explizites Opt-in per Eingabeaufforderung auf Betriebssystemebene. Die geringfügigen Unterschiede werden hier beschrieben.

Da die Entscheidung eines Nutzers endgültig ist und Sie ihn nicht noch einmal fragen können, nachdem er abgelehnt hat, ist der Einsatz von [Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) In-App-Nachrichten eine wichtige Strategie zur Steigerung Ihrer Opt-in-Raten.

**OS-native Push-Einwilligungsanfragen**

|Plattform|Bildschirmfoto|Beschreibung|
|--|--|--|
|iOS| ![Eine iOS-eigene Push-Aufforderung mit der Frage "Meine App möchte Ihnen Benachrichtigungen senden" mit zwei Buttons "Nicht zulassen" und "Zulassen" am unteren Rand der Nachricht.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Dies gilt nicht für die Beantragung einer [vorläufigen Push-Erlaubnis](#provisional-push).|
|Android| ![Eine Android Push-Nachricht mit der Frage "Erlauben Sie Kitchenerie, Ihnen Benachrichtigungen zu senden?" mit zwei Buttons "Erlauben" und "Nicht erlauben" am unteren Rand der Nachricht.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Diese Push-Erlaubnis wurde in Android 13 eingeführt. Vor Android 13 war eine Genehmigung zum Senden von Push-Nachrichten nicht erforderlich.|
|Internet| ![Die systemeigene Push-Eingabeaufforderung eines Webbrowsers mit der Frage "Braze.com möchte eine Benachrichtigung anzeigen" mit zwei Buttons "Blockieren" und "Zulassen" am unteren Rand der Nachricht.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Bis Android 13 war für den Versand von Push-Benachrichtigungen keine Einwilligung erforderlich. Unter Android 12 und darunter werden alle Nutzer:innen bei ihrer ersten Sitzung als `Subscribed` betrachtet, wenn Braze automatisch ein Push-Token anfordert. Ab jetzt ist der Nutzer mit einem gültigen Push-Token für dieses Gerät und dem Standard-Abostatus `Subscribed` **aktiviert**.

Ab [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/) muss die Push-Erlaubnis vom Nutzer:innen erbeten und erteilt werden. Ihre App kann den Benutzer zu gegebener Zeit manuell um Erlaubnis bitten, aber wenn nicht, werden die Benutzer automatisch gefragt, wenn Ihre App einen [Benachrichtigungskanal](https://developer.android.com/reference/android/app/NotificationChannel) erstellt.

### iOS

![Eine Benachrichtigung im Systembenachrichtigungscenter mit einer Nachricht am unteren Rand, die fragt: "Erhalten Sie weiterhin Benachrichtigungen von der Yachtr App?" mit zwei Buttons darunter für "Behalten" oder "Ausschalten".]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Ihre App kann provisorischen Push oder autorisierten Push anfordern. 

Autorisiertes Push erfordert die ausdrückliche Erlaubnis eines Nutzers:innen, bevor Sie Benachrichtigungen senden können, während [provisorisches Push](https://www.braze.com/resources/articles/mastering-provisional-push) es Ihnen ermöglicht, Benachrichtigungen __still__ und leise direkt an das Benachrichtigungszentrum zu senden, ohne dass ein Ton oder eine Warnung ertönt.

#### Vorläufige Einwilligung und stiller Versand {#provisional-push}

Vor iOS 12 (veröffentlicht 2018) müssen alle Nutzer:innen explizit Opt-in wählen, um Push-Benachrichtigungen zu erhalten.

Mit iOS 12 hat Apple eine [vorläufige Autorisierung](https://www.braze.com/resources/articles/mastering-provisional-push) eingeführt, die es Marken erlaubt, stille Push-Benachrichtigungen an die Benachrichtigungszentrale ihrer Nutzer:innen zu senden, bevor diese sich explizit dafür entscheiden. So haben Sie die Chance, den Wert Ihrer Nachrichten frühzeitig zu demonstrieren. Weitere Informationen finden Sie unter [Vorläufige Zulassung]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

### Internet

Im Web müssen Sie eine ausdrückliche Einwilligung über den nativen Browser-Dialog einholen.

Im Gegensatz zu iOS und Android, bei denen Ihre App die Eingabeaufforderung jederzeit anzeigen kann, zeigen einige moderne Browser die Aufforderung nur an, wenn sie durch eine "Benutzergeste" (Mausklick oder Tastendruck) ausgelöst wird. Wenn Ihre Website versucht, beim Laden der Seite eine Einwilligung in Push-Benachrichtigungen einzuholen, wird sie wahrscheinlich vom Browser ignoriert oder stummgeschaltet.

Daher sollten Sie nur dann um Erlaubnis bitten, wenn ein Benutzer irgendwo auf Ihrer Website klickt und nicht zufällig beim Laden einer Seite.

## Push-Token

[Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) sind eindeutige anonyme Bezeichner, die vom Gerät eines Nutzers generiert und an Braze gesendet werden, um festzustellen, wohin die Push-Benachrichtigung des jeweiligen Empfängers:in gesendet werden soll.

Es gibt zwei Arten von [Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/), die für das Verständnis der Push-Benachrichtigung an Ihre Nutzer:innen wichtig sind.

1. **Foreground Push** bietet die Möglichkeit, regelmäßig sichtbare Push-Benachrichtigungen in den Vordergrund des Geräts eines Benutzers zu senden.
2. **Hintergrund-Push** ist unabhängig davon verfügbar, ob ein bestimmtes Gerät sich für den Empfang von Push-Benachrichtigungen der jeweiligen Marke entschieden hat. Per Hintergrund-Push können Sie stille Push-Benachrichtigungen, die absichtlich nicht angezeigt werden, für wichtige Funktionen wie [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/) an Geräte senden.

Wenn ein Nutzerprofil ein gültiges Vordergrund-Push-Token enthält, das mit einer App verknüpft ist, betrachtet Braze es für die jeweilige App als "bei Push angemeldet". Braze bietet daher einen speziellen Filter für die Segmentierung, `Foreground Push Enabled for App,`, um diese Nutzer:innen zu identifizieren.

{% alert note %}
Der `Foreground Push Enabled for App` Filter berücksichtigt nur das Vorhandensein eines gültigen Vordergrund- und Hintergrund-Push-Tokens für die jeweilige App. Der allgemeinere [`Foreground Push Enabled`](#foreground-push-enabled) Filter segmentiert jedoch Benutzer, die Push-Benachrichtigungen für beliebige Apps in Ihrem Arbeitsbereich explizit aktiviert haben. Diese Zählung umfasst nur den Push im Vordergrund und schließt Nutzer:innen, die sich abgemeldet haben, nicht mit ein. Mehr über diese und andere Filter erfahren Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Mehrere Benutzer auf einem Gerät

Push-Token sind sowohl für ein Gerät als auch für eine App spezifisch. Es ist also nicht möglich, mit Push-Token zwischen mehreren Nutzer:innen zu unterscheiden, die dasselbe Gerät verwenden.

Nehmen wir zum Beispiel an, Sie haben zwei Benutzer: Charlie und Kim. Wenn Charlie auf seinem Telefon Push-Benachrichtigungen für Ihre App aktiviert hat und Kim Charlies Telefon benutzt, um sich von Charlies Profil abzumelden und bei ihrem eigenen anzumelden, wird das Push-Token erneut Kims Profil zugewiesen. Das Push-Token bleibt dann Kims Profil auf diesem Gerät zugewiesen, bis sie sich abmeldet und Charlie sich wieder anmeldet.

Eine App oder Website kann nur ein Push-Abonnement pro Gerät haben. Wenn sich also ein Benutzer von einem Gerät oder einer Website abmeldet und sich ein neuer Benutzer anmeldet, wird das Push-Token dem neuen Benutzer neu zugewiesen. Dies wird im Profil des Benutzers im Abschnitt **Kontakteinstellungen** auf der Registerkarte **Engagement** angezeigt:

Changelog des Push-Tokens auf dem Tab \*\*Engagement** des Profils eines Nutzers, der auflistet, wann der Push-Token zu einem anderen Nutzer verschoben wurde und was der Token war.]({% image_buster /assets/img/push_token_changelog.png %})

Da es für Push-Anbieter (APNs/FCMs) keine Möglichkeit gibt, zwischen mehreren Benutzern auf einem Gerät zu unterscheiden, übergeben wir das Push-Token an den zuletzt eingeloggten Benutzer, um zu bestimmen, welcher Benutzer auf dem Gerät für Push angesprochen werden soll.

### Mehrere Geräte und ein Benutzer

Der Push-Abostatus ist nutzerabhängig und nicht auf eine bestimmte App begrenzt. Der Status des Push-Abonnements ist der Wert, der zuletzt eingestellt wurde. Wenn sich ein Benutzer also für Push-Benachrichtigungen entschieden hat, ist sein Push-Abonnementstatus auf allen in Frage kommenden Geräten `Opted-in`. Wenn sich ein Benutzer später explizit von den Push-Benachrichtigungen abmeldet, sei es über Ihre Anwendung oder über andere Methoden, die Ihre Marke zur Verfügung stellt, wird der Status seines Push-Abonnements auf `Unsubscribed` aktualisiert, und keine bei Push registrierten Geräte können Push-Benachrichtigungen empfangen.

## Filter für Push im Vordergrund Enablement {#foreground-push-enabled}

`Foreground Push Enabled` ist ein Segmentierungsfilter in Braze, mit dem Marketingexperten auf einfache Weise Benutzer identifizieren können, die Braze erlauben, Push-Benachrichtigungen zu senden, und Benutzer, die keine Präferenzen geäußert haben, keine Push-Benachrichtigungen zu erhalten. 

Der Filter `Foreground Push Enabled` berücksichtigt Folgendes:
- Die Möglichkeit für Braze, eine Push-Benachrichtigung zu senden (Foreground Push Token)
- Die allgemeine Präferenz des Benutzers, Push-Nachrichten auf jedem seiner Geräte zu empfangen (Push-Abonnementstatus)

![Ein Screenshot des Dashboards, der zeigt, dass ein Nutzer:innen "Push für Marketing (iOS) registriert" ist]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Nutzerprofile gelten als "Push-aktiviert" oder "Push-registriert", wenn sie ein aktives Push-Token für eine App in Ihrem Workspace aufweisen. Der Push-Aktivierungsstatus ist also App-spezifisch. 

{% alert note %}
Informationen darüber, wie Sie den Status der Push-Registrierung überprüfen können, finden Sie unter [Push-Registrierungsstatus]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Andere plattformspezifische Szenarien

{% tabs %}
{% tab Android %}

Ist Vordergrund-Push im Nutzerprofil aktiviert, Push aber in den Betriebssystemeinstellungen deaktiviert, geschieht zu Beginn der nächsten Sitzung Folgendes:
- Braze markiert sie als im Vordergrund deaktivierte Push-Nachrichten und versucht nicht mehr, ihnen Push-Nachrichten zu senden.
- Der Filter `Foreground Push Enabled for App (Android)` und der Segmentierungsfilter `Foreground Push Enabled` (unter der Annahme, dass keine anderen Apps im Nutzerprofil ein gültiges Push-Token für den Vordergrund haben) geben `false` zurück.

Da in diesem Szenario weiterhin ein Hintergrund-Push-Token existiert, können Sie mit dem Segmentierungsfilter `Background or Foreground Push Enabled = true` weiterhin (stille) Push-Benachrichtigungen im Hintergrund versenden.

Bei Android betrachtet Braze einen Nutzer:innen als Push deaktiviert, wenn:

- Ein Benutzer deinstalliert die App von seinem Gerät.
- Eine Push-Nachricht aufgrund eines Bounce nicht zugestellt werden kann. Dies geht meist auf eine Deinstallation zurück, kann aber auch durch App-Updates, eine neue Push-Token-Version oder ein neues Format verursacht werden. 
- Die Push-Registrierung bei Firebase Cloud Messaging schlägt fehl (teils wegen einer schlechten Netzwerkverbindung oder weil FCM kein gültiges Token zurückgibt).
- Der Nutzer:innen blockiert Push-Benachrichtigungen für die App in den Einstellungen seines Geräts und protokolliert anschließend eine Sitzung.

{% alert note %}
Sie können eine Android Push-Benachrichtigung nur abfangen, wenn sich die App im Vordergrund oder im Hintergrund befindet (aber noch läuft). Sie können keine Benachrichtigungen abfangen, wenn die App beendet oder vollständig beendet wird.
{% endalert %}

{% endtab %}
{% tab iOS %}

Unabhängig davon, ob die Einwilligung in Vordergrund-Pushes erteilt wird, können Sie Hintergrund-Pushes senden, wenn Sie in Xcode Remote-Benachrichtigungen aktiviert haben und Ihre App [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications) aufruft.

Wenn Ihre App vorläufig autorisiert ist oder der Nutzer:innen sich für Push entschieden hat, erhält er ein Push-Token für den Vordergrund, mit dem Sie ihm alle Arten von Push senden können. Innerhalb von Braze betrachten wir einen Nutzer:innen auf iOS, der im Vordergrund Push aktiviert hat, als Push enabled, entweder explizit (auf App-Ebene) oder provisorisch (auf Geräte-Ebene).

Wenn ein Nutzer:innen den Empfang von Push-Benachrichtigungen auf Betriebssystemebene ablehnt, lautet der Status seines Push-Abonnements `Subscribed` und in seinem Profil wird nicht angezeigt, dass ein Push-Token für den Vordergrund registriert wurde. 

Wenn ein Benutzer, der sich ursprünglich auf Betriebssystemebene für Push-Benachrichtigungen entschieden hat, diese in seinen Betriebssystemeinstellungen deaktiviert, geschieht beim nächsten Start der Sitzung Folgendes:
- Braze kennzeichnet sie als deaktivierte Vordergrund-Pushes und versucht nicht mehr, Push-Nachrichten zu senden.
- Der Filter `Foreground Push Enabled for App (iOS)` und der Segmentierungsfilter `Foreground Push Enabled` (unter der Annahme, dass keine anderen Apps im Nutzerprofil ein gültiges Push-Token für den Vordergrund haben) geben `false` zurück.

Da in diesem Szenario weiterhin ein Hintergrund-Push-Token existiert, können Sie mit dem Segmentierungsfilter `Background or Foreground Push Enabled = true` weiterhin (stille) Push-Benachrichtigungen im Hintergrund versenden.

{% alert note %}
Unter iOS ist es nicht zulässig, dass Apps eine Push-Benachrichtigung abfangen, bevor die Push-Benachrichtigung angezeigt wird. Das bedeutet, dass Apps (und Braze) keine Kontrolle darüber haben, ob Sie die Benachrichtigung anzeigen oder ausblenden können. Ein Nutzer:innen kann Push-Benachrichtigungen für eine App in den Einstellungen des Geräts abwählen, aber das wird vom Betriebssystem gesteuert.
{% endalert %}

{% endtab %}
{% tab Web %}

Wird die Einwilligung in Push-Benachrichtigungen über die native Eingabeaufforderung erteilt, wird der Abo-Status auf `opted in` geändert.

Um Abos zu verwalten, können Sie mit der Nutzermethode [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) eine Einstellungsseite auf Ihrer Website erstellen. Danach können Sie im Dashboard nach dem Einwilligungsstatus filtern.

Wenn ein Benutzer die Benachrichtigungen in seinem Browser deaktiviert, wird die nächste Push-Benachrichtigung, die an diesen Benutzer gesendet wird, abgewiesen, und Braze aktualisiert das Push-Token des Benutzers entsprechend. So wird die Berechtigung für die Push-Aktivierungsfilter (`Background or Foreground Push Enabled`, `Foreground Push Enabled` und `Foreground Push Enabled for App`) konfiguriert. Der Abonnementstatus, der im Benutzerprofil eingestellt ist, ist eine Einstellung auf Benutzerebene und ändert sich nicht, wenn eine Push-Nachricht abprallt.

{% alert note %}
Webplattformen erlauben keinen Push im Hintergrund oder im Stillen.
{% endalert %}
{% endtab %}
{% endtabs %}

## Bewährte Praktiken

In unserem Artikel über [Push-Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) finden Sie eine ausführliche Anleitung, wie Sie Push bei Braze optimal nutzen können.

