---
nav_title: Recomendaciones de la IA
article_title: Crear recomendaciones de elementos de IA
description: "Este artículo de referencia explica cómo crear una recomendación de artículos de IA para los artículos de un catálogo."
page_order: 1
---

# Crear recomendaciones de elementos de IA

> Aprende a crear una herramienta de recomendaciones de IA a partir de los elementos de tu catálogo.

## Acerca de las recomendaciones de artículos AI

Utiliza las recomendaciones de artículos de IA para calcular los productos más populares o crear recomendaciones de IA personalizadas para un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) específico. Después de crear tu recomendación, puedes utilizar la personalización para insertar esos productos en tus mensajes.

{% alert tip %}
[Las recomendaciones personalizadas con IA](#recommendation-types) funcionan mejor con cientos o miles de artículos y, normalmente, al menos 30.000 usuarios con datos de compra o interacción. Esto es sólo una guía aproximada y puede variar. Los otros tipos de recomendación pueden funcionar con menos datos.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Crear una recomendación de artículo de IA

### Requisitos previos

Antes de empezar, tendrás que completar lo siguiente:

- Debes tener al menos un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) para utilizar cualquiera de los tipos de recomendación descritos a continuación.
- Debes tener datos de compra o evento en Braze (eventos personalizados o el objeto de compra) que incluyan una referencia a ID de producto únicos almacenados en un catálogo.

### Paso 1: Crear una nueva recomendación

Puedes crear una recomendación de elemento de IA desde cualquier lugar del panel:

{% tabs local %}
{% tab From the navigation menu %}
1. Ve a **Análisis** > **Recomendación de elementos de IA**.
2. Selecciona **Crear predicción** > **Recomendación de elementos AI**.
{% endtab %}

{% tab From a catalog %}
También puedes elegir crear una recomendación directamente desde un catálogo individual. Selecciona tu catálogo en la página **Catálogos** y, a continuación, selecciona **Crear recomendación**.
{% endtab %}
{% endtabs %}

### Paso 2: Añadir detalles de la recomendación

Dale a tu recomendación un nombre y una descripción opcional.

\!["Detalles de la recomendación" paso con los campos nombre y descripción.]({% image_buster /assets/img/item_recs_1.png %})

### Paso 3: Define tu recomendación {#recommendation-type}

Selecciona un tipo de recomendación. Cada tipo utiliza los últimos seis meses de datos de interacción de artículos, como una compra o datos de eventos personalizados. Para obtener información más detallada y casos de uso de cada uno, consulta [Tipos y casos de uso]({{site.baseurl}}/user_guide/brazeai/recommendations/).

{% alert tip %}
Al utilizar **Más recientes** o **AI personalizada**, los usuarios con datos insuficientes para crear recomendaciones individualizadas recibirán los elementos **Más populares** como alternativa. La proporción de usuarios que reciben la alternativa **Más popular** se muestra en la página **de análisis**.
{% endalert %}

#### Paso 3.1: Excluir compras o interacciones anteriores (opcional)

Para evitar sugerir artículos que un usuario ya haya comprado o con los que ya haya interactuado, selecciona **No recomendar artículos con los que los usuarios hayan interactuado previamente**. Esta opción sólo está disponible cuando el **Tipo de** recomendación está configurado como **AI Personalizado**.

\!["Define tu recomendación" paso con "AI Personalizada" como tipo y la opción "No recomendar artículos con los que los usuarios hayan interactuado previamente" seleccionada.]({% image_buster /assets/img/item_recs_2-3.png %})

Esta configuración impide que la mensajería reutilice los artículos que un usuario ya ha comprado o con los que ya ha interactuado, siempre que la recomendación se haya actualizado recientemente. Los artículos comprados o con los que se haya interactuado entre las actualizaciones de las recomendaciones pueden seguir apareciendo. En la versión gratuita de las recomendaciones de artículos, las actualizaciones son semanales. Para la versión pro de las recomendaciones de elementos de IA, las actualizaciones se producen cada 24 horas.

Por ejemplo, al utilizar la versión pro de las recomendaciones de artículos de IA, si un usuario compra algo y luego recibe un correo electrónico de marketing en 30 minutos, es posible que el artículo que acaba de comprar no se excluya del correo electrónico a tiempo. Sin embargo, los mensajes enviados después de 24 horas no incluirán ese elemento.

#### Paso 3.2: Selecciona un catálogo

Si aún no está rellenado, selecciona el [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) del que esta recomendación extraerá artículos.

#### Paso 3.3: Añade una selección (opcional)

Si quieres tener más control sobre tu recomendación, elige una [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para aplicar filtros personalizados. Las selecciones filtran las recomendaciones por columnas específicas de tu catálogo, como marca, tamaño o ubicación. Las selecciones que contienen Liquid no pueden utilizarse en tu recomendación.

\![Un ejemplo de la selección "en stock" seleccionada para la recomendación.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Si no encuentras tu selección, asegúrate primero de que está configurada en tu catálogo.
{% endalert %}

### Paso 4: Selecciona la interacción para impulsar las recomendaciones

Selecciona el evento para el que quieres que se optimice esta recomendación. Este evento suele ser una compra, pero también puede ser cualquier interacción con un artículo.

Puedes optimizar para:

- Eventos de compra con el [Objeto de Compra]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Eventos personalizados que representan una compra
- Eventos personalizados que representen cualquier otra interacción con elementos (como vistas de productos, clics o reproducciones multimedia)

Si eliges **Evento personalizado**, selecciona tu evento de la lista.

\![El evento personalizado "Compra finalizada" seleccionado como la forma en que se realiza actualmente el seguimiento de los eventos.]({% image_buster /assets/img/item_recs_3.png %})

### Paso 5: Elige el nombre de la propiedad correspondiente {#property-name}

Para crear una recomendación, tienes que decirle a Braze qué campo de tu evento de interacción (objeto de compra o evento personalizado) tiene el identificador único que coincide con el campo `id` de un artículo en el catálogo. ¿No estás seguro? [Ver requisitos](#requirements).

Selecciona este campo para el **Nombre de la propiedad**.

El campo **Nombre de propiedad** se rellenará previamente con una lista de campos enviados a través del SDK a Braze. Si se proporcionan datos suficientes, estas propiedades también se clasificarán por orden de probabilidad de ser la propiedad correcta. Selecciona la que corresponda al campo `id` del catálogo.

\![El nombre de la propiedad "purchase_item" seleccionada que corresponde al ID del artículo en el catálogo.]({% image_buster /assets/img/item_recs_4.png %})

#### Requisitos {#requirements}

Hay algunos requisitos para seleccionar tu propiedad:

- Debe estar mapeado en el campo `id` de tu catálogo seleccionado.
- **Si has seleccionado Objeto de compra:** Debe ser el `product_id` o un campo del `properties` de tu evento de interacción.
- **Si has seleccionado Evento personalizado:** Debe ser un campo de tu evento personalizado `properties`.
- Los campos anidados deben escribirse en el desplegable **Nombre de la propiedad** en notación de puntos con el formato `event_property.nested_property`. Por ejemplo, si seleccionas la propiedad anidada `district_name` dentro de la propiedad de evento `location`, introducirías `location.district_name`.
- El campo puede estar dentro de una matriz de productos, o terminar con una matriz de ID. En cualquier caso, cada ID de producto se tratará como un evento independiente y secuencial con la misma marca de tiempo.

#### Ejemplos de mapeados

Los siguientes ejemplos de mapeados hacen referencia a este catálogo de muestra:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">título</th>
    <th class="tg-0pky">precio</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Negro Talla 7</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Rojo Talla 8</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas Blanco Talla 9</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Morado Talla 10</td>
    <td class="tg-0pky">75,00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Custom event %}

Supongamos que quieres utilizar el evento personalizado `added_to_cart` para poder recomendar productos similares antes de que el cliente pase por caja. El evento `added_to_cart` tiene una propiedad de evento `product_sku`.

Entonces la propiedad `product_sku` debe incluir al menos uno de los valores de la columna `id` del catálogo de muestras: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" o "ADI-PP-10". No necesitas eventos para cada elemento del catálogo, pero necesitas algunos para que la herramienta de recomendaciones tenga suficiente contenido con el que trabajar.

##### Ejemplo de objeto evento personalizado

Este evento tiene `"product_sku": "ADI-BL-7"`, que coincide con el primer elemento del catálogo de muestras.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Ejemplo de objeto evento personalizado con una matriz de productos

Si las propiedades del evento contienen varios productos en una matriz, cada ID de producto se tratará como un evento independiente y secuencial. Este evento puede utilizar la propiedad `products.sku` para que coincida con el primer y el tercer elemento del catálogo de muestras.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Ejemplo de objeto evento personalizado con un objeto anidado que contiene una matriz de ID de producto

Si los ID de tus productos son valores de una matriz en lugar de objetos, puedes utilizar la misma notación y cada ID de producto se tratará como un evento secuencial independiente. Esto puede combinarse de forma flexible con objetos anidados en el siguiente evento configurando la propiedad como `purchase.product_skus` para que coincida con el primer y el tercer elemento del catálogo de muestra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Purchase object %}

Se pasa un objeto de compra a través de la API cuando se ha realizado una compra.

En cuanto al mapeado, para los objetos de compra se aplica una lógica similar a la de los eventos personalizados, con la diferencia de que puedes elegir entre utilizar el `product_id` del objeto de compra o un campo del objeto `properties`.

Recuerda que no necesitas eventos para cada elemento del catálogo, pero sí algunos de ellos para que la herramienta de recomendaciones tenga suficiente contenido con el que trabajar.

##### Ejemplo de objeto de compra mapeado a ID de producto

Este evento tiene `"product_id": "ADI-BL-7`, que mapea al primer elemento del catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Ejemplo de objeto de compra mapeado a un campo de propiedades

Este evento tiene una propiedad de `"sku": "ADI-RD-8"`, que mapea al segundo elemento del catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Paso 6: Entrena la recomendación

Cuando estés listo, selecciona **Crear recomendación**. Este proceso puede durar entre 10 minutos y 36 horas. Recibirás una actualización por correo electrónico cuando la recomendación se haya formado correctamente o una explicación de por qué puede haber fallado la creación.

Puedes encontrar la recomendación en la página **Predicciones**, donde luego puedes editarla o archivarla según necesites. Las recomendaciones se reciclarán automáticamente una vez a la semana (de pago) o al mes (gratis).