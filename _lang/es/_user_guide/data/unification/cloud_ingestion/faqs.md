---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la ingesta de datos en la nube
page_order: 100
page_type: FAQ
description: "Esta página responde a las preguntas más frecuentes sobre la ingesta de datos en la nube."
toc_headers: h2
---

# Preguntas más frecuentes

> Esta página contiene respuestas a algunas preguntas frecuentes sobre la Ingesta de datos en la nube.

## ¿Por qué me enviaron un correo electrónico? ¿"Error en la sincronización CDI"?

Este tipo de correo electrónico suele significar que hay un problema con la configuración de tu CDI. Aquí tienes algunos problemas comunes y cómo solucionarlos:

### El CDI no puede acceder al almacén de datos o a la tabla utilizando tus credenciales

Esto podría significar que las credenciales en CDI son incorrectas o están mal configuradas en el almacén de datos. Para más información, consulta [Integración de almacenes de datos]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### No se encuentra la tabla

Prueba a actualizar tu integración con la configuración correcta de la base de datos o a crear recursos coincidentes en el almacén de datos, como `database/table`.

### No se encuentra el catálogo

El catálogo configurado en la integración no existe en el catálogo Braze. Se puede eliminar un catálogo después de configurar la integración. Para resolver el problema, actualiza la integración para utilizar un catálogo diferente o crea un catálogo nuevo que coincida con el nombre del catálogo de la integración.

## ¿Por qué me enviaron un correo electrónico? ¿"Errores de fila en tu sincronización CDI"?

Este tipo de correo electrónico significa que algunos de tus datos no pudieron procesarse durante la sincronización. Para averiguar el error concreto, puedes revisar los registros en Braze yendo a **CDI** > **Registro de sincronización**.

## ¿Cómo corrijo los errores de los correos electrónicos de Test Connection y de asistencia?

{% tabs %}
{% tab Snowflake %}
### Prueba La conexión va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Utilizar una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede suponer unos costes de integración ligeramente superiores.

### Error al conectar con la instancia de Snowflake: La solicitud entrante con IP no puede acceder a Snowflake

Prueba a añadir las IP oficiales de Braze a tu lista de IP permitidas. Para más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), o permite las IP correspondientes:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Error al ejecutar SQL debido a la configuración del cliente: 002003 (42S02): Error de compilación SQL: no existe o no está autorizado

Si la tabla no existe, créala. Si la tabla existe, comprueba que el usuario y el rol tienen permisos para leer de la tabla.

### No se ha podido utilizar el esquema

Si recibes este error, concede acceso a ese esquema al usuario o rol especificado.

### No se ha podido utilizar el rol

Si recibes este error, permite que ese usuario utilice el rol especificado.

### Acceso de usuario desactivado

Si recibes este error, permite que ese usuario acceda a tu cuenta de Snowflake.

### Error al conectar a la instancia Snowflake con la clave actual y la antigua

Si recibes este error, asegúrate de que el usuario está utilizando la clave pública actual que se muestra en tu panel Braze.
{% endtab %}

{% tab Redshift %}
### Prueba La conexión va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Utilizar una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede suponer unos costes de integración ligeramente superiores.

### Permiso denegado para la relación {table_name}

Si recibes este error:

  - Concede el permiso `usage` en el esquema para ese usuario.
  - Concede el permiso `select` en la tabla para ese usuario.

### Crear error de conexión

Si recibes este error, comprueba que el punto final y el puerto de Redshift son correctos.

### Error al crear túnel SSH

Si recibes este error:

  - Comprueba que la clave pública de tu panel de Braze está en el host ec2 utilizado para el túnel SSH.
  - Comprueba que tu nombre de usuario es correcto.
  - Comprueba que el Túnel SSH es correcto.
{% endtab %}

{% tab BigQuery %}
### Prueba La conexión va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Utilizar una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede suponer unos costes de integración ligeramente superiores.

### El usuario no tiene permiso para consultar la tabla

Si recibes este error, añade permisos de usuario para consultar la tabla.

### Tu uso ha superado la cuota personalizada

Si recibes este error, es necesario actualizar tu cuota para que puedas seguir sincronizando a tu tasa actual.

### No se ha encontrado la tabla en la ubicación {región} Ubicación

Si recibes este error, comprueba que tu tabla está en el proyecto y conjunto de datos correctos.

### Firma JWT no válida

Si recibes este error, comprueba que el servicio API BigQuery está habilitado para tu cuenta.
{% endtab %}

{% tab Databricks %}
### Prueba La conexión va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. En el caso de Databricks, puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecte a las instancias SQL Clásica y Pro, lo que provocará retrasos durante la configuración y prueba de la conexión, así como al inicio de las sincronizaciones programadas. Utilizar una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede suponer unos costes de integración ligeramente superiores.

### El comando falló porque el almacén estaba parado

Si recibes este error, asegúrate de que se está ejecutando el almacén Databricks.

### Servicio: Amazon S3; Código de estado: 403; Código de error: 403 Prohibido

Si recibes este error, consulta [Databricks: Error prohibido al acceder a los datos de S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## ¿Cómo actualizo mis preferencias de alertas por correo electrónico para las integraciones CDI?

Cada integración tiene su propia preferencia de notificación. Ve a la página CDI y selecciona el nombre de la integración que quieres actualizar. En la sección **Preferencias de notificación** puedes actualizar cómo recibes las notificaciones relativas a la integración seleccionada.

## ¿Qué ocurre si un futuro UPDATED_AT se sincroniza con una integración?

El CDI utiliza `UPDATED_AT` para decidir qué datos son nuevos. Después de sincronizar un `UPDATED_AT` futuro, no se procesarán los datos anteriores a esa fecha y hora futuras. Para solucionarlo:

1. Correcto `UPDATED_AT`.
2. Elimina los datos antiguos que ya estén sincronizados con Braze
3. Crea una nueva integración para procesar de nuevo esa tabla.

## ¿Por qué "Filas sincronizadas" no coincide con el número de mi almacén?

El CDI utiliza `UPDATED_AT` para decidir qué registros recoger durante una sincronización. Mira [esta ilustración]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) para ver cómo funciona. Al principio de una ejecución de sincronización, CDI consulta tu almacén para obtener todos los registros con `UPDATED_AT` igual o posterior a la marca de tiempo `UPDATED_AT` procesada previamente. Cualquier registro recogido en el momento en que se ejecute la consulta se sincronizará en Braze. Estos son los casos habituales en los que un registro puede no estar sincronizado:

- Estás añadiendo registros a la tabla con un valor `UPDATED_AT` que ya ha sido procesado.
- Estás actualizando los valores de los registros después de que hayan sido procesados por una sincronización, pero dejando `UPDATED_AT` sin cambios. 
- Estás añadiendo o actualizando registros mientras se realiza una sincronización. Dependiendo del momento en que se ejecute la consulta CDI, puede haber condiciones de carrera que provoquen que no se recojan los registros.

{% alert tip %}
Para evitar estos comportamientos en el futuro, recomendamos utilizar valores `UPDATED_AT` que aumenten monotónicamente y no actualizar la tabla durante la ejecución programada de la sincronización.
{% endalert %}

## Durante una sincronización, ¿se conserva el orden si varios registros comparten el mismo ID?

El orden de procesamiento no es 100% previsible. Por ejemplo, si hay varias filas con el mismo `EXTERNAL_ID` en la tabla durante una sincronización, no podemos garantizar qué valor acabará en el perfil final. Si estás actualizando el mismo `EXTERNAL_ID` con diferentes atributos en la columna de carga útil, todos los cambios se reflejarán cuando finalice la sincronización.

## ¿Cuáles son las medidas de seguridad del CDI?

### Nuestras medidas

Braze cuenta con las siguientes medidas para la CDI:

- Todas las credenciales están encriptadas dentro de nuestra base de datos, y sólo determinados empleados tienen acceso autenticado a ellas.
- Utilizamos conexiones encriptadas para obtener datos de los almacenes de clientes.
- Hacemos solicitudes a los puntos finales de la API Braze utilizando las mismas claves de API y conexiones TLS que recomendamos utilizar a nuestros clientes.
- Actualizamos regularmente nuestras bibliotecas y recibimos todos los parches de seguridad.

### Tus medidas

Te recomendamos que tú y tu equipo configuréis las siguientes medidas de seguridad: 

- Restringe el acceso a las credenciales al mínimo necesario para que funcione el CDI. Esto se debe a que necesitamos poder ejecutar selecciones (y recuentos) en las tablas y vistas específicas.
- Restringe las IP que pueden acceder a las tablas a [las IP de Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views) publicadas oficialmente.
