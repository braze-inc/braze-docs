Ein [Benutzer-Alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) dient als alternativer eindeutiger Benutzeridentifikator. Sie können Aliasnamen verwenden, um Benutzer anhand anderer Dimensionen als Ihrer Haupt-Benutzer-ID zu identifizieren:

* Legen Sie eine einheitliche Kennung für die Analyse fest, die einen bestimmten Benutzer sowohl vor als auch nach der Anmeldung bei einer mobilen App oder Website verfolgt.
* Fügen Sie Ihren Braze-Benutzern die von einem Drittanbieter verwendeten Bezeichner hinzu, um Ihre Daten leichter extern abzugleichen.

Jeder Alias besteht aus zwei Teilen: einem Namen für den Bezeichner selbst und einer Bezeichnung, die den Typ des Alias angibt. Benutzer können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen Namen pro Bezeichnung. 

Weitere Informationen zum Einrichten von Benutzer-Aliasnamen für ein Benutzerprofil finden Sie unter [Benutzer-Aliasnamen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% if include.platform == "iOS" %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```

{% endtab %}
{% endtabs %}

{% elsif include.platform == "Android" %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```

{% endtab %}
{% endtabs %}

Für weitere Informationen siehe [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html#-1106019389%2FFunctions%2F-1725759721).

{% elsif include.platform == "Web" %}

```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% elsif include.platform == "Swift" %}

```swift
AppDelegate.braze?.user.add(alias: ALIAS_NAME, label: ALIAS_LABEL)
```

{% elsif include.platform == "REST" %}

```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

{% endif %}
