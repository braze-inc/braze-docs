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

### Einstellung von Standardattributen

{% tabs %}
{% tab Methoden verwenden %}
Um ein Standardattribut für einen Nutzer festzulegen, rufen Sie die Methode `getUser()` auf Ihrer Braze-Instanz auf, um eine Referenz auf den aktuellen Nutzer:innen Ihrer App zu erhalten. Dann können Sie Methoden aufrufen, um ein Nutzer:in-Attribut zu setzen.

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

{% tab Google Tag Manager %}
Bei der Verwendung von Google Tag Manager sollten Standard-Attribute für Nutzer:innen (z.B. der Vorname eines Nutzers) auf die gleiche Weise protokolliert werden wie angepasste Attribute für Nutzer:innen. Stellen Sie sicher, dass die Werte, die Sie für Standardattribute übergeben, dem erwarteten Format entsprechen, das in der Dokumentation [Nutzerklasse](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) angegeben ist.

Das Attribut "gender" kann zum Beispiel folgende Werte annehmen: `"m" | "f" | "o" | "u" | "n" | "p"`. Um also das Geschlecht eines Nutzers als weiblich festzulegen, erstellen Sie ein angepasstes HTML-Tag mit folgendem Inhalt:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Standardattribute zurücksetzen

Um ein Standardattribut für Nutzer:innen zu deaktivieren, übergeben Sie `null` an die entsprechende Methode. Zum Beispiel:

{% tabs local %}
{% tab Vorname %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Geschlecht %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Geburtsdatum %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Angepasste Nutzerattribute

### Anpassen der Attribute

{% tabs %}
{% tab Methoden verwenden %}
Zusätzlich zu den Standardattributen können Sie auch [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) für Ihre Nutzer:innen festlegen. Die vollständigen Spezifikationen der Methode finden Sie in [unseren JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
So legen Sie ein angepasstes Attribut mit einem `string` Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
So legen Sie ein angepasstes Attribut mit einem `integer` Wert fest:

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
So legen Sie ein angepasstes Attribut mit einem `date` Wert fest:

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

Sie können bis zu 25 Elemente in angepassten Attribut-Arrays haben. Einzelne Arrays, die manuell für den **Datentyp** angepasst werden (nicht automatisch erkannt), können im Braze-Dashboard unter **Dateneinstellungen** > Angepasste Attribute auf bis zu 100 erhöht werden. Wenn Sie diesen Höchstbetrag erhöhen möchten, wenden Sie sich an Ihren Braze-Konto Manager:in.

[Arrays]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays), die die maximale Anzahl von Elementen überschreiten, werden so abgeschnitten, dass sie die maximale Anzahl von Elementen enthalten.

So passen Sie ein angepasstes Attribut mit einem `array` Wert an:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Daten, die mit dieser Methode an Braze übergeben werden, müssen JavaScript-Datumsobjekte sein.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Angepasste Attribut-Schlüssel und -Werte dürfen nur maximal 255 Zeichen lang sein. Weitere Informationen über gültige Werte für angepasste Attribute finden Sie in der [referenzierten Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Benutzerdefinierte Benutzerattribute sind aufgrund einer Einschränkung in der Skriptsprache von Google Tag Manager nicht verfügbar. Um angepasste Attribute zu protokollieren, erstellen Sie ein angepasstes HTML-Tag mit folgendem Inhalt:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Die GTM-Vorlage unterstützt keine verschachtelten Eigenschaften für Ereignisse oder Käufe. Mit dem vorstehenden HTML-Code können Sie alle Events oder Käufe protokollieren, die verschachtelte Eigenschaften erfordern.
{% endalert %}
{% endtab %}
{% endtabs %}

### Angepasste Attribute nicht anpassen

Um ein angepasstes Attribut zu deaktivieren, übergeben Sie `null` an die entsprechende Methode.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Verschachtelte angepasste Attribute

Sie können auch Eigenschaften innerhalb angepasster Attribute verschachteln. Im folgenden Beispiel wird ein `favorite_book` Objekt mit verschachtelten Eigenschaften als angepasstes Attribut auf das Nutzerprofil gesetzt. Weitere Einzelheiten finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

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

Sie können auch unsere REST API verwenden, um Nutzer:innen-Attribute zu setzen oder zu löschen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data):in.

## Einstellen von Nutzer:in-Abonnements

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder per E-Mail oder per Push), rufen Sie die Funktionen `setEmailNotificationSubscriptionType()` bzw. `setPushNotificationSubscriptionType()` auf. Beide Funktionen nehmen den `enum` Typ `braze.User.NotificationSubscriptionTypes` als Argumente. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Abonniert, aber nicht explizit angemeldet |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn ein Benutzer für Push registriert ist, zwingt der Browser ihn, zu entscheiden, ob er Benachrichtigungen zulassen oder blockieren möchte. Wenn er sich für Push entscheidet, wird standardmäßig `OPTED_IN` eingestellt. 

Weitere Informationen zur Implementierung von Abonnements und expliziten Opt-Ins finden Sie unter [Verwaltung von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

### Nutzer:innen von E-Mails abmelden

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Nutzer:innen von Push abmelden

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
