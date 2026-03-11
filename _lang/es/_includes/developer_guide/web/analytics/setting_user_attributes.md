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
{% tab using methods %}
Para establecer un atributo predeterminado para un usuario, llama al`getUser()`método en tu instancia de Braze para obtener una referencia al usuario actual de tu aplicación. A continuación, puedes llamar a métodos para establecer un atributo de usuario.

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

{% tab google tag manager %}
Con Google Tag Manager, los atributos de usuario estándar (como el nombre de usuario) deben registrarse de la misma manera que los atributos de usuario personalizados. Asegúrate de que los valores que pasas para los atributos estándar coinciden con el formato esperado especificado en la documentación de [la clase Usuario](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por ejemplo, el atributo género puede aceptar cualquiera de los siguientes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Por lo tanto, para establecer el sexo de un usuario como femenino, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Desactivar los atributos predeterminados

Para desactivar un atributo de usuario predeterminado, pasa`null`  al método relacionado. Por ejemplo:

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Atributos personalizados del usuario

### Establecer atributos personalizados

{% tabs %}
{% tab using methods %}
Además de los métodos de atributos de usuario predeterminados, también puedes establecer [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para tus usuarios. Para obtener las especificaciones completas del método, consulta [nuestros JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Para establecer un atributo personalizado con un`string`valor:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Para establecer un atributo personalizado con un`integer`valor:

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
Para establecer un atributo personalizado con un`date`valor:

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

Puedes tener hasta 25 elementos en las matrices de atributos personalizados. Las matrices individuales que se configuran manualmente (no se detectan automáticamente) para **el tipo de datos** se pueden aumentar hasta 500 en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Para aumentar este límite por encima de 500, ponte en contacto con tu director de cuentas de Braze.

[Las matrices]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) que superen la cantidad máxima de elementos se truncarán para contener el número máximo de elementos.

Para establecer un atributo personalizado con un`array`valor:

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
Las claves y los valores de los atributos personalizados solo pueden tener un máximo de 255 caracteres. Para obtener más información sobre los valores válidos de los atributos personalizados, consulta la [documentación de referencia](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab google tag manager %}
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

Para desactivar un atributo personalizado, pasa`null`  al método relacionado.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Atributo personalizado anidado

También puedes anidar propiedades dentro de atributos personalizados. En el siguiente ejemplo, un`favorite_book`objeto con propiedades anidadas se establece como un atributo personalizado en el perfil de usuario. Para obtener más información, consulta [Attributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Uso de la API REST

También puedes utilizar nuestra API REST para establecer o desactivar atributos de usuario. Para obtener más información, consulta [Puntos finales]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) de [datos de]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) [usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuración de suscripciones de usuarios

Para configurar una suscripción para tus usuarios (por correo electrónico o push), llama a las funciones `setEmailNotificationSubscriptionType()` o `setPushNotificationSubscriptionType()`, respectivamente. Ambas funciones toman el`enum`tipo`braze.User.NotificationSubscriptionTypes`como argumento. Este tipo tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando un usuario se registra para recibir notificaciones push, el navegador le obliga a elegir entre permitir o bloquear las notificaciones, y si elige permitir las notificaciones push, éstas se configuran por defecto en `OPTED_IN`. 

Visita [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para obtener más información sobre la implementación de las suscripciones y las adhesiones voluntarias explícitas.

### Cancelar la suscripción del usuario al correo electrónico

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Cancelar la suscripción de un usuario a las notificaciones push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
