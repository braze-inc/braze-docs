{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Standard-Nutzerattribute

Um Nutzer:innen-Attribute festzulegen, müssen Sie die entsprechende Methode für das Objekt `BrazeBinding` aufrufen. Im Folgenden finden Sie eine Liste der integrierten Attribute, die mit dieser Methode aufgerufen werden können.

| Attribut                 | Code Beispiel |
|---------------------------|-------------|
| Vorname                | `AppboyBinding.SetUserFirstName("first name");` |
| Nachname                 | `AppboyBinding.SetUserLastName("last name");` |
| Nutzer-E-Mail                | `AppboyBinding.SetUserEmail("email@email.com");` |
| Geschlecht                    | `AppboyBinding.SetUserGender(Appboy.Models.Gender);` |
| Geburtsdatum                | `AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");` |
| Benutzerland              | `AppboyBinding.SetUserCountry("country name");` |
| Heimatort des Nutzers            | `AppboyBinding.SetUserHomeCity("city name");` |
| E-Mail-Abonnement des Nutzers   | `AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| Benutzer-Push-Abonnement    | `AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| Telefonnummer des Nutzers         | `AppboyBinding.SetUserPhoneNumber("phone number");` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Angepasste Nutzerattribute

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Nutzer:innen-Datenerfassung]({{site.baseurl}}/developer_guide/analytics).

### Anpassen der Attribute

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Integer %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Boolesch %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Datum %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Datumsangaben, die an Braze übergeben werden, müssen entweder im [ISO 8601-Format](http://en.wikipedia.org/wiki/ISO_8601) (z.B. `2013-07-16T19:20:30+01:00`) oder im `yyyy-MM-dd'T'HH:mm:ss:SSSZ` -Format (z.B.`2016-12-14T13:32:31.601-0800`) vorliegen.
{% endalert %}

{% endtab %}

{% tab Array %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

### Angepasste Attribute nicht anpassen

Um ein angepasstes Attribut eines Nutzers:innen wieder aufzuheben, verwenden Sie die folgende Methode:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Verwendung der REST API

Sie können auch unsere REST API verwenden, um Nutzer:innen-Attribute zu setzen oder zu löschen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data):in.

## Einstellen von Nutzer:in-Abonnements

Um ein E-Mail- oder Push-Abonnement für Ihre Nutzer:innen einzurichten, rufen Sie eine der folgenden Funktionen auf.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Beide Funktionen nehmen `Appboy.Models.AppboyNotificationSubscriptionType` als Argumente, das drei verschiedene Zustände hat:

| Abostatus | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `SUBSCRIBED` | Abonniert, aber nicht explizit angemeldet |
| `UNSUBSCRIBED` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Windows benötigt kein explizites Opt-in, um Nutzern Push-Benachrichtigungen zu senden. Wenn ein Nutzer für Push registriert ist, wird er standardmäßig auf `SUBSCRIBED` und nicht auf `OPTED_IN` gesetzt. Weitere Informationen finden Sie in unserer Dokumentation zur [Implementierung von Abonnements und expliziten Opt-Ins]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Abo Typ                        | Beschreibung |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Beim Empfang einer gültigen E-Mail-Adresse werden Nutzer automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert auf `OPTED_IN` zu setzen, sobald Sie die ausdrückliche Zustimmung Ihres Nutzers erhalten haben. Besuchen Sie unser Dokument [Benutzerabonnements ändern]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) für weitere Details. |
| `PushNotificationSubscriptionType`       | Die Benutzer werden bei einer gültigen Push-Registrierung automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert auf `OPTED_IN` zu setzen, sobald Sie die ausdrückliche Zustimmung Ihres Nutzers erhalten haben. Besuchen Sie unser Dokument [Benutzerabonnements ändern]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) für weitere Details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Diese Typen fallen unter `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Einstellen von E-Mail-Abonnements

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Abonnements für Push-Benachrichtigungen einstellen

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
