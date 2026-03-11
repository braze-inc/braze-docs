## Push-Abostatus {#push-sub-states}

Ein "Push-Abonnement-Status" in Braze identifiziert die globale Präferenz eines **Benutzers** für seinen Wunsch, Push-Benachrichtigungen zu erhalten. Da der Abostatus nutzerabhängig ist, ist er nicht auf eine bestimmte App begrenzt. Die Abo-Status werden zu hilfreichen Flaggen, wenn Sie entscheiden, welche Nutzer:innen Sie für Push-Benachrichtigungen ansprechen wollen.

{% alert note %}
Der Status des Push-Abonnements eines Benutzers gilt für sein gesamtes Benutzerprofil, das alle Geräte des Benutzers umfasst.
{% endalert %}

Die folgenden Abo-Statusoptionen sind verfügbar: `Subscribed`, `Opted-In`, und `Unsubscribed`.

Standardmäßig muss das Push-Abo Ihrer Nutzer:innen entweder`Subscribed`  oder  sein und sie müssen `Opted-In`Push-Benachrichtigungen im Vordergrund aktiviert haben, damit sie Ihre Nachrichten per Push erhalten können. Sie können diese Einstellung bei Bedarf beim Verfassen einer Nachricht außer Kraft setzen.

|Einwilligungsstatus|Beschreibung|
|---|---|
|`Subscribed`| Standard-Push-Abonnementstatus, wenn ein Benutzerprofil in Braze erstellt wird. |
|`Opted-In`| Ein Benutzer hat sich ausdrücklich für den Erhalt von Push-Benachrichtigungen entschieden. Braze verschiebt den Opt-in-Status einer Nutzer:in automatisch auf `Opted-In`„Ja“, wenn die Nutzer:in eine Push-Aufforderung auf Betriebssystemebene akzeptiert.<br><br>Dies gilt nicht für Nutzer:innen von Android 12 oder darunter.|
|`Unsubscribed`| Ein Nutzer hat sich über Ihre Anwendung oder andere von Ihrer Marke angebotene Methoden explizit von Push abgemeldet. Standardmäßig richten sich Braze-Push-Kampagnen nur an Nutzer:innen, die für `Opted-in`Push-Benachrichtigungen aktiviert`Subscribed`sind.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze ändert den Status des Push-Abonnements eines Benutzers nicht automatisch in `Unsubscribed`. Bitte beachten Sie, dass, wenn der Status des Push-Abos einer Nutzer:in „“ ist`Unsubscribed`, der Filter `Foreground Push Enabled`der Nutzer:in in der Segmentierung „“ ist`false`.
{% endalert %}

### Push-Abostatus ändern {#update-push-subscription-state}

Bitte beachten Sie die folgenden Möglichkeiten, um den Push-Abo-Status einer Nutzer:in zu Update:

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

![Benutzerprofil von John Doe, dessen Push-Abonnementstatus auf Abonniert gesetzt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Sie können den Status des Push-Abonnements eines Nutzers mit Braze auf eine der folgenden Arten überprüfen:

* **Benutzerprofil:** Sie können über das Braze-Dashboard auf die einzelnen Nutzer:innen-Profile zugreifen. **[Nutzer:innen-Suche]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** Seite. Nachdem Sie das Profil eines Benutzers gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Benutzer-ID), können Sie die Registerkarte **Engagement** auswählen, um den Abonnementstatus eines Benutzers anzuzeigen und manuell anzupassen.
* **REST API-Export:** Mit den Endpunkten [Benutzer:innen nach Segmenten]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) oder [Benutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) exportieren können Sie einzelne Nutzerprofile im JSON-Format exportieren. Braze gibt ein Push-Token-Objekt zurück, das Push-Enablement-Informationen pro Gerät enthält.