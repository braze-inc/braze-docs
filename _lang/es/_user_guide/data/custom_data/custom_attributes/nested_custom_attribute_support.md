---
nav_title: Atributos personalizados anidados
article_title: Atributos personalizados anidados
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre el uso de atributos personalizados anidados como tipo de datos para atributos personalizados, incluyendo limitaciones y ejemplos de uso."
---

# Atributos personalizados anidados

> Esta página trata de los atributos personalizados anidados, que te permiten definir un conjunto de atributos como propiedad de otro atributo. En otras palabras, cuando se define un objeto de atributo personalizado, se puede definir un conjunto de atributos adicionales para ese objeto.

Digamos que quieres definir un atributo personalizado en el perfil de usuario llamado `favorite_book`. Este atributo personalizado puede definirse como un objeto que tiene los atributos anidados `title`, `author`, y `publishing_date`, de la siguiente manera:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```

Estos datos anidados le permiten crear segmentos utilizando información de un objeto de atributo personalizado, y personalizar sus mensajes utilizando un objeto de atributo personalizado y Liquid.

Los objetos de atributo personalizados pueden contener [tipos de datos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types), como:

- Números
- Cadenas
- Booleanos
- Matrices
- Tiempo
  - Al filtrar un atributo personalizado de hora anidado, puede elegir filtrar en función del "Día del año" o de la "Hora". "Día del año" comprobará sólo el mes y el día para la comparación. "Hora" comparará la marca de tiempo completa, incluido el año.
- Otros objetos
- [Matrices de objetos]({{site.baseurl}}/array_of_objects/)

## Limitaciones

- Los atributos personalizados anidados están pensados para atributos personalizados enviados a través del SDK o la API de Braze. 
- Los objetos tienen un tamaño máximo de 100 KB.
- Los nombres de las claves y los valores de las cadenas tienen un límite de tamaño de 255 caracteres.
- Los nombres de las claves no pueden contener espacios.
- Los puntos (`.`) y los signos de dólar (`$`) no son caracteres admitidos en una carga útil de la API si intentas enviar un atributo personalizado anidado a un perfil de usuario.
- No todos los socios Braze admiten atributos personalizados anidados. Consulta la [documentación del socio]({{site.baseurl}}/partners/home) para confirmar si determinadas integraciones del socio admiten esta característica.
- Los atributos personalizados anidados no se pueden utilizar como filtro al realizar una llamada a la API de Connected Audience.

## Ejemplo de API

{% tabs local %}
{% tab Crear %}
A continuación se muestra un ejemplo de `/users/track` con un objeto "Canción más reproducida". Para capturar las propiedades de la canción, enviaremos una solicitud de API que incluya `most_played_song` como objeto, junto con un conjunto de propiedades del objeto.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Actualización %}
Para actualizar un objeto existente, envíe un POST a `users/track` con el parámetro `_merge_objects` en la solicitud. Esto fusionará en profundidad su actualización con los datos existentes del objeto. La fusión profunda garantiza que todos los niveles de un objeto se fusionen en otro objeto en lugar de sólo el primer nivel. En este ejemplo, ya tenemos un objeto `most_played_song` en Braze, y ahora estamos añadiendo un nuevo campo, `year_released`, al objeto `most_played_song`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Una vez recibida esta solicitud, el objeto de atributo personalizado tendrá el siguiente aspecto:

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
Debe establecer `_merge_objects` en `true`, o sus objetos se sobrescribirán. `_merge_objects` es `false` por defecto.
{% endalert %}

{% endtab %}
{% tab Borrar %}
Para eliminar un objeto de atributo personalizado, envíe un POST a `users/track` con el objeto de atributo personalizado configurado en `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Este método no puede utilizarse para eliminar una clave anidada dentro de una [matriz de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects).
{% endalert %}

{% endtab %}
{% endtabs %}

## Ejemplo de SDK

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab SDK para Android %}

**Crear**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Actualizar**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Eliminar**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab SDK de Swift %}

**Crear**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Actualizar**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Eliminar**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab SDK Web %}

**Crear**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Actualizar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Eliminar**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Captura de fechas como propiedades de objetos

Para capturar fechas como propiedades de objetos, debes utilizar la clave `$time`. En el siguiente ejemplo, se utiliza un objeto "Fechas importantes" para capturar el conjunto de propiedades del objeto, `birthday` y `wedding_anniversary`. El valor de estas fechas es un objeto con una clave `$time`, que no puede ser un valor nulo.

{% alert note %}
Si inicialmente no ha capturado las fechas como propiedades del objeto, le recomendamos que reenvíe estos datos utilizando la clave `$time` para todos los usuarios. De lo contrario, podrían aparecer segmentos incompletos al utilizar el atributo `$time`. Sin embargo, si el valor de `$time` en un atributo personalizado anidado no tiene el formato correcto, no se actualizará todo el atributo personalizado anidado.
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Para los atributos personalizados anidados, si el año es menor que 0 o mayor que 3000, Braze no almacena estos valores en el usuario.
{% endalert %}

## Plantillas de Liquid

El siguiente ejemplo de plantilla de Liquid muestra cómo hacer referencia a las propiedades del objeto de atributo personalizado guardadas de la solicitud de API anterior y utilizarlas en su mensajería.

Utilice la etiqueta de personalización `custom_attribute` y la notación de puntos para acceder a las propiedades de un objeto. Especifique el nombre del objeto (y la posición en la matriz si hace referencia a una matriz de objetos), seguido de un punto, seguido del nombre de la propiedad.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` - "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` - "Soleá"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` - "1000"
{% endraw %}

![Utilizando Liquid para crear una plantilla con el nombre de una canción y el número de veces que un oyente ha reproducido esa canción en un mensaje]({% image_buster /assets/img_archive/nca_liquid_2.png %})

## Segmentación

Puede crear segmentos basados en atributos personalizados anidados para segmentar aún más a sus usuarios. Para ello, filtre su segmento basándose en el objeto de atributo personalizado y, a continuación, especifique la ruta al nombre de la propiedad y el valor asociado sobre el que desea segmentar. Si no está seguro de cómo es esa ruta, puede [generar un esquema](#generate-schema) y utilizar el explorador de objetos anidados para que Braze rellene esa ruta por usted.

Tras añadir una ruta a tu propiedad, selecciona **Validar** para comprobar que el valor del campo de la ruta es válido.

![Filtrado basado en un atributo personalizado de la canción más reproducida cuando un oyente ha reproducido una canción más de un número especificado de veces]({% image_buster /assets/img_archive/nca_segmentation_2.png %})

Para segmentar con atributos personalizados anidados, seleccione el filtro **Atributos personalizados anidados** para exponer un desplegable en el que puede seleccionar un atributo personalizado anidado específico.

![]({% image_buster /assets/img_archive/nested_custom_attributes.png %}){: style="max-width:70%;"}

Cuando trabaje con la segmentación de atributos personalizados anidados, tendrá acceso a un nuevo comparador agrupado por tipo de datos. Por ejemplo, como `play_analytics.count` es un número, puedes seleccionar un comparador en la categoría **Número**.

![Un usuario que elige un operador basado en el tipo de datos del atributo personalizado anidado]({% image_buster /assets/img_archive/nca_comparator.png %})

### Filtrado de tipos de datos temporales

Al filtrar un atributo personalizado de hora anidado, puede elegir filtrar con operadores en las categorías **Día del año** u **Hora** al comparar el valor de la fecha. 

Si selecciona un operador en la categoría **Día del año**, sólo se comprobarán para la comparación el mes y el día en lugar de la marca de tiempo completa del valor del atributo personalizado anidado. Al seleccionar un operador en la categoría **Hora**, se comparará la marca de tiempo completa, incluido el año.

### Segmentación multicriterios

Utilice **la Segmentación Multicriterio** para crear un segmento que coincida con varios criterios dentro de un mismo objeto. Esto califica al usuario en el segmento si tiene al menos una matriz de objetos que coincida con todos los criterios especificados. Por ejemplo, los usuarios sólo coincidirán con este segmento si su clave no está en blanco y si su número es superior a 0.

También puede utilizar la función **Copiar Liquid para segmento** para generar código Liquid para este segmento y utilizarlo en un mensaje. Por ejemplo, supongamos que tiene una matriz de objetos de cuenta y un segmento dirigido a clientes con cuentas imponibles activas. Para conseguir que los clientes contribuyan al objetivo de cuenta asociado a una de sus cuentas activas y sujetas a impuestos, deberá crear un mensaje para darles un empujón. 

![Un segmento de ejemplo con la casilla seleccionada para la Segmentación Multicriterio.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Al seleccionar **Copiar Liquid para segmento**, Braze generará automáticamente código Liquid que devuelva una matriz de objetos que sólo contenga cuentas activas y sujetas a impuestos.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

Desde aquí, puedes utilizar `segmented_nested_objects` y personalizar tu mensaje. En este ejemplo, queremos tomar un objetivo de la primera cuenta fiscal activa y personalizarlo:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Esto devuelve el siguiente mensaje a su cliente: "Alcanza tu objetivo de jubilación más rápido, ¡haz un depósito utilizando nuestra nueva función de depósito rápido!"

### Generar un esquema utilizando el explorador de objetos anidados {#generate-schema}

Puede generar un esquema para sus objetos para construir filtros de segmentos sin necesidad de memorizar rutas de objetos anidados. Para ello, siga estos pasos.

#### Paso 1: Generar un esquema

Para este ejemplo, supongamos que tenemos una matriz de objetos `accounts` que acabamos de enviar a Braze:

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

En el panel de Braze, ve a **Configuración de datos** > **Atributos personalizados**.

Busca tu objeto o matriz de objetos. En la columna **Nombre del atributo**, selecciona **Generar esquema**.

![]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
Su esquema puede tardar unos minutos en generarse, dependiendo de la cantidad de datos que nos haya enviado.
{% endalert %}

Una vez generado el esquema, aparece un nuevo botón <i class="fas fa-plus"></i> plus en lugar del botón **Generar esquema**. Puede hacer clic en él para ver lo que Braze sabe sobre este atributo personalizado anidado. 

Durante la generación del esquema, Braze examina los datos enviados anteriormente y construye una representación ideal de sus datos para este atributo. Braze también analiza y añade un tipo de datos para sus valores anidados. Esto se hace muestreando los datos anteriores enviados a Braze para el atributo anidado dado.

Para nuestro array de objetos `accounts`, puedes ver que dentro del array de objetos, hay un objeto que contiene lo siguiente:

- Un tipo booleano con una clave de `active` (independientemente de si la cuenta está activa o no)
- Un tipo de número con una clave de `balance` (importe del saldo en la cuenta)
- Un tipo de cadena con una clave de `type` (cuenta no imponible o imponible)

![]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:50%" }

Ahora que hemos analizado y construido una representación de los datos, vamos a construir un segmento.

#### Paso 2: Crea un segmento

Dirijámonos a los clientes con un saldo inferior a 100 para enviarles un mensaje que les anime a realizar un ingreso.

Cree un segmento y añada el filtro `Nested Custom Attribute`, después busque y seleccione su objeto o conjunto de objetos. Aquí hemos añadido la matriz de objetos `accounts`. 

![]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Selecciona el botón más <i class="fas fa-plus"></i> en el campo de la ruta. Esto mostrará una representación de su objeto o matriz de objetos. Puedes seleccionar cualquiera de los elementos de la lista y Braze los insertará en el campo de ruta por ti. En este ejemplo, necesitamos conseguir el equilibrio. Selecciona la balanza y la ruta (en este caso, `[].balance`) se rellenará automáticamente en el campo ruta.

![]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Puedes seleccionar **Validar** para comprobar que el contenido del campo de la ruta es válido y, a continuación, construir el resto del filtro según sea necesario. Aquí hemos especificado que el saldo debe ser inferior a 100.

![]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

Eso es todo. Acaba de crear un segmento utilizando un atributo personalizado anidado, todo ello sin necesidad de saber cómo están estructurados los datos. El explorador de objetos anidados de Braze generaba una representación visual de sus datos y le permitía explorar y seleccionar exactamente lo que necesitaba para crear un segmento.

### Activar cambios de atributos personalizados anidados

Puede disparar cuando cambia un objeto de atributo personalizado anidado. Esta opción no está disponible para cambios en matrices de objetos. Si no ve una opción para ver el explorador de rutas, compruebe que ha generado un esquema. 

![]({% image_buster /assets/img_archive/nca_triggered_changes2.png %})

Por ejemplo, en la siguiente campaña basada en acciones, puede añadir una nueva acción desencadenante para **Cambiar valor de atributo personalizado** para dirigirse a los usuarios que han cambiado sus preferencias de oficina de barrio. 

![]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

### Personalización

Mediante el modal **Añadir personalización**, también puede insertar atributos personalizados anidados en su mensajería. Seleccione **Atributos personalizados anidados** como tipo de personalización. A continuación, seleccione el atributo de nivel superior y la clave de atributo. 

Por ejemplo, en el modal de personalización que aparece a continuación, se inserta el atributo personalizado anidado de una oficina de barrio local basada en las preferencias de un usuario.

![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
Compruebe que se ha generado un esquema si no ve la opción de insertar atributos personalizados anidados.
{% endalert %}

### Regenerar esquemas {#regenerate-schema}

Una vez generado un esquema, puede regenerarse una vez cada 24 horas. Esta sección describe cómo regenerar su esquema. Para obtener información más detallada sobre los esquemas, consulte la sección de este artículo sobre la [generación de un esquema](#generate-schema).

Para regenerar el esquema de su atributo personalizado anidado:

1. Vaya a **Configuración de datos** > **Atributos personalizados**.
2. Busque su atributo personalizado anidado.
3. En la columna **Nombre del** atributo de tu atributo, selecciona <i class="fas fa-plus"></i> para administrar el esquema.
4. Aparecerá un modal. Selecciona **Regenerar esquema**.

La opción de regenerar el esquema se desactivará si han transcurrido menos de 24 horas desde la última regeneración del esquema. La regeneración del esquema sólo detectará los objetos nuevos y no borrará los objetos que ya existen en el esquema.

{% alert important %}
Para restablecer el esquema de una matriz de objetos con un objeto existente, debes crear un nuevo atributo personalizado. La regeneración del esquema no elimina los objetos existentes.
{% endalert %}

Si los datos no aparecen como se esperaba tras regenerar el esquema, puede que el atributo no se ingiera con la frecuencia suficiente. Los datos del usuario se muestrean en los datos anteriores enviados a Braze para el atributo anidado dado. Si el atributo no se ingiere lo suficiente, no se recogerá para el esquema.

## Puntos de datos

Cualquier clave que se envíe consume un punto de datos. Por ejemplo, este objeto inicializado en el perfil de usuario cuenta como siete (7) puntos de datos:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
La actualización de un objeto de atributo personalizado en `null` también consume un punto de datos.
{% endalert %}

