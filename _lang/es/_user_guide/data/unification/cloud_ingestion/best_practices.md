---
nav_title: Buenas prácticas
article_title: Prácticas recomendadas para la ingesta de datos en la nube
toc_headers: h2
page_order: 0
page_type: reference
description: "Esta página ofrece un resumen de la ingesta de datos en la nube, las mejores prácticas y las limitaciones del producto."

---

# Buenas prácticas

> Braze Cloud Data Ingestion te permite configurar una conexión directa desde tu almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos. Al sincronizar estos datos con Braze, puedes aprovecharlos para casos de uso como la personalización, el desencadenamiento o la segmentación. 

## Comprender la columna `UPDATED_AT`

{% alert note %}
`UPDATED_AT` es relevante solo para integraciones de almacenes de datos, no para sincronizaciones S3.
{% endalert %}

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y actualiza los datos correspondientes en tu panel de Braze. Cada vez que se ejecuta la sincronización, Braze refleja cualquier dato actualizado.

{% alert important %}
Braze CDI sincronizará las filas basándose estrictamente en el valor de `UPDATED_AT`, independientemente de si el contenido de la fila es el mismo que el que hay actualmente en Braze. Teniendo esto en cuenta, recomendamos utilizar `UPDATED_AT` correctamente para sincronizar solo los datos nuevos o actualizados y evitar así el Uso de puntos de datos innecesario.
{% endalert %}

### Ejemplo: sincronización recurrente

Para ilustrar cómo se utiliza `UPDATED_AT` en una sincronización CDI, considera este ejemplo de sincronización periódica para actualizar los atributos de usuario:

- Fuentes de almacenamiento de archivos 
   - Amazon S3

## Tipos de datos admitidos 

La ingesta de datos en la nube admite los siguientes tipos de datos: 
- Atributos de usuario, incluyendo:
   - Atributos personalizados anidados
   - Matrices de objetos
   - Estados de suscripción
- Eventos personalizados
- Eventos de compra
- Artículos del catálogo
- Solicitudes de eliminación de usuarios

Puedes actualizar los datos de usuario mediante el ID externo, el alias de usuario, el ID de Braze, el correo electrónico o el número de teléfono. Puedes eliminar usuarios por ID externo, alias de usuario o ID de Braze. 

## Qué se sincroniza

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Lo comprobamos utilizando la columna `UPDATED_AT` de tu tabla o vista. Braze selecciona e importa todas las filas en las que `UPDATED_AT` es posterior al último valor de `UPDATED_AT` sincronizado. Las filas que se encuentran exactamente en la marca de tiempo límite también pueden volver a sincronizarse si se añaden nuevas filas con esa misma marca de tiempo entre ejecuciones.

{% alert important %}
CDI registra el número de filas en el último valor de `UPDATED_AT` sincronizado. Si se añaden nuevas filas con esa misma marca de tiempo entre ejecuciones, CDI cambia a un límite inclusivo (`>=`) y vuelve a sincronizar todas las filas con esa marca de tiempo, incluidas las ya procesadas. Para evitar sincronizaciones duplicadas y el consumo innecesario de puntos de datos, utiliza valores de `UPDATED_AT` únicos entre ejecuciones de sincronización. Para más información, consulta [Evitar la resincronización de filas con marcas de tiempo duplicadas](#avoid-resyncing-rows-with-duplicate-timestamps).
{% endalert %}

En tu almacén de datos, añade los siguientes usuarios y atributos a tu tabla, ajustando la hora de `UPDATED_AT` a la hora en que añadas estos datos:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Durante la siguiente sincronización programada, Braze sincroniza todas las filas con una marca de tiempo de `UPDATED_AT` posterior a la marca de tiempo sincronizada más reciente. Braze actualiza o añade campos, por lo que no es necesario sincronizar el perfil de usuario completo cada vez. Tras la sincronización, los perfiles de usuario reflejan las nuevas actualizaciones:

**Sincronización periódica, segunda ejecución el 20 de julio de 2022 a las 12 p. m.**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Se añadió una nueva fila para `customer_9012`, pero su valor de `UPDATED_AT` (`2022-07-16 00:25:30`) es anterior a la marca de tiempo almacenada (`2022-07-19 09:07:23`), por lo que no se sincronizará. Sin embargo, la fila existente de `customer_5678` tiene un valor de `UPDATED_AT` igual a la marca de tiempo almacenada, por lo que se vuelve a sincronizar debido al límite inclusivo. Para más detalles sobre este comportamiento, consulta [Asegúrate de que la hora de UPDATED_AT no sea la misma que la de tu sincronización](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync). El `UPDATED_AT` almacenado permanece como `2022-07-19 09:07:23`.

**Sincronización periódica, tercera ejecución el 21 de julio de 2022 a las 12 p. m.**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

En esta tercera ejecución, se añadió otra fila nueva para `customer_1234` con un valor de `UPDATED_AT` (`2022-07-21 08:30:00`) posterior a la marca de tiempo almacenada. Esta nueva fila y la fila existente de `customer_5678` (que tiene un `UPDATED_AT` igual a la marca de tiempo almacenada) se sincronizan ambas. El `UPDATED_AT` almacenado ahora se establece como `2022-07-21 08:30:00`.

{% alert note %}
Los valores de `UPDATED_AT` pueden ser incluso posteriores a la hora de inicio de la ejecución para una sincronización determinada. Sin embargo, esto no es recomendable, ya que empuja la última marca de tiempo de `UPDATED_AT` «hacia el futuro» y las sincronizaciones posteriores no sincronizarán los valores anteriores.
{% endalert %}

## Utiliza una marca de tiempo UTC para la columna `UPDATED_AT`

La columna `UPDATED_AT` debe estar en UTC para evitar problemas con el horario de verano. Prefiere funciones solo UTC, como `SYSDATE()` en lugar de `CURRENT_DATE()` siempre que sea posible.

## Evitar la resincronización de filas con marcas de tiempo duplicadas {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI registra el número de filas en la última marca de tiempo de `UPDATED_AT` sincronizada. Si CDI detecta que se han añadido nuevas filas con esa misma marca de tiempo desde la última ejecución, utiliza un límite inclusivo (`>=`) para volver a seleccionar todas las filas con esa marca de tiempo, incluidas las ya procesadas. De lo contrario, CDI utiliza un límite exclusivo (`>`) y solo selecciona filas estrictamente posteriores al último valor sincronizado.

Por ejemplo, si una sincronización procesa cinco filas con `UPDATED_AT = 2025-04-01 00:00:00`, y posteriormente se añade una sexta fila con la misma marca de tiempo, la siguiente sincronización detecta el cambio en el recuento y vuelve a sincronizar las seis filas. Esto puede resultar en datos duplicados y consumo innecesario de puntos de datos.

Para evitar esto:

- Si estás configurando una sincronización contra un `VIEW`, no utilices `CURRENT_TIMESTAMP` como valor predeterminado. Esto hace que todos los datos se sincronicen cada vez que se ejecuta la sincronización, porque el campo `UPDATED_AT` se evalúa a la hora en que se ejecuta la consulta.
- Si tienes pipelines o consultas de larga duración que escriben datos en tu tabla de origen, evita ejecutarlos simultáneamente con una sincronización, o evita utilizar la misma marca de tiempo para cada fila insertada.
- Utiliza una transacción para escribir todas las filas que compartan la misma marca de tiempo.
- Utiliza valores de `UPDATED_AT` únicos y monótonamente crecientes para evitar que las filas se vuelvan a seleccionar después de haber sido procesadas.

### Ejemplo: administración de actualizaciones posteriores

Este ejemplo muestra el proceso general para sincronizar datos por primera vez y luego solo actualizar los datos cambiantes (deltas) en las actualizaciones posteriores. Supongamos que tenemos una tabla `EXAMPLE_DATA` con algunos datos de usuario. El día 1 tiene los siguientes valores:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Para obtener estos datos en el formato que espera CDI, puedes ejecutar la siguiente consulta:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Nada de esto se ha sincronizado antes con Braze, así que añádelo todo a la tabla de origen para CDI:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

Se ejecuta una sincronización y Braze registra que has sincronizado todos los datos disponibles hasta "2023-03-16 15:00:00". A continuación, en la mañana del día 2, se ejecuta un ETL y se actualizan algunos campos de la tabla de usuarios (resaltados):

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">red</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Ahora solo necesitas añadir los valores modificados a la tabla de origen de CDI. Estas filas pueden añadirse en lugar de actualizar las filas antiguas. Esa tabla ahora tiene este aspecto:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI solo sincronizará las nuevas filas, por lo que la próxima sincronización que se ejecute solo sincronizará las últimas cinco filas.

## Consejos adicionales

### Escribe solo atributos nuevos o actualizados para minimizar el consumo

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Lo comprobamos utilizando la columna `UPDATED_AT` de tu tabla o vista. Braze selecciona e importa todas las filas en las que `UPDATED_AT` es posterior al último valor de `UPDATED_AT` sincronizado, independientemente de si son iguales a las que se encuentran actualmente en el perfil de usuario. Las filas en la marca de tiempo límite también pueden volver a sincronizarse si nuevas filas comparten esa marca de tiempo. Por ello, recomendamos sincronizar únicamente los atributos que desees añadir o actualizar.

El Uso de puntos de datos es idéntico con CDI y con otros métodos de ingesta, como las API REST o los SDK, por lo que depende de ti asegurarte de que solo añades atributos nuevos o actualizados a tus tablas de origen.

### Separa `EXTERNAL_ID` de la columna `PAYLOAD`

El objeto `PAYLOAD` no debe incluir un ID externo u otro tipo de ID. 

### Eliminar un atributo

Puedes establecerlo en `null` si quieres omitir un atributo del perfil de un usuario. Si quieres que un atributo no se modifique, no lo envíes a Braze hasta que se haya actualizado. Para eliminar completamente un atributo, utiliza `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Haz actualizaciones incrementales

Realiza actualizaciones incrementales de tus datos para evitar sobrescrituras involuntarias cuando se realicen actualizaciones simultáneas.

{% alert important %}
* **Actualizaciones de diferentes atributos:** En la gran mayoría de los casos, si dos actualizaciones no afectan a los mismos atributos de un usuario, sus resultados son totalmente independientes. Por ejemplo, si actualizas el atributo `Color` de un usuario y actualizas por separado su atributo `Size`, ambas actualizaciones deben aplicarse correctamente, incluso si se producen con unos segundos de diferencia.
* **Actualizaciones del mismo atributo:** Las condiciones de carrera pueden producirse cuando varias actualizaciones apuntan al mismo atributo dentro de una sola ejecución de sincronización. En estos casos excepcionales, una actualización puede sobrescribir otra. La mejor manera de evitar este comportamiento es asegurarte de que los datos de origen para la sincronización de CDI reflejen solo el estado más reciente de cada usuario, o que todas las actualizaciones para un usuario determinado o una combinación de usuario + atributo estén contenidas en una sola fila.
* **Operadores de matriz de objetos:** Las únicas excepciones a las actualizaciones independientes son los operadores `$add`, `$remove` y `$update` para matrices de objetos, donde las actualizaciones de la misma matriz pueden interactuar entre sí.
* **Eventos:** Las condiciones de carrera no afectan a los eventos porque cada evento es único y tiene una marca de tiempo asociada.
{% endalert %}

La mejor manera de evitar este comportamiento es asegurarte de que los datos de origen para la sincronización de CDI reflejen solo el estado más reciente de cada usuario, o que todas las actualizaciones para un usuario determinado o una combinación de usuario + atributo estén contenidas en una sola fila.

### Crear una cadena JSON a partir de otra tabla

Si prefieres almacenar internamente cada atributo en su propia columna, necesitas convertir esas columnas en una cadena JSON para rellenar la sincronización con Braze. Para ello, puedes utilizar una consulta como:

{% tabs local %}
{% tab Snowflake %}
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Utiliza la marca de tiempo `UPDATED_AT`

Braze utiliza la marca de tiempo `UPDATED_AT` para rastrear qué datos se han sincronizado correctamente. CDI también registra el número de filas en la última marca de tiempo sincronizada. Si se añaden nuevas filas con esa misma marca de tiempo entre ejecuciones, CDI vuelve a sincronizar todas las filas con esa marca de tiempo, lo que puede generar datos duplicados. Para más detalles y consejos, consulta [Evitar la resincronización de filas con marcas de tiempo duplicadas](#avoid-resyncing-rows-with-duplicate-timestamps).

### Configuración de la tabla

Disponemos de un [repositorio público en GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) para que los clientes compartan las mejores prácticas o fragmentos de código. Para contribuir con tus propios fragmentos de código, ¡crea un pull request!

### Formato de los datos

Cualquier operación que sea posible a través del punto de conexión `/users/track` de Braze se admite a través de la ingesta de datos en la nube, incluida la actualización de atributos personalizados anidados, la adición del estado de suscripción y la sincronización de eventos personalizados o compras. 

Los campos de la carga útil deben seguir el mismo formato que el punto de conexión correspondiente de `/users/track`. Para conocer los requisitos de formato detallados, consulta lo siguiente:

| Tipo de datos | Especificaciones de formato |
| --------- | ---------| --------- | ----------- |
| `attributes` | Ver [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Ten en cuenta el requisito especial para [capturar fechas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) en atributos anidados. 

{% tabs local %}
{% tab Nested Custom Attributes %}
Puedes incluir atributos personalizados anidados en la columna de carga útil para una sincronización de atributos personalizados. 

```json
{
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
```

{% endtab %}
{% tab Event %}
Para sincronizar eventos, se requiere un nombre de evento. Formatea el campo `time` como una cadena ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si el campo `time` no está presente, Braze utiliza el valor de la columna `UPDATED_AT` como hora del evento. Otros campos como `app_id` y `properties` son opcionales. 

Ten en cuenta que solo puedes sincronizar un evento por fila.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab Purchase %}
Para sincronizar eventos de compra, se requieren `product_id`, `currency` y `price`. Formatea el campo `time`, que es opcional, como una cadena ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si el campo `time` no está presente, Braze utiliza el valor de la columna `UPDATED_AT` como hora del evento. Otros campos, como `app_id`, `quantity` y `properties` son opcionales.

Ten en cuenta que solo puedes sincronizar un evento de compra por fila.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab Subscription Groups %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### Evita los tiempos de espera en las consultas del almacén de datos

Recomendamos que las consultas se completen en el plazo de una hora para obtener un rendimiento óptimo y evitar posibles errores. Si las consultas superan este plazo, considera revisar la configuración de tu almacén de datos. La optimización de los recursos asignados a tu almacén puede ayudar a mejorar la velocidad de ejecución de las consultas.

## Limitaciones del producto

| Limitación            | Descripción                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integraciones | No hay límite en el número de integraciones que puedes configurar. Sin embargo, solo podrás configurar una integración por tabla o vista.                                             |
| Cantidad de filas         | De forma predeterminada, cada ejecución puede sincronizar hasta 500 millones de filas. Braze detiene cualquier sincronización con más de 500 millones de filas nuevas. Si necesitas un límite superior, ponte en contacto con tu administrador del éxito del cliente de Braze o con soporte de Braze. |
| Atributos por fila     | Cada fila debe contener un único ID de usuario y un objeto JSON con un máximo de 250 atributos. Cada clave del objeto JSON cuenta como un atributo (es decir, un array cuenta como un atributo). |
| Tamaño de la carga útil           | Cada fila puede contener una carga útil de hasta 1 MB. Braze rechaza cargas útiles superiores a 1&nbsp;MB y registra el error «La carga útil era superior a 1 MB» en el registro de sincronización, junto con el ID externo asociado y la carga útil truncada. |
| Tipo de datos              | Puedes sincronizar atributos de usuario, eventos y compras a través de la ingesta de datos en la nube.                                                                                                  |
| Región de Braze           | Este producto está disponible en todas las regiones de Braze. Cualquier región de Braze puede conectarse a cualquier región de datos de origen.                                                                              |
| Región de origen       | Braze se conectará a tu almacén de datos o entorno en la nube en cualquier región o proveedor de nube.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>