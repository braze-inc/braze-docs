---
nav_title: Calentamiento de IP
article_title: Calentamiento de IP
page_order: 1
page_type: reference
description: "Este artículo de referencia trata el tema del calentamiento de IP y las mejores prácticas."
channel: email

---

# Calentamiento de IP

> El calentamiento de IP es la práctica de acostumbrar a los proveedores de buzón de entrada de correo electrónico a recibir mensajería de tus direcciones IP dedicadas. Es una parte extremadamente importante del envío de correo electrónico con cualquier proveedor de servicios de correo electrónico (ESP) y una práctica habitual en Braze confirmar que tus mensajes llegan a sus buzones de entrada de destino a una tasa elevada y constante.

El calentamiento de IP está diseñado para ayudarte a establecer una reputación positiva con los proveedores de servicios de Internet (ISP). Cada vez que se utiliza una nueva dirección IP para enviar un correo electrónico, los ISP supervisan programáticamente esos correos para verificar que no se está utilizando para enviar correo no deseado a los usuarios.

## ¿Y si no tengo tiempo para calentar IPs?

**Es necesario el calentamiento de IP.** Si no calientas las IP adecuadamente, y el patrón de tu correo electrónico levanta sospechas, la velocidad de entrega de tu correo electrónico podría reducirse o ralentizarse considerablemente. Tu dominio o IP también podrían estar bloqueados por los ISP, lo que puede hacer que tus correos electrónicos vayan directamente a la carpeta de correo no deseado de la bandeja de entrada de tu usuario. Por ello, es importante que calientes bien tus IP.

Los ISP limitan la entrega de correo electrónico cuando sospechan que se trata de correo no deseado, para proteger a sus usuarios. Por ejemplo, si envías a 100.000 usuarios, puede que el ISP entregue el correo electrónico sólo a 5.000 de esos usuarios durante la primera hora. A continuación, el ISP controla las medidas de interacción, como las tarifas abiertas, las tasas de clics, las cancelaciones de suscripción y los informes de correo no deseado. Así, si se produce un número significativo de informes de correos no deseados, podrían optar por relegar el resto de ese envío a la carpeta de correo no deseado en lugar de entregarlo en el buzón de entrada del usuario. 

Si la interacción es moderada, pueden seguir estrangulando tu correo electrónico para recopilar más datos de interacción y determinar con mayor certeza si el correo es o no spam. Si el correo electrónico tiene unas métricas de interacción muy altas, pueden dejar de acelerar este correo electrónico por completo. Utilizan esos datos para crear una reputación de correo electrónico que acabará determinando si tus correos electrónicos se filtran o no automáticamente al correo no deseado.

Si tu dominio o IP está bloqueado por un ISP, los registros de mensajes del [Registro de Actividad de Mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) contendrán información sobre qué sitios web visitar para apelar a estos ISP y salir de esas listas.

## Horarios de calentamiento de IP

Recomendamos encarecidamente cumplir este calendario de calentamiento de IP estrictamente para apoyar la capacidad de entrega. También es importante que no te saltes días, ya que un escalado constante mejora las métricas de entrega.

Día | \# Nº de correos electrónicos a enviar
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 5,000
6 | 10,000
7 | 20,000
8 | 40,000
9 | 70,000
10 | 100,000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18+ | Doblar diariamente hasta el volumen deseado

Sugerimos calentar hasta tu envío máximo. Es decir, si normalmente envías 2 millones de correos electrónicos al día, pero tienes previsto enviar 7 millones durante un periodo estacional, ese "pico" de envíos es el que debes calentar.

Una vez completado el calentamiento y alcanzado el volumen diario deseado, debes tratar de mantener ese volumen diariamente. Es de esperar cierta fluctuación, pero alcanzar el volumen deseado y luego hacer un envío masivo sólo una vez a la semana puede afectar negativamente a tus métricas de entrega y a la reputación del remitente. 

{% alert important %}
La mayoría de los ISP sólo almacenan los datos de reputación durante 30 días. Si pasas un mes sin enviar ningún mensaje, tendrás que repetir el proceso de calentamiento de IP.
{% endalert %}

## Cómo limitar los envíos durante el calentamiento

Nuestra característica integrada de limitación de usuarios es una herramienta útil para ayudarte con el calentamiento de IP. Tras elegir los segmentos de mensajería deseados durante la creación de la campaña, en el paso [Usuarios objetivo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), selecciona el desplegable **Opciones avanzadas** para limitar a tus usuarios. A medida que tu programa de calentamiento continúe, puedes aumentar gradualmente este límite para incrementar el volumen de correos electrónicos que envías.

\![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentación de subdominios

Muchos ISP y proveedores de acceso al correo electrónico ya no filtran sólo por la reputación de la dirección IP. Estas tecnologías de filtrado ahora también tienen en cuenta la reputación basada en dominios. Esto significa que los filtros examinarán todos los datos asociados al dominio del remitente y no sólo la dirección IP. Por esta razón, además de calentar tu IP de correo electrónico, también recomendamos tener dominios o subdominios separados para el correo de marketing, transaccional y corporativo. 

{% alert important %}
La segmentación por subdominios es especialmente importante para los remitentes de gran volumen. Estos remitentes deben trabajar con un representante de Braze al configurar su cuenta para confirmar que se adhieren a esta práctica.
{% endalert %}

Te recomendamos segmentar tus dominios para que el correo corporativo se envíe a través de tu dominio de nivel superior, y el correo de marketing y transacciones se envíe a través de dominios o subdominios diferentes.

## Buenas prácticas

Todas las consecuencias de no calentar de IP pueden evitarse si sigues estas buenas prácticas de calentamiento de IP.

### Empieza con pequeños volúmenes de envío de correo electrónico

Aumenta la cantidad que envías cada día lo más gradualmente posible. Las campañas de correo electrónico bruscas y de gran volumen son consideradas con el mayor escepticismo por los ISP. Por lo tanto, debes empezar enviando pequeñas cantidades de correo electrónico y escalar gradualmente hacia el volumen de correo electrónico que pretendes enviar en última instancia. Independientemente del volumen, te aconsejamos que calientes tu IP para estar seguro. Consulta [el programa de calentamiento de IP](#ip-warming-schedule).

### Tener un contenido introductorio atractivo

Confirma que tu primer contenido es muy atractivo y maximiza la probabilidad de que los usuarios hagan clic, abran y participen en tu correo electrónico. Prefiere siempre los correos electrónicos bien dirigidos a los bombardeos indiscriminados a la hora de calentar IP.

### Establece una cadencia de envío coherente

Una vez completado el calentamiento de IP, crea una cadencia de envío, asegurándote también de repartir tus correos electrónicos a lo largo de un día o varios días. Creando un horario lo más coherente posible, puedes evitar un enfriamiento de la IP, que puede producirse si el volumen de envíos se detiene o disminuye significativamente durante más de unos días. 

Consulta nuestro [calendario de calentamiento de IP](#ip-warming-schedules) para distribuir tus envíos a lo largo de un periodo de tiempo más prolongado, en lugar de enviar un bombardeo masivo a una sola hora concreta.

### Limpia tus listas de correo electrónico

Confirma que tu lista de correo electrónico está limpia y no tiene correos electrónicos antiguos o no verificados. Lo ideal es que te asegures de que [cumples tanto la CASL como la CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Controla la reputación del remitente

Cuando lleves a cabo el proceso de calentamiento de IP, asegúrate de vigilar cuidadosamente la reputación del remitente mientras realizas el proceso de calentamiento de IP. Es importante vigilar estas métricas concretas:
- **Tasas de rebote:** Si alguna campaña rebota más de un 3-5%, deberías evaluar la limpieza de tu lista siguiendo las directrices de nuestro [Mantenla limpia: La importancia de la higiene de las listas de correo electrónico](https://www.braze.com/blog/email-list-hygiene/) article. Además, deberías plantearte implantar una [política de suspensión]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) para dejar de enviar por correo electrónico a las direcciones de correo electrónico inactivas o no comprometidas.
- **Informes de correos no deseados:** Si alguna campaña recibe una tasa de spam superior al 0,08%, deberías volver a evaluar el contenido que envías, comprobar que está dirigido a una audiencia interesada y asegurarte de que tus correos electrónicos están redactados adecuadamente para despertar su interés.
- **Tarifas abiertas:** Las tasas de apertura son un indicador útil de la ubicación en el buzón de entrada. Si tus tasas de apertura únicas superan el 25%, es probable que estés experimentando una alta colocación en el buzón de entrada, lo que indica una reputación positiva del remitente.

{% alert tip %}
Braze recomienda no utilizar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para calentar tus IP. Como las campañas de calentamiento de IP son algunas de las primeras campañas que envías, Braze no tendrá suficiente información sobre tus usuarios para calcular una hora de envío óptima. En este caso, todos los mensajes con Intelligent Timing se predeterminarían a la hora alternativa y se enviarían a la misma hora de todos modos.
{% endalert %}

{% alert tip %}
Es normal que el correo se envíe a la carpeta de correo no deseado durante el calentamiento de IP porque tu dominio e IP aún no han establecido una reputación positiva. Si el correo llega a tu carpeta de correo no deseado, es posible que tu administrador de correo tenga que añadir el dominio de envío y la IP de Braze a la lista de permitidos de tu empresa.
{% endalert %}

