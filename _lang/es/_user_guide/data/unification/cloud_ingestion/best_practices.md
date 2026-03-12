---
nav_title: Buenas prácticas
article_title: Prácticas recomendadas para la ingesta de datos en la nube
toc_headers: h2
page_order: 0
page_type: reference
description: "Esta página ofrece un resumen de la ingesta de datos en la nube, las mejores prácticas y las limitaciones del producto."

---

# Buenas prácticas

> Braze Cloud Data Ingestion le permite configurar una conexión directa desde su almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos. Al sincronizar estos datos con Braze, puedes aprovecharlos para casos de uso como la personalización, el desencadenamiento o la segmentación. 

## Comprender la`UPDATED_AT`  columna

{% alert note %}
`UPDATED_AT` Es relevante solo para integraciones de almacenes de datos, no para sincronizaciones S3.
{% endalert %}

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y actualiza los datos correspondientes en tu panel Braze. Cada vez que se ejecuta la sincronización, Braze refleja cualquier dato actualizado.

{% alert important %}
Braze CDI sincronizará las filas basándose estrictamente en el`UPDATED_AT`valor, independientemente de si el contenido de la fila es el mismo que el que hay actualmente en Braze. Teniendo esto en cuenta, recomendamos utilizar`UPDATED_AT`  correctamente para sincronizar solo los datos nuevos o actualizados y evitar así el uso innecesario de puntos de datos.
{% endalert %}

### Ejemplo: Sincronización recurrente

Para ilustrar cómo`UPDATED_AT`se utiliza  en una sincronización CDI, considera este ejemplo de sincronización periódica para actualizar los atributos de usuario:

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

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Lo comprobamos utilizando la columna `UPDATED_AT` de su tabla o vista. Braze selecciona e importa todas las filas en las que`UPDATED_AT`  es igual o posterior a la última`UPDATED_AT`marca de tiempo de la última tarea de sincronización realizada con éxito.

En tu almacén de datos, añade los siguientes usuarios y atributos a tu tabla, ajustando la hora `UPDATED_AT` a la hora en que añadas estos datos:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>DESCARGA</th>
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

Durante la siguiente sincronización programada, Braze sincroniza todas las filas con una`UPDATED_AT`marca de tiempo igual o posterior a la marca de tiempo más reciente en los perfiles de usuario. Braze actualiza o añade campos, por lo que no es necesario sincronizar el perfil completo de usuario cada vez. Tras la sincronización, los perfiles de usuario reflejan las nuevas actualizaciones:

**Sincronización periódica, segunda ejecución el 20 de julio de 2022 a las 12 p. m.**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>DESCARGA</th>
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

Se ha añadido una fila, pero el`UPDATED_AT`valor es anterior al`2022-07-19 09:07:23`(almacenado desde la primera ejecución). Como resultado, ninguna de estas filas se sincronizará en esta ejecución. El último`UPDATED_AT`  para la sincronización no se ve afectado por esta ejecución y permanece como  `2022-07-19 09:07:23`.

**Sincronización periódica, tercera ejecución el 21 de julio de 2022 a las 12 p. m.**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>DESCARGA</th>
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

En esta tercera tanda, se añadió otra fila nueva. Ahora, una fila tiene un`UPDATED_AT`valor posterior a `2022-07-19 09:07:23`, lo que significa que solo se sincronizará una fila. El último  ahora`UPDATED_AT` está configurado como `2022-07-21 08:30:00`.

{% alert note %}
`UPDATED_AT` Los valores pueden ser incluso posteriores a la hora de inicio de la ejecución para una sincronización determinada. Sin embargo, esto no es recomendable, ya que pusha la última`UPDATED_AT`marca de tiempo «hacia el futuro» y las sincronizaciones posteriores no sincronizarán los valores anteriores.
{% endalert %}

## Utiliza una fecha y hora UTC para la columna `UPDATED_AT` 

La columna `UPDATED_AT` debe estar en UTC para evitar problemas con el horario de verano. Prefiere funciones solo UTC, como `SYSDATE()` en lugar de `CURRENT_DATE()` siempre que sea posible.

## Asegúrate de que`UPDATED_AT`la hora no sea la misma que la de tu sincronización.

Tu sincronización CDI podría tener datos duplicados si alguno`UPDATED_AT`de los campos tiene exactamente la misma hora que la última`UPDATED_AT`marca de tiempo del último trabajo de sincronización realizado con éxito. Esto se debe a que CDI elegirá un «límite inclusivo» cuando identifique cualquier fila que coincida con la sincronización anterior y hará que las filas se puedan sincronizar. CDI volverá a importar esas filas y creará datos duplicados.

A continuación, se incluyen algunas sugerencias para evitar la duplicación de datos:

- Si estás configurando una sincronización con un `VIEW`, no utilices`CURRENT_TIMESTAMP`  como valor predeterminado. Esto hará que todos los datos se sincronicen cada vez que se ejecute la sincronización porque el campo `UPDATED_AT` se evaluará a la hora en que se ejecuten nuestras consultas.
- Si tiene procesos o consultas de muy larga duración que escriben datos en la tabla de origen, evite ejecutarlos simultáneamente con una sincronización, o evite utilizar la misma marca de tiempo para cada fila insertada.
- Utilice una transacción para escribir todas las filas que tengan la misma marca de tiempo.

### Ejemplo: Administración de actualizaciones posteriores

Este ejemplo muestra el proceso general para sincronizar datos por primera vez y, a continuación, sólo actualizar los datos cambiantes (deltas) en las actualizaciones posteriores. Supongamos que tenemos una tabla `EXAMPLE_DATA` con algunos datos de usuario. El día 1 tiene los siguientes valores:

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
            <td>azul</td>
            <td>380</td>
            <td>FALSO</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>azul</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>azul</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>rojo</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>rojo</td>
            <td>813</td>
            <td>FALSO</td>
        </tr>
    </tbody>
</table>

Para obtener estos datos en el formato que espera CDI, puede ejecutar la siguiente consulta:

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
      <th>DESCARGA</th>
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
            <td style="background-color: #FFFF00;">rojo</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>azul</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>azul</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSO</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">verde</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>rojo</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSO</td>
        </tr>
    </tbody>
</table>

Ahora tienes que añadir solo los valores modificados en la tabla fuente CDI. Estas filas pueden añadirse en lugar de actualizar las filas antiguas. Esa tabla tiene ahora este aspecto:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>DESCARGA</th>
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

CDI sólo sincronizará las nuevas filas, por lo que la próxima sincronización que se ejecute sólo sincronizará las últimas cinco filas.

## Consejos adicionales

### Escribir sólo atributos nuevos o actualizados para minimizar el consumo

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Lo comprobamos utilizando la columna `UPDATED_AT` de su tabla o vista. Braze selecciona e importa todas las filas en las que`UPDATED_AT`  es igual o posterior a la última`UPDATED_AT`marca de tiempo del último trabajo de sincronización realizado con éxito, independientemente de si son iguales a las que se encuentran actualmente en el perfil de usuario. Por ello, recomendamos sincronizar únicamente los atributos que desee añadir o actualizar.

El uso de puntos de datos es idéntico con CDI y con otros métodos de ingestión, como las API REST o los SDK, por lo que depende de ti asegurarte de que solo añades atributos nuevos o actualizados a tus tablas de origen.

### Separa `EXTERNAL_ID` de la columna `PAYLOAD` 

El objeto `PAYLOAD` no debe incluir un ID externo u otro tipo de ID. 

### Eliminar un atributo

Puedes establecerlo en `null` si quieres omitir un atributo del perfil de un usuario. Si quieres que un atributo no se modifique, no lo envíes a Braze hasta que se haya actualizado. Para eliminar completamente un atributo, utiliza `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Haz actualizaciones incrementales

Realiza actualizaciones incrementales de tus datos para evitar sobrescrituras involuntarias cuando se realicen actualizaciones simultáneas.

{% alert important %}
* **Actualizaciones de diferentes atributos:** En la gran mayoría de los casos, si dos actualizaciones no afectan a los mismos atributos de un usuario, sus resultados son totalmente independientes. Por ejemplo, si actualizas el `Color`atributo  de un usuario y actualizas por separado su`Size`atributo , ambas actualizaciones deben aplicarse correctamente, incluso si se producen con unos segundos de diferencia.
* **Actualizaciones del mismo atributo:** Las condiciones de carrera pueden producirse cuando varias actualizaciones apuntan al mismo atributo dentro de una sola ejecución de sincronización. En estos casos excepcionales, una actualización puede sobrescribir otra. La mejor manera de evitar este comportamiento es asegurarse de que los datos de origen para la sincronización de CDI reflejen solo el estado más reciente de cada usuario, o que todas las actualizaciones para un usuario determinado o una combinación de usuario + atributo estén contenidas en una sola fila.
* **Operadores de matriz de objetos:** Las únicas excepciones a las actualizaciones independientes son los operadores `$add`,`$remove`  `$update`y  para matrices de objetos, donde las actualizaciones de la misma matriz pueden interactuar entre sí.
* **Eventos:** Las condiciones de carrera no afectan a los eventos porque cada evento es único y tiene una marca de tiempo asociada.
{% endalert %}

La mejor manera de evitar este comportamiento es asegurarse de que los datos de origen para la sincronización de CDI reflejen solo el estado más reciente de cada usuario, o que todas las actualizaciones para un usuario determinado o una combinación de usuario + atributo estén contenidas en una sola fila.

### Crear una cadena JSON a partir de otra tabla

Si prefiere almacenar internamente cada atributo en su propia columna, deberá convertir esas columnas en una cadena JSON para rellenar la sincronización con Braze. Para ello, puede utilizar una consulta del tipo:

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

Utilizamos la marca de tiempo `UPDATED_AT` para realizar un seguimiento de los datos que se han sincronizado correctamente con Braze. Si se escriben muchas filas con la misma marca de tiempo mientras se está ejecutando una sincronización, esto puede provocar que se sincronicen datos duplicados con Braze. Algunas sugerencias para evitar la duplicación de datos:
- Si estás configurando una sincronización con un `VIEW`, no utilices `CURRENT_TIMESTAMP` como valor predeterminado. Esto hará que todos los datos se sincronicen cada vez que se ejecute la sincronización porque el campo `UPDATED_AT` se evaluará a la hora en que se ejecuten nuestras consultas. 
- Si tiene procesos o consultas de muy larga duración que escriben datos en la tabla de origen, evite ejecutarlos simultáneamente con una sincronización, o evite utilizar la misma marca de tiempo para cada fila insertada.
- Utilice una transacción para escribir todas las filas que tengan la misma marca de tiempo.

### Configuración de la tabla

Disponemos de un [repositorio público en GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) para que los clientes compartan las mejores prácticas o fragmentos de código. Para contribuir con tus propios fragmentos de código, ¡crea un pull request!

### Formato de los datos

Cualquier operación que sea posible a través del punto final Braze `/users/track` se admite a través de la Ingesta de datos en la nube, incluida la actualización de atributos personalizados anidados, la adición del estado de suscripción y la sincronización de eventos personalizados o compras. 

Los campos de la carga útil deben seguir el mismo formato que el punto final correspondiente de `/users/track`. A continuación se detallan los requisitos de formato:

| Tipo de datos | Especificaciones de formato |
| --------- | ---------| --------- | ----------- |
| `attributes` | Ver [objeto atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Tenga en cuenta el requisito especial para [capturar fechas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) en atributos anidados. 

{% tabs local %}
{% tab Nested Custom Attributes %}
Puede incluir atributos personalizados anidados en la columna de carga útil para una sincronización de atributos personalizados. 

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
Para sincronizar eventos, se requiere un nombre de evento. Formatea el`time`campo como una cadena ISO 8601 o en`yyyy-MM-dd'T'HH:mm:ss:SSSZ`formato . Si el`time`campo no está presente, Braze utiliza el valor`UPDATED_AT` de la columna como hora del evento. Otros campos como `app_id` y `properties` son opcionales. 

Nota: solo puedes sincronizar un evento por fila.

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
Para sincronizar los eventos de compra,`product_id` se `price`requiere ,`currency` , y . Formatea el`time`campo, que es opcional, como una cadena ISO 8601 o en`yyyy-MM-dd'T'HH:mm:ss:SSSZ`formato . Si el`time`campo no está presente, Braze utiliza el valor`UPDATED_AT` de la columna como hora del evento. Otros campos, como `app_id`, `quantity` y `properties` son opcionales.

Nota: solo puedes sincronizar un evento de compra por fila.

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

### Evita los tiempos de espera en las consultas del almacén de datos.

Recomendamos que las consultas se realicen en el plazo de una hora para obtener un rendimiento óptimo y evitar posibles errores. Si las consultas superan este plazo, considere la posibilidad de revisar la configuración de su almacén de datos. La optimización de los recursos asignados a su almacén puede ayudar a mejorar la velocidad de ejecución de las consultas.

## Limitaciones del producto

| Limitación            | Descripción                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integraciones | No hay límite en el número de integraciones que puedes configurar. Sin embargo, sólo podrá configurar una integración por tabla o vista.                                             |
| Cantidad de filas         | De forma predeterminada, cada ejecución puede sincronizar hasta 500 millones de filas. Braze detiene cualquier sincronización con más de 500 millones de filas nuevas. Si necesitas un límite superior a este, ponte en contacto con tu administrador del éxito del cliente de Braze o con el soporte de Braze. |
| Atributos por fila     | Cada fila debe contener un único ID de usuario y un objeto JSON con un máximo de 250 atributos. Cada clave del objeto JSON cuenta como un atributo (es decir, un array cuenta como un atributo). |
| Tamaño de la carga útil           | Cada fila puede contener una carga útil de hasta 1 MB. Braze rechaza cargas útiles superiores a 1 MB y registra el error «La carga útil era superior a 1 MB» en el registro de sincronización, junto con el ID externo asociado y la carga útil truncada. |
| Tipo de datos              | Puedes sincronizar atributos de usuario, eventos y compras a través de la ingesta de datos en la nube.                                                                                                  |
| Región de Braze           | Este producto está disponible en todas las regiones Braze. Cualquier región Braze puede conectarse a cualquier región de datos de origen.                                                                              |
| Región de origen       | Braze se conectará a su almacén de datos o entorno de nube en cualquier región o proveedor de nube.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
