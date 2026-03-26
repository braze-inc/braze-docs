---
nav_title: Plantillas de carrusel
article_title: Plantillas de carrusel de WhatsApp
description: "Este artículo de referencia cubre las plantillas de carrusel de WhatsApp."
tool:
  - WhatsApp
alias: /whatsapp_carousel_templates/
toc_headers: h2
---

# Plantillas de carrusel de WhatsApp

> Las plantillas de carrusel de WhatsApp te permiten crear mensajes interactivos con múltiples tarjetas por las que los usuarios pueden deslizarse. Cada carrusel puede contener hasta 10 tarjetas con imágenes o videos, junto con botones personalizables para la interacción. Esta característica es ideal para mostrar tus productos y servicios, o contenido de varios pasos en un formato visualmente atractivo.

{% alert note %}
Las plantillas de carrusel de WhatsApp están en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si te interesa participar en este acceso anticipado.
{% endalert %}

## Requisitos previos

{% multi_lang_include whatsapp/carousel_template_prerequisites.md %}

## Crear una plantilla de carrusel

Puedes crear plantillas de carrusel dentro de Braze con el constructor de plantillas de WhatsApp. Cuando creas plantillas, Braze valida tu contenido para cumplir con los criterios de Meta.

Al crear una plantilla en Braze, puedes usar:
- Liquid que esperas utilizar al enviar el mensaje. Braze lo guarda para referencia futura.
- Variables genéricas como {% raw %}`{{1}}`{% endraw %}.

{% alert note %}
Las etiquetas de Liquid {% raw %}`{% %}`{% endraw %} no son compatibles en el constructor de plantillas porque no pasan los criterios de contenido de Meta. 
{% endalert %}

Después de enviar la plantilla, aparece en la lista de plantillas de la WABA y se revisa en un plazo de 24 horas. Sin embargo, la revisión suele ocurrir en pocos minutos.

### Paso 1: Acceder al constructor de plantillas

1. En Braze, ve a **Plantillas**.
2. Selecciona **WhatsApp Templates** de las opciones disponibles.

![WhatsApp Templates en el menú de navegación de plantillas.]({% image_buster /assets/img/whatsapp/templates/whatsapp_templates.png %}){: style="max-width:70%;"}

{: start="3"}
3. Selecciona **Create Carousel Template**.

![Botón para crear una plantilla de carrusel.]({% image_buster /assets/img/whatsapp/templates/create_carousel_template.png %})

### Paso 2: Configurar los ajustes de la plantilla

Completa los campos obligatorios.

| Campo | Descripción |
| --- | --- |
| Cuenta de WhatsApp Business | Selecciona la WABA donde se almacenará esta plantilla. Recuerda que todos los grupos de suscripción y números de teléfono dentro de esta WABA tendrán acceso a la plantilla. |
| Idioma de la plantilla | Selecciona el idioma para tu plantilla. Meta restringe las plantillas a un solo idioma, así que elige el idioma que verá tu audiencia. |
| Nombre de la plantilla | Introduce un nombre descriptivo que te ayude a identificar esta plantilla más adelante. Los nombres de plantilla no pueden contener espacios; usa guiones bajos o elimina los espacios por completo (como `carousel_example` o `carouselexample`). |
| Categoría | Se establece automáticamente como **Marketing**. Todos los mensajes de carrusel se categorizan como mensajes de marketing. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Panel de detalles de la plantilla de WhatsApp con una cuenta de WhatsApp Business seleccionada, inglés como idioma de la plantilla y un nombre de plantilla "welcome_message".]({% image_buster /assets/img/whatsapp/templates/whatsapp_template_details.png %}){: style="max-width:70%"}

### Paso 3: Añadir contenido del cuerpo

Cada mensaje de carrusel debe comenzar con contenido del cuerpo, que es el texto que aparece encima de las tarjetas del carrusel.

Puedes incluir variables de Liquid para personalización, como {% raw %}`{{first_name}}`{% endraw %}, que crea un espacio de variable vacío que puede llenarse con contenido dinámico o modificarse más adelante al usar la plantilla en campañas. Las variables no pueden colocarse al principio ni al final del contenido del cuerpo.

### Paso 4: Configurar los ajustes del carrusel

Antes de crear tarjetas individuales, define la estructura general del carrusel con los ajustes del carrusel. Estos ajustes se aplican a todas las tarjetas y no pueden cambiarse después de enviar la plantilla.

#### Tipo de medio

Elige el tipo de medio: **Imagen** o **Video**. Se usa para todas las tarjetas.

![Compositor con opciones para seleccionar un tipo de medio de imagen o video.]({% image_buster /assets/img/whatsapp/templates/media_types.png %})

#### Configuración de botones

Elige el tipo de botón: **Respuesta rápida**, **Número de teléfono** o **Visitar sitio web**. Esta configuración se usa para todas las tarjetas. Luego, selecciona hasta dos botones por tarjeta.

### Paso 5: Crear tarjetas del carrusel

Ahora puedes crear tarjetas individuales del carrusel. Todas las tarjetas mantienen la misma forma y estructura. Puedes añadir hasta 10 tarjetas, pero debes añadir al menos dos.

{% alert important %}
No puedes cambiar el número de tarjetas después de enviar la plantilla a Meta para revisión.
{% endalert %}

1. Carga una imagen o video, según el tipo de medio seleccionado.
2. Añade texto o una descripción a la tarjeta.
3. Configura el texto y las acciones de los botones.
4. Añade variables de Liquid donde sea necesario. Puedes añadirlas donde haya un botón **+** de más.

{% alert tip %}
Usa variables de Liquid estratégicamente para personalizar contenido como porcentajes de descuento, nombres de productos u ofertas específicas para el usuario. Las variables pueden añadirse al texto de la tarjeta, texto de los botones y URLs.
{% endalert %}

![Compositor con tarjetas de carrusel de ejemplo promocionando alimentos nutritivos.]({% image_buster /assets/img/whatsapp/templates/example_carousel_cards.png %})

### Paso 6: Vista previa y envío

1. Usa la sección **Vista previa** para ver cómo aparecerá tu carrusel a los usuarios.
2. Selecciona **Submit to Meta for review** para que Braze envíe la plantilla a Meta para su aprobación.
3. La aprobación generalmente toma unos minutos, pero puede tardar hasta 24 horas.
4. Verifica el estado de la plantilla en tu lista de **Plantillas** en la página de plantillas de WhatsApp o en el selector de Canvas y campañas.

{% alert note %}
El envío de prueba no está disponible hasta que Meta apruebe la plantilla. El estado de la plantilla se muestra como **Draft** durante la creación y cambia a **Approved** después de que Meta complete la revisión.
{% endalert %}

## Usar plantillas de carrusel

Después de que Meta apruebe tu plantilla de carrusel, puedes usarla en campañas y Canvas. El proceso es similar para ambos tipos de mensaje.

### Paso 1: Crear un mensaje de WhatsApp

1. En Braze, ve a **Campañas** o **Canvas** y crea un mensaje de WhatsApp.
2. Selecciona el grupo de suscripción que corresponde a la cuenta de WhatsApp Business (WABA) de tu plantilla.

{% alert important %}
Si tienes múltiples cuentas de WhatsApp Business, selecciona un grupo de suscripción de la misma WABA donde se creó la plantilla. Las plantillas no se comparten entre WABAs, pero sí se comparten entre todos los grupos de suscripción y números de teléfono dentro de la misma WABA.
{% endalert %}

### Paso 2: Seleccionar tu plantilla de carrusel

1. Busca tu plantilla por nombre (como "carousel_example").
2. Verifica que el estado de la plantilla sea **Approved**.
3. Selecciona la plantilla para cargarla en el creador de mensajes.

### Paso 3: Personalizar el contenido dinámico

Cuando tu plantilla se carga, contiene contenido bloqueado y editable.

{% tabs local %}
{% tab Contenido bloqueado %}


- El texto estático (cualquier contenido enviado sin variables) está bloqueado y no puede editarse.
- El número de tarjetas del carrusel es fijo.
- El tipo de medio y la configuración de botones no pueden cambiarse.

{% endtab %}
{% tab Contenido editable %}


{% raw %}
- Cualquier campo con una variable puede modificarse con diferente Liquid.
- Si enviaste la plantilla con Liquid (por ejemplo, `{{first_name}}`), Braze lo preserva y muestra automáticamente.
- Puedes cambiar el Liquid a diferentes variables (por ejemplo, cambiar de `{{first_name}}` a `{{last_name}}`).
- Las imágenes con variables pueden hacerse dinámicas usando URLs con Liquid.
- Puedes cargar nuevas imágenes desde la biblioteca de medios de Braze en lugar de usar los medios enviados. 
{% endraw %}

#### Ejemplo

{% raw %}Por ejemplo, supongamos que tu plantilla incluye una variable de porcentaje de descuento: `{{discount_percentage}}`. En la campaña, puedes mantenerla o cambiarla a `{{custom_attributes.vip_discount}}`.{% endraw %} Meta solo requiere que el espacio de la variable esté lleno; el Liquid específico utilizado es flexible.

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar tu campaña o Canvas

Después de la composición, continúa con el flujo de trabajo de lanzamiento de tu campaña o Canvas, incluyendo las pruebas. La plantilla de carrusel funciona como cualquier otra plantilla de mensaje de WhatsApp.

## Mejores prácticas

### Directrices de contenido

- **Ubicación del contenido del cuerpo:** Las variables no pueden colocarse al final del contenido del cuerpo. Añade al menos una palabra o signo de puntuación después de cada variable.
- **Estructura de tarjetas consistente:** Todas las tarjetas deben tener la misma forma, tipo de medio y configuración de botones. Planifica tu contenido en consecuencia.
- **Cantidad óptima de tarjetas:** Aunque puedes crear hasta 10 tarjetas, considera la experiencia del usuario. Demasiadas tarjetas pueden resultar abrumadoras; de 3 a 5 tarjetas funcionan bien para la mayoría de los casos de uso.
- **Valores predeterminados:** Al usar variables de Liquid, siempre proporciona valores predeterminados para una vista previa precisa. Esto ayuda a confirmar que el mensaje se muestra correctamente si faltan ciertos datos del perfil de usuario.

### Cuentas de WhatsApp Business y grupos de suscripción

- **Entiende cómo se comparten las plantillas:** Las plantillas se comparten entre todos los grupos de suscripción dentro de la misma cuenta de WhatsApp Business (WABA), pero no entre diferentes WABAs. Planifica en consecuencia si administras múltiples WABAs.
- **Organiza por WABA:** Si tienes múltiples WABAs, considera organizar tus plantillas por cuenta de negocio para evitar confusiones al seleccionar plantillas en campañas.

### Pruebas y aprobación

- **Vista previa antes del envío:** Siempre revisa la vista previa de tus plantillas para detectar errores antes de enviarlas a Meta para su aprobación.
- **Planifica el tiempo de aprobación:** Aunque la aprobación generalmente toma solo unos minutos, ten en cuenta posibles retrasos al planificar los lanzamientos de campañas.
- **Prueba a fondo:** Después de la aprobación, prueba tu carrusel con datos reales de usuarios para confirmar que todas las variables se completan correctamente y que la experiencia del usuario es fluida.

## Solución de problemas

| Problema | Solución |
| --- | --- |
| La plantilla no aparece en la campaña | Verifica que el grupo de suscripción seleccionado pertenezca a la misma WABA que la plantilla. También, comprueba que el estado de la plantilla sea **Approved** y no esté aún en estado **Draft** o **Pending**. |
| No se puede colocar una variable al final del cuerpo | Mueve la variable antes en el texto y añade al menos un carácter o signo de puntuación después. Este es un requisito de Meta para las plantillas de WhatsApp. |
| Las variables no se completan en la prueba | Asegúrate de que la sintaxis de Liquid sea correcta y que los atributos existan en los perfiles de usuario. Revisa si hay errores tipográficos en los nombres de las variables y verifica que los valores predeterminados estén configurados donde corresponda. |
| El nombre de la plantilla tiene espacios | Los nombres de plantilla no pueden contener espacios. Usa guiones bajos en su lugar (`template_name`) o elimina los espacios por completo (`templatename`). |
| No se puede cambiar el número de tarjetas | El número de tarjetas se fija cuando creas la plantilla y no puede cambiarse después del envío. Si necesitas un número diferente de tarjetas, tendrás que crear una nueva plantilla. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }