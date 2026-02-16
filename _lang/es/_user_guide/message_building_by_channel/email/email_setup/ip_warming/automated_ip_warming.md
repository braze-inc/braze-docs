---
nav_title: Calentamiento de IP automatizado
article_title: Calentamiento de IP automatizado
page_order: 1
page_type: reference
description: "Este artículo de referencia trata del calentamiento de IP automatizado y de cómo supervisar tu calentamiento de IP."
channel: email
---

# Calentamiento de IP automatizado

> Utiliza la automatización del calentamiento de IP para aumentar gradualmente el volumen de correo electrónico desde una nueva dirección IP, con el fin de crear reputación del remitente entre los proveedores de buzón de entrada.

{% include early_access_beta_alert.md feature='Automated IP warming' %}

## Cómo funciona

Puedes utilizar el calentamiento de IP automatizado para aumentar gradualmente tu volumen de envíos diarios, permitiendo que los proveedores de buzones de entrada aprendan y confíen en tus patrones de envío. Cuando añades un dominio a tu espacio de trabajo, puedes seleccionar la ficha **Calentamiento de IP automatizado** en la sección **Retomar donde lo dejaste** del panel de inicio, y esta ficha permanece aquí durante 60 días.

Braze envía primero a tus suscriptores más comprometidos, lo que permite que el volumen diario crezca a un ritmo acorde con las mejores prácticas. Después, Braze hace un seguimiento de las señales de interacción y capacidad de entrega. Si Braze detecta algún problema, el sistema ajusta tu horario automáticamente.

{% alert note %}
Sólo puedes realizar un calentamiento de IP.
{% endalert %}

## Requisitos previos

Para realizar el calentamiento de IP automatizado, debes tener lo siguiente:

- Subdominio verificado y direcciones IP activas
- Permisos para ver y lanzar un calentamiento IP
    - "Ver Datos de Uso" para ver la sección de calentamiento de IP
    - "Ver plantillas de correo electrónico" para ver y seleccionar las plantillas de correo electrónico para el calentamiento de IP
    - "Administrar configuración de correo electrónico" para iniciar el calentamiento de la IP
- "Campañas de acceso" 
- "Aprobar y denegar campañas" si el flujo de trabajo de aprobación de campañas está activado 
    - Braze aprueba automáticamente las campañas creadas a partir del calentamiento de IP automatizado en tu nombre.

## Configura un plan automatizado de calentamiento de IP

### Paso 1: Establecer un horario

1. En la sección **Información de envío**, selecciona la **dirección De** para calentar direcciones IP.
2. Introduce el volumen de envío diario actual y el volumen de envío objetivo.
3. Selecciona la fecha de inicio del calentamiento de IP automatizado. Esta fecha debe ser al menos un día después del lanzamiento del plan.
4. Introduce la hora de envío. Esto envía los mensajes en la zona horaria de la empresa.
5. Selecciona **Siguiente: Segmenta** para continuar la configuración.

![Ejemplo de detalles del horario.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Paso 2: Selecciona y clasifica los segmentos

1. A continuación, selecciona los segmentos a los que dirigirte. Durante el calentamiento de IP, Braze comienza a enviar a tus usuarios más comprometidos y aumenta gradualmente el volumen de envíos a lo largo del tiempo, añadiendo poco a poco segmentos con menos interacción. 
2. Después, arrastra y suelta los segmentos para ordenarlos de mayor a menor interacción. Una alta interacción incluye a los destinatarios que abren y hacen clic constantemente en tus correos electrónicos. El bajo nivel de interacción incluye a los destinatarios que no son constantes en su interacción con tus correos electrónicos o que llevan mucho tiempo sin interactuar con ellos.
3. Selecciona **Siguiente: Mensajes** para continuar la configuración.

![Dos segmentos seleccionados como objetivo para el calentamiento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Paso 3: Selecciona los mensajes a enviar

1. **Selecciona Seleccionar plantillas de correo electrónico**.
2. Elige las plantillas de correo electrónico para los mensajes a enviar. El contenido que envíes durante el calentamiento de IP debe fomentar las aperturas y los clics. Te recomendamos que elijas contenidos que hayan tenido buena acogida en el pasado. Por ejemplo, puedes utilizar ofertas promocionales para fomentar la interacción y las compras inmediatas.
3. Selecciona **Seleccionar plantillas**. Braze calcula el número de plantillas necesarias antes de que puedas lanzarte. Recomendamos proporcionar más plantillas que el mínimo requerido para permitir que el sistema se ajuste a los problemas de capacidad de entrega sin detenerse.
4. Tras añadir el número necesario de plantillas, selecciona **Siguiente: Resumen**.

{% alert important %}
Los cambios realizados en las campañas creadas desde la herramienta de calentamiento de IP (como cambiar la fecha programada, el segmento o el volumen) no se reflejarán en la página **Resumen del** calentamiento de IP.
{% endalert %}

### Paso 4: Revisión y lanzamiento

Revisa los detalles de tu plan de calentamiento de IP. A continuación, selecciona **Iniciar**.

## Durante el calentamiento de IP activo

Las campañas de calentamiento de IP se crean con 1 ó 2 días de antelación, a menos que vayas a lanzar un calentamiento de IP al día siguiente. Estas campañas se nombran automáticamente con el siguiente formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Cuando se alcanza el objetivo de envíos diarios, el sistema detiene los envíos de ese día para proteger tu reputación. 

El sistema controla tu salud basándose en los siguientes puntos de referencia del sector: 

- La tasa de entrega cae por debajo o igual al 90%.
- Tarifa abierta inferior al 10%.
- Rebotes superiores al 5%.
- Tasas de reclamaciones por correo no deseado superiores al 0,1%.

Si las estadísticas están por debajo de nuestros valores de referencia, el sistema retiene el volumen al día siguiente en lugar de aumentarlo para mitigar el riesgo para tu reputación del remitente.

## Detener un plan de calentamiento IP

Braze te permite detener el calentamiento de IP y la creación de futuras campañas, pero si una campaña ya está activa o programada para las próximas 24 a 48 horas, puede que tengas que detener la campaña específica manualmente. Detener un plan de calentamiento de IP también detiene todas las campañas asociadas.

Sin embargo, cuando se detiene, el calentamiento de la IP no puede reanudarse. En su lugar, debes configurar un nuevo plan para retomarlo desde donde lo dejaste:

- Descargar los datos existentes de tu plan parado para conservarlos para tu registro, ya que una vez que inicies un nuevo calentamiento IP, se eliminará el rastreador anterior.
- Actualizar el **volumen de envío diario actual** al volumen más reciente
- Añade un filtro a un segmento si piensas utilizar el mismo segmento del último calentamiento de IP excluyendo a los usuarios que ya han recibido campañas anteriores

## Cuando finaliza el calentamiento de una IP

El calentamiento de IP se marca como finalizado cuando el último día de calentamiento de IP termina a medianoche en la zona horaria de tu empresa. Por ejemplo, si la última campaña enviada en el plan de calentamiento de IP se envía a las 8 de la tarde, entonces el plan se marca como realizado después de cuatro horas.

El rastreador permanece en la página de inicio durante 90 días después de que finalice el plan. Transcurridos 90 días, se retira el rastreador. La descarga de los datos incluye estas métricas estándar de correo electrónico:

- _Enviadas_	
- _Entregado_	
- _Rebotes_	
- _Informes de correos no deseados_	
- _Total de aperturas_	
- _Unique Opens_	
- _Hizo clic_	
- _No suscrito_

Si un día incluye varias campañas utilizadas para cumplir los requisitos de volumen, éstas se agregan en la vista diaria.

![Seguimiento del calentamiento de IP con el volumen de envíos de la semana del 16 de enero.]({% image_buster /assets/img/automated_ip_warming_example.png %})