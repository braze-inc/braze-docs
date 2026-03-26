---
nav_title: Constructor de plantillas de WhatsApp
article_title: Constructor de plantillas de WhatsApp
description: "Aprende a crear, configurar y enviar plantillas de mensajes de WhatsApp directamente en Braze usando el constructor de plantillas de WhatsApp."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# Constructor de plantillas de WhatsApp

> El constructor de plantillas de WhatsApp te permite crear y enviar plantillas de mensajes de WhatsApp directamente en Braze, sin necesidad de alternar entre Braze y Meta Business Manager. Una vez que Meta apruebe tu plantilla, úsala en tantas campañas y Canvas como quieras.

{% alert note %}
El constructor de plantillas de WhatsApp se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze para obtener acceso.
{% endalert %}

## Requisitos previos

Antes de crear una plantilla de WhatsApp en Braze, completa la [configuración de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/).

### Plantillas de carrusel de WhatsApp

{% multi_lang_include whatsapp/carousel_template_prerequisites.md %}

## Crear una plantilla

### Paso 1: Ve a plantillas de WhatsApp

Ve a **Plantillas** > **Plantillas de WhatsApp** y selecciona **Crear nueva plantilla**.

![Página de plantillas de WhatsApp con botón para crear una nueva plantilla.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Paso 2: Configura los ajustes de la plantilla

Completa los siguientes campos:

| Campo | Descripción |
| ----- | ----- |
| **Cuenta** | La cuenta de WhatsApp Business (WABA) a la que deseas enviar la plantilla. Todos los grupos de suscripción y números de teléfono dentro de una WABA compartirán el acceso a la plantilla. |
| **Idioma** | El idioma de esta plantilla. WhatsApp requiere una plantilla separada para cada idioma. |
| **Nombre de la plantilla** | Un nombre único para tu plantilla. Los nombres de plantilla solo pueden contener letras minúsculas, números y guiones bajos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 3: Elige un diseño

En **Diseño**, selecciona el tipo de plantilla:

- **Predeterminado:** Un mensaje estándar de WhatsApp. Este es el diseño que se cubre en este artículo.  
- **Carrusel:** Un mensaje con tarjetas desplazables horizontalmente. Para más información, consulta [Plantillas de carrusel]({{site.baseurl}}/whatsapp_carousel_templates/).

### Paso 4: Construye tu plantilla

#### Encabezado (opcional)

Añade un encabezado que aparecerá sobre el cuerpo del mensaje. Puedes elegir:

- **Texto:** Un encabezado de texto corto.  
- **Multimedia:** Una imagen, video o documento (solo URL). Braze almacena la referencia multimedia y envía una muestra a Meta para su aprobación.  
- **Ninguno:** Sin encabezado 

#### Cuerpo

Introduce el contenido principal de tu mensaje y personaliza el cuerpo según sea necesario usando Liquid o variables genéricas:

{% raw %}
- Usa etiquetas de Liquid (por ejemplo, `{{${first_name}}}`). Braze guarda tu Liquid y lo muestra cuando usas la plantilla en una campaña o en el creador de mensajes de Canvas.  
- Usa variables genéricas, como marcadores de posición numerados (por ejemplo, `{{1}}`), si prefieres añadir la personalización más adelante al construir tu mensaje.
{% endraw %}

Puedes añadir personalización donde aparezca el botón **+** (más). No todos los campos admiten personalización.

#### Pie de página (opcional)

Añade un pie de página corto que aparecerá debajo del cuerpo del mensaje.

#### Botones (opcional)

Añade hasta 10 botones a tu plantilla. Los tipos de botones tienen diferentes categorías y especificaciones.

| Tipo de botón | Categoría | Especificaciones |
| --- | --- | --- |
| Respuesta rápida | Botones de respuesta rápida |{::nomarkdown}<ul><li><b>Cantidad máxima:</b> 10</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li></ul> {:/}|
| Número de teléfono | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 1</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li><li><b>Número de teléfono:</b> Número de teléfono válido con código de país, sin + (como "14155552671")</li></ul> {:/}|
| Visitar sitio web | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 2</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li><li><b>URL del sitio web:</b> Hasta 2000 caracteres</li></ul> {:/}|
| Copiar código de oferta | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 1</li><li><b>Texto del botón:</b> "Copy offer code" (no se puede editar)</li><li><b>Código de oferta:</b> Hasta 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

![Creador de plantillas de WhatsApp con botones de respuesta rápida y llamada a la acción.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Paso 5: Previsualiza tu plantilla

Antes de enviar, previsualiza cómo aparecerá tu mensaje para los destinatarios:

- **Previsualizar como usuario:** Ve una vista previa genérica del mensaje.  
- **Previsualizar como un usuario específico:** Selecciona un perfil de usuario para previsualizar cómo se renderizará la plantilla con los datos de ese usuario.

### Paso 6: Envía para revisión

Selecciona **Enviar** para enviar tu plantilla a Meta para revisión, lo que normalmente tarda unos minutos pero puede tardar hasta 24 horas. La plantilla aparece en tu página de **Plantillas de WhatsApp** cuando se envía, y el estado se actualiza cuando actualizas la página de **Plantillas de WhatsApp**.

## Categorías de plantillas compatibles

Actualmente solo se admiten plantillas de marketing en el constructor de plantillas de WhatsApp.

## Usar una plantilla aprobada en una campaña

Una vez que Meta apruebe tu plantilla, puedes usarla en una campaña de WhatsApp o Canvas.

1. Ve a **Campañas** y selecciona **Crear campaña** > **WhatsApp**.  
2. En el creador de mensajes, selecciona tu plantilla aprobada.  
3. Braze completa automáticamente el contenido de la plantilla, incluyendo cualquier multimedia y Liquid que hayas introducido durante la creación de la plantilla, para que no tengas que volver a ingresarlo.  
4. Actualiza cualquier contenido variable o personalización según sea necesario. Los campos bloqueados por Meta (mostrados en gris) no se pueden editar. Para cambiar contenido bloqueado, debes editar y volver a enviar la plantilla para su aprobación.  
5. Usa la pestaña **Prueba** para previsualizar el mensaje, actualizar las variables del cuerpo y confirmar que el mensaje se ve como esperas antes de lanzar.

Para más información sobre cómo crear campañas de WhatsApp, consulta [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/).

## Preguntas frecuentes

### ¿Cuánto tarda la revisión de plantillas de Meta?

Las revisiones normalmente se completan en cinco minutos, pero pueden tardar hasta 24 horas.

### ¿Puedo editar una plantilla después de que ha sido aprobada?

Cualquier cambio en el contenido bloqueado (texto del cuerpo u otros campos controlados por Meta) requiere volver a enviar la plantilla para su aprobación, lo cual debe hacerse desde WhatsApp Business Manager. Puedes actualizar el contenido y la personalización al construir tu campaña o Canvas.

### ¿Qué pasa con las plantillas que envié antes de que el constructor de plantillas estuviera disponible?

Las plantillas creadas en Meta Business Manager siguen disponibles para usar en Braze. El constructor de plantillas es una forma adicional de crear y administrar plantillas sin salir del dashboard de Braze.

### ¿Por qué no puedo añadir personalización a todos los campos?

Meta restringe qué partes de una plantilla se pueden personalizar. El botón **+** (más) solo aparece en los campos que admiten contenido variable.