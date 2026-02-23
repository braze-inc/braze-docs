---
nav_title: Configúralo con Salesforce Marketing Cloud
article_title: Configurar con Salesforce Marketing Cloud para BrazeAI Decisioning Studio Go
page_order: 5
description: "Aprende a configurar la automatización de una consulta de datos y Journey en Salesforce Marketing Cloud para su uso con BrazeAI Decisioning <sup>StudioTM</sup> Go."
toc_headers: h2
---

# Configurar con Salesforce Marketing Cloud para BrazeAI Decisioning Studio™ Go

> Configura un Viaje en Salesforce Marketing Cloud (SFMC) para empezar a desencadenar envíos a través de BrazeAI Decisioning Studio™ Go.

## Configuración de una automatización de consulta de datos

### Paso 1: Crear una nueva automatización

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

### Paso 2: Crea tus consultas SQL

A continuación, crearemos 2 consultas SQL: una consulta de suscriptores y una consulta de interacción. Estas consultas permiten a BrazeAI Decisioning Studio™ Go recuperar datos para poblar la audiencia e ingerir eventos de interacción.

{% tabs %}
{% tab Subscribers query %}
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
{% endtab %}
{% tab Engagement query %}
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
El nombre de extensión de los datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para hacer referencias cruzadas.  Asegúrate de que estás viendo la Extensión de Datos de destino para la consulta de interacción. La **Extensión de datos** para la consulta de interacción debe terminar con un sufijo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Selecciona **Sobrescribir** y luego **Siguiente**.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### Paso 3: Ejecuta la automatización

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

## Crear tu Trayecto SFMC

### Paso 1: Configurar el Viaje

1. En Salesforce Marketing Cloud, ve a **Journey Builder** > **Journey Builder**.
2. Selecciona **Crear nuevo viaje**.
3. Para tu tipo de trayecto, selecciona **Trayecto de varios pasos** y, a continuación, **Crear**.

![Una fuente de entrada de Eventos API conectada a un nodo de división de decisiones y a varios nodos de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### Paso 2: Construye el viaje

#### Paso 2.1: Crear una fuente de entrada

1. Para tu fuente de entrada, arrastra **Evento API** al Creador de Viajes.

!["Evento API" seleccionado como fuente de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. En el **Evento API**, selecciona **Crear un evento**.

![La opción "crear un evento" en el Evento API.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. **Selecciona Seleccionar extensión de datos**. Localiza y selecciona la extensión de datos en la que BrazeAI Decisioning Studio™ Go escribirá las recomendaciones.
4\. Selecciona **Resumen** para guardar los cambios.
5\. Selecciona **Hecho** para guardar el evento API.

![Resumen del evento API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### Paso 2.2: Añadir una división de decisiones

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

#### Paso 2.3: Añadir un correo electrónico para cada división de decisiones

1. Arrastra un nodo **Correo electrónico** a cada ruta de la **División de decisiones**.
2. Selecciona **Correo electrónico** y, a continuación, selecciona la plantilla adecuada que debe ir en cada Ruta (es decir, la plantilla con el valor ID debe coincidir con la lógica de tu División de decisiones).

![Un nodo de correo electrónico añadido al Viaje.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### Paso 3: Activa el Viaje

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
3. Selecciona el nombre del Viaje. Nota: el Viaje se encuentra actualmente en estado Borrador.
4. Selecciona **Validar**.

![El Viaje a activar completado.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. A continuación, revisa los resultados de la validación y selecciona **Activar**.

![Recomendaciones enumeradas en la sección Reglas de validación.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. En el resumen **Activar viaje**, selecciona **Activar** de nuevo.

![Resumen para el viaje.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

¡Ya está todo listo! Ya puedes empezar a desencadenar envíos a través de BrazeAI Decisioning Studio™ Go.
