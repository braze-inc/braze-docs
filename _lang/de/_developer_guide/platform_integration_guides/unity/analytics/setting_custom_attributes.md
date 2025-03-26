---
nav_title: Benutzerdefinierte Attribute einstellen
article_title: Benutzerdefinierte Attribute für Unity festlegen
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "In diesem Referenzartikel erfahren Sie, wie Sie angepasste Attribute auf der Unity-Plattform festlegen und ihre Festlegung aufheben."

---

# Benutzerdefinierte Attribute einstellen

> Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

Sehen Sie sich vor der Implementierung unbedingt in unseren [Best Practices][1] die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an.

## Zuweisen von Standard-Nutzerattributen

Um Nutzerattribute zuzuweisen, müssen Sie die entsprechende Methode für das BrazeBinding-Objekt aufrufen. Im Folgenden finden Sie eine Liste der integrierten Attribute, die mit dieser Methode aufgerufen werden können.

### Vorname
`AppboyBinding.SetUserFirstName("first name");`

### Nachname
`AppboyBinding.SetUserLastName("last name");`

### Nutzer-E-Mail
`AppboyBinding.SetUserEmail("email@email.com");`

>  Es ist nach wie vor sinnvoll, E-Mail-Adressen festzulegen, auch wenn Sie keine E-Mails über Braze versenden. E-Mail erleichtert die Suche nach einzelnen Benutzerprofilen und die Behebung von Problemen, sobald diese auftreten.

### Geschlecht
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### Geburtsdatum
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### Benutzerland
`AppboyBinding.SetUserCountry("country name");`

### Heimatort des Nutzers
`AppboyBinding.SetUserHomeCity("city name");`

### E-Mail-Abonnement des Nutzers
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Benutzer-Push-Abonnement
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Telefonnummer des Nutzers
`AppboyBinding.SetUserPhoneNumber("phone number");`

## Zuweisen von benutzerdefinierten Benutzerattributen

Neben den Standard-Benutzerattributen können Sie in Braze auch benutzerdefinierte Attribute mit einer Reihe verschiedener Datentypen definieren:
Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden in unserer [Best Practices-Dokumentation][1] in diesem Abschnitt.

### Benutzerdefinierte Attributwerte festlegen

{% tabs %}
{% tab Boolescher Wert %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab Datum %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  Datumsangaben, die an Braze übergeben werden, müssen entweder im Format [ISO 8601][2], e.g `2013-07-16T19:20:30+01:00` oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` vorliegen. e.g `2016-12-14T13:32:31.601-0800`

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
{% endtabs
%}
### Zurücksetzen eines benutzerdefinierten Attributs

Benutzerdefinierte Attribute können auch mit der folgenden Methode deaktiviert werden:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## Setzen eines benutzerdefinierten Attributs über die REST API
Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen. Lesen Sie dazu die [Dokumentation der Benutzer-API][3].

## Benutzerdefinierte Attributwertgrenzen
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

## Einrichten von Benutzerabonnements

Um ein Abo für Ihre Nutzer einzurichten (entweder E-Mail oder Push), rufen Sie folgende Funktionen auf:     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` bzw. `AppboyBinding.SetPushNotificationSubscriptionType()`. Beide Funktionen nehmen die Parameter `Appboy.Models.AppboyNotificationSubscriptionType` als Argumente an. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `SUBSCRIBED` | Abonniert, aber nicht explizit angemeldet |
| `UNSUBSCRIBED` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Windows benötigt kein explizites Opt-in, um Nutzern Push-Benachrichtigungen zu senden. Wenn ein Nutzer für Push registriert ist, wird er standardmäßig auf `SUBSCRIBED` und nicht auf `OPTED_IN` gesetzt. Weitere Informationen finden Sie in unserer Dokumentation zur [Implementierung von Abonnements und expliziten Opt-Ins][10].

- `EmailNotificationSubscriptionType`
  - Beim Empfang einer gültigen E-Mail-Adresse werden Nutzer automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert auf `OPTED_IN` zu setzen, sobald Sie die ausdrückliche Zustimmung Ihres Nutzers erhalten haben. Besuchen Sie unser Dokument [Benutzerabonnements ändern][8] für weitere Details.
- `PushNotificationSubscriptionType`
  - Die Benutzer werden bei einer gültigen Push-Registrierung automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert auf `OPTED_IN` zu setzen, sobald Sie die ausdrückliche Zustimmung Ihres Nutzers erhalten haben. Besuchen Sie unser Dokument [Benutzerabonnements ändern][8] für weitere Details.

>  Diese Typen fallen unter `Appboy.Models.AppboyNotificationSubscriptionType`.

## Beispiel-Code

### E-Mail-Abonnement:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Push-Abonnement

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
