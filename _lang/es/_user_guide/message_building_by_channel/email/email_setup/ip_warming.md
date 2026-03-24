---
nav_title: Calentamiento de IP
article_title: Calentamiento de IP
page_order: 1
page_type: reference
description: "Este artículo de referencia trata el tema del calentamiento de IP y las buenas prácticas."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/automated_ip_warming/'
---

# Calentamiento de IP

> El calentamiento de IP es la práctica de acostumbrar a los proveedores de buzones de correo electrónico a recibir mensajes de tus direcciones IP dedicadas. Es una parte extremadamente importante del envío de correo electrónico con cualquier proveedor de servicios de correo electrónico (ESP) y una práctica estándar en Braze para confirmar que tus mensajes llegan a sus buzones de entrada de destino a una tasa consistentemente alta.

El calentamiento de IP está diseñado para ayudarte a establecer una reputación positiva con los proveedores de servicios de Internet (ISP). Cada vez que se utiliza una nueva dirección IP para enviar un correo electrónico, los ISP supervisan programáticamente esos correos para verificar que no se está utilizando para enviar correo no deseado a los usuarios. Piensa en tu IP y la reputación de tu dominio como una puntuación crediticia: los ISP utilizan esta reputación para determinar si tu correo llega al buzón de entrada o a la carpeta de correo no deseado. Al igual que una puntuación crediticia, lleva tiempo construir una reputación positiva y aún más tiempo reconstruir una mala.

## ¿Y si no tengo tiempo para calentar IPs?

**El calentamiento de IP es obligatorio.** Si no calientas las IP adecuadamente, y el patrón de tu correo electrónico levanta sospechas, la velocidad de entrega de tu correo electrónico podría reducirse o ralentizarse considerablemente. Tu dominio o IP también podrían ser bloqueados por los ISP, lo que puede hacer que tus correos vayan directamente a la carpeta de correo no deseado del buzón de entrada de tu usuario. Por ello, es importante que calientes bien tus IP.

Los ISP limitan la entrega de correo electrónico cuando sospechan que se trata de correo no deseado para proteger a sus usuarios. Por ejemplo, si realizas un envío a 100.000 usuarios, el ISP podría entregar el correo electrónico solo a 5.000 de esos usuarios durante la primera hora. A continuación, el ISP monitoriza las medidas de interacción, como las tasas de apertura, las tasas de clics, las cancelaciones de suscripción y los informes de correos no deseados. Así, si se produce un número significativo de informes de correo no deseado, podrían optar por relegar el resto de ese envío a la carpeta de correo no deseado en lugar de entregarlo en el buzón de entrada del usuario.

Si la interacción es moderada, es posible que sigan limitando tu correo electrónico para recopilar más datos de interacción y determinar con mayor certeza si el correo electrónico es correo no deseado o no. Si el correo electrónico tiene unas métricas de interacción muy altas, pueden dejar de limitar este correo electrónico por completo. Utilizan esos datos para crear una reputación de correo electrónico que, a la larga, determinará si tus mensajes se filtran automáticamente a correo no deseado o no.

Si tu dominio o IP está bloqueado por un ISP, los registros de mensajes en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) contendrán información sobre qué sitios web visitar para apelar a estos ISP y salir de esas listas.

## Calendarios de calentamiento de IP

Recomendamos encarecidamente respetar estrictamente un calendario de calentamiento de IP para apoyar la capacidad de entrega. También es importante que no te saltes ningún día, ya que la escalabilidad constante mejora las métricas de entrega. Elige un calendario basado en tu historial de envío de correo electrónico existente y tus métricas de capacidad de entrega.

{% alert tip %}
Si te interesa contar con un recurso dedicado de capacidad de entrega como parte de tu equipo de cuenta, ponte en contacto con tu director de cuentas de Braze para obtener más información.
{% endalert %}

{% tabs local %}
{% tab Conservador %}

El calendario conservador es un enfoque más lento y cauteloso que ayuda a establecer una sólida reputación de envío desde cero. Se recomienda si eres nuevo en el envío de correo electrónico, estás migrando desde una IP compartida o has experimentado problemas de capacidad de entrega como limitaciones o bloqueos por parte de un proveedor de buzón de entrada.

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1.000
11 | 1.000
12 | 1.000
13 | 2.000
14 | 2.000
15 | 2.000
16 | 4.000
17 | 4.000
18 | 4.000
19 | 8.000
20 | 8.000
21 | 8.000
22+ | Duplicar cada 3 días hasta alcanzar el volumen deseado

{% endtab %}
{% tab Moderado %}

El calendario moderado es un enfoque equilibrado que aumenta el volumen de envío a un ritmo constante. Se recomienda para la mayoría de los remitentes, incluidos aquellos con algo de historial de envío de correo electrónico que están haciendo la transición a una nueva IP.

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.000
6 | 4.000
7 | 8.000
8 | 16.000
9 | 25.000
10 | 35.000
11 | 50.000
12 | 75.000
13 | 100.000
14 | 150.000
15 | 200.000
16 | 275.000
17 | 375.000
18 | 500.000
19 | 650.000
20 | 825.000
21 | 1.000.000
22+ | Duplicar cada 2 días hasta alcanzar el volumen deseado

{% endtab %}
{% tab Agresivo %}

{% alert important %}
El calendario agresivo es el enfoque más rápido y solo se recomienda para remitentes con un historial de envío establecido y positivo, y métricas de capacidad de entrega que se alineen con las buenas prácticas, incluyendo altas tasas de apertura, altas tasas de clics y bajas tasas de rebote. Usar este calendario sin un historial comprobado puede perjudicar tu reputación del remitente.
{% endalert %}

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.500
6 | 5.000
7 | 9.000
8 | 16.000
9 | 29.000
10 | 52.000
11 | 98.000
12 | 160.000
13 | 225.000
14 | 315.000
15 | 450.000
16 | 615.000
17 | 875.000
18 | 1.200.000
19 | 1.750.000
20 | 2.750.000
21+ | Duplicar a diario hasta alcanzar el volumen deseado

{% endtab %}
{% endtabs %}

En la mayoría de los casos, calienta hasta tu volumen de envío diario promedio en lugar de tu pico. Los ISP principalmente analizan las últimas semanas de comportamiento de envío para evaluar tu reputación, así que si alcanzas el volumen pico solo cada pocos meses (por ejemplo, 7 millones durante un periodo estacional), puedes aumentar hacia ese pico más cerca de la fecha de envío. Sin embargo, si alcanzas el volumen pico cada una o dos semanas, calienta hasta ese pico desde el principio.

Una vez completado el calentamiento de IP y alcanzado el volumen diario deseado, debes intentar mantener ese volumen a diario. Es normal que haya cierta fluctuación, pero alcanzar el volumen deseado y luego realizar solo un envío masivo una vez a la semana puede afectar negativamente a tus métricas de entrega y a la reputación del remitente.

{% alert important %}
La mayoría de los ISP solo almacenan los datos de reputación durante 30 días. Si pasas un mes sin enviar ningún mensaje, tendrás que repetir el proceso de calentamiento de IP.
{% endalert %}

## Cómo limitar los envíos durante el calentamiento

Nuestra función integrada de limitación de usuarios es una herramienta útil para ayudarte a calentar tu dirección IP. Después de elegir los segmentos de mensajería deseados durante la creación de la campaña, en el paso [Usuarios objetivo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), selecciona el menú desplegable **Opciones avanzadas** para limitar tus usuarios. A medida que tu calendario de calentamiento continúe, puedes aumentar gradualmente este límite para incrementar el volumen de correos electrónicos que envías.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentación de subdominios

Muchos ISP y proveedores de acceso al correo electrónico ya no filtran por la reputación de la dirección IP. Estas tecnologías de filtrado ahora también tienen en cuenta la reputación basada en el dominio. Esto significa que los filtros examinarán todos los datos asociados al dominio del remitente y no solo la dirección IP. Por esta razón, además de calentar la IP de tu correo electrónico, también recomendamos tener dominios o subdominios separados para el correo de marketing, transaccional y corporativo.

{% alert important %}
La segmentación por subdominios es especialmente importante para los remitentes de gran volumen. Estos remitentes deben trabajar con un representante de Braze al configurar su cuenta para confirmar que se adhieren a esta práctica.
{% endalert %}

Recomendamos segmentar tus dominios de modo que el correo corporativo se envíe a través de tu dominio de nivel superior, y el correo de marketing y transaccional se envíe a través de dominios o subdominios diferentes.

## Buenas prácticas

Puedes evitar todas las consecuencias de no realizar el calentamiento de IP siguiendo estas buenas prácticas:

### Empezar con pequeños volúmenes de envío de correo electrónico

Aumenta la cantidad que envías cada día lo más gradualmente posible. Las campañas de correo electrónico bruscas y de gran volumen son vistas con el mayor escepticismo por los ISP. Por lo tanto, debes empezar enviando pequeñas cantidades de correo electrónico e ir aumentando gradualmente hasta alcanzar el volumen de correo electrónico que pretendes enviar en última instancia. Ten en cuenta que estás calentando tu IP en cada ISP de forma individual: los ISP no comparten datos de reputación entre sí. Al planificar tus volúmenes de calentamiento, asegúrate de no aumentar el volumen demasiado rápido en ningún ISP individual. Independientemente del volumen, te aconsejamos que calientes tu IP para estar seguro. Consulta [Calendarios de calentamiento de IP](#ip-warming-schedules).

### Tener un contenido introductorio atractivo

Confirma que tu primer contenido es muy atractivo y maximiza la probabilidad de que los usuarios hagan clic, abran e interactúen con tu correo electrónico. Prefiere siempre los correos electrónicos bien dirigidos a los envíos indiscriminados a la hora de calentar IPs.

### Establecer una cadencia de envío coherente

Una vez completado el calentamiento de IP, crea una cadencia de envío, asegurándote también de repartir tus correos electrónicos a lo largo de uno o varios días. Si creas un calendario lo más coherente posible, puedes evitar un enfriamiento de la IP, que puede ocurrir si el volumen de envíos se detiene o disminuye significativamente durante más de unos días.

Consulta nuestro [calendario de calentamiento de IP](#ip-warming-schedules) para distribuir tu envío a lo largo de un periodo de tiempo más largo, en lugar de enviar un bombardeo masivo a una hora concreta.

### Limpia tus listas de correo electrónico

Confirma que tu lista de correo electrónico está limpia y no tiene correos electrónicos antiguos o no verificados. Lo ideal es asegurarte de que cumples tanto [con la ley CASL como con la ley CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Controla la reputación del remitente

Cuando lleves a cabo el proceso de calentamiento de IP, asegúrate de vigilar cuidadosamente la reputación del remitente. Es importante vigilar estas métricas específicas:
- **Tasas de rebote:** Si alguna campaña rebota más del 3-5%, debes evaluar la limpieza de tu lista siguiendo las directrices de nuestro artículo [Mantén tu lista limpia: la importancia del saneamiento de las listas de correo electrónico](https://www.braze.com/blog/email-list-hygiene/). Además, deberías considerar la posibilidad de implementar una [política de caducidad]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) para dejar de enviar correos electrónicos a direcciones inactivas o que no generan interacción.
- **Informes de correos no deseados:** Si alguna campaña se reporta como correo no deseado en un porcentaje superior al 0,08%, debes reevaluar el contenido que envías, comprobar que está dirigido a una audiencia interesada y asegurarte de que tus correos electrónicos están redactados adecuadamente para despertar su interés.
- **Tasas de apertura:** Las tasas de apertura son un indicador útil de la ubicación en el buzón de entrada. Si tus tasas de apertura únicas superan el 25%, es probable que estés experimentando una alta colocación en el buzón de entrada, lo que indica una reputación del remitente positiva.

{% alert tip %}
Braze recomienda no utilizar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para calentar tus IPs. Dado que las campañas de calentamiento de IP son algunas de las primeras campañas que envías, Braze no dispondrá de suficiente información sobre tus usuarios para calcular el momento óptimo de envío. En este caso, todos los mensajes con Intelligent Timing se enviarían a la hora alternativa predeterminada de todos modos.
{% endalert %}

{% alert tip %}
Es normal que se envíe correo a la carpeta de correo no deseado durante el calentamiento de IP porque tu dominio e IP aún no han establecido una reputación positiva. Si el correo llega a tu carpeta de correo no deseado, es posible que tu administrador de correo tenga que añadir el dominio y la IP de envío de Braze a la lista de permitidos de tu empresa.
{% endalert %}