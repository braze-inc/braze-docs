---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "Este artículo de referencia cubre los pasos necesarios para crear un mensaje de WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows es una mejora del canal de mensajería de WhatsApp existente, que te permite crear experiencias de mensajería interactivas y dinámicas. Esta página proporciona instrucciones paso a paso para utilizar WhatsApp Flows.

## Configuración de los Flujos de WhatsApp

1. Conéctate a tu cuenta Meta.
2. Crea Flujos desde una de las dos ubicaciones principales:
    - **Herramientas de la cuenta:** Ve a la pestaña **Flujos** para ver el ID del Flujo y crear un nuevo Flujo.
    - **Administra plantillas:** Este es el método recomendado para crear Flujos. Aquí puedes generar plantillas y seleccionar una opción de Flujo durante el proceso de creación de plantillas.

![Administrador de WhatsApp con una página para crear una plantilla de Flujos.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Selecciona un Flujo existente o crea uno. Si creas un Flujo, elige entre dos opciones:
  - **Formulario personalizado:** Para requisitos específicos
  - **Elementos prediseñados:** Para una configuración más rápida

## Configuración de mensajes y respuestas de WhatsApp Flow

{% tabs local %}
{% tab Template message %}

1. En un Canvas de Braze, crea un paso en mensaje de WhatsApp que utilice la plantilla de mensaje que contiene el Flujo respectivo.
2. Continúa creando tu plantilla. Si es necesario, añade medios, contenido variable o ambos a tu mensaje. Tu selección de Flujo se elige cuando se confecciona la plantilla, por lo que no se requiere información adicional para la experiencia de flujo.

![Creador de mensajes de WhatsApp utilizando una plantilla de flujo de WhatsApp.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. En un Canvas de Braze, crea un paso de mensaje de WhatsApp que utilice un mensaje de respuesta y un mensaje de flujo.

![Un paso de mensaje para un tipo de mensaje de respuesta de WhatsApp y un diseño de mensaje de flujo.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Selecciona el Flujo correspondiente y continúa creando tu mensaje. 

![Un creador de mensajes de respuesta a un Flujo con un desplegable ampliado para seleccionar un Flujo.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Vista previa del Flow

Antes de lanzar un Canvas con un Flujo, puedes seleccionar **Vista previa Flujo** para previsualizar el Flujo directamente en Braze y confirmar que se comporta como se espera. También puedes interactuar con el Flujo en la vista previa para experimentar cómo navegaría un usuario por el Flujo, y luego hacer ajustes en tiempo real. Si un Flujo contiene varias páginas, puedes interactuar con cada una de ellas.

![Ventana de vista previa que muestra un formulario para que un usuario termine de registrarse.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Guardar la respuesta de Flujo completo {#full-flow}

Al incorporar un mensaje de WhatsApp Flow a un Braze Canvas o a una campaña, puede que quieras capturar y utilizar información específica que los usuarios envíen a través del Flow. Braze necesita recibir información adicional sobre la estructura de la respuesta del usuario, concretamente sobre la forma prevista de la respuesta JSON, para generar el esquema de atributos personalizados anidados (NCA) requerido.

### Paso 1: Genera el atributo personalizado Flujo

{% tabs local %}
{% tab Recommended method %}

La forma más sencilla de dar a Braze la información sobre la estructura de la respuesta es guardar la respuesta Flujo como un atributo personalizado y completar un envío de prueba.

#### Utilizar un flujo que no se ha utilizado en Braze

Si estás utilizando un Flujo que no se ha utilizado previamente en Braze, al ver la sección **Atributo personalizado del Flujo** en **Redactar mensajes**, es posible que no veas ninguna información. Esto significa que aún no se ha generado el esquema.

![Sección Meta Flow con una opción para ver el atributo personalizado Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Para resolverlo, haz lo siguiente:

1. Paso 1\. Completa la configuración de tus mensajes de WhatsApp.
2. Confirma que has marcado **Guardar respuestas de flujo como atributo personalizado**.

![Sección Meta Flow con una casilla de verificación para guardar las respuestas Flow como un atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Envíate un mensaje de prueba y completa el Flujo como usuario.

Ahora, Braze tiene la forma del JSON de respuesta del Flujo y puede generar el atributo personalizado.

{% endtab %}
{% tab Alternative methods %}

Utiliza el editor JSON avanzado para guardar atributos de la respuesta del Flujo en atributos personalizados, o utiliza un Canvas de varios pasos para guardar la respuesta en un atributo personalizado anidado. 

{% subtabs %}
{% subtab Advanced JSON editor %}

En el editor JSON avanzado, introduce {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, donde “flow_1” es el atributo personalizado en el que quieres que se guarde el flujo.

![Paso de actualización de usuarios con un editor JSON avanzado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Confirma que ya has creado un atributo personalizado con el tipo de datos de objeto ("flow_1" en este ejemplo) dentro de la configuración de datos de tu espacio de trabajo.
2. En el editor de interfaz de usuario, utiliza Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` para rellenar el atributo personalizado y guardar en él toda la respuesta Flow del usuario. Tienes que rellenar el valor clave como ```{{whats_app.${inbound_flow_response}}}```{% endraw %} antes de seleccionar el atributo personalizado que has creado.

![Paso de actualización de usuario que utiliza el editor de IU.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Después de que Braze reciba una respuesta de Flujo, guardaremos el atributo personalizado anidado con la denominación prescrita en el perfil de usuario. Ese atributo personalizado puede extraerse al crear Lienzos. 

![Una ventana que muestra el contenido de un atributo personalizado de "flow_1".]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Ver la respuesta de Flujo guardada

Cuando se completa el Flujo, Braze crea automáticamente un atributo personalizado del Flujo con un nombre basado en el ID del Flujo. A continuación, puedes ir al perfil de usuario para ver la respuesta de Flujo guardada como un objeto anidado en la sección **Atributos personalizados**.

Una vez generado el esquema, la sección **Atributo personalizado** del flujo mostrará la estructura esperada, incluidos los tipos de datos previstos para cada respuesta (por ejemplo, "Cadena" o "Matriz de cadenas").

![Ventana de detalles de atributos personalizados de flujo con desplegable de esquema.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Consideraciones

- **Atributos existentes:** Si ya se ha generado un atributo personalizado para un Flujo concreto, el Flujo se cargará con la información del atributo disponible. En estos casos, no necesitas enviar un mensaje de prueba para generar el esquema, ya que Braze ya reconoce los mensajes de respuesta esperados.
- **Cambios de flujo:** Si realizas algún cambio en el Flujo después de que se genere el esquema, debes enviar un mensaje de prueba adicional para que Braze pueda entender que la forma de la respuesta del Flujo ha cambiado y ajustar la estructura de atributos en consecuencia. Esta acción está limitada a una vez cada 24 horas. 
- **Coherencia:** El atributo personalizado del Flujo generado es coherente y será el mismo atributo para este Flujo concreto, independientemente del Canvas en el que se utilice.
- **Opción manual:** No es necesario que selecciones la casilla de verificación **Guardar respuestas de flujo como atributo personalizado**. Puedes generar manualmente el atributo personalizado [guardando campos específicos de las respuestas del Flujo en un atributo personalizado concreto](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), lo que evita duplicar los pasos del usuario.

## Guardar campos específicos de respuestas de Flujo en un atributo personalizado específico 

### Paso 1: Crear una ruta de acción

Crea un paso en Canvas [de Ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) o una campaña basada en la acción. Selecciona un desencadenante de **Enviar un mensaje entrante de WhatsApp** y la condición **Respondido al flujo** y, a continuación, selecciona el Flujo correspondiente o **Cualquier flujo**.

![Un desencadenante para los usuarios que enviaron un mensaje entrante de WhatsApp y respondieron a cualquier Flujo.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Paso 2: Extraer campos de las respuestas de Flujo

Puedes utilizar atributos personalizados anidados o la etiqueta de Liquid `json_parse` para extraer campos específicos de las respuestas de Flow.

{% tabs %}
{% tab Nested custom attributes %}

Para guardar partes específicas de la [respuesta de Flujo](#full-flow) del usuario, completa todos los pasos de [Guardar la respuesta de Flujo completa](#full-flow), **incluido el lanzamiento del Canvas**. El Canvas debe iniciarse para crear el atributo personalizado anidado al que harás referencia. Tras iniciar el Canvas y completar un Flujo, sigue los siguientes pasos:

1. Crea un paso posterior de Actualización de Usuario que utilice el editor de IU.
2. Selecciona **Añadir personalización** y, a continuación, selecciona **Atributo personalizado anidado** y el correspondiente atributo de nivel superior donde se almacena el Flujo.  

![Paso de actualización de usuario con una personalización de atributos personalizados anidados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Selecciona el atributo clave que quieras guardar e inserta el Liquid en el campo **Valor clave**.

![Ventana para "flow_1" con atributos para seleccionar.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Elige el atributo donde quieres almacenarlo.
5\. Envía un mensaje de prueba para probar el Flujo.

{% endtab %}
{% tab Parse function %}

Utiliza la etiqueta de Liquid `json_parse` para extraer respuestas específicas del flujo. Por ejemplo, puedes extraer el token de Flujo y las opciones seleccionadas para personalizar un mensaje de seguimiento.

En el editor de IU, selecciona lo siguiente: 

- **Nombre del atributo:** YOUR_CUSTOM_ATTRIBUTE (en este ejemplo: “First_name”)
- **Acción:** Actualizar
- **Valor clave:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![Creador de mensajes de WhatsApp con un componente "Añadir personalización" para insertar una personalización de propiedades de WhatsApp con el atributo personalizado `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Cuando estés listo, envía un mensaje de prueba para comprobar el Flujo. Después, ¡lanza el Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Un nuevo mensaje de WhatsApp "borra" la capacidad del Canvas de utilizar (y reutilizar) la respuesta del Flujo Líquido, así que asegúrate de que los mensajes de seguimiento sean posteriores a todos los pasos de Actualización de usuario, webhooks u otros pasos que utilicen la respuesta del Flujo Líquido.
{% endalert %}

## Añadir una etiqueta de personalización de Flujo

Para utilizar la respuesta Flujo a través de Liquid con [etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), completa los siguientes pasos:

1. Cuando redactes tu mensaje de WhatsApp, selecciona el icono más para abrir la ventana **Añadir personalización** 
2. Selecciona **Propiedades de WhatsApp** para el tipo de personalización y **inbound_flow_response** para el atributo personalizado. Puede utilizarse para guardar información en perfiles de usuario, incluirla en mensajes o reenviarla a otros servicios, como webhooks.

![Creador de mensajes de WhatsApp con un componente "Añadir personalización" para insertar una personalización de propiedades de WhatsApp con el atributo personalizado inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Si tienes alguna duda o necesitas más ayuda, ponte en contacto con [el Servicio de Asistencia]({{site.baseurl}}/braze_support/).