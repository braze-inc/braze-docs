---
nav_title: Informes de participación
article_title: Informes de participación
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Este artículo explica cómo crear, personalizar y programar informes de participación para campañas y lienzos."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Informes de compromiso

> Los informes de participación le permiten extraer estadísticas de participación de mensajes específicos de campañas y lienzos para recibirlos por correo electrónico a la hora que prefiera.

{% alert note %}
Necesitas permisos de "Exportar datos de usuario" para ejecutar informes de interacción.
{% endalert %}

Con los informes de participación, puede seleccionar manualmente las campañas y los lienzos que desea incluir en su informe de correo electrónico, o especificar reglas para seleccionar automáticamente las campañas y los lienzos pertinentes.

Independientemente del número de campañas o lienzos que seleccione, se generarán hasta dos archivos CSV: uno para todos los datos de la campaña y otro para todos los datos del lienzo. Puede acceder a estos archivos CSV desde el enlace incluido en el correo electrónico de su informe. Los informes de compromiso no se guardan en el panel de control de Braze.

Ciertos datos se agregan a nivel de campaña o Canvas frente al nivel de variante de campaña individual o paso de Canvas. Si [eliminas un paso en Canvas después del lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), también se eliminarán los datos de los Informes de interacción.

{% alert tip %}
Puede volver a ejecutar el informe para generar estadísticas actualizadas.
{% endalert %}

## Crear un nuevo informe

### Paso 1: Crear un informe

En tu cuenta del panel, ve a **Análisis** > **Informes de interacción**. Selecciona **\+ Crear informe nuevo**.

### Paso 2: Añadir mensajes

Añada las campañas y los mensajes Canvas que desea compilar en su informe. Puedes seleccionar tus mensajes de dos maneras:

- Seleccionar manualmente campañas y lienzos
- Selección automática de campañas y lienzos en función de reglas específicas

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Seleccionar manualmente campañas o lienzos

Esta opción le da la libertad de elegir las campañas o lienzos que desee en este informe.

#### Seleccionar automáticamente campañas o lienzos

Esta opción te permite incluir automáticamente todos los mensajes que incluyan una [etiqueta]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) específica. Puedes dirigirte a mensajes que tengan una o todas las etiquetas enumeradas. Esta opción es útil si está configurando informes recurrentes y etiqueta regularmente sus mensajes de compromiso.

### Paso 3: Añadir estadísticas {#add-statistics-to-your-reports}

El paso **Añadir estadísticas** le muestra las estadísticas de los tipos de campañas o Lienzos que haya seleccionado. Por ejemplo, si seleccionaste mensajes de correo electrónico, sólo puedes ver las estadísticas de correo electrónico relevantes. Si elegiste una combinación de correo electrónico y push, puedes ver las estadísticas de esos dos canales.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

| Canal | Estadísticas disponibles |
| ------| --------------|
| Correo electrónico | Envíos, Aperturas, Aperturas únicas, Clics, Clics únicos, Clics para abrir, Anulaciones de suscripción, Rebotes, Entregados, Spam denunciado |
| Push  | Envíos, aperturas, Influenced Opens, rebotes, clics en el cuerpo |
| Notificación push web | Envíos, aperturas, rebotes, clics en el cuerpo |
| Mensaje dentro de la aplicación | Impresiones, clics, primeros clics del botón, segundos clics del botón |
| Webhook  |  Envíos, Errores |
| SMS | Envíos, envíos al transportista, entregas confirmadas, fallos de entrega, rechazos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
*Enviar al transportista* está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tengan.
{% endalert %}

### Paso 4: Configuración completa de informes

Asigne un nombre al informe, elija el formato y seleccione los destinatarios. Por defecto, los Informes de compromiso se envían como un archivo ZIP en el que los datos están delimitados por comas (donde cada dato está separado por una coma).

Puede elegir entre las siguientes opciones de compresión y delimitador:

- **Compresión:** ZIP, sin comprimir o gzip
- **Delimitador:** Coma (`,`), Dos puntos (`:`), Punto y coma (`;`), o Tubo (`|`)

{% alert note %}
Las estadísticas sólo se recogen para el intervalo de fechas especificado en el informe. Para recibir estadísticas precisas de tasa de apertura y clics, seleccione un intervalo de fechas que incluya cuándo se realizaron los eventos de Envío para sus campañas y Canvases.
{% endalert %}

#### Selecciona el marco temporal

Por predeterminado, el intervalo de datos mostrado se basa en la zona horaria de tu empresa e irá desde el mensaje más antiguo seleccionado hasta la fecha actual. Puede personalizarlo seleccionando el desplegable de fechas y utilizando la selección de intervalo personalizado O seleccionando el botón de opción siguiente y definiendo su intervalo de fechas con las opciones desplegables disponibles.

#### Seleccionar visualización de datos

Por defecto, los datos mostrados en los informes de interacción son diarios (un día). Para ver estos datos en diferentes intervalos, elige un número explícito de días o semanas para agregar los datos del informe. Así, en lugar de ver las métricas diarias, puedes ver tu interacción por semanas, meses, trimestres o similar. Si una agregación centrada en el tiempo no es suficiente, también puede optar por exportar los datos a nivel de campaña o de lienzo.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

#### Programa tu informe

Existen dos opciones a la hora de programar su informe:

- **Enviar inmediatamente:** Una vez lanzado el informe, Braze lo enviará inmediatamente.
- **Enviar a una hora determinada:** Esta opción te da la flexibilidad de elegir con qué frecuencia recibes este informe. Puede elegir enviar este informe cada determinado número de días, semanas o meses. También puede definir cuándo dejar de enviar el informe.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Paso 5: Revisión y lanzamiento

El último paso de la configuración de su informe muestra una vista general de las opciones configuradas. Revisa tu informe y, cuando estés satisfecho, selecciona **Iniciar informe**.

### Paso 6: Compruebe su correo electrónico  

Recibirá un correo electrónico con enlaces a sus informes en el momento u horario que elija. **Estos enlaces caducan una hora después del envío del informe.** Cuando selecciones los enlaces proporcionados, descargarás automáticamente un archivo ZIP que contiene tus archivos CSV, uno para todas las campañas.

El informe contiene todas las estadísticas seleccionadas en la sección [Añadir estadísticas](#add-statistics-to-your-reports) del proceso de configuración.


