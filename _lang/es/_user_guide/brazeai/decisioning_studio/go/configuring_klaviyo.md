---
nav_title: Configurar con Klaviyo
article_title: Configurar con Klaviyo para BrazeAI Decisioning Studio
page_order: 3
description: "Aprende a configurar un Flujo Klaviyo para utilizarlo con BrazeAI Decisioning <sup>StudioTM</sup> Go."
toc_headers: h2
---

# Configurar con Klaviyo para BrazeAI Decisioning Studio™ Go

> Configura una plantilla de marcador de posición y un flujo en Klaviyo para desencadenar activaciones a través de BrazeAI Decisioning Studio™ Go.

{% alert important %}
Debes crear un nuevo flujo en Klaviyo para cada nuevo experimentador que configures. Si previamente creaste un flujo marcador de posición para importar tus plantillas, deberás crear un nuevo flujo y no podrás reutilizar el flujo marcador de posición anterior.
{% endalert %}

Antes de crear un flujo en Klaviyo, debes tener como referencia los siguientes datos de tu portal BrazeAI Decisioning Studio™ Go:

- Nombre del flujo
- Nombre del evento desencadenante

## Crear una plantilla de marcador de posición en Klaviyo

BrazeAI Decisioning Studio™ Go importa plantillas que están asociadas a flujos existentes en tu cuenta de Klaviyo. Para utilizar una plantilla que no esté asociada a ningún flujo, puedes crear un flujo marcador de posición que contenga las plantillas que te gustaría utilizar. El flujo puede dejarse como borrador; no es necesario que sea en vivo.

### Paso 1: Configura tu flujo

{% alert note %}
El propósito de este marcador de posición es importar el contenido que desees a BrazeAI Decisioning Studio™ Go. Debes crear un flujo separado en un paso posterior, que BrazeAI Decisioning Studio™ Go utiliza para desencadenar activaciones una vez que tu experimentador está en vivo.
{% endalert %}

1. En Klaviyo, selecciona **Flujos**. 
2. Selecciona **Crear flujo** > **Crear desde cero**.
3. Dale al marcador de posición Flujo un nombre que reconozcas y, a continuación, selecciona **Crear Flujo**.

![Un Flujo llamado "Flujo marcador de posición OFE".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Selecciona cualquier desencadenante y guarda el flujo.
5\. Selecciona **Confirmar y guardar**. 

### Paso 2: Crea la plantilla del marcador de posición

A continuación, crea la plantilla del marcador de posición: 

1. Arrastra y suelta un nodo de **correo electrónico** después del **desencadenante**.

![Un flujo con un nodo desencadenante seguido de un nodo de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. En el nodo **Correo electrónico**, selecciona **Seleccionar plantilla**.
3\. A continuación, elige la plantilla que quieras utilizar y selecciona **Utilizar plantilla**.
4\. Selecciona **Guardar** > **Hecho**.
5\. (Opcional) Para añadir más plantillas que se utilizarán en BrazeAI Decisioning Studio™ Go, añade otro nodo **Correo electrónico** y repite los pasos 2-4.
6\. Deja todos los correos electrónicos en modo **Borrador** y sal del Flujo.

En el portal BrazeAI Decisioning Studio™ Go, tus plantillas deberían poder seleccionarse bajo tu flujo de marcadores de posición.

![Ejemplo de una plantilla Klaviyo de marcador de posición en el portal Decisioning Studio Go.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## Crear un flujo en Klaviyo

### Paso 1: Configura el flujo

1. En Klaviyo, selecciona **Flujos** > **Crear flujo**.
2. Selecciona **Construye el tuyo**.
3. En **Nombre**, introduce el nombre del flujo de tu portal BrazeAI Decisioning Studio™ Go. A continuación, selecciona **Crear manualmente**.

![La opción "Crear manualmente" seleccionada para un flujo de ejemplo.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Selecciona el desencadenante.
5\. Haz coincidir el nombre de la métrica con el nombre del evento desencadenante de tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo de nombre de métrica que coincide con el nombre del evento desencadenante "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Seleccione **Guardar**.

{% alert note %}
Si tu experimentador dispone de una plantilla base, sigue los pasos siguientes. Si tu experimentador dispone de dos o más plantillas base, pasa a [Paso 3: Añade una división desencadenante a tu flujo](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

### Paso 2: Añade un correo electrónico a tu flujo 

1. Arrastra y suelta un nodo de **correo electrónico** después del nodo **desencadenante**.
2. En los **detalles del correo electrónico**, selecciona **Seleccionar plantilla**.

!["Seleccionar plantilla" en la sección "Detalles del correo electrónico".]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Busca y selecciona tu plantilla base. Puedes buscar tu plantilla por el nombre de la plantilla en la sección **Recursos a utilizar** del portal BrazeAI Decisioning Studio™ Go.

![Una plantilla base de ejemplo en Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Selecciona **Utilizar plantilla** > **Guardar**.
5\. Para la **línea del asunto**, introduce {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. Para **Nombre del remitente** y **Dirección de correo electrónico del remitente**, introduce los datos que quieras utilizar.

![Un ejemplo de línea del asunto, nombre del remitente y dirección de correo electrónico del remitente para "Correo electrónico 1".]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Selecciona **Hecho**.
8\. Desmarca la casilla **Omitir perfiles enviados recientemente por correo electrónico** y, a continuación, selecciona **Guardar**.
9\. En el nodo de correo electrónico, actualiza el modo de **Borrador** a **En vivo**.

![El editor de flujos de Klaviyo muestra un nodo Desencadenar conectado a un nodo Correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

¡Ya está todo listo! Ahora puedes desencadenar activaciones a través de BrazeAI Decisioning Studio™ Go. 

### Paso 3: Añade una división desencadenante a tu flujo 

1. Arrastra y suelta un nodo de **división del Desencadenante** después del **nodo del Desencadenante**.
2. Selecciona el nodo **Desencadenar división** y establece la **Dimensión** en **EmailTemplateID**.

![Diagrama de flujo de Klaviyo que muestra un nodo desencadenante que desencadena una división configurada con la dimensión EmailTemplateID.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### Paso 3.1: Añade tu plantilla de correo electrónico

1. En el portal BrazeAI Decisioning Studio™ Go, busca el **ID de la plantilla de correo electrónico** de tu primera plantilla en la sección **Recursos a utilizar**. Introduce el **ID de la plantilla de correo electrónico** para el campo **Dimensión** y, a continuación, selecciona **Guardar**.
2. Arrastra y suelta un nodo **Correo electrónico** a la rama **Sí** de la **división Desencadenar**. 

![Un flujo Klaviyo con un nodo Trigger split, que tiene una rama Sí que lleva a un nodo Correo electrónico y una rama No que conecta con otro Trigger split.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. En los **detalles del correo electrónico**, selecciona **Seleccionar plantilla**.
4\. Busca y selecciona tu plantilla base. Puedes buscar tu plantilla por el nombre de la plantilla base en la sección **Recursos a utilizar** del portal BrazeAI Decisioning Studio™ Go.
5\. Selecciona **Utilizar plantilla** > **Guardar**.
6\. Para la **línea del asunto**, introduce {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. Para **Nombre del remitente** y **Dirección de correo electrónico del remitente**, introduce los datos que quieras utilizar.

![Una plantilla de correo electrónico seleccionada y campos para la línea del asunto, el nombre del remitente y la dirección de correo electrónico del remitente.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Selecciona **Hecho**.
9\. Desmarca la casilla **Omitir perfiles enviados recientemente por correo electrónico** y, a continuación, selecciona **Guardar**.
10\. En el nodo de correo electrónico, actualiza el modo de **Borrador** a **En vivo**.

#### Paso 3.2: Añade una nueva división desencadenante

A continuación, crea una nueva **división Desencadenar** y un nodo **Correo electrónico** para cada plantilla base adicional que vaya a utilizar tu experimentador. 

1. Arrastra y suelta otro nodo de **desencadenar** en la rama **No** del nodo de **desencadenar** anterior.
2. Establece la **Dimensión** como **EmailTemplateID** y rellena el valor de la **Dimensión** con el **ID de la plantilla de correo electrónico** de la plantilla base que estás configurando.
3. Seleccione **Guardar**.

![Diagrama de un editor de flujo Klaviyo que muestra un nodo Desencadenar que desemboca en una división Desencadenar. La división de desencadenar tiene una rama Sí que lleva a un nodo de correo electrónico y una rama No que conecta con otra división de desencadenar que lleva a nodos de correo electrónico adicionales.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Arrastra y suelta un nodo **Correo electrónico** en la rama **Sí** de tu nueva división desencadenante.
5\. Repite los pasos 1-5 del [Paso 3.1](#step-31-add-your-email-template) para seleccionar la plantilla correspondiente.
5\. Establece la **línea del asunto** en {% raw %}`{{event.SubjectLine}}`{% endraw %}, y desmarca la casilla **Omitir perfiles enviados recientemente por correo electrónico**.
6\. Repite este proceso hasta que tengas un nodo **Desencadenar división** y un nodo **Correo electrónico** por cada plantilla base que esté utilizando tu experimentador. Tu última rama desencadenar no debe tener nada en la rama "No".

![Un flujo Klaviyo con múltiples nodos de división de desencadenantes que se ramifican en múltiples nodos de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7\. En cada uno de tus nodos de **correo electrónico**, actualiza el modo de **Borrador** a **En vivo**.

![La opción de actualizar el estado del nodo a "En vivo".]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

¡Ya está todo listo! Ahora puedes desencadenar activaciones a través de BrazeAI Decisioning Studio™ Go. 