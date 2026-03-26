---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la ingesta de datos en la nube
page_order: 100
page_type: FAQ
description: "Esta página responde a las preguntas más frecuentes sobre la ingesta de datos en la nube."
toc_headers: h2
---

# Preguntas más frecuentes

> Esta página contiene respuestas a algunas preguntas frecuentes sobre la ingesta de datos en la nube.

## ¿Por qué me enviaron un correo electrónico: "Error en la sincronización CDI"?

Este tipo de correo electrónico suele significar que hay un problema con tu configuración de CDI. Aquí tienes algunos problemas comunes y cómo solucionarlos:

### CDI no puede acceder al almacén de datos o a la tabla utilizando tus credenciales

Esto podría significar que las credenciales en CDI son incorrectas o están mal configuradas en el almacén de datos. Para más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### No se encuentra la tabla

Intenta actualizar tu integración con la configuración correcta de la base de datos o crea recursos coincidentes en el almacén de datos, como `database/table`.

### No se encuentra el catálogo

El catálogo configurado en la integración no existe en el catálogo de Braze. Se puede eliminar un catálogo después de configurar la integración. Para resolver el problema, actualiza la integración para utilizar un catálogo diferente o crea un catálogo nuevo que coincida con el nombre del catálogo en la integración.

## ¿Por qué me enviaron un correo electrónico: "Errores de fila en tu sincronización CDI"?

Este tipo de correo significa que algunos de tus datos no pudieron ser procesados durante la sincronización. Para averiguar el error concreto, puedes revisar los registros en Braze yendo a **CDI** > **Registro de sincronización**.

## ¿Cómo corrijo los errores de Test Connection y de los correos electrónicos de asistencia?

{% tabs %}
{% tab Snowflake %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### Error al conectar con la instancia de Snowflake: solicitud entrante con IP no autorizada para acceder a Snowflake

Intenta añadir las IP oficiales de Braze a tu lista de IP permitidas. Para obtener más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/) o permite las direcciones IP pertinentes:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Error al ejecutar SQL debido a la configuración del cliente: 002003 (42S02): error de compilación SQL: no existe o no está autorizado

Si la tabla no existe, créala. Si la tabla existe, comprueba que el usuario y el rol tienen permisos para leer la tabla.

### No se ha podido utilizar el esquema

Si recibes este error, concede acceso a ese esquema para el usuario o rol especificado.

### No se ha podido utilizar el rol

Si recibes este error, permite que ese usuario utilice el rol especificado.

### Acceso de usuario desactivado

Si recibes este error, permite a ese usuario el acceso a tu cuenta de Snowflake.

### Error al conectarse a la instancia de Snowflake con la clave actual y la antigua

Si recibes este error, asegúrate de que el usuario está utilizando la clave pública actual que se muestra en tu panel de Braze.
{% endtab %}

{% tab Redshift %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### Permiso denegado para la relación {table_name}

Si recibes este error:

  - Concede el permiso `usage` en el esquema para ese usuario.
  - Concede el permiso `select` en la tabla para ese usuario.

### Error al crear conexión

Si recibes este error, comprueba que el punto de conexión y el puerto de Redshift son correctos.

### Error al crear túnel SSH

Si recibes este error:

  - Comprueba que la clave pública de tu panel de Braze está en el host ec2 utilizado para el túnel SSH.
  - Comprueba que tu nombre de usuario es correcto.
  - Comprueba que el túnel SSH es correcto.
{% endtab %}

{% tab BigQuery %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### El usuario no tiene permiso para consultar la tabla

Si recibes este error, añade permisos de usuario para consultar la tabla.

### Tu uso ha superado la cuota personalizada

Si recibes este error, es necesario actualizar tu cuota para que puedas seguir sincronizando al ritmo actual.

### No se ha encontrado la tabla en la ubicación {region}

Si recibes este error, comprueba que la tabla se encuentra en el proyecto y el conjunto de datos correctos.

### Firma JWT no válida

Si recibes este error, comprueba que el servicio de API de BigQuery está habilitado para tu cuenta.
{% endtab %}

{% tab Databricks %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. En el caso de Databricks, puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecta a instancias Classic y Pro SQL, lo que provocará retrasos durante la configuración y las pruebas de conexión, así como al inicio de las sincronizaciones programadas. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### El comando ha fallado porque el almacén estaba detenido

Si recibes este error, asegúrate de que el almacén de Databricks está en ejecución.

### Servicio: Amazon S3; código de estado: 403; código de error: 403 Forbidden

Si recibes este error, consulta [Databricks: error Forbidden al acceder a los datos de S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## ¿Cómo actualizo mis preferencias de alertas por correo electrónico para las integraciones CDI?

Cada integración tiene sus propias preferencias de notificación. Ve a la página CDI y selecciona el nombre de la integración que deseas actualizar. En la sección **Preferencias de notificación** puedes actualizar cómo recibes las alertas relativas a la integración seleccionada.

## ¿Qué sucede si un UPDATED_AT futuro se sincroniza con una integración?

CDI utiliza `UPDATED_AT` para decidir qué datos son nuevos. Después de sincronizar un `UPDATED_AT` futuro, no se procesarán los datos anteriores a esa fecha y hora futuras. Para solucionarlo:

1. Corrige `UPDATED_AT`.
2. Elimina los datos antiguos que ya estén sincronizados con Braze.
3. Crea una nueva integración para procesar de nuevo esa tabla.

## ¿Por qué "Filas sincronizadas" no coincide con el número de mi almacén?

CDI utiliza `UPDATED_AT` para decidir qué registros recoger durante una sincronización. Mira [esta ilustración]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) para ver cómo funciona. Al inicio de una sincronización, CDI realiza una consulta en tu almacén para obtener todos los registros con `UPDATED_AT` posterior al valor `UPDATED_AT` procesado anteriormente. Los registros que se encuentren exactamente en la marca de tiempo límite también pueden volver a sincronizarse si nuevas filas comparten esa marca de tiempo. Cualquier registro recogido en el momento en que se ejecuta la consulta se sincroniza en Braze. Estos son los casos habituales en los que un registro puede no sincronizarse:

- Estás añadiendo registros a la tabla con un valor `UPDATED_AT` que ya ha sido procesado.
- Estás actualizando los valores de los registros después de que hayan sido procesados por una sincronización, pero dejando `UPDATED_AT` sin cambios. 
- Estás añadiendo o actualizando registros mientras se realiza una sincronización. Dependiendo del momento en que se ejecute la consulta CDI, puede haber condiciones de carrera que provoquen que no se recojan los registros.

{% alert tip %}
Para evitar estos comportamientos en el futuro, recomendamos utilizar valores `UPDATED_AT` que aumenten monotónicamente y no actualizar la tabla durante la ejecución de la sincronización programada.
{% endalert %}

## Durante una sincronización, ¿se mantiene el orden si varios registros comparten el mismo ID?

El orden de procesamiento no es 100 % predecible. Por ejemplo, si hay varias filas con el mismo `EXTERNAL_ID` en la tabla durante una sincronización, no podemos garantizar qué valor acabará en el perfil final. Si actualizas el mismo `EXTERNAL_ID` con diferentes atributos en la columna de carga útil, todos los cambios se reflejarán cuando se complete la sincronización.

## ¿Por qué no se crean nuevos usuarios a partir de mi sincronización CDI?

Si tu integración CDI tiene habilitada la opción **Actualizar solo usuarios existentes**, solo se actualizarán los usuarios que ya existen en Braze y no se crearán nuevos usuarios. Esto significa que si una fila de tu tabla de sincronización hace referencia a un `EXTERNAL_ID` que no coincide con ningún usuario existente de Braze, esa fila se omite.

Para crear nuevos usuarios a través de CDI, desactiva la opción **Actualizar solo usuarios existentes** en la configuración de la integración. Ve a **Configuración de datos** > **Ingesta de datos en la nube** y selecciona una integración.

## ¿Cuáles son las medidas de seguridad de CDI?

### Nuestras medidas

Braze cuenta con las siguientes medidas para CDI:

- Todas las credenciales están cifradas dentro de nuestra base de datos, y solo determinados empleados tienen acceso autenticado a ellas.
- Utilizamos conexiones cifradas para obtener los datos de los almacenes de los clientes.
- Realizamos solicitudes a los puntos finales de la API de Braze utilizando las mismas claves de API y conexiones TLS que recomendamos utilizar a nuestros clientes.
- Actualizamos regularmente nuestras bibliotecas y aplicamos todos los parches de seguridad.

### Tus medidas

Te recomendamos que tú y tu equipo establezcan las siguientes medidas de seguridad: 

- Restringe el acceso a las credenciales al mínimo necesario para el funcionamiento de CDI. Esto se debe a que necesitamos poder ejecutar select (y count) en las tablas y vistas específicas.
- Restringe las IP que pueden acceder a las tablas a las [IP de Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views) publicadas oficialmente.