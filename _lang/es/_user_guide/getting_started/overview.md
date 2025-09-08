---
nav_title: Visión general de Braze
article_title: "Cómo empezar: Visión general de Braze"
page_order: 1
page_type: reference
description: "Familiarízate con los conceptos básicos que necesitarás conocer cuando trabajes en Braze."

---

# Cómo empezar: Visión general de Braze

¡Te damos la bienvenida a Braze! Esta colección de artículos le ayudará a iniciarse en nuestra plataforma y le introducirá en los términos, características y funcionalidades clave de Braze. Esta página presenta los conceptos básicos que necesitará conocer cuando trabaje en Braze.

{% alert tip %}
Le recomendamos encarecidamente que consulte nuestro curso gratuito [Braze Foundations for](https://learning.braze.com/page/braze-foundations-for-everyone) Everyone junto con estos artículos. No se necesita ningún nombre de usuario o cuenta especial para este curso. Si eres desarrollador y buscas un resumen técnico de Braze, consulta también [Introducción para desarrolladores]({{site.baseurl}}/developer_guide/getting_started/platform_overview/).
{% endalert %}

En las secciones de Introducción, nos centraremos en las implementaciones habituales de Braze. Sin embargo, Braze es increíblemente flexible y puede personalizarse para aportar valor a su organización de diversas maneras. Para establecer claridad y brevedad, hemos proporcionado una descripción general de la configuración por defecto en lugar de ofrecer instrucciones rígidas. Reconocemos que cada organización tiene sus propias necesidades, y Braze está diseñado para satisfacer una amplia gama de opciones de personalización que pueden adaptarse a sus requisitos específicos.

Exploremos juntos el poder de Braze.

## Cómo funciona Braze

Braze es una plataforma de captación de clientes que ayuda a marcas de todos los tamaños a crear campañas personalizadas y dirigidas a través de diversos canales. Braze le ofrece la posibilidad de escuchar a sus clientes, comprender lo que su comportamiento está indicando y, a continuación, actuar enviando a los clientes el mensaje adecuado, a través del canal adecuado, en el momento adecuado.

{% alert tip %}
Asegúrate de [añadir a tus colegas a Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users) para que puedan explorar la plataforma contigo.
{% endalert %}

## Usuarios y segmentos

Los usuarios son tus clientes, las personas que reciben los mensajes que envías con Braze. Todos los datos que se recopilan sobre un usuario y se ingieren en Braze se almacenan en su perfil de usuario, como sus datos demográficos, información personal, preferencias y comportamientos. Esta información potencia su mensajería y es la forma en que puede adaptar sus mensajes al usuario adecuado.

![]({% image_buster /assets/img/getting_started/user_profile.png %})

Los segmentos dividen su base de clientes en grupos más pequeños a los que puede dirigirse con mensajes específicos. Puede utilizar diferentes variables para crear segmentos, desde características como el sexo, la ubicación y la edad hasta comportamientos como patrones de interacción con campañas anteriores o en qué punto del recorrido del cliente se encuentran.

Los segmentos son dinámicos: los usuarios pueden entrar y salir de ellos en tiempo real en función de su comportamiento y de su relación con la marca. Esto garantiza que sus clientes reciban los mensajes más relevantes para ellos en cada momento. Puede crear tantos segmentos como necesite para sus objetivos y mensajes.

![]({% image_buster /assets/img/getting_started/segment.png %})

Más información: [Cómo empezar: Usuarios y segmentos]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Campañas y Canvas

Las campañas y los lienzos son la forma de enviar mensajes a los usuarios.

Las campañas son mejores para mensajes únicos enviados a un segmento de audiencia específico a través de varios canales. Puede aprovechar cualquiera de nuestros canales de mensajería compatibles en su campaña (correo electrónico, push, mensajes dentro de la aplicación, SMS, etc.).

Los lienzos son flujos de trabajo de campaña avanzados que le permiten automatizar y orquestar recorridos personalizados de los clientes a través de múltiples canales. Dentro de un Canvas, puede configurar lógica de ramificación, retrasos, puntos de decisión y eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los lienzos ayudan a garantizar una comunicación coherente y fluida en los distintos puntos de contacto, lo que aumenta las posibilidades de captación y conversión de clientes. 

Más información: [Cómo empezar: Campañas y lonas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Espacios de trabajo

Los espacios de trabajo agrupan sus datos -usuarios, segmentos, campañas y lienzos- en una única ubicación. La información no se comparte entre espacios de trabajo, así que tenlo en cuenta cuando añadas sitios web y aplicaciones a tus espacios de trabajo. Como práctica recomendada, sugerimos que sólo se agrupen en un espacio de trabajo diferentes versiones de la misma aplicación o de aplicaciones muy similares.

Ejemplos de uso de los espacios de trabajo

- Diferentes líneas de productos o aplicaciones
- Diferentes audiencias (como conductores de entrega frente a clientes)
- Separar las empresas
- Entorno de pruebas

Más información: [Cómo empezar: Espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Integración de Braze

Braze está diseñado para ponerse en marcha rápida y fácilmente. Nuestro tiempo medio de creación de valor es de seis semanas en nuestra base de clientes de cientos de marcas.

![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Este es el marco de Braze para estimar la duración de su integración basándose en cuatro componentes en los que puede trabajar en paralelo. El intervalo típico es de 30 a 180 días, y la mayoría de las cuentas completan su integración en un plazo de 45 a 60 días.

- **Nivel de complejidad de la migración de la campaña:** El tiempo que se tarda en migrar las campañas depende de cuántas tengas, de lo personalizadas que estén y de tus recursos. Si tienes menos de diez campañas que migrar, tardarás menos de 60 días. Pero si tienes más de 100 campañas, será más complicado. Si es una sola persona la que migra 100 campañas, no es lo mismo que si son 10 personas las que migran 100.

{% alert tip %}
¿Necesita ayuda con su migración? Nuestros [socios Braze certificados](https://www.braze.com/partners/solutions-partners) pueden ayudarle.
{% endalert %}

- **Volumen de correo electrónico:** Para enviar correos electrónicos, tendrás que calentar tus IP. [El calentamiento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) es el proceso de construir la reputación del remitente con tus direcciones IP recién asignadas. Si envías menos de 2-3 millones de correos electrónicos al día, tu calentamiento de IP debería durar 30 días o menos. Ten en cuenta tu pico de envío. Es decir, si normalmente envías 2 millones de correos electrónicos al día, pero tienes previsto enviar 7 millones durante un período estacional, ese "pico" de envíos es el que debes calentar. Los remitentes de gran volumen pueden utilizar varias IP para acelerar el proceso de calentamiento.
- **Complejidad organizativa:** Nuestro proceso de incorporación puede adaptarse a las necesidades de su empresa. Tanto si se trata de una única unidad de negocio, como si tiene un Centro de Excelencia, varias unidades independientes o utiliza agencias para aumentar sus equipos, Braze tiene experiencia trabajando en todos los escenarios.
- **Sofisticación de la infraestructura de datos:** Si solo estás implementando el SDK de Braze o ya tienes una Plataforma de Datos de los Clientes (CDP), es posible tenerlo todo configurado en solo 30 días. El uso de un CDP moderno puede acelerar el proceso. Pero si tiene muchos sistemas backend, herramientas o bases de datos que conectar con Braze, puede llevar más tiempo y necesitar más recursos dedicados para terminar la configuración.

Más información: [Cómo empezar: Visión general de la integración]({{site.baseurl}}/user_guide/getting_started/integration/).

