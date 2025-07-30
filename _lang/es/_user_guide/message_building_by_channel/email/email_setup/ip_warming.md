---
nav_title: Calentamiento de IP
article_title: Calentamiento de IP
page_order: 1
page_type: reference
description: "Este artículo de referencia trata el tema del calentamiento de IP y las buenas prácticas."
channel: email

---

# Calentamiento de IP

> El calentamiento de IP es la práctica de acostumbrar a los proveedores de buzones de correo electrónico a recibir mensajes de tus direcciones IP dedicadas. Es una parte extremadamente importante del envío de correo electrónico con cualquier proveedor de servicios de correo electrónico (ESP) y una práctica estándar en Braze para confirmar que sus mensajes llegan a sus bandejas de entrada de destino a un ritmo consistentemente alto.

El calentamiento de IP está diseñado para ayudarte a establecer una reputación positiva con los proveedores de servicios de Internet (ISP). Cada vez que se utiliza una nueva dirección IP para enviar un correo electrónico, los ISP supervisan programáticamente esos correos para verificar que no se está utilizando para enviar spam a los usuarios.

## ¿Y si no tengo tiempo para calentar IPs?

**Es necesario el calentamiento de IP.** Si no calientas las IP adecuadamente, y el patrón de tu correo electrónico levanta sospechas, la velocidad de entrega de tu correo electrónico podría reducirse o ralentizarse considerablemente. Tu dominio o IP también podrían estar bloqueados por los ISP, lo que puede hacer que tus correos vayan directamente a la carpeta de spam de la bandeja de entrada de tu usuario. Por ello, es importante que calientes bien tus IP.

Los ISP estrangulan el envío de correo electrónico cuando sospechan que se trata de spam para proteger a sus usuarios. Por ejemplo, si realiza un envío a 100.000 usuarios, el ISP podría entregar el correo electrónico sólo a 5.000 de esos usuarios durante la primera hora. A continuación, el ISP controla las medidas de interacción, como las tarifas abiertas, las tasas de clics, las cancelaciones de suscripción y los informes de correo no deseado. Así, si se produce un número significativo de informes de spam, podrían optar por relegar el resto de ese envío a la carpeta de spam en lugar de entregarlo en la bandeja de entrada del usuario. 

Si el compromiso es moderado, pueden seguir estrangulando su correo electrónico para recopilar más datos de compromiso y determinar con mayor certeza si el correo es spam o no. Si el correo electrónico tiene unas métricas de interacción muy altas, pueden dejar de acelerar este correo electrónico por completo. Utilizan esos datos para crear una reputación de correo electrónico que, a la larga, determinará si sus mensajes se filtran automáticamente a spam o no.

Si tu dominio o IP está bloqueado por un ISP, los registros de mensajes en el [Registro de Actividad de Mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) contendrán información sobre qué sitios web visitar para apelar a estos ISP y salir de esas listas.

## Calendario de calentamiento de IP

Recomendamos encarecidamente respetar este calendario de calentamiento de IP estrictamente para apoyar la capacidad de entrega. También es importante que no te saltes días, ya que un escalado constante mejora las métricas de entrega.

Día | Nº de correos electrónicos a enviar
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
10 | 100.000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18+ | Duplicar a diario hasta alcanzar el volumen deseado

Sugerimos calentar hasta tu envío máximo. Es decir, si normalmente envías 2 millones de correos electrónicos al día, pero tienes previsto enviar 7 millones durante un periodo estacional, ese "pico" de envíos es el que debes calentar.

Una vez completado el calentamiento y alcanzado el volumen diario deseado, debes tratar de mantener ese volumen diariamente. Es de esperar cierta fluctuación, pero alcanzar el volumen deseado y luego hacer un envío masivo solo una vez a la semana puede afectar negativamente a tus métricas de entrega y a la reputación del remitente. 

{% alert important %}
La mayoría de los ISP solo almacenan los datos de reputación durante 30 días. Si pasas un mes sin enviar ningún mensaje, tendrás que repetir el proceso de calentamiento de IP.
{% endalert %}

## Cómo limitar los envíos durante el calentamiento

Nuestra función integrada de limitación de usuarios es una herramienta útil para ayudarle a calentar su dirección IP. Después de elegir los segmentos de mensajería deseados durante la creación de la campaña, en el paso [Usuarios objetivo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), seleccione el menú desplegable **Opciones avanzadas** para limitar sus usuarios. A medida que tu programa de calentamiento continúe, puedes aumentar gradualmente este límite para incrementar el volumen de correos electrónicos que envías.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentación de subdominios

Muchos ISP y proveedores de acceso al correo electrónico ya no filtran únicamente por la reputación de la dirección IP. Estas tecnologías de filtrado ahora también tienen en cuenta la reputación basada en el dominio. Esto significa que los filtros examinarán todos los datos asociados al dominio del remitente y no sólo la dirección IP. Por esta razón, además de calentar la IP de su correo electrónico, también recomendamos tener dominios o subdominios separados para el correo de marketing, transaccional y corporativo. 

{% alert important %}
La segmentación por subdominios es especialmente importante para los remitentes de gran volumen. Estos remitentes deben trabajar con un representante de Braze al configurar su cuenta para confirmar que se adhieren a esta práctica.
{% endalert %}

Recomendamos segmentar sus dominios de modo que el correo corporativo se envíe a través de su dominio de nivel superior, y el correo de marketing y transaccional se envíe a través de dominios o subdominios diferentes.

## Buenas prácticas

Todas las consecuencias de no calentar de IP pueden evitarse si sigues estas buenas prácticas de calentamiento de IP.

### Empezar con pequeños volúmenes de envío de correo electrónico

Aumenta la cantidad que envías cada día lo más gradualmente posible. Las campañas de correo electrónico bruscas y de gran volumen son vistas con el mayor escepticismo por los ISP. Por lo tanto, debe empezar enviando pequeñas cantidades de correo electrónico e ir aumentando gradualmente hasta alcanzar el volumen de correo electrónico que pretende enviar en última instancia. Independientemente del volumen, te aconsejamos que calientes tu IP para estar seguro. Consulta [el calendario de calentamiento de IP](#ip-warming-schedule).

### Tener un contenido introductorio atractivo

Confirma que tu primer contenido es muy atractivo y maximiza la probabilidad de que los usuarios hagan clic, abran y participen en tu correo electrónico. Prefiere siempre los correos electrónicos bien dirigidos a los bombardeos indiscriminados a la hora de calentar IP.

### Establecer una cadencia de envío coherente

Una vez completado el calentamiento de IP, cree una cadencia de envío, asegurándose también de repartir sus correos electrónicos a lo largo de uno o varios días. Si creas un calendario lo más coherente posible, puedes evitar un enfriamiento de la IP, que puede ocurrir si el volumen de envíos se detiene o disminuye significativamente durante más de unos días. 

Consulte nuestro [calendario de calentamiento de IP](#ip-warming-schedules) para distribuir su envío a lo largo de un periodo de tiempo más largo, en lugar de enviar un bombardeo masivo a una hora concreta.

### Limpie sus listas de correo electrónico

Confirme que su lista de correo electrónico está limpia y no tiene correos electrónicos antiguos o no verificados. Lo ideal es que te asegures de que [cumples tanto la CASL como la CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Controla la reputación del remitente

Cuando lleves a cabo el proceso de calentamiento de IP, asegúrate de vigilar cuidadosamente la reputación del remitente mientras realizas el proceso de calentamiento de IP. Es importante vigilar estas métricas específicas:
- **Tasas de rebote:** Si alguna campaña rebota más de un 3-5%, deberías evaluar la limpieza de tu lista siguiendo las directrices de nuestro [Mantenla limpia: la importancia del saneamiento de las listas de correo electrónico](https://www.braze.com/blog/email-list-hygiene/). Además, deberías plantearte implantar una [política de suspensión]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) para dejar de enviar por correo electrónico a las direcciones de correo electrónico inactivas o no comprometidas.
- **Informes de spam:** Si alguna campaña se considera spam en un porcentaje superior al 0,08%, debe reevaluar el contenido que envía, comprobar que está dirigido a un público interesado y asegurarse de que sus mensajes están redactados adecuadamente para despertar su interés.
- **Tasas de apertura:** Las tasas de apertura son un indicador útil de la ubicación en la bandeja de entrada. Si sus tasas de apertura únicas superan el 25%, es probable que esté experimentando una alta colocación en la bandeja de entrada, lo que indica una reputación de remitente positiva.

{% alert tip %}
Braze recomienda no utilizar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para calentar sus IPs. Dado que las campañas de calentamiento por IP son algunas de las primeras campañas que se envían, Braze no dispondrá de suficiente información sobre los usuarios para calcular el momento óptimo de envío. En este caso, todos los mensajes con Intelligent Timing se predeterminarían a la hora alternativa y se enviarían a la misma hora de todos modos.
{% endalert %}

{% alert tip %}
Es normal que se envíe correo a la carpeta de spam durante el calentamiento de IP porque su dominio e IP aún no han establecido una reputación positiva. Si el correo llega a la carpeta de spam, es posible que el administrador de correo tenga que añadir el dominio y la IP de envío Braze a la lista de permitidos de la empresa.
{% endalert %}

