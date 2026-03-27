> Aprende a utilizar el Generador de consultas, para que puedas generar informes utilizando datos de Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL predefinidas para empezar, o puedes escribir tus propias consultas SQL personalizadas para obtener aún más información.

## Requisitos previos

Necesitarás [permisos de "Ver PII"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) para utilizar el Generador de consultas, ya que permite acceder directamente a algunos datos de clientes.

## Utilizar el Generador de consultas

### Paso 1: Crear una consulta SQL

Para crear una nueva consulta, ve a **Análisis** > **Generador de consultas** y, a continuación, selecciona **Crear consulta SQL**.

![Las opciones "Plantilla de consulta" y "Editor SQL" que se encuentran dentro del desplegable "Crear consulta SQL".]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Si necesitas inspiración o ayuda para elaborar tu consulta, elige **Plantilla de consulta** y selecciona una [plantilla prefabricada]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/). Para empezar con una consulta en blanco, selecciona **Editor SQL**.

Tu informe recibe automáticamente un nombre con la fecha y hora actuales. Pasa el ratón por encima del nombre y selecciona <i class="fas fa-pencil" alt="Edit"></i> para dar un nombre significativo a tu consulta SQL.

![Un ejemplo de informe con el nombre "Interacción del canal para mayo de 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Paso 2: Construye tu consulta

Cuando construyas tu consulta, puedes optar por obtener ayuda de la IA o construirla por tu cuenta.

{% tabs local %}
{% tab Using BrazeAI %}
El Generador de consultas con IA aprovecha [GPT](https://openai.com/gpt-4), impulsado por OpenAI, para recomendar SQL para tu consulta. Para generar SQL con el Generador de consultas con IA:

1. Tras crear un informe en el Generador de consultas, selecciona la pestaña **Generador de consultas con IA**.
2. Escribe tu prompt o selecciona un prompt de ejemplo y selecciona **Generar** para traducir tu prompt a SQL.
3. Revisa el SQL generado para asegurarte de que parece correcto y, a continuación, selecciona **Insertar en el editor**.

![El generador de consultas SQL con IA.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Consejos

- Familiarízate con las [tablas de datos de Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esta característica. El incumplimiento de estas reglas provocará un error.
- Puedes enviar hasta 20 prompts por minuto con el Generador de consultas con IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab On My Own %}
Escribe tu consulta SQL utilizando [la sintaxis de Snowflake](https://docs.snowflake.com/en/sql-reference). Consulta la [referencia de tablas]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obtener una lista completa de las tablas y columnas disponibles para consultar.

Para ver los detalles de la tabla en el Generador de consultas:

1. Desde la página **Generador de consultas**, abre el panel **Referencia** y selecciona **Tablas de datos disponibles** para ver las tablas de datos disponibles y sus nombres.
3. Selecciona <i class="fas fa-chevron-down" alt=""></i> **Ver detalles** para ver la descripción de la tabla e información sobre las columnas de la tabla, como los tipos de datos.
4. Para insertar el nombre de la tabla en tu SQL, selecciona <i class="fas fa-copy" title="Copy table name to SQL editor"></i>.

Restringir tu consulta a un periodo de tiempo específico te ayudará a generar resultados más rápidamente. A continuación se muestra un ejemplo de consulta que obtiene el número de compras y los ingresos generados durante la última hora.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Esta consulta recupera el número de envíos de correo electrónico en el último mes:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Si consultas por `CANVAS_ID`, `CANVAS_VARIATION_API_ID` o `CAMPAIGN_ID`, sus columnas de nombre asociadas se incluirán automáticamente en la tabla de resultados. No es necesario que las incluyas en la propia consulta `SELECT`.

| Nombre del ID | Columna de nombre asociado |
| --- | --- |
| `CANVAS_ID` | Nombre del Canvas |
| `CANVAS_VARIATION_API_ID` | Nombre de la variante en Canvas |
| `CAMPAIGN_ID` | Nombre de la campaña |
{: .reset-td-br-1 .reset-td-br-2 }

Esta consulta recupera los tres ID y sus columnas de nombre asociadas con un máximo de 100 filas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

#### Solución de problemas

Tu consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en la consulta SQL
- Tiempo de espera de procesamiento (después de 6 minutos)
    - Los informes que tarden más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si se agota el tiempo de espera de un informe, intenta limitar el intervalo de tiempo en el que consultas los datos o consulta un conjunto de datos más específico.
{% endtab %}
{% endtabs %}

### Paso 3: Genera tu informe

Cuando hayas terminado de crear la consulta, selecciona **Ejecutar consulta**. Si no hay errores ni [tiempos de espera del informe](#report-timeouts), se generará un archivo CSV a partir de la consulta.

Para descargar el informe CSV, selecciona **Exportar**.

![Generador de consultas que muestra los resultados de la consulta con plantilla "Interacción e ingresos del canal en los últimos 30 días".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Cada informe solo puede generar resultados una vez al día. Si ejecutas el mismo informe varias veces en un mismo día del calendario, verás los mismos resultados en cada informe.
{% endalert %}

## Tiempos de espera del informe

Los informes que tarden más de seis minutos en ejecutarse agotarán el tiempo de espera. Si se trata de la primera consulta que ejecutas desde hace tiempo, puede tardar más en procesarse y, por tanto, es más probable que se agote el tiempo de espera. Si esto ocurre, intenta ejecutar el informe de nuevo.

Si tu informe sigue agotando el tiempo de espera tras varios intentos, [ponte en contacto con Soporte]({{site.baseurl}}/help/support#braze-support).

## Consultar motivos de cancelación

Puedes consultar la columna `ABORT_TYPE` en cualquier tabla `USERS_MESSAGES_*_ABORT_SHARED` para analizar por qué no se enviaron los mensajes. El campo `ABORT_TYPE` contiene un valor de cadena que describe el motivo específico de la cancelación, y el campo complementario `ABORT_LOG` contiene detalles adicionales (como la regla de limitación de frecuencia que se desencadenó).

Por ejemplo, para contar las cancelaciones de correo electrónico por tipo en los últimos 30 días:

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Para ver la lista completa de valores de `ABORT_TYPE` y sus descripciones, consulta [Tipos de cancelación]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/#abort-types).

## Datos y resultados

Todas las consultas muestran datos de los últimos 60 días. Cuando exportes tus resultados, solo contendrán hasta 1000 filas. Para los informes que requieren mayores cantidades de datos, puedes utilizar herramientas como [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) o el [punto de conexión de la API de exportación]({{site.baseurl}}/api/endpoints/export).

## Créditos de Snowflake

Cada empresa dispone de 5 créditos de Snowflake al mes, compartidos en todos los espacios de trabajo. Cada vez que ejecutas una consulta o previsualizas una tabla, se utiliza una pequeña parte de un crédito de Snowflake.

{% alert note %}
Los créditos de Snowflake no se comparten entre características. Por ejemplo, los créditos de las extensiones de segmento SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de tu consulta SQL. Cuanto mayor sea el tiempo de ejecución, mayor será la parte del crédito de Snowflake que costará una consulta. El tiempo de ejecución puede variar en función de la complejidad y el tamaño de tus consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas que ejecutes, mayor será la asignación de recursos y más rápido será el tiempo de ejecución.

Los créditos no se utilizan al escribir, editar o guardar informes dentro del editor SQL de Braze. Tus créditos volverán a ser 5 el primer día de cada mes a las 12 am UTC. Puedes controlar el uso mensual de tus créditos en la parte superior de la página del Generador de consultas.

![Generador de consultas que muestra la cantidad de créditos utilizados en el mes en curso.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Cuando alcances el límite de créditos, no podrás ejecutar consultas, pero podrás crear, editar y guardar informes SQL. Si deseas adquirir más créditos del Generador de consultas, ponte en contacto con tu director de cuentas.