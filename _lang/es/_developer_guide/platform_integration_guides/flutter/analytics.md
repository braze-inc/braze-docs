---
nav_title: Análisis
article_title: Análisis para Flutter
platform: Flutter
page_order: 5
description: "Este artículo explica cómo configurar y hacer un seguimiento de los análisis básicos en la aplicación Flutter."

---
 
# Análisis de Flutter

> Este artículo explica cómo configurar y hacer un seguimiento de los análisis básicos en tu aplicación Flutter.

Antes de empezar, lee nuestro artículo [Resumen de análisis]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) para obtener más información sobre los análisis de Braze y lo que ya se sigue de forma predeterminada. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Seguimiento de la sesión

El SDK de Braze informa de los datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. Basándose en la siguiente semántica de sesión, nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y los recuentos de sesiones visibles dentro del panel Braze.

Para establecer un ID de usuario o iniciar una sesión, utiliza el método `changeUser`, que toma un parámetro de ID de usuario.

```dart
braze.changeUser('user_id');
```

## Registro de eventos personalizados

Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios por sus acciones en el panel.

```dart
braze.logCustomEvent('my_custom_event');
```

Puedes añadir metadatos sobre el evento pasando un objeto de propiedades con tu evento personalizado.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## Registro de atributos personalizados

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

### Atributos predeterminados del usuario

Para asignar atributos de usuario recogidos automáticamente por Braze, puedes utilizar los métodos setter que vienen con el SDK.

```dart
braze.setFirstName('Name');
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

### Configuración de valores de atributos personalizados

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes:

{% tabs %}
{% tab Valor booleano %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab Entero %}

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Doble %}
```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Cadena %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Fecha %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Matriz %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### Desactivar un atributo personalizado

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## Registrar compras

Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

Por ejemplo:

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
Si introduces un valor de `10 USD` y una cantidad de `3`, se registrarán en el perfil del usuario tres compras de 10 dólares por un total de 30 dólares. Las cantidades deben ser inferiores o iguales a 100. Los valores de las compras pueden ser negativos.
{% endalert %}

### Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

