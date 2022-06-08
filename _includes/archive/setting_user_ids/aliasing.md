A [user alias](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID:

* Set a consistent identifier for analytics that will follow a given user both before and after they have logged in to a mobile app or website.
* Add the identifiers used by a third-party vendor to your Braze users in order to more easily reconcile your data externally.

Each alias consists of two parts: a name for the identifier itself, and a label indicating the type of alias. Users can have multiple aliases with different labels, but only one name per label.

{% if include.platform == "iOS" %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```

 {% endtab %}
{% tab swift %}

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

{% elsif include.platform == "Web" %}

```javascript
appboy.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% elsif include.platform == "REST" %}

```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

{% endif %}
