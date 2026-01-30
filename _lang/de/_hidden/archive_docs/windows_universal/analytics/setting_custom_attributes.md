---
nav_title: Angepasste Attribute festlegen
article_title: Angepasste Attribute für Windows Universal festlegen
platform: Windows Universal
page_order: 3
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie angepasste Attribute auf der Windows Universal-Plattform festlegen."
hidden: true
---

# Angepasste Attribute festlegen
{% multi_lang_include archive/windows_deprecation.md %}

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

Sehen Sie sich vor der Implementierung unbedingt in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an.

Die Attribute der Nutzer:innen können der aktuellen `IAppboyUser` zugewiesen werden. Um einen Verweis auf die aktuelle `IAppboyUser` zu erhalten, rufen Sie `Appboy.SharedInstance.AppboyUser`

## Zuweisen von Standard-Benutzerattributen

Die folgenden Attribute sollten als Eigenschaften der `IAppboyUser` definiert werden:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Beispiel-Implementierung**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Zuweisen von benutzerdefinierten Benutzerattributen

Neben den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung einer Reihe von verschiedenen Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen und zu den Auswirkungen der einzelnen Attribute finden Sie in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Benutzerdefinierte Attributwerte festlegen

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double or Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze behandelt FLOAT- und DOUBLE-Werte in unserer Datenbank genau gleich.
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Datumsangaben, die an Braze übergeben werden, müssen entweder im Format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601), e.g `2013-07-16T19:20:30+01:00` oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` vorliegen. e.g `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Array %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Inkrementieren/Dekrementieren von angepassten Attributen

Dieser Code ist ein Beispiel für ein inkrementelles benutzerdefiniertes Attribut. Sie können den Wert eines angepassten Attributs um jeden positiven oder negativen ganzzahligen Wert erhöhen.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Zurücksetzen eines benutzerdefinierten Attributs

Benutzerdefinierte Attribute können auch mit der folgenden Methode deaktiviert werden:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Setzen eines benutzerdefinierten Attributs über die REST API

Sie können auch unsere REST API verwenden, um Benutzerattribute festzulegen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

### Benutzerdefinierte Attributwertgrenzen

Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

## Verwaltung des Status von Abo-Benachrichtigungen

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder per E-Mail oder per Push), können Sie die folgenden Eigenschaften des `IAppboyUser` als Abo-Status festlegen. Der Abo-Status in Braze hat drei verschiedene Zustände für E-Mail und Push:

| Abostatus | Definition |
| ------------------- | ---------- |
| `OptedIn` | Abonniert und ausdrücklich angemeldet |
| `Subscribed` | Abonniert, aber nicht explizit angemeldet |
| `UnSubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

- `EmailNotificationSubscriptionType`
  - Nutzer:innen werden bei Erhalt einer gültigen E-Mail Adresse automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in Verfahren einzurichten und diesen Wert bei Erhalt einer expliziten Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen.
- `PushNotificationSubscriptionType`
  - Nutzer:innen werden bei einer gültigen Push-Registrierung automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert nach Erhalt der ausdrücklichen Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen.

>  Diese Typen fallen unter `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Weitere Informationen finden Sie unter [Verwalten von Nutzer:innen-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

