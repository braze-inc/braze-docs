{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Atributos predeterminados del usuario

### Métodos predefinidos

Braze proporciona métodos predefinidos para configurar los siguientes atributos de usuario utilizando el objeto `BrazeBinding`. Para más información, consulta [el archivo de declaración de Unity de Braze](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Nombre
- Apellido
- Correo electrónico del usuario
- Género
- Fecha de nacimiento
- País del usuario
- Ciudad de residencia del usuario
- Suscripción por correo electrónico del usuario
- Suscripción push de usuario
- Número de teléfono del usuario

### Configuración de atributos predeterminados

Para establecer un atributo predeterminado, llama al método correspondiente en el objeto `BrazeBinding`.

{% tabs local %}
{% tab Nombre %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Apellidos %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab Correo electrónico %}
```csharp
BrazeBinding.SetUserEmail("email@email.com");
```
{% endtab %}
{% tab Género %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Fecha de nacimiento %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab País %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Ciudad de origen %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Suscripción por correo electrónico %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Suscripción push %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Número de teléfono %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Desactivar atributos predeterminados

Para desactivar un atributo predeterminado del usuario, pasa `null` al método correspondiente.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Atributos personalizados del usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes. Para más información sobre la opción de segmentación de cada atributo, consulta [Recopilación de datos de usuario]({{site.baseurl}}/developer_guide/analytics).

### Establecer atributos personalizados

Para establecer un atributo personalizado, utiliza el método correspondiente para el tipo de atributo: 

{% tabs %}
{% tab Cadena %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Entero %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Doble %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Booleano %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Fecha %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Las fechas que se pasen a Braze deben estar en el formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (como `2013-07-16T19:20:30+01:00`) o en el formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (como`2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}

{% tab Matriz %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.
{% endalert %}

### Desactivar atributos personalizados

Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `UnsetCustomUserAttribute`. 

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Utilizar la API REST

También puedes utilizar nuestra API REST para establecer o desestablecer atributos de usuario. Para más información, consulta [Puntos finales de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción por correo electrónico o push para tus usuarios, llama a una de las siguientes funciones.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Ambas funciones toman como argumento `Appboy.Models.AppboyNotificationSubscriptionType`, que tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `UNSUBSCRIBED` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Windows no necesita una adhesión voluntaria explícita para enviar notificaciones push a los usuarios. Cuando un usuario se registra para push, se establece de manera predeterminada `SUBSCRIBED` en lugar de `OPTED_IN`. Para saber más, consulta nuestra documentación sobre [la implementación de suscripciones y adhesiones voluntarias explícitas]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Tipo de suscripción                        | Descripción |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Los usuarios se configurarán en `SUBSCRIBED` automáticamente al recibir una dirección de correo electrónico válida. Sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OPTED_IN` cuando recibas el consentimiento explícito de tu usuario. Visita nuestro documento [Cambiar las suscripciones de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) para más detalles. |
| `PushNotificationSubscriptionType`       | Los usuarios se configurarán en `SUBSCRIBED` automáticamente tras un registro push válido. Sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OPTED_IN` cuando recibas el consentimiento explícito de tu usuario. Visita nuestro documento [Cambiar las suscripciones de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) para más detalles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Estos tipos se incluyen en `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Configuración de las suscripciones por correo electrónico

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Configuración de suscripciones a notificaciones push

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
