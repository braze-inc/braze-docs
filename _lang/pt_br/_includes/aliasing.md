Um [alias de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) serve como um identificador de usuário exclusivo alternativo. É possível usar aliases para identificar usuários em dimensões diferentes do seu ID de usuário principal:

* Defina um identificador consistente para análise de dados que seguirá um determinado usuário antes e depois de ele ter feito o registro em um app ou site móvel.
* Adicione os identificadores usados por um fornecedor terceirizado aos seus usuários do Braze para reconciliar mais facilmente seus dados externamente.

Cada alias consiste em duas partes: um nome para o próprio identificador e um rótulo que indica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um nome por rótulo. 

Para saber mais sobre a configuração de aliases de usuário em relação a um perfil de usuário, consulte [Aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% if include.platform == "iOS" %}

{% tabs %}
{% tab OBJECTIVE C %}

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
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% elsif include.platform == "REST" %}

```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

{% endif %}
