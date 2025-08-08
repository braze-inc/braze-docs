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

> Los segmentos de catálogo son un tipo de extensión de segmento SQL que se crea combinando datos de catálogo con datos de eventos o compras personalizados. Pueden referenciarse en un segmento y luego ser objeto de campañas y Canvas. 

{% alert important %}
Los segmentos del catálogo se encuentran actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

Los segmentos de catálogo utilizan SQL para unir datos de catálogos y datos de eventos o compras personalizados. Para ello, debe tener un campo identificador común en todos sus catálogos y sus eventos o compras personalizados. Por ejemplo, el valor de un ID de artículo en un catálogo debe coincidir con el valor de una propiedad en un evento personalizado.

## Creación de un segmento de catálogo

1. Ve a **Extensiones de segmento** > **Crear nueva extensión** > **Empezar con plantilla** y selecciona una plantilla. <br>![Modal con la opción de crear un segmento de catálogo para eventos o compras.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. El editor SQL se rellena automáticamente con una plantilla. <br>![Editor SQL con una plantilla pregenerada.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Esta plantilla une los datos de eventos de usuario con los datos del catálogo para segmentar a los usuarios que han interactuado con determinados artículos del catálogo.

3. Utilice la pestaña **Variables** para proporcionar los campos necesarios para su plantilla antes de generar su segmento. <br>Para que Braze identifique a los usuarios en función de su compromiso con los artículos del catálogo, debe hacer lo siguiente: <br> \- Seleccione un catálogo que contenga un campo de catálogo <br> \- Seleccione un evento personalizado que contenga una propiedad de evento <br> \- Haga coincidir los valores de las propiedades de los campos y eventos de su catálogo

Estas son las pautas para seleccionar las variables:

| Campo variable | Descripción |
| --- | --- |
| `Catalog` | El nombre del catálogo que utilizas para dirigirte a los usuarios. |
| `Catalog field`| El campo de su catálogo que contiene los mismos valores que su `Custom event property`. Suele ser un tipo de identificación. En el caso de uso del comercio electrónico, sería `shopify_id`. |
| `Custom event` | El nombre de su evento personalizado, que es el mismo evento que contiene una propiedad con valores que coinciden con su `Catalog field`. En el caso de uso del comercio electrónico, sería `Made Order`. |
| `Custom event property` | El nombre de su propiedad de evento personalizada, que coincide con los valores de su `Catalog field`. En el caso de uso del ejemplo de comercio electrónico, sería `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. Si es necesario, rellene campos opcionales adicionales para su caso de uso para segmentar por un valor de campo concreto dentro de su catálogo:
- `Catalog field`: Un campo concreto (nombre de columna) dentro de este catálogo
- `Value`: Un valor específico dentro de ese campo o columna <br><br> Usando la aplicación de salud como ejemplo, digamos que dentro del catálogo de cada médico que podrías reservar, hay un campo llamado `specialty` que contiene un valor como `vision` o `dental`. Para segmentar a los usuarios que han visitado algún médico con el valor `dental`, puede seleccionar `specialty` como el `Catalog field`, y seleccionar `dental` como el `Value`.

5. Después de crear un Segmento SQL, recomendamos hacer clic en **Ejecutar Vista Previa** para ver si su consulta devuelve usuarios o si hay errores. Para obtener más información sobre [la vista previa de los resultados de las consultas]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), la gestión de [las extensiones de segmentos SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions), etc., consulta [Extensiones de segmentos SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Si vas a crear un segmento SQL que utilice la tabla `CATALOGS_ITEMS_SHARED`, debes especificar un ID de catálogo. Por ejemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

## Actualizar la membresía de segmentos

Para actualizar la pertenencia a un segmento de cualquier segmento del catálogo, abre el segmento del catálogo y selecciona **Acciones** > **Actualizar** > **Sí, Actualizar**.

{% alert tip %}
Si has creado un segmento en el que esperas que los usuarios entren y salgan con regularidad, actualiza manualmente el segmento del catálogo que utiliza antes de dirigirte a ese segmento en una campaña o Canvas.
{% endalert %}

### Designar configuración de actualización

{% multi_lang_include segments.md section='Refresh settings' %}

## Casos de uso

### Aplicación de salud

Supongamos que tiene una aplicación de salud y desea segmentar a los usuarios que han reservado una visita al dentista. También tienes lo siguiente:

- Un catálogo `Doctors` que contiene los diferentes médicos que un paciente puede reservar, cada uno asignado con un `doctor ID`
- Un evento personalizado `Booked Visit` con una propiedad `doctor ID` que comparte los mismos valores que el campo `doctor ID` de su catálogo.
- Un campo `speciality` dentro de su catálogo que contenga el valor `dental` 

Usted configuraría un segmento de catálogo utilizando las siguientes variables:

| Variable | Propiedad |
| --- | --- |
| `Catalog`| Médicos |
| `Catalog field` | identificación del médico |
| `Custom event`| Visita reservada|
| `Custom event property` | identificación del médico |
| `(Under Filter SQL Results) Catalog field` | Especialidad |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Plataforma SaaS

Supongamos que tiene una plataforma SaaS B2B y desea segmentar a los usuarios que son empleados de un cliente existente. También tienes lo siguiente:

- Un catálogo `Accounts` que contiene las diferentes cuentas que están utilizando actualmente su plataforma SaaS, cada una asignada con un `account ID`
- Un evento personalizado `Event Attendance` con una propiedad "ID de cuenta" que comparte los mismos valores que el campo "ID de cuenta" de su catálogo.
- Un campo `Classification` dentro de su catálogo que contenga el valor `enterprise` 

Usted configuraría un segmento de catálogo utilizando las siguientes variables:

| Variable | Propiedad |
| --- | --- |
| `Catalog` | Cuentas |
| `Catalog field `| ID de cuenta |
| `Custom event` | Asistencia a eventos |
| `Custom event property` | ID de cuenta |
| `(Under Filter SQL Results) Catalog field` | Clasificación |
| `(Under Filter SQL Results) Value` | Empresa |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas más frecuentes

### ¿La ejecución de un segmento de catálogo consume créditos de la Extensión de Segmento SQL?

Sí, los segmentos de catálogo funcionan con SQL y consumen créditos de la Extensión de segmentos SQL. Para saber más, consulta el [uso de Segmentos SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### ¿Consume la creación de un segmento de catálogo las asignaciones de la Extensión de Segmento SQL?

Sí. Del mismo modo que las Extensiones de Segmento SQL cuentan para su asignación de Extensiones de Segmento, los segmentos de catálogo también cuentan para esa asignación.

### Tengo un caso de uso de segmento de catálogo que la plantilla actual no sirve. ¿Cómo debo configurarlo?

Póngase en contacto con su gestor de atención al cliente o con [el servicio de asistencia de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) para obtener más información.

