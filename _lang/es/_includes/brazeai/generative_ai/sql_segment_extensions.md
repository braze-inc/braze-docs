# Extensiones de segmentos SQL

> Puede generar una Extensión de Segmento utilizando consultas SQL Snowflake de datos [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). SQL puede ayudarle a desbloquear nuevos casos de uso de los segmentos, ya que ofrece la flexibilidad necesaria para describir las relaciones entre los datos de formas que no son posibles con otras funciones de segmentación.
>
> Al igual que las extensiones de segmento estándar, puede consultar eventos de hasta los dos últimos años (730 días) en su extensión de segmento SQL. A diferencia de las extensiones de segmento estándar, las extensiones de segmento SQL [consumen créditos](#credits).

## Requisitos previos

Como es posible acceder a datos PII a través de esta característica, debes tener permisos PII para ejecutar consultas SQL de segmento.

## Crear una extensión de segmento

### Paso 1: Elige un editor

Hay dos tipos de editores SQL entre los que puedes elegir para crear tu Extensión de Segmento SQL: el Editor SQL y el Editor SQL Incremental.

- **Refresco completo:** Cada vez que se actualice su segmento, Braze consultará todos los datos disponibles para actualizarlo, lo que consumirá más créditos que las actualizaciones incrementales. Las extensiones de actualización completa pueden regenerar automáticamente la afiliación a diario, pero no pueden actualizarse mediante la actualización incremental.
- **Actualización incremental:** La actualización incremental sólo calcula los datos de los dos últimos días, lo que resulta más rentable y consume menos créditos cada vez. Al crear un segmento SQL de actualización incremental, puede configurarlo para que regenere automáticamente la afiliación diariamente. Esto te permite configurar tu segmento para que se actualice automáticamente a diario, lo que ayuda a reducir el coste de una actualización diaria de datos para las extensiones de segmento SQL.
- **Generador AI SQL:** El Generador SQL de IA te permite escribir una consulta en lenguaje llano y la convierte en una consulta SQL para tu segmento. Es una forma rápida de empezar sin necesidad de escribir tú mismo el SQL.

{% alert tip %}
Puede realizar una actualización manual completa de todos los segmentos SQL creados en cualquiera de los dos editores SQL.
{% endalert %}

{% tabs local %}
{% tab Actualización completa %}

Para crear una extensión de segmento SQL de actualización completa:

1. Vaya a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Crear nueva extensión** y, a continuación, **Actualizar completamente**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Añada un nombre para su Extensión de Segmento e introduzca su SQL. Consulta [el Paso 2](#step-2-write-your-sql) para ver los requisitos y recursos.<br><br>
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
2\. Selecciona **Crear nueva extensión** y selecciona **Actualización incremental**.<br><br>
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

1. Selecciona **Iniciar Generador SQL AI** después de crear un [segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) utilizando la actualización completa o incremental.
2. Escribe tu consulta y selecciona **Generar** para traducir tu consulta a SQL.
3. Revisa el SQL generado para asegurarte de que parece correcto y, a continuación, guarda tu segmento.

#### Ejemplos de indicaciones
- Usuarios que recibieron un correo electrónico en el último mes
- Usuarios que realizaron menos de cinco compras en el último año

#### Consejos
- Familiarícese con las [tablas de datos Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para esta característica. El incumplimiento de estas normas provocará un error. Por ejemplo, tu código SQL debe seleccionar la columna `user_id`. Empezar tu pregunta con "usuarios que" puede ayudar.
- Puedes enviar hasta 20 consultas por minuto con el generador de SQL con IA.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}
{% endtabs %}

{% alert note %}
Las consultas SQL que tarden más de 20 minutos en ejecutarse agotarán el tiempo de espera.
{% endalert %}

Cuando la extensión termine de procesarse, podrás [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) utilizando tu Extensión de segmento y dirigirte a este nuevo segmento con tus campañas y Lienzos.

### Paso 2: Escribe tu SQL

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

#### Normas adicionales

Además, tu consulta SQL estándar debe cumplir las siguientes reglas:

- No puedes utilizar las declaraciones `DECLARE`.
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

{% alert tip %}
Los segmentos de actualización incremental tienen en cuenta los eventos tardíos, que son eventos que ocurrieron hace más de 2 días (por ejemplo, eventos SDK que no se enviaron en el momento en que se capturaron).
{% endalert %}

#### Normas adicionales

Además, tu consulta de actualización incremental debe cumplir las siguientes reglas:

- Escriba una única sentencia SQL. No incluya ningún punto y coma.
- Su segmento SQL incremental podría referirse a un único evento. Los desplegables de fecha y recuento hacen referencia al evento elegido.
- Su SQL debe tener las siguientes columnas: `user_id`, `$start_date`, y una función de agregación (como `COUNT`). Cualquier SQL guardado sin estos tres campos dará lugar a un error.
- No puedes utilizar las declaraciones `DECLARE`.
{% endtab %}
{% endtabs %}

{% alert note %}
Si vas a crear un segmento SQL que utilice la tabla `CATALOGS_ITEMS_SHARED`, debes especificar un ID de catálogo. Por ejemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Paso 3: Vista previa de la consulta

Antes de guardar, puedes ejecutar una vista previa de tu consulta. Las previsualizaciones de consultas se limitan automáticamente a 100 filas y expiran a los 60 segundos. El requisito de la columna `user_id` no se aplica cuando se ejecuta una vista previa.

En el caso de las extensiones incrementales de segmentos SQL, la vista previa no incluirá los criterios adicionales de los campos operador, número de veces y periodo de tiempo.

### Paso 4: Determina si necesitas invertir SQL

A continuación, determina si necesitas invertir el SQL. Aunque no es posible consultar directamente a los usuarios con cero eventos, puedes utilizar **Invert SQL** para dirigirte a estos usuarios.

{% alert note %}
Por predeterminado, **Invertir SQL** no está alternado. Sin embargo, si utilizas el generador AI SQL para generar una sentencia SQL que necesite ser negada, ChatGPT podría devolver una salida que alternara automáticamente esta característica.
{% endalert %}

Por ejemplo, para dirigirte a los usuarios que tienen menos de tres compras, escribe primero una consulta para seleccionar a los usuarios que tienen tres o más compras. A continuación, selecciona **Invertir SQL** para dirigirte a los usuarios con menos de tres compras (incluidos los que tienen cero compras).

{% alert important %}
A menos que te dirijas específicamente a usuarios con cero eventos, no necesitarás invertir SQL. Si se selecciona **Invertir SQL**, confirma que la característica es necesaria y que el segmento coincide con tu audiencia deseada. Por ejemplo, si una consulta se dirige a usuarios con al menos un evento, sólo se dirigirá a usuarios con cero eventos cuando se invierta.
{% endalert %}

![Extensión de segmento denominada "Se ha hecho clic en 1-4 correos electrónicos en los últimos 30 días" con la opción de invertir SQL seleccionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Actualizar la membresía de segmentos

Para actualizar la pertenencia a un segmento de cualquier extensión de segmento creada mediante SQL, abra la extensión de segmento y seleccione **Actualizar**.

{% alert tip %}
Si ha creado un segmento en el que espera que los usuarios entren y salgan con regularidad, actualice manualmente la Extensión de segmento que utiliza antes de dirigirse a ese segmento en una campaña o Canvas.
{% endalert %}

## Administra tus extensiones de segmento

En la página **Extensiones de segmento**, los segmentos generados mediante SQL se indican con <i class="fas fa-code" alt="SQL Segment Extension"></i> junto a su nombre.

Seleccione una extensión de segmento SQL para ver dónde se está utilizando la extensión, archivar la extensión o [actualizar manualmente la pertenencia al segmento](#refreshing-segment-membership).

![Mensajería Sección de uso del editor SQL que muestra dónde se está utilizando el segmento SQL.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Designar la configuración de actualización

{% multi_lang_include segments.md section='Refresh settings' %}

## Créditos de Snowflake {#credits}

Cada espacio de trabajo Braze dispone de 5 créditos Snowflake al mes. Si necesita más créditos, póngase en contacto con su gestor de cuenta. Los créditos se utilizan cada vez que se actualiza, o se guarda y actualiza, la suscripción a un segmento SQL. Los créditos no se utilizan cuando se ejecutan vistas previas dentro de un Segmento SQL o se guarda o actualiza una Extensión de Segmento clásica.

{% alert note %}
Los créditos copo de nieve no se comparten entre funciones. Por ejemplo, los créditos de las extensiones de segmentos SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de su consulta SQL. Cuanto mayor sea el tiempo de ejecución, más créditos costará una consulta. El tiempo de ejecución puede variar en función de la complejidad y el tamaño de las consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas, mayor será la asignación de recursos y más rápido el tiempo de ejecución.

Para ahorrar créditos, previsualice su consulta para asegurarse de que es correcta antes de guardar la Extensión de Segmento SQL.

Tus créditos volverán a ser 5 el primer día de cada mes a las 12 am UTC. Puede controlar el uso de sus créditos a lo largo del mes en el panel de uso de créditos. En la página **Extensiones de segmento**, haga clic en <i class="fa-solid fa-chart-column"></i> **Ver uso de créditos SQL**.

![Panel de uso de créditos SQL en la página de extensiones de segmento SQL]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

Cuando tus créditos lleguen a cero, ocurrirá lo siguiente:

- Todas las extensiones de segmento SQL configuradas para actualizarse automáticamente dejan de actualizarse, lo que afecta a los miembros de estos segmentos y a cualquier campaña o lienzo que se dirija a estos segmentos.
- Sólo puede guardar nuevas Extensiones de Segmento SQL como borradores durante el resto del mes.

Todos los usuarios de la empresa que hayan creado un segmento SQL y los administradores de la empresa recibirán una notificación por correo electrónico cuando se haya agotado el 50%, el 80% y el 100% de los créditos. Después de que sus créditos se restablezcan al comienzo del mes siguiente, podrá crear más segmentos SQL y se reanudarán las actualizaciones automáticas.

Si desea adquirir más créditos de Segmento SQL o Extensiones de Segmento adicionales, póngase en contacto con su gestor de cuenta.
