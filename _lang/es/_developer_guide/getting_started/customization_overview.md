---
nav_title: Resumen de la personalización
article_title: Resumen de la personalización
page_order: 10
description: "Este artículo de referencia cubre los conceptos esenciales de la personalización y ampliación de los canales de mensajería del SDK."
hidden: true
layout: redirect
redirect_to: /docs/developer_guide/getting_started/
---

# Resumen de la personalización

> ¡Casi todo en Braze es totalmente personalizable! Los artículos de esta Guía de personalización te muestran cómo enfocar el perfeccionamiento de tu experiencia Braze mediante una mezcla de configuración y personalización. Durante este proceso, los equipos de marketing e ingeniería deben colaborar estrechamente para coordinar exactamente cómo personalizar los canales de mensajería Braze.

{% alert note %}
El SDK de Braze es un potente conjunto de herramientas, pero a alto nivel proporciona dos importantes funciones: ayuda a recopilar y sincronizar los datos de usuario entre plataformas en un perfil de usuario consolidado, y también gestiona canales de mensajería como mensajes dentro de la aplicación, notificaciones push y tarjetas de contenido. Para los artículos de la Guía de personalización, se asume que ya has pasado por el [proceso de implementación del SDK]({{site.baseurl}}/developer_guide/home).
{% endalert %}

Todos los componentes de Braze están diseñados para ser accesibles, adaptables y personalizables. Por ello, te recomendamos que empieces con los componentes predeterminados de `BrazeUI` y los personalices para adaptarlos a las necesidades de tu marca y a tu caso de uso. En Braze, dividimos la personalización en tres enfoques diferentes, según el esfuerzo asociado y el nivel de flexibilidad proporcionado. Estos enfoques se denominan "gatear", "caminar" o "correr".

- **Gatear:** Aprovecha las opciones básicas de estilo para una implementación rápida y de poco esfuerzo.
- **Caminar:** Añade un estilo personalizado a las plantillas predeterminadas para adaptarlas mejor a la experiencia de tu marca.
- **Correr:** Personaliza cada parte de tu mensajería, desde el estilo hasta el comportamiento y las conexiones entre canales.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Gatear %}

![Ejemplo de aplicación financiera que muestra tarjetas de contenido con imagen subtitulada y sólo imagen]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

El enfoque Crawl pone el poder de la personalización directamente en manos de los especialistas en marketing. Aunque para integrar los canales de mensajería Braze en tu aplicación o sitio web es necesario un ligero trabajo de desarrollo previo, este enfoque te permite ponerte en marcha antes. 

Los especialistas en marketing determinan el contenido, la audiencia y el momento de los mensajes a través del panel. Sin embargo, las opciones de estilo son limitadas. Este enfoque es el más adecuado para equipos con recursos limitados de desarrolladores o que desean compartir rápidamente contenidos sencillos. 

<table>
<thead>
  <tr>
    <th>Personalización</th>
    <th>Descripción</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Esfuerzo</b></td>
    <td>Baja</td>
  </tr>
    <tr>
    <td><b>Trabajo de desarrollador</b></td>
    <td>0-1 horas</td>
  </tr>
  <tr>
    <td><b>Estilo de tarjeta</b></td>
    <td>Utiliza las plantillas predeterminadas de Braze.</td>
  </tr>
  <tr>
    <td><b>Comportamiento</b></td>
    <td>Elige entre las opciones de comportamiento predeterminadas.</td>
  </tr>
  <tr>
    <td><b>Seguimiento analítico</b></td>
    <td>Los análisis se capturan en Braze.</td>
  </tr>
  <tr>
    <td><b>Pares clave-valor</b></td>
    <td>Opcional, potencia la personalización adicional de IU/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Caminar %}

![Ejemplo de aplicación financiera que muestra tarjetas de contenido con personalización]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Un enfoque híbrido de la implementación, el enfoque Walk implica que tanto el equipo de marketing como el de desarrolladores colaboren para hacer coincidir la marca de tu aplicación o sitio web. 

Durante el proceso de implementación, los desarrolladores escriben código personalizado para actualizar el aspecto de un canal de mensajería para que se ajuste más a tu marca. Esto incluye cambiar el tipo y tamaño de letra, las esquinas redondeadas y los colores. Este enfoque sigue utilizando las opciones predeterminadas, sólo que con un estilo de plantilla programado.

Los especialistas en marketing siguen manteniendo el control de la audiencia, el contenido, el comportamiento al hacer clic y la caducidad directamente en el panel Braze.

<table>
<thead>
  <tr>
    <th>Personalización</th>
    <th>Descripción</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Esfuerzo</b></td>
    <td>Baja</td>
  </tr>
    <tr>
    <td><b>Trabajo de desarrollador</b></td>
    <td>0-4 horas</td>
  </tr>
  <tr>
    <td><b>INTERFAZ DE USUARIO</b></td>
    <td>Utiliza plantillas Braze o utiliza plantillas creadas por tus propios desarrolladores.</td>
  </tr>
  <tr>
    <td><b>Comportamiento</b></td>
    <td>Elige entre las opciones de comportamiento predeterminadas.</td>
  </tr>
  <tr>
    <td><b>Seguimiento analítico</b></td>
    <td>Los análisis predeterminados se capturan en Braze.</td>
  </tr>
  <tr>
    <td><b>Pares clave-valor</b></td>
    <td>Opcional, potencia la personalización adicional de IU/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Correr %}

![Ejemplo de aplicación financiera que muestra tarjetas de contenido personalizadas con captura de correo electrónico]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Con el enfoque de "correr", los desarrolladores toman la iniciativa con pleno control de la experiencia del usuario. El código personalizado dicta qué aspecto tendrán los mensajes, cómo se comportan y cómo interactúan con otros canales de mensajería (por ejemplo, desencadenar una tarjeta de contenido basada en una notificación push).

Cuando crees contenido personalizado completamente nuevo, como nuevos tipos de tarjetas de contenido o mensajes dentro de la aplicación con una interfaz de usuario a medida, el SDK de Braze no hará un [seguimiento automático]({{site.baseurl}}/developer_guide/analytics/) de los análisis. Debes gestionar los análisis mediante programación para que los especialistas en marketing sigan teniendo acceso a métricas como impresiones, clics y descartes en el panel Braze. Llama a los métodos de análisis del SDK de Braze para que el SDK devuelva estos datos a Braze. Cada canal de mensajería dispone de un artículo de análisis para facilitar esta tarea.

<table>
<thead>
  <tr>
    <th>Personalización</th>
    <th>Descripción</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Esfuerzo</b></td>
    <td>Depende del caso de uso.</td>
  </tr>
    <tr>
    <td><b>Trabajo de desarrollador</b></td>
    <td>Poco esfuerzo: 1-4 horas<br>Esfuerzo medio: 4-8 horas<br>Mucho esfuerzo: Más de 8 horas</td>
  </tr>
  <tr>
    <td><b>INTERFAZ DE USUARIO</b></td>
    <td>Personalizado</td>
  </tr>
  <tr>
    <td><b>Comportamiento</b></td>
    <td>Personalizado</td>
  </tr>
  <tr>
    <td><b>Seguimiento analítico</b></td>
    <td>Personalizado</td>
  </tr>
  <tr>
    <td><b>Pares clave-valor</b></td>
    <td>Obligatoria</td>
  </tr>
</tbody>
</table>
{% endtab %}
{% endtabs %}

{% alert tip %}
Cuando los desarrolladores e implementadores crean contenido personalizado para Braze, existe la oportunidad de una colaboración interfuncional con los especialistas en marketing. Por ejemplo, si desarrollas una nueva interfaz de usuario o una nueva funcionalidad para un componente concreto, prepara a tu equipo para el éxito documentando el nuevo comportamiento y cómo se integra con tu backend.
{% endalert %}