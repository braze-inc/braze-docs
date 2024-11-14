---
nav_title: Configuración de atributos personalizados
article_title: Configuración de atributos personalizados para iOS
platform: Swift
page_order: 3
description: "En este artículo de referencia se muestra cómo establecer atributos personalizados para el SDK Swift."

---

# Configuración de atributos personalizados

> Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

Antes de la implementación, asegúrate de revisar los ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Asignar atributos predeterminados al usuario

Para asignar atributos de usuario, tienes que establecer el campo apropiado en el objeto compartido `ABKUser`.

A continuación se muestra un ejemplo de configuración del atributo nombre:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

Los siguientes atributos deben establecerse en el objeto `Braze.User`:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

## Asignar atributos personalizados al usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes. Consulta nuestra [recopilación de datos de usuario]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) para obtener más información sobre las opciones de segmentación que te ofrece cada uno de estos atributos.

### Atributo personalizado con un valor de cadena

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### Atributo personalizado con un valor entero

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### Atributo personalizado con valor doble

Braze trata de la misma manera los valores `float` y `double` dentro de nuestra base de datos.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### Atributo personalizado con valor booleano

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### Atributo personalizado con un valor de fecha

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### Atributo personalizado con un valor de matriz

El número máximo de elementos de [las matrices de atributos personalizadas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) está predeterminado en 25. Las matrices que superen la cantidad máxima de elementos se truncarán para contenerla. El máximo para matrices individuales puede aumentarse hasta 100. Si deseas aumentar este máximo, ponte en contacto con tu administrador del servicio de atención al cliente. 


{% tabs %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% endtabs %}

### Desactivar un atributo personalizado

Los atributos personalizados también se pueden desactivar utilizando el siguiente método:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Aumentar/disminuir atributos personalizados

Este código es un ejemplo de atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado en cualquier valor entero o largo positivo o negativo:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Configuración de un atributo personalizado a través de la API REST

También puedes utilizar nuestra API REST para establecer atributos de usuario. Consulta la [documentación de la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

### Límites del valor del atributo personalizado

Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.

#### Información adicional

- Consulta la [documentación de`Braze.User` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class) para obtener más información.

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción para tus usuarios (por correo electrónico o push), llama a las funciones `set(emailSubscriptionState:)` o `set(pushNotificationSubscriptionState:)`, respectivamente. Estas dos funciones toman como argumento el tipo de enumeración `Braze.User.SubscriptionState`. Este tipo tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `optedIn` | Suscrito y con adhesión voluntaria explícita |
| `subscribed` | Suscrito, pero sin adhesión voluntaria explícita |
| `unsubscribed` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los usuarios que conceden permiso para que una aplicación les envíe notificaciones push están predeterminados al estado de `optedIn`, ya que iOS requiere una adhesión voluntaria explícita.

Los usuarios se configurarán en `subscribed` automáticamente al recibir una dirección de correo electrónico válida; sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `optedIn` al recibir el consentimiento explícito de tu usuario. Consulta la sección [Gestión de las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) para obtener más detalles.

### Configuración de las suscripciones por correo electrónico

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Configuración de suscripciones a notificaciones push

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Consulta la sección [Gestión de las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) para obtener más detalles.

