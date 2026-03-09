---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "Este artículo de referencia describe los pasos necesarios para desarrollar y crear un mensaje de WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows es una mejora del canal WhatsApp existente que te permite crear experiencias de mensajería interactivas y dinámicas. Esta página proporciona instrucciones paso a paso para utilizar WhatsApp Flows.

## Configuración de WhatsApp Flows

1. Inicia sesión en tu cuenta de Meta.
2. Crea flujos desde una de las dos ubicaciones principales:
    - **Herramientas de la cuenta:** Ve a la pestaña **Flujos** para ver el ID del flujo y crear un nuevo flujo.
    - **Administrar plantillas:** Este es el método recomendado para crear flujos. Aquí puedes generar plantillas y seleccionar una opción de flujo durante el proceso de creación de plantillas.

![WhatsApp Administrador con una página para crear una plantilla de Flows.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Selecciona un flujo existente o crea uno nuevo. Si vas a crear un flujo, elige entre dos opciones:
  - **Formulario personalizado:** Para requisitos específicos
  - **Elementos prediseñados:** Para una configuración más rápida

## Configuración de mensajes y respuestas de WhatsApp Flow

{% tabs local %}
{% tab Template message %}

1. En BRAZE CANVAS, crea un paso de mensaje de WhatsApp que utilice la plantilla de mensaje que contiene el flujo correspondiente.
2. Continúa creando tu plantilla. Si es necesario, añade medios, contenido variable o ambos a tu mensaje. Tu selección de flujo se elige al crear la plantilla, por lo que no se requiere información adicional para la experiencia de flujo.

![Creador de mensajes de WhatsApp utilizando una plantilla de WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. En BRAZE CANVAS, crea un paso de mensaje de WhatsApp que utilice un mensaje de respuesta y un mensaje de flujo.

![Un paso de mensaje para un tipo de mensaje de respuesta de WhatsApp y un diseño de mensaje de Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Selecciona el flujo correspondiente y continúa creando tu mensaje. 

![Un creador de respuestas de mensajes de Flow con un menú desplegable ampliado para seleccionar un Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Vista previa del Flow

Antes de lanzar un Canvas con un flujo, puedes seleccionar **Vista previa del flujo** para obtener una vista previa del flujo directamente en Braze y confirmar que funciona según lo esperado. También puedes interactuar con el flujo en la vista previa para experimentar cómo navegaría un usuario por el flujo y, a continuación, realizar ajustes en tiempo real. Si un flujo contiene varias páginas, puedes interactuar con cada una de ellas.

![Ventana de vista previa que muestra un formulario para que el usuario se registre.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Guardar la respuesta completa de Flow {#full-flow}

Al incorporar un mensaje de WhatsApp Flow en un BRAZE CANVAS o una campaña, es posible que quieras capturar y utilizar información específica que los usuarios envían a través del Flow. Braze necesita recibir información adicional sobre la estructura de la respuesta del usuario, concretamente la forma prevista de la respuesta JSON, para generar el esquema de atributos personalizados anidados (NCA) necesario.

### Paso 1: Generar el atributo personalizado Flow

{% tabs local %}
{% tab Recommended method %}

La forma más sencilla de proporcionar a Braze la información sobre la estructura de la respuesta es guardar la respuesta del flujo como un atributo personalizado y completar un envío de prueba.

#### Usar un flujo que no se ha utilizado en Braze

Si utilizas un flujo que no se ha utilizado anteriormente en Braze, es posible que no veas ninguna información al consultar la sección **de atributos personalizados del flujo** en **Redactar mensajes**. Esto significa que el esquema aún no se ha generado.

![Sección Meta Flow con una opción para ver el atributo personalizado Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Para resolver esto, haz lo siguiente:

1. Completa la configuración del paso del mensaje de WhatsApp.
2. Confirma que has marcado **Guardar respuestas de flujo como atributo personalizado**.

![Sección Meta Flow con una casilla de verificación para guardar las respuestas de Flow como un atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Envíate un mensaje de prueba y completa el flujo como usuario.

Ahora, Braze tiene la forma de la respuesta JSON de Flow y puede generar el atributo personalizado.

{% endtab %}
{% tab Alternative methods %}

Utiliza el editor JSON avanzado para guardar los atributos de la respuesta de Flow en atributos personalizados, o utiliza un Canvas de varios pasos para guardar la respuesta en un atributo personalizado anidado. 

{% subtabs %}
{% subtab Advanced JSON editor %}

En el editor JSON avanzado, introduce {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, donde“flow_1”  es el atributo personalizado en el que deseas guardar el flujo.

![Paso de actualización de usuario con un editor JSON avanzado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Confirma que ya has creado un atributo personalizado con el tipo de datos de("flow_1" objeto  en este ejemplo) dentro de la configuración de datos de tu espacio de trabajo.
2. En el editor de interfaz de usuario, utiliza Liquid{% raw %}```{{whats_app.${inbound_flow_response}}}```  para rellenar el atributo personalizado y guardar toda la respuesta de Flow del usuario en él. Debes rellenar el valor clave como```{{whats_app.${inbound_flow_response}}}```{% endraw %}  antes de seleccionar el atributo personalizado que has creado.

![Paso de actualización de usuario que utiliza el editor de interfaz de usuario.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Una vez que Braze reciba una respuesta de Flow, guardaremos el atributo personalizado anidado con el nombre prescrito en el perfil de usuario. Ese atributo personalizado se puede extraer al crear lienzos. 

![Una ventana que muestra el contenido de un "flow_1"atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Ver la respuesta de flujo guardada

Cuando se completa el flujo, Braze crea automáticamente un atributo personalizado del flujo con un nombre basado en el ID del flujo. A continuación, puedes ir al perfil de usuario para ver la respuesta de Flow guardada como un objeto anidado en la sección **Atributos personalizados**.

Una vez generado el esquema, la sección **Atributo personalizado** de flujo mostrará la estructura esperada, incluidos los tipos de datos previstos para cada respuesta (por ejemplo, «Cadena» o «Matriz de cadenas»).

![Ventana de detalles de atributos personalizados de flujo con menú desplegable de esquema.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Consideraciones

- **Atributos existentes:** Si ya se ha generado un atributo personalizado para un flujo concreto, el flujo se cargará con la información del atributo disponible. En estos casos, no es necesario enviar un mensaje de prueba para generar el esquema, ya que Braze ya reconoce los mensajes de respuesta esperados.
- **Cambios en el flujo:** Si realizas algún cambio en el flujo después de que se genere el esquema, debes enviar un mensaje de prueba adicional para que Braze pueda comprender que la forma de la respuesta del flujo ha cambiado y ajustar la estructura de los atributos en consecuencia. Esta acción está limitada a una vez cada 24 horas. 
- **Coherencia:** El atributo personalizado generado por Flow es coherente y será el mismo atributo para este Flow específico, independientemente del Canvas en el que se utilice.
- **Opción manual:** No es necesario que selecciones la casilla **Guardar respuestas de flujo como atributo personalizado**. Puedes generar manualmente el atributo personalizado [guardando campos específicos de las respuestas de Flow en un atributo personalizado específico](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), lo que evita duplicar los pasos del usuario.

## Guardar campos específicos de las respuestas de Flow en un atributo personalizado específico 

### Paso 1: Crear una ruta de acción

Crea un paso en Canvas [de ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) o una campaña basada en acciones. Selecciona un desencadenante **Enviar un mensaje entrante de WhatsApp** y la condición **Respondido al flujo**, y luego selecciona el flujo relevante o **Cualquier flujo**.

![Un desencadenante para los usuarios que enviaron un mensaje entrante de WhatsApp y respondieron a cualquier flujo.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Paso 2: Extraer campos de las respuestas de Flow

Puedes utilizar atributos personalizados anidados o la etiqueta`json_parse` de Liquid para extraer campos específicos de las respuestas de Flow.

{% tabs %}
{% tab Nested custom attributes %}

Para guardar partes específicas de la respuesta de Flow del usuario, completa todos los pasos descritos en [Guardar la respuesta completa de Flow](#full-flow), **incluido el inicio de Canvas**. Debes iniciar Canvas para crear el atributo personalizado anidado al que harás referencia. Después de iniciar Canvas y completar un flujo, sigue estos pasos:

1. Crea un paso posterior de actualización de usuario que utilice el editor de interfaz de usuario.
2. Selecciona **Añadir personalización**, luego selecciona **Atributo personalizado anidado** y el atributo de nivel superior correspondiente donde se almacena el flujo.  

![Paso de actualización del usuario con una personalización de atributos personalizados anidados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Selecciona el atributo clave que deseas guardar e inserta Liquid en el campo **Valor clave**.

![Ventana con"flow_1" atributos entre los que elegir.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Elige el atributo donde deseas almacenarlo.
5\. Envía un mensaje de prueba para comprobar el flujo.

{% endtab %}
{% tab Parse function %}

Utiliza la etiqueta`json_parse` de Liquid para extraer respuestas específicas del flujo. Por ejemplo, puedes extraer el token Flow y las opciones seleccionadas para personalizar un mensaje de seguimiento.

En el editor de interfaz de usuario, selecciona lo siguiente: 

- **Nombre del atributo:**YOUR_CUSTOM_ATTRIBUTE  (en este ejemplo: “First_name”)
- **Acción:** Actualizar
- **Valor clave:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![Creador de mensajes de WhatsApp con un componente «Añadir personalización» para insertar una personalización de las propiedades de WhatsApp con el atributo `inbound_flow_response`.]({%image_buster/assets/img/whatsapp/flows/parsed_json.pngpersonalizado    %})

Cuando estés listo, envía un mensaje de prueba para comprobar el flujo. A continuación, ¡inicia Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Un nuevo mensaje de WhatsApp «borra» la capacidad de Canvas para utilizar (y reutilizar) la respuesta de Liquid Flow, así que asegúrate de que los mensajes de seguimiento se envíen después de todos los pasos de actualización del usuario, webhooks u otros pasos que utilicen la respuesta de Liquid Flow.
{% endalert %}

## Añadir una etiqueta de personalización de Flow

Para utilizar la respuesta Flow a través de Liquid con [etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), sigue estos pasos:

1. Al redactar tu mensaje de WhatsApp, selecciona el icono más para abrir la ventana **Añadir personalización.**
2. Selecciona **Propiedades de WhatsApp** para el tipo de personalización y**inbound_flow_response**  para el atributo personalizado. Esto se puede utilizar para guardar información en perfiles de usuario, incluirla en mensajes o reenviarla a otros servicios, como webhooks.

![Creador de mensajes de WhatsApp con un componente «Añadir personalización» para insertar una personalización de las propiedades de WhatsApp con el atributo inbound_flow_response.]({%image_buster/assets/img/whatsapp/flows/inbound_flow_response.pngpersonalizado    %}){: style="max-width:80%;"}

Si tienes alguna pregunta o necesitas ayuda, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/braze_support/).