Un [alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) sirve como identificador único alternativo del usuario. Puedes utilizar alias para identificar a los usuarios en dimensiones diferentes a tu ID de usuario principal:

* Establece un identificador coherente para el análisis que seguirá a un usuario determinado tanto antes como después de que haya iniciado sesión en una aplicación móvil o sitio web.
* Añade los identificadores utilizados por un proveedor externo a tus usuarios de Braze para conciliar más fácilmente tus datos externamente.

Cada alias consta de dos partes: un nombre para el propio identificador y una etiqueta que indica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un nombre por etiqueta. 

Para más información sobre la configuración de alias de usuario contra un perfil de usuario, consulta [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% if include.platform == "iOS" %}

{% tabs %}
{% tab OBJETIVO-C %}

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

Para más información, consulta [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html#-1106019389%2FFunctions%2F-1725759721).

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
