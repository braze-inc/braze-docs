{% multi_lang_include developer_guide/prerequisites/web.md %}

## Atributos predeterminados del usuario

### Métodos predefinidos

Braze proporciona métodos predefinidos para configurar los siguientes atributos de usuario dentro de la [clase`User`:](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)

- Nombre
- Apellido
- Idioma
- País
- Fecha de nacimiento
- Correo electrónico
- Género
- Ciudad natal
- Número de teléfono

### Configuración de atributos predeterminados

{% tabs %}
{% tab utilizando métodos %}
Para establecer un atributo predeterminado para un usuario, llama al método `getUser()` en tu instancia de Braze para obtener una referencia al usuario actual de tu aplicación. A continuación, puedes llamar a los métodos para establecer un atributo de usuario.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Al utilizar Google Tag Manager, los atributos estándar de usuario (como el nombre de pila de un usuario), deben registrarse del mismo modo que los atributos personalizados de usuario. Asegúrate de que los valores que pasas para los atributos estándar coinciden con el formato esperado especificado en la documentación de [la clase Usuario](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por ejemplo, el atributo género puede aceptar cualquiera de los siguientes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Por lo tanto, para establecer el sexo de un usuario como femenino, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Desactivar atributos predeterminados

Para desactivar un atributo predeterminado del usuario, pasa `null` al método correspondiente. Por ejemplo:

{% tabs local %}
{% tab Nombre %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Género %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Fecha de nacimiento %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Atributos personalizados del usuario

### Establecer atributos personalizados

{% tabs %}
{% tab utilizando métodos %}
Además de los métodos predeterminados de atributos de usuario, también puedes establecer [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para tus usuarios. Especificaciones completas del método, consulta [nuestros JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Para establecer un atributo personalizado con un valor `string`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Para establecer un atributo personalizado con un valor `integer`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

{% endsubtab %}
{% subtab Date %}
Para establecer un atributo personalizado con un valor `date`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```

{% endsubtab %}
{% subtab Array %}

Puedes tener hasta 25 elementos en matrices de atributos personalizadas. Las matrices individuales que se establecen manualmente (no se detectan automáticamente) para el **Tipo de datos** pueden aumentarse hasta 100 en el panel de Braze, en **Configuración de datos** > **Atributos** personalizados **.** Si quieres aumentar este máximo, ponte en contacto con tu director de cuentas Braze.

[Las matrices]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) que superen la cantidad máxima de elementos se truncarán para contener el número máximo de elementos.

Para establecer un atributo personalizado con un valor `array`:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Las fechas pasadas a Braze con este método deben ser objetos Date de JavaScript.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Las claves y valores de los atributos personalizados sólo pueden tener un máximo de 255 caracteres. Para más información sobre los valores válidos de atributos personalizados, consulta la [documentación de referencia](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Los atributos personalizados de usuario no están disponibles debido a una limitación del lenguaje de programación de Google Tag Manager. Para registrar atributos personalizados, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
La plantilla GTM no admite propiedades anidadas sobre eventos o compras. Puedes utilizar el HTML anterior para registrar cualquier evento o compra que requiera propiedades anidadas.
{% endalert %}
{% endtab %}
{% endtabs %}

### Desactivar atributos personalizados

Para desactivar un atributo personalizado, pasa `null` al método correspondiente.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Atributos personalizados anidados

También puedes anidar propiedades dentro de atributos personalizados. En el siguiente ejemplo, se establece un objeto `favorite_book` con propiedades anidadas como atributo personalizado en el perfil de usuario. Para más detalles, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Utilizar la API REST

También puedes utilizar nuestra API REST para establecer o desestablecer atributos de usuario. Para más información, consulta [Puntos finales de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción para tus usuarios (por correo electrónico o push), llama a las funciones `setEmailNotificationSubscriptionType()` o `setPushNotificationSubscriptionType()`, respectivamente. Ambas funciones toman como argumentos el tipo `enum` `braze.User.NotificationSubscriptionTypes` . Este tipo tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando un usuario se registra para recibir notificaciones push, el navegador le obliga a elegir entre permitir o bloquear las notificaciones, y si elige permitir las notificaciones push, éstas se configuran por defecto en `OPTED_IN`. 

Visita [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para obtener más información sobre la implementación de las suscripciones y las adhesiones voluntarias explícitas.

### Cancelar suscripción de un usuario a un correo electrónico

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Cancelar suscripción de un usuario desde push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
