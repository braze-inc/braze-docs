---
nav_title: "Mensajes dentro de la aplicación"
article_title: Mensajes dentro de la aplicación
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "Mensajes dentro de la aplicación"
guide_top_text: "Los mensajes dentro de la aplicación te ayudan a hacer llegar contenido a tu usuario sin interrumpir su día con una notificación push, ya que estos mensajes no se entregan fuera de la aplicación del usuario y no interfieren en su pantalla de inicio. <br><br>Los mensajes dentro de la aplicación, personalizados y adaptados, mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con una gran variedad de diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca. Vienen con contexto, tienen menor urgencia y se entregan cuando el usuario está activo dentro de tu aplicación. Para ver ejemplos de mensajes dentro de la aplicación, consulta <a href='https://www.braze.com/customers'>las historias de nuestros clientes</a>."
description: "Esta página de inicio es el hogar de todos los mensajes dentro de la aplicación. Aquí puedes encontrar artículos sobre cómo crear mensajes dentro de la aplicación, el editor de arrastrar y soltar, cómo personalizar tus mensajes, informes y mucho más."
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "Artículos populares"
guide_featured_list:
- name: "Editor de arrastrar y soltar"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Editor tradicional"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Detalles creativos"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "Prueba"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "Informar"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Modo oscuro"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Pregunta de valoración de la App Store"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "Cuestionario sencillo"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "Localizaciones en mensajes"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "Buenas prácticas"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "PREGUNTAS FRECUENTES"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Casos de uso potencial

Con el rico nivel de contenido que ofrecen los mensajes dentro de la aplicación, puedes aprovechar este canal para una gran variedad de casos de uso:

| Casos de uso | Explicación |
| --- | --- |
| Preparación para las notificaciones push | Ejecuta una campaña [de preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) utilizando un mensaje dentro de la aplicación para mostrar a tus clientes las ventajas de optar por push para tu aplicación o sitio web, y preséntales una solicitud para que concedan permiso push.
| Ventas y promociones | Utiliza mensajes modales dentro de la aplicación para saludar a los clientes con medios visualmente atractivos que contengan códigos promocionales estáticos u ofertas. Incentivarles para que realicen compras o conversiones cuando de otro modo no lo habrían hecho. |
| Fomentar la adopción de características | Anima a los clientes a utilizar otras partes de tu aplicación o a beneficiarse de un servicio. |
| Campañas altamente personalizadas | Coloca mensajes dentro de la aplicación como lo primero que ven tus clientes cuando entran en tu aplicación o sitio web. Añade algunas características de personalización Braze, como el [Contenido Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), para obligar a los usuarios a actuar y, por tanto, hacer que tu difusión sea más eficaz.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Otros casos de uso a tener en cuenta son los siguientes:

- Nuevas características de la aplicación
- Administrador de aplicaciones
- Comentarios
- Mejoras o actualizaciones de la aplicación
- Regalos y sorteos

## Tipos de mensajes estándar

Las siguientes pestañas muestran cómo se ven tus usuarios al abrir uno de nuestros tipos de mensajes dentro de la aplicación estándar: mensajes deslizantes, modales y a pantalla completa dentro de la aplicación.

{% tabs %}
{% tab Slideup %}

Los mensajes deslizantes suelen aparecer en la parte superior e inferior de la pantalla de la aplicación (puedes configurarlo cuando crees tu mensaje). Son ideales para alertar a tus usuarios sobre nuevas condiciones de servicio, cookies y otros fragmentos de información.

\![Mensaje deslizamiento hacia arriba dentro de la aplicación que aparece desde la parte inferior de la pantalla de la aplicación. El deslizador incluye la imagen de un icono y un breve mensaje.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Los modales aparecen en el centro de la pantalla del dispositivo con una superposición de pantalla que ayuda a que destaque sobre tu aplicación en segundo plano. Son perfectos para sugerir no tan sutilmente a tu usuario que aproveche una oferta o sorteo.

\![Mensaje modal dentro de la aplicación que aparece en el centro de una aplicación y sitio web como un diálogo. El modal incluye una imagen, una cabecera, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

Los mensajes a pantalla completa son exactamente lo que esperas: ¡ocupan toda la pantalla del dispositivo! Este tipo de mensaje es ideal cuando realmente necesitas la atención de tu usuario, como en el caso de las actualizaciones obligatorias de la aplicación.

Mensaje dentro de la aplicación a pantalla completa ocupando una pantalla de la aplicación. El mensaje a pantalla completa incluye una imagen grande, una cabecera, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

Además de estas plantillas de mensajes listas para usar, también puedes personalizar aún más tu mensajería utilizando mensajes HTML dentro de la aplicación, modales web con CSS o formularios web de captura de correo electrónico. Para más información, consulta [Personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Más recursos

Antes de empezar a crear tus propias campañas de mensajes dentro de la aplicación -o de utilizar mensajes dentro de la aplicación en una campaña multicanal-, te recomendamos encarecidamente que consultes nuestra [Guía de preparación de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Esta guía trata de las cuestiones de segmentación, contenido y conversión que debes tener en cuenta al crear mensajes dentro de la aplicación.
