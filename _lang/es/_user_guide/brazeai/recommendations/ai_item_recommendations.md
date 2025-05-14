---
nav_title: Recomendaciones de elementos de IA
article_title: Recomendaciones de elementos de IA
page_order: 15
alias: "/ai_item_recommendations/"
description: "Este artículo de referencia explica cómo crear una recomendación de artículos de IA para los artículos de un catálogo."
---

# Recomendaciones de artículos de AI

> Aprende a crear una recomendación de artículos AI para los artículos de un catálogo.

Utiliza las recomendaciones de artículos de IA para calcular los productos más populares o crear recomendaciones de IA personalizadas para un [catalog][catalog]. Después de crear tu recomendación, puedes utilizar la personalización para insertar esos productos en tus mensajes.

## Requisitos previos

Antes de empezar, tendrás que completar lo siguiente:

- Debes tener al menos un [catálogo][catálogo] para utilizar cualquiera de los tipos de recomendación descritos a continuación.
- Debes tener datos de compra o evento en Braze (eventos personalizados o el objeto de compra) que incluyan una referencia a ID de producto únicos almacenados en un catálogo.

{% alert tip %}
[Las recomendaciones personalizadas con IA](#recommendation-types) funcionan mejor con cientos o miles de artículos y, normalmente, al menos 30.000 usuarios con datos de compra o interacción. Esto es sólo una guía aproximada y puede variar. Los otros tipos de recomendación pueden funcionar con menos datos.
{% endalert %}

## Crear una recomendación de artículo de IA

Para crear una recomendación de artículo:

1. Ve a **Análisis** > **Recomendación de elementos de IA**.
2. Selecciona **Crear predicción** > **Recomendación de elementos AI**.

También puedes elegir crear una recomendación directamente desde un catálogo individual. Selecciona tu catálogo en la página **Catálogos** y, a continuación, selecciona **Crear recomendación**.

### Paso 1: Añadir detalles de la recomendación

Dale a tu recomendación un nombre y una descripción opcional.

![Paso "Detalles de la recomendación" con los campos nombre y descripción.][1]

### Paso 2: Define tu recomendación {#recommendation-type}

Selecciona el tipo de recomendación. Todos los tipos de recomendación utilizan los datos de los últimos seis meses de interacción con el artículo (compra o evento personalizado). La interacción mencionada a continuación se refiere a un evento de compra o a un evento personalizado elegido en [el Paso 3](#step-3-select-the-interaction-to-drive-recommendations).

- **Los más populares:** Calcula hasta 30 elementos del catálogo con los que interactúan más a menudo todos los usuarios del espacio de trabajo, como los productos más comprados.
- **La más reciente:** Crea una lista de hasta 30 productos con los que un usuario ha interactuado más recientemente.
- **AI Personalización:** Utiliza transformadores, un nuevo tipo de aprendizaje profundo, para predecir el siguiente conjunto de elementos con los que es más probable que interactúe cada usuario. Calculamos hasta 30 de los siguientes elementos más probables ordenados de mayor a menor probabilidad. Este tipo de recomendación no utiliza grandes modelos lingüísticos (LLM) para combinar tus datos con los de ningún otro cliente de Braze.
- **En tendencia:** Calcula hasta 30 elementos del espacio de trabajo que hayan tenido el impulso positivo más reciente en lo que respecta a las interacciones de los usuarios.

{% alert tip %}
Al utilizar **Más recientes** o **AI personalizada**, los usuarios con datos insuficientes para crear recomendaciones individualizadas recibirán los elementos **Más populares** como alternativa. La proporción de usuarios que reciben la alternativa **Más popular** se muestra en la página **de análisis**.
{% endalert %}

#### Paso 2a: Excluir compras o interacciones anteriores (opcional)

Para evitar sugerir artículos que un usuario ya haya comprado o con los que ya haya interactuado, selecciona **No recomendar artículos con los que los usuarios hayan interactuado previamente**. Esta opción sólo está disponible cuando el **Tipo de** recomendación está configurado como **AI Personalizado**.

![Paso "Define tu recomendación" con "Más populares" como tipo y la opción "No recomendar artículos con los que los usuarios hayan interactuado previamente" seleccionada.][2-3]

Esta configuración impide que la mensajería reutilice los artículos que un usuario ya ha comprado o con los que ya ha interactuado, siempre que la recomendación se haya actualizado recientemente. Los artículos comprados o con los que se haya interactuado entre las actualizaciones de las recomendaciones pueden seguir apareciendo. En la versión gratuita de las recomendaciones de artículos, las actualizaciones son semanales. Para la versión pro de las recomendaciones de elementos de IA, las actualizaciones se producen cada 24 horas.

Por ejemplo, al utilizar la versión pro de las recomendaciones de artículos de IA, si un usuario compra algo y luego recibe un correo electrónico de marketing en 30 minutos, es posible que el artículo que acaba de comprar no se excluya del correo electrónico a tiempo. Sin embargo, los mensajes enviados después de 24 horas no incluirán ese elemento.

#### Paso 2b: Seleccionar un catálogo

Si aún no está rellenado, selecciona el [catálogo][catálogo] del que esta recomendación extraerá artículos.

#### Paso 2c: Añade una selección (opcional)

Si quieres tener más control sobre tu recomendación, elige una [selección]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) para aplicar filtros personalizados. Las selecciones filtran las recomendaciones por columnas específicas de tu catálogo, como marca, tamaño o ubicación. Las selecciones que contienen Liquid no pueden utilizarse en tu recomendación.

![Un ejemplo de la selección "en stock" seleccionada para la recomendación.][2-2]

{% alert tip %}
Si no puedes encontrar tu selección, asegúrate de que esté configurada en tu catálogo.
{% endalert %}

### Paso 3: Selecciona la interacción para impulsar las recomendaciones

Selecciona el evento para el que quieres que se optimice esta recomendación. Este evento suele ser una compra, pero también puede ser cualquier interacción con un artículo.

Puedes optimizar para:

- Eventos de compra con el [Objeto de Compra]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Eventos personalizados que representan una compra
- Eventos personalizados que representen cualquier otra interacción con elementos (como vistas de productos, clics o reproducciones multimedia)

Si eliges **Evento personalizado**, selecciona tu evento de la lista.

![El evento personalizado "Compra finalizada" seleccionado es la forma en que se realiza actualmente el seguimiento de los eventos.][3]

### Paso 4: Elige el nombre de la propiedad correspondiente {#property-name}

Para crear una recomendación, tienes que decirle a Braze qué campo de tu evento de interacción (objeto de compra o evento personalizado) tiene el identificador único que coincide con el campo `id` de un artículo en el catálogo. ¿No estás seguro? [Ver requisitos](#requirements).

Selecciona este campo para el **Nombre de la propiedad**.

El campo **Nombre de propiedad** se rellenará previamente con una lista de campos enviados a través del SDK a Braze. Si se proporcionan datos suficientes, estas propiedades también se clasificarán por orden de probabilidad de ser la propiedad correcta. Selecciona la que corresponda al campo `id` del catálogo.

![El nombre de la propiedad "purchase_item" seleccionada que corresponde a los ID de artículo del catálogo.][4]

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
{% tab Evento personalizado %}

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

Si tus propiedades del evento contienen varios productos en una matriz, cada ID de producto se tratará como un evento independiente y secuencial. Este evento puede utilizar la propiedad `products.sku` para que coincida con el primer y el tercer elemento del catálogo de muestras.

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
{% tab Objeto de compra %}

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

Este evento tiene una propiedad `"sku": "ADI-RD-8"`, que está mapeada en el segundo elemento del catálogo.

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

### Paso 5: Entrena la recomendación

Cuando estés listo, selecciona **Crear recomendación**. Este proceso puede durar entre 10 minutos y 36 horas. Recibirás una actualización por correo electrónico cuando la recomendación se haya formado correctamente o una explicación de por qué puede haber fallado la creación.

Puedes encontrar la recomendación en la página **Predicciones**, donde luego puedes editarla o archivarla según necesites. Las recomendaciones se reciclarán automáticamente una vez al mes.

## Análisis

Puedes consultar los análisis de tu recomendación para ver qué artículos se recomendaron a los usuarios y la precisión del modelo de recomendación.

1. Ve a **Análisis** > **Recomendación de artículos**.
2. Selecciona tu recomendación de la lista.

En la parte superior de la página, puedes encontrar estadísticas sobre tu recomendación, como la precisión y la cobertura.

![Métricas de audiencia de las recomendaciones que muestran la precisión (21,1%), la cobertura (83,0%) y los tipos de recomendación divididos entre artículos personalizados y más populares.][5]

Estas métricas se definen en la tabla siguiente. 

| Métrica              | Descripción |
| ------------------- | ---------- |
| Precisión           | El porcentaje de veces que el modelo adivinó correctamente el siguiente artículo que compró un usuario. La precisión depende en gran medida del tamaño y la mezcla específicos de tu catálogo, y debe utilizarse como guía para comprender con qué frecuencia el modelo es correcto.<br><br>En pruebas anteriores, hemos visto que los modelos rinden bien con cifras de precisión que oscilan entre el 6 y el 20%. Esta métrica se actualiza cuando el modelo vuelve a entrenarse.  |
| Cobertura            | Qué porcentaje de artículos disponibles en el catálogo se recomiendan al menos a un usuario. Puedes esperar ver una mayor cobertura de artículos con recomendaciones de artículos personalizados sobre los más populares. |
| Tipo de recomendación | Porcentaje de usuarios que recibirán recomendaciones personalizadas o más recientes frente a la alternativa de los artículos más populares. La alternativa se envía a los usuarios que no tienen datos suficientes para generar una recomendación personalizada o más reciente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La siguiente sección muestra un desglose de los elementos del catálogo, dividido en dos columnas posibles:

- **Artículos personalizados** o **Artículos más recientes:** Esta columna enumera cada artículo del catálogo en orden descendente de los más recomendados a los usuarios. Esta columna también muestra a cuántos usuarios asignó el modelo cada elemento.
- **Artículos más populares:** Esta columna enumera cada artículo del catálogo en orden descendente de popularidad. La popularidad aquí se refiere a los elementos del catálogo con los que los usuarios interactúan más a menudo en todo el espacio de trabajo. El más popular se utiliza como alternativa cuando no se puede calcular el personalizado o el más reciente para un usuario individual.

![Tablas contiguas que enumeran los elementos asignados a los usuarios, separados por recomendaciones personalizadas y recomendaciones más populares.][6]

El **resumen de recomendaciones** muestra un resumen de la configuración de recomendaciones elegida, incluyendo cuándo se actualizó la recomendación por última vez.

![Tabla resumen de recomendaciones que muestra el tipo, el catálogo, el tipo de evento, el nombre del evento personalizado, el nombre de la propiedad y la última fecha de actualización.][7]{: style="max-width:45%" }

## Utilizar recomendaciones en mensajería

![Modalidad "Añadir personalización" con la recomendación de artículos como tipo de personalización.][10]{: style="max-width:30%;float:right;margin-left:15px;"}

Después de que tu recomendación termine de formarse, puedes personalizar tus mensajes con Liquid para insertar los productos más populares de ese catálogo. El Liquid puede ser generado para ti por la ventana de personalización que se encuentra en los creadores de mensajes:

1. En cualquier creador de mensajes que admita la personalización, selecciona <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> para abrir la ventana de personalización.
2. En **Tipo de personalización**, selecciona **Recomendación de artículos**.
3. En **Nombre de la** recomendación, selecciona la recomendación que acabas de crear.
4. En **Número de artículos predichos**, introduce cuántos productos principales quieres que se inserten. Por ejemplo, puedes mostrar los tres artículos más comprados.
5. En **Información a mostrar**, selecciona qué campos del catálogo deben incluirse para cada artículo. Los valores de estos campos para cada artículo se extraerán del catálogo asociado a esta recomendación.
6. Selecciona el icono **Copiar** y pega el Liquid donde sea necesario en tu mensaje.

## Niveles de recomendación de elementos de IA

En la tabla siguiente se describen las diferencias entre la versión gratuita y la pro de los tipos de recomendación AI Personalizada, Popular y Tendencias:

| Área                   | Versión gratuita                          | Versión Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Frecuencia de actualización de <sup>usuarios1</sup>   | Semanalmente                                | Diariamente                                    |
| Frecuencia de reentrenamiento del modelo  | Mensualmente                               | Mensualmente                                   |
| Modelos de recomendación máxima | 1 modelo por <sup>tipo2</sup> | 100 modelos por <sup>tipo2</sup> |

<sup>1\. Es la frecuencia con la que se actualizan las recomendaciones de artículos específicas del usuario (todos los modelos excepto Artículos más populares, que se actualiza cuando el modelo se vuelve a entrenar). Por ejemplo, si un usuario compra un artículo recomendado basándose en las recomendaciones de artículos de la IA, sus artículos recomendados se actualizarán según esta frecuencia</sup><br>
<sup>2\. Los tipos de recomendación disponibles son AI Personalizada, Más reciente, Más popular y Tendencias.</sup>

## Preguntas más frecuentes

### ¿Qué hace que los artículos "Más populares" se mezclen con las recomendaciones de otros modelos?

Cuando nuestra herramienta de recomendaciones selecciona una lista para ti, primero da prioridad a las selecciones personalizadas basadas en el modelo específico que has elegido, como "Más reciente" o "Personalizado con IA". Si este modelo no puede llenar la lista completa de 30 recomendaciones por cualquier motivo, se añaden entonces algunos de tus artículos más populares entre todos los usuarios, para asegurarte de que cada usuario tenga siempre un conjunto completo de recomendaciones.

Esto ocurre en algunas condiciones específicas:

- El modelo encuentra menos de 30 artículos que coinciden con tus criterios.
- Los artículos relevantes ya no están disponibles o en stock.
- Los artículos no cumplen los criterios de selección actuales, quizás debido a un cambio en las existencias o a las preferencias del usuario.

### ¿Las recomendaciones existentes se entrenan semanalmente después de actualizar a Recomendaciones de Artículos Pro?

Sí, pero sólo después de su próxima actualización programada. Las recomendaciones existentes no cambian a entrenamiento semanal y predicción diaria inmediatamente después de actualizar a Recomendaciones de artículos Pro. Sin embargo, adoptarán el nuevo horario automáticamente en su próximo ciclo de reciclaje. Por ejemplo, si una recomendación se entrenó por última vez el 1 de febrero y está configurada para volver a entrenarse cada 30 días, adoptará el nuevo programa semanal tras su próxima actualización el 2 de marzo.

[1]: {% image_buster /assets/img/item_recs_1.png %}
[2-1]: {% image_buster /assets/img/item_recs_2-1.png %}
[2-2]: {% image_buster /assets/img/item_recs_2-2.png %}
[2-3]: {% image_buster /assets/img/item_recs_2-3.png %}
[3]: {% image_buster /assets/img/item_recs_3.png %}
[4]: {% image_buster /assets/img/item_recs_4.png %}
[5]: {% image_buster /assets/img/item_recs_analytics_1.png %}
[6]: {% image_buster /assets/img/item_recs_analytics_2.png %}
[7]: {% image_buster /assets/img/item_recs_analytics_3.png %}
[10]: {% image_buster /assets/img/add_personalization.png %}
[catálogo]: {{site.baseurl}}/user_guide/personalización_y_contenido_dinámico/catálogos/
