---
nav_title: "Extensiones de segmentos SQL"
article_title: Extensiones de segmentos SQL
alias: "/sql_segments/"
page_order: 3.2

page_type: reference
description: "Este artículo describe cómo crear una Extensión de Segmento SQL utilizando consultas Snowflake."
tool: Segments
---

# Extensiones de segmentos SQL

> Puede generar una Extensión de Segmento utilizando consultas SQL Snowflake de datos [Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/). SQL puede ayudarle a desbloquear nuevos casos de uso de los segmentos, ya que ofrece la flexibilidad necesaria para describir las relaciones entre los datos de formas que no son posibles con otras funciones de segmentación.

Al igual que las extensiones de segmento estándar, puede consultar eventos de hasta los dos últimos años (730 días) en su extensión de segmento SQL.

## Tipos de extensiones de segmentos SQL

Hay dos tipos de editores SQL entre los que puedes elegir para crear tu Extensión de Segmento SQL: el Editor SQL y el Editor SQL Incremental.

- **Creación de extensiones con el Editor SQL (actualización completa):** Cada vez que se actualice su segmento, Braze consultará todos los datos disponibles para actualizarlo, lo que consumirá más créditos que las actualizaciones incrementales. Las extensiones de actualización completa pueden regenerar automáticamente la afiliación a diario, pero no pueden actualizarse mediante la actualización incremental.
- **Creación de extensiones con el Editor SQL incremental (actualización incremental):** La actualización incremental sólo calcula los datos de los dos últimos días, lo que resulta más rentable y consume menos créditos cada vez. Al crear un segmento SQL de actualización incremental, puede configurarlo para que regenere automáticamente la afiliación diariamente. <br><br>La principal ventaja de las extensiones con actualización incremental es que puedes configurar tu segmento para que se actualice automáticamente a diario. Los segmentos creados con nuestro editor SQL normal sólo pueden actualizar sus miembros manualmente. Esto ayuda a reducir el coste de una actualización diaria de datos para las extensiones de segmentos SQL.

{% alert tip %}
Puede realizar una actualización manual completa de todos los segmentos SQL creados en cualquiera de los dos editores SQL.
{% endalert %}

## Creación de extensiones de segmentos SQL

{% tabs local %}
{% tab Actualización completa %}

Para crear una extensión de segmento SQL de actualización completa:

1. Vaya a **Audiencia** > **Extensiones de segmento**.
2. Haga clic en **Crear nueva extensión** y seleccione **Actualización completa**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Añada un nombre para su Extensión de Segmento e introduzca su SQL. Consulte la sección [Escribir SQL](#writing-sql) para conocer los requisitos y recursos.<br><br>
   ![Editor SQL que muestra un ejemplo de extensión de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Guarda tu extensión de segmento.

{% endtab %}
{% tab Actualización incremental %}

El editor SQL de actualización incremental permite al usuario realizar agregaciones de consultas por fecha para un evento dentro de un marco temporal determinado. Para crear una actualización incremental Extensión de segmento SQL:

1. Vaya a **Audiencia** > **Extensiones de segmento**.
{% alert note %}

Si está utilizando la [navegación antigua]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), puede encontrar esta página en **Compromiso** > **Segmentos** > **Extensiones de segmento**.
{% endalert %}

{:start="2"}
2\. Haga clic en **Crear nueva extensión** y seleccione **Actualización incremental**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\. Añada un nombre para su Extensión de Segmento e introduzca su SQL. Consulte la sección [Escribir SQL](#writing-sql) para conocer los requisitos y recursos.<br><br>
   ![Editor SQL que muestra un ejemplo de extensión de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4\. Si lo desea, seleccione **Regenerar extensión diariamente**.<br><br>
   ![Casilla de verificación para regenerar la extensión diariamente.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Si se selecciona esta opción, Braze actualizará automáticamente cada día el número de miembros del segmento. Esto significa que cada día a medianoche en la zona horaria de su empresa (con un retraso potencial de una hora), Braze comprobará si hay nuevos usuarios en su segmento y los añadirá automáticamente a su segmento. Si una Extensión de Segmento no se ha utilizado en 7 días, Braze pausará automáticamente la regeneración diaria. Una Extensión de Segmento no utilizada es aquella que no forma parte de una campaña o Lienzo (no es necesario que la campaña o el Lienzo estén activos para que la extensión se considere "utilizada").<br><br>
5\. Guarda tu extensión de segmento.

{% endtab %}

{% tab Generador de SQL con IA %}

{% alert note %}
El generador de SQL con IA está disponible actualmente como característica beta. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en esta prueba beta.
{% endalert %}

El generador de SQL con IA aprovecha [la GPT](https://openai.com/gpt-4), impulsada por OpenAI, para recomendar SQL para tu segmento SQL.

![Generador de SQL con IA con la pregunta "Usuarios que recibieron una notificación el mes pasado"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Para utilizar el generador de SQL con IA, haz lo siguiente:

1. Haga clic en **Launch AI SQL Generator** después de crear un [segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) utilizando la actualización completa o incremental.
2. Escriba su consulta y haga clic en **Generar** para traducir su consulta a SQL.
3. Revisa el SQL generado para asegurarte de que parece correcto y, a continuación, guarda tu segmento.

### Ejemplos de indicaciones
- Usuarios que recibieron un correo electrónico en el último mes
- Usuarios que realizaron menos de cinco compras en el último año

### Consejos
- Familiarícese con las [tablas de datos Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para esta característica. El incumplimiento de estas normas provocará un error. Por ejemplo, tu código SQL debe seleccionar la columna `user_id`. Empezar tu pregunta con "usuarios que" puede ayudar.
- Puedes enviar hasta 20 consultas por minuto con el generador de SQL con IA.

### ¿Cómo se utilizan y envían mis datos a OpenAI?

Para generar tu SQL, Braze enviará tus solicitudes a la Plataforma API de OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que usted incluya información identificable de forma única en el contenido que proporcione. Como se detalla en [los Compromisos de la Plataforma API de OpenAI](https://openai.com/policies/api-data-usage-policies), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Asegúrate de que cumples las políticas de OpenAI relevantes para ti, incluida la [Política de uso](https://openai.com/policies/usage-policies). Braze no ofrece garantías de ningún tipo con respecto a los contenidos generados por IA.
{% endtab %}
{% endtabs %}

{% alert note %}
Las consultas SQL que tarden más de 20 minutos en ejecutarse agotarán el tiempo de espera.
{% endalert %}

Cuando la extensión termine de procesarse, puede [crear un segmento][4] utilizando su Extensión de Segmento y apuntar a este nuevo segmento con sus campañas y Canvases.

## Escribir SQL

Su consulta SQL debe escribirse utilizando [la sintaxis Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consulte la [referencia de la tabla]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obtener una lista completa de las tablas y columnas disponibles para su consulta.

{% alert important %}
Nota que las tablas disponibles para consulta solo contienen datos de eventos. Si desea consultar los atributos de los usuarios, deberá combinar su segmento SQL con filtros de atributos personalizados del [segmentador clásico]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
{% endalert %} 

{% tabs %}
{% tab Editor SQL %}

Además, su SQL debe cumplir las siguientes normas:

- Escriba una única sentencia SQL. No incluya ningún punto y coma.
- Su SQL debe seleccionar sólo una columna: la columna `user_id`. Esto significa que su SQL debe contener:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- No es posible consultar usuarios con cero eventos, lo que significa que cualquier consulta de usuarios que hayan realizado un evento menos de X veces tendría que seguir esta solución:
   1. Escriba una consulta para seleccionar los usuarios que tienen el evento MÁS de X veces.
   2. Cuando haga referencia a su Extensión de segmento en su segmento, seleccione `doesn't include` para invertir el resultado.

{% endtab %}
{% tab Editor SQL incremental %}

Todas las consultas de actualización incremental constan de dos partes: una consulta y los detalles del esquema.

1. En el editor, escriba una consulta que seleccione `user_id`s de la tabla que desee.
2. Añada detalles del esquema seleccionando un **Operador**, **Número de veces** y **Periodo de tiempo** en los campos situados encima del editor. La consulta comprobará si la suma de la columna agregada cumple una determinada condición especificada por los marcadores de posición {% raw %}`{{operator}}` y `{{number of times}}`{% endraw %}. Esto funciona de forma similar al flujo de trabajo para crear Extensiones de Segmento clásicas.<br><br>
   - **Operador:** Indica si el suceso ha ocurrido más, menos o igual que un número de veces.<br>
   ![Campo de operador con "Más que" seleccionado.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Número de veces:** Cuántas veces quieres evaluar el suceso en relación con el operador.<br>
   ![Número de veces con "5" introducido.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Período de tiempo:** Número de días de 1 a 730 en los que desea comprobar las instancias del evento. Este periodo de tiempo se refiere a días pasados en relación con el día actual. El siguiente ejemplo muestra la consulta de usuarios que realizaron el evento más de 5 veces en los últimos 365 días.<br>
   ![Campo de periodo de tiempo con "365" introducido.]({% image_buster /assets/img_archive/sql_segments_period.png %})

En el siguiente ejemplo, el segmento resultante contendría los usuarios que realizaron el evento `favorited` más de 3 veces durante los últimos 30 días, después de una fecha especificada.

![Editor SQL que muestra un ejemplo de extensión de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Vista previa de una extensión de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

### Normas adicionales

Además, su consulta de actualización incremental debe cumplir las siguientes reglas:

- Escriba una única sentencia SQL. No incluya ningún punto y coma.
- Su segmento SQL incremental podría referirse a un único evento. Los desplegables de fecha y recuento hacen referencia al evento elegido.
- Su SQL debe tener las siguientes columnas: `user_id`, `$start_date`, y una función de agregación (como `COUNT`). Cualquier SQL guardado sin estos tres campos dará lugar a un error.

{% alert tip %}
Los segmentos de actualización incremental tienen en cuenta los eventos tardíos, que son eventos que ocurrieron hace más de 2 días (por ejemplo, eventos SDK que no se enviaron en el momento en que se capturaron).
{% endalert %}

{% endtab %}
{% endtabs %}

## Vista previa de los resultados

Antes de guardar, puedes ejecutar una vista previa de tu consulta. Las previsualizaciones de consultas se limitan automáticamente a 100 filas y expiran a los 60 segundos. El requisito de la columna `user_id` no se aplica cuando se ejecuta una vista previa.

En el caso de las extensiones incrementales de segmentos SQL, la vista previa no incluirá los criterios adicionales de los campos operador, número de veces y periodo de tiempo.

## Gestión de extensiones de segmentos SQL

En la página **Extensiones de segmento**, los segmentos generados mediante SQL se indican con <i class="fas fa-code" alt="SQL Segment Extension"></i> junto a su nombre.

Seleccione una extensión de segmento SQL para ver dónde se está utilizando la extensión, archivar la extensión o [actualizar manualmente la pertenencia al segmento](#refreshing-segment-membership).

![Sección de uso de mensajería del editor SQL que muestra dónde se está utilizando el segmento SQL.][3]

### Actualizar la membresía de segmentos

Para actualizar la pertenencia a un segmento de cualquier extensión de segmento creada mediante SQL, abra la extensión de segmento y seleccione **Actualizar**. Sólo la actualización incremental Extensiones de segmento SQL puede regenerar automáticamente (si está seleccionado).

{% alert tip %}
Si ha creado un segmento en el que espera que los usuarios entren y salgan con regularidad, actualice manualmente la Extensión de segmento que utiliza antes de dirigirse a ese segmento en una campaña o Canvas.
{% endalert %}

## Supervisión del uso de los segmentos SQL

Cada espacio de trabajo Braze dispone de 5 créditos Snowflake al mes. Si necesita más créditos, póngase en contacto con su gestor de cuenta. Los créditos se utilizan cada vez que se actualiza, o se guarda y actualiza, la suscripción a un segmento SQL. Los créditos no se utilizan cuando se ejecutan vistas previas dentro de un Segmento SQL o se guarda o actualiza una Extensión de Segmento clásica.

{% alert note %}
Los créditos copo de nieve no se comparten entre funciones. Por ejemplo, los créditos de las extensiones de segmentos SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de su consulta SQL. Cuanto mayor sea el tiempo de ejecución, más créditos costará una consulta. El tiempo de ejecución puede variar en función de la complejidad y el tamaño de las consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas, mayor será la asignación de recursos y más rápido el tiempo de ejecución.

Para ahorrar créditos, previsualice su consulta para asegurarse de que es correcta antes de guardar la Extensión de Segmento SQL.

Tus créditos volverán a ser 5 el primer día de cada mes a las 12 am UTC. Puede controlar el uso de sus créditos a lo largo del mes en el panel de uso de créditos. En la página **Extensiones de segmento**, haga clic en <i class="fa-solid fa-chart-column"></i> **Ver uso de créditos SQL**.

![Panel de uso de créditos SQL en la página de extensiones de segmentos SQL][5]{: style="max-width:60%"}

Cuando tus créditos lleguen a cero, ocurrirá lo siguiente:

- Todas las extensiones de segmento SQL configuradas para actualizarse automáticamente dejan de actualizarse, lo que afecta a los miembros de estos segmentos y a cualquier campaña o lienzo que se dirija a estos segmentos.
- Sólo puede guardar nuevas Extensiones de Segmento SQL como borradores durante el resto del mes.

Todos los usuarios de la empresa que hayan creado un segmento SQL y los administradores de la empresa recibirán una notificación por correo electrónico cuando se haya agotado el 50%, el 80% y el 100% de los créditos. Después de que sus créditos se restablezcan al comienzo del mes siguiente, podrá crear más segmentos SQL y se reanudarán las actualizaciones automáticas.

Si desea adquirir más créditos de Segmento SQL o Extensiones de Segmento adicionales, póngase en contacto con su gestor de cuenta.

## Solución de problemas

Su consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en la consulta SQL
- SQL no respeta las [reglas SQL](#writing-sql)
- Tiempo de espera de procesamiento (después de 20 minutos)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment
[5]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
[6]: {% image_buster /assets/img/ai_sql_generator.png %}
