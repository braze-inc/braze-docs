---
nav_title: Calentamiento de IP automatizado
article_title: Calentamiento de IP automatizado
page_order: 1
page_type: reference
description: "Este artículo de referencia trata sobre el calentamiento de IP automatizado y cómo supervisar tu calentamiento de IP."
channel: email
---

# Calentamiento de IP automatizado

> Utiliza el calentamiento de IP automatizado para aumentar gradualmente el volumen de correos electrónicos desde una nueva dirección IP y así mejorar la reputación del remitente ante los proveedores de buzón de entrada.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Cómo funciona

Puedes utilizar el calentamiento de IP automatizado para aumentar gradualmente tu volumen de envío diario, lo que permite a los proveedores de buzón de entrada conocer y confiar en tus patrones de envío. Cuando añades un dominio a tu espacio de trabajo, puedes seleccionar el mosaico **Calentamiento de IP automatizado** en la sección **Continuar donde lo dejaste** del dashboard de tu página de inicio, y este mosaico permanecerá aquí durante 60 días.

Braze envía primero a tus suscriptores más activos, lo que permite que el volumen diario crezca a un ritmo que se ajusta a las mejores prácticas. A continuación, Braze realiza el seguimiento de las señales de interacción y capacidad de entrega. Si Braze detecta algún problema, el sistema ajusta tu planificación automáticamente.

{% alert note %}
Solo puedes realizar un calentamiento de IP.
{% endalert %}

## Requisitos previos

Para realizar el calentamiento de IP automatizado, debes disponer de lo siguiente:

- Subdominio verificado y direcciones IP activas
- Permisos para ver e iniciar un calentamiento de IP
    - "View Usage Data" para ver la sección sobre calentamiento de IP
    - "View Email Templates" para ver y seleccionar las plantillas de correo electrónico para el calentamiento de IP
    - "Manage Email Settings" para iniciar el calentamiento de IP
- "Access Campaigns" 
- "Approve and Deny Campaigns" si el flujo de trabajo de aprobación de campañas está activado 
    - Braze aprueba automáticamente las campañas creadas a partir del calentamiento de IP automatizado en tu nombre.

## Configura un plan de calentamiento de IP automatizado

### Paso 1: Establece una planificación

1. En la sección **Información de envío**, selecciona la **dirección De** para calentar las direcciones IP.
2. Introduce el volumen diario de envíos actual y el volumen de envíos objetivo.
3. Selecciona la fecha de inicio para el calentamiento de IP automatizado. Esta fecha debe ser al menos un día después de la puesta en marcha del plan.
4. Introduce la hora de envío. Esto envía los mensajes en la zona horaria de la empresa.
5. Selecciona **Siguiente: Segmentos** para continuar con la configuración.

![Detalles de la planificación de ejemplo.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Paso 2: Seleccionar y clasificar segmentos

1. A continuación, selecciona los segmentos a los que te quieres dirigir. Durante el calentamiento de IP, Braze comienza a enviar mensajes a los usuarios más activos y aumenta gradualmente el volumen de envíos con el tiempo, añadiendo poco a poco segmentos con menor nivel de interacción. 
2. A continuación, arrastra y suelta los segmentos para clasificarlos de mayor a menor interacción. El alto nivel de interacción incluye a los destinatarios que abren y hacen clic en tus correos electrónicos de forma constante. El bajo nivel de interacción incluye a los destinatarios que interactúan de forma irregular con tus correos electrónicos o que no han interactuado con ellos en mucho tiempo.
3. Selecciona **Siguiente: Mensajes** para continuar con la configuración.

![Dos segmentos seleccionados como objetivo para el calentamiento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Paso 3: Selecciona los mensajes que deseas enviar

1. Selecciona **Seleccionar plantillas de correo electrónico**.
2. Elige las plantillas de correo electrónico para los mensajes que deseas enviar. El contenido que envíes durante el calentamiento de IP debe fomentar las aperturas y los clics. Recomendamos elegir contenido que haya tenido buena acogida en el pasado. Por ejemplo, puedes utilizar ofertas promocionales para fomentar la interacción y las compras inmediatas.
3. Selecciona **Seleccionar plantillas**. Braze calcula el número de plantillas necesarias antes de que puedas iniciar el proceso. Recomendamos proporcionar más plantillas que el mínimo requerido para permitir que el sistema se ajuste a los problemas de capacidad de entrega sin detenerse.
4. Después de añadir el número necesario de plantillas, selecciona **Siguiente: Resumen**.

{% alert important %}
Los cambios realizados en las campañas creadas desde la herramienta de calentamiento de IP (como cambiar la fecha programada, el segmento o el volumen) no se reflejarán en la página **Resumen** del calentamiento de IP.
{% endalert %}

### Paso 4: Revisar y lanzar

Revisa los detalles de tu plan de calentamiento de IP. A continuación, selecciona **Lanzar**.

## Durante el calentamiento de IP activo

Las campañas de calentamiento de IP se crean con 1 o 2 días de antelación, a menos que vayas a lanzar un calentamiento de IP al día siguiente. Estas campañas se nombran automáticamente con el siguiente formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Cuando se alcanza el objetivo diario de envíos, el sistema deja de enviar mensajes ese día para proteger tu reputación. 

El sistema supervisa tu salud basándose en los siguientes parámetros de referencia del sector: 

- La tasa de entrega cae por debajo o es igual al 90 %
- Tasa de apertura inferior al 10 %
- Rebotes superiores al 5 %
- Tasa de quejas por correo no deseado superior al 0,04 %

Si las estadísticas están por debajo de nuestros puntos de referencia, el sistema mantiene el volumen al día siguiente en lugar de aumentarlo para mitigar el riesgo para la reputación del remitente.

## Detener un plan de calentamiento de IP

Braze te permite detener el calentamiento de IP y la creación de campañas futuras, pero si una campaña ya está activa o programada para las próximas 24 a 48 horas, es posible que tengas que detenerla manualmente. Al detener un plan de calentamiento de IP, también se detienen todas las campañas asociadas.

Sin embargo, una vez detenido, el calentamiento de IP no se puede reanudar. En su lugar, debes establecer un nuevo plan para retomar donde lo dejaste:

- Descarga los datos existentes de tu plan detenido para conservarlos en tus registros, ya que una vez que comiences un nuevo calentamiento de IP, el rastreador anterior se eliminará.
- Actualiza el **Volumen diario actual de envíos** al volumen más reciente.
- Añade un filtro a un segmento si tienes pensado utilizar el mismo segmento del último calentamiento de IP, excluyendo a los usuarios que ya hayan recibido campañas anteriores.

## Cuando finaliza el calentamiento de IP

El calentamiento de IP se marca como completado cuando el último día del calentamiento de IP finaliza a medianoche en la zona horaria de tu empresa. Por ejemplo, si la última campaña enviada en el plan de calentamiento de IP se envía a las 8 p. m., el plan se marca como completado después de cuatro horas.

El rastreador permanece en la página de inicio durante 90 días después de que finalice el plan. Después de 90 días, se retira el rastreador. La descarga de los datos incluye estas métricas estándar de correo electrónico:

- _Enviados_	
- _Entregados_	
- _Rebotes_	
- _Informes de correos no deseados_	
- _Total de aperturas_	
- _Aperturas únicas_	
- _Clics_	
- _Cancelaciones de suscripción_

Si un día incluye varias campañas utilizadas para cumplir con los requisitos de volumen, estas se agregan en la vista diaria.

![Rastreador de calentamiento de IP con volumen de envío para la semana del 16 de enero.]({% image_buster /assets/img/automated_ip_warming_example.png %})