---
nav_title: Cómo utiliza Braze Currents
article_title: Cómo utiliza Braze Currents
page_order: 6
page_type: tutorial
description: "Este artículo práctico de Currents te guiará por el proceso básico para configurar las entradas adecuadas para los datos de eventos, así como para trasladarlos a una base de datos y a una herramienta de inteligencia empresarial (BI)."
tool: Currents
 
---

# Cómo utiliza Braze Currents

> ¡Braze utiliza Currents! Así es, nos gusta nuestro propio producto lo suficiente como para utilizarlo junto con algunos de [nuestros socios]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/).

Filtramos los datos de nuestras campañas de correo electrónico y push en una herramienta de información empresarial, Looker, pero hay que recorrer un interesante camino para llegar a ella. Utilizamos una versión ligeramente invertida de la metodología Extraer, Transformar, Cargar (ETL): ¡simplemente cambiamos el orden a Extraer, Cargar, Transformar (ELT)!

## Paso 1: Datos de admisión y de eventos agregados

Después de lanzar campañas utilizando cualquiera de nuestras herramientas de interacción (como campañas o Canvas), hacemos un seguimiento de los datos del evento utilizando nuestro propio sistema, así como algunos de nuestros socios de correo electrónico. Algunos de estos datos se agregan y se muestran en el panel, ¡pero nos interesa profundizar más!

## Paso 2: Enviar datos de eventos a un socio de almacenamiento de datos

Configuramos Currents para que envíe los datos de eventos de Braze a Amazon S3 para su almacenamiento y extracción. Ahora bien, sabemos que puedes utilizar [Athena](https://aws.amazon.com/athena/) para sentarte encima de S3 y ejecutar consultas. Es una gran solución a corto plazo. Pero queríamos una solución a largo plazo utilizando una base de datos relacional y una herramienta de inteligencia empresarial/análisis. (Te recomendamos que hagas lo mismo).

¡Consideramos el S3 como nuestras llaves del castillo! Abre la puerta a tantas posibilidades de mover, pivotar y analizar nuestros datos transfiriéndolos donde necesitemos que vayan. Sin embargo, tenemos cuidado de no transformar nuestros datos en S3, ya que tenemos una estructura muy específica para ellos.

## Paso 3: Transformar datos de eventos con una base de datos relacional

Desde S3, elegimos un almacén[(Snow](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) flake[Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) o Snowflake Reader Accounts, en nuestro caso). Lo transformamos allí y luego lo trasladamos a Looker, donde tenemos bloques configurados que estructurarán y organizarán nuestros datos.

Snowflake no es la única opción de almacén. Otras opciones son [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), ¡y muchas más!

### Cuentas de lector Snowflake

Las cuentas de Snowflake Reader ofrecen a los usuarios acceso a los mismos datos y funcionalidades que [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), todo ello sin necesidad de tener una cuenta Snowflake o una relación de cliente con Snowflake. Con las Cuentas de Lector, Braze creará y compartirá tus datos en una cuenta y te proporcionará credenciales para iniciar sesión y acceder a tus datos. De este modo, todos los datos compartidos y la facturación por uso serán gestionados íntegramente por Braze. 

Para más información, ponte en contacto con tu administrador del éxito del cliente.

#### Recursos adicionales
Para obtener recursos útiles de supervisión del uso, consulta los artículos de Snowflake [Monitores de recursos](https://docs.snowflake.com/en/user-guide/resource-monitors.html) y [Ver el uso del crédito del almacén](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Paso 4: Utiliza una herramienta de inteligencia empresarial (BI) para manipular tus datos

Por último, utilizamos una herramienta de BI para analizar nuestros datos, convertirlos en gráficos y otras herramientas visuales, y más utilizando [Looker y bloques de Looker](https://www.marketplace.looker.com/) para no tener que ETL o ELT los datos cada vez que se mueven desde Currents.

¿Te sientes inspirado para hacer lo mismo? Consulta los siguientes documentos para obtener más información sobre ellos y cómo puedes utilizarlos para crear tu base de datos.

- [Bloque Comportamiento del usuario](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloque de interacción de mensajes](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

