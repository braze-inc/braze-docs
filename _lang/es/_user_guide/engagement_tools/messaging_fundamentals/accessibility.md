---
nav_title: Accesibilidad
article_title: Crea mensajes accesibles en Braze
page_order: 0.5
page_type: reference
description: "Este artículo de referencia explica por qué es importante tener en cuenta la accesibilidad en tus contenidos de marketing, y cómo puedes crear mensajes accesibles en Braze."
---

# Crea mensajes accesibles en Braze

> Comprende por qué es importante tener en cuenta la accesibilidad en tu contenido de marketing y cómo puedes crear mensajes accesibles en Braze. Para obtener más información, consulta nuestro curso [Fundamentos de la mensajería accesible](https://learning.braze.com/accessible-messaging-foundations) en Braze Learning.

Los contenidos de marketing que excluyen a las personas con discapacidad, aunque sea involuntariamente, pueden impedir que millones de personas interactúen con tu marca. La accesibilidad en marketing consiste en habilitar que todo el mundo pueda experimentar tu marketing, comprender tu comunicación y tener la oportunidad de invertir en tu producto, servicio o marca, o convertirse en fan de ellos. 

Cuando diseñes tu mensajería, tómate un tiempo extra para considerar cómo puedes hacer que tus diseños sean accesibles a todos tus clientes.

{% alert important %}
Este contenido tiene como objetivo servir de orientación general y no garantiza el cumplimiento de las normas de accesibilidad, como las WCAG. Braze ofrece herramientas que facilitan la creación de mensajes más accesibles, pero es tu responsabilidad asegurarte de que el contenido final cumpla con todos los requisitos aplicables. La accesibilidad es un tema complejo con muchos aspectos variables. Muchas empresas trabajan con especialistas o consultores en accesibilidad para garantizar que su contenido, diseño y prácticas de desarrollo satisfagan las necesidades de todos los usuarios.
{% endalert %}

## Accesibilidad en Braze

Apoyar la comunicación accesible significa mantener una actitud abierta, curiosa y dispuesta a aprender. En Braze, nos preocupamos por ayudar a las personas a conectarse, y sabemos que hacer espacio para todos es parte de hacerlo bien. La accesibilidad no es algo que consideremos «terminado», y agradecemos la oportunidad de seguir aprendiendo.

{% multi_lang_include accessibility/feedback.md %}

## Áreas de discapacidad a considerar

*Esta sección está parcialmente adaptada de [W3C: Capacidades diversas y barreras](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visual %}

Las discapacidades visuales pueden ir desde la pérdida de visión leve o moderada en uno o ambos ojos hasta la pérdida sustancial o completa de visión en ambos ojos. Algunas personas tienen una sensibilidad reducida o nula a determinados colores o una sensibilidad aumentada a los colores brillantes.

Para interactuar con tu contenido, estos usuarios necesitan tener la capacidad de:

- Ampliar o reducir el tamaño del texto y las imágenes
- Personaliza la configuración de fuentes, colores y espaciado
- Escuchar la síntesis de texto a voz del contenido (es decir, utilizar un lector de pantalla)
- Escucha las descripciones de audio del video
- Leer texto utilizando Braille actualizable

{% alert note %}
- En todo el mundo, al menos 2200 millones de personas tienen una deficiencia visual de cerca o de lejos (ver [OMS](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Alrededor de 1 de cada 12 hombres y 1 de cada 200 mujeres tienen algún grado de deficiencia en la visión de los colores, lo que supone unos 300 millones de personas en el mundo (ver [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/)).
{% endalert %}

{% endtab %}
{% tab Hearing %}

Las discapacidades auditivas pueden incluir deficiencias auditivas de leves a moderadas en uno o ambos oídos. Incluso una pérdida parcial de audición puede ser problemática en relación con el contenido de audio.

Para comprender tu contenido, estos usuarios se basan en:

- Transcripciones y subtítulos de contenidos de audio
- Reproductores multimedia que muestran subtítulos y ofrecen opciones para ajustar el tamaño del texto y los colores de los subtítulos
- Opciones para detener, pausar y ajustar el volumen del contenido de audio (independientes del volumen del sistema)
- Audio de primer plano de alta calidad que se distingue claramente de cualquier ruido de fondo

{% alert note %}
- Una de cada ocho personas en Estados Unidos (13%, o 30 millones) de 12 años o más tiene pérdida de audición en ambos oídos, según las exploraciones auditivas estándar.
- Aproximadamente el 15% de los adultos estadounidenses (37,5 millones) de 18 años o más afirman tener algún problema de audición (ver [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Physical %}

Las discapacidades físicas pueden incluir debilidad y limitaciones del control muscular o de la sensibilidad, trastornos articulares, dolor que impide el movimiento y falta de miembros.

Estos usuarios confían en la ayuda del teclado para activar la funcionalidad (aunque no utilicen un teclado estándar). Para interactuar con tu contenido, estos usuarios necesitan:

- Grandes áreas clicables
- Tiempo suficiente para completar las tareas
- Indicadores visibles del enfoque actual
- Mecanismos para saltar bloques de contenido, como cabeceras de página o barras de navegación

{% alert note %}
Casi 2 millones de personas en EE. UU. viven con pérdida de extremidades (ver [Coalición de Amputados](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Cognitive %}

Las discapacidades cognitivas, de aprendizaje y neurológicas implican neurodiversidad y trastornos neurológicos, así como trastornos del comportamiento y de la salud mental que no son necesariamente neurológicos. Pueden afectar a cualquier parte del sistema nervioso y repercutir en la forma en que las personas oyen, se mueven, ven, hablan y comprenden la información.

En función de las necesidades individuales, estos usuarios se basan en:

- Contenidos claramente estructurados
- Etiquetado coherente de formularios, botones y otros contenidos
- Objetivos de enlace predecibles e interacción global
- Diferentes formas de navegar, como menús y barras de búsqueda
- Configuración para desactivar el contenido parpadeante, intermitente o que distraiga de alguna otra forma
- Texto más sencillo que se apoya en imágenes


{% alert note %}
- Una de cada cinco personas en Estados Unidos tiene problemas de aprendizaje y atención (ver [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Aproximadamente entre el 10 % y el 20 % de la población mundial se considera neurodivergente (véase [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html)).
- Aproximadamente 1 de cada 100 niños tiene autismo en todo el mundo (ver [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Buenas prácticas

Crear contenido accesible no tiene por qué ser una tarea abrumadora. Las pequeñas decisiones meditadas pueden marcar una gran diferencia. En esta sección se ofrecen consejos prácticos que ayudarán a más personas a leer, navegar e interactuar con tus mensajes correctamente. Ya sea que estés ajustando tu texto, diseñando tus botones o añadiendo texto alternativo a las imágenes, cada pequeño cambio contribuye a crear una experiencia más inclusiva. Empecemos.

### Contenido

#### Estructura y flujo

Empecemos por los cimientos. Cuando tu contenido tiene una estructura clara, es más fácil de seguir para todo el mundo, especialmente para las personas que utilizan lectores de pantalla o navegación por teclado.

- **Divide tu contenido en secciones:** El uso de encabezados, viñetas y listas ayuda a las personas a comprender y examinar rápidamente tu contenido, incluso cuando tienen prisa. 
- **No te saltes los niveles de encabezado:** Los encabezados dan estructura a tu contenido, lo que ayuda a los lectores a comprender rápidamente cómo se relacionan entre sí las secciones. Cuando omites niveles de encabezado (por ejemplo, saltando directamente de un H2 a un H4), rompes esta estructura lógica. Esto dificulta a los usuarios, especialmente a los que utilizan lectores de pantalla, navegar y comprender tu mensaje con claridad. Sigue siempre una jerarquía lógica y secuencial de encabezados (H1 a H2 a H3, y así sucesivamente) para asegurarte de que tu contenido permanezca organizado, accesible y fácil de seguir para todos.

#### Legibilidad

Una vez que tengas la estructura lista, el siguiente paso es asegurarte de que tus palabras sean realmente fáciles de leer. Esto significa mantener las cosas sencillas, fáciles de escanear y cómodas de leer en todos los dispositivos y según las necesidades de los usuarios.

- **Escribe frases cortas y claras:** Las frases cortas son fáciles de entender para todo el mundo, especialmente para las personas que utilizan lectores de pantalla o que tienen dificultades para procesar información compleja. Escribe a un nivel de lectura de séptimo grado de Estados Unidos. Puedes utilizar recursos como [la aplicación Hemingway](https://hemingwayapp.com/) para comprobar el nivel de lectura de tu texto.
- **Elige tamaños de fuente y espaciado legibles:** El texto demasiado pequeño puede resultar difícil de leer, especialmente en dispositivos móviles. Utiliza al menos 14 píxeles para el texto del cuerpo. Aumenta el tamaño de los encabezados para que los usuarios puedan ver claramente la diferencia. El espaciado adicional entre líneas (aproximadamente 1,5 veces la altura de la línea) y párrafos mejora la legibilidad, especialmente para las personas con necesidades visuales o cognitivas.
- **Evita el texto justificado:** El texto justificado crea un espaciado desigual entre las palabras, lo que dificulta la lectura a las personas con dislexia o discapacidades cognitivas. Considera la posibilidad de crear contenido que ocupe más de dos líneas alineadas a la izquierda para los idiomas de escritura de izquierda a derecha, o alineadas a la derecha para [los idiomas de escritura de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages).
- **Utiliza el texto en negrita, cursiva y mayúsculas con moderación:** Poner demasiado énfasis en el texto dificulta la lectura, especialmente para las personas con dislexia o discapacidad visual. Hazlo sencillo.

#### Claridad y facilidad de uso

Por último, hablemos de los detalles más sutiles, aquellos que ayudan a los usuarios no solo a ver tu contenido, sino también a comprenderlo e interactuar con él. 

- **Etiqueta claramente los enlaces y botones:** Asegúrate de que el texto del [enlace](#links) y [del botón](#buttons) explique claramente lo que sucederá a continuación. Ayuda a las personas que utilizan lectores de pantalla o navegan con el teclado a saber qué pueden esperar.
- **No abuses de los símbolos y los emojis:** Los caracteres especiales y los emojis pueden hacer que tu contenido sea más divertido, pero pueden resultar confusos cuando los leen los lectores de pantalla. Úsalos con moderación y asegúrate de que no sustituyan a un texto claro y descriptivo.
- **Prueba de truncamiento:** Comprueba siempre tu texto [enviando un mensaje de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) a un dispositivo para asegurarte de que no se trunca. Si tu mensaje se ve truncado, esto perjudica tanto a ti como a tu audiencia, ya que impide que tu contenido llegue a ella.

### Botones de acción

Utiliza **botones** para indicar una acción, como enviar un formulario o reproducir un carrusel. Si vas a navegar a una nueva URL, considera la posibilidad de utilizar un [enlace](#links) en su lugar.

#### Escribe textos claros y orientados a la acción.

Al igual que el texto de los enlaces, las etiquetas de los botones deben describir claramente la acción. El texto eficaz de un botón es específico y orientado a la acción. Por ejemplo, «Enviar pedido» indica claramente a los usuarios lo que sucederá cuando realicen un clic, mientras que simplemente «Enviar» puede resultar ambiguo. Cada etiqueta debe describir con precisión la acción prevista, de modo que los lectores de pantalla y todos los usuarios puedan comprender y realizar una predicción del resultado al interactuar con tus botones.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Texto del botón correcto <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Texto del botón incorrecto <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>«Enviar pedido»</td>
      <td>«Enviar»</td>
    </tr>
    <tr>
      <td>Crear cuenta</td>
      <td>«Registrarse»</td>
    </tr>
    <tr>
      <td>Descarga nuestro folleto</td>
      <td>«Descargar»</td>
    </tr>
    <tr>
      <td>Ver detalles del producto</td>
      <td>Más información</td>
    </tr>
    <tr>
      <td>Suscríbete para recibir actualizaciones</td>
      <td>Suscríbete</td>
    </tr>
  </tbody>
</table>

Mantén el texto del botón conciso para evitar que se trunque. Si el texto de un botón es demasiado largo, puede cortarse con puntos suspensivos en lugar de ajustarse.

#### Utiliza un contraste de colores suficiente.

El texto del botón debe ser fácil de leer sobre el color de fondo del botón. Comprueba que el texto de tus botones cumple con [los requisitos mínimos de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) de WCAG 2.2 AA:

- Relación de contraste de 4,5:1 para texto de tamaño normal (la mayoría de los botones).
- Relación de contraste de 3:1 para texto grande (normalmente superior a 18 pt).

El alto contraste ayuda a que los botones sigan siendo legibles y se puedan pulsar para todo el mundo, incluidos los usuarios con discapacidad visual o aquellos que ven tu mensaje en entornos difíciles. Para obtener más información, consulta la sección [Contraste de color](#color-contrast).

#### Haz que los botones sean fáciles de pulsar.

Asegúrate de que los botones (y enlaces) sean lo suficientemente grandes y estén lo suficientemente separados para los usuarios de dispositivos móviles. [Los objetivos táctiles](#touch-targets) pequeños o apiñados pueden resultar frustrantes o imposibles de interactuar para los usuarios con discapacidades motoras.  

### Enlaces

Utiliza enlaces para la navegación, como dirigir a los usuarios a una página externa.

#### Escribe un texto descriptivo para el enlace.

Escribe un texto de enlace que describa claramente adónde llevará el enlace al usuario. Los usuarios de lectores de pantalla suelen pasar de un enlace a otro para hojear el contenido, así que asegúrate de que el texto de tu enlace se sostiene por sí solo. Evita frases como "haz clic aquí", "más" y "haz clic para más detalles", ya que son ambiguas cuando se leen fuera de contexto.

Por ejemplo, piensa en cómo podrías escribir un enlace para ver un parte meteorológico.

| Mal  | Mejor | Mejor |
| --- | --- | --- | 
| Haz clic aquí | Haz clic aquí para acceder al tiempo de hoy | El tiempo hoy |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como con todo el contenido, que sea sencillo y con el menor número posible de palabras adicionales.

#### Evita diseñar enlaces como botones.

Los editores de arrastrar y soltar de Braze generan HTML semántico de forma predeterminada, por lo que los enlaces no tienen el mismo estilo que los botones. Sin embargo, si trabajas con [HTML personalizado](#custom-html) o realizas cambios a nivel de código, ten en cuenta lo siguiente:

- **Los enlaces (`<a>`)** responden a la tecla <kbd>Intro</kbd>.
- **Los botones (`<button>`)** responden tanto a la tecla <kbd>Intro</kbd> como a la tecla <kbd>Espacio</kbd>.

Diseñar un enlace para que parezca un botón puede confundir a las personas que navegan con el teclado, ya que pueden intentar pulsar <kbd>la barra espaciadora</kbd> y esperar que funcione.

Utiliza el elemento adecuado para la acción:

- Úsalo`<button>`para acciones como enviar un formulario o abrir una ventana modal.
- Úsalo`<a>`para la navegación, como por ejemplo para enlazar con otra página o archivo.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Objetivos táctiles

Los objetivos táctiles son cualquier parte de tu mensaje en la que los usuarios pulsan para realizar una acción, como botones, enlaces o iconos. Estos elementos deben ser lo suficientemente grandes y estar lo suficientemente separados entre sí para que las personas puedan pulsarlos fácilmente, especialmente en dispositivos móviles.

Cuando los objetivos táctiles son demasiado pequeños o están demasiado juntos, puede resultar frustrante o imposible para los usuarios con problemas de movilidad o destreza interactuar con tu mensaje. Mejorar esto puede ayudar a reducir los errores y crear una experiencia más fluida para todos.

Esto es lo que debes tener en cuenta:
- **Utiliza un tamaño adecuado para los objetivos táctiles.** Intenta que el tamaño mínimo del objetivo táctil sea de 44 x 44 píxeles. Esto se ajusta a las directrices WCAG 2.2 para [objetivos táctiles](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) y a los estándares comunes de usabilidad móvil.
- **Dale a cada objetivo un respiro.** Si los objetivos táctiles están demasiado juntos, como enlaces apilados o botones muy agrupados, es fácil equivocarse o pulsar el botón equivocado. Añade espacio o relleno entre los elementos para evitarlo.
- **No te bases solo en lo visual.** Incluso los iconos pequeños pueden hacerse más fáciles de usar con un relleno adicional, lo que les permite cumplir los requisitos mínimos de tamaño sin alterar el diseño.
- **Vista previa en el móvil.** Prueba tu mensaje en diferentes tamaños de pantalla y asegúrate de que los elementos interactivos sean fáciles de usar.

Mejorar los objetivos táctiles es una de las formas más eficaces de hacer que tu mensaje sea más accesible en los dispositivos móviles, y es una buena experiencia de usuario para todos.

### Imágenes

#### Proporcionar texto alternativo

El texto alternativo (texto alt) es una breve descripción del contenido o la función de una imagen que los lectores de pantalla y otras tecnologías de asistencia proporcionan a los usuarios. Para cada imagen significativa, escribe un texto alternativo descriptivo para que los usuarios que no puedan ver las imágenes sigan entendiendo tu mensaje o llamada a la acción. 

#### Evita las imágenes de texto.

Siempre que sea posible, evita colocar texto dentro de imágenes, ya que los lectores de pantalla no pueden leer el texto basado en imágenes y los usuarios no pueden ajustar fácilmente el tamaño o el color de la fuente para mejorar la visibilidad. Ten en cuenta estos consejos:

- **Elimina el texto donde puedas:** Mueve cualquier texto descriptivo o promocional de la imagen a un campo de texto de tu mensaje. De esta manera, los usuarios pueden cambiar el tamaño o el color según sea necesario utilizando las preferencias de su dispositivo o navegador.
- **Prueba de legibilidad y contraste:** Si debes mantener el texto en la imagen, sigue las prácticas recomendadas en materia de [contraste de colores](#color-contrast) y utiliza una [fuente de gran tamaño](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Esto significa que el texto debe tener un tamaño mínimo de 18 puntos (unos 24 píxeles) si no está en negrita, o de 14 puntos (unos 18 píxeles) si está en negrita. El uso de estos tamaños ayuda a que el texto siga siendo legible sin obligar a los usuarios a ampliar la imagen, y mejora el contraste general y la legibilidad del contenido. Comprueba que sigue siendo legible en pantallas más pequeñas.
- **Proporcionar texto alternativo:** Para el texto esencial que debe permanecer en la imagen, incluye texto alternativo que describa las palabras.

Cuando las imágenes contienen texto que no se puede editar, los usuarios con discapacidad visual pierden la flexibilidad para realizar ajustes de lectura. Al separar el texto de las imágenes, ayudas a más usuarios a leer e interactuar con tu mensaje cómodamente.

#### Consejos para escribir texto alternativo

- [Describe lo que realmente aparece en la imagen.](#tip-1)
- [Sé breve, pero específico.](#tip-2)
- [Evita expresiones como «imagen de» o «foto de».](#tip-3) 
- [Refleja el texto que aparece en la imagen.](#tip-4)
- [Cíñete al contexto relevante, sin jerga de marketing adicional.](#tip-5)
- [Ten en cuenta el propósito de la imagen.](#tip-6)

##### Describe lo que realmente aparece en la imagen. {#tip-1}

Los usuarios de lectores de pantalla dependen del texto alternativo para comprender el contenido o la función de una imagen. Evita el lenguaje genérico de marketing que no se corresponde con lo que se muestra visualmente.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Ejemplos incorrectos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mujer sonriente con una chaqueta vaquera azul, sosteniendo una bolsa de la compra.</td>
      <td>«¡Es hora de darse un capricho!» (Sin mencionar lo que realmente aparece en la imagen)</td>
    </tr>
    <tr>
      <td>Hombre con camiseta negra, apoyado en una bicicleta en una calle de la ciudad.</td>
      <td>¡Disfruta ahora de tu mejor vida! (Ignora la bicicleta y la configuración de la ciudad).</td>
    </tr>
    <tr>
      <td>Edificio de apartamentos azul con un cartel de «Se alquila» en la fachada.</td>
      <td>«¡La clave para un mañana mejor!» (No refleja el apartamento ni el letrero).</td>
    </tr>
  </tbody>
</table>

##### Sé breve, pero específico. {#tip-2}

Un texto alternativo conciso facilita su procesamiento por parte de los usuarios. Incluye suficientes detalles para transmitir el propósito, pero omite cualquier información superflua. Como regla general, el texto alternativo no debe superar los 125 caracteres. Si necesitas algo más que una frase o una oración breve, considera la posibilidad de utilizar uno de los [métodos de descripción larga](https://www.w3.org/WAI/tutorials/images/complex/) del W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Ejemplos incorrectos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>«Zapatillas deportivas rojas sobre fondo blanco».</td>
      <td>«Zapatillas deportivas extremadamente cómodas y perfectas para tu estilo de vida activo, en un vibrante tono rojo». (Demasiado largo y lleno de palabrería promocional).</td>
    </tr>
    <tr>
      <td>Cuatro ordenadores portátiles en un expositor.</td>
      <td>«Descubre el potenciador de productividad definitivo que redefine tu forma de trabajar cada día, en todos los aspectos imaginables». (No describe lo que realmente se muestra).</td>
    </tr>
    <tr>
      <td>«Grupo de amigos comiendo helado en un día soleado».</td>
      <td>«Captura la felicidad pura con el dulce más delicioso: ¡la vida es mejor con nuestra marca de helados!» (Demasiado abstracto y centrado en la marca).</td>
    </tr>
  </tbody>
</table>

##### Evita expresiones como «imagen de» o «foto de». {#tip-3}

Los lectores de pantalla ya anuncian una imagen. Empieza directamente a describir el tema.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Ejemplos incorrectos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mesa preparada para el brunch con tortitas, fruta y café.</td>
      <td>Imagen de una mesa preparada para el brunch.</td>
    </tr>
    <tr>
      <td>Cartel publicitario en la carretera con el texto «Gran inauguración» en letras grandes.</td>
      <td>Foto de una valla publicitaria al lado de una carretera.</td>
    </tr>
    <tr>
      <td>«Paisaje montañoso nevado al atardecer»</td>
      <td>Foto de nieve y montañas</td>
    </tr>
  </tbody>
</table>

##### Refleja el texto que aparece en la imagen. {#tip-4}

Si una imagen incluye texto esencial, pon esa información en el texto alternativo para que los usuarios no se la pierdan.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Ejemplos incorrectos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cartel con el siguiente texto: «Rebajas de verano: 50 % de descuento en todos los bañadores».</td>
      <td>«Cartel promocional de rebajas» (no menciona el descuento real).</td>
    </tr>
    <tr>
      <td>Logotipo con el texto «Café Toscana» en fuente script.</td>
      <td>Imagen del logotipo para una cafetería. (No incluye el texto «Café Toscana»).</td>
    </tr>
    <tr>
      <td>Anuncio publicitario «Entradas para conciertos ya a la venta: a partir del 5 de junio».</td>
      <td>«Anuncio de concierto». (Sin detalles del evento).</td>
    </tr>
  </tbody>
</table>

##### Cíñete al contexto relevante, sin jerga de marketing adicional. {#tip-5}

No rellenes el texto alternativo con términos SEO o llamadas a la acción que no estén directamente relacionados con la imagen. Aporta valor a quienes no pueden ver la imagen.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Ejemplos incorrectos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ordenador portátil mostrando el gráfico de análisis del panel de Braze.</td>
      <td>«¡Aumenta las conversiones y dispara el ROI con la mejor plataforma del mundo!» (Añade lenguaje de marketing innecesario).</td>
    </tr>
    <tr>
      <td>Característica del conjunto de muebles de jardín: cuatro sillas y una mesa de cristal.</td>
      <td>«¡Organiza ahora una increíble fiesta de verano para todos tus amigos y familiares!» (Describe una situación, no la imagen).</td>
    </tr>
    <tr>
      <td>Teléfono móvil mostrando una aplicación de previsión meteorológica con una temperatura de 24 °C en pantalla.</td>
      <td>«Experimenta innovaciones en tiempo real en el seguimiento meteorológico que suponen un gran cambio» (No refleja lo que se muestra visiblemente).</td>
    </tr>
  </tbody>
</table>

##### Ten en cuenta el propósito de la imagen. {#tip-6}

Si una imagen funciona como un enlace o una llamada a la acción, describe la acción prevista («Comprar», «Enlace a», «Registrarse»), no solo la etiqueta o el producto que se muestra.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Ejemplos incorrectos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>«Compra la colección de otoño»</td>
      <td>«Colección otoño» (Acción prevista omitida)</td>
    </tr>
    <tr>
      <td>Enlace al eBook gratuito</td>
      <td>«eBook gratuito» (no queda claro que se trata de un enlace)</td>
    </tr>
    <tr>
      <td>Regístrate en la lista de correo.</td>
      <td>«Lista de correo» (no describe lo que el usuario puede hacer)</td>
    </tr>
  </tbody>
</table>

Si la imagen no tiene ningún propósito, hazlo saber también. Las imágenes decorativas, como los logotipos, deben tener una etiqueta alt vacía (`alt=""`) para que los lectores de pantalla sepan que deben omitir su anuncio. Sin él, normalmente se lee el nombre del archivo de imagen.

### Vídeos

Los videos generan interacción, pero si no son accesibles, corres el riesgo de excluir a parte de tu audiencia. Sigue estos consejos para que tu contenido de video sea más inclusivo:

- [Proporcionar subtítulos ocultos](#closed-captions)
- [Proporcionar controles de reproducción](#playback-controls)
- [Evita la reproducción automática](#no-auto-play)
- [Evita el contenido intermitente o estroboscópico.](#no-seizures)

#### Proporcionar subtítulos ocultos {#closed-captions}

Incluye subtítulos en tus videos para que los usuarios puedan seguir el diálogo, los efectos de sonido y otros contenidos de audio. Ayuda con los subtítulos:

- Personas sordas o con dificultades auditivas
- Ustedes que ven el programa en un entorno sin sonido
- Los hablantes no nativos que prefieren leer al mismo tiempo

Los subtítulos ocultos se pueden alternar, lo que permite a los usuarios elegir la opción que más les convenga.

{% multi_lang_include accessibility/video.md %}

#### Proporcionar controles de reproducción {#playback-controls}

Asegúrate de que tu video incrustado incluya controles de reproducción accesibles, como reproducir, pausar, silenciar y buscar, para que los usuarios puedan interactuar con él de la forma que mejor les convenga.

#### Evita la reproducción automática {#no-auto-play}

Siempre que sea posible, evita la configuración de los videos para que se reproduzcan automáticamente. La reproducción automática puede resultar molesta o desorientadora para:

- Usuarios que utilizan lectores de pantalla o navegación por teclado
- Personas con sensibilidad al movimiento
- Cualquier persona que se encuentre en un entorno tranquilo (como un lugar de trabajo o una configuración nocturna).

Permite a los usuarios elegir cuándo reproducir un video incluyendo controles claros.

#### Evita el contenido intermitente o estroboscópico. {#no-seizures}

No incluyas videos con efectos intermitentes o estroboscópicos, especialmente a alta frecuencia. Esto puede desencadenar convulsiones en usuarios con epilepsia fotosensible y causar molestias a otras personas.

### Contraste de color

Un contraste de color suficiente ayuda a garantizar que tus mensajes sean fáciles de leer para todo el mundo, incluidas las personas con baja visión o aquellas que ven tu contenido en condiciones de mucha luz o difíciles. Busca ratios de contraste que cumplan con [los requisitos del nivel AA de las WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Relación de contraste de 4,5:1 para texto normal (por ejemplo, texto del cuerpo, botones y enlaces).
- Relación de contraste de 3:1 para texto grande (como títulos y etiquetas grandes).

Puedes probar tus elecciones de color utilizando la herramienta [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/).

{% multi_lang_include accessibility/color.md %}

### HTML personalizado

Si utilizas algún HTML personalizado en tu mensajería:

- Utiliza [HTML semántico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Esto significa utilizar los elementos HTML correctos para su propósito, en lugar de estilizar un elemento para que parezca otro. La mayoría de los elementos HTML tienen incorporado su propio soporte de accesibilidad.
- Establece el[`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)[atributo](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) en tu HTML como identificador del idioma en el que está tu contenido. Los lectores de pantalla utilizan diferentes bibliotecas de sonidos para cada idioma, según la pronunciación y las características de ese idioma. Si no se especifica, el lector de pantalla asume que el contenido está escrito en el idioma predeterminado que el usuario ha elegido al configurar el lector de pantalla. Si el mensaje no está realmente en el idioma predeterminado, es posible que el lector de pantalla no pronuncie el mensaje correctamente. 

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Cuando usas el editor de arrastrar y soltar del correo electrónico, el valor del idioma del correo electrónico se puede configurar yendo a la pestaña **de configuración** y seleccionando el valor del idioma adecuado.
{% endalert %}

- Utiliza [los atributos ARIA](#aria-attributes) para proporcionar contexto adicional. Estos atributos proporcionan información adicional a las tecnologías de asistencia, ayudando a aclarar la función, el estado o las propiedades de los elementos de la interfaz de usuario que, de otro modo, podrían resultar confusos. 

### Atributos ARIA

Cuando utilices código personalizado en los editores de Braze, puedes usar las aplicaciones de Internet enriquecidas accesibles ([ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) para proporcionar asistencia adicional en materia de accesibilidad a los usuarios que dependen de tecnologías de asistencia. Las funciones y los atributos ARIA ayudan a los lectores de pantalla a interpretar tu contenido con mayor claridad, especialmente cuando utilizas elementos que no transmiten significado por sí mismos (como`<div>`  o `<span>`).

{% alert important %}
Aunque ARIA está diseñado para hacer que el contenido de la Web sea más accesible, si se usa incorrectamente, puede hacer más daño que bien. ARIA no sustituye al HTML semántico, sino que lo complementa, por lo que solo debes utilizar ARIA cuando los elementos HTML nativos no satisfagan tus necesidades.
{% endalert %}

Aquí hay algunos ejemplos que son especialmente útiles en contextos de mensajería:

- [etiqueta aria](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentación"](#rolepresentation)
- [aria-live="en vivo"](#aria-livepolite)

#### etiqueta aria

`aria-label` Añade un nombre accesible a los elementos que no tienen texto visible. Si utilizas un icono sin texto (como una papelera o una «X» para cerrar), alguien que utilice un lector de pantalla no sabrá para qué sirve, a menos que lo etiquetes.`aria-label`  le da voz a ese icono.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby

`aria-labelledby` conecta un elemento a algo que ya tiene una etiqueta visible. Así que si tienes un banner o una región que debe leerse en voz alta con un título, puedes utilizar`aria-labelledby`  para indicar a la tecnología de asistencia: «Oye, utiliza ese encabezado de ahí para nombrar esta parte».

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true"

`aria-hidden="true"` oculta información a los lectores de pantalla.  Es útil para textos o elementos visuales que no transmiten un significado importante, como un brillo, una marca de verificación o un emoji utilizado únicamente por motivos estéticos.

Esto mantiene la experiencia más limpia para los usuarios de lectores de pantalla, que de otro modo podrían escuchar contenido redundante o confuso. También es útil para ocultar elementos como el contenido de un acordeón fuera de pantalla que aún no se ha expandido.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

En general, es mejor utilizar`alt=""`  para [imágenes decorativas](#images) e iconos en lugar de `aria-hidden="true"`. Aunque el HTML semántico es ampliamente compatible con todos los lectores de pantalla y programas de asistencia, la compatibilidad con ARIA varía. Incluso si utilizas ,`aria-hidden` debes incluir un atributo alt vacío.

#### role="presentación"

`role="presentation"` Indica a la tecnología de asistencia que ignore los elementos que solo afectan al diseño, como las tablas de diseño. Por ejemplo, en los correos electrónicos se suelen utilizar tablas solo para alinear los elementos. Sin esta función, los lectores de pantalla podrían asumir que tu diseño es una tabla de datos y comenzar a leer los números de filas y columnas.  

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

Los correos electrónicos creados en el editor de arrastrar y soltar tienen elementos de presentación marcados automáticamente con el atributo `role="presentation"`ARIA.

#### aria-live="en vivo"

`aria-live="polite"` Anuncia las actualizaciones cuando cambia el contenido sin necesidad de interacción por parte del usuario. Úsalo cuando muestres actualizaciones dinámicas dentro de un mensaje, como éxitos, errores u otras notificaciones.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Pruebas de accesibilidad automatizadas

Para ayudarte a identificar y solucionar problemas de accesibilidad de forma temprana, Braze ofrece pruebas de accesibilidad automatizadas en las siguientes áreas:

- [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) para correos electrónicos
- [Escáner]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=in-app%20message#accessibility-scanner) [de accesibilidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=in-app%20message#accessibility-scanner) para mensajes creados con nuestro editor HTML (por ejemplo, mensajes HTML dentro de la aplicación, bloques de contenido HTML, [pies de página de correo electrónico personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer), [páginas de adhesión voluntaria a correos electrónicos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-opt-in-page) y [páginas para cancelar la suscripción a correos electrónicos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-unsubscribe-page)).

Estas pruebas comprueban tu mensaje según el estándar de las Pautas de Accesibilidad al Contenido en la Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un conjunto de normas técnicas reconocidas internacionalmente para el contenido accesible. Cualquier problema que se pueda detectar automáticamente se marca y se clasifica según su gravedad para ayudarte a establecer prioridades.

{% alert note %}
Inbox Vision funciona tanto con correos electrónicos HTML como con correos electrónicos de arrastrar y soltar. El escáner solo funciona con contenido creado con el editor HTML.
{% endalert %}

### Lo que las pruebas de automatización pueden y no pueden detectar

Las pruebas de accesibilidad automatizadas son un excelente punto de partida, pero no pueden detectar todo. Algunas cuestiones requieren un toque humano para evaluarlas adecuadamente, especialmente cuando el contexto o el diseño visual influyen en la forma en que los usuarios perciben tu correo electrónico.

Es posible que veas algunos problemas marcados como **«Necesita revisión**». Estos son casos en los que el verificador no puede determinar con certeza si algo supone un problema para la accesibilidad. Cuando eso ocurra, recomendamos revisarlo manualmente.

Algunos ejemplos de lo que las herramientas de automatización no pueden detectar de forma fiable son:

- Si el orden de enfoque de los elementos interactivos sigue una secuencia lógica
- Si el contenido es totalmente operativo con un teclado, sin necesidad de ratón.
- Si el texto alternativo describe de forma significativa una imagen
- Si los encabezados se utilizan correctamente para organizar el contenido
- Si los enlaces y botones están claramente etiquetados y son fáciles de entender.
- Si los objetivos táctiles son lo suficientemente grandes y están espaciados adecuadamente
- Si el texto de las imágenes de fondo cumple los requisitos de contraste de color.
- Si las instrucciones o etiquetas son claras y útiles para todos los usuarios.

Estas limitaciones no son únicas de Braze, sino que son comunes a todas las herramientas de accesibilidad automatizadas. Las comprobaciones automatizadas no pueden imitar todas las tecnologías de asistencia, lectores de pantalla o necesidades de los usuarios. Por eso la accesibilidad no es una comprobación puntual, sino una práctica continua.

Aunque tu mensaje supere todos los controles de automatización, sigue siendo importante:

- Revisa cuidadosamente los problemas señalados, especialmente los etiquetados como **«Necesita revisión**».
- Realiza pruebas manuales siempre que sea posible, especialmente en lo que respecta al diseño y los patrones de interacción.
- Utiliza herramientas como lectores de pantalla, navegación solo con teclado y zoom del navegador para simular diferentes necesidades de acceso.

Al combinar las pruebas de automatización con una revisión manual minuciosa, detectarás más problemas potenciales y crearás campañas más inclusivas y útiles para todos los destinatarios.
