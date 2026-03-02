---
nav_title: Configurar la orquestación
article_title: Configurar la orquestación
page_order: 2
description: "Aprende a conectar BrazeAI Decisioning Studio Go a tu plataforma de interacción con los clientes para habilitar comunicaciones personalizadas."
toc_headers: h2
---

# Configurar la orquestación

> BrazeAI Decisioning Studio™ Go necesita conectarse a tu plataforma de interacción con los clientes (CEP) para orquestar comunicaciones personalizadas. Este artículo explica cómo configurar la integración para cada CEP compatible.

## PEC apoyados

Decisioning Studio Go es compatible con las siguientes plataformas de interacción con los clientes:

| CEP | Tipo de integración | Características principales |
|-----|-----------------|--------------|
| **Braze** | Campañas activadas por API | Integración nativa, desencadenar en tiempo real |
| **Salesforce Marketing Cloud** | Constructor de Viajes con Eventos API | Automatización de consultas SQL, extensiones de datos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecciona tu CEP a continuación para empezar a configurar la integración.

{% tabs %}
{% tab Braze %}

## Configuración de la integración Braze

Para integrar Decisioning Studio Go con Braze, crearás una clave de API, configurarás una campaña desencadenada por API y proporcionarás los identificadores necesarios al portal de Decisioning Studio Go.

### Paso 1: Crear una clave de API REST

1. En el panel de Braze, ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Selecciona **Crear clave de API**.
3. Introduce un nombre para tu clave de API. Un ejemplo es "DecisioningStudioGoEmail".
4. Selecciona los permisos en función de las siguientes categorías:
    - **Datos de usuario:** selecciona `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Mensajes:** seleccionar `messages.send`
    - **Campañas:** selecciona todos los permisos de la lista
    - **Canvas:** selecciona todos los permisos de la lista
    - **Segmentos:** selecciona todos los permisos de la lista
    - **Plantillas:** selecciona todos los permisos de la lista

{: start="5"}
5\. Selecciona **Crear clave de API**.
6\. Copia la clave de API y pégala en tu portal BrazeAI Decisioning Studio™ Go.

### Paso 2: Localiza el nombre para mostrar de tu correo electrónico

1. En el panel de Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Localiza el nombre de pantalla que se utilizará con BrazeAI Decisioning Studio™ Go.
3. Copia y pega el **Nombre para** **mostrar** **de** en el portal BrazeAI Decisioning Studio™ Go como **Nombre para mostrar de correo electrónico**.
4. Copia y pega la dirección de correo electrónico asociada en tu portal BrazeAI Decisioning Studio™ Go como **dirección de correo electrónico De**, que combina la parte local y el dominio.

### Paso 3: Encuentra tu URL Braze y tu ID de aplicación

**Para encontrar tu URL Braze:**
1. Ve al panel de Braze.
2. En la ventana de tu navegador, tu URL de Braze empieza por `https://` y termina por `braze.com`. Un ejemplo de URL de Braze es `https://dashboard-01.braze.com`.

**Para encontrar el ID de tu aplicación (clave de API):**

{% alert note %}
Braze ofrece ID de aplicaciones (denominadas claves de API en el panel de Braze) que puedes utilizar con fines de seguimiento, como asociar la actividad a una aplicación específica de tu espacio de trabajo. Si utilizas ID de aplicación, BrazeAI Decisioning Studio™ Go permite asociar un ID de aplicación a cada experimentador.<br><br>Si no utilizas ID de aplicación, puedes introducir cualquier cadena de caracteres como marcador de posición.
{% endalert %}

1. En el panel de Braze, ve a **Configuración** > Configuración de la aplicación **.**
2. Ve a la aplicación que quieras seguir.
3. Copia y pega la **clave de API** en tu portal BrazeAI Decisioning Studio™ Go.

### Paso 4: Crea una campaña desencadenada por la API

1. En el panel de Braze, ve a **Mensajería** > Campañas.
2. Selecciona **Crear campaña**.
3. Para tu tipo de campaña, selecciona **Campaña API**.
4. Escribe un nombre para tu campaña. Un ejemplo es "Decisioning Studio Go Email".

![Una campaña API llamada "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Para tu canal de mensajería, selecciona **Correo electrónico**.

![Opción para seleccionar tu canal de mensajería para la campaña de API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. En **Opciones adicionales**, selecciona la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña**.
7\. Para el tiempo para volver a ser elegible, introduce **1** y selecciona **Horas** en el desplegable.

![Reelegibilidad para la campaña API seleccionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Selecciona **Guardar campaña**.

### Paso 5: Copia tus ID de campaña y mensaje

1. En tu campaña API, copia el **ID de la campaña**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de la campaña**.

![Un ejemplo de ID de variación de mensaje para copiar y pegar.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Copia el **ID de variación del mensaje**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de variación del mensaje**.

### Paso 6: Localiza un ID de usuario de prueba

Para probar tu integración, necesitarás un ID de usuario:

1. En el panel de Braze, ve a **Audiencia** > **Buscar usuarios**.
2. Busca al usuario por su ID externo, alias de usuario, correo electrónico, número de teléfono o token de notificaciones push.
3. Copia el ID de usuario como referencia en tu configuración.

![Ejemplo de perfil de usuario a partir de la ubicación de un usuario con su ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuración de la integración SFMC

Para integrar Decisioning Studio Go con Salesforce Marketing Cloud, deberás configurar un paquete de aplicación, crear una automatización de consulta de datos y construir un Viaje para gestionar los envíos desencadenados.

### Parte 1: Configurar un paquete de aplicaciones SFMC

1. Ve a tu página de inicio de Marketing Cloud.
2. Abre el menú de la cabecera global y selecciona **Configuración**.
3. Ve a **Aplicaciones** en **Herramientas de la plataforma** en el panel lateral de navegación y, a continuación, selecciona **Paquetes instalados**.
4. Selecciona **Nuevo** para crear un paquete de aplicación.
5. Da un nombre y una descripción al paquete de la aplicación.

![Un paquete de aplicación con el nombre "Experimentador 1 - Prueba 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Selecciona **Añadir componente**.
7\. Para el **Tipo de componente**, selecciona **Integración API**. A continuación, selecciona **Siguiente**.
8\. Para el **Tipo de integración**, selecciona **Servidor a servidor**. A continuación, selecciona **Siguiente**.
9\. Selecciona los siguientes ámbitos recomendados sólo para el paquete de tu aplicación:
    \- Canales > Correo electrónico > Leer, Escribir, Enviar
    \- Canales > OTT > Leer
    \- Canales > Push > Leer
    \- Canales > SMS > Leer
    \- Canales > Social > Leer
    \- Canales > Web > Leer
    \- Activos > Documentos e imágenes > Leer, Escribir
    \- Activos > Contenido guardado > Leer, Escribir
    \- Automatización > Automatizaciones > Leer, Escribir, Ejecutar
    \- Automatización > Viajes > Leer, Escribir, Ejecutar, Activar/Parar/Pausar/Enviar/Programar
    \- Contactos > Audiencias > Leer
    \- Contactos > Lista y suscriptores > Leer, Escribir
    \- Cross Cloud Platform > Audiencia de mercado > Ver
    \- Cross Cloud Platform > Miembro de la audiencia de marketing > Ver
    \- Cross Cloud Platform > Marketing Cloud Connect > Leer
    \- Datos > Extensiones de datos > Lectura, Escritura
    \- Datos > Ubicación de los archivos > Leer
    \- Datos > Seguimiento de Eventos > Lectura, Escritura
    \- Notificaciones de eventos > Devoluciones de llamada > Leer
    \- Notificaciones de eventos > Suscripciones > Leer

{% details Show image of recommended scopes %}

![Los ámbitos recomendados para el paquete de aplicaciones de Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Seleccione **Guardar**.
11\. Copia y pega los siguientes campos en el portal BrazeAI Decisioning Studio™ Go: **ID de cliente**, **Secreto de cliente**, **URI base de autenticación**, **URI base REST**, **URI base SOAP**.

### Parte 2: Configurar una automatización de consulta de datos

#### Paso 1: Crear una nueva automatización

1. Desde tu página de inicio de Salesforce Marketing Cloud, ve a **Journey Builder** y selecciona **Automation Studio**.

![Opción Estudio de automatización en la navegación del Constructor de viajes.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Selecciona **Nueva automatización**.
3\. Arrastra y suelta un nodo de **Programación** como **Fuente de Inicio**.

!["Programar" como origen inicial de un Viaje.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. En el nodo **Programación**, selecciona **Configurar**.
5\. Configura lo siguiente para la programación:
    - **Fecha de inicio:** Mañana es día de calendario
    - **Hora:** **12:00 AM**
    - **Zona horaria:** **(GMT-05:00) Este (US & Canadá)**
6\. Para **Repetir**, selecciona **Diariamente**.
7\. Configura este horario para que no termine nunca.
8\. Selecciona **Hecho** para guardar la programación.

![Una programación de ejemplo definida para el 25 de enero de 2024 a las 12 h ET, que se repetirá todos los días.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Paso 2: Crea tus consultas SQL

A continuación, crea 2 consultas SQL: una consulta de suscriptores y una consulta de interacción. Estas consultas permiten a BrazeAI Decisioning Studio™ Go recuperar datos para poblar la audiencia e ingerir eventos de interacción.

**Consulta de suscriptores:**

1. Arrastra y suelta una **consulta SQL** en el lienzo.
2. Selecciona **Elegir**.
3. Selecciona **Crear nueva actividad de consulta**.
4. Dale a la consulta un nombre y una clave externa. Te recomendamos que utilices el nombre y la clave externa sugeridos para la consulta del suscriptor proporcionados en tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo "OFE_Subscribers_query_Test5" y la llave externa.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Seleccione **Siguiente**.
6\. En tu portal BrazeAI Decisioning Studio™ Go, localiza la consulta SQL de Datos del sistema en **Recursos de consulta del suscriptor**.
7\. Copia y pega la consulta en el cuadro de texto y selecciona **Siguiente**.

![Un ejemplo de consulta en la sección Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. En tu portal BrazeAI Decisioning Studio™ Go, en la sección **Recursos a utilizar**, localiza la clave externa de la extensión de datos de destino. Luego, pégalo en la barra de búsqueda para buscar.

![Una clave externa pegada en la barra de búsqueda]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Selecciona la extensión de datos que coincida con la clave externa que has buscado. El nombre de extensión de los datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para hacer referencias cruzadas. La **Extensión de datos** para la consulta del suscriptor debe terminar en un sufijo `BASE_AUDIENCE_DATA`.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Selecciona **Sobrescribir** y luego **Siguiente**.

**Consulta de interacción:**

1. Arrastra y suelta una **consulta SQL** en el lienzo.

!["Consulta SQL" añadida como actividad en el Viaje.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Selecciona **Elegir**.
3\. Selecciona **Crear nueva actividad de consulta**.
4\. Dale a la consulta un nombre y una clave externa. Te recomendamos que utilices el nombre y la clave externa sugeridos para la consulta de interacción proporcionados en tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo "OFE_Engagement_query" y la llave externa.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Seleccione **Siguiente**.
6\. En tu portal BrazeAI Decisioning Studio™ Go, localiza la consulta SQL de Datos del sistema en **Recursos de consulta de interacción**.
7\. Copia y pega la consulta en el cuadro de texto y selecciona **Siguiente**.

![Un ejemplo de consulta en la sección Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Localiza y selecciona la Extensión de datos de destino para la Consulta de interacción especificada en tu portal BrazeAI Decisioning Studio™ Go.

{% alert tip %}
El nombre de extensión de los datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para hacer referencias cruzadas. Asegúrate de que estás viendo la Extensión de Datos de destino para la consulta de interacción. La **extensión de datos** de la consulta de interacción debe terminar con un sufijo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Selecciona **Sobrescribir** y luego **Siguiente**.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Paso 3: Ejecuta la automatización

1. Dale un nombre a la automatización y selecciona **Guardar**.

![Un ejemplo de automatización "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. A continuación, selecciona **Ejecutar una vez** para confirmar que todo funciona como se espera.
3\. Selecciona ambas consultas y elige **Ejecutar**.

![Una automatización "OFE_Experimenter_Test5_Automation" con una lista de actividades de consultas SQL seleccionadas para ejecutar.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Selecciona **Ejecutar ahora**.

![Una actividad de Consulta SQL seleccionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Ahora puedes comprobar que la automatización se está ejecutando correctamente. Ponte en contacto con el soporte de Braze para obtener más ayuda si tu automatización no funciona como esperabas.

### Parte 3: Crea tu Viaje SFMC

#### Paso 1: Configurar el Viaje

1. En Salesforce Marketing Cloud, ve a **Journey Builder** > **Journey Builder**.
2. Selecciona **Crear nuevo viaje**.
3. Para tu tipo de trayecto, selecciona **Trayecto de varios pasos** y, a continuación, **Crear**.

![Una fuente de entrada de Eventos API conectada a un nodo de división de decisiones y a varios nodos de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Paso 2: Construye el viaje

**Crea una fuente de entrada:**

1. Para tu fuente de entrada, arrastra **Evento API** al Creador de Viajes.

!["Evento API" seleccionado como fuente de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. En el **Evento API**, selecciona **Crear un evento**.

![La opción "crear un evento" en el Evento API.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. **Selecciona Seleccionar extensión de datos**. Localiza y selecciona la extensión de datos en la que BrazeAI Decisioning Studio™ Go escribirá las recomendaciones.
4\. Selecciona **Resumen** para guardar los cambios.
5\. Selecciona **Hecho** para guardar el evento API.

![Resumen del evento API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Añade una división de decisiones:**

1. Arrastra y suelta una **división de decisiones** tras el **evento de entrada en la API**.
2. En los detalles de **la División de decisiones**, selecciona **Editar** para la primera ruta.

![Detalles de la división de decisiones con el botón "Editar".]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Actualiza la **división de decisiones** para que utilice el ID de plantilla pasado por la extensión de datos de recomendaciones. Localiza el campo apropiado en **Datos del viaje**.

![La sección Datos del viaje en la Ruta 1 de la división de decisiones.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Selecciona tu evento de entrada y localiza el campo ID de plantilla deseado, luego arrástralo al espacio de trabajo.

![El ID de la plantilla de correo electrónico que debes incluir.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Introduce el ID de plantilla de tu primera plantilla de correo electrónico y, a continuación, selecciona **Hecho**.
6\. Selecciona **Resumen** para guardar esta ruta.
7\. Añade una ruta para cada una de tus plantillas de correo electrónico y, a continuación, repite los pasos 4-6 anteriores para establecer los criterios de filtrado de modo que el ID de la plantilla coincida con el valor de ID de cada plantilla.
8\. Selecciona **Hecho** para guardar el nodo **División de decisiones**.

![Dos caminos en una división de decisiones para cada ID de plantilla de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Añade un correo electrónico para cada división de decisiones:**

1. Arrastra un nodo **Correo electrónico** a cada ruta de la **División de decisiones**.
2. Selecciona **Correo electrónico** y, a continuación, selecciona la plantilla adecuada que debe ir en cada Ruta (es decir, la plantilla con el valor ID debe coincidir con la lógica de tu División de decisiones).

![Un nodo de correo electrónico añadido al Viaje.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Paso 3: Activa el Viaje

Después de configurar tu Viaje, actívalo y comparte los siguientes detalles con el equipo de BrazeAI Decisioning Studio™ Go:

* ID del viaje
* Nombre del viaje
* Clave de definición del evento API
* Recomendaciones ampliación datos clave externa

{% alert note %}
El portal BrazeAI Decisioning Studio™ Go te muestra la automatización de SFMC que aprovisionó para exportar los datos de suscriptores e interacción una vez al día. Si abres esta automatización en SFMC, asegúrate de desactivarla y volver a ponerla en vivo.
{% endalert %}

1. En el portal BrazeAI Decisioning Studio™ Go, copia el **nombre del Viaje**.
2. A continuación, en el Constructor de Trayectos de Salesforce Marketing Cloud, pega el nombre del Trayecto en la barra de búsqueda.
3. Selecciona el nombre del Viaje. Toma nota de que el Viaje se encuentra actualmente en estado Borrador.
4. Selecciona **Validar**.

![El Viaje a activar completado.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. A continuación, revisa los resultados de la validación y selecciona **Activar**.

![Recomendaciones enumeradas en la sección Reglas de validación.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. En el resumen **Activar viaje**, selecciona **Activar** de nuevo.

![Resumen para el viaje.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

¡Ya está todo listo! Ya puedes empezar a desencadenar envíos a través de BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Próximos pasos

Ahora que ya has configurado la orquestación, procede a diseñar tu agente:

- [Diseña tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
