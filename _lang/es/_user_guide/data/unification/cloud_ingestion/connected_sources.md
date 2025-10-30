---
nav_title: Fuentes conectadas
article_title: Fuentes conectadas
description: "Esta página explica cómo utilizar Braze Cloud Data Ingestion para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Fuentes conectadas

> Las fuentes conectadas son una alternativa de copia cero a la sincronización directa de datos con la característica de ingestión de datos en la nube (CDI) de Braze. Un origen conectado consulta directamente tu almacén de datos para crear nuevos segmentos sin copiar ninguno de los datos subyacentes a Braze. 

Después de añadir una fuente conectada a tu espacio de trabajo Braze, puedes crear un segmento CDI dentro de Extensiones de segmento. Las extensiones de segmento CDI te permiten escribir SQL que consulta directamente tu almacén de datos (utilizando los datos que allí se ponen a disposición a través de tu CDI Connected Source), y crea y mantiene un grupo de usuarios a los que se puede dirigir dentro de Braze. 

Para más información sobre cómo crear un segmento con esta fuente, consulta [Extensiones de segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert warning %}
Dado que las fuentes conectadas se ejecutan directamente en tu almacén de datos, incurrirás en todos los costes asociados a la ejecución de estas consultas en tu almacén de datos. Las fuentes conectadas no registran puntos de datos, y las extensiones de segmento CDI no consumen créditos de segmento SQL.
{% endalert %}

## Integración de fuentes conectadas

### Paso 1: Conecta tus recursos

Las fuentes conectadas a la ingesta de datos en la nube requieren cierta configuración en Braze y en tu instancia. Sigue estos pasos para configurar la integración: algunos pasos se harán en tu almacén de datos y otros en tu panel Braze.

{% tabs %}
{% tab Snowflake %}
**En tu almacén de datos**
1. Crea un rol y concede permisos para consultar y crear tablas en un esquema.
2. Configura tu almacén y da acceso a ese rol.
3. Crea un usuario para ese rol.
4. Dependiendo de tu configuración, puede que tengas que permitir las IP de Braze en tu política de red de Snowflake.

**En el panel de Braze**

{: start="5"}
5\. Crea una nueva fuente conectada en el panel de Braze.
6\. Configura los detalles de sincronización de la fuente conectada.
7\. Recupera la clave pública proporcionada en el panel de Braze.

**En tu almacén de datos**

{: start="8"}
8\. Añade la clave pública del panel de Braze al [usuario Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Cuando hayas terminado, puedes utilizar la fuente conectada para crear una o varias extensiones de segmento CDI.
{% endtab %}

{% tab Redshift %}
1. Configura los datos de origen y los recursos necesarios en tu entorno Redshift.
2. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias extensiones de segmento CDI.
{% endtab %}

{% tab BigQuery %}
1. Configura los datos de origen y los recursos necesarios en tu entorno BigQuery.
2. Crea una cuenta de servicio y permite el acceso al proyecto o proyectos BigQuery y al conjunto o conjuntos de datos que contienen los datos que quieres sincronizar.  
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias extensiones de segmento CDI.
{% endtab %}

{% tab Databricks %}
1. Configura los datos de origen y los recursos necesarios en tu entorno Databricks.
2. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contengan los datos que deseas sincronizar.  
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias extensiones de segmento CDI.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecte a las instancias SQL Clásica y Pro, lo que provocará retrasos durante la configuración y prueba de la conexión, así como durante la creación y actualización de la Extensión de Segmento CDI. Utilizar una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede suponer unos costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Crea un principal de servicio y permite el acceso al espacio de trabajo de Fabric que se utilizará para tu integración.   
2. En tu espacio de trabajo de Fabric, configura los datos de origen y concede permisos al director de tu servicio 
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias extensiones de segmento CDI.
{% endtab %}

{% endtabs %}

### Paso 2: Configura tu almacén de datos

Configura los datos de origen y los recursos necesarios en tu entorno de almacén de datos. La fuente conectada puede hacer referencia a una o más tablas, así que asegúrate de que tu usuario de Braze tiene permiso para acceder a todas las tablas que quieras en la fuente conectada.

{% tabs %}
{% tab Snowflake %}
#### Paso 2.1: Crear un rol y conceder permisos

Crea un rol para que lo utilice tu fuente conectada. Este rol se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI, y para consultar las tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente.

Puedes elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios sólo a tablas concretas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en la Extensión de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla sólo persistirá mientras Braze esté actualizando el segmento.

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Paso 2.2: Configurar el almacén y dar acceso al rol Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén debe tener activada la bandera de **reanudación automática**. Si no lo está, tendrás que conceder a Braze privilegios adicionales de `OPERATE` en el almacén para que Braze lo active cuando llegue el momento de ejecutar la consulta.
{% endalert %}

#### Paso 2.3: Configurar el usuario
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Compartirás la información de conexión con Braze y recibirás una clave pública para adjuntar al usuario en un paso posterior.

{% alert note %}
Cuando conectes diferentes espacios de trabajo a la misma cuenta Snowflake, debes crear un usuario único para cada espacio de trabajo Braze en el que estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración fallará si un usuario de la misma cuenta de Snowflake está duplicado en todos los espacios de trabajo.
{% endalert %}

#### Paso 2.4: Permitir IPs Braze en tu política de red Snowflake (opcional)

Dependiendo de la configuración de tu cuenta Snowflake, puede que tengas que permitir las siguientes direcciones IP en tu política de red Snowflake. Para más información sobre cómo hacerlo, consulta la documentación correspondiente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Paso 2.1: Crear usuario y conceder permisos 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crea un usuario para que lo utilice tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI, y para consultar las tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. Si creas varias integraciones CDI, tal vez quieras conceder permisos a un esquema o administrar los permisos mediante un grupo. 

Puedes elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios sólo a tablas concretas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en la Extensión de segmento CDI. Asegúrate de conceder acceso a cualquier tabla nueva al usuario cuando se cree, o establece permisos predeterminados para el usuario. 

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que sólo persistirá mientras Braze actualice el segmento.


#### Paso 2.2: Permitir el acceso a las IP Braze    

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze. 

Puede que también tengas que cambiar tus grupos de seguridad para permitir el acceso de Braze a tus datos en Redshift. Asegúrate de permitir explícitamente el tráfico entrante en las IP indicadas a continuación y en el puerto utilizado para consultar tu clúster Redshift (predeterminado es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto, aunque las reglas de entrada estén configuradas como "permitir todo". Además, es importante que el punto final del clúster Redshift sea de acceso público para que Braze pueda conectarse a tu clúster.

Si no quieres que tu clúster de Redshift sea de acceso público, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel ssh para acceder a los datos de Redshift. Para más información, consulta [AWS: ¿Cómo accedo a un clúster privado de Amazon Redshift desde mi máquina local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Paso 2.1: Crear una cuenta de servicio y conceder permisos 

Crea una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de tu(s) tabla(s). La cuenta de servicio debe tener los siguientes permisos: 

- **Usuario de conexión a BigQuery:** Permite a Braze realizar conexiones.
- **Usuario de BigQuery:** Proporciona acceso Braze para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **Visor de datos BigQuery:** Proporciona acceso Braze para ver conjuntos de datos y su contenido.
- **Usuario de BigQuery Job:** Proporciona acceso Braze para ejecutar trabajos.
- **bigquery.tables.create** Proporciona acceso Braze para crear tablas temporales durante la actualización de segmentos.

Crea una cuenta de servicio para que la utilice tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI, y para consultar las tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. 

Puedes elegir conceder acceso a todas las tablas de un conjunto de datos, o conceder privilegios sólo a tablas concretas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en la Extensión de segmento CDI. 

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla sólo persistirá mientras Braze esté actualizando el segmento. 

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Para más información, consulta [Google Cloud: Crear y eliminar claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). Más tarde lo subirás al panel de Braze.

#### Paso 2.2: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Big Query. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Paso 2.1: Crear un token de acceso  

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **Configuración de usuario** en el desplegable.
2. Asegúrate de que la cuenta de servicio tiene privilegios `CREATE TABLE` en el esquema utilizado para la fuente conectada. 
3. En la pestaña **Tokens de acceso**, selecciona **Generar nuevo token**.
4. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la duración del token a sin duración dejando la casilla Duración (días) vacía (en blanco).
5. Selecciona **Generar**.
6. Copia el token mostrado y selecciona **Hecho**.

Este token se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI, y para consultar las tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. 

Puedes elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios sólo a tablas concretas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en la Extensión de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que sólo persistirá mientras Braze actualice el segmento. 

Guarda el token en un lugar seguro hasta que necesites introducirlo en el panel de Braze durante el paso de creación de credenciales.

#### Paso 2.2: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Paso 2.1: Conceder acceso a los recursos de Fabric 
Braze se conectará a tu almacén Fabric utilizando un principal de servicio con autenticación Entra ID. Crearás un nuevo principal de servicio para que lo utilice Braze, y concederás acceso a los recursos de Fabric según sea necesario. Braze necesitará los siguientes datos para conectarse:    

* Tenant ID (también llamado directorio) de tu cuenta Azure 
* ID de la entidad de seguridad (también llamado ID de aplicación) para la entidad de seguridad del servicio 
* Secreto de cliente para que Braze se autentique

1. En el portal de Azure, ve al centro de administración de Microsoft Entra y, a continuación, a **Registros de aplicaciones**.
2. Selecciona **\+ Nuevo registro** en **Identidad > Aplicaciones > Registros de aplicaciones** 
3. Introduce un nombre y selecciona `Accounts in this organizational directory only` como tipo de cuenta admitido. A continuación, selecciona **Registro**. 
4. Selecciona la aplicación (servicio principal) que acabas de crear y, a continuación, ve a **Certificados & secrets > + Nuevo secreto de cliente**
5. Introduce una descripción para el secreto y establece un periodo de caducidad para el secreto. Después, selecciona **Añadir**. 
6. Toma nota del secreto de cliente creado para utilizarlo en la configuración de Braze. 

{% alert note %}
Azure no permite la caducidad ilimitada de los secretos de principal de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos a Braze.
{% endalert %}

#### Paso 2.2: Conceder acceso a los recursos de Fabric 
Proporcionarás acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, ve a **Configuración** > **Gobierno e información** > **Portal de administración** > **Configuración de inquilinos**.    

* En la **configuración del desarrollador** habilita "Los principales del servicio pueden utilizar APIs de Fabric" para que Braze pueda conectarse utilizando Microsoft Entra ID.
* En la **configuración de OneLake** habilita "Los usuarios pueden acceder a los datos almacenados en OneLake con aplicaciones externas a Fabric" para que el principal del servicio pueda acceder a los datos de una aplicación externa.

#### Paso 2.3: Obtener cadena de conexión al almacén 

Necesitarás el punto final SQL de tu almacén para que Braze pueda conectarse. Para recuperar el punto final SQL, ve al **espacio de trabajo** en Fabric y, en la lista de elementos, pasa el ratón por encima del nombre del almacén y selecciona **Copiar cadena de conexión SQL**.

\![La página "Fabric Console" de Microsoft Azure, donde los usuarios deben recuperar la cadena de conexión SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Paso 2.4: Permitir IPs de Braze en el Cortafuegos (Opcional)

Dependiendo de la configuración de tu cuenta Microsoft Fabric, puede que tengas que permitir las siguientes direcciones IP en tu cortafuegos para permitir el tráfico desde Braze. Para más información sobre cómo habilitarlo, consulta la documentación correspondiente sobre el [Acceso Condicional Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 3: Crea una fuente conectada en el panel de Braze

{% tabs %}
{% tab Snowflake %}
#### Paso 3.1: Añadir información de conexión Snowflake y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Snowflake Importar**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu almacén de datos Snowflake y el esquema de origen, y pasa al siguiente paso.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Paso 3.2: Configurar los detalles de la sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI. 

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta Snowflake. 

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de la consulta o dedicar un almacén mayor al usuario de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Paso 3.3: Nota la clave pública  

En el paso **Probar conexión**, toma nota de la clave pública RSA. La necesitarás para completar la integración en Snowflake.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Paso 3.1: Añade la información de conexión a Redshift y la tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear conexión de datos** > **Importación de Amazon Redshift**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu almacén de datos Redshift y el esquema de origen, y pasa al siguiente paso.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Paso 3.2: Configurar los detalles de la sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI. 

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Redshift. 

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de la consulta o dedicar un almacén mayor al usuario de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Paso 3.3: Anota la clave pública (opcional)

Si tus credenciales tienen seleccionada la opción **Conectar con túnel SSH**, toma nota de la clave pública RSA en el paso **Probar conexión**. La necesitarás para completar la integración en Redshift.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Paso 3.1: Añade la información de conexión de BigQuery y la tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Importación de Google BigQuery**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu proyecto BigQuery y del conjunto de datos, y pasa al siguiente paso.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Paso 3.2: Configurar los detalles de la sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI. 

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta BigQuery. 

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de la consulta o dedicar un almacén mayor al usuario de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Probar conexión** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para usar en Extensiones de segmento CDI.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Paso 3.1: Añadir información de conexión Databricks y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Importación de Databricks**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tus credenciales Databricks y, opcionalmente, el catálogo y el esquema de origen, y pasa al siguiente paso.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Paso 3.2: Configurar los detalles de la sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI. 

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Databricks. 

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de la consulta o dedicar un almacén mayor al usuario de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Probar conexión** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para usar en Extensiones de segmento CDI.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Paso 3.1: Añadir información de conexión Microsoft Fabric y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Importar Microsoft Fabric**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tus credenciales de Microsoft Fabric, así como el almacén de origen y el esquema, y pasa al siguiente paso.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Paso 3.2: Configurar los detalles de la sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI. 

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta Microsoft Fabric. 

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de tus consultas o de ampliar la capacidad del Tejido.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Probar conexión** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para usar en Extensiones de segmento CDI.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Finaliza la configuración del almacén de datos

{% tabs %}
{% tab Snowflake %}
Añade la clave pública que has anotado en el último paso a tu usuario en Snowflake. Esto permitirá a Braze conectarse a Snowflake. Para saber cómo hacerlo, consulta [la documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

Si quieres rotar las claves en cualquier momento, puedes crear una nueva clave pública yendo a **Gestión de acceso a datos** en **la Ingesta de datos en la nube** y seleccionando **Generar nueva clave** para la cuenta correspondiente.

\![Gestión de acceso a datos para credenciales de acceso a datos Snowflake, con un botón para generar una nueva clave.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Después de añadir la clave al usuario en Snowflake, selecciona **Probar conexión** en Braze y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para usar en Extensiones de segmento CDI.
{% endtab %}

{% tab Redshift %}
Si te conectas con un túnel SSH, añade la clave pública que anotaste en el último paso al usuario del túnel SSH. 

Después de añadir la clave al usuario, selecciona **Probar conexión** en Braze y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para usar en Extensiones de segmento CDI.

{% endtab %}
{% tab BigQuery %}
Esto no se aplica a BigQuery.

{% endtab %}
{% tab Databricks %}
Esto no se aplica a los Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Esto no se aplica a Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una fuente antes de que pueda pasar del estado "borrador" al estado "activo". Si necesitas salir de la página de creación, tu integración se guardará y podrás volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Configuración de integraciones o usuarios adicionales (opcional)

{% tabs %}
{% tab Snowflake %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para conectar un esquema diferente. Al crear conexiones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake.

Si reutilizas el mismo usuario y función en distintas integraciones, no tendrás que volver a añadir la clave pública.
{% endtab %}

{% tab Redshift %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe estar configurada para conectar un esquema diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Redshift.
{% endtab %}

{% tab BigQuery %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe estar configurada para conectar un conjunto de datos diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.
{% endtab %}

{% tab Databricks %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe estar configurada para conectar un esquema diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe estar configurada para conectar un esquema diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Azure.
{% endtab %}
{% endtabs %}

## Utilizar la fuente conectada

Una vez creada la fuente, puedes utilizarla para crear una o varias extensiones de segmento CDI. Para más información sobre la creación de un segmento con esta fuente, consulta la [documentación Extensiones de segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de la consulta o dedicar más recursos de computación (como un almacén más grande) al usuario de Braze.
{% endalert %}
