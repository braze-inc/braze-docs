---
nav_title: Resumen de Braze
article_title: "Cómo empezar: Resumen de Braze"
page_order: 1
page_type: reference
description: "Familiarízate con los conceptos básicos que necesitarás conocer cuando trabajes en Braze."

---

# Cómo empezar: Resumen de Braze

¡Bienvenido a Braze! Esta colección de artículos te ayudará a empezar a utilizar nuestra plataforma y te presentará los términos, características y funcionalidades clave de Braze. Esta página presenta los conceptos básicos que necesitarás conocer cuando trabajes en Braze.

{% alert tip %}
Te recomendamos encarecidamente que consultes nuestro curso gratuito [Fundamentos de Braze para todos](https://learning.braze.com/page/braze-foundations-for-everyone) junto con estos artículos. No es necesario iniciar sesión ni tener una cuenta especial para este curso. Si eres desarrollador y buscas un resumen técnico de Braze, consulta también [Introducción para desarrolladores]({{site.baseurl}}/developer_guide/getting_started/platform_overview/).
{% endalert %}

En las secciones de Introducción, nos centraremos en las implementaciones habituales de Braze. Sin embargo, Braze es increíblemente flexible y puede personalizarse para aportar valor a tu organización de diversas maneras. Para establecer claridad y brevedad, hemos proporcionado un resumen descriptivo de la configuración predeterminada en lugar de ofrecer instrucciones rígidas. Reconocemos que cada organización tiene sus propias necesidades, y Braze está construido para atender a una diversa gama de opciones de personalización que pueden adaptarse a tus requisitos específicos.

Exploremos juntos el poder de Braze.

## Cómo funciona Braze

Braze es una plataforma de interacción con los clientes que ayuda a las marcas de todos los tamaños a crear campañas personalizadas y específicas en varios canales. Braze te da la capacidad de escuchar a tus clientes, comprender lo que su comportamiento está indicando y, a continuación, actuar enviando a los clientes el mensaje adecuado, a través del canal adecuado, en el momento adecuado.

{% alert tip %}
Asegúrate de [añadir a tus colegas a Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users) para que puedan explorar la plataforma contigo.
{% endalert %}

## Usuarios y segmentos

Los usuarios son tus clientes: las personas que reciben los mensajes que envías con Braze. Todos los datos que recopilas sobre un usuario e ingestas en Braze se almacenan en su perfil de usuario, como sus datos demográficos, información personal, preferencias y comportamientos. Esta información potencia tu mensajería y es la forma en que puedes adaptar tus mensajes al usuario adecuado.

\![]({% image_buster /assets/img/getting_started/user_profile.png %})

Los segmentos dividen tu base de clientes en grupos más pequeños a los que puedes dirigirte con mensajería específica. Puedes utilizar distintas variables para crear segmentos, desde características como el sexo, la ubicación y la edad hasta comportamientos como patrones de interacción con campañas anteriores o en qué punto del recorrido del cliente se encuentran.

Los segmentos son dinámicos: los usuarios pueden entrar y salir de los segmentos en tiempo real en función de su comportamiento y de dónde se encuentran en relación con tu marca. Esto garantiza que tus clientes reciban la mensajería más relevante para ellos en cada momento. Puedes crear tantos segmentos como necesites para tus fines de segmentación y mensajería.

\![]({% image_buster /assets/img/getting_started/segment.png %})

Para más información, consulta [Cómo empezar: Usuarios y segmentos]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Campañas y Lonas

Las campañas y los lienzos son la forma de enviar mensajes a tus usuarios.

Las campañas son mejores para mensajes únicos enviados a un segmento de audiencia específico a través de varios canales. Puedes aprovechar cualquiera de nuestros canales de mensajería compatibles en tu campaña (correo electrónico, push, mensajes dentro de la aplicación, SMS y más).

Los lienzos son flujos de trabajo de campaña avanzados que te permiten automatizar y orquestar recorridos del cliente personalizados a través de múltiples canales. Dentro de un Canvas, puedes configurar la lógica de ramificación, los retrasos, los puntos de decisión y los eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los lienzos ayudan a garantizar una comunicación coherente y sin fisuras en diferentes puntos de intervención, aumentando las posibilidades de interacción con los clientes y la conversión. 

Para más información, consulta [Cómo empezar: Campañas y lonas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Espacios de trabajo

Los espacios de trabajo agrupan tus datos -usuarios, segmentos, campañas y Lienzos- en una sola ubicación. La información no se comparte entre espacios de trabajo, así que tenlo en cuenta cuando añadas sitios web y aplicaciones a tus espacios de trabajo. Como práctica recomendada, te sugerimos que sólo agrupes diferentes versiones de la misma aplicación o de aplicaciones muy similares en un mismo espacio de trabajo.

Algunos ejemplos de uso de los espacios de trabajo son:

- Diferentes líneas de productos o aplicaciones
- Diferentes audiencias (como conductores de entrega frente a clientes)
- Separar empresas
- Entorno de pruebas

Para más información, consulta [Cómo empezar: Espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Integración de Braze

Braze está diseñado para ponerse en marcha rápida y fácilmente. Nuestro tiempo medio de obtención de valor es de seis semanas en nuestra base de clientes de cientos de marcas.

\![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Aquí tienes el marco Braze para estimar la duración de tu integración basándote en cuatro componentes en los que puedes trabajar en paralelo. El intervalo típico es de 30 a 180 días, y la mayoría de las cuentas completan su integración en un plazo de 45 a 60 días.

- **Nivel de complejidad de la migración de la campaña:** El tiempo que se tarda en migrar las campañas depende de cuántas tengas, de lo personalizadas que estén y de tus recursos. Si tienes menos de diez campañas que migrar, tardarás menos de 60 días. Pero si tienes más de 100 campañas, será más complicado. Si es una sola persona la que migra 100 campañas, es diferente a que sean 10 personas las que migren 100.

{% alert tip %}
¿Necesitas ayuda con tu migración? ¡Nuestros [socios certificados de Braze](https://www.braze.com/partners/solutions-partners) pueden ayudarte!
{% endalert %}

- **Volumen de correo electrónico:** Para enviar correos electrónicos, tendrás que calentar tus IP. [El calentamiento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) es el proceso de construir la reputación del remitente con tus direcciones IP recién asignadas. Si envías menos de 2-3 millones de correos electrónicos al día, tu calentamiento de IP debería durar 30 días o menos. Ten en cuenta tu pico de envío. Si normalmente envías 2 millones de correos electrónicos al día, pero tienes previsto enviar 7 millones durante un periodo estacional, ese "pico" de envíos es el que debes calentar. Los remitentes de gran volumen pueden utilizar varias IP para acelerar el proceso de calentamiento.
- **Complejidad organizativa:** Nuestro proceso de incorporación puede adaptarse a las necesidades de tu empresa. Tanto si eres una única unidad de negocio, tienes un Centro de Excelencia, varias unidades independientes o utilizas agencias para aumentar tus equipos, Braze tiene experiencia trabajando en todos los escenarios.
- **Sofisticación de la infraestructura de datos:** Si sólo estás implementando el SDK de Braze o ya tienes una Plataforma de Datos de los Clientes (CDP), es posible tenerlo todo configurado en sólo 30 días. Utilizar un CDP moderno puede acelerar el proceso. Pero si tienes muchos sistemas backend, herramientas o bases de datos que conectar con Braze, puede que te lleve más tiempo y necesites más recursos dedicados para terminar la configuración.

Para más información, consulta [Cómo empezar: Resumen de la integración]({{site.baseurl}}/user_guide/getting_started/integration/).

