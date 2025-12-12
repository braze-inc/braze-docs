---
nav_title: "Segmentos del catálogo"
article_title: Segmentos del catálogo
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "Este artículo describe cómo crear segmentos de catálogo, que utilizan datos de catálogo en Extensiones de Segmento SQL para crear audiencias de usuarios."
tool: Segments
---

# Segmentos del catálogo

> Los segmentos de catálogo son un tipo de extensión de segmento SQL que se crea combinando datos de catálogo con datos de eventos personalizados o compras. Pueden referenciarse en un segmento y luego ser objeto de campañas y Lienzos. 

{% alert important %}
Los segmentos del catálogo están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

Los segmentos de catálogos utilizan SQL para unir datos de catálogos y datos de eventos personalizados o compras. Para ello, debes tener un campo identificador común en todos tus catálogos y en tus eventos personalizados o compras. Por ejemplo, el valor de un ID de artículo en un catálogo debe coincidir con el valor de una propiedad en un evento personalizado.

## Crear un segmento de catálogo

1. Ve a **Extensiones de segmento** > **Crear nueva extensión** > **Empezar con plantilla** y selecciona una plantilla. <br>Modal con la opción de crear un segmento de catálogo para eventos o compras.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. El editor SQL se rellena automáticamente con una plantilla. <br>\![Editor SQL con una plantilla pregenerada.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Esta plantilla une los datos de eventos de usuario con los datos del catálogo para segmentar a los usuarios que interactuaron con determinados artículos del catálogo.

3. Utiliza la pestaña **Variables** para proporcionar los campos necesarios para tu plantilla antes de generar tu segmento. <br>Para que Braze identifique a los usuarios en función de su interacción con los elementos del catálogo, tienes que hacer lo siguiente: <br> \- Selecciona un catálogo que contenga un campo de catálogo <br> \- Selecciona un evento personalizado que contenga una propiedad de evento <br> \- Haz coincidir los valores del campo del catálogo y de las propiedades del evento

Aquí tienes unas pautas para seleccionar las variables:

| Campo variable | Descripción |
| --- | --- |
| `Catalog` | El nombre del catálogo que utilizas para dirigirte a los usuarios. |
| `Catalog field`| El campo de tu catálogo que contiene los mismos valores que tu `Custom event property`. Suele ser un tipo de ID. En el caso de uso del comercio electrónico, sería `shopify_id`. |
| `Custom event` | El nombre de tu evento personalizado, que es el mismo evento que contiene una propiedad con valores que coinciden con tu `Catalog field`. En el caso de uso del comercio electrónico, sería `Made Order`. |
| `Custom event property` | El nombre de la propiedad de tu evento personalizado, que coincide con los valores de tu `Catalog field`. En el caso de uso del ejemplo de comercio electrónico, sería `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. Si es necesario, rellena campos opcionales adicionales para tu caso de uso para segmentar por un valor de campo concreto dentro de tu catálogo:
- `Catalog field`: Un campo concreto (nombre de columna) dentro de este catálogo
- `Value`: Un valor específico dentro de ese campo o columna <br><br> Utilizando la aplicación de salud como ejemplo, digamos que dentro del catálogo de cada médico que podrías reservar, hay un campo llamado `specialty` que contiene un valor como `vision` o `dental`. Para segmentar a los usuarios que han visitado algún médico con el valor `dental`, puedes seleccionar `specialty` como el `Catalog field`, y seleccionar `dental` como el `Value`.

5. Después de crear un segmento SQL, te recomendamos que hagas clic en **Ejecutar vista previa** para ver si tu consulta devuelve usuarios o si hay errores. Para obtener más información sobre [la vista previa de los resultados de las consultas]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), la gestión de las extensiones [de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) y mucho más, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Si vas a crear un segmento SQL que utilice la tabla `CATALOGS_ITEMS_SHARED`, debes especificar un ID de catálogo. Por ejemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Determinar si necesitas invertir SQL

Aunque no es posible consultar directamente a los usuarios con cero eventos, puedes utilizar **Invert SQL** para dirigirte a estos usuarios.

Por ejemplo, para dirigirte a los usuarios que tienen menos de tres compras, escribe primero una consulta para seleccionar a los usuarios que tienen tres o más compras. A continuación, selecciona **Invertir SQL** para dirigirte a los usuarios con menos de tres compras (incluidos aquellos con cero compras).

\![Extensión de segmento denominada "Se ha hecho clic en 1-4 correos electrónicos en los últimos 30 días" con la opción de invertir SQL seleccionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
A menos que te dirijas específicamente a usuarios con cero eventos, no necesitarás invertir SQL. Si se selecciona **Invertir SQL**, confirma que la característica es necesaria y que el segmento coincide con tu audiencia deseada. Por ejemplo, si una consulta se dirige a usuarios con al menos un evento, sólo se dirigirá a usuarios con cero eventos cuando se invierta.
{% endalert %}

## Refrescar la pertenencia a un segmento

Para actualizar la pertenencia a un segmento de cualquier segmento del catálogo, abre el segmento del catálogo y selecciona **Acciones** > **Actualizar** > **Sí, Actualizar**.

{% alert tip %}
Si has creado un segmento en el que esperas que los usuarios entren y salgan con regularidad, actualiza manualmente el segmento del catálogo que utiliza antes de dirigirte a ese segmento en una campaña o Canvas.
{% endalert %}

### Designar la configuración de actualización

{% multi_lang_include segments.md section='Refresh settings' %}

## Casos de uso

{% tabs local %}
{% tab Health %}

### Aplicación Salud

Supongamos que tienes una aplicación de salud y quieres segmentar a los usuarios que han reservado una visita al dentista. También tienes lo siguiente:

- Un catálogo `Doctors` que contiene los distintos médicos que puede reservar un paciente, cada uno asignado con un `doctor ID`
- Un evento personalizado `Booked Visit` con una propiedad `doctor ID` que comparte los mismos valores que el campo `doctor ID` de tu catálogo.
- Un campo `speciality` dentro de tu catálogo que contenga el valor `dental` 

Configurarías un segmento de catálogo utilizando las siguientes variables:

| Variable | Propiedad |
| --- | --- |
| `Catalog`| Médicos |
| `Catalog field` | ID del médico |
| `Custom event`| Visita reservada|
| `Custom event property` | ID del médico |
| `(Under Filter SQL Results) Catalog field` | Especialidad |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### Plataforma SaaS

Supongamos que tienes una plataforma SaaS B2B y quieres segmentar a los usuarios que son empleados de un cliente existente. También tienes lo siguiente:

- Un catálogo `Accounts` que contiene las diferentes cuentas que están utilizando actualmente tu plataforma SaaS, cada una asignada con un `account ID`
- Un evento personalizado `Event Attendance` con una propiedad "ID de cuenta" que comparte los mismos valores que el campo "ID de cuenta" de tu catálogo.
- Un campo `Classification` dentro de tu catálogo que contenga el valor `enterprise` 

Configurarías un segmento de catálogo utilizando las siguientes variables:

| Variable | Propiedad |
| --- | --- |
| `Catalog` | Cuentas |
| `Catalog field `| ID de cuenta |
| `Custom event` | Asistencia al acto |
| `Custom event property` | ID de cuenta |
| `(Under Filter SQL Results) Catalog field` | Clasificación |
| `(Under Filter SQL Results) Value` | Empresa |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes

### ¿La ejecución de un segmento de catálogo consume créditos de Extensión de Segmento SQL?

Sí, los segmentos del catálogo funcionan con SQL y consumen créditos de Extensión de Segmento SQL. Para saber más, consulta el [uso de Segmentos SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### ¿La creación de un segmento de catálogo consume asignaciones de extensiones de segmento SQL?

Sí. Del mismo modo que las Extensiones de Segmento SQL cuentan para tu asignación de Extensiones de Segmento, los segmentos de catálogo también cuentan para esa asignación.

### Tengo un caso de uso de segmento de catálogo para el que la plantilla actual no sirve. ¿Cómo debo configurarlo?

Ponte en contacto con tu administrador de atención al cliente o con [el soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) para obtener más información.

