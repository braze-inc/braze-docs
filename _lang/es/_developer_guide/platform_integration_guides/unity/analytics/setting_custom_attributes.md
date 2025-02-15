---
nav_title: Configuración de atributos personalizados
article_title: Configuración de atributos personalizados para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Este artículo de referencia explica cómo configurar y desconfigurar atributos personalizados en la plataforma Unity."

---

# Configuración de atributos personalizados

> Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [Mejores prácticas][1].

## Asignar atributos predeterminados al usuario

Para asignar atributos de usuario, tienes que llamar al método apropiado del objeto BrazeBinding. La siguiente es una lista de atributos incorporados que pueden invocarse mediante este método.

### Nombre
`AppboyBinding.SetUserFirstName("first name");`

### Apellido
`AppboyBinding.SetUserLastName("last name");`

### Correo electrónico del usuario
`AppboyBinding.SetUserEmail("email@email.com");`

>  Sigue siendo útil configurar las direcciones de correo electrónico aunque no envíes correos electrónicos a través de Braze. El correo electrónico facilita la búsqueda de perfiles de usuarios individuales y la solución de problemas a medida que surgen.

### Género
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### Fecha de nacimiento
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### País del usuario
`AppboyBinding.SetUserCountry("country name");`

### Ciudad de residencia del usuario
`AppboyBinding.SetUserHomeCity("city name");`

### Suscripción por correo electrónico del usuario
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Suscripción push de usuario
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Número de teléfono del usuario
`AppboyBinding.SetUserPhoneNumber("phone number");`

## Asignar atributos personalizados al usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes:
Para más información sobre las opciones de segmentación que te ofrece cada uno de estos atributos, consulta nuestra [ documentación sobre "Buenas prácticas"][1] en esta sección.

### Configuración de valores de atributos personalizados

{% tabs %}
{% tab Valor booleano %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab Cadena %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab Fecha %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  Las fechas transmitidas a Braze deben estar en el formato [ISO 8601][2], e.g `2013-07-16T19:20:30+01:00` o en el formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` e.g `2016-12-14T13:32:31.601-0800`

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
{% endtabs
%}
### Desactivar un atributo personalizado

Los atributos personalizados también se pueden desactivar utilizando el siguiente método:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## Configuración de un atributo personalizado a través de la API REST
También puedes utilizar nuestra API REST para establecer atributos de usuario. Para ello, consulta la [documentación de la API de usuario][3].

## Límites del valor del atributo personalizado
Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción para tus usuarios (por correo electrónico o push), llama a las funciones     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` o `AppboyBinding.SetPushNotificationSubscriptionType()`, respectivamente. Estas dos funciones toman como argumentos los parámetros `Appboy.Models.AppboyNotificationSubscriptionType`. Este tipo tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `UNSUBSCRIBED` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Windows no necesita una adhesión voluntaria explícita para enviar notificaciones push a los usuarios. Cuando un usuario se registra para push, se establece de manera predeterminada `SUBSCRIBED` en lugar de `OPTED_IN`. Para saber más, consulta nuestra documentación sobre [la implementación de suscripciones y adhesiones voluntarias explícitas][10].

- `EmailNotificationSubscriptionType`
  - Los usuarios se configurarán en `SUBSCRIBED` automáticamente al recibir una dirección de correo electrónico válida. Sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OPTED_IN` cuando recibas el consentimiento explícito de tu usuario. Visita nuestro documento [Cambiar las suscripciones de usuario][8] para más detalles.
- `PushNotificationSubscriptionType`
  - Los usuarios se configurarán en `SUBSCRIBED` automáticamente tras un registro push válido. Sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OPTED_IN` cuando recibas el consentimiento explícito de tu usuario. Visita nuestro documento [Cambiar las suscripciones de usuario][8] para más detalles.

>  Estos tipos se incluyen en `Appboy.Models.AppboyNotificationSubscriptionType`.

## Ejemplo de código

### Suscripción por correo electrónico:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Suscripción a notificaciones push:

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
