{% multi_lang_include developer_guide/prerequisites/android.md %}

## Standard-Nutzerattribute

### Vordefinierte Methoden

Braze stellt vordefinierte Methoden zur Verfügung, um die folgenden Nutzerattribute innerhalb der[`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html)Klasse festzulegen. Für Methodenspezifikationen referenzieren wir auf [unser KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html).

- Vorname
- Nachname
- Land
- Sprache
- Geburtsdatum
- E-Mail
- Geschlecht
- Wohnort
- Telefonnummer

{% alert note %}
Alle String-Werte wie Vorname, Nachname, Land und Wohnort sind auf 255 Zeichen begrenzt.
{% endalert %}

### Standardattribut festlegen

Um ein Standardattribut für einen Benutzer festzulegen, rufen Sie die`getCurrentUser()`Methode auf Ihrer Braze-Instanz auf, um eine Referenz zum aktuellen Benutzer Ihrer App zu erhalten. Dann können Sie Methoden aufrufen, um ein Nutzer:in-Attribut zu setzen.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName("first_name");
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName("first_name")
}
```

{% endtab %}
{% endtabs %}

### Standardattribut zurücksetzen

Um ein Attribut des Nutzers zurückzusetzen, übergeben Sie bitte`null` an die entsprechende Methode.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName(null);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName(null)
}
```

{% endtab %}
{% endtabs %}

## Angepasste Nutzerattribute

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Nutzer:innen-Datenerfassung]({{site.baseurl}}/developer_guide/analytics).

### Anpassen der Attribute

{% tabs local %}
{% tab String %}
So legen Sie ein angepasstes Attribut mit einem `string` Wert fest:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Integers %}
So passen Sie ein angepasstes Attribut mit einem `int` Wert an:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
    
    // Integer attributes may also be incremented using code like the following:
    brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

  // Integer attributes may also be incremented using code like the following:
  brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

Um ein benutzerdefiniertes Attribut mit einem`long`ganzzahligen Wert festzulegen:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Floating-points %}
So legen Sie ein angepasstes Attribut mit einem `float` Wert fest:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

So legen Sie ein angepasstes Attribut mit einem `double` Wert fest:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Boolean %}
So legen Sie ein angepasstes Attribut mit einem `boolean` Wert fest:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
    // This method will assign the current time to a custom attribute at the time the method is called:
    brazeUser.setCustomUserAttributeToNow("your_attribute_key");
    // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
    brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
  // This method will assign the current time to a custom attribute at the time the method is called:
  brazeUser.setCustomUserAttributeToNow("your_attribute_key")
  // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
  brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Datumsangaben, die mit dieser Methode an Braze übergeben werden, müssen entweder im Format [ISO 8601 ](http://en.wikipedia.org/wiki/ISO_8601) (e.g `2013-07-16T19:20:30+01:00`) oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (e.g `2016-12-14T13:32:31.601-0800`) vorliegen.
{% endalert %}

{% endtab %}
{% tab Array %}

Die maximale Anzahl von Elementen in benutzerdefinierten Attribut-Arrays ist standardmäßig auf 25 festgelegt. Das Maximum für einzelne Arrays kann im Braze-Dashboard unter **„Dateneinstellungen“** > **„Angepasste Attribute“** auf bis zu 500 erhöht werden. Arrays, die die Höchstzahl an Elementen überschreiten, werden gekürzt, um die Höchstzahl an Elementen zu enthalten. Weitere Informationen zu benutzerdefinierten Attribut-Arrays und deren Verhalten finden Sie unter [Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays).

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    // Setting a custom attribute with an array value
    brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
    // Adding to a custom attribute with an array value
    brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
    // Removing a value from an array type custom attribute
    brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
  }
});
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  // Setting a custom attribute with an array value
  brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
  // Adding to a custom attribute with an array value
  brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
  // Removing a value from an array type custom attribute
  brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Angepasste Attribute nicht anpassen

Um ein angepasstes Attribut zu löschen, übergeben Sie den entsprechenden Attributschlüssel an die`unsetCustomUserAttribute`Methode.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.unsetCustomUserAttribute("your_attribute_key");
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.unsetCustomUserAttribute("your_attribute_key")
}
```

{% endtab %}
{% endtabs %}

### Verschachtelte angepasste Attribute

Sie können Eigenschaften auch in angepassten Attributen verschachteln. Im folgenden Beispiel wird ein`favorite_book`Objekt mit verschachtelten Eigenschaften als benutzerdefiniertes Attribut im Nutzerprofil festgelegt. Weitere Informationen finden Sie unter [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

{% tabs %}
{% tab JAVA %}
```java
JSONObject favoriteBook = new JSONObject();
try {
  favoriteBook.put("title", "The Hobbit");
  favoriteBook.put("author", "J.R.R. Tolkien");
  favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
  e.printStackTrace();
}

braze.getCurrentUser(user -> {
  user.setCustomUserAttribute("favorite_book", favoriteBook);
  return null;
});
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
val favoriteBook = JSONObject()
  .put("title", "The Hobbit")
  .put("author", "J.R.R. Tolkien")
  .put("publishing_date", "1937")

braze.getCurrentUser { user ->
  user.setCustomUserAttribute("favorite_book", favoriteBook)
}
```
{% endtab %}
{% endtabs %}

### Verwendung der REST API

Sie können auch unsere REST API verwenden, um Nutzer:innen-Attribute zu setzen oder zu löschen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data):in.

## Einstellen von Nutzer:in-Abonnements

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder per E-Mail oder per Push), rufen Sie die Funktionen `setEmailNotificationSubscriptionType()` bzw. `setPushNotificationSubscriptionType()` auf. Beide Funktionen nehmen den Enum-Typ `NotificationSubscriptionType` als Argumente. Dieser Typ hat drei verschiedene Zustände:

| Abo-Status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `SUBSCRIBED` | Abonniert, aber nicht explizit angemeldet |
| `UNSUBSCRIBED` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Android verlangt kein explizites Opt-in, um Nutzer:innen Push-Benachrichtigungen zu senden. Wenn ein Benutzer für Push registriert ist, wird er standardmäßig auf `SUBSCRIBED` und nicht auf `OPTED_IN` gesetzt. Weitere Informationen zur Implementierung von Abos und expliziten Opt-ins finden Sie unter [Verwalten von Nutzer:innen-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

### Einstellen von E-Mail-Abonnements

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

### Push-Benachrichtigung Abo einstellen

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

