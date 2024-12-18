---
nav_title: Configuração de atributos personalizados
article_title: Configuração de atributos personalizados para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Este artigo de referência mostra como definir atributos personalizados em seu app Android ou FireOS."

---

# Definição de atributos personalizados

> O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard. Este artigo de referência mostra como definir atributos personalizados em seu app Android ou FireOS.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossa [visão geral da análise de dados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Atribuição de atribuições ao usuário

Para atribuir atribuições aos seus usuários, chame o método `getCurrentUser()` em sua instância do Braze para obter uma referência ao usuário atual do seu app. Depois de ter uma referência ao usuário atual, é possível chamar métodos para definir atributos predefinidos ou personalizados.

### Atribuições padrão do usuário

O Braze fornece métodos predefinidos para configurar as seguintes atribuições de usuário dentro da [classe BrazeUser](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html). Consulte as [especificações do método](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html) em nosso KDoc:

- Nome
- Sobrenome
- País
- Idioma
- Data de nascimento
- E-mail
- Gênero
- Cidade natal
- Número de telefone

Todos os valores de string, como nome, sobrenome, país e cidade natal, estão limitados a 255 caracteres.

#### Definição do valor da atribuição padrão

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

#### Definição de valores de atributos personalizados

{% tabs localização %}
{% tab String %}
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
{% tab Inteiro %}
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
{% endtab %}
{% tab Booleano %}
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
{% tab Long %}
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
{% tab Float %}
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
{% endtab %}
{% tab Double %}
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
{% tab Data %}
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
As datas passadas para a Braze com esse método devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (e.g `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (e.g `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Matriz %}

O número máximo de elementos em matrizes de atributos personalizados tem como padrão 25. O máximo para vetores individuais pode ser aumentado para até 100 no dashboard da Braze, em **Configurações de dados** > **Atributos personalizados**). As matrizes que excederem o número máximo de elementos serão truncadas para conter o número máximo de elementos. Para saber mais sobre matrizes de atributos personalizados e seu comportamento, consulte nossa documentação sobre [matrizes]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays).

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

#### Desativação de um atributo personalizado

Os atributos personalizados também podem ser desmarcados usando o seguinte método:

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

#### Atributo personalizado por meio da API REST

Você também pode usar nossa API REST para definir atribuições de usuário. Para fazer isso, consulte a [documentação da API do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuração de inscrições de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivamente. Ambas as funções usam o tipo de enum `NotificationSubscriptionType` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrição e aceitação explícita |
| `SUBSCRIBED` | Inscrição feita, mas sem aceitação explícita |
| `UNSUBSCRIBED` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Nenhuma aceitação explícita é exigida pelo Android para enviar notificações por push aos usuários. Quando um usuário é registrado para push, ele é definido como `SUBSCRIBED` em vez de `OPTED_IN` por padrão. Consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para saber mais sobre a implementação de inscrições e aceitação explícita.
{% endalert %}

### Configuração de envios de e-mail

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

### Configuração da inscrição de notificações por push

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

