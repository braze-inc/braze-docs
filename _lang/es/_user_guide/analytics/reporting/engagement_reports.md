---
nav_title: Informes de interacción
article_title: Informes de interacción
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Este artículo explica cómo crear, personalizar y programar informes de interacción para campañas y lienzos."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Informes de interacción

> Los informes de interacción te permiten extraer estadísticas de interacción de mensajes específicos de campañas y Lienzos para recibirlos como correo electrónico en el momento que prefieras.

{% alert note %}
Necesitas permisos de "Exportar datos de usuario" para ejecutar informes de interacción.
{% endalert %}

Con los informes de interacción, puedes seleccionar manualmente campañas y Canvases para incluirlos en tu informe de correo electrónico, o especificar reglas para seleccionar automáticamente campañas y Canvases relevantes.

Independientemente del número de campañas o Canvas que selecciones, se generan hasta dos archivos CSV: uno para todos los datos de campaña y otro para todos los datos de Canvas. Puedes acceder a estos archivos CSV desde el enlace incluido en el correo electrónico de tu informe. Los informes de interacción no se guardan en el panel de Braze.

Determinados datos se agregan a nivel de campaña o Canvas frente al nivel de variante de campaña individual o paso en Canvas. Si [eliminas un paso en Canvas después del lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), también se eliminarán los datos de los Informes de interacción.

{% alert tip %}
Puedes volver a ejecutar el informe para generar estadísticas actualizadas.
{% endalert %}

## Crear informe nuevo

### Paso 1: Crear un informe

En tu cuenta del panel, ve a **Análisis** > **Informes de** interacción **.** Selecciona **\+ Crear informe nuevo**.

### Paso 2: Añadir mensajes

Añade las campañas y mensajes de Canvas que quieras recopilar en tu informe. Puedes seleccionar tus mensajes de dos formas:

- Selecciona manualmente campañas y Lienzos
- Selecciona automáticamente campañas y Lienzos en función de reglas específicas

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Selecciona manualmente campañas o Lienzos

Esta opción te da la libertad de elegir las campañas o Lienzos que quieras en este informe.

#### Selecciona automáticamente campañas o Lienzos

Esta opción te permite incluir automáticamente todos los mensajes que incluyan una [etiqueta]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) específica. Puedes dirigirte a mensajes que tengan una o todas las etiquetas de la lista. Esta opción es útil si estás configurando informes periódicos y etiquetas regularmente tus mensajes de interacción.

### Paso 3: Añadir estadísticas {#add-statistics-to-your-reports}

El paso **Añadir estadísticas** te muestra las estadísticas de los tipos de campañas o Lienzos que hayas seleccionado. Por ejemplo, si seleccionaste mensajes de correo electrónico, sólo puedes ver las estadísticas de correo electrónico relevantes. Si elegiste una combinación de correo electrónico y push, puedes ver las estadísticas de esos dos canales.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

| Canal | Estadísticas disponibles |
| ------| --------------|
| Correo electrónico | Envíos, Aperturas, Aperturas únicas, Clics, Clics únicos, Clic para abrir, Desuscripciones, Rebotes, Entregados, Spam reportado |
| Push  | Envíos, Aperturas, Influenced Opens, Rebotes, Clics Corporales |
| Web Push | Envíos, aperturas, rebotes, clics en el cuerpo |
| Mensaje dentro de la aplicación | Impresiones, Clics, Clics en el primer botón, Clics en el segundo botón |
| Webhook  |  Envíos, Errores |
| SMS | Envíos, Envíos al operador, Entregas confirmadas, Fallos de entrega, Rechazos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
*Enviar al operador* está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tengan.
{% endalert %}

### Paso 4: Configuración completa del informe

Dale un nombre a tu informe, elige cómo se formateará y selecciona los destinatarios. Por predeterminado, los informes de interacción se envían como un archivo ZIP en el que los datos están delimitados por comas (donde cada dato está separado por una coma).

Puedes elegir entre las siguientes opciones de compresión y delimitador:

- **Compresión:** ZIP, Sin comprimir o gzip
- **Delimitador:** Coma (`,`), Dos puntos (`:`), Punto y coma (`;`), o Tubo (`|`)

{% alert note %}
Las estadísticas sólo se recogen para el intervalo de fechas especificado en el informe. Para recibir estadísticas precisas sobre la tarifa abierta y la tasa de clics, selecciona un intervalo de fechas que incluya cuándo se realizaron los eventos de Envío para tus campañas y Lienzos.
{% endalert %}

#### Selecciona el marco temporal

Por predeterminado, el intervalo de datos mostrado se basa en la zona horaria de tu empresa e irá desde el mensaje más antiguo seleccionado hasta la fecha actual. Puedes personalizarlo seleccionando el desplegable de fecha y utilizando la selección de rango personalizado O seleccionando el botón de opción siguiente y definiendo tu rango de fechas con las opciones desplegables disponibles.

#### Seleccionar visualización de datos

Por defecto, los datos mostrados en los informes de interacción son diarios (un día). Para ver estos datos en diferentes intervalos, elige un número explícito de días o semanas para agregar los datos del informe. Así, en lugar de ver las métricas diarias, puedes ver tu interacción por semanas, meses, trimestres o similar. Si una agregación centrada en el tiempo no es suficiente, también puedes optar por exportar los datos a nivel de campaña o de Canvas.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

#### Programa tu informe

Hay dos opciones a la hora de programar tu informe:

- **Enviar inmediatamente:** Una vez lanzado el informe, Braze lo enviará inmediatamente.
- **Enviar a una hora determinada:** Esta opción te da la flexibilidad de elegir con qué frecuencia recibes este informe. Puedes elegir enviar este informe cada un número determinado de días, semanas o meses. También puedes definir cuándo dejar de enviar el informe.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Paso 5: Revisión y lanzamiento

El paso final de la configuración de tu informe muestra un resumen de las opciones configuradas. Revisa tu informe y, cuando estés satisfecho, selecciona **Iniciar informe**.

### Paso 6: Comprueba tu correo electrónico  

Recibirás un correo electrónico con enlaces a tus informes en el momento u horario que elijas. **Estos enlaces caducan 1 hora después del envío del informe.** Cuando selecciones los enlaces proporcionados, descargarás automáticamente un archivo ZIP que contiene tus archivos CSV, uno para todas las campañas.

El informe contiene todas las estadísticas seleccionadas en la sección [Añadir estadísticas](#add-statistics-to-your-reports) del proceso de configuración.


