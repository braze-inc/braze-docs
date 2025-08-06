---
nav_title: LiveRamp
article_title: LiveRamp
description: "Aprenda a conectar LiveRamp, Snowflake y Braze para crear campañas de marketing altamente personalizadas y relevantes."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Conexión de LiveRamp, Snowflake y Braze

> Aprenda a conectar LiveRamp, Snowflake y Braze para crear campañas de marketing altamente personalizadas y relevantes reduciendo el tiempo de obtención de información, eliminando los silos de datos y optimizando la interacción con los clientes. Esta integración mejora el marketing basado en datos al proporcionar información procesable basada en las personas y consolidar los puntos de contacto con el consumidor para una mejor segmentación de la audiencia y campañas oportunas. También aprovecha los puntos de referencia de Snowflake para ayudarle a perfeccionar sus estrategias de marketing comparándolas con los estándares del sector.

{% alert important %}
El [intercambio seguro de datos](https://docs.snowflake.com/en/user-guide/data-sharing-intro) de Snowflake no transfiere datos entre LiveRamp, Snowflake y Braze. Los datos sólo se comparten a través de los servicios y el almacén de metadatos de Snowflake, lo que significa que no se copian datos ni se producen cargos adicionales por almacenamiento. El acceso a los datos compartidos se controla y regula mediante los controles de acceso de su cuenta Snowflake.
{% endalert %}

## Casos prácticos

- **Minimización de datos:** La aplicación Activación de LiveRamp utiliza la característica Compartir datos seguros de Snowflake para leer eficazmente las tablas directamente desde tu instancia. No se mueven datos desde Snowflake hasta el punto de entrega al socio posterior.
- **Asegurar la activación de la 1a Parte:** Al utilizar la aplicación de Resolución de Identidad anterior, la aplicación de Activación de LiveRamp sólo utilizará las tablas basadas en RampID en su instancia de Snowflake, y por lo tanto la PII nunca tendrá que salir de sus paredes.
- **Acelerar el tiempo de vida:** Al resolver los datos a RampID directamente en su entorno, la entrega a un destino final puede producirse en cuestión de horas, en comparación con varios días cuando se utiliza el enfoque más tradicional basado en archivos de LiveRamp. Esto aumenta enormemente la capacidad de optimizar el rendimiento de las campañas en el momento oportuno.
- **Ahorro operativo:** De forma similar a lo anterior, mediante el uso de la característica Compartir datos de forma segura de Snowflake, los clientes ahorran tiempo y dinero en comparación con la coordinación de la salida de archivos a LiveRamp o directamente a cualquier destino final.

## Requisitos previos

| Requisito previo       | Descripción                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cuenta Snowflake | Necesita una cuenta Snowflake con permisos de nivel de administrador.                                                                                                                                      |
| Cuenta LiveRamp  | Póngase en contacto con el equipo de su cuenta LiveRamp o con [snowflake@liveramp.com](mailto:snowflake@liveramp.com) para hablar de las aplicaciones LiveRamp necesarias dentro de Snowflake.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## Configuración de la integración

### Paso 1: Solicitar un intercambio de datos a Braze

En primer lugar, ponte en contacto con tu director de cuentas Braze o tu administrador del éxito de los clientes para adquirir un conector Snowflake Data Share para tu cuenta Braze. Cuando solicite un uso compartido de datos, Braze aprovisionará el uso compartido desde el espacio o espacios de trabajo en los que se adquirió el uso compartido. Una vez aprovisionado el recurso compartido, se puede acceder inmediatamente a todos los datos desde su instancia de Snowflake en forma de recurso compartido de datos entrantes. Una vez que el recurso compartido sea visible en su instancia, cree una base de datos a partir del recurso compartido para poder ver y consultar las tablas.

Para obtener un tutorial completo, consulte la [guía de integración de Snowflake con Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Paso 2: Configurar la aplicación LiveRamp en Snowflake 

Las funciones de traducción y resolución de identidades están disponibles en Snowflake a través de la aplicación nativa LiveRamp Identity Resolution and Translation, que crea un recurso compartido en su cuenta y abre una vista para consultar el conjunto de datos de referencia desde su propio entorno Snowflake.

Para configurar la aplicación nativa, siga estos pasos en los documentos de LiveRamp: [Configurar la aplicación nativa LiveRamp en Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Cuando hayas terminado, continúa con el siguiente paso.

### Paso 3: Crear una tabla de datos

{% alert warning %}
Antes de preparar cualquier tabla basada en PII, asegúrese de entender [el filtro de privacidad de LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) que se ejecuta durante los trabajos para asegurar que las columnas de atributos (no identificadores) en sus tablas de entrada no contengan valores demasiado únicos. Esto es fundamental para mantener la privacidad del consumidor y evitar la reidentificación.
{% endalert %}

A continuación, cree una tabla de datos con el [formato requerido](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) que se llamará contra la aplicación nativa LiveRamp. Consulte las siguientes categorías para determinar cuáles de sus identificadores son susceptibles de resolución:

| Tipo de identificador | Descripción  |
|-----------------|--------------|
| PII completo        | La información personal identificable (IPI) incluye el nombre, la dirección postal, el correo electrónico y el número de teléfono del usuario. **Nota:** No todos los identificadores son necesarios para todos los registros. |
| Sólo correo electrónico      | Las direcciones de correo electrónico de los usuarios, como `alex-lee@email.com`. |
| Dispositivo          | Esto incluye cookies de terceros, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs) y RampIDs (resueltos a un Household RampID). |
| CID            | Se trata de identificadores de un socio de la plataforma o de una identidad sincronizada con LiveRamp, como tu ID de cliente interno. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Identificadores de soldadura

Los registros de eventos de Braze contienen identificadores que puede utilizar dentro de la aplicación nativa LiveRamp. Para obtener una lista completa de los identificadores disponibles para cada tipo de evento, descargue los [esquemas e identificadores de eventos Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

| Tipo de identificador | Descripción  |
|-----------------|--------------|
| `AD_ID` | Identificadores de publicidad, como `ios_idfa`, `google_ad_id`, `roku_ad_id`, capturados dentro de determinados tipos de eventos, que pueden utilizarse junto con los servicios de resolución de dispositivos de LiveRamp. Por defecto, los ID de publicidad no se recopilan; sin embargo, puedes habilitar el seguimiento siguiendo [la documentación de Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS`   | Dirección de correo electrónico que puede utilizarse junto con los servicios de Resolución sólo por correo electrónico de LiveRamp |
| `TO_PHONE_NUMBER` | Número de teléfono, que puede utilizarse junto con los servicios de Resolución PII de LiveRamp. |
| `EXTERNAL_USER_ID` | El ID externo asociado a un usuario, que puede utilizarse junto con los servicios de Resolución de Dispositivos (CID) de LiveRamp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
El uso de cualquier identificador personalizado específico del cliente o de la marca dentro de la aplicación de LiveRamp requiere una [sincronización de identidad con LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Paso 4: Establezca sus variables

A continuación, establezca sus variables para el trabajo en la hoja de cálculo Pasos de ejecución que se proporciona en la aplicación. Esto incluye detalles como la base de datos de destino, las tablas asociadas (datos de entrada, métricas, registro) y la definición del nombre de la tabla de salida. Para un recorrido completo, consulta [LiveRamp: Especifica las variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Paso 5: Crear la tabla de metadatos para la resolución PII

Ahora que sus variables están configuradas, cree la tabla de metadatos para la resolución PII. Esto dará detalles sobre el tipo de trabajo específico que debe ejecutarse en función de la categoría de los identificadores implicados. Para un recorrido completo, consulta [LiveRamp: Crear la tabla de metadatos](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Paso 6: Realizar la operación de resolución de identidad

Por último, realice la operación de resolución de identidad. Para un recorrido completo, consulta [LiveRamp: Realice la operación de resolución de identidad](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab ejemplo de entrada %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab ejemplo de salida %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Próximos pasos

Con sus datos ahora seudonimizados a su codificación dedicada de RampID, usted tiene la capacidad de compartir las tablas basadas en RampID a la Aplicación de Activación Gestionada de LiveRamp para el cumplimiento racionalizado a sus socios clave de la plataforma de publicidad. La aplicación de activación incluye una interfaz de usuario empresarial fácil de usar para la segmentación adicional y la selección/configuración de socios de destino descendentes. Para más detalles sobre la aplicación, ponte en contacto con tu equipo de cuentas LiveRamp o con [Snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Solución de problemas

{% alert note %}
Si tienes dudas o preguntas más concretas, ponte en contacto con [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Regiones Snowflake

Actualmente, esta aplicación sólo está disponible para las siguientes regiones de EEUU:

  - aws-us-este-1: POA18931
  - aws-us-oeste-2: FAA28932
  - azure-east-us-2: BL60425

### Privacidad y valores de columna

El proceso evalúa la combinación de todos los valores de columna por fila en busca de valores únicos. Si una determinada combinación de valores de columna aparece 3 o menos veces, las filas que contengan esos valores de columna no serán coincidentes y no se devolverán en la tabla de salida. Asimismo, para garantizar la privacidad, el servicio LiveRamp evalúa la unicidad de las combinaciones de valores de columna, garantizando que si más del 5% de las filas del archivo resultan incomparables debido a combinaciones raras, el trabajo fallará.

### Datos históricos

Los datos históricos en Snowflake se remontan a abril de 2019, pero puede haber ligeras diferencias en los datos anteriores a agosto de 2019 debido a cambios en el producto.

### Velocidad, rendimiento, coste

La velocidad y el coste de las consultas dependen del tamaño del almacén utilizado. Tenga en cuenta sus necesidades de acceso a los datos a la hora de seleccionar el tamaño del almacén.

### Puntos de referencia Braze

Los puntos de referencia le permiten comparar sus métricas con los estándares del sector, disponibles directamente en el Snowflake Data Exchange.

### Cambios de ruptura vs. Cambios sin ruptura

Esté atento a los cambios que puedan afectar a su integración. Los cambios de última hora irán precedidos de un anuncio y de un periodo de migración.
