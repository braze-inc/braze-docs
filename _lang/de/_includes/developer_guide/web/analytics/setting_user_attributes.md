{% multi_lang_include developer_guide/prerequisites/web.md %}

## Standard-Nutzerattribute

### Vordefinierte Methoden

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

### Standardattribute festlegen

{% tabs %}
{% tab using methods %}
Um ein Standardattribut für eine:n Nutzer:in festzulegen, rufen Sie die Methode `getUser()` auf Ihrer Braze-Instanz auf, um eine Referenz zum aktuellen Nutzer bzw. zur aktuellen Nutzerin Ihrer App zu erhalten. Anschließend können Sie Methoden aufrufen, um ein Nutzerattribut zu setzen.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab google tag manager %}
Mit Google Tag Manager sollten Standard-Nutzerattribute (wie z. B. der Vorname) auf dieselbe Weise wie angepasste Nutzerattribute protokolliert werden. Stellen Sie sicher, dass die Werte, die Sie für Standardattribute übergeben, dem erwarteten Format entsprechen, das in der Dokumentation der [Klasse User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) angegeben ist.

Das Attribut „gender" kann zum Beispiel folgende Werte annehmen: `"m" | "f" | "o" | "u" | "n" | "p"`. Um also das Geschlecht als weiblich festzulegen, erstellen Sie ein angepasstes HTML-Tag mit folgendem Inhalt:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Standardattribute zurücksetzen

Um ein Standardattribut zurückzusetzen, übergeben Sie `null` an die entsprechende Methode. Zum Beispiel:

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Angepasste Nutzerattribute

### Angepasste Attribute festlegen

{% tabs %}
{% tab using methods %}
Zusätzlich zu den Standardmethoden für Nutzerattribute können Sie auch [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) für Ihre Nutzer:innen festlegen. Die vollständigen Methodenspezifikationen finden Sie in [unseren JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
So legen Sie ein angepasstes Attribut mit einem `string`-Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
So legen Sie ein angepasstes Attribut mit einem `integer`-Wert fest:

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

{% endsubtab %}
{% subtab Date %}
So legen Sie ein angepasstes Attribut mit einem `date`-Wert fest:

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

{% endsubtab %}
{% subtab Array %}

Die Standard- und Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl an Elementen im Braze-Dashboard unter **Dateneinstellungen** > **Angepasste Attribute** aktualisieren. Arrays, die die Höchstzahl an Elementen überschreiten, werden auf die Höchstzahl an Elementen gekürzt.


So legen Sie ein angepasstes Attribut mit einem `array`-Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Datumsangaben, die mit dieser Methode an Braze übergeben werden, müssen JavaScript-Date-Objekte sein.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Schlüssel und Werte angepasster Attribute dürfen maximal 255 Zeichen umfassen. Weitere Informationen zu gültigen Werten angepasster Attribute finden Sie in der [Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab google tag manager %}
Angepasste Nutzerattribute sind aufgrund einer Einschränkung in der Skriptsprache von Google Tag Manager nicht verfügbar. Um angepasste Attribute zu protokollieren, erstellen Sie ein angepasstes HTML-Tag mit folgendem Inhalt:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Das GTM-Template unterstützt keine verschachtelten Eigenschaften für Ereignisse oder Käufe. Mit dem vorstehenden HTML-Code können Sie alle Ereignisse oder Käufe protokollieren, die verschachtelte Eigenschaften erfordern.
{% endalert %}
{% endtab %}
{% endtabs %}

### Angepasste Attribute zurücksetzen

Um ein angepasstes Attribut zurückzusetzen, übergeben Sie `null` an die entsprechende Methode.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Verschachtelte angepasste Attribute

Sie können Eigenschaften auch in angepassten Attributen verschachteln. Im folgenden Beispiel wird ein `favorite_book`-Objekt mit verschachtelten Eigenschaften als angepasstes Attribut im Nutzerprofil festgelegt. Weitere Informationen finden Sie unter [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Verwendung der REST API

Sie können auch unsere REST API verwenden, um Nutzerattribute zu setzen oder zurückzusetzen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Nutzer-Abos einrichten

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder per E-Mail oder per Push), rufen Sie die Funktionen `setEmailNotificationSubscriptionType()` bzw. `setPushNotificationSubscriptionType()` auf. Beide Funktionen verwenden den `enum`-Typ `braze.User.NotificationSubscriptionTypes` als Argumente. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Abonniert, aber nicht ausdrücklich angemeldet |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn sich Nutzer:innen für Push registrieren, fordert der Browser sie auf, Benachrichtigungen zuzulassen oder zu blockieren. Wenn sie Push zulassen, wird standardmäßig `OPTED_IN` gesetzt.

Weitere Informationen zur Implementierung von Abos und expliziten Opt-ins finden Sie unter [Verwaltung von Nutzer-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

### Nutzer:in von E-Mails abmelden

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Nutzer:in von Push-Benachrichtigungen abmelden

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
