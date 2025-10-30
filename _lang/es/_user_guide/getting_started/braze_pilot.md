---
nav_title: Piloto Braze
page_order: 10.5
layout: dev_guide
guide_top_header: "Piloto Braze"
guide_top_text: "Braze Pilot es una aplicación móvil diseñada para conectarse fácilmente con tu panel Braze. Esto te permite lanzar campañas y Lienzos a la aplicación, dando vida a los mensajes Braze en tu propio teléfono. Braze Pilot incluye una biblioteca de simulaciones de aplicaciones para marcas ficticias que representan diferentes sectores, lo que te permite experimentar cómo podría ser tu mensajería desde la perspectiva de tus clientes."
description: "Echa un vistazo a las distintas formas en que puedes utilizar Braze para lanzar mensajes desde el panel de Braze a tu teléfono."

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Primeros pasos con Braze Pilot
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

El núcleo de Braze Pilot es su biblioteca de simulaciones de aplicaciones. Cada aplicación es una simulación realista de una marca ficticia específica del sector, instrumentada para registrar una rica variedad de eventos y atributos que crean infinitas oportunidades para potenciar los casos de uso comunes de Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington es una aplicación de fitness con entrenamientos, objetivos de ejercicio y un servicio premium Steppington+. Ofrece varios lugares para mostrar [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), una sección que puede revelarse con [banderas de características]({{site.baseurl}}/developer_guide/feature_flags), y una sólida biblioteca de registro de eventos personalizados que hacen posible ilustrar muchos recorridos del cliente para este sector.

Página de inicio de Steppington con iconos de entrenamiento para maratón, yoga, ciclismo y pesas.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantalonesLaberinto

PantsLabyrinth es una aplicación de comercio electrónico que vende (lo has adivinado) ¡pantalones! La aplicación PantsLabyrinth incluye una experiencia completa de pago con carrito de la compra, una característica opcional de lista de deseos que puede habilitarse con una bandera de característica, y muchas oportunidades de bromas socarronas con amigos del Reino Unido.

Página de producto de PantsLabyrinth con opciones para añadir vaqueros a la cesta.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon es un servicio de streaming perfectamente diseñado para ilustrar casos de uso comunes de Braze en torno a la interacción con los contenidos. 

La aplicación MovieCanon con diferentes películas de suspense para ver.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Cómo se conecta Pilot con tu panel de Braze

El SDK de Braze es un paquete de código que recopila datos de tus usuarios una vez integrado en tu aplicación o sitio web. Cuando conectas Pilot a tu panel, inicializas esta conexión entre la aplicación Pilot de tu teléfono y el SDK de Braze, y estableces una conexión única con tu instancia de Braze dando a Pilot tu identificador de clave de API para tu panel.

El primer paso para configurar Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Después de que Pilot se conecte a tu panel de Braze, el SDK de Braze funcionará en la aplicación igual que lo hará cuando integres el SDK con tu propia aplicación o sitio web. Esto significa que Braze lo hará:

- Almacenar datos sobre tu actividad de usuario en Pilot, incluidos datos personalizados específicos de las marcas ficticias de la aplicación.
- Recoge automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push.
- Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de tarjeta de contenido que requieren la integración de SDK para funcionar.

Para más información sobre el SDK de Braze, consulta [Integración]({{site.baseurl}}/user_guide/getting_started/integration).

La pila de interacción con los clientes Braze, que incluye integraciones, API, SDK para la ingesta de datos, clasificación, orquestación, personalización y acción con canales de mensajería para un bucle de retroalimentación interactivo con tus clientes.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Perfiles de usuario en Braze

Cada dato enviado a Braze se almacena en un perfil de usuario dedicado a un usuario concreto de tu aplicación o sitio web. Una vez que conectes Pilot con tu panel Braze, Braze empezará a registrar datos sobre ti como usuario de Pilot. Hay dos tipos de usuarios que podrían crearse para ti a través de esta conexión: anónimos e identificados.

### Anónimo 

Este estado de conexión representa la experiencia de un invitado de tu aplicación o sitio web que aún no se ha conectado. Si inicializas Pilot como usuario anónimo, Braze crea un [perfil de usuario anónimo]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) para ti y registra datos sobre tu actividad en él. Los usuarios anónimos pueden seguir siendo objeto de campañas, pero no podrás consultar su perfil de usuario directamente en tu panel Braze.

### Identificado

Este estado de conexión significa que Braze reconoce tu perfil de usuario a través de un identificador único que se te ha asignado, conocido como identificador externo. Puedes buscar este identificador externo en la página **de Búsqueda de usuarios** de tu panel para localizar tu perfil de usuario, que almacenará todos los atributos de usuario y eventos registrados desde Pilot en función de tu actividad en la aplicación.

\![Un ejemplo de perfil de usuario Braze para el usuario "torchie-208117".]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Tipo de conexión

Para comprobar qué tipo de conexión tienes, puedes consultar el estado de la conexión en la parte superior derecha de tu pantalla.

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

**No conectado** indica que aún no has inicializado la conexión del SDK de Braze con Piloto.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campañas y Lonas

Las campañas y los lienzos son la forma de enviar mensajes a tus usuarios. 

- Las campañas son mejores para mensajes únicos enviados a un segmento de audiencia específico a través de varios canales. 
- Los lienzos son flujos de trabajo de campaña avanzados que te permiten automatizar y orquestar recorridos del cliente personalizados a través de múltiples canales. Dentro de un Canvas, puedes configurar la lógica de ramificación, los retrasos, los puntos de decisión y los eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los lienzos ayudan a garantizar una comunicación coherente y sin fisuras en los distintos puntos de contacto, aumentando las posibilidades de interacción con los clientes y la conversión.

## Canales de mensajería compatibles

Braze Pilot actualmente admite [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), que aparecen en tu aplicación, entregando mensajería oportuna mientras el usuario está interactuando activamente.

Mensaje dentro de la aplicación MovieCanon "¿Disfrutas de MovieCanon? Recomienda a tus amigos!" con la opción de introducir tu dirección de correo electrónico para enviar referidos.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}