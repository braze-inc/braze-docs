---
nav_title: Resumen
article_title: Visión general de la ingesta de datos en la nube 
page_order: 0
page_type: reference
description: "Esta página ofrece un resumen de la ingesta de datos en la nube, las mejores prácticas y las limitaciones del producto."

---

# Resumen de la ingesta de datos en la nube Braze

> La ingesta de datos en la nube Braze te permite configurar una conexión directa desde tu almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos. Cuando se sincronizan con Braze, estos datos pueden aprovecharse para casos de uso como la personalización, la desencadenación o la segmentación. 

## Cómo funciona

Con la ingesta de datos en la nube Braze (CDI), configuras una integración entre tu instancia de almacén de datos y el espacio de trabajo Braze para sincronizar datos de forma periódica. Esta sincronización se ejecuta según el calendario que tú establezcas, y cada integración puede tener un calendario diferente. Las sincronizaciones pueden ser tan frecuentes como cada 15 minutos o tan infrecuentes como una vez al mes. Si necesitas que las sincronizaciones se produzcan con una frecuencia superior a 15 minutos, ponte en contacto con tu administrador del éxito del cliente o considera la posibilidad de utilizar llamadas a la API REST para la ingesta de datos en tiempo real.

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y actualiza los datos correspondientes en tu panel Braze. Cada vez que se ejecute la sincronización, los datos actualizados se reflejarán en Braze.

## Orígenes de datos admitidos

La Ingesta de Datos en la Nube puede sincronizar datos de las siguientes fuentes con Braze:

- Orígenes de almacén de datos 
   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Tejido Microsoft
   - Snowflake

- Fuentes de almacenamiento de archivos 
   - Amazon S3

## Tipos de datos admitidos 

La Ingesta de Datos en la Nube admite los siguientes tipos de datos: 
- Atributos del usuario, incluidos:
   - Atributos personalizados anidados
   - Matrices de objetos
   - Estados de suscripción
- Eventos personalizados
- Eventos de compra
- Artículos del catálogo
- Solicitudes de eliminación de usuarios

Los datos de usuario pueden actualizarse mediante ID externo, alias de usuario, ID de Braze, correo electrónico o número de teléfono. Los usuarios pueden ser eliminados por ID externo, alias de usuario o ID de Braze. 

## Qué se sincroniza

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Lo comprobamos utilizando la columna `UPDATED_AT` de tu tabla o vista. Cualquier fila en la que `UPDATED_AT` sea igual o posterior a la última marca de tiempo `UPDATED_AT` del último trabajo de sincronización realizado con éxito se seleccionará y se introducirá en Braze.

En tu almacén de datos, añade los siguientes usuarios y atributos a tu tabla, ajustando la hora `UPDATED_AT` a la hora en que añadas estos datos:

| UPDATED_AT | EXTERNAL_ID | CARGA ÚTIL |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |

Durante la siguiente sincronización programada, todas las filas con una marca de tiempo `UPDATED_AT` igual o posterior a la marca de tiempo más reciente se sincronizarán con los perfiles de usuario de Braze. Los campos se actualizarán o añadirán, por lo que no tendrás que sincronizar el perfil de usuario completo cada vez. Tras la sincronización, los usuarios reflejarán las nuevas actualizaciones:

```json
{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":{
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_2"
    },
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Casos de uso: Primera sincronización y actualizaciones posteriores

Este ejemplo muestra el proceso general para sincronizar datos por primera vez, y luego sólo actualizar los datos cambiantes (deltas) en las actualizaciones posteriores. Supongamos que tenemos una tabla `EXAMPLE_DATA` con algunos datos de usuario. El día 1, tiene los siguientes valores:

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
            <td>VERDADERO</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>azul</td>
            <td>384</td>
            <td>VERDADERO</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>rojo</td>
            <td>349</td>
            <td>VERDADERO</td>
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

Para obtener estos datos en el formato que espera CDI, podrías ejecutar la siguiente consulta:

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

| UPDATED_AT          | EXTERNAL_ID | CARGA ÚTIL                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Se ejecuta una sincronización y Braze registra que has sincronizado todos los datos disponibles hasta "2023-03-16 15:00:00". Luego, en la mañana del día 2, tienes una ETL que se ejecuta y algunos campos de tu tabla de usuarios se actualizan (se resaltan):

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
            <td style="background-color: #FFFF00;">VERDADERO</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>azul</td>
            <td>823</td>
            <td>VERDADERO</td>
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
            <td>VERDADERO</td>
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

Ahora tienes que añadir sólo los valores modificados en la tabla fuente CDI. Estas filas se pueden añadir en lugar de actualizar las filas antiguas. Esa tabla tiene ahora este aspecto:

| UPDATED_AT          | EXTERNAL_ID | CARGA ÚTIL                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 12345       | { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} |
| 2023-03-17 09:30:00 | 23456       | { "ATTRIBUTE_1": "15"} |
| 2023-03-17 09:30:00 | 34567       | { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 45678       | { "ATTRIBUTE_2":"green"} |
| 2023-03-17 09:30:00 | 56789       | { "ATTRIBUTE_3":"693"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

CDI sólo sincronizará las nuevas filas, por lo que la siguiente sincronización que se ejecute sólo sincronizará las últimas cinco filas.

### Casos de uso: Actualizar un campo en una matriz de objetos existente

Este ejemplo muestra cómo actualizar un campo en una matriz de objetos existente. Supongamos que tenemos una tabla de origen con la siguiente definición:

```json 
Create table BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list (
    pet_id int IDENTITY(1,1), 
    breed VARCHAR, 
    type VARCHAR, 
    name VARCHAR, 
    owner_id VARCHAR, 
    age int
);
```

En este ejemplo, queremos añadir una matriz de mascotas propiedad de cada usuario, que corresponde a `owner_id`. Concretamente, queremos incluir la identificación, la raza, el tipo y el nombre. Podemos utilizar la siguiente consulta para rellenar una tabla o una vista:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$add', ARRAY_AGG( OBJECT_CONSTRUCT(
                'id',
                pet_id,
                'breed',
                breed,
                'type',
                type,
                'name',
                name
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID;
```

El resultado esperado sería el siguiente

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

A continuación, para enviar un campo de nombre actualizado y un nuevo campo de edad para cada propietario, podemos utilizar la siguiente consulta para rellenar una tabla o vista:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$update', ARRAY_AGG( OBJECT_CONSTRUCT(
                '$identifier_key','id',
                '$identifier_value',pet_id,
                '$new_object',OBJECT_CONSTRUCT(
                    'name',name,
                    'age',age
                )
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID; 
```

El resultado esperado sería el siguiente

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## Uso de punto de datos

La facturación del punto de datos para la Ingesta de Datos en la Nube es equivalente a la facturación de las actualizaciones a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Consulta [Puntos de datos]({{site.baseurl}}/user_guide/data/data_points/) para más información. 

{% alert important %}
La Ingesta de datos en la nube Braze cuenta para el límite de tasa disponible, por lo que si envías datos utilizando otro método, el límite de velocidad se combina entre la API Braze y la Ingesta de datos en la nube.
{% endalert %}

## Recomendaciones para la configuración de datos

### Escribe sólo atributos nuevos o actualizados para minimizar el consumo

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Lo comprobamos utilizando la columna `UPDATED_AT` de tu tabla o vista. Todas las filas en las que `UPDATED_AT` sea igual o posterior a la última marca de tiempo `UPDATED_AT` del último trabajo de sincronización realizado con éxito se seleccionarán y se introducirán en Braze, independientemente de si coinciden o no con lo que hay actualmente en el perfil de usuario. Por ello, te recomendamos que sólo sincronices los atributos que quieras añadir o actualizar.

El uso de punto de datos es idéntico con CDI que con otros métodos de ingesta como las API REST o los SDK, por lo que depende de ti asegurarte de que sólo añades atributos nuevos o actualizados a tus tablas de origen.

### Utiliza una fecha y hora UTC para la columna `UPDATED_AT` 

La columna `UPDATED_AT` debe estar en UTC para evitar problemas con el horario de verano. Prefiere funciones sólo UTC, como `SYSDATE()` en lugar de `CURRENT_DATE()` siempre que sea posible.

### Asegúrate de que la hora de `UPDATED_AT` no coincide con la hora de tu sincronización.

Tu sincronización CDI podría tener datos duplicados si alguno de los campos `UPDATED_AT` está exactamente a la misma hora que la última marca de tiempo `UPDATED_AT` del anterior trabajo de sincronización realizado con éxito. Esto se debe a que CDI elegirá un "límite inclusivo" cuando identifique cualquier fila que coincida en el tiempo con la sincronización anterior, y hará que las filas puedan sincronizarse. CDI volverá a analizar esas filas y creará datos duplicados.

### Separa `EXTERNAL_ID` de la columna `PAYLOAD` 

El objeto `PAYLOAD` no debe incluir un ID externo u otro tipo de ID. 

### Eliminar un atributo

Puedes establecerlo en `null` si quieres omitir un atributo del perfil de un usuario. Si quieres que un atributo no se modifique, no lo envíes a Braze hasta que se haya actualizado. Para eliminar completamente un atributo, utiliza `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Haz actualizaciones incrementales

Realiza actualizaciones incrementales de tus datos para evitar sobrescrituras involuntarias cuando se realicen actualizaciones simultáneas.

En el siguiente ejemplo, un usuario tiene dos atributos:
- Color: "Verde"
- Talla: "Grande"

Entonces Braze recibe simultáneamente las dos actualizaciones siguientes para ese usuario:
- Petición 1: Cambiar el color a "Rojo"
- Petición 2: Cambia el tamaño a "Medio"

Como la Petición 1 se produce en primer lugar, los atributos del usuario se actualizan a lo siguiente:
- Color: "Rojo"
- Talla: "Grande"

Sin embargo, cuando se produce la Petición 2, Braze comienza con los valores originales de los atributos ("Verde" y "Grande") y, a continuación, actualiza los atributos del usuario a los siguientes:
- Color: "Verde"
- Talla: "Medio"

Cuando finalicen las solicitudes, la Solicitud 2 sobrescribirá la actualización de la Solicitud 1, por lo que es mejor escalonar las actualizaciones para evitar que se sobrescriban las solicitudes.

### Crear una cadena JSON a partir de otra tabla

Si prefieres almacenar internamente cada atributo en su propia columna, tienes que convertir esas columnas en una cadena JSON para rellenar la sincronización con Braze. Para ello, puedes utilizar una consulta como

{% tabs local %}
{% tab Snowflake %}
```json
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
```json
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
```json
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
```json
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
```json
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

Utilizamos la marca de tiempo `UPDATED_AT` para hacer un seguimiento de los datos que se han sincronizado correctamente con Braze. Si se escriben muchas filas con la misma marca de tiempo mientras se está ejecutando una sincronización, esto puede provocar que se sincronicen datos duplicados con Braze. Algunas sugerencias para evitar la duplicación de datos:
- Si estás configurando una sincronización con un `VIEW`, no utilices `CURRENT_TIMESTAMP` como valor predeterminado. Esto hará que todos los datos se sincronicen cada vez que se ejecute la sincronización, porque el campo `UPDATED_AT` se evaluará a la hora en que se ejecuten nuestras consultas. 
- Si tienes canalizaciones o consultas de muy larga duración que escriben datos en tu tabla de origen, evita ejecutarlas simultáneamente con una sincronización, o evita utilizar la misma marca de tiempo para cada fila insertada.
- Utiliza una transacción para escribir todas las filas que tengan la misma marca de tiempo.

### Configuración de la mesa

Tenemos un [repositorio](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) público [en GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) para que los clientes compartan las mejores prácticas o fragmentos de código. Para contribuir con tus propios fragmentos de código, ¡crea un pull request!

### Formato de los datos

Cualquier operación que sea posible a través del punto final Braze `/users/track` se admite a través de la Ingesta de datos en la nube, incluida la actualización de atributos personalizados anidados, la adición del estado de suscripción y la sincronización de eventos personalizados o compras. 

Los campos de la carga útil deben seguir el mismo formato que el correspondiente punto final de `/users/track`. Para conocer los requisitos detallados de formato, consulta lo siguiente:

| Tipo de datos | Especificaciones de formato |
| --------- | ---------| --------- | ----------- |
| `attributes` | Ver [objeto atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Ver [objeto eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Ver [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) |

Nota el requisito especial para [capturar fechas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) en atributos anidados. 

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
Para sincronizar eventos, se necesita un nombre de evento. El campo `time` debe formatearse como una cadena ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si el campo `time` no está presente, se utiliza el valor de la columna `UPDATED_AT` como hora del evento. Otros campos como `app_id` y `properties` son opcionales. 

Ten en cuenta que sólo puedes sincronizar un evento por fila.

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
Para sincronizar los eventos de compra, se necesitan `product_id`, `currency`, y `price`. El campo `time`, que es opcional, debe formatearse como una cadena ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si el campo `time` no está presente, se utiliza el valor de la columna `UPDATED_AT` como hora del evento. Otros campos, como `app_id`, `quantity` y `properties` son opcionales.

Ten en cuenta que sólo puedes sincronizar un evento de compra por fila.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
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

### Evitar los tiempos de espera en las consultas del almacén de datos

Recomendamos que las consultas se completen en el plazo de una hora para obtener un rendimiento óptimo y evitar posibles errores. Si las consultas superan este plazo, plantéate revisar la configuración de tu almacén de datos. Optimizar los recursos asignados a tu almacén puede ayudar a mejorar la velocidad de ejecución de las consultas.

## Limitaciones del producto

| Limitación            | Descripción                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integraciones | No hay límite en el número de integraciones que puedes configurar. Sin embargo, sólo podrás configurar una integración por tabla o vista.                                             |
| Número de filas         | Por defecto, cada ejecución puede sincronizar hasta 500 millones de filas. Se detendrá cualquier sincronización con más de 500 millones de filas nuevas. Si necesitas un límite superior, ponte en contacto con tu administrador del éxito del cliente de Braze o con el soporte de Braze. |
| Atributos por fila     | Cada fila debe contener un único ID de usuario y un objeto JSON con un máximo de 250 atributos. Cada clave del objeto JSON cuenta como un atributo (es decir, una matriz cuenta como un atributo). |
| Tamaño de la carga útil           | Cada fila puede contener una carga útil de hasta 1 MB. Las cargas útiles superiores a 1 MB serán rechazadas, y el error "La carga útil era superior a 1 MB" se registrará en el registro de sincronización junto con el ID externo asociado y la carga útil truncada. |
| Tipo de datos              | Puedes sincronizar atributos de usuario, eventos y compras a través de la Ingesta de datos en la nube.                                                                                                  |
| Región de Braze           | Este producto está disponible en todas las regiones Braze. Cualquier región Braze puede conectarse a cualquier región de origen de datos.                                                                              |
| Región de origen       | Braze se conectará a tu almacén de datos o entorno de nube en cualquier región o proveedor de nube.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
