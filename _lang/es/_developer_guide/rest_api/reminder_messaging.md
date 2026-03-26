---
nav_title: Mensajería de recordatorios seleccionados por el usuario
article_title: Mensajería de recordatorios seleccionados por el usuario
page_order: 5
page_type: reference
description: "Este artículo de referencia explica cómo usar las páginas de inicio de Braze, los atributos personalizados y las campañas para permitir que los usuarios se registren para recibir mensajes de recordatorio personalizados sobre próximos eventos o citas."
---

# Mensajería de recordatorios seleccionados por el usuario

> Usa las [páginas de inicio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) de Braze, los atributos personalizados y las campañas para permitir que los usuarios elijan cuándo quieren recibir mensajes de recordatorio sobre próximos eventos o citas. Este enfoque permite que los usuarios no técnicos de Braze creen y editen el contenido de las páginas de registro de recordatorios, mientras que las preferencias que seleccionan los usuarios pueden impulsar la segmentación, la orientación y la personalización en toda tu mensajería con Braze.

Con este enfoque, puedes:

- Permitir que los usuarios seleccionen la fecha de su mensaje de recordatorio en relación con un próximo evento.
- Capturar preferencias directamente de los usuarios mediante una página de inicio de Braze y escribirlas en los perfiles de usuario, sin necesidad de un backend adicional.
- Enviar mensajes en las fechas que los usuarios elijan, para que la mensajería sea relevante y basada en permisos.
- Ampliar el caso de uso con características adicionales de Braze, como retrasos de mensajes, reorientación de seguimiento y pruebas A/B.

## Requisitos previos

Para completar esta guía, necesitas:

| Requisito | Descripción |
| --- | --- |
| Acceso a páginas de inicio | Acceso y permisos para crear [páginas de inicio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) en Braze. |
| Conocimientos de HTML y JavaScript | Familiaridad básica con HTML y JavaScript para personalizar tu página de inicio. Solo es necesario para la [Opción B](#option-b-personal-dates-custom-code-block). |
| Conocimientos de Liquid | Familiaridad básica con [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para crear plantillas de variables personalizadas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 1: Crea una página de inicio y enlázala desde un mensaje

Primero, [crea una página de inicio de Braze]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/). Luego, crea un mensaje (como un correo electrónico) que dirija a los usuarios a la página de inicio.

{% raw %}
Para asociar automáticamente la actividad de la página de inicio con el perfil de usuario del destinatario, usa la etiqueta de Liquid `{% landing_page_url %}` al enlazar a la página desde un mensaje de Braze. Por ejemplo:

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

Cuando un usuario hace clic en este enlace, Braze lo identifica automáticamente, de modo que cualquier preferencia que envíe se escribe en su perfil existente, sin necesidad de parámetros de URL manuales. Para un recorrido completo, consulta [Rastrear usuarios a través de un formulario]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/).

## Paso 2: Captura las preferencias en la página de inicio

La forma en que capturas las preferencias de los usuarios depende de si estás recopilando fechas compartidas o fechas personales. Elige la opción que se ajuste a tu caso de uso.

### Opción A: Fechas compartidas (bloques de formulario de arrastrar y soltar)

Para eventos en los que muchos usuarios comparten la misma fecha (como días festivos o eventos deportivos), usa los [bloques de formulario de **casilla de verificación**]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks) integrados en el editor de arrastrar y soltar para capturar preferencias. Cada casilla de verificación establece de forma nativa un atributo personalizado booleano (`true` o `false`) en el perfil del usuario cuando se envía el formulario, sin necesidad de código personalizado.

Por ejemplo, agrega una casilla de verificación con la etiqueta "Recordatorio del Super Bowl 2026" que se mapee al atributo personalizado `super_bowl_2026_reminder`. Cuando un usuario marca la casilla y envía el formulario, Braze establece:

```
super_bowl_2026_reminder = true
```

Estos atributos booleanos se pueden usar directamente en los [filtros de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) para construir tu audiencia objetivo.

### Opción B: Fechas personales (bloque de código personalizado)

Para fechas únicas de cada usuario (como cumpleaños o aniversarios), usa un [bloque de **código personalizado**]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#basic-blocks) en tu página de inicio para capturar la fecha y escribirla en Braze usando la API `lpBridge`. Este enfoque te proporciona una entrada de fecha (o selector) y te permite almacenar preferencias en un [array de objetos de atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/), que los bloques de formulario de arrastrar y soltar no admiten.

Cuando los usuarios llegan a través de la etiqueta de Liquid {% raw %}`{% landing_page_url %}`{% endraw %}, Braze ya sabe quiénes son, por lo que tu script solo necesita:

1. Escuchar el clic del botón de envío del formulario.
2. Leer el valor de fecha de tu entrada personalizada.
3. Usar la API `lpBridge` para establecer atributos personalizados anidados y enviar los datos a Braze.

Almacena estas preferencias usando un array de objetos de atributos personalizados anidados. Esta estructura te permite almacenar múltiples recordatorios por usuario y agregar campos derivados más adelante, como `next_reminder_name` o `last_reminder_date`.

#### Script de ejemplo

El siguiente script de ejemplo desactiva el comportamiento predeterminado del botón y ejecuta métodos personalizados al hacer clic en el botón. Reemplaza los ID de los elementos y los valores de los atributos con los tuyos.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

Para encontrar los ID de los elementos de los componentes de tu página de inicio, previsualiza tu página, haz clic derecho y selecciona **Inspeccionar** en tu navegador. Localiza los ID del botón y los componentes de mensaje en el HTML.

## Paso 3: Configura y desencadena los mensajes de recordatorio

Después de recopilar atributos personalizados a través de la página de inicio, crea campañas para enviar mensajes a los usuarios sobre próximos eventos.

### Opción A: Fechas compartidas {#step-3-option-a-shared-dates}

Si usaste atributos personalizados booleanos (Opción A en el [Paso 2](#option-a-shared-dates-dnd-form-blocks)), usa ese atributo como filtro de segmento para construir la audiencia de tu mensaje de recordatorio. Luego crea una nueva campaña, planificada antes del evento, para dirigirte a este grupo con el contenido que elijas.

### Opción B: Fechas personales {#step-3-option-b-personal-dates}

Si usaste atributos personalizados anidados (Opción B en el [Paso 2](#option-b-personal-dates-custom-code-block)), usa el filtro de audiencia **Atributo personalizado anidado** para seleccionar a todos los usuarios que tengan una fecha de recordatorio dentro de una ventana específica, por ejemplo, dos días a partir de ahora.

Para enviar recordatorios de forma continua, configura una campaña recurrente diaria para que cada día los usuarios con recordatorios próximos que caigan dentro de tu ventana reciban sus mensajes.

## Paso 4: Verifica tu integración

Después de completar la configuración, verifica tu integración:

1. Envíate un enlace a la página de inicio y completa el formulario.
2. Navega a tu perfil de usuario en el dashboard de Braze y confirma que el atributo personalizado aparece.
3. Envía un mensaje de recordatorio de prueba a tu perfil y verifica que los detalles personalizados se muestren correctamente.
4. Monitorea los resultados de cerca cuando lances tu campaña.

## Consideraciones

- Para un ejemplo detallado de cómo enviar mensajes basados en atributos personalizados de fecha, consulta el caso de uso de correo electrónico en la [guía de mensajería de la API REST]({{site.baseurl}}/developer_guide/rest_api/messaging/).
- Si duplicas una página de inicio o reemplazas algún campo, los ID de los componentes cambian. Actualiza tu bloque de código personalizado para reflejar los nuevos ID.
- Los atributos personalizados anidados consumen [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) por cada clave en el array de objetos. Actualizar un objeto de atributo personalizado a null también consume un punto de datos.
- El código presentado en esta guía está pensado como un ejemplo ilustrativo. Prueba exhaustivamente todo el código y los componentes en tu entorno antes de desplegarlo en producción.