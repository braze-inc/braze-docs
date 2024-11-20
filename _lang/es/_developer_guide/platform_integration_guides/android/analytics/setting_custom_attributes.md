---
nav_title: Configuración de atributos personalizados
article_title: Configuración de atributos personalizados para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Este artículo de referencia muestra cómo establecer atributos personalizados en tu aplicación Android o FireOS."

---

# Configuración de atributos personalizados

> Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel. Este artículo de referencia muestra cómo establecer atributos personalizados en tu aplicación Android o FireOS.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestro [resumen de análisis]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Asignación de atributos de usuario

Para asignar atributos a tus usuarios, llama al método `getCurrentUser()` en tu instancia de Braze para obtener una referencia al usuario actual de tu aplicación. Después de tener una referencia al usuario actual, puedes llamar a métodos para establecer atributos predefinidos o personalizados.

### Atributos estándar del usuario

Braze proporciona métodos predefinidos para configurar los siguientes atributos de usuario dentro de la [clase BrazeUser](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html). Consulta nuestro KDoc para ver [las especificaciones del método](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html):

- Nombre
- Apellido
- País
- Idioma
- Fecha de nacimiento
- Correo electrónico
- Género
- Ciudad de origen
- Número de teléfono

Todos los valores de cadena como nombre, apellidos, país y ciudad de residencia están limitados a 255 caracteres.

#### Configuración del valor del atributo estándar

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

#### Configuración de valores de atributos personalizados

{% tabs local %}
{% tab Cadena %}
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
{% tab Entero %}
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
{% tab Largo %}
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
{% tab Flotante %}
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
{% tab Doble %}
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
{% tab Fecha %}
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
Las fechas pasadas a Braze con este método deben estar en el formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (e.g `2013-07-16T19:20:30+01:00`) o en el formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (e.g `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Matriz %}

El número máximo de elementos de las matrices de atributos personalizadas está predeterminado en 25. El máximo para matrices individuales puede aumentarse hasta 100 en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Las matrices que superen la cantidad máxima de elementos se truncarán para contenerla. Para obtener más información sobre las matrices de atributos personalizadas y su comportamiento, consulta nuestra documentación sobre [Matrices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays).

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

#### Desactivar un atributo personalizado

Los atributos personalizados también se pueden desactivar utilizando el siguiente método:

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

#### Atributo personalizado a través de la API REST

También puedes utilizar nuestra API REST para establecer atributos de usuario. Para ello, consulta la [documentación de la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción para tus usuarios (por correo electrónico o push), llama a las funciones `setEmailNotificationSubscriptionType()` o `setPushNotificationSubscriptionType()`, respectivamente. Estas dos funciones toman como argumento el tipo de enumeración `NotificationSubscriptionType`. Este tipo tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `UNSUBSCRIBED` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Android no requiere ninguna adhesión voluntaria explícita para enviar notificaciones push a los usuarios. Cuando un usuario se registra para push, se establece de manera predeterminada `SUBSCRIBED` en lugar de `OPTED_IN`. Consulta la sección [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para obtener más información sobre la implementación de las suscripciones y las adhesiones voluntarias explícitas.
{% endalert %}

### Configuración de las suscripciones por correo electrónico

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

### Configuración de la suscripción a notificaciones push

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

