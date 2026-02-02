---
nav_title: Jasper
article_title: Jasper
description: "Este artículo de referencia describe la integración entre Braze y Jasper."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jasper 

> [Jasper](https://www.jasper.ai/) es una plataforma de contenidos impulsada por inteligencia artificial que permite a tu marca crear, gestionar y ampliar contenidos de alta calidad y adaptados a la marca en varios canales, como blogs, anuncios y redes sociales.

_Esta integración está mantenida por Jasper._

## Resumen

La integración de Jasper y Braze te permite agilizar la creación de contenidos y la ejecución de campañas. Con Jasper, tus equipos de marketing pueden generar textos de alta calidad y adaptados a la marca en cuestión de minutos. Braze facilitará entonces la entrega de estos mensajes a la audiencia adecuada en el momento óptimo. Esta integración fomenta flujos de trabajo sin fisuras, reduce el esfuerzo manual e impulsa resultados de interacción más sólidos.

Las ventajas de utilizar esta integración incluyen:

- **Ejecución rápida de la campaña:** Lanza campañas en minutos, no en semanas.
- **Una voz de marca coherente:** Utiliza las plantillas de Jasper para asegurarte de que los textos generados se ajustan estrictamente a las directrices de la marca.
- **Generación de contenidos específicos:** Crea mensajes altamente personalizados con segmentos de audiencia, guías de estilo y elementos de conocimiento propios.
- **Personalización dinámica:** Utiliza marcadores de posición Liquid, como {% raw %}```{{${first_name}}}```{% endraw %}, para una personalización escalable dentro de Braze.
- **Reducción de errores:** Los flujos de trabajo automatizados minimizan los errores de copiar y pegar y reducen los pasos manuales.

## Requisitos previos

| Requisito   | Descripción  |
| ------------------- | ---------------- |
| Cuenta Jasper      | Necesitas una cuenta Jasper para utilizar esta asociación. |
| Clave de API REST Braze  | Una clave de API REST Braze con los siguientes permisos. <br>  <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>Esta clave puede generarse en el panel de Braze navegando a **Configuración > Claves de API**.  |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final específico depende de la URL Braze de tu instancia. Consulta la página [Aspectos básicos de la API de Braze: Puntos finales]({{site.baseurl}}/api/basics#endpoints) documentación para más detalles. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

## Métodos de integración

Hay dos métodos para generar contenido en Jasper y actualizar plantillas Braze:

1. Utiliza directamente la API de Jasper
2. Utiliza Jasper Studio para crear una aplicación personalizada preparada para Braze

{% tabs %}
{% tab Jasper API %}

## Método: Utiliza directamente la API de Jasper

Este método es ideal para crear y actualizar mediante programación plantillas HTML de correo electrónico en Braze, evitando la configuración manual en Jasper y Braze.

### Paso 1: Configurar Jasper

1. Sigue las instrucciones de [Cómo empezar](https://developers.jasper.ai/docs/getting-started-1) para generar tu clave de API de Jasper.
2. Utiliza la plantilla preconstruida de Jasper que está optimizada para generar plantillas de correo electrónico Braze HTML, que tiene un ID de plantilla de `skl_BC53D8AC5B4B47E8BE557EBB706E9B47`.
3. Recopila los valores de los siguientes campos, que son necesarios para realizar una solicitud para generar contenido para una plantilla de correo electrónico HTML de Braze.

| Campo | Descripción |
| --- | --- |
| `emailObjective`| Define claramente el objetivo del correo electrónico. |
| `ctaLink`| La URL de tu llamada a la acción. |
| `unsubscribeLink`| Necesario para los envíos por correo electrónico de marketing. |
| `brandColor`| El color primario de tu marca en formato hexadecimal (por ejemplo, `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

**Campos opcionales**

| Campo | Descripción |
| --- | --- |
|`toneId` | Voz de marca |
| `audienceId`| Segmentación de la audiencia |
| `styleId`| Guía de estilo |
| `knowledgeIds` | Contexto de contenido mejorado. Puedes añadir hasta tres ID. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

{: start="4"}
4\. Genera tu salida ejecutando la plantilla a través de la API de Jasper. Esto producirá una carga útil JSON que contendrá `subject`, `preheader`, y `body` (contenido HTML).

{% subtabs %}
{% subtab Sample request %}

### Solicitud de muestra

{% raw %}
```json
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### Muestra de resultados
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### Paso 2: Configurar Braze

Utilizando las direcciones `subject`, `preheader`, y `body` generadas por Jasper en el Paso 1, haz una solicitud POST a la API REST de Braze para [crear una nueva plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Asegúrate de que tu clave de API REST Braze tiene los permisos `templates.email.create` y `templates.email.update`.

### Ejemplo de solicitud de la API Braze para crear una plantilla de correo electrónico

```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## Método: Crea una aplicación personalizada preparada para Braze con Jasper Studio

Jasper Studio es una plataforma sin código dentro de Jasper que te permite crear aplicaciones de IA a medida sin necesidad de soporte informático. Puedes diseñar una aplicación personalizada que genere estructuras JSON formateadas específicamente para la API de Braze, o generar contenido que pueda añadirse manualmente a tus mensajes Braze.

1. En la pantalla de inicio de Jasper, selecciona **Crear una aplicación**.
2. Especifica la aplicación que quieres crear, como **Plantilla de correo electrónico HTML Braze** o **Plantilla de bloque de contenido**.
3. Edita los campos de solicitud de entrada que genera Jasper. Para una plantilla de correo electrónico HTML, puedes incluir formularios de entrada para la línea del asunto, el preencabezado, el cuerpo HTML, las etiquetas, alternar CSS en línea y el nombre de la plantilla.
4. Integra incrustaciones de conocimiento con orientación sobre las mejores prácticas de Liquid para una personalización coherente y un contenido dinámico.
5. Perfecciona las instrucciones proporcionadas al Gran Modelo Lingüístico (LLM) para la generación de contenidos.
6. Proporciona un ejemplo de la salida deseada, que puede incluir una salida JSON automatizada formateada para cargas útiles Braze.
7. Genera y exporta lo siguiente:
- **Copiar/Pegar directamente:** El contenido se puede copiar y pegar directamente en la plataforma Braze.
- **Salida JSON:** Generar salida JSON. Esta carga útil puede utilizarse para llamar directamente al punto final Braze a través de `curl` o middleware, o integrarse en tu flujo de trabajo de operaciones de correo electrónico.

![Aplicación personalizada Jasper Braze.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## Ejemplo de salida JSON (aplicación personalizada)

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## Ejemplo de solicitud de la API Braze (utilizando la salida personalizada de la aplicación)

{% raw %}
```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

Alternativamente, si eres especialista en marketing, puedes crear tu aplicación personalizada para alinearte con las directrices de la marca para generar contenido sin HTML ni copiar y pegar, y utilizar plantillas Braze para el estilo.

{% endtab %}
{% endtabs %}

{% alert note %}
Para obtener más ayuda, consulta [la documentación de la API de Jasper](https://developers.jasper.ai/reference/gettemplate-1) y el [Centro de Ayuda de Jasper Studio](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio).
{% endalert %}
