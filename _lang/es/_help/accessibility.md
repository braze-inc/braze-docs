---
nav_title: Construir mensajes accesibles
article_title: Construir mensajes accesibles en Braze
page_order: 3.5
page_type: reference
description: "Este artículo de referencia explica por qué es importante tener en cuenta la accesibilidad en tus contenidos de marketing, y cómo puedes crear mensajes accesibles en Braze."
---

# Construir mensajes accesibles en Braze

> Comprende por qué es importante tener en cuenta la accesibilidad en tus contenidos de marketing, y cómo puedes crear mensajes accesibles en Braze. Para más orientación, consulta nuestro curso [Fundamentos de la mensajería accesible](https://learning.braze.com/accessible-messaging-foundations) en Braze Learning.

Los contenidos de marketing que excluyen a las personas con discapacidad, aunque sea involuntariamente, pueden impedir que millones de personas interactúen con tu marca. La accesibilidad en marketing consiste en facilitar que todo el mundo experimente tu marketing, reciba y comprenda tu comunicación, y tenga la oportunidad de invertir en tu producto, servicio o marca, o de convertirse en fan de ellos. 

Cuando diseñes tu mensajería, tómate un tiempo extra para considerar cómo puedes hacer que tus diseños sean accesibles a todos tus clientes.

{% alert important %}
Este contenido pretende servir de orientación general y no garantiza el cumplimiento de normas de accesibilidad como las WCAG. Braze ofrece herramientas que ayudan a crear mensajes más accesibles, pero es tu responsabilidad asegurarte de que el contenido final cumple los requisitos aplicables. La accesibilidad es un tema complejo con muchas partes móviles. Muchas empresas trabajan con especialistas o consultores en accesibilidad para asegurarse de que sus prácticas de contenido, diseño y desarrollo satisfacen las necesidades de todos los usuarios.
{% endalert %}

## Accesibilidad en Braze

Apoyar la comunicación accesible significa permanecer abierto, curioso y dispuesto a aprender. En Braze, nos preocupamos por ayudar a las personas a conectarse, y sabemos que hacer sitio a todo el mundo forma parte de hacerlo bien. La accesibilidad no es algo que consideremos "hecho", y agradecemos la oportunidad de seguir aprendiendo.

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
{% tab Audición %}

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
{% tab Físico %}

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
{% tab Cognitivo %}

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
- Aproximadamente, entre el 10 % y el 20 % de la población mundial se considera neurodivergente (ver [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Aproximadamente 1 de cada 100 niños tiene autismo en todo el mundo (ver [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Buenas prácticas

Crear contenidos accesibles no tiene por qué ser abrumador. Las elecciones pequeñas y meditadas pueden marcar una gran diferencia. Esta sección recorre consejos prácticos que ayudan a que más personas lean, naveguen e interactúen con éxito con tus mensajes. Tanto si ajustas tu texto, como si das estilo a tus botones o añades texto alternativo a las imágenes, cada ajuste contribuye a una experiencia más inclusiva. Vamos a profundizar.

### Contenido

#### Estructura y flujo

Empecemos por los cimientos. Cuando tu contenido tiene una estructura clara, es más fácil de seguir para todos, especialmente para las personas que dependen de lectores de pantalla o de la navegación por teclado.

- **Divide tu contenido en secciones:** Utilizar encabezamientos, viñetas y listas ayuda a las personas a comprender y escanear rápidamente tu contenido, incluso cuando tienen prisa. 
- **No te saltes los niveles de encabezamiento:** Los encabezamientos estructuran tu contenido, ayudando a los lectores a comprender rápidamente cómo se relacionan las secciones entre sí. Cuando te saltas niveles de encabezamiento (por ejemplo, saltando directamente de un H2 a un H4), rompes esta estructura lógica. Esto dificulta a los usuarios, especialmente a los que utilizan lectores de pantalla, la navegación y la comprensión clara de tu mensaje. Sigue siempre una jerarquía lógica y secuencial de encabezamientos (H1 a H2 a H3, etc.) para asegurarte de que tu contenido permanece organizado, accesible y fácil de seguir para todos.

#### Legibilidad

Una vez establecida la estructura, el siguiente paso es asegurarte de que tus palabras sean realmente fáciles de leer. Esto significa mantener las cosas sencillas, escaneables y cómodas de leer en todos los dispositivos y necesidades de los usuarios.

- **Escribe frases cortas y claras:** Las frases cortas son fáciles de entender para todos, especialmente para las personas que utilizan lectores de pantalla o que tienen problemas para procesar información compleja. Escribe a un nivel de lectura de séptimo grado de Estados Unidos. Puedes utilizar recursos como [la aplicación Hemingway](https://hemingwayapp.com/) para comprobar el nivel de lectura de tu texto.
- **Elige tamaños de letra y espaciado legibles:** Un texto demasiado pequeño puede ser difícil de leer, sobre todo en el móvil. Utiliza al menos 14px para el cuerpo del texto. Haz los títulos más grandes para que los usuarios puedan ver claramente la diferencia. El espaciado adicional entre líneas (alrededor de 1,5 de altura de línea) y párrafos mejora la legibilidad, especialmente para las personas con necesidades visuales o cognitivas.
- **Evita el texto justificado:** El texto justificado crea un espaciado desigual entre las palabras, lo que dificulta la lectura a las personas con dislexia o discapacidades cognitivas. Considera la posibilidad de alinear a la izquierda los contenidos que ocupen más de dos líneas en las lenguas de izquierda a derecha, o a la derecha en [las lenguas de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages).
- **Utiliza con moderación la negrita, la cursiva y las mayúsculas:** Enfatizar demasiado el texto dificulta la lectura, sobre todo a las personas con dislexia o deficiencias visuales. Hazlo sencillo.

#### Claridad y usabilidad

Por último, hablemos de los detalles más sutiles: las cosas que ayudan a los usuarios no sólo a ver tu contenido, sino a comprenderlo e interactuar con él. 

- **Etiqueta claramente los enlaces y botones:** Asegúrate de que el texto de tu [enlace](#links) y [botón](#buttons) explica claramente lo que ocurre a continuación. Ayuda a las personas que utilizan lectores de pantalla o navegan con un teclado a saber qué esperar.
- **No te pases con los símbolos y emojis:** Los caracteres especiales y los emojis pueden hacer que tu contenido sea divertido, pero pueden ser confusos cuando los leen los lectores de pantalla. Utilízalos con moderación y asegúrate de que no sustituyen a un texto claro y descriptivo.
- **Prueba de truncamiento:** Comprueba siempre tu texto [enviando un mensaje de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) a un dispositivo para asegurarte de que no se trunca. Si tu mensaje se corta, esto te perjudica tanto a ti como a tu audiencia, ya que impide que tu contenido les llegue.

### Botones de acción

Utiliza **botones** para indicar una acción, como enviar un formulario o reproducir un carrusel. Si navegas a una nueva URL, considera utilizar un [enlace](#links) en su lugar.

#### Escribe textos claros y orientados a la acción

Al igual que el texto del enlace, las etiquetas de los botones deben describir claramente la acción. El texto de un botón eficaz es específico y está orientado a la acción. Por ejemplo, "Enviar pedido" indica claramente a los usuarios lo que ocurrirá cuando hagan clic, mientras que "Enviar" simplemente puede ser ambiguo. Cada etiqueta debe describir con precisión su acción prevista, para que los lectores de pantalla y todos los usuarios puedan comprender y predecir fácilmente el resultado al interactuar con tus botones.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buen texto del botón <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Texto del botón pobre <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Enviar pedido"</td>
      <td>"Enviar"</td>
    </tr>
    <tr>
      <td>"Crear cuenta"</td>
      <td>"Registrarse"</td>
    </tr>
    <tr>
      <td>"Descarga nuestro folleto"</td>
      <td>"Descargar"</td>
    </tr>
    <tr>
      <td>"Ver detalles del producto"</td>
      <td>"Más información"</td>
    </tr>
    <tr>
      <td>"Suscribirse para recibir actualizaciones"</td>
      <td>"Suscriptor"</td>
    </tr>
  </tbody>
</table>

Mantén el texto del botón conciso para evitar que se trunque. Si el texto de un botón es demasiado largo, puede cortarse con una elipsis en lugar de envolverlo.

#### Utiliza un contraste de color suficiente

El texto del botón debe ser fácil de leer sobre el color de fondo del botón. Comprueba que el texto de tu botón cumple [los mínimos de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) WCAG 2.2 AA:

- Relación de contraste de 4,5:1 para texto de tamaño normal (la mayoría de los botones)
- Relación de contraste 3:1 para texto grande (normalmente por encima de 18pt)

El alto contraste ayuda a que los botones sigan siendo legibles y se pueda hacer clic en ellos para todo el mundo, incluidos los usuarios con deficiencias visuales o los que ven tu mensaje en entornos difíciles. Para más orientación, consulta la sección [Contraste de color](#color-contrast).

#### Haz que los botones sean fáciles de pulsar

Asegúrate de que tus botones (y enlaces) sean lo suficientemente grandes y estén lo suficientemente separados para los usuarios de dispositivos móviles. Los [objetivos táctiles](#touch-targets) pequeños o abarrotados pueden resultar frustrantes o imposibles de interactuar para los usuarios con discapacidad motora.  

### Enlaces

Utiliza enlaces para la navegación, como dirigir a los usuarios a una página externa.

#### Escribe un texto de enlace descriptivo

Escribe un texto de enlace que describa claramente adónde llevará el enlace al usuario. Los usuarios de lectores de pantalla suelen pasar de un enlace a otro para hojear el contenido, así que asegúrate de que el texto de tu enlace se sostiene por sí solo. Evita frases como "haz clic aquí", "más" y "haz clic para más detalles", ya que son ambiguas cuando se leen fuera de contexto.

Por ejemplo, piensa en cómo podrías escribir un enlace para ver un parte meteorológico.

| Mal  | Mejor | Mejor |
| --- | --- | --- | 
| Haz clic aquí | Haz clic aquí para acceder al tiempo de hoy | El tiempo hoy |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como con todo el contenido, que sea sencillo y con el menor número posible de palabras adicionales.

#### Evita estilizar los enlaces como botones

Los editores de arrastrar y soltar de Braze producen HTML semántico predeterminado, por lo que los enlaces no tienen el estilo de los botones. Sin embargo, si trabajas con [HTML personalizado](#custom-html) o haces cambios a nivel de código, ten esto en cuenta:

- **Los enlaces (`<a>`** ) responden a la tecla <kbd>Intro</kbd>.
- **Los botones (`<button>`** ) responden a las teclas <kbd>Intro</kbd> y <kbd>Espacio</kbd>.

Estilizar un enlace para que parezca un botón puede confundir a las personas que navegan con un teclado: pueden intentar pulsar <kbd>la barra espaciadora</kbd> y esperar que funcione.

Utiliza el elemento adecuado para la acción:

- Utiliza `<button>` para acciones, como enviar un formulario o abrir un modal.
- Utiliza `<a>` para la navegación, como enlace a otra página o archivo.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Objetivos táctiles

Los objetivos táctiles son cualquier parte de tu mensaje que los usuarios tocan para realizar una acción, como botones, enlaces o iconos. Estos elementos deben ser lo suficientemente grandes y espaciados para que la gente pueda tocarlos con facilidad, especialmente en los dispositivos móviles.

Cuando los objetivos táctiles son demasiado pequeños o están demasiado juntos, puede resultar frustrante o imposible para los usuarios con problemas de movilidad o destreza interactuar con tu mensaje. Mejorar esto puede ayudar a reducir los errores y crear una experiencia más fluida para todos.

Esto es lo que debes tener en cuenta:
- **Haz que sea fácil de pulsar.** Procura que el tamaño mínimo del objetivo táctil sea de 44 x 44 píxeles. Esto se ajusta a las directrices WCAG 2.2 para [objetivos táctiles](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) y a las normas comunes de usabilidad móvil.
- **Da un respiro a cada objetivo.** Si los objetivos de pulsación están demasiado juntos -como enlaces apilados o botones muy agrupados- puede ser fácil pasar por alto o pulsar el objetivo equivocado. Añade espaciado o relleno entre los elementos para evitarlo.
- **No te fíes sólo de lo visual.** Incluso los iconos pequeños pueden hacerse más utilizables con un relleno adicional, que les permita cumplir los requisitos de tamaño mínimo sin alterar el diseño.
- **Vista previa en el móvil.** Prueba tu mensaje en diferentes tamaños de pantalla y asegúrate de que los elementos interactivos son fáciles de usar.

Mejorar los objetivos táctiles es una de las formas más eficaces de hacer que tu mensaje sea más accesible en el móvil, y es una buena experiencia de usuario para todos.

### Imágenes

#### Proporcionar texto alternativo

El texto alternativo (alt text) es una breve descripción del contenido o función de una imagen que los lectores de pantalla y otras tecnologías de apoyo proporcionan a los usuarios. Para cada imagen significativa, escribe un texto alternativo descriptivo para que los usuarios que no puedan ver los elementos visuales comprendan tu mensaje o llamada a la acción. 

#### Evita las imágenes de texto

Siempre que sea posible, evita colocar texto dentro de imágenes: los lectores de pantalla no pueden leer el texto basado en imágenes, y los usuarios no pueden ajustar fácilmente el tamaño o el color de la fuente para mejorar la visibilidad. Ten en cuenta estos consejos:

- **Elimina el texto donde puedas:** En su lugar, traslada cualquier texto descriptivo o promocional de la imagen a un campo de texto de tu mensaje. De este modo, los usuarios pueden cambiar el tamaño o el color según lo necesiten utilizando las preferencias de su dispositivo o navegador.
- **Comprueba la legibilidad y el contraste:** Si debes mantener el texto en la imagen, sigue las mejores prácticas de [contraste de color](#color-contrast) y utiliza una [fuente a gran escala](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Esto significa que el texto debe tener al menos 18 puntos (unos 24 píxeles) si no está en negrita, o 14 puntos (unos 18 píxeles) si está en negrita. Utilizar estos tamaños ayuda a que el texto siga siendo legible sin obligar a los usuarios a hacer zoom, y mejora el contraste general y la legibilidad del contenido. Haz una prueba para confirmar que sigue siendo legible en pantallas más pequeñas.
- **Proporciona un texto alternativo:** Para el texto esencial que debe permanecer en la imagen, incluye un texto alternativo que describa las palabras.

Cuando las imágenes contienen texto que no puede editarse, los usuarios con deficiencias visuales pierden flexibilidad para realizar ajustes de lectura. Al separar el texto de las imágenes, ayudas a que más usuarios lean e interactúen con tu mensaje cómodamente.

#### Consejos para escribir texto alternativo

- [Describe lo que hay realmente en la imagen](#tip-1)
- [Sé breve, pero específico](#tip-2)
- [Evita "imagen de" o "foto de"](#tip-3) 
- [Refleja el texto que aparece en la imagen](#tip-4)
- [Cíñete al contexto pertinente, sin jerga adicional de marketing](#tip-5)
- [Considera la finalidad de la imagen](#tip-6)

##### Describe lo que hay realmente en la imagen {#tip-1}

Los usuarios de lectores de pantalla confían en el texto alternativo para comprender el contenido o la función de una imagen. Evita el "lenguaje de marketing" genérico que no coincide con lo que se muestra visualmente.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Malos ejemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mujer sonriente con chaqueta vaquera azul, sosteniendo una bolsa de la compra".</td>
      <td>"¡Es hora de darse un capricho!" (No se menciona lo que hay realmente en la imagen)</td>
    </tr>
    <tr>
      <td>"Hombre con camiseta negra, apoyado en una bici en una calle de la ciudad".</td>
      <td>"¡Abraza tu mejor vida ahora!" (Ignora la configuración de bicicleta y ciudad)</td>
    </tr>
    <tr>
      <td>"Edificio de apartamentos azul con un cartel de "Se alquila" delante".</td>
      <td>"¡La clave para un mañana mejor!" (No refleja el apartamento ni el cartel)</td>
    </tr>
  </tbody>
</table>

##### Sé breve, pero específico {#tip-2}

Un texto alternativo conciso facilita el procesamiento por parte de los usuarios. Incluye suficientes detalles para transmitir el propósito, pero omite cualquier palabrería. Como regla general, mantén el texto alternativo en 125 caracteres o menos. Si es necesario algo más que una frase u oración breve, considera la posibilidad de utilizar uno de los [métodos de descripción larga](https://www.w3.org/WAI/tutorials/images/complex/) del W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Malos ejemplos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Zapatillas de correr rojas sobre fondo blanco"</td>
      <td>"Zapatillas de running extremadamente cómodas y perfectas para tu estilo de vida activo en un vibrante tono rojo" (Demasiado largas y llenas de palabrería promocional).</td>
    </tr>
    <tr>
      <td>"Cuatro portátiles en un expositor"</td>
      <td>"Descubre el potenciador definitivo de la productividad que redefine cómo trabajas cada día, de todas las formas imaginables" (No describe lo que se muestra en realidad).</td>
    </tr>
    <tr>
      <td>"Grupo de amigos comiendo helado en un día soleado"</td>
      <td>"Captura la felicidad pura con la golosina más dulce: ¡la vida es mejor con nuestra marca de helados!" (Demasiado abstracto y centrado en la marca)</td>
    </tr>
  </tbody>
</table>

##### Evita "imagen de" o "foto de" {#tip-3}

Los lectores de pantalla ya anuncian una imagen. Pasa directamente a describir el tema.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Malos ejemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mesa preparada para el brunch con tortitas, fruta y café".</td>
      <td>"Imagen de una mesa puesta para el brunch"</td>
    </tr>
    <tr>
      <td>"Valla publicitaria al borde de la carretera con el texto en negrita "Gran inauguración"".</td>
      <td>"Imagen de una valla publicitaria en el arcén de una carretera"</td>
    </tr>
    <tr>
      <td>"Paisaje montañoso nevado al atardecer"</td>
      <td>"Foto de nieve y montañas"</td>
    </tr>
  </tbody>
</table>

##### Refleja el texto que aparece en la imagen {#tip-4}

Si una imagen incluye texto esencial, pon esa información en el texto alternativo para que los usuarios no se la pierdan.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Malos ejemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Cartel con la leyenda 'Rebajas de verano: 50% de descuento en todos los trajes de baño'".</td>
      <td>"Banner promocionando una venta" (No menciona el descuento real).</td>
    </tr>
    <tr>
      <td>"Logotipo con el texto 'Café Toscana' en fuente script"</td>
      <td>"Imagen del logotipo de una cafetería" (No incluye el texto "Café Toscana").</td>
    </tr>
    <tr>
      <td>"Anuncio que anuncia 'Entradas para conciertos disponibles ahora - Comienza el 5 de junio'"</td>
      <td>"Anuncio de concierto" (Sin detalles del evento)</td>
    </tr>
  </tbody>
</table>

##### Cíñete al contexto pertinente, sin jerga adicional de marketing {#tip-5}

No rellenes el texto alternativo con términos SEO o llamadas a la acción que no estén directamente relacionadas con la imagen. Aporta valor para los que no pueden ver la imagen.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Malos ejemplos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Portátil que muestra el gráfico de análisis del panel de Braze"</td>
      <td>"¡Aumenta las conversiones y dispara el ROI con la mejor plataforma del mundo!" (Añade lenguaje de marketing innecesario)</td>
    </tr>
    <tr>
      <td>"Juego de patio con cuatro sillas y mesa de cristal"</td>
      <td>"¡Organiza ahora una increíble fiesta de verano para todos tus amigos y familiares!" (Describe un escenario, no la imagen)</td>
    </tr>
    <tr>
      <td>"Teléfono móvil mostrando una aplicación de previsión meteorológica con 75°F a la vista"</td>
      <td>"Experimenta innovaciones en tiempo real en el seguimiento meteorológico que cambian las reglas del juego" (No refleja lo que se muestra visiblemente)</td>
    </tr>
  </tbody>
</table>

##### Considera la finalidad de la imagen {#tip-6}

Si una imagen funciona como un enlace o una llamada a la acción, describe la acción prevista ("Compra", "Enlace a", "Regístrate"), no sólo la etiqueta o el producto mostrado.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Malos ejemplos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Compra la Colección de Otoño"</td>
      <td>"Colección de Otoño" (Falta de acción prevista)</td>
    </tr>
    <tr>
      <td>"Enlace al eBook gratuito"</td>
      <td>"Free eBook" (No aclara que se trata de un enlace)</td>
    </tr>
    <tr>
      <td>"Regístrate en la lista de correo"</td>
      <td>"Lista de correo" (No describe lo que puede hacer el usuario)</td>
    </tr>
  </tbody>
</table>

Si la imagen no tiene una finalidad, hazlo saber también. Las imágenes decorativas, como los logotipos, deben tener una etiqueta alt vacía (`alt=""`) para que los lectores de pantalla sepan que deben omitir su anuncio. Sin ella, normalmente se lee el nombre del archivo de imagen.

### Videos

Los videos son atractivos, pero si no son accesibles, corres el riesgo de excluir a parte de tu audiencia. Utiliza los siguientes consejos para que tus contenidos de video sean más inclusivos:

- [Proporcionar subtítulos](#closed-captions)
- [Proporcionar controles de reproducción](#playback-controls)
- [Evita la reproducción automática](#no-auto-play)
- [Evita los contenidos intermitentes o estroboscópicos](#no-seizures)

#### Proporcionar subtítulos {#closed-captions}

Incluye subtítulos en tus videos para que los usuarios puedan seguir el diálogo, los efectos de sonido y otros contenidos de audio. Los subtítulos ayudan:

- Personas sordas o con dificultades auditivas
- Espectadores en un entorno sin sonido
- Hablantes no nativos que prefieren leer en voz alta

Los subtítulos se pueden alternar entre activarlos y desactivarlos, permitiendo a los usuarios elegir lo que más les convenga.

{% multi_lang_include accessibility/video.md %}

#### Proporcionar controles de reproducción {#playback-controls}

Asegúrate de que tu video incrustado incluye controles de reproducción accesibles -como reproducir, pausar, silenciar y buscar- para que los usuarios puedan interactuar con él de la forma que mejor les convenga.

#### Evita la reproducción automática {#no-auto-play}

Siempre que sea posible, evita configurar los videos para que se reproduzcan automáticamente. La reproducción automática puede resultar chocante o desorientadora para:

- Usuarios que utilizan lectores de pantalla o navegación por teclado
- Personas con sensibilidad al movimiento
- Cualquier persona en un entorno tranquilo (como un lugar de trabajo o un entorno nocturno)

Deja que los usuarios elijan cuándo reproducir un video incluyendo controles claros.

#### Evita los contenidos intermitentes o estroboscópicos {#no-seizures}

No incluyas videos con efectos intermitentes o estroboscópicos, especialmente con una frecuencia elevada. Pueden desencadenar ataques en usuarios con epilepsia fotosensible y causar molestias a los demás.

### Contraste de color

Un contraste de color suficiente ayuda a garantizar que tus mensajes sean fáciles de leer para todo el mundo, incluidas las personas con baja visión o las que ven tu contenido en condiciones de mucha luz o difíciles. Procura que las relaciones de contraste cumplan [los requisitos del nivel AA de las WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Relación de contraste de 4,5:1 para texto normal (piensa en el cuerpo del texto, botones y enlaces)
- Relación de contraste 3:1 para texto grande (piensa en títulos y etiquetas grandes)

Puedes probar tus elecciones de color utilizando la [herramienta de comprobación de contraste de WebAim](https://webaim.org/resources/contrastchecker/).

{% multi_lang_include accessibility/color.md %}

### HTML personalizado

Si utilizas algún HTML personalizado en tu mensajería:

- Utiliza [HTML semántico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Esto significa utilizar los elementos HTML correctos para su propósito, en lugar de estilizar un elemento para que parezca otro. La mayoría de los elementos HTML tienen incorporado su propio soporte de accesibilidad.
- Establece el [atributo`lang` ](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) dentro de tu HTML para identificar el idioma en el que está tu contenido. Los lectores de pantalla utilizan diferentes bibliotecas de sonidos para cada idioma, según la pronunciación y las características de ese idioma. Si no se especifica, un lector de pantalla asume que el contenido está escrito en el idioma predeterminado que el usuario eligió al configurar el lector de pantalla. Si el mensaje no está en la lengua predeterminada, es posible que el lector de pantalla no pronuncie el mensaje correctamente. 

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Cuando utilices el editor de arrastrar y soltar de correo electrónico, el valor del idioma para el correo electrónico se puede establecer yendo a la pestaña **Configuración** y seleccionando el valor del idioma adecuado.
{% endalert %}

- Utiliza [atributos ARIA](#aria-attributes) para dar un contexto adicional. Estos atributos proporcionan información adicional a las tecnologías de asistencia, ayudando a aclarar la función, el estado o las propiedades de los elementos de la IU que, de otro modo, podrían no estar claros. 

### Atributos ARIA

Cuando utilices código personalizado en los editores de Braze, puedes utilizar Aplicaciones de Internet Ricas Accesibles[(ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) para proporcionar soporte de accesibilidad adicional a los usuarios que dependen de tecnología de asistencia. Los roles y atributos ARIA ayudan a los lectores de pantalla a interpretar tu contenido con mayor claridad, especialmente cuando utilizas elementos que no transmiten significado por sí solos (como `<div>` o `<span>`).

{% alert important %}
Aunque ARIA está diseñada para hacer más accesible el contenido Web, si se utiliza incorrectamente, puede hacer más mal que bien. ARIA no sustituye al HTML semántico, sino que lo complementa, así que utiliza ARIA sólo cuando los elementos HTML nativos no satisfagan tus necesidades.
{% endalert %}

He aquí algunos ejemplos especialmente útiles en contextos de mensajería:

- [aria-etiqueta](#aria-label)
- [aria-etiquetadapor](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentación"](#rolepresentation)
- [aria-live="cortés"](#aria-livepolite)

#### aria-etiqueta

`aria-label` añade un nombre accesible a los elementos que no tienen texto visible. Si utilizas un icono sin texto (como una papelera o una "X" de cerrar), alguien que utilice un lector de pantalla no sabrá lo que hace, a menos que lo etiquetes. `aria-label` da voz a ese icono.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-etiquetadapor

`aria-labelledby` conecta un elemento a algo que ya tiene una etiqueta visible. Así que si tienes un banner o una región que debe leerse en voz alta con un título, puedes utilizar `aria-labelledby` para decirle a la tecnología de asistencia: "Oye, utiliza ese encabezamiento de ahí para nombrar esta parte".

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true"

`aria-hidden="true"` oculta cosas a los lectores de pantalla.  Es útil para textos o elementos visuales que no transmiten un significado importante, como un destello, una marca de verificación o un emoji utilizado únicamente por estilo.

Esto mantiene la experiencia más limpia para los usuarios de lectores de pantalla, que de otro modo podrían oír contenidos redundantes o confusos. También es útil para ocultar cosas como el contenido del acordeón fuera de la pantalla que aún no se ha expandido.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

En general, es mejor utilizar `alt=""` para [imágenes decorativas](#images) e iconos que `aria-hidden="true"`. Mientras que el HTML semántico es ampliamente compatible con todos los lectores de pantalla y software de asistencia, la compatibilidad con ARIA varía. Aunque utilices `aria-hidden`, debes incluir un atributo alt vacío.

#### role="presentación"

`role="presentation"` indica a la tecnología de asistencia que ignore los elementos de diseño, como las tablas de diseño. Por ejemplo, los correos electrónicos suelen utilizar tablas sólo para alinear las cosas. Sin esta función, los lectores de pantalla podrían suponer que tu diseño es una tabla de datos y empezar a leer los números de fila y columna.  

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

Los correos electrónicos creados en el editor de arrastrar y soltar tienen elementos de presentación marcados automáticamente con el atributo ARIA `role="presentation"`.

#### aria-live="cortés"

`aria-live="polite"` anuncia las actualizaciones cuando cambia el contenido sin necesidad de interacción por parte del usuario. Utilízalo cuando muestres actualizaciones dinámicas dentro de un mensaje, como aciertos, errores u otras notificaciones.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Pruebas automatizadas de accesibilidad

Para ayudarte a identificar y solucionar pronto los problemas de accesibilidad, Braze ofrece pruebas automatizadas de accesibilidad en las siguientes áreas:

- [Buzón de entrada Visión]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) para los correos electrónicos
- [Escáner de accesibilidad]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/#accessibility-scanner) para mensajes creados con nuestro editor HTML (por ejemplo, mensajes HTML dentro de la aplicación, bloques de contenido HTML, [pies de página de correo electrónico personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer), [páginas de adhesión voluntaria por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-opt-in-page) y [páginas para cancelar suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-unsubscribe-page)).

Estas pruebas comprueban si tu mensaje cumple las Pautas de Accesibilidad al Contenido en la Web[(WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/), un conjunto de normas técnicas reconocidas internacionalmente para el contenido accesible. Cualquier problema que pueda detectarse automáticamente se marca y se clasifica por gravedad para ayudarte a priorizar.

{% alert note %}
Inbox Vision funciona tanto para correos electrónicos HTML como para arrastrar y soltar. El escáner sólo funciona con contenidos creados con el editor HTML.
{% endalert %}

### Lo que las pruebas de automatización pueden y no pueden detectar

Las pruebas automatizadas de accesibilidad son un buen punto de partida, pero no pueden detectarlo todo. Algunas cuestiones necesitan un toque humano para evaluarse correctamente, sobre todo cuando el contexto o el diseño visual influyen en la forma en que los usuarios experimentan tu correo electrónico.

Puede que veas algunas cuestiones marcadas como **Necesita revisión**. Estos son casos en los que el verificador no puede decir con seguridad si algo es un problema para la accesibilidad. Cuando eso ocurra, te recomendamos que lo revises manualmente.

Algunos ejemplos de lo que las herramientas de automatización no pueden detectar con fiabilidad son:

- Si el orden de enfoque de los elementos interactivos sigue una secuencia lógica
- Si el contenido es totalmente manejable con un teclado, sin necesidad de un ratón
- Si el texto alternativo describe significativamente una imagen
- Si los encabezamientos se utilizan correctamente para organizar el contenido
- Si los enlaces y botones están claramente etiquetados y son fáciles de entender
- Si los objetivos táctiles son lo suficientemente grandes y están espaciados adecuadamente
- Si el texto sobre imágenes de fondo cumple los requisitos de contraste de color
- Si las instrucciones o etiquetas son claras y útiles para todos los usuarios

Estas limitaciones no son únicas de Braze, sino comunes a todas las herramientas de accesibilidad automatizada. Las comprobaciones automatizadas no pueden imitar todas las tecnologías de apoyo, lectores de pantalla o necesidades de los usuarios. Por eso la accesibilidad no se comprueba una sola vez, sino que es una práctica continua.

Aunque tu mensaje pase todas las comprobaciones de automatización, sigue siendo importante:

- Revisa detenidamente las cuestiones marcadas, especialmente las etiquetadas como **Necesita revisión**.
- Pruébalo manualmente siempre que sea posible, sobre todo en lo que se refiere a patrones de diseño e interacción.
- Utiliza herramientas como lectores de pantalla, navegación sólo con teclado y zoom del navegador para simular diferentes necesidades de acceso.

Combinando la automatización de las pruebas con una revisión manual concienzuda, detectarás más problemas potenciales y crearás campañas más inclusivas y útiles para todos los destinatarios.
