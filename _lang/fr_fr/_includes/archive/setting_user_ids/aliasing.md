Un [alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) sert d'identifiant unique alternatif pour l'utilisateur. Vous pouvez utiliser des aliases pour identifier les utilisateurs selon d'autres critères que votre ID principal :

* Définissez un identifiant cohérent pour l’analyse qui suivra un utilisateur donné avant et après qu’il s’est connecté à une application mobile ou un site Internet.
* Ajoutez les identifiants utilisés par un fournisseur tiers à vos utilisateurs Braze afin de faciliter le rapprochement de vos données en externe.

Chaque alias se compose de deux parties : un nom pour l’identifiant lui-même et une étiquette indiquant le type d’alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul nom par étiquette. 

Pour plus d'informations sur la définition d'alias d'utilisateur par rapport à un profil utilisateur, reportez-vous à la section [Alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% if include.platform == "iOS" %}

{% tabs %}
{% tab OBJECTIF-C %}

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

Pour plus d'informations, voir [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html#-1106019389%2FFunctions%2F-1725759721).

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
