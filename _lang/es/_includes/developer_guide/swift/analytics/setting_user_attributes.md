{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Atributos predeterminados del usuario

### Atributos admitidos

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

### Configuración de atributos predeterminados

Para establecer un atributo predeterminado de usuario, establece el campo apropiado en el objeto compartido `Braze.User`. A continuación se muestra un ejemplo de configuración del atributo nombre:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objetivo-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### Desactivar atributos predeterminados

Para desactivar un atributo predeterminado del usuario, pasa `nil` al método correspondiente.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objetivo-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## Atributos personalizados del usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes. Para más información sobre la opción de segmentación de cada atributo, consulta [Recopilación de datos de usuario]({{site.baseurl}}/developer_guide/analytics/).

{% alert important %}
Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán. Para más información, consulta [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Establecer atributos personalizados

{% tabs local %}
{% tab cadena %}
Para establecer un atributo personalizado con un valor `string`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab entero %}
Para establecer un atributo personalizado con un valor `integer`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab puntos flotantes %}
Braze trata de la misma manera los valores `float` y `double` dentro de nuestra base de datos. Para establecer un atributo personalizado con un valor doble:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab booleano %}
Para establecer un atributo personalizado con un valor `boolean`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab fecha %}
Para establecer un atributo personalizado con un valor `date`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab matriz %}
El número máximo de elementos de [las matrices de atributos personalizadas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) está predeterminado en 25. Las matrices que superen la cantidad máxima de elementos se truncarán para contenerla. El máximo para matrices individuales puede aumentarse hasta 100. Si deseas aumentar este máximo, ponte en contacto con tu administrador del servicio de atención al cliente.

Para establecer un atributo personalizado con un valor `array`:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Aumentar o disminuir atributos personalizados

Este código es un ejemplo de atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado con cualquier valor de `integer` o `long`:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objetivo-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Desactivar atributos personalizados

{% tabs %}
{% tab swift %}
Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `unsetCustomAttribute`.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objetivo-c %}
Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `unsetCustomAttributeWithKey`.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Atributos personalizados anidados

También puedes anidar propiedades dentro de atributos personalizados. En el siguiente ejemplo, se establece un objeto `favorite_book` con propiedades anidadas como atributo personalizado en el perfil de usuario. Para más detalles, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objetivo-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### Utilizar la API REST

También puedes utilizar nuestra API REST para establecer o desestablecer atributos de usuario. Para más información, consulta [Puntos finales de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

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
{% tab objetivo-c %}

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
{% tab objetivo-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Consulta la sección [Gestión de las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) para obtener más detalles.
