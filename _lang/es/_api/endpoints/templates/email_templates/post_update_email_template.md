---
nav_title: "PUBLICAR: Actualizar plantilla de correo electrónico"
article_title: "PUBLICAR: Actualizar plantillas de correo electrónico"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar plantilla de correo electrónico de Braze."

---
{% api %}
# Actualizar las plantillas de correo electrónico existentes
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> Utiliza este punto final para actualizar plantillas de correo electrónico en el panel Braze.

Puedes acceder a la página `email_template_id` de una plantilla de correo electrónico navegando hasta ella en la página **Plantillas & Medios**. El [punto final Crear plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) también devolverá una referencia `email_template_id`.

Todos los campos que no sean `email_template_id` son opcionales, pero debes especificar al menos un campo para actualizarlo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Requisitos previos
Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `templates.email.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Obligatoria |Cadena|[El identificador API de]({{site.baseurl}}/api/identifier_types/) tu [plantilla de correo electrónico.]({{site.baseurl}}/api/identifier_types/)|
|`template_name`|Opcional|Cadena|Nombre de tu plantilla de correo electrónico.|
|`subject`|Opcional|Cadena|Línea del asunto de la plantilla de correo electrónico.|
|`body`|Opcional|Cadena|Cuerpo de la plantilla de correo electrónico que puede incluir HTML.|
|`plaintext_body`|Opcional|Cadena|Una versión en texto plano del cuerpo de la plantilla de correo electrónico.|
|`preheader`|Opcional|Cadena|Preencabezado de correo electrónico utilizado para generar vistas previas en algunos clientes.|
|`tags`|Opcional|Cadena|[Las etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) ya deben existir.|
|`should_inline_css`|Opcional|Booleano|Habilita o deshabilita la característica `inline_css` por plantilla. Si no se proporciona, Braze utilizará la configuración predeterminada para el AppGroup. Se espera una de `true` o `false`.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas, si procede.

| Error | Solución de problemas |
| --- | --- |
| El nombre de la plantilla es obligatorio. | Introduce un nombre para la plantilla. |
| Las etiquetas deben ser una matriz | Las etiquetas deben formatearse como una matriz de cadenas, por ejemplo `["marketing", "promotional", "transactional"]`. |
| Todas las etiquetas deben ser cadenas | Asegúrate de que tus etiquetas estén entre comillas (`""`). |
| No se han encontrado algunas etiquetas | Para añadir una etiqueta al crear una plantilla de correo electrónico, la etiqueta debe existir ya en Braze. |
| Valor no válido para `should_inline_css`. Se esperaba una de `true` o `false` | Este parámetro solo acepta valores booleanos (verdadero o falso). Asegúrate de que el valor de `should_inline_css` no está encapsulado entre comillas (`""`), lo que hace que el valor se envíe como una cadena. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
