---
nav_title: Benutzerdefinierte Attribute einstellen
article_title: Benutzerdefinierte Attribute für Web festlegen
platform: Web
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Attribute für Web-Anwendungen zuweisen und festlegen."

---

# Benutzerdefinierte Attribute einstellen

> Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Sie können Ihre Benutzer auf dem Dashboard nach diesen Attributen filtern und segmentieren.

Sehen Sie sich vor der Implementierung in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices) die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an.

Um Ihren Nutzern Attribute zuzuweisen, rufen Sie die Methode `braze.getUser()` auf, um den aktuellen Nutzer Ihrer App zu referenzieren. Nachdem Sie auf den aktuellen Nutzer referenziert haben, können Sie Methoden aufrufen, um vordefinierte oder angepasste Attribute festzulegen.

## Zuweisung von vordefinierten Benutzerattributen

Braze stellt vordefinierte Methoden zum Festlegen der folgenden Nutzerattribute in der [Klasse `User`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) bereit:

- Vorname
- Nachname
- Sprache
- Land
- Geburtsdatum
- E-Mail
- Geschlecht
- Heimatstadt
- Telefonnummer

### Beispiele für die Umsetzung

#### Einen Vornamen festlegen

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### Ein Geschlecht festlegen

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### Festlegen eines Geburtsdatums

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## Zuweisen von benutzerdefinierten Benutzerattributen

Zusätzlich zu unseren vordefinierten Methoden für Benutzerattribute bietet Braze auch [benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types), um Daten aus Ihren Anwendungen zu verfolgen. 

Die vollständigen Methodenspezifikationen für benutzerdefinierte Attribute finden Sie hier in den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

### Benutzerdefinierte Attributlänge

Schlüssel und Werte angepasster Attribute haben eine maximale Länge von 255 Zeichen. Einzelheiten zu den gültigen Werten für benutzerdefinierte Attribute finden Sie in der [vollständigen technischen Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

### Beispiele für die Umsetzung

#### Setzen eines benutzerdefinierten Attributs mit einem String-Wert
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### Setzen eines benutzerdefinierten Attributs mit einem Integer-Wert
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### Setzen eines benutzerdefinierten Attributs mit einem Datumswert
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```
>  Daten, die mit dieser Methode an Braze übergeben werden, müssen JavaScript-Datumsobjekte sein.

#### Setzen eines benutzerdefinierten Attributs mit einem Array-Wert

Die maximale Anzahl von Elementen in benutzerdefinierten Attribut-Arrays ist standardmäßig auf 25 festgelegt. Einzelne Arrays können im Braze Dashboard unter **Dateneinstellungen** > **Benutzerdefinierte Attribute** auf bis zu 100 erhöht werden. Wenn Sie diese Höchstgrenze erhöhen möchten, wenden Sie sich an Ihren Kundendienstleiter. [Arrays]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays), die die maximale Anzahl von Elementen überschreiten, werden so abgeschnitten, dass sie die maximale Anzahl von Elementen enthalten.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### Zurücksetzen eines benutzerdefinierten Attributs

Angepasste Attribute können deaktiviert werden, indem ihr Wert auf `null` gesetzt wird.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Setzen eines benutzerdefinierten Attributs über die REST API

Sie können auch unsere REST API verwenden, um Benutzerattribute festzulegen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Einrichten von Benutzerabonnements

Um ein Abo für Ihre Nutzer einzurichten (entweder E-Mail oder Push), rufen Sie die Funktion `setEmailNotificationSubscriptionType()` bzw. `setPushNotificationSubscriptionType()` auf. Beide Funktionen nehmen den Typ `enum` `braze.User.NotificationSubscriptionTypes` als Argumente an. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Abonniert, aber nicht explizit angemeldet |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn ein Benutzer für Push registriert ist, zwingt der Browser ihn, zu entscheiden, ob er Benachrichtigungen zulassen oder blockieren möchte. Wenn er sich für Push entscheidet, wird standardmäßig `OPTED_IN` eingestellt. 

Weitere Informationen zur Implementierung von Abonnements und expliziten Opt-Ins finden Sie unter [Verwaltung von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

### Beispiel-Code

#### Abmelden eines Nutzers von E-Mails-Benachrichtigungen:
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### Abmelden eines Nutzers von Push-Benachrichtigungen:
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

