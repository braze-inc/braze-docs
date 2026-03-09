---
nav_title: Configurar la orquestación
article_title: Configurar la orquestación
page_order: 2
description: "Aprende a conectar BrazeAI Decisioning Studio Ve a tu plataforma de interacción con los clientes para habilitar las comunicaciones personalizadas."
toc_headers: h2
---

# Configurar la orquestación

> BrazeAI Decisioning Studio™ Go necesita conectarse a tu plataforma de interacción con los clientes (CEP) para realizar la orquestación de comunicaciones personalizadas. Este artículo explica cómo configurar la integración para cada CEP compatible.

## CEP compatibles

Decisioning Studio Go es compatible con las siguientes plataformas de interacción con los clientes:

| CEP | Tipo de integración | Características principales |
|-----|-----------------|--------------|
| **Braze** | Campañas activadas por API | Integración nativa, desencadenamiento en tiempo real |
| **Salesforce Marketing Cloud** | Journey Builder con eventos API | Automatización de consultas SQL, extensiones de datos |
| **Klaviyo** | Flujos con desencadenantes métricos | Basado en plantillas, divisiones por desencadenadores |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecciona tu CEP a continuación para comenzar con la configuración de la integración.

{% tabs %}
{% tab Braze %}

## Configuración de la integración con Braze

Para integrar Decisioning Studio Go con Braze, deberás crear una clave de API, configurar una campaña que se desencadene mediante API y proporcionar los identificadores necesarios al portal Decisioning Studio Go.

### Paso 1: Crear una clave de API REST

1. En el panel de Braze, ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Selecciona **Crear clave de API**.
3. Introduce un nombre para tu clave de API. Un ejemplo es «DecisioningStudioGoEmail».
4. Selecciona los permisos según las siguientes categorías:
    - **Datos de usuario:** selecciona `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Mensajes:** seleccionar `messages.send`
    - **Campañas:** selecciona todos los permisos enumerados.
    - **Canvas:** selecciona todos los permisos enumerados.
    - **Segmentos:** selecciona todos los permisos enumerados.
    - **Plantillas:** seleccionar todos los permisos enumerados

{: start="5"}
5\. Selecciona **Crear clave de API**.
6\. Copia la clave de API y pégala en tu portal BrazeAI Decisioning Studio™ Go.

### Paso 2: Busca tu nombre de usuario de correo electrónico.

1. En el panel de Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. La ubicación del nombre que se mostrará en pantalla para utilizarlo con BrazeAI Decisioning Studio™ Go.
3. Copia y pega el **nombre para mostrar del remitente** en el portal BrazeAI Decisioning Studio™ Go como **nombre para mostrar del** **correo electrónico**.
4. Copia y pega la dirección de correo electrónico asociada en tu portal BrazeAI Decisioning Studio™ Go como **dirección de correo electrónico del remitente**, que combina la parte local y el dominio.

### Paso 3: Busca tu URL de Braze y tu ID de aplicación.

**Para encontrar tu URL de Braze:**
1. Ve al panel de Braze.
2. En la ventana de tu navegador, la URL de Braze comienza por`https://`  y termina por `braze.com`. Un ejemplo de URL de Braze es `https://dashboard-01.braze.com`.

**Para encontrar tu ID de aplicación (clave de API):**

{% alert note %}
Braze ofrece ID de aplicaciones (denominadas claves de API en el panel de Braze) que puedes utilizar con fines de seguimiento, por ejemplo, para asociar la actividad con una aplicación específica en tu espacio de trabajo. Si utilizas ID de aplicaciones, BrazeAI Decisioning Studio™ Go admite la asociación de un ID de aplicación con cada experimentador.<br><br>Si no utilizas ID de aplicación, puedes introducir cualquier cadena de caracteres como marcador de posición.
{% endalert %}

1. En el panel de Braze, ve a **Configuración** > **Configuración de la aplicación**.
2. Ve a la aplicación que deseas realizar el seguimiento.
3. Copia y pega la **clave de API** en tu portal BrazeAI Decisioning Studio™ Go.

### Paso 4: Crear una campaña desencadenada por API

1. En el panel de Braze, ve a **Mensajería** > **Campañas**.
2. Selecciona **Crear campaña**.
3. Para el tipo de campaña, selecciona **campaña API**.
4. Escribe un nombre para tu campaña. Un ejemplo es «Decisioning Studio Go Correo electrónico».

![Una campaña API denominada «Decisioning Studio Go Email».]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Para tu canal de mensajería, selecciona **Correo electrónico**.

![Opción para seleccionar tu canal de mensajería para la campaña API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. En **Opciones adicionales**, selecciona la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir campañas**.
7\. Para volver a ser elegible, introduce **1** y selecciona **Horas** en el menú desplegable.

![Reelegibilidad para la campaña API seleccionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Selecciona **Guardar campaña**.

### Paso 5: Copia los ID de tu campaña y mensaje.

1. En tu campaña API, copia el **ID de la campaña**. A continuación, accede al portal BrazeAI Decisioning Studio™ Go y pega el **ID de la campaña**.

![Un ejemplo de ID de variación de mensaje para copiar y pegar.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Copia el **ID de variación del mensaje**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de variación del mensaje**.

### Paso 6: Busca un ID de usuario de prueba.

Para probar tu integración, necesitarás un ID de usuario:

1. En el panel de Braze, ve a **Audiencia** > **Buscar usuarios**.
2. Busca al usuario por su ID de usuario externo, alias de usuario, correo electrónico, número de teléfono o token de notificaciones push.
3. Copia el ID de usuario para consultarlo en tu configuración.

![Ejemplo de perfil de usuario a partir de la ubicación de un usuario con su ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuración de la integración con SFMC

Para integrar Decisioning Studio Go con Salesforce Marketing Cloud, deberás configurar un paquete de aplicaciones, crear una automatización de consultas de datos y diseñar un recorrido para gestionar los envíos desencadenados.

### Parte 1: Configurar un paquete de aplicaciones SFMC

1. Ve a la página de inicio de Marketing Cloud.
2. Abre el menú en el encabezado global y selecciona **Configuración**.
3. Ve a **Aplicaciones** en **Herramientas de plataforma** en el panel de navegación lateral y, a continuación, selecciona **Paquetes instalados**.
4. Selecciona **Nuevo** para crear un paquete de aplicaciones.
5. Pon un nombre y una descripción al paquete de la aplicación.

![Un paquete de aplicaciones con el nombre «Experimentador 1 - Prueba 5».]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Selecciona **Añadir componente**.
7\. En **Tipo** de **componente**, selecciona **Integración API**. A continuación, selecciona **Siguiente**.
8\. Para el **tipo de integración**, selecciona **De servidor a servidor**. A continuación, selecciona **Siguiente**.
9\. Selecciona los siguientes ámbitos recomendados solo para tu paquete de aplicaciones:
    \- Canales > Correo electrónico > Leer, escribir, enviar
    \- Canales > OTT > Leer
    \- Canales > Push > Leer
    \- Canales > SMS > Leer
    \- Canales > Social > Leer
    \- Canales > Web > Leer
    \- Activos > Documentos e imágenes > Leer, escribir
    \- Activos > Contenido guardado > Leer, escribir
    \- Automatización > Automatizaciones > Leer, escribir, ejecutar
    \- Automatización > Recorridos > Leer, escribir, ejecutar, activar/detener/pausar/enviar/programar
    \- Contactos > Audiencias > Leer
    \- Contactos > Lista y suscriptores > Leer, escribir
    \- Plataforma Cross Cloud > Audiencia del mercado > Ver
    \- Plataforma Cross Cloud > Miembro de la audiencia del mercado > Ver
    \- Plataforma Cross Cloud > Marketing Cloud Connect > Leer
    \- Datos > Extensiones de datos > Leer, escribir
    \- Datos > Ubicaciones de archivos > Leer
    \- Datos > Seguimiento de eventos > Lectura, escritura
    \- Notificaciones de eventos > Devoluciones de llamada > Leer
    \- Notificaciones de eventos > Suscripciones > Leer

{% details Show image of recommended scopes %}

![Los ámbitos recomendados para el paquete de aplicaciones de Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Seleccione **Guardar**.
11\. Copia y pega los siguientes campos en el portal BrazeAI Decisioning Studio™ Go: **ID de cliente**, **secreto de cliente**, **URI base de autenticación**, **URI base REST**, **URI base SOAP**.

### Parte 2: Configurar la automatización de consultas de datos

#### Paso 1: Crear una nueva automatización

1. Desde la página de inicio de Salesforce Marketing Cloud, ve a **Journey Builder** y selecciona **Automation Studio**.

![Opción de automatización Studio en la navegación de Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Selecciona **Nueva automatización**.
3\. Arrastrar y soltar un nodo **Programación** como **Origen** **inicial**.

![«Calendario» como origen inicial de un viaje.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. En el nodo **Programación**, selecciona **Configurar**.
5\. Configura lo siguiente para el programa:
    - **Fecha de inicio:** El día de mañana en el calendario
    - **Hora:** **12:00 A. M.**
    - **Zona horaria:** **(GMT-05:00) Este (EE. UU.&  Canadá)**
6\. Para **Repetir**, selecciona **Diario**.
7\. Configura este programa para que nunca termine.
8\. Selecciona **Hecho** para guardar la programación.

![Un ejemplo de programación definida para el 25 de enero de 2024 a las 12 a. m. ET, que se repetirá todos los días.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Paso 2: Crea tus consultas SQL

A continuación, crea dos consultas SQL: una consulta de suscriptores y una consulta de interacción. Estas consultas permiten a BrazeAI Decisioning Studio™ Go recuperar datos para completar la audiencia e incorporar eventos de interacción.

**Consulta de los suscriptores:**

1. Arrastrar y soltar una **consulta SQL** en el Canvas.
2. Selecciona **Elegir**.
3. Selecciona **Crear nueva actividad de consulta**.
4. Asigna un nombre y una clave externa a la consulta. Recomendamos utilizar el nombre y la clave externa sugeridos para la consulta de suscriptores que se proporcionan en tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo"OFE_Subscribers_query_Test5"  y la clave externa.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Seleccione **Siguiente**.
6\. En tu portal BrazeAI Decisioning Studio™ Go, la ubicación de la consulta SQL de datos del sistema en **Recursos de consulta de suscriptores** es **Recursos de consulta** de suscriptores.
7\. Copia y pega la consulta en el cuadro de texto y selecciona **Siguiente**.

![Un ejemplo de consulta en la sección Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. En el portal BrazeAI Decisioning Studio™ Go, en la sección **Recursos para usar**, ubica la clave externa de la extensión de datos de destino. A continuación, pégalo en la barra de búsqueda para realizar la búsqueda.

![Una clave externa pegada en la barra de búsqueda.]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Selecciona la extensión de datos que coincida con la clave externa que has buscado. El nombre de la extensión de datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para que puedas consultarlo. La **extensión de datos** para la consulta del suscriptor debe terminar en un`BASE_AUDIENCE_DATA`sufijo.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Selecciona **Sobrescribir** y, a continuación**, Siguiente**.

**Consulta de interacción:**

1. Arrastrar y soltar una **consulta SQL** en el Canvas.

![Se ha añadido «Consulta SQL» como actividad en el recorrido.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Selecciona **Elegir**.
3\. Selecciona **Crear nueva actividad de consulta**.
4\. Asigna un nombre y una clave externa a la consulta. Recomendamos utilizar el nombre y la clave externa sugeridos para la consulta de interacción que se proporcionan en tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo"OFE_Engagement_query"  y la clave externa.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Seleccione **Siguiente**.
6\. En tu portal BrazeAI Decisioning Studio™ Go, la ubicación de la consulta SQL de datos del sistema en **Recursos de consultas de interacción** es **Recursos de consultas de interacción**.
7\. Copia y pega la consulta en el cuadro de texto y selecciona **Siguiente**.

![Un ejemplo de consulta en la sección Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Localiza y selecciona la extensión de datos de destino para la consulta de interacción especificada en tu portal BrazeAI Decisioning Studio™ Go.

{% alert tip %}
El nombre de la extensión de datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para que puedas consultarlo. Asegúrate de que estás viendo la extensión de datos de destino para la consulta de interacción. La **extensión de datos** para la consulta de interacción debe terminar con elENGAGEMENT_DATAsufijo .
{% endalert %}

{: start="9"}
9\. Selecciona **Sobrescribir** y, a continuación**, Siguiente**.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Paso 3: Ejecuta la automatización.

1. Ponle un nombre a la automatización y selecciona **Guardar**.

![Un ejemplo de automatización/assets/img/decisioning_studio_go/query3.pngimage_buster"OFE_Experimenter_Test5_Automation".]({%    %})

{: start="2"}
2\. A continuación, selecciona **Ejecutar una vez** para confirmar que todo funciona según lo previsto.
3\. Selecciona ambas consultas y selecciona **Ejecutar**.

![Una automatización"OFE_Experimenter_Test5_Automation"con una lista de actividades de consultas SQL seleccionadas para ejecutar.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Selecciona **Ejecutar ahora**.

![Una actividad de consulta SQL seleccionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Ahora puedes comprobar que la automatización se está ejecutando correctamente. Si tu automatización no funciona como esperabas, ponte en contacto con el soporte de Braze para obtener más ayuda.

### Parte 3: Crea tu experiencia SFMC

#### Paso 1: Configura el viaje

1. En Salesforce Marketing Cloud, ve a **Journey Builder** > **Journey Builder**.
2. Selecciona **Crear nuevo recorrido**.
3. Para tu tipo de viaje, selecciona **Viaje de varios pasos** y, a continuación, selecciona **Crear**.

![Una fuente de entrada de eventos API conectada a un nodo de división de decisiones y a varios nodos de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Paso 2: Construye el viaje

**Crear una fuente de entrada:**

1. Para la fuente de entrada, arrastra **API Event** al Journey Builder.

![«API Event» seleccionado como fuente de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. En el **evento API**, selecciona **Crear un evento**.

![La opción «crear un evento» en la API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Selecciona **Extensión de datos**. Localiza y selecciona la ubicación de la extensión de datos en la que BrazeAI Decisioning Studio™ Go escribirá las recomendaciones.
4\. Selecciona **Resumen** para guardar los cambios.
5\. Selecciona **Hecho** para guardar el evento API.

![Resumen del evento API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Añadir una división de decisiones:**

1. Arrastrar y soltar una **división de decisiones** después del **evento de entrada de API**.
2. En los detalles **de la división de decisiones**, selecciona **Editar** para la primera ruta.

![Detalles de la división de decisiones con el botón «Editar».]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Actualiza la **división de decisiones** para utilizar el ID de plantilla pasado por la extensión de datos de recomendaciones. Ubica el campo correspondiente en **«Datos del viaje**».

![La sección Datos del viaje en la ruta 1 de la división de decisiones.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Selecciona tu evento de entrada y localiza el campo ID de plantilla deseado, luego arrástralo al espacio de trabajo.

![El ID de la plantilla de correo electrónico que se va a incluir.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Introduce el ID de la plantilla de tu primer correo electrónico y, a continuación, selecciona **Hecho**.
6\. Selecciona **Resumen** para guardar esta ruta.
7\. Añade una ruta para cada una de tus plantillas de correo electrónico y, a continuación, repite los pasos 4 a 6 anteriores para establecer los criterios de filtrado de modo que el ID de la plantilla coincida con el valor de ID de cada plantilla.
8\. Selecciona **Hecho** para guardar el nodo **de división de decisiones**.

![Dos rutas en una división de decisiones para cada ID de plantilla de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Añade un correo electrónico para cada división de decisiones:**

1. Arrastra un nodo **de correo electrónico** a cada ruta de la **división de decisiones.**
2. Selecciona **Correo electrónico** y, a continuación, selecciona la plantilla adecuada que debe ir en cada ruta (es decir, la plantilla con el valor de ID debe coincidir con la lógica de tu división de decisiones).

![Un nodo de correo electrónico añadido al recorrido.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Paso 3: Activa el viaje

Después de configurar tu Journey, actívalo y comparte los siguientes detalles con el equipo de BrazeAI Decisioning Studio™ Go:

* Identificación del viaje
* Nombre del viaje
* Clave de definición de evento API
* Extensión de datos de recomendaciones clave externa

{% alert note %}
El portal BrazeAI Decisioning Studio™ Go te muestra la automatización de SFMC que ha configurado para exportar los datos de suscriptores y de interacción una vez al día. Si abres esta automatización en SFMC, asegúrate de reanudarla y volver a activarla en vivo.
{% endalert %}

1. En el portal BrazeAI Decisioning Studio™ Go, copia el **nombre del recorrido**.
2. A continuación, en Salesforce Marketing Cloud Journey Builder, pega el nombre del recorrido en la barra de búsqueda.
3. Selecciona el nombre del viaje. Ten en cuenta que el Viaje se encuentra actualmente en estado de borrador.
4. Selecciona **Validar**.

![El viaje completado para activar.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. A continuación, revisa los resultados de la validación y selecciona **Activar**.

![Recomendaciones enumeradas en la sección Reglas de validación.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. En el resumen **Activar viaje**, selecciona **Activar** de nuevo.

![Resumen del viaje.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

¡Ya está todo listo! Ahora puedes empezar a desencadear envíos a través de BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% tab Klaviyo %}

## Configuración de la integración con Klaviyo

Para integrar Decisioning Studio Go con Klaviyo, deberás configurar una clave de API, crear una plantilla de flujo de marcador de posición y crear un flujo para gestionar los envíos desencadenados.

### Parte 1: Configurar las claves de API de Klaviyo

1. En Klaviyo, ve a **Configuración** > **Claves de API**.
2. Selecciona **Crear clave de API privada**.
3. Introduce un nombre para la clave de API. Un ejemplo es «Decisioning Studio Experimenters».
4. Selecciona los siguientes permisos para la clave de API:
    - Campañas: Acceso de lectura
    - Privacidad de datos: Acceso total
    - Eventos: Acceso total
    - Flujos: Acceso total
    - Imágenes: Acceso de lectura
    - Lista: Acceso total
    - Métricas: Acceso total
    - Perfiles: Acceso total
    - Segmentos: Acceso de lectura
    - Plantillas: Acceso total
    - Webhooks: Acceso de lectura

![Una clave de API de Klaviyo con los permisos seleccionados.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Seleccione **Crear**.
6\. Copia esta clave de API y pégala en el portal BrazeAI Decisioning Studio™ Go cuando se te solicite.

### Parte 2: Crea una plantilla de marcador de posición en Klaviyo.

BrazeAI Decisioning Studio™ Go importa plantillas asociadas a flujos existentes en tu cuenta de Klaviyo. Para utilizar una plantilla que no esté asociada a ningún flujo, puedes crear un flujo marcador de posición que contenga las plantillas que deseas utilizar. El flujo se puede dejar como borrador; no es necesario que esté en vivo.

{% alert note %}
El propósito de este marcador de posición es importar el contenido deseado a BrazeAI Decisioning Studio™ Go. Debes crear un flujo independiente en un paso posterior, que BrazeAI Decisioning Studio™ Go utilizará para desencadenar las activaciones una vez que tu experimentador esté en vivo.
{% endalert %}

**Paso 1: Configura tu flujo**

1. En Klaviyo, selecciona **Flujos**.
2. Selecciona **Crear flujo** > **Crear desde cero**.
3. Asigna un nombre reconocible al marcador de posición Flujo y, a continuación, selecciona **Crear flujo**.

![Un flujo denominado «Flujo marcador de posición OFE».]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Selecciona cualquier activador y guarda el flujo.
5\. Selecciona **Confirmar y guardar**.

**Paso 2: Crear la plantilla de marcador de posición**

1. Arrastrar y soltar un nodo **de correo electrónico** después del **Desencadenador**.

![Un flujo con un nodo Desencadenante seguido de un nodo de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. En el nodo **de correo electrónico**, selecciona **Seleccionar plantilla**.
3\. A continuación, elige la plantilla que deseas utilizar y selecciona **Usar plantilla**.
4\. Selecciona **Guardar** > **Hecho**.
5\. (Opcional) Para añadir más plantillas que se utilizarán en BrazeAI Decisioning Studio™ Go, añade otro nodo **de correo electrónico** y repite los pasos 2 a 4.
6\. Deja todos los correos electrónicos en modo **Borrador** y sal del Flujo.

En el portal BrazeAI Decisioning Studio™ Go, tus plantillas deben poder seleccionarse en tu flujo de marcadores de posición.

![Ejemplo de una plantilla Klaviyo de marcador de posición en el portal Decisioning Studio Go.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

### Parte 3: Crea un flujo en Klaviyo

{% alert important %}
Debes crear un nuevo flujo en Klaviyo para cada nuevo experimentador que configures. Si anteriormente creaste un flujo marcador de posición para importar tus plantillas, debes crear un nuevo flujo y no puedes reutilizar el flujo marcador de posición anterior.
{% endalert %}

Antes de crear un flujo en Klaviyo, debes disponer de los siguientes datos de tu portal BrazeAI Decisioning Studio™ Go para poder consultarlos:

- Nombre del flujo
- Nombre del evento que desencadena el proceso

#### Paso 1: Configura el flujo

1. En Klaviyo, selecciona **Flujos** > **Crear flujo**.
2. Selecciona **«Crea tu propio**».
3. En **Nombre**, introduce el nombre del flujo de tu portal BrazeAI Decisioning Studio™ Go. A continuación, selecciona **Crear manualmente**.

![La opción «Crear manualmente» seleccionada para un flujo de ejemplo.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Selecciona el disparador.
5\. Empareja el nombre de la métrica con el nombre del evento que desencadena tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo de nombre de métrica que coincide con el nombre del evento "OFE_TEST_CASE_API_EVENT_TRIGGER".]({%image_buster/assets/img/decisioning_studio_go/flow2.pngdesencadenante    %})

{: start="6"}
6\. Seleccione **Guardar**.

{% alert note %}
Si tu experimentador tiene una plantilla base, pasa al paso 2. Si tu experimentador tiene dos o más plantillas base, pasa al [paso 3: Añade una división de activación a tu flujo](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

#### Paso 2: Añadir un correo electrónico a tu flujo (plantilla única)

1. Arrastre y suelte un nodo **de correo electrónico** después del nodo **Desencadenante**.
2. En los **detalles del correo electrónico**, selecciona **Seleccionar plantilla**.

![Opción «Seleccionar plantilla» en la sección «Detalles del correo electrónico».]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Busca y selecciona tu plantilla base. Puedes buscar tu plantilla por su nombre en la sección **Recursos para usar** del portal BrazeAI Decisioning Studio™ Go.

![Una plantilla base de ejemplo en Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Selecciona **Usar plantilla** > **Guardar**.
5\. En la **línea del asunto**, escribe {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. En los campos **Nombre del remitente** y **Dirección de correo electrónico del remitente**, introduce los datos que desees utilizar.

![Ejemplo de línea del asunto, nombre del remitente y dirección de correo electrónico del remitente para el «Correo electrónico 1».]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Selecciona **Hecho**.
8\. Desmarca la casilla **Omitir perfiles enviados recientemente por correo electrónico** y, a continuación, selecciona **Guardar**.
9\. En el nodo del correo electrónico, actualiza el modo de **Borrador** a **En vivo**.

![El editor de flujos de Klaviyo muestra un nodo de activación conectado a un nodo de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

¡Ya está todo listo! Ahora puedes desencadear activaciones a través de BrazeAI Decisioning Studio™ Go.

#### Paso 3: Añade una división por desencadenante a tu flujo (varias plantillas)

1. Arrastrar y soltar un nodo **de división de activador** después del **nodo de activador**.
2. Selecciona el nodo **Trigger split** y configura la **dimensión** en **EmailTemplateID**.

![Diagrama de flujo de Klaviyo que muestra un nodo de activación que es la fuente de una división de activación configurada con la dimensión EmailTemplateID.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

**Añade tu plantilla de correo electrónico:**

1. En el portal BrazeAI Decisioning Studio™ Go, busca el **ID** de **plantilla de correo electrónico** de tu primera plantilla en la sección **Recursos para usar**. Introduce el **ID** de **la plantilla de correo electrónico** en el campo **Dimensión** y, a continuación, selecciona **Guardar**.
2. Arrastre y suelte un nodo **de correo electrónico** en la rama **Sí** de la **división del desencadenador**.

![Un flujo de Klaviyo con un nodo de división de activación, que tiene una rama «Sí» que conduce a un nodo de correo electrónico y una rama «No» que se conecta a otra división de activación.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. En los **detalles del correo electrónico**, selecciona **Seleccionar plantilla**.
4\. Busca y selecciona tu plantilla base. Puedes buscar tu plantilla por el nombre de la plantilla base en la sección **Recursos para usar** del portal BrazeAI Decisioning Studio™ Go.
5\. Selecciona **Usar plantilla** > **Guardar**.
6\. En la **línea del asunto**, escribe {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. En los campos **Nombre del remitente** y **Dirección de correo electrónico del remitente**, introduce los datos que desees utilizar.

![Una plantilla de correo electrónico seleccionada y campos para la línea del asunto, el nombre del remitente y la dirección de correo electrónico del remitente.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Selecciona **Hecho**.
9\. Desmarca la casilla **Omitir perfiles enviados recientemente por correo electrónico** y, a continuación, selecciona **Guardar**.
10\. En el nodo del correo electrónico, actualiza el modo de **Borrador** a **En vivo**.

**Añade una nueva división de activación para cada plantilla adicional:**

1. Arrastrar y soltar otro nodo **de división de disparador** en la rama **No** del nodo **de división de disparador** anterior.
2. Establece la **dimensión** en **EmailTemplateID** y rellena el valor **de la dimensión** con el **ID** de la **plantilla de correo electrónico** de la plantilla base que estás configurando.
3. Seleccione **Guardar**.

![Diagrama de un editor de flujos de Klaviyo que muestra un nodo de desencadenamiento que conduce a una división de desencadenamiento. La división del desencadenador tiene una rama «Sí» que conduce a un nodo «Correo electrónico» y una rama «No» que se conecta a otra división del desencadenador que conduce a nodos «Correo electrónico» adicionales.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Arrastre y suelte un nodo **de correo electrónico** en la rama **Sí** de su nueva división de desencadenantes.
5\. Repite los pasos de configuración de la plantilla de correo electrónico anteriores para seleccionar la plantilla correspondiente.
6\. Establece la **línea del asunto** en {% raw %}`{{event.SubjectLine}}`{% endraw %}y desmarca la casilla **Omitir perfiles enviados recientemente por correo electrónico**.
7\. Repite este proceso hasta que tengas un nodo **de división de activadores** y un nodo **de correo electrónico** para cada plantilla base que utilice tu experimentador. Tu última división de desencadenamiento no debería tener nada en la rama «No».

![Un flujo de Klaviyo con múltiples nodos de división de activadores que se ramifican en múltiples nodos de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="8"}
8\. En cada uno de tus nodos **de correo electrónico**, actualiza el modo de **Borrador** a **En vivo**.

![La opción de actualizar el estado del nodo a «En vivo».]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

¡Ya está todo listo! Ahora puedes desencadear activaciones a través de BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Próximos pasos

Ahora que ya has configurado la orquestación, continúa con el diseño de tu agente:

- [Diseña tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
