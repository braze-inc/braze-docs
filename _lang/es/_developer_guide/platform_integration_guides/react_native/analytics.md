---
nav_title: Análisis
article_title: Análisis para React Native
platform: React Native
page_order: 5
description: "Este artículo explica cómo configurar y realizar un seguimiento de los análisis básicos, como el seguimiento de sesiones, el registro de eventos personalizados, etc., en la aplicación React Native."

---
 
# Análisis de React Native

> Este artículo explica cómo configurar y hacer un seguimiento de los análisis básicos en tu aplicación React Native.

Antes de empezar, lee nuestro artículo [Resumen de análisis]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) para obtener más información sobre los análisis de Braze y lo que ya se sigue de forma predeterminada. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Seguimiento de la sesión

El SDK Braze informa de los datos de sesión utilizados por el panel Braze para calcular la interacción del usuario y otros análisis esenciales para comprender a tus usuarios. Basándose en la siguiente semántica de sesión, nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y los recuentos de sesiones visibles dentro del panel Braze.

Para establecer un ID de usuario o iniciar una sesión, utiliza el método `changeUser`, que toma un parámetro de ID de usuario.

```javascript
Braze.changeUser("user_id");
```

## Registro de eventos personalizados

Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios por sus acciones en el panel.

```javascript
Braze.logCustomEvent("react_native_custom_event");
```

Puedes añadir metadatos sobre el evento pasando un objeto de propiedades con tu evento personalizado.

```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## Registro de atributos personalizados

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

### Atributos predeterminados del usuario

Para asignar atributos de usuario recogidos automáticamente por Braze, puedes utilizar los métodos setter que vienen con el SDK.

```javascript
Braze.setFirstName("Name");
```

Se admiten los siguientes atributos:

- Nombre
- Apellido
- Género
- Fecha de nacimiento
- Ciudad natal
- País
- Número de teléfono
- Idioma
- Correo electrónico

Todos los valores de cadena como nombre, apellidos, país y ciudad de residencia están limitados a 255 caracteres.

### Atributos personalizados del usuario

Además de nuestros métodos predefinidos de atributos de usuario, Braze también proporciona [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para hacer un seguimiento de los datos de tus aplicaciones. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Desactivar un atributo personalizado


```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Matrices de atributos personalizadas

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```

## Registrar compras

Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

Por ejemplo:

```javascript
Braze.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
Si introduces un valor de `10 USD` y una cantidad de `3`, se registrarán en el perfil del usuario tres compras de 10 dólares por un total de 30 dólares. Las cantidades deben ser inferiores o iguales a 100. Los valores de las compras pueden ser negativos.
{% endalert %}

### Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Claves reservadas

Las siguientes claves están **reservadas** y **no pueden** utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

