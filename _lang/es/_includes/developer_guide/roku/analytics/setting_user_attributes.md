{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Atributos predeterminados del usuario

### Métodos predefinidos

Braze proporciona métodos predefinidos para configurar los siguientes atributos de usuario utilizando el objeto `m.Braze`.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Configuración de atributos predeterminados

Para establecer un atributo predeterminado, llama al método correspondiente en el objeto `m.Braze`.

{% tabs local %}
{% tab Nombre %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Apellidos %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab Correo electrónico %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Género %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Fecha de nacimiento %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab País %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Idioma %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Ciudad de origen %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Número de teléfono %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## Atributos personalizados del usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes.

### Configuración de atributos personalizados

{% tabs %}
{% tab Cadena %}
Para establecer un atributo personalizado un valor `string`:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Entero %}
Para establecer un atributo personalizado con un valor `integer`:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Puntos flotantes %}
Braze trata exactamente igual los valores `float` y `double`. Para establecer un atributo personalizado con cualquier valor:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Booleano %}
Para establecer un atributo personalizado con un valor `boolean`:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Fecha %}
Para establecer un atributo personalizado con un valor `date`:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Matriz %}
Para establecer un atributo personalizado con un valor `array`:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.
{% endalert %}

### Aumento y disminución de atributos personalizados

Este código es un ejemplo de atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado en cualquier valor entero positivo o negativo.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Desactivar atributos personalizados

Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `unsetCustomAttribute`.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Utilizar la API REST

También puedes utilizar nuestra API REST para establecer o desestablecer atributos de usuario. Para más información, consulta [Puntos finales de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuración de las suscripciones por correo electrónico

Puedes configurar los siguientes estados de suscripción por correo electrónico para tus usuarios mediante programación a través del SDK.

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `OptedIn` | Suscrito y con adhesión voluntaria explícita |
| `Subscribed` | Suscrito, pero sin adhesión voluntaria explícita |
| `UnSubscribed` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Estos tipos se incluyen en `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

El método para configurar el estado de la suscripción por correo electrónico es `setEmailSubscriptionState()`. Los usuarios se configurarán en `Subscribed` automáticamente al recibir una dirección de correo electrónico válida, sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OptedIn` al recibir el consentimiento explícito de tu usuario. Para más detalles, visita [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
