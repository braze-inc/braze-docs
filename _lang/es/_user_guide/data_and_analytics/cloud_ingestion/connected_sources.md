---
nav_title: Fuentes conectadas
article_title: Fuentes conectadas
description: "Este artículo de referencia cubre cómo utilizar Braze Cloud Data Ingestion para sincronizar datos relevantes con su integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Fuentes conectadas

> Las fuentes conectadas son una alternativa de copia cero a la sincronización directa de datos con la función Cloud Data Ingestion (CDI) de Braze. Un origen conectado consulta directamente tu almacén de datos para crear nuevos segmentos sin copiar ninguno de los datos subyacentes a Braze. 

Después de añadir una fuente conectada a tu espacio de trabajo Braze, puedes crear un segmento CDI dentro de Extensiones de segmento. Los segmentos CDI te permiten escribir SQL que consulta directamente tu almacén de datos (utilizando los datos que allí están disponibles a través de tu Origen Conectado CDI), y crea y mantiene un grupo de usuarios a los que se puede dirigir dentro de Braze. 

Para más información sobre cómo crear un segmento con esta fuente, consulta [Segmentos CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert warning %}
Dado que las fuentes conectadas se ejecutan directamente en su almacén de datos, incurrirá en todos los costes asociados a la ejecución de estas consultas en su almacén de datos. Las fuentes conectadas no consumen puntos de datos, y los segmentos CDI no consumen créditos de segmentos SQL.
{% endalert %}

## Integración de fuentes conectadas

### Paso 1: Conecta tus recursos

Las fuentes conectadas a la ingesta de datos en la nube requieren cierta configuración en Braze y en tu instancia. Siga estos pasos para configurar la integración: algunos pasos se realizarán en el almacén de datos y otros en el panel Braze.

{% tabs %}
{% tab Snowflake %}
**En tu almacén de datos**
1. Crear un rol y otorgar permisos para consultar y crear tablas en un esquema.
2. Configure su almacén y dé acceso a ese rol.
3. Crea un usuario para ese rol.
4. Dependiendo de su configuración, puede que necesite permitir las IP Braze en su política de red Snowflake.

**En el panel de Braze**

{: start="5"}
5\. Crea una nueva fuente conectada en el panel de Braze.
6\. Configura los detalles de sincronización de la fuente conectada.
7\. Recupera la clave pública proporcionada en el panel de Braze.

**En tu almacén de datos**

{: start="8"}
8\. Añada la clave pública del panel Braze al [usuario Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Cuando hayas terminado, puedes utilizar la fuente conectada para crear uno o varios Segmentos CDI.
{% endtab %}

{% tab Redshift %}
1. Configure los datos de origen y los recursos necesarios en su entorno Redshift.
2. Crea una nueva fuente conectada en el panel de Braze.
4. Pruebe la integración.
5. Utilice la fuente conectada para crear uno o más segmentos CDI.
{% endtab %}

{% tab BigQuery %}
1. Configure los datos de origen y los recursos necesarios en su entorno BigQuery.
2. Cree una cuenta de servicio y permita el acceso a los proyectos de BigQuery y a los conjuntos de datos que contienen los datos que desea sincronizar.  
3. Crea una nueva fuente conectada en el panel de Braze.
4. Pruebe la integración.
5. Utilice la fuente conectada para crear uno o más segmentos CDI.
{% endtab %}

{% tab Databricks %}
1. Configura los datos de origen y los recursos necesarios en tu entorno Databricks.
2. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contienen los datos que deseas sincronizar.  
3. Crea una nueva fuente conectada en el panel de Braze.
4. Pruebe la integración.
5. Utilice la fuente conectada para crear uno o más segmentos CDI.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecte a instancias Classic y Pro SQL, lo que provocará retrasos durante la configuración y prueba de la conexión, así como durante la creación y actualización de segmentos CDI. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 2: Configure su almacén de datos

Configura los datos de origen y los recursos necesarios en tu entorno de almacén de datos. La fuente conectada puede hacer referencia a una o más tablas, así que asegúrate de que tu usuario de Braze tiene permiso para acceder a todas las tablas que quieras en la fuente conectada.

{% tabs %}
{% tab Snowflake %}
#### Paso 2.1: Crear un rol y conceder permisos

Crea un rol para que lo utilice tu fuente conectada. Este rol se utilizará para generar la lista de tablas disponibles en sus segmentos CDI, y para consultar tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente.

Puede elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios sólo a tablas específicas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en el segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta del segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla sólo persistirá mientras Braze esté actualizando el segmento.

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

#### Paso 2.2: Configura el almacén y da acceso al rol de Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén debe tener activada la bandera de **reanudación automática**. Si no lo está, tendrás que conceder a Braze privilegios adicionales de `OPERATE` en el almacén para que Braze lo active cuando llegue el momento de ejecutar la consulta.
{% endalert %}

#### Paso 2.3: Configura el usuario
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Compartirás la información de conexión con Braze y recibirás una clave pública para añadir al usuario en un paso posterior.

{% alert note %}
Cuando conecte diferentes espacios de trabajo a la misma cuenta Snowflake, debe crear un usuario único para cada espacio de trabajo Braze en el que esté creando una integración. Dentro de un espacio de trabajo, puede reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración fallará si un usuario de la misma cuenta Snowflake se duplica en todos los espacios de trabajo.
{% endalert %}

#### Paso 2.4: Permitir IPs Braze en tu política de red Snowflake (opcional)

Dependiendo de la configuración de su cuenta Snowflake, puede que necesite permitir las siguientes direcciones IP en su política de red Snowflake. Para más información sobre cómo hacerlo, consulta la documentación correspondiente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% subtabs %}
{% subtab United States (US) %}
Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, éstas son las direcciones IP correspondientes:
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Para las instancias `EU-01` y `EU-02`, estas son las direcciones IP correspondientes:
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Redshift %}
#### Paso 2.1: Crear usuario y conceder permisos 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crea un usuario para que lo utilice tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en sus segmentos CDI, y para consultar las tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. Si crea varias integraciones CDI, puede que desee conceder permisos a un esquema o gestionar los permisos mediante un grupo. 

Puede elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios sólo a tablas específicas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en el segmento CDI. Asegúrate de conceder acceso a las nuevas tablas al usuario cuando se creen, o establece permisos por defecto para el usuario. 

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que sólo persistirá mientras Braze actualice el segmento.


#### Paso 2.2: Permitir el acceso a las IP Braze    

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Permita el acceso desde las siguientes IP correspondientes a la región de su panel de control Braze. 

Es posible que también tenga que cambiar sus grupos de seguridad para permitir el acceso de Braze a sus datos en Redshift. Asegúrese de permitir explícitamente el tráfico entrante en las IP indicadas a continuación y en el puerto utilizado para consultar su clúster Redshift (por defecto es 5439). Debe permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas para "permitir todo". Además, es importante que el punto final del clúster Redshift sea de acceso público para que Braze pueda conectarse a tu clúster.

Si no quieres que tu clúster de Redshift sea de acceso público, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel ssh para acceder a los datos de Redshift. Para más información, consulta [AWS: ¿Cómo accedo a un clúster privado de Amazon Redshift desde mi máquina local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% subtabs %}
{% subtab United States (US) %}
Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, éstas son las direcciones IP correspondientes:
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Para las instancias `EU-01` y `EU-02`, estas son las direcciones IP correspondientes:
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}
#### Paso 2.1: Crear una cuenta de servicio y conceder permisos 

Cree una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de su(s) tabla(s). La cuenta de servicio debe tener los siguientes permisos: 

- **Usuario de conexión BigQuery:** Permite a Braze realizar conexiones.
- **Usuario de BigQuery:** Proporciona acceso Braze para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **Visor de datos BigQuery:** Proporciona acceso Braze para ver conjuntos de datos y su contenido.
- **Usuario de BigQuery Job:** Proporciona acceso Braze para ejecutar trabajos.
- **bigquery.tables.create** Proporciona acceso Braze para crear tablas temporales durante la actualización de segmentos.

Crea una cuenta de servicio para que la utilice tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en sus segmentos CDI, y para consultar las tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. 

Puede optar por conceder acceso a todas las tablas de un conjunto de datos, o conceder privilegios sólo a tablas específicas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en el segmento CDI. 

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta del segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla sólo persistirá mientras Braze esté actualizando el segmento. 

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Para más información, consulta [Google Cloud: Creación y eliminación de claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). Más tarde lo cargarás en el panel de control de Braze.

#### Paso 2.2: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de BigQuery. Permita el acceso desde las siguientes IP correspondientes a la región de su panel de control Braze.  

{% subtabs %}
{% subtab United States (US) %}
Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, éstas son las direcciones IP correspondientes:
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Para las instancias `EU-01` y `EU-02`, estas son las direcciones IP correspondientes:
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Databricks %}
#### Paso 2.1: Crear un token de acceso  

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **Configuración de usuario** en el desplegable.
2. Asegúrate de que la cuenta de servicio tiene privilegios `CREATE TABLE` en el esquema utilizado para la fuente conectada. 
3. En la pestaña **Tokens de acceso**, selecciona **Generar nuevo token**.
4. Introduzca un comentario que le ayude a identificar este token, como "Braze CDI", y cambie la vida útil del token a sin vida útil dejando la casilla Vida útil (días) vacía (en blanco).
5. Seleccione **Generar**.
6. Copie el token mostrado y seleccione **Hecho**.

Este token se utilizará para generar la lista de tablas disponibles en sus segmentos CDI, y para consultar tablas de origen para crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. 

Puede elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios sólo a tablas específicas. Las tablas a las que tenga acceso el rol Braze estarán disponibles para su consulta en el segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que sólo persistirá mientras Braze actualice el segmento. 

Guarde el token en un lugar seguro hasta que necesite introducirlo en el panel de control de Braze durante el paso de creación de credenciales.

#### Paso 2.2: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Databricks. Permita el acceso desde las siguientes IP correspondientes a la región de su panel de control Braze.  

{% subtabs %}
{% subtab United States (US) %}
Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, éstas son las direcciones IP correspondientes:
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Para las instancias `EU-01` y `EU-02`, estas son las direcciones IP correspondientes:
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 3: Crea una fuente conectada en el panel de Braze

{% tabs %}
{% tab Snowflake %}
#### Paso 3.1: Añadir información de conexión Snowflake y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Snowflake Importar**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu almacén de datos Snowflake y el esquema de origen, y pasa al siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Paso 3.2: Configurar los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees un nuevo segmento CDI. 

Configure un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta Snowflake. 

{% alert note %}
Si las consultas se demoran constantemente y ha establecido un tiempo de ejecución máximo de 60 minutos, considere la posibilidad de intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Paso 3.3: Tenga en cuenta la clave pública  

En el paso **Probar conexión**, toma nota de la clave pública RSA. La necesitarás para completar la integración en Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Paso 3.1: Añadir información de conexión Redshift y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear conexión de datos** > **Importación de Amazon Redshift**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu almacén de datos Redshift y el esquema de origen, y pasa al siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Paso 3.2: Configurar los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees un nuevo segmento CDI. 

Configure un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Redshift. 

{% alert note %}
Si las consultas se demoran constantemente y ha establecido un tiempo de ejecución máximo de 60 minutos, considere la posibilidad de intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Paso 3.3: Anota la clave pública (opcional)

Si tus credenciales tienen seleccionada la opción **Conectar con túnel SSH**, toma nota de la clave pública RSA en el paso **Probar conexión**. Lo necesitarás para completar la integración en Redshift.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Paso 3.1: Añadir información de conexión BigQuery y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Importación de Google BigQuery**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu proyecto BigQuery y del conjunto de datos, y pasa al siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Paso 3.2: Configurar los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees un nuevo segmento CDI. 

Configure un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta BigQuery. 

{% alert note %}
Si las consultas se demoran constantemente y ha establecido un tiempo de ejecución máximo de 60 minutos, considere la posibilidad de intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Probar conexión** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para ser utilizada en segmentos CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Paso 3.1: Añadir información de conexión Databricks y tabla de origen

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Importación de Databricks**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tus credenciales Databricks y, opcionalmente, el catálogo y el esquema de origen, y pasa al siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Paso 3.2: Configurar los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees un nuevo segmento CDI. 

Configure un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Databricks. 

{% alert note %}
Si las consultas se demoran constantemente y ha establecido un tiempo de ejecución máximo de 60 minutos, considere la posibilidad de intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Probar conexión** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para ser utilizada en segmentos CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Finalizar la configuración del almacén de datos

{% tabs %}
{% tab Snowflake %}
Añade la clave pública que anotaste en el último paso a tu usuario en Snowflake. Esto permitirá a Braze conectarse a Snowflake. Para saber cómo hacerlo, consulta [la documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

Si quieres rotar las claves en cualquier momento, puedes crear una nueva clave pública yendo a **Gestión de acceso a datos** en **la Ingesta de datos en la nube** y seleccionando **Generar nueva clave** para la cuenta correspondiente.

![Gestión de acceso a datos para credenciales de acceso a datos Snowflake, con un botón para generar una nueva clave.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Después de añadir la clave al usuario en Snowflake, selecciona **Probar conexión** en Braze y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para ser utilizada en segmentos CDI.
{% endtab %}

{% tab Redshift %}
Si te conectas con un túnel SSH, añade la clave pública que anotaste en el último paso al usuario del túnel SSH. 

Después de añadir la clave al usuario, selecciona **Probar conexión** en Braze y, a continuación, selecciona **Hecho**. Tu fuente conectada ya está creada y lista para ser utilizada en segmentos CDI.

{% endtab %}
{% tab BigQuery %}
Esto no se aplica a BigQuery.

{% endtab %}
{% tab Databricks %}
Esto no se aplica a los Databricks.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una fuente antes de que pueda pasar del estado "borrador" al estado "activo". Si necesita salir de la página de creación, su integración se guardará y podrá volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Configuración de integraciones o usuarios adicionales (opcional)

{% tabs %}
{% tab Snowflake %}
Puede configurar varias integraciones con Braze, pero cada integración debe configurarse para conectar un esquema diferente. Al crear conexiones adicionales, puede reutilizar las credenciales existentes si se conecta a la misma cuenta Snowflake.

Si reutilizas el mismo usuario y función en distintas integraciones, no tendrás que volver a añadir la clave pública.
{% endtab %}

{% tab Redshift %}
Puede configurar varias fuentes con Braze, pero cada fuente debe configurarse para conectar un esquema diferente. Al crear fuentes adicionales, puede reutilizar las credenciales existentes si se conecta a la misma cuenta de Redshift.
{% endtab %}

{% tab BigQuery %}
Puede configurar varias fuentes con Braze, pero cada fuente debe estar configurada para conectar un conjunto de datos diferente. Al crear fuentes adicionales, puede reutilizar las credenciales existentes si se conecta a la misma cuenta de BigQuery.
{% endtab %}

{% tab Databricks %}
Puede configurar varias fuentes con Braze, pero cada fuente debe configurarse para conectar un esquema diferente. Al crear fuentes adicionales, puede reutilizar las credenciales existentes si se conecta a la misma cuenta de Databricks.
{% endtab %}
{% endtabs %}

## Utilizar la fuente conectada

Una vez creada la fuente, puede utilizarse para crear uno o varios segmentos CDI. Para más información sobre la creación de un segmento con esta fuente, consulte la [documentación de Segmentos CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera la posibilidad de intentar optimizar el tiempo de ejecución de la consulta o dedicar más recursos de computación (como un almacén más grande) al usuario de Braze.
{% endalert %}
