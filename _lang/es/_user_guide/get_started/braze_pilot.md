---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot es una aplicación móvil diseñada para conectarse fácilmente con tu panel de Braze. Esto te permite lanzar campañas y Canvases a la aplicación, dando vida a los mensajes de Braze en tu propio teléfono. Braze Pilot incluye una biblioteca de simulaciones de aplicaciones para marcas ficticias que representan diferentes sectores, lo que te permite experimentar cómo se verían tus mensajes desde la perspectiva de tus clientes."
description: "Echa un vistazo a las diferentes formas en que puedes utilizar Braze para enviar mensajes desde el panel de Braze a tu teléfono."

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Introducción a Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Diccionario de datos
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Vínculos profundos
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Simulaciones de aplicaciones piloto

El núcleo de Braze Pilot es su biblioteca de simulaciones de aplicaciones. Cada aplicación es una simulación realista de una marca ficticia específica del sector, equipada para registrar una amplia variedad de eventos y atributos que crean infinitas oportunidades para impulsar los casos de uso habituales de Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington es una aplicación de fitness con entrenamientos, objetivos de ejercicio y un servicio premium Steppington+. Ofrece varios lugares para mostrar [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), una sección que se puede revelar con [indicadores de características]({{site.baseurl}}/developer_guide/feature_flags) y una sólida biblioteca de registro de eventos personalizados que permite ilustrar muchos recorridos del cliente para este sector.

![La página de inicio de Steppington con iconos para entrenamiento de maratón, yoga, ciclismo y pesas.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinth es una aplicación de comercio electrónico que vende (lo has adivinado) ¡pantalones! La aplicación PantsLabyrinth incluye una experiencia completa de pago con carrito de la compra, una característica opcional de lista de deseos que se puede habilitar con un indicador de característica y muchas oportunidades para hacer bromas ingeniosas a tus amigos del Reino Unido.

![Página de producto de PantsLabyrinth con opciones para añadir vaqueros al carrito.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon es un servicio de streaming perfectamente diseñado para ilustrar los casos de uso habituales de Braze en torno a la interacción con el contenido. 

![La aplicación MovieCanon con diferentes thrillers para ver.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Cómo se conecta Pilot con tu panel de Braze

El SDK de Braze es un paquete de código que recopila datos de tus usuarios una vez que se integra con tu aplicación o sitio web. Cuando conectas Pilot a tu panel de control, inicializas esta conexión entre la aplicación Pilot de tu teléfono y el SDK de Braze, y estableces una conexión única con tu instancia de Braze al proporcionar a Pilot tu identificador de clave de API para tu panel de control.

![El primer paso para la configuración de Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Una vez que Pilot se conecta a tu panel de Braze, el SDK de Braze funciona en la aplicación igual que lo haría una vez que integras el SDK en tu propia aplicación o sitio web. Esto significa que Braze:

- Almacena datos sobre tu actividad de usuario en Pilot, incluidos datos personalizados específicos de las marcas ficticias de la aplicación.
- Recopila automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push.
- Notificaciones push potentes, mensajes dentro de la aplicación y canales de mensajería de tarjetas de contenido que requieren la integración de SDK para funcionar.

Para obtener más información sobre el SDK de Braze, consulta [Integración]({{site.baseurl}}/user_guide/getting_started/integration).

![La pila de interacción con los clientes de Braze, que incluye integraciones, API, SDK para la ingesta de datos, clasificación, orquestación, personalización y acción con canales de mensajería para un bucle de retroalimentación interactivo con tus clientes.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Perfiles de usuario en Braze

Todos los datos enviados a Braze se almacenan en un perfil de usuario dedicado a un usuario concreto de tu aplicación o sitio web. Una vez que conectes Pilot con tu panel de Braze, Braze comenzará a registrar datos sobre ti como usuario de Pilot. Hay dos tipos de usuarios que se pueden crear para ti a través de esta conexión: usuarios anónimos e identificados.

### Anónimo 

Este estado de conexión representa la experiencia de un visitante de tu aplicación o sitio web que aún no ha iniciado sesión. Si inicializas Pilot como usuario anónimo, Braze crea un [perfil de usuario anónimo]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) para ti y registra allí los datos sobre tu actividad. Los usuarios anónimos pueden seguir siendo objeto de campañas, pero no podrás consultar su perfil de usuario directamente en tu panel de Braze.

### Identificado

Este estado de conexión significa que Braze reconoce tu perfil de usuario a través de un identificador único que se te ha asignado, conocido como identificador externo. Puedes buscar este identificador externo en la página **Búsqueda** de **usuarios** de tu panel para localizar tu perfil de usuario, que almacenará todos los atributos de usuario y eventos registrados desde Pilot en función de tu actividad en la aplicación.

![Ejemplo de perfil de usuario de Braze para el usuario «torchie-208117».]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Tipo de conexión

Para comprobar qué tipo de conexión tienes, puedes consultar el estado de la conexión en la parte superior derecha de la pantalla.

{% tabs local %}
{% tab Anonymous user  %}

**Anónimo** indica que estás registrando datos como usuario anónimo.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

Si estás registrando datos como usuario identificado, aparecerá un icono de usuario junto a tu ID externo.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**«No conectado»** indica que aún no has inicializado la conexión del SDK de Braze con Pilot.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campañas y Canvas

Las campañas y los lienzos son la forma de enviar mensajes a los usuarios. 

- Las campañas son mejores para mensajes únicos enviados a un segmento de audiencia específico a través de varios canales. 
- Los lienzos son flujos de trabajo de campaña avanzados que le permiten automatizar y orquestar recorridos personalizados de los clientes a través de múltiples canales. Dentro de un Canvas, puede configurar lógica de ramificación, retrasos, puntos de decisión y eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los lienzos ayudan a garantizar una comunicación coherente y fácil entre los diferentes puntos de contacto, lo que aumenta las posibilidades de lograr una interacción con los clientes y conseguir conversiones.

## Canales de mensajería compatibles

Braze Pilot actualmente admite [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), que aparecen en tu aplicación y entregan mensajes oportunos mientras el usuario está realizando una interacción activa.

![Un mensaje dentro de la aplicación MovieCanon: «¿Te gusta MovieCanon? ¡Recomienda a tus amigos!», con la opción de introducir tu dirección de correo electrónico para enviar un referido.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}