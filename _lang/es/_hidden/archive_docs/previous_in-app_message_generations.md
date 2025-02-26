---
nav_title: Generaciones anteriores
article_title: Anterior Generación de mensajes dentro de la aplicación
page_order: 20
page_type: reference
description: "Este artículo revisa la información anterior sobre los mensajes dentro de la aplicación en Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Generaciones anteriores de mensajes dentro de la aplicación

{% alert important %}
Esta página revisa la información anterior sobre nuestros mensajes dentro de la aplicación. Para ver la información más actualizada sobre nuestra generación actual de mensajes dentro de la aplicación, consulta nuestra documentación actual sobre [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).
{% endalert %}

## Universal

Esto revisará la información anterior sobre nuestros mensajes dentro de la aplicación. Para ver la información más actualizada sobre nuestra generación actual de mensajes dentro de la aplicación, consulta nuestra [documentación de resumen de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).

{% details Pantalla completa %}
Son las más atractivas, pero también las más intrusivas, ya que cubren toda la pantalla de tu usuario. Son geniales para mostrar imágenes grandes y enriquecidas, y pueden ser útiles para transmitir información muy importante, como nuevas características cruciales y promociones que caducan. Como interrumpen más la experiencia del usuario, utilízalos con moderación para los contenidos de máxima prioridad.

![Mensaje a pantalla completa]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Características personalizables**

- Cabecera y cuerpo del texto
- Una imagen grande
- Hasta dos botones de llamada a la acción con comportamiento separado al hacer clic y vínculos en profundidad
- Diferentes colores para el encabezado y el cuerpo del texto, los botones y el fondo
- Pares clave-valor

{% enddetails %}
{% details  Modal %}
Estos mensajes no son tan intrusivos como los mensajes a pantalla completa, ya que permiten a los usuarios ver parte de la interfaz de usuario de tu aplicación. Dado que siguen conteniendo botones e imágenes, los mensajes modales pueden ser una mejor opción que los deslizamientos hacia arriba si deseas una campaña más interactiva y visual. Son ideales para contenidos de prioridad media, como actualizaciones de aplicaciones y ofertas y eventos no urgentes.

![Mensaje modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Características personalizables**

- Cabecera y cuerpo del texto
- Una imagen o un icono de señal personalizable
- Hasta dos botones de llamada a la acción con comportamiento separado al hacer clic y vínculos en profundidad
- Diferentes colores para el encabezado y el cuerpo del texto, los botones y el fondo
- Pares clave-valor

{% enddetails %}

{% details Deslizamiento hacia arriba tradicional %}
Son el tipo de mensaje menos intrusivo, aunque pueden llamar más o menos la atención según el uso que hagas de los colores y los iconos de las señales. Este puede ser el formato de mensaje a utilizar cuando se incorporan nuevos usuarios y se les dirige hacia características concretas de la aplicación, ya que no detienen la experiencia de la aplicación y permiten una exploración continua.

![Mensaje de deslizamiento hacia arriba]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Características personalizables**

- Cuerpo del texto
- Una imagen o un icono de señal personalizable
- Diferentes colores para el fondo del deslizamiento hacia arriba, el texto y el icono
- Comportamiento de cierre de mensajes
- Posición de deslizamiento hacia arriba (parte superior o inferior de la pantalla de la aplicación)
- Pares clave-valor

{% enddetails %}

<br>

## Web

Esto revisará la información anterior sobre mensajes dentro de la aplicación más personalizados. Para ver la información más actualizada sobre nuestra generación actual de mensajes dentro de la aplicación, consulta nuestra [documentación de personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% details Captura de mensaje por correo electrónico %}
Los mensajes de captura de correo electrónico te permiten pedir fácilmente a los usuarios de tu sitio que envíen su dirección de correo electrónico, tras lo cual estará disponible en el sistema Braze para utilizarla en todas tus campañas de mensajería.

![Captura de mensaje por correo electrónico]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Para habilitar la captura de mensajes por correo electrónico dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad: los mensajes dentro de la aplicación en HTML pueden ejecutar JavaScript, por lo que necesitamos que un mantenedor del sitio los habilite.

**Características personalizables**

- Cabecera, cuerpo y texto del botón de envío
- Una imagen opcional
- Un enlace opcional a las "Condiciones del servicio".
- Diferentes colores para el encabezado y el cuerpo del texto, los botones y el fondo
- Pares clave-valor

{% enddetails %}

{% details Mensaje HTML personalizado %}

Aunque los mensajes dentro de la aplicación de Braze se pueden personalizar de muchas maneras, puedes obtener un control aún mayor sobre el aspecto y la sensación de tus campañas utilizando mensajes diseñados y creados con HTML, CSS y JavaScript. Con una simple composición, puedes desbloquear funcionalidades y marcas personalizadas que se ajusten a cualquiera de tus necesidades. Los mensajes dentro de la aplicación en HTML permiten un mayor control sobre el aspecto de un mensaje, y todo lo que es compatible con HTML5 también lo es con Braze.

**Puente JavaScript (appboyBridge)**

Los mensajes HTML dentro de la aplicación admiten una interfaz "puente" de JavaScript con el SDK Web de Braze, lo que te permite desencadenar acciones Braze personalizadas cuando los usuarios hacen clic en elementos con enlaces o interactúan de otro modo con tu contenido. Los siguientes métodos de JavaScript son compatibles con los mensajes HTML dentro de la aplicación de Braze:

{% multi_lang_include archive/appboyBridge.md platform="web" %}

Además, para el seguimiento de los análisis, cualquier elemento `<a>` o `<button>` de tu HTML registrará automáticamente una acción de "clic" en la campaña asociada al mensaje dentro de la aplicación. Para registrar un "clic de botón" en lugar de un "clic de cuerpo", proporciona un valor de cadena de consulta de abButtonId en el href de tu enlace (por ejemplo, `<a href="http://mysite.com?abButtonId=0">click me</a>`), o proporciona un ID en el elemento HTML (por ejemplo, `<a id="0" href="http://mysite.com">click me</a>`). Ten en cuenta que los únicos ID de botón aceptados actualmente son "0" y "1". Un enlace con un ID de botón 0 se representará como "Botón 1" en el panel, mientras que un enlace con un ID de botón 1 se representará como "Botón 2".

>  Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad: los mensajes dentro de la aplicación en HTML pueden ejecutar JavaScript, por lo que necesitamos que un mantenedor del sitio los habilite.

{% enddetails %}

{% details Plantillas HTML de mensajes dentro de la aplicación %}

Hemos diseñado un conjunto de plantillas HTML5 de mensajes dentro de la aplicación para ayudarte a empezar. Consulta nuestro [repositorio de GitHub](https://github.com/braze-inc/in-app-message-templates), que contiene instrucciones detalladas sobre cómo utilizar y personalizar estas plantillas según tus necesidades.

**Características personalizables**

- Fuentes
- Estilos
- Imágenes + videos
- Comportamientos al hacer clic
- Componentes interactivos

{% enddetails %}

<br>

## Especificaciones

Esto revisará la información anterior sobre nuestras especificaciones creativas de mensajes dentro de la aplicación. Para ver la información más actualizada sobre nuestra generación actual de mensajes dentro de la aplicación, consulta nuestra [documentación de especificaciones creativas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Límites de carácter e imagen

Para todos los tipos de mensajes dentro de la aplicación enumerados en la siguiente tabla, se aplican las siguientes directrices adicionales:

- **Tamaño de imagen recomendado:** 500 KB 
- **Tamaño máximo de imagen:** 5 MB
- **Tipos de archivo admitidos:** PNG, JPEG, GIF

| Tipo                               | Relación de aspecto | Número máximo de caracteres |
| :--------------------------------- | :----------: | :-----------------: |
| Retrato a pantalla completa (sólo imagen)  |    10:16     |         240         |
| Retrato a pantalla completa (con texto)   |     5:4      |         240         |
| Paisaje Pantalla completa (Con texto)  |     16:5     |         240         |
| Paisaje Pantalla completa (sólo imagen) |    16:10     |         240         |
| deslizamiento hacia arriba                            |     1:1      |         140         |
| Modal (Sólo imagen)                 |     1:1      |         140         |
| Modal (con texto)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Reducir el tamaño de los archivos de mensajes dentro de la aplicación

Braze recomienda que mantengas el tamaño de tus imágenes y activos HTML lo más bajo posible por varias razones:

- Las cargas útiles de mensajes HTML e imágenes más pequeñas se descargarán más rápido y se mostrarán de forma más rápida y fiable para tus clientes.
- Las cargas útiles de mensajes HTML y de imágenes más pequeñas también mantendrán bajos los costes de datos de tus clientes. Los mensajes dentro de la aplicación Braze se descargan en segundo plano al iniciar la sesión, por lo que pueden desencadenarse en tiempo real en función de los criterios que selecciones. Como resultado, si tienes 10 mensajes HTML dentro de la aplicación de 1 MB cada uno, todos tus clientes incurrirían en un gasto de datos de 10 MB, aunque nunca hayan desencadenado todos esos mensajes. Esto puede acumularse rápidamente con el tiempo, a pesar de que los mensajes dentro de la aplicación se almacenan en caché y no se vuelven a descargar de sesión en sesión.

Las siguientes estrategias son útiles para mantener bajo el tamaño de los archivos:

- Haz referencia a fuentes incrustadas en tu aplicación o sitio web para personalizar tus mensajes HTML dentro de la aplicación, en lugar de incluir los archivos de fuentes en tu carpeta ZIP de activos HTML.
- Asegúrate de no incluir CSS o JavaScript superfluos o duplicados en tus ZIP de activos HTML.
- Utiliza [ImageOptim][25] en todas las imágenes para comprimirlas al mínimo tamaño posible sin reducir su calidad.

### Especificaciones del iPhone 5

![Especificaciones del iPhone 5][18]

### Especificaciones del iPhone 6

![Especificaciones del iPhone 6][19]


[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}

[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
