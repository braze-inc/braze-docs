> Aprende a utilizar el Generador de consultas, para que puedas generar informes utilizando datos Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL predefinidas para empezar, o bien puede escribir sus propias consultas SQL personalizadas para obtener aún más información.

## Requisitos previos

Necesitarás [ permisos de "Ver PII]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) " para utilizar el Generador de consultas, ya que permite acceder directamente a algunos datos de clientes.

## Utilizar el Generador de consultas

### Paso 1: Crear una consulta SQL

Para crear una nueva consulta, ve a **Análisis** > **Generador de consultas** y, a continuación, selecciona **Crear consulta SQL**.

![Las opciones "Plantilla de consulta" y "Editor SQL" que se encuentran dentro del desplegable "Crear consulta SQL".]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Si necesitas inspiración o ayuda para elaborar tu consulta, elige **Plantilla de consulta** y selecciona una [plantilla prefabricada]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/). Para empezar con una consulta en blanco, selecciona **Editor SQL**.

Su informe recibe automáticamente un nombre con la fecha y hora actuales. Pase el ratón por encima del nombre y seleccione <i class="fas fa-pencil" alt="Edit"></i> para dar un nombre significativo a su consulta SQL.

![Un ejemplo de nombre de informe "Interacción con el canal para mayo de 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Paso 2: Construye tu consulta

Cuando construyas tu consulta, puedes optar por obtener ayuda de la IA o construirla por tu cuenta.

{% tabs local %}
{% tab Uso de BrazeAI %}
El Generador de consultas con IA aprovecha [la GPT](https://openai.com/gpt-4), impulsada por OpenAI, para recomendar SQL para tu consulta. Generar SQL con el Generador de consultas con IA

1. Tras crear un informe en el Generador de consultas, selecciona la pestaña **Generador de consultas con IA**.
2. Escriba su consulta o seleccione una consulta de ejemplo y seleccione **Generar** para traducir su consulta a SQL.
3. Revise el SQL generado para asegurarse de que parece correcto y, a continuación, seleccione **Insertar en el editor**.

![El constructor de consultas SQL AI.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Consejos

- Familiarícese con las [tablas de datos Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esta característica. El incumplimiento de estas normas provocará un error.
- Puedes enviar hasta 20 consultas por minuto con el Generador de Consultas con IA.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Por mi cuenta %}
Escriba su consulta SQL utilizando [la sintaxis Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte la [referencia de la tabla]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obtener una lista completa de las tablas y columnas disponibles para su consulta.

Para ver los detalles de la tabla en el Generador de consultas:

1. En la página **Generador de consultas**, abra el panel **Referencia** y seleccione **Tablas de datos disponibles** para ver las tablas de datos disponibles y sus nombres.
3. Seleccione <i class="fas fa-chevron-down" alt=""></i> **Ver detalles** para ver la descripción de la tabla e información sobre las columnas de la tabla, como los tipos de datos.
4. Para insertar el nombre de la tabla en su SQL, seleccione <i class="fas fa-copy" title="Copiar nombre de tabla al editor SQL"></i>.

Restringir su consulta a un periodo de tiempo específico le ayudará a generar resultados más rápidamente. A continuación se muestra un ejemplo de consulta que obtiene el número de compras y los ingresos generados durante la última hora.

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

Si consultas por las columnas `CANVAS_ID`, `CANVAS_VARIATION_API_ID`, o `CAMPAIGN_ID`, sus nombres asociados se incluirán automáticamente en la tabla de resultados. No es necesario que los incluyas en la propia consulta `SELECT`.

| Nombre ID | Columna de nombre asociado |
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

Su consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en la consulta SQL
- Tiempo de espera de procesamiento (después de 6 minutos)
    - Los informes que tarden más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si se agota el tiempo de espera de un informe, intente limitar el intervalo de tiempo en el que consulta los datos o consulte un conjunto de datos más específico.
{% endtab %}
{% endtabs %}

### Paso 3: Genera tu informe

Cuando hayas terminado de crear la consulta, selecciona **Ejecutar consulta**. Si no hay errores ni [se agota el tiempo de informe](#report-timeouts), se generará un archivo CSV a partir de la consulta.

Para descargar el informe CSV, selecciona **Exportar**.

![Generador de consultas que muestra los resultados de la consulta con plantilla "Interacción e ingresos del canal en los últimos 30 días".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Cada informe sólo puede generar resultados una vez al día. Si ejecutas el mismo informe varias veces en un mismo día del calendario, verás los mismos resultados en cada informe.
{% endalert %}

## Informar de tiempos muertos

Los informes que tarden más de seis minutos en ejecutarse agotarán el tiempo de espera. Si se trata de la primera consulta que ejecutas desde hace tiempo, puede tardar más en procesarse y, por tanto, es más probable que se agote el tiempo de espera. Si esto ocurre, intente ejecutar el informe de nuevo.

Si tu informe sigue sin recibir respuesta tras varios intentos, [ponte en contacto con el servicio de asistencia]({{site.baseurl}}/help/support#braze-support).

## Datos y resultados

Todas las consultas muestran datos de los últimos 60 días. Cuando exportes tus resultados, sólo contendrá hasta 1.000 filas. Para los informes que requieren mayores cantidades de datos, puedes utilizar herramientas como [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) o el [punto final de la API de exportación]({{site.baseurl}}/api/endpoints/export).

## Créditos de Snowflake

Cada empresa dispone de 5 créditos Snowflake al mes, compartidos en todos los espacios de trabajo. Cada vez que se ejecuta una consulta o se previsualiza una tabla, se utiliza una pequeña parte de un crédito Snowflake.

{% alert note %}
Los créditos copo de nieve no se comparten entre funciones. Por ejemplo, los créditos de las extensiones de segmentos SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de su consulta SQL. Cuanto mayor sea el tiempo de ejecución, mayor será la parte del crédito Snowflake que costará una consulta. El tiempo de ejecución puede variar en función de la complejidad y el tamaño de las consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas, mayor será la asignación de recursos y más rápido el tiempo de ejecución.

Los créditos no se utilizan al escribir, editar o guardar informes dentro del editor Braze SQL. Tus créditos volverán a ser 5 el primer día de cada mes a las 12 am UTC. Puede controlar el uso mensual de su crédito en la parte superior de la página del Generador de consultas.

![Generador de consultas que muestra la cantidad de créditos utilizados en el mes actual.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Cuando alcances el límite de crédito, no podrás ejecutar consultas, pero podrás crear, editar y guardar informes SQL. Si desea adquirir más créditos del Generador de consultas, póngase en contacto con su gestor de cuenta.
