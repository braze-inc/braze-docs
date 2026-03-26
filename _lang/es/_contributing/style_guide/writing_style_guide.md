---
nav_title: Guía de estilo de Braze Docs
article_title: Guía de estilo de Braze Docs
description: "Guía de estilo de redacción para Braze Docs."
page_order: 0
noindex: true
---

# Guía de estilo de Braze Docs

## Guía de estilo de redacción

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### Directrices generales {#general-guidelines}

#### Voz y tono {#voice-and-tone}

La voz de la marca Braze es inteligente, conversacional y directa. Somos una voz humana en un mundo de tecnicismos; proporcionamos claridad y orientación a cualquier persona interesada en el arte de la interacción con los clientes; y evitamos la jerga en favor de un lenguaje conciso que es tan fácil de entender como poderoso.

Para alinear esta voz de marca en nuestra redacción y edición, usamos tres directrices de voz: **directa, empoderadora** y **humana**.

##### Directa

Estructura tu redacción de forma clara y facilita que las personas encuentren la información que necesitan.

* Explica las cosas complicadas de forma sencilla.
* Sé conciso.
* Usa un lenguaje consistente para funciones y acciones.

###### Directrices

✅ Usa elementos visuales para ayudar a aclarar temas complejos. <br>
**Ejemplo:** La imagen del ciclo de vida del perfil de usuario en el [artículo sobre el ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) ayuda a ilustrar un concepto complejo.

✅ Crea una jerarquía de información clara. <br>
**Ejemplo:** "Esta es una descripción general de cómo se gestiona el contenido en Braze Docs. Para obtener más información sobre un tema específico, elige la página del tema dedicada en la navegación."

✅ Elimina sin piedad la jerga y los acrónimos si es posible. Si no es posible, defínelos. <br>
**Ejemplo:** "El servicio de mensajes cortos (SMS) se usa para enviar y recibir mensajes de texto breves."

##### Empoderadora

¿Qué problema intentas resolver con tu redacción? Ten ese problema en mente al crear cualquier contenido.

* Explica el "por qué" y el "cómo" para dar a los usuarios la confianza de actuar.
* Sé específico al explicar los beneficios, y sé claro sobre lo que es y no es posible.
* Ofrece consejos prácticos y ánimo sincero.

###### Directrices

✅ Facilita encontrar el camino correcto. <br>
**Ejemplo:** "Cuando detienes un Canvas, se aplica lo siguiente: 1. Se impide que los usuarios entren al Canvas. 2. No se envían más mensajes, sin importar dónde se encuentre un usuario en el flujo. 3. **Excepción:** Los Canvas de correo electrónico no se detienen inmediatamente."

✅ Proporciona ejemplos, casos de uso y plantillas que simplifiquen o mejoren el trabajo del usuario. <br>
**Ejemplo:** "`IInAppMessageManagerListener` también incluye métodos delegados para clics en el mensaje en sí o en uno de los botones. Un caso de uso común sería interceptar un mensaje cuando se hace clic en un botón o mensaje para un procesamiento adicional."

##### Humana

La redacción informativa es inherentemente seca; queremos que los lectores se centren en el contenido, no en la forma de entregarlo. Aun así, podemos escribir de una manera que ayude a nuestros lectores a procesar la información que están consumiendo y que sea más probable que interioricen el conocimiento. Sé humano, deja que tu personalidad se muestre y sé memorable.

* Apunta a un tono conversacional en lugar de uno formal.
* Céntrate en el usuario; respeta su situación y estado emocional.
* Centra activamente la experiencia humana, no el estado de la máquina.

###### Directrices

✅ Aplica el tono y los recursos de marca de forma reflexiva. <br>
**Ejemplo:** "Integrar con Braze es un proceso que vale la pena. Pero eres inteligente. Estás aquí. Claramente, ya lo sabes."

✅ Aplica las [mejores prácticas de accesibilidad](#accessibility) tanto para contenido visual como verbal. <br>
**Ejemplo:** Reemplazar expresiones idiomáticas como "listo para usar" con "predeterminado" hace que tu texto sea más accesible para hablantes de español como segundo idioma.

✅ Proporciona soporte consistente a lo largo del recorrido del usuario. <br>
**Ejemplo:** Usa el marco Diátaxis para asegurarte de que estás satisfaciendo las necesidades de diferentes usuarios en diferentes momentos.

#### Accesibilidad {#accessibility}

Braze busca proporcionar una experiencia inclusiva. Usa las siguientes directrices para asegurarte de que tu contenido de aprendizaje sea accesible para los [mil millones de personas](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health) con una necesidad de accesibilidad.

##### General

* Evita el lenguaje sesgado o capacitista. Para más información, consulta la sección sobre [lenguaje inclusivo](#inclusive-language).
* Usa un [lector de pantalla](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac) para probar tu contenido.
* No uses un [ampersand](#ampersands) (&) en lugar de "y" a menos que hagas referencia a elementos de la interfaz que usen un ampersand.

##### Lenguaje y formato

* Usa [lenguaje sencillo](https://www.plainlanguage.gov/guidelines/).
* Coloca la información más importante al principio de las secciones. Usa el modelo periodístico de la [pirámide invertida](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)).
* Divide los bloques de texto para ayudar a los lectores a escanear la información. Usa párrafos, [listas](#lists), [alertas](#callouts-and-alerts) e [imágenes](#figures-and-other-images) para mejorar la legibilidad.
* [Escribe oraciones y párrafos cortos](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html). Como regla general, apunta a no más de 20 palabras por oración, cinco oraciones por párrafo.
* Evita usar acrónimos y frases en latín, ya que pueden ser difíciles de traducir. En su lugar, usa palabras o frases sencillas.

##### Encabezados

* Usa [encabezados y títulos](#headings-and-titles) únicos, descriptivos y claros.
* Usa un h1 para los títulos de página.
* No te saltes niveles de encabezado. Un h3 debe seguir a un h2, y así sucesivamente.

##### Enlaces

* No uses texto de enlace como "Más información", "aquí" o "este documento". Para más frases a evitar, consulta la sección [Redacción de enlaces](#writing-links).
* Evita colocar dos enlaces seguidos en una oración. Pon un carácter o palabra entre ellos para separarlos.
* Los [enlaces para descargar archivos](#links-for-file-download) deben indicar que al hacer clic se descarga el archivo, así como el tipo de archivo (PDF, CSV, etc.)
* Si no queda claro por el contexto, los enlaces a secciones del mismo documento deben usar una [frase estándar](#structuring-links) que indique esta acción.

##### Imágenes, videos y GIF

* Proporciona [texto alternativo](#alt-text) para cada imagen que resuma la información presentada en la imagen.
* No uses imágenes como la única forma de mostrar información. Siempre proporciona los pasos, contenido u otros detalles presentados en la imagen en el texto circundante.
* No uses imágenes de salida de terminal, muestras de código o texto. En su lugar, usa texto real.
* Proporciona subtítulos para el contenido de video.
* No uses elementos parpadeantes en videos o GIF.

##### Tablas {#tables-1}

* Siempre usa una oración introductoria para describir el propósito de la tabla.
* Evita tablas en medio de una lista, especialmente una lista de pasos.

#### Audiencia global {#global-audience}

Escribimos nuestro contenido de aprendizaje en inglés americano. Sin embargo, Braze es una marca global y, como tal, escribimos para una audiencia global. Usa las siguientes directrices para asegurarte de que los clientes entiendan tu redacción incluso cuando el inglés no sea su primer idioma.

1. **Escribe pensando en la localización:**
  * Formatea las [fechas y horas](#dates-and-times) de formas no ambiguas.
  * No pongas superposiciones de texto en imágenes, ya que este texto no se puede traducir.
  * Evita [jerga y expresiones idiomáticas](#slang-and-idioms).
  * Proporciona contexto. No asumas que el lector sabe de qué estás hablando.
2. **Escribe oraciones cortas y precisas:**
  * Usa [lenguaje sencillo](https://www.plainlanguage.gov/guidelines/).
  * Define las [abreviaturas](#abbreviations).
  * Evita [pronombres ambiguos](#ambiguous-pronouns). Si un pronombre puede ser ambiguo, reemplázalo con el sustantivo apropiado.
3. **Sé consistente:**
  * Usa el mismo término para un concepto en todas las menciones del término, incluyendo la misma capitalización y formato de texto.
  * Escribe oraciones en orden sujeto + verbo + objeto.
  * Si las instrucciones dependen de que se cumpla una condición, coloca la cláusula condicional primero. Para más información, consulta [orden de cláusulas](#clause-order).
4. **Sé inclusivo:**
  * Usa [lenguaje inclusivo](#inclusive-language).
  * Usa [nombres de ejemplo](#example-names) diversos.
  * Evita el humor culturalmente específico.

#### Lenguaje inclusivo {#inclusive-language}

Puede que seamos una empresa B2B, pero las personas están en el centro de lo que hacemos, y la nuestra es una marca global. Siempre que nos referimos a una persona en nuestro contenido, somos conscientes de ser inclusivos y considerados. En caso de duda, consulta esta sección o [The Diversity Style Guide](https://www.diversitystyleguide.com/).

##### Edad

A menos que sea relevante para tu redacción, no te refieras a la edad de un sujeto. No uses calificadores como "joven" o "viejo" para describir a ningún sujeto o audiencia.

Si estás representando un grupo de edad, sé descriptivo y específico como "Generación Z" en lugar de "juventud". No uses descriptores vagos como "edad universitaria" cuando podrías decir "estudiantes universitarios" en su lugar.

##### Color

Evita incluir términos de color en tu redacción a menos que sea absolutamente necesario, y si es necesario, incluye texto explicativo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pulsa ✅ Guardar.</td><td style="width: 50%;">Pulsa el ícono verde de Guardar.</td></tr>
<tr><td style="width: 50%;">Pulsa el ícono de marca de verificación verde.</td><td style="width: 50%;">Pulsa el ícono verde junto al botón rojo de Cancelar.</td></tr>
<tr><td style="width: 50%;">Pulsa el ícono verde.</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

No dependas del color como el único indicador para elementos interactivos. Por ejemplo, subraya los enlaces al pasar el cursor, o marca un campo obligatorio con un asterisco.

Evita depender únicamente del verde y el rojo para indicadores de "bueno" y "malo" (o, más frecuentemente, "correcto" e "incorrecto"). El daltonismo rojo/verde es el tipo más común de daltonismo. Si usas color para comunicar lo correcto y lo incorrecto, asegúrate de incluir también otro texto o símbolos para transmitir el mismo punto.

##### Lenguaje condescendiente {#condescending-language}

Al escribir instrucciones o detallar pasos para que un lector siga, evita usar palabras o frases como:

* simple, como "Crear una campaña es simple."
* simplemente, como "...simplemente agrega X en Y"
* solo, como "...solo instala X"
* "Es fácil"

Si alguien tiene dificultades con los pasos o instrucciones, tus descriptores casuales pueden sentirse condescendientes. También puedes excluir involuntariamente a personas de tu documentación que interpreten eso como un indicador de que de alguna manera no son lo suficientemente hábiles para seguir tus instrucciones.

##### Clientes versus consumidores

Al referirte a los usuarios de la empresa y sus consumidores, usa los siguientes términos según corresponda:

* **Clientes:** Marcas con las que trabajamos. Nunca te refieras a nuestros clientes como "clients".
 * **Usuarios de la empresa:** En el contexto de la documentación, cuando es importante distinguir entre los usuarios de la plataforma y los usuarios finales que reciben mensajes de marketing, usa "usuarios de la empresa".
* **Consumidores:** Clientes de una marca con la que trabajamos.
* **Usuarios:** Generalmente reservado para una estadística específica que depende de métricas de "usuario" (como "retención de usuarios"). Al referirte a "usuarios" en nuestro contenido, primero intenta ser más específico. Piensa en compradores, consumidores, pacientes, jugadores.

##### Departamentos y equipos

Capitaliza los nombres de departamentos o equipos. No capitalices "equipo" o "departamento".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, equipo de producto de Inteligencia Empresarial</td><td style="width: 50%;">marketing, inteligencia empresarial Equipo de Producto</td></tr>
<tr><td style="width: 50%;">departamento de Ingresos</td><td style="width: 50%;">Departamento de Ingresos</td></tr>
</tbody>
</table>
{:/}

##### Discapacidad

No te refieras a la discapacidad de una persona a menos que sea específicamente relevante para tu redacción. En ese caso, sé considerado y pregunta si el sujeto prefiere lenguaje centrado en la identidad o centrado en la persona. Al referirte a un sujeto con discapacidad, no uses términos como "discapacitado" de forma despectiva.

El lenguaje capacitista incluye palabras o frases como "loco", "demente", "ciego ante" o "hacer la vista gorda", "paralizar", "tonto" y otros. Elige palabras alternativas según el contexto.

##### Enfermedad

Al describir una enfermedad, evita palabras como "sufrir", "luchar" o "víctima". Intenta ser neutral y objetivo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Le diagnosticaron cáncer.</td></tr>
<tr><td style="width: 100%;">Viven con VIH.</td></tr>
<tr><td style="width: 100%;">Se recuperó de su derrame cerebral.</td></tr>
</tbody>
</table>
{:/}


##### Inclusividad en el contenido

Destaca y representa a una comunidad diversa. Sé consciente e inclusivo al involucrar a nuestros clientes, ponentes, expertos de la industria y miembros del equipo de Braze.

##### Títulos de trabajo

En cuanto a los títulos de trabajo, nos desviamos del estilo AP. En todos los casos, capitalizamos los títulos de trabajo cuando nos referimos a alguien específicamente.

###### Título de trabajo con nombre de empresa

Capitaliza los títulos formales cuando van antes o después del nombre de una persona. Los formateamos de tres maneras:

1. **[Título formal]** en **[Nombre de empresa]** + **[Nombre completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Director Creativo en PantsLabyrinth David Bowie</td><td style="width: 50%;">director creativo en PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Nombre completo]** + coma + **[Título formal]** en **[Nombre de empresa]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Director Creativo en PantsLabyrinth</td><td style="width: 50%;">David Bowie, director creativo en PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[Nombre de empresa]** + **[Título formal]** + **[Nombre completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Director Creativo David Bowie</td><td style="width: 50%;">PantsLabyrinth director creativo David Bowie</td></tr>
</tbody>
</table>
{:/}

###### Título de trabajo sin nombre de empresa

Al referirte a una persona específica por su título formal, capitaliza su título formal y nombre de la siguiente manera:

1. **[Título formal]** + **[Nombre completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Título formal]** + coma + **[Nombre completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### Otros

Los títulos formales van "en [EMPRESA]." Los fundadores y cofundadores van "de [EMPRESA]." Los títulos formales y las ocupaciones por sí solos no necesitan capitalizarse.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Le escribí a su director de datos.</td><td style="width: 50%;">Le escribí a su Director de Datos</td></tr>
<tr><td style="width: 50%;">Hablamos con varios analistas de inteligencia empresarial.</td><td style="width: 50%;">Hablamos con varios Analistas de Inteligencia Empresarial.</td></tr>
<tr><td style="width: 50%;">Contacta a tu director de cuentas de Braze.</td><td style="width: 50%;">Le escribí a su Director de Datos Contacta a tu Director de Cuentas de Braze.</td></tr>
</tbody>
</table>
{:/}

Adhiérete a títulos de trabajo de género neutro a menos que el género ya se haya establecido.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">vendedor/a</td><td style="width: 50%;">vendedor/vendedora</td></tr>
</tbody>
</table>
{:/}

Abrevia los títulos donde sea apropiado, como VP o SVP, si así es como la persona se refiere a su título. En caso de espacio de texto limitado, las abreviaturas estándar (VP, SVP, Sr. o Jr.) son aceptables.

##### Género

No hagas suposiciones sobre el género de las personas. Pregunta a los sujetos que aparecen en tu contenido cómo se identifican.

Al referirte a miembros de la comunidad, "queer" es aceptable. "Gay" no lo es. Puedes referirte a un grupo de personas como "LGBTQ". No uses esto para describir a un individuo.

Al dirigirte a grupos de personas en tu contenido, evita asignar género a tu audiencia (ejemplo: "¡OK, señoras!"). Usa expresiones de género neutro en su lugar (ejemplo: "¡Empecemos, todos!").

"Ellos/ellas" siempre es aceptable como pronombre singular o plural en todo nuestro contenido.

##### Salud mental

La salud mental y las enfermedades cubren una amplia gama de condiciones. A menos que sea relevante para lo que estás escribiendo, no te refieras a la salud mental de una persona. Evita palabras y frases estigmatizantes. No uses términos médicos coloquialmente (ejemplo: "El estado deprimente de las cosas...").

##### Nombres

La primera vez que mencionas a una persona, usa su nombre y apellido completo. A partir de ahí, usa su nombre o apellido al referirte a ella.

##### Pronombres

Para información sobre el uso apropiado de pronombres, consulta la sección de lenguaje y gramática sobre [pronombres](#pronouns).

##### Raza, religión y etnia

No te refieras a la raza, religión o etnia de una persona a menos que sea relevante para lo que estás escribiendo. En redacciones donde la raza o etnia es un factor, pregunta a tu sujeto cómo se identifica.

No uses un guion para indicar herencia o religión dual. En su lugar, usa un espacio.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">musulmán estadounidense</td><td style="width: 50%;">musulmán-estadounidense</td></tr>
<tr><td style="width: 50%;">cubano estadounidense</td><td style="width: 50%;">cubano-estadounidense</td></tr>
</tbody>
</table>
{:/}

Capitaliza los nombres propios de etnias, nacionalidades, pueblos y tribus.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Camboyano</td><td style="width: 50%;">camboyano</td></tr>
<tr><td style="width: 50%;">Afroamericanos</td><td style="width: 50%;">afroamericanos</td></tr>
</tbody>
</table>
{:/}

Capitaliza los nombres de religiones o términos religiosos.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Fe Bahá'í</td><td style="width: 50%;">fe bahá'í</td></tr>
<tr><td style="width: 50%;">Budista</td><td style="width: 50%;">budista</td></tr>
</tbody>
</table>
{:/}

No te apropies de palabras o expresiones que pertenecen al inglés vernáculo afroamericano (on fleek, bae, lit, woke).

No te apropies de palabras o expresiones específicas de pueblos indígenas (ejemplo: animal espiritual, powwow).

#### Fuentes de terceros {#third-party-sources}

Nunca copies contenido de otros sitios, ya que puede violar los derechos de autor. El contenido puede ser tanto texto como imágenes.

En lugar de copiar o citar sitios de terceros, parafrasea el contenido o proporciona un enlace al sitio de terceros para más información. Para más información, consulta [Enlaces a otros sitios](#links-to-other-sites).

### Lenguaje y gramática {#language-and-grammar}

Mantener la coherencia con la gramática y la mecánica acordadas nos ayuda a mantener nuestra redacción clara y consistente. Esta sección cubre lo que intentamos seguir en nuestra documentación técnica a menos que se especifique lo contrario.

#### Abreviaturas {#abbreviations}

Las abreviaturas, como acrónimos, siglas y palabras acortadas, pueden afectar nuestra claridad, voz y SEO.

Aunque algunas abreviaturas son ampliamente comprendidas, otras no son bien conocidas o son familiares solo para un grupo específico de clientes. Usa tu mejor criterio y, como regla general, está bien no deletrear una abreviatura si está listada en el [American Heritage Dictionary](https://ahdictionary.com/).

Si una abreviatura no es bien conocida, deletréala en la primera mención, seguida de la abreviatura entre paréntesis. Para todas las menciones posteriores del término, usa la abreviatura.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Deletrea las abreviaturas poco comunes en la primera mención</em></th><th style="width: 50%;">Incorrecto: <em>Deletrear abreviaturas comunes</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Dominio de nivel superior (TLD)</td><td style="width: 50%;">Formato de documento portátil (PDF)</td></tr>
<tr><td style="width: 50%;">Identificador único universal (UUID)</td><td style="width: 50%;">Bus serie universal (USB)</td></tr>
</tbody>
</table>
{:/}


Trata las abreviaturas como palabras regulares al hacerlas plurales, y no agregues un apóstrofo; por ejemplo, APIs y SDKs. Lo mismo aplica para qué artículo (un o una) usas: mira cómo se pronuncia la abreviatura. Cuando una abreviatura comienza con un sonido vocálico, usa "una"; para sonidos consonánticos, usa "un".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa artículos según cómo se pronuncia la abreviatura, no cómo se escribe</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">un ISP</td></tr>
<tr><td style="width: 100%;">una DLL</td></tr>
<tr><td style="width: 100%;">un sitio HTML</td></tr>
<tr><td style="width: 100%;">un archivo CSV</td></tr>
</tbody>
</table>
{:/}

#### Voz activa {#active-voice}

En Braze usamos la voz activa cuando es posible. La voz activa es nuestro estándar de oro. Evita la voz pasiva, en la que puede ser difícil determinar quién o qué está realizando una acción particular.

Para ver si tu oración está en voz pasiva, inserta "por alguien" después del verbo. Si la oración tiene sentido, lo más probable es que esté en voz pasiva.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa voz activa</em></th><th style="width: 50%;">Incorrecto: <em>Usar voz pasiva, si es posible</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze conecta a los consumidores con las marcas que aman.</td><td style="width: 50%;">Los consumidores son conectados con las marcas que aman.</td></tr>
<tr><td style="width: 50%;">Braze requiere que los empleados mantengan sus direcciones actualizadas.</td><td style="width: 50%;">Se requiere que los empleados mantengan sus direcciones actualizadas.</td></tr>
<tr><td style="width: 50%;">Los administradores de la empresa pueden configurar los requisitos de autenticación para iniciar sesión en Braze.</td><td style="width: 50%;">Los requisitos de autenticación para iniciar sesión en Braze pueden ser configurados por los administradores de la empresa.</td></tr>
</tbody>
</table>
{:/}

##### Excepciones

Está bien usar la voz pasiva en los siguientes casos:

* Para restar énfasis a un sujeto, generalmente para evitar culpar al lector:
  - **Correcto:** Se encontraron dos errores en el correo electrónico.
  - **Incorrecto:** Creaste dos errores en el correo electrónico.
* Si saber quién es responsable de la acción no es importante:
  - **Correcto:** Este artículo se actualizó por última vez en diciembre de 2020.

#### Artículos {#articles}

Usa los artículos "un", "una" y "el/la" para hacer tu redacción clara y ayudar en la traducción. Usa "el/la" antes de un sustantivo singular o plural específico, y "un" o "una" antes de un sustantivo singular no específico.

Para determinar si debes usar "un" o "una", mira el género del sustantivo que sigue. Las mismas directrices aplican a las [abreviaturas](#abbreviations).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa artículos según el género del sustantivo.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">una hora</td></tr>
<tr><td style="width: 100%;">un minuto</td></tr>
<tr><td style="width: 100%;">un artículo de preguntas frecuentes</td></tr>
<tr><td style="width: 100%;">un curso LAB</td></tr>
</tbody>
</table>
{:/}

#### Pronombres {#pronouns}

##### Pronombres personales

Usa pronombres de segunda persona (tú) siempre que sea posible.

No te refieras a los clientes de Braze como el "usuario" en redacción externa; en su lugar, habla directamente al lector usando "tú". Para referirte a los clientes de nuestros clientes, usa "tus consumidores" o, si la situación se relaciona con estadísticas de usuarios, "tus usuarios".

Evita los pronombres de primera persona (yo, nosotros, nuestro) excepto en los siguientes casos:

* Entradas en preguntas frecuentes. Por ejemplo, "¿Cómo restablezco mi contraseña?".
* Usar "nosotros" para referirse a Braze como organización.
 * Si puede no estar claro a quién se refiere "nosotros", primero refiere a Braze por nombre, luego usa "nosotros" en menciones posteriores.

##### Pronombres de género neutro

Usa los pronombres que usan tus sujetos. Si hay alguna incertidumbre, usa "ellos", "ellas" y "su" para pronombres singulares. No uses "él/ella" como alternativa al singular "ellos".

Solo usa pronombres con género (él/ella, su) si la persona a la que te refieres es realmente de ese género.

##### Pronombres ambiguos {#ambiguous-pronouns}

Los pronombres sustituyen a los sustantivos. La palabra a la que un pronombre se refiere se llama su antecedente. Al escribir instrucciones o material de aprendizaje, asegúrate de hacer referencias claras entre un pronombre y su antecedente. Esto puede requerir repetir sujetos para que el significado sea claro.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Asegúrate de que un pronombre haga referencia clara a su antecedente</em></th><th style="width: 50%;">Incorrecto: <em>Usar referencias pronominales ambiguas</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Si escribes texto en el campo, el texto no cambia.</td><td style="width: 50%;">Si escribes texto en el campo, no cambia.</td></tr>
<tr><td style="width: 50%;">Le dijo a Sara que la respuesta de Sara era incorrecta.</td><td style="width: 50%;">Le dijo a Sara que su respuesta era incorrecta.</td></tr>
<tr><td style="width: 50%;">No puedes editar una campaña archivada. Desarchiva una campaña para editarla.</td><td style="width: 50%;">No puedes editar una campaña archivada. Desarchívala para editarla.</td></tr>
</tbody>
</table>
{:/}

##### Pronombres opcionales

Para agregar claridad adicional a tu redacción y ayudar en la localización, usa pronombres como "que", "el cual" y "quien".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa "que", "el cual" y "quien" para agregar claridad adicional.</em></th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Haz clic derecho en el enlace que quieres abrir.</td><td style="width: 50%;">Haz clic derecho en el enlace quieres abrir.</td></tr>
<tr><td style="width: 50%;">Desde aquí, puedes elegir qué cohorte de Tinyclues quieres incluir.</td><td style="width: 50%;">Desde aquí, puedes elegir una cohorte de Tinyclues quieres incluir.</td></tr>
</tbody>
</table>
{:/}

#### Capitalización {#capitalization}

Evita la capitalización innecesaria. En la mayoría de los casos, usa capitalización de oración. La capitalización de título solo debe usarse para nombres propios o nombres de funciones.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa minúsculas para escribir URLs de sitios web y direcciones de correo electrónico</em></th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa minúsculas para direcciones cardinales</em></th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">norte, sur, este, oeste</td><td style="width: 50%;">Norte, Sur, Este, Oeste</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Capitaliza regiones específicas, y usa mayúsculas para regiones abreviadas</em></th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">el Noroeste</td><td style="width: 50%;">el noroeste</td></tr>
<tr><td style="width: 50%;">el sur de Connecticut</td><td style="width: 50%;">el Sur de Connecticut</td></tr>
<tr><td style="width: 50%;">Europa del Este</td><td style="width: 50%;">europa del este</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### Marcas y productos

Al referirte a una marca o producto, usa la capitalización que usa la marca. En la mayoría de los casos, capitaliza los nombres de marcas (Grindr, Walmart) y productos (Benchmarks, Looker Blocks). Está bien comenzar una oración con minúscula si la primera palabra es el nombre estilizado de una marca como eBay o iTunes.

Para intercaps, siempre refiere al uso preferido por la marca en texto impreso (OkCupid, YouTube). No uses intercaps que solo aparecen en logotipos o tratamientos de diseño gráfico (Amazon).

#### Orden de cláusulas {#clause-order}

Si quieres decirle al lector que haga algo en una circunstancia específica, intenta mencionar la circunstancia antes de proporcionar la instrucción. Esto permite al lector omitir la instrucción si la circunstancia no aplica.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Para pasos de solución de problemas, consulta las preguntas frecuentes de Campañas.</td><td style="width: 50%;">Consulta las preguntas frecuentes de Campañas para pasos de solución de problemas.</td></tr>
<tr><td style="width: 50%;">Para archivar tu campaña, haz clic en el ícono de engranaje y selecciona Archivar.</td><td style="width: 50%;">Haz clic en el ícono de engranaje y selecciona Archivar para archivar tu campaña.</td></tr>
</tbody>
</table>
{:/}

#### Formas combinadas {#combining-forms}

[Usa guion](#hyphens) en las formas combinadas cuando la frase se usa como adjetivo antes del sustantivo.

**Ejemplo:** Un artículo único en su tipo

#### Contracciones {#contractions}

Una contracción es una versión acortada de una palabra o frase. Usa contracciones para mantener un tono accesible e informal. Sin embargo, no uses contracciones de sustantivo y verbo ni contracciones dobles, o una combinación de dos contracciones. Estas pueden interrumpir el flujo y la coherencia de la oración.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa contracciones</em></th><th style="width: 50%;">Incorrecto: <em>Usar contracciones de sustantivo y verbo</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Si eres administrador, puedes gestionar la información de contacto de tu empresa.</td><td style="width: 50%;">Braze ahora soportará la integración con Shoptify.</td></tr>
<tr><td style="width: 50%;">No puedes editar una campaña archivada.</td><td style="width: 50%;">Puede que no hayas visto el tamaño de carga restringido.</td></tr>
</tbody>
</table>
{:/}

#### Modificadores colgantes y mal colocados {#dangling-and-misplaced-modifiers}

Los modificadores son palabras o frases que modifican otras palabras o frases. Un modificador colgante no modifica ningún sujeto en la oración. Un modificador mal colocado está ubicado lejos del sujeto que pretende modificar. Esencialmente, los modificadores colgantes y mal colocados pueden causar confusión al conectarse con la parte incorrecta de la oración.

Escribir con voz activa ayuda a prevenir el uso de modificadores colgantes y mal colocados. Asegúrate de usar un modificador que modifique claramente.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Mantén las oraciones cortas y concisas. Usa voz activa.</em></th><th style="width: 50%;">Incorrecto: <em>Usar oraciones largas con modificadores que pueden causar confusión</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Los clientes deben configurar sus ajustes de SAML.</td><td style="width: 50%;">Puede que tengas mensajes de prueba en tus campañas que se pueden eliminar.</td></tr>
<tr><td style="width: 50%;">Asegúrate de guardar los borradores de tu campaña.</td><td style="width: 50%;">De camino a casa, Sara encontró un reloj de bolsillo de oro de hombre.</td></tr>
</tbody>
</table>
{:/}

#### Preposiciones {#prepositions}

No hay nada malo en terminar una oración con una preposición cuando mejora la legibilidad. Coloca una preposición o frase preposicional donde tenga más sentido en una oración. Si tienes dificultades, lee la oración en voz alta y ve si suena natural.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cada opción corresponde a la prioridad en la que aparece la notificación.</td><td style="width: 50%;">Cada opción corresponde a la prioridad en la cual la notificación aparece.</td></tr>
<tr><td style="width: 50%;">Para más detalles, consulta la documentación del SDK para la plataforma con la que estás trabajando.</td><td style="width: 50%;">Para más detalles, consulta la documentación del SDK para la plataforma con la cual estás trabajando.</td></tr>
</tbody>
</table>
{:/}

#### Tiempo presente {#present-tense}

Usa el tiempo presente en lugar del tiempo futuro. El tiempo presente transmite inmediatez y demuestra confianza. Evita usar "será" o el hipotético "sería", especialmente al referirte al resultado de una acción del usuario.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Los grupos de suscripción archivados no se pueden editar y ya no aparecen en los filtros de segmento.</td><td style="width: 50%;">Los grupos de suscripción archivados no se pueden editar y ya no aparecerán en los filtros de segmento.</td></tr>
<tr><td style="width: 50%;">Usar un código abreviado es el tipo de número más confiable para incluir enlaces.</td><td style="width: 50%;">Usar un código abreviado sería el tipo de número más confiable para incluir enlaces.</td></tr>
</tbody>
</table>
{:/}

Solo usa el tiempo futuro cuando realmente estés hablando del futuro. Evita predecir [funciones futuras](#describing-limitations).

#### Lenguaje soez {#profanity}

Mantén el contenido apto para todos los públicos. Esto tiene menos que ver con la moralidad que con el hecho de que el lenguaje soez puede ser divisivo y desagradable para una audiencia tan amplia e internacional como la nuestra. También se puede argumentar que a veces el lenguaje soez es una cobertura para una redacción a medio hacer. Eso simplemente no es nuestro estilo.

#### Plurales entre paréntesis {#plurals-in-parentheses}

No uses plurales entre paréntesis. En su lugar, usa la forma plural o singular de la palabra.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Personaliza tu campaña con los siguientes filtros.</td><td style="width: 50%;">Personaliza tu campaña con el/los siguiente(s) filtro(s).</td></tr>
</tbody>
</table>
{:/}

#### Segunda persona y primera persona {#second-person-and-first-person}

Usa la segunda persona en tus instrucciones en lugar de la primera persona: "tú" en lugar de "nosotros".

Refiere al lector como quien realiza la acción. Establece un tono conversacional: la mayoría de los lectores acuden a la documentación cuando no tienen acceso inmediato a un agente de soporte. Haz que se sienta como si el artículo les estuviera hablando directamente.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Si quieres agregar una variante...</td><td style="width: 50%;">Si queremos agregar una variante...</td></tr>
</tbody>
</table>
{:/}

Si le estás diciendo al lector que haga algo, puedes omitir el "tú" y usar el imperativo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sube el archivo CSV.</td><td style="width: 50%;">Puedes subir el archivo CSV.</td></tr>
<tr><td style="width: 50%;">Selecciona Enviar.</td><td style="width: 50%;">Necesitarás seleccionar Enviar.</td></tr>
</tbody>
</table>
{:/}

Al usar la segunda persona, asegúrate de saber quién es la audiencia del documento y sé consistente sobre a quién le estás hablando.

#### Jerga y expresiones idiomáticas {#slang-and-idioms}

Somos un grupo que habla claro. Evita usar jerga de moda o expresiones idiomáticas que hablen demasiado específicamente a una audiencia singular. También puede fechar rápidamente los materiales y dificultar la localización del contenido.

#### Ortografía {#spelling}

Usa la ortografía del inglés americano para palabras que difieren en inglés británico. Si no estás seguro de cómo se escribe una palabra, primero consulta el [glosario](#glossary). Si la palabra no está listada allí, consulta el [Merriam-Webster's Collegiate Dictionary](https://www.merriam-webster.com/).

Para palabras que llevan acento o contienen caracteres especiales, asegúrate de seguir correctamente la ortografía del diccionario. En algunos casos, omitir involuntariamente estos acentos puede resultar en una palabra diferente. Por ejemplo, "resume" significa comenzar de nuevo después de detenerse, mientras que "résumé" es un relato de las cualificaciones de alguien.

### Puntuación {#punctuation}

#### Ampersands {#ampersands}

No uses un ampersand (&) en lugar de "y" en texto o encabezados a menos que te refieras directamente a la interfaz de usuario.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Editor de arrastrar y soltar</td><td style="width: 50%;">Editor de arrastrar & soltar</td></tr>
<tr><td style="width: 50%;">SMS y MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### Apóstrofos {#apostrophes}

Usamos un apóstrofo más frecuentemente para hacer posesivo un sustantivo.

* Para sustantivos singulares que terminan en S, está bien colocar otra S después del apóstrofo.
 * **Ejemplo:** de Chris, del negocio, del alias
* Para sustantivos plurales que terminan en S, agrega un apóstrofo pero no una S adicional.
 * **Ejemplo:** de los usuarios

#### Dos puntos {#colons}

Usa dos puntos al final de una frase introductoria que precede a una lista o ejemplo. Tu oración introductoria debe poder sostenerse por sí sola como una oración completa. Esto es tanto por accesibilidad como por localización, ya que es difícil traducir fragmentos de oraciones.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">La estructura general es la siguiente:</td><td style="width: 50%;">La estructura general es:</td></tr>
</tbody>
</table>
{:/}

Si el texto que precede a los dos puntos está en negrita, pon los dos puntos en negrita también.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Planificada:</strong> Entrada basada en tiempo.</td><td style="width: 50%;"><strong>Planificada</strong>: Entrada basada en tiempo.</td></tr>
</tbody>
</table>
{:/}

Si el texto que precede a los dos puntos es texto de código, no incluyas los dos puntos en el texto de código a menos que sea parte del elemento de código.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code>: Una etiqueta común para agrupar alias de usuario.</td><td style="width: 50%;"><code>user_alias_label:</code> Una etiqueta común para agrupar alias de usuario.</td></tr>
</tbody>
</table>
{:/}

También puedes usar dos puntos para unir dos frases relacionadas en una oración. Sin embargo, usa los dos puntos para esto con moderación. Dos oraciones son generalmente más legibles.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">La próxima semana: haremos un recorrido por el West Village.</td></tr>
</tbody>
</table>
{:/}


#### Comas {#commas}

Braze usa la coma de Oxford (serial) al escribir instrucciones o contenido de aprendizaje. Usa una coma antes de la última conjunción para separar elementos en una serie.

Usa una coma después de una frase introductoria.

Si una conjunción coordinante (palabras como "y", "pero", "o", "sin embargo", "así que") separa dos cláusulas independientes, coloca la coma después de la primera cláusula y antes de la conjunción. Sin embargo, esta coma no es necesaria si ambas cláusulas son cortas.

Por ejemplo, aquí hay dos cláusulas independientes:

* "Todos los campos son opcionales."
* "Debes especificar al menos un campo."

La oración al usar una conjunción coordinante "pero" es "Todos los campos son opcionales, pero debes especificar al menos un campo."

Si una cláusula independiente y una cláusula dependiente se usan en la misma oración, no uses una coma para separarlas. Solo usa una coma en este escenario si la oración puede malinterpretarse sin la coma.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Los estados de suscripción push son filtros y pueden permitir a los usuarios editar las preferencias de notificación.</td><td style="width: 50%;">Los estados de suscripción push son filtros, y pueden permitir a los usuarios editar las preferencias de notificación.</td></tr>
</tbody>
</table>
{:/}

#### Guiones {#dashes}

##### Raya

Usa una raya (—) cuando uses un guion en una oración para indicar un pensamiento separado o una interrupción. No pongas espacios antes o después de la raya. No uses una raya donde una coma o paréntesis funcionaría igual de bien.

Consulta tu sistema operativo para saber cómo escribir una raya:

* **macOS:** Presiona Option + Shift + Guion.
* **Windows:** Activa el bloqueo numérico, luego mantén presionada la tecla Alt izquierda y escribe 0151 en el teclado numérico.

##### Semirraya {#en-dash}

Usa una semirraya (–) para indicar un rango de números, como signo de menos o para indicar números negativos. No pongas espacios antes o después de la semirraya excepto cuando se usa como signo de menos. No uses un guion (-).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa una semirraya para un rango de números</em></th><th style="width: 50%;">Incorrecto: <em>Usar un guion</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

No uses una semirraya para rangos de tiempo. Para más detalles, consulta la sección [Fechas y horas](#dates-and-times).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa una semirraya como signo de menos e incluye espacios alrededor de la semirraya</em></th><th style="width: 50%;">Incorrecto: <em>Usar un guion</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa una semirraya para números negativos</em></th><th style="width: 50%;">Incorrecto: <em>Usar un guion</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

Consulta tu sistema operativo para saber cómo escribir una semirraya:

* **macOS:** Presiona Option + Guion.
* **Windows:** Activa el bloqueo numérico, luego mantén presionada la tecla Alt izquierda y escribe 0150 en el teclado numérico.

#### Puntos suspensivos {#ellipses}

Los puntos suspensivos son una serie de tres puntos (...) que indican la omisión de una o más palabras. En general, evita usar puntos suspensivos cuando sea posible al escribir instrucciones o contenido de aprendizaje.

#### Signos de exclamación {#exclamation-points}

Un signo de exclamación puede usarse con moderación para un tono informal. Sin embargo, evita usar signos de exclamación en exceso a lo largo del texto. En su lugar, considera usar [alertas](#callouts-and-alerts).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa signos de exclamación para un tono informal en recordatorios e introducciones</em></th><th style="width: 50%;">Incorrecto: <em>Usar signos de exclamación para indicar advertencia o precaución a los lectores</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">¡Asegúrate de guardar tus cambios antes de salir de la página!</td><td style="width: 50%;">¡Los usuarios deben recibir uno o más mensajes de un paso para ser contados como destinatario único!</td></tr>
</tbody>
</table>
{:/}

#### Guiones {#hyphens}

Los guiones pueden ayudar al lector a obtener más claridad en una oración al vincular palabras en una frase. Aquí hay algunas directrices para hacerlo correctamente.

Usa guiones para modificadores compuestos que ayuden al lector a entender el sujeto más claramente.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">transmisión de datos en tiempo real</td></tr>
</tbody>
</table>
{:/}

Usa guiones para vincular una frase, con un espacio entre el modificador y el sujeto.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Soluciones todo en uno</td></tr>
</tbody>
</table>
{:/}

Usa guiones para una frase que modifica un sujeto. No es necesario usar un guion si la frase es el sujeto.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Era un hecho bien conocido.</td><td style="width: 50%;">Ese hecho es bien-conocido</td></tr>
</tbody>
</table>
{:/}

No uses guiones en lugar de una raya para crear una pausa en una oración.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...integraciones de terceros—como Slack—y automatizar...</td><td style="width: 50%;">...integraciones de terceros-como Slack-y automatizar...</td></tr>
</tbody>
</table>
{:/}

No uses un guion después de un adverbio. Mantén las palabras separadas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Hecho apresuradamente</td><td style="width: 50%;">Hecho-apresuradamente</td></tr>
</tbody>
</table>
{:/}

#### Paréntesis {#parentheses}

Usa paréntesis con moderación. Nunca pongas información importante entre paréntesis, ya que algunos lectores omiten el contenido entre paréntesis.

Para paréntesis menos importantes, considera reformular la oración para eliminar los paréntesis. Por ejemplo, puedes separar la frase u oración usando comas, guiones, punto y coma o agregando una nueva oración.

Si un paréntesis es parte de una oración más grande, coloca el punto fuera del paréntesis. Si el paréntesis contiene una oración completa, coloca el punto dentro.

**Sección relacionada:** [Plurales entre paréntesis](#plurals-in-parentheses)

#### Puntos {#periods}

Usa un punto para terminar oraciones. No uses un punto para terminar titulares, encabezados, subtítulos o elementos de la interfaz.

Para directrices sobre cuándo usar puntos con elementos de lista, consulta [Listas](#lists).

#### Punto y coma {#semicolons}

Los punto y coma son excelentes para dividir una oración más larga y complicada. Usa un punto y coma para separar dos cláusulas independientes que están estrechamente relacionadas en tema.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa un punto y coma para dividir una oración con dos cláusulas independientes relacionadas</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">El gato durmió durante la tormenta; el perro se escondió debajo de la cama.</td></tr>
</tbody>
</table>
{:/}

Los punto y coma pueden usarse para separar elementos de lista si uno (o más) de los elementos contiene una coma.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa un punto y coma para dividir una oración más larga</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, nuestra moderadora; Simon Mayer, CEO y cofundador de PantsLabyrinth; y Kara Seberg, CMO de Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### Barras {#slashes}

Hay dos tipos de barras: invertida (\\) y diagonal (/). No uses barras para indicar palabras o ejemplos alternativos ("y/o").

Usa barras según sea necesario en rutas de archivos y URLs.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa una barra para rutas de archivos</em></th><th style="width: 50%;">Incorrecto: <em>Usar una barra para separar alternativas</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">tú/tus clientes</td></tr>
</tbody>
</table>
{:/}

#### Comillas {#quotation-marks}

Hay dos tipos de comillas: rectas (" ") y curvas (" "). Los puntos y las comas van dentro de las comillas. Una excepción es cuando las comillas incluyen información exacta como una cadena de texto. Usa comillas cuando dirijas a los usuarios a ingresar una cadena de texto específica en un campo de texto.

{% alert note %}

Al describir la sintaxis de búsqueda, las comillas se usan frecuentemente para indicar la búsqueda de texto exacto. En este caso, usa corchetes alrededor de la cadena de texto y comillas según lo requiera la sintaxis de búsqueda. Por ejemplo: <br><br>

*Pon comillas alrededor de cualquier palabra o frase, como ["segmento de prueba"], y mostramos resultados que contienen solo esas palabras o frases exactas.*

{% endalert %}

Los ejemplos de código deben usar comillas rectas. Para más información sobre el formato de código en texto, consulta [Código en texto](#code-in-text).

### Documentación técnica {#technical-documentation}

#### Puntos finales de API {#api-endpoints}

En general, la documentación para puntos finales de API debe seguir las directrices de esta guía de estilo. Sin embargo, hay temas específicos que pueden requerir directrices de contenido diferentes listadas en este documento. Para más información sobre cómo formatear y referenciar puntos finales, consulta las [directrices de documentación de puntos finales de API]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

#### Evita garantías {#avoid-guarantees}

Nuestra documentación debe abstenerse de hacer compromisos que puedan resultar en implicaciones legales. Evita usar términos definitivos como "garantizar" o "asegurar". En su lugar, emplea declaraciones prospectivas como "Diseñado para" o "Con la intención de" para transmitir con precisión las capacidades e intenciones del producto.

#### Describir interacciones con la interfaz {#describing-interactions-with-the-ui}

Al referirte a elementos de la interfaz, usa la misma capitalización que aparece en la interfaz. Sin embargo, si una etiqueta está toda en mayúsculas, usa capitalización de oración (excepción: etiquetas cortas, como los operadores AND u OR).

Al instruir a un lector para que interactúe con la interfaz, pon en negrita el elemento de la interfaz con el que está interactuando. Para cadenas que un usuario ingresaría en un campo, usa comillas.

Para orientación sobre qué verbos usar al describir interacciones con la interfaz, consulta la siguiente tabla:

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>Verbo</th><th>Uso</th><th>Ejemplo</th></tr>
</thead>
<tbody>
<tr><td>Abrir</td><td><ul><li>Abrir aplicaciones</li><li>Abrir archivos y carpetas</li></ul></td><td><ul><li>Abre Droidboy.</li><li>Abre el archivo braze.xml.</li></ul></td></tr>
<tr><td>Cerrar</td><td><ul><li>Cerrar aplicaciones</li><li>Cerrar archivos y carpetas</li></ul></td><td><ul><li>Cierra Droidboy.</li><li>Cierra el archivo braze.xml.</li></ul></td></tr>
<tr><td>Ir a</td><td><ul><li>Ir a una página específica en la interfaz (pestaña, página, sección)</li><li>Ir a una página web</li></ul></td><td><ul><li>Ve a la página <strong>Segments</strong> y haz clic en…</li><li>Ve a example.com para registrarte.</li></ul></td></tr>
<tr><td>&gt;</td><td>Seguir una secuencia de pasos cuando todos los pasos son del mismo tipo.</td><td>Ve a <strong>Segments</strong> &gt; <strong>Segment Insights</strong>.</td></tr>
<tr><td>Elegir</td><td>Tomar una decisión que es subjetiva, estratégica, abierta o compleja.</td><td>Elige una estrategia de campaña.</td></tr>
<tr><td>Seleccionar</td><td><ul><li>Seleccionar una casilla de verificación</li><li>Seleccionar elementos de un menú desplegable</li><li>Seleccionar una pestaña</li><li>Tomar una decisión simple</li></ul></td><td><ul><li>Selecciona <strong>Show Password</strong>.</li><li>Selecciona un tipo de datos del menú desplegable.</li><li>En la página <strong>Manage Settings</strong>, selecciona la pestaña <strong>Custom Events</strong>.</li><li>Selecciona una imagen.</li></ul></td></tr>
<tr><td>Desmarcar</td><td>Desmarcar la selección de una casilla de verificación.</td><td>Desmarca la casilla de verificación <strong>Show Password</strong>.</td></tr>
<tr><td>Seleccionar</td><td>Seleccionar un elemento en la interfaz.</td><td>Agrega un atributo personalizado y selecciona <strong>Save</strong>.</td></tr>
<tr><td>Activar</td><td>Habilitar una opción de alternancia</td><td>Activa el <strong>List-Unsubscribe header</strong>.</td></tr>
<tr><td>Desactivar</td><td>Deshabilitar una opción de alternancia</td><td>Desactiva <strong>Inline CSS on New Emails by Default</strong>.</td></tr>
<tr><td>Ingresar</td><td>Escribir un valor.</td><td><ul><li>En el campo de texto, ingresa el nombre de tu atributo personalizado.</li><li>Ingresa "Braze" como el nombre de la fuente.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### Describir limitaciones {#describing-limitations}

Escribe con franqueza sobre las limitaciones del producto, sin distorsión ni manipulación. Los lectores reaccionan intensamente cuando se sienten manipulados o engañados, y esto pone en peligro la eficacia de la documentación como fuente de verdad utilitaria. Los clientes dependen de la documentación para entender los límites del sistema sobre el que están construyendo para poder usar Braze con éxito.

Al mismo tiempo, apoya la intencionalidad del desarrollo del producto enmarcando las limitaciones con un contexto positivo apropiado.

* Si hay una limitación flexible (por ejemplo, un límite de velocidad de API), enmarca la limitación hablando del **límite predeterminado** o la **asignación inicial.**
* Proporciona un camino significativo para navegar las limitaciones flexibles. Proporciona ejemplos de estas soluciones alternativas según corresponda.
 * Por ejemplo, Braze usa ejercicios de dimensionamiento durante la incorporación para ayudar a los clientes a entender cómo cosas como los puntos de datos son usados por otros negocios de tamaño similar. Al hablar de puntos de datos, es apropiado hablar del ejercicio de dimensionamiento al mismo tiempo.
* Es mejor describir un camino a seguir de manera positiva que como una mitigación.
 * Por ejemplo, en lugar de decir "Braze no permite que los clientes hagan esto por su cuenta. El equipo de soporte debe activar esta función por ti", di "Para activar esta función, contacta al equipo de soporte."
* No dependas excesivamente de las mismas frases estándar para navegar las limitaciones flexibles. Si un usuario lee "Habla con tu representante de servicio al cliente" una y otra vez, el consejo pierde significado.
* Si hay una limitación estricta, intenta describir la razón detrás de este límite.
 * Por ejemplo: "Hay un límite de 200 campañas activas de mensajes dentro de la aplicación basadas en acciones por grupo de aplicaciones para optimizar la velocidad de entrega de mensajes y prevenir tiempos de espera. …El cliente promedio de Braze tiene un total de 26 campañas activas a la vez, así que es poco probable que esta limitación te afecte."
* No describas [funcionalidad planificada o funciones futuras](#future-features) como una forma de explicar las limitaciones actuales.
* Al referirte a límites de datos personalizados, usa el término "capacidad" en lugar de límites.
 * Por ejemplo: De forma predeterminada, puedes tener 20 propiedades de evento segmentables por espacio de trabajo. Contacta a tu director de cuentas de Braze para aumentar tu capacidad.

#### Funciones futuras {#future-features}

Evita referencias a funciones futuras o sugerencias de que algo pueda ser soportado en el futuro.

No uses palabras y frases que anclen tu redacción a un punto en el tiempo, ya que hacen que el contenido quede desactualizado rápidamente. Céntrate en cómo funciona el producto ahora, no en lo que ha cambiado (excepto para contenido enfocado en el tiempo, como en las notas de la versión).

Específicamente evita la siguiente lista de palabras y frases, tomada de la [guía de estilo de documentación para desarrolladores](https://developers.google.com/style/timeless-documentation) de Google:

* al momento de escribir esto
* actualmente
* aún no
* eventualmente
* futuro, en el futuro
* más reciente
* nuevo, más nuevo
* ahora
* viejo, más viejo
* actualmente, en la actualidad
* pronto

#### Deprecación de funciones {#features-deprecations}

Antes de incluir información sobre deprecaciones de funciones, asegúrate de tener un marco de tiempo general de cuándo los lectores pueden esperar que la función sea deprecada (por ejemplo, finales de 2025).

Después de tener un marco de tiempo general, comunica la deprecación de la función con anticipación. Sé claro al escribir sobre deprecaciones para que los lectores puedan entender claramente qué esperar.

No uses frases que puedan generar miedo, incertidumbre o duda en los lectores. Proporciona un camino claro a seguir, como por qué se reemplaza la función deprecada o una solución alternativa.

#### General versus específico {#general-vs-specific}

Como mejor práctica, escribe artículos que discutan la funcionalidad de una manera generalmente aplicable. Si se necesita más detalle para casos específicos o excepciones, crea una sección separada (o un artículo separado si el contenido tiene la extensión de un artículo web, ~500 palabras) que describa este caso atípico. Crea referencias cruzadas del artículo general al específico para ayudar a los usuarios a conectar estos conceptos.

Evita crear contenido duplicado o repetitivo para diferentes canales o funciones. Si se necesita repetición, usa archivos `includes` y otras [mejores prácticas de contenido reutilizable]({{site.baseurl}}/contributing/content_management/reusing_content).

**Como ejemplo:** Un caso de uso común para los clientes de Braze es volver a dirigirse a usuarios que previamente han interactuado con su mensajería. Volver a dirigirse a usuarios puede hacerse a través de muchas herramientas de interacción, incluyendo campañas, Canvas, páginas de inicio y segmentos. Volver a dirigirse a usuarios puede hacerse a través de muchos canales: WhatsApp, SMS, Tarjetas de contenido, correo electrónico, notificaciones push y más. A menudo, los clientes intentan reactivar la interacción con un usuario a través de un canal diferente al usado previamente.
En lugar de crear un artículo para cada herramienta de interacción y cada canal, crea un solo artículo que discuta estrategias para volver a dirigirse a usuarios y describa todas las opciones disponibles. Si hay consideraciones especiales para canales/herramientas específicos, crea un artículo separado que describa esas consideraciones y ubícalo dentro de esa sección de documentación. Crea referencias cruzadas entre el artículo general y el artículo específico.

#### Metadatos y YAML {#metadata-and-yaml}

Los artículos en la documentación de Braze requieren ciertos metadatos para fines de búsqueda e indexación. Para información sobre qué metadatos son necesarios, consulta la página de GitHub sobre [YAML y diseños de metadatos](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Convenciones de nomenclatura {#naming-conventions}

Al nombrar artículos y nombres de archivo, asegúrate de describir el tema general en el título. Siempre incluye una palabra clave y una descripción breve que los lectores entiendan fácilmente, especialmente con los títulos de artículos.

Para nombres de archivo, mantén el nombre breve y evita usar artículos (un, una, el, la). Separa cada palabra con un guion bajo (_).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Dirigirse a usuarios</td></tr>
<tr><td style="width: 100%;">Crear una campaña de correo electrónico</td></tr>
<tr><td style="width: 100%;">Errores y respuestas de API</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

En general, para artículos y archivos de imagen, usa la misma ortografía y capitalización que el artículo y los archivos referenciados. Para directrices sobre el estilo de títulos de artículos, consulta [Encabezados y títulos](#headings-and-titles).

Al referirte a un archivo específico, usa la misma ortografía del nombre de archivo y fuente de código. Para detalles de formato, consulta la página de GitHub sobre [Formato especial](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting).

#### Procedimientos e instrucciones {#procedures-and-instructions}

Esta sección cubre algunas directrices a tener en cuenta al escribir instrucciones para procedimientos en el dashboard de Braze.

Directrices generales:

* **Usa el tono correcto.** Para instrucciones, mantén tu redacción corta, directa y orientada a tareas. Tu redacción no necesita ser seca o escueta, pero debe ser directa. Al introducir tareas o subtareas, puedes usar un tono más informal para agregar variedad. Evita usar "por favor" para mantener el tono informal. Usa contracciones generosamente para mantener tu tono accesible.
* **Sigue un formato de encabezado paralelo.** Elige un formato para tus encabezados y mantenlo. Mantén tu contenido escaneable y predecible. Para encabezados basados en tareas y títulos de página, prefiere verbos imperativos (por ejemplo, "Crear una campaña de correo electrónico").

Antes de las instrucciones:

* **Usa introducciones y requisitos previos.** No saltes directamente a los pasos. En su lugar, da contexto sobre lo que cubre tu artículo o sección, y proporciona cualquier información que el lector necesite saber antes de escanear las instrucciones. Asegúrate de que los requisitos previos estén listados en la parte superior del artículo con el encabezado "Requisitos previos". Los encabezados de tabla en esta sección deben decir "Requisitos". "Requisitos" es un término aceptable para indicar un requisito de Braze, un proveedor externo o un socio.
* **Comienza al principio del procedimiento.** No asumas que el lector ha llegado a esta página después de completar un paso anterior. Si las instrucciones para una tarea continúan donde otra terminó, da una descripción general de dónde se encuentra el lector en el procedimiento y qué debe completar antes de este paso. Incluye enlaces a cualquier paso anterior.

Escribir instrucciones:

* **Usa lenguaje accionable.** Estructura la documentación en torno a lo que el usuario puede hacer, no lo que el producto puede hacer. Evita lenguaje como "Esta función [hace xyz]". En su lugar, piensa en términos de "Usa esta función para [hacer xyz]".
* **Proporciona pasos de ubicación cuando sea necesario.** Asegúrate de que el lector esté mirando en el lugar correcto con frases breves como "En la página **Settings**, selecciona **Edit**." Si eso puede no ser suficientemente claro, proporciona un paso introductorio. Por ejemplo, "Ve a **Manage Settings** y selecciona la pestaña **Settings**."
* **Antepón las declaraciones condicionales**. Coloca las [cláusulas condicionales](#clause-order) primero. Para instrucciones condicionales, antepón el paso con "si" para que el lector sepa que puede omitir el paso si la condición no aplica. Por ejemplo, "Si necesitas X, entonces haz A > B > C."
* **Refuerza el orden de las tareas.** Para el progreso dentro de una serie de pasos, usa la frase "Cuando hayas" o "Después de haber". Para el progreso entre tareas, comienza una sección con "Ahora que has" o "Después de haber". Evita la frase "Una vez que hayas", ya que ese uso específico de "una vez" no se traduce bien.

#### Pestañas {#tabs}

Las pestañas pueden usarse en documentación técnica como una forma de organizar información agrupada.

Una pestaña se refiere a un elemento que puede usarse al escribir instrucciones para demostrar un resumen de flujo de trabajo o para organizar información agrupada. Esto es similar a una tabla o lista, pero la información se agrupa en paneles.

Considera usar pestañas cuando la información pueda agruparse para evitar duplicación o para visualizar un flujo de trabajo para los lectores. Asegúrate de que las pestañas incluyan información paralela y no se usen cuando el lector deba seguir pasos secuenciales en un flujo de trabajo.

Por ejemplo, puedes usar pestañas para mostrar ejemplos de código en diferentes lenguajes de programación. En este caso, un lector alternaría entre los ejemplos según las etiquetas de las pestañas en lugar de desplazarse por el artículo.

Para detalles de formato, consulta la página de GitHub sobre [Formato especial](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). Alternativamente, también puedes usar una [lista](#lists) o [tabla](#tables-1) para organizar información.

### Formato y organización {#formatting-and-organizing}

#### Direcciones {#addresses}

Usa el número seguido del nombre de la calle de la siguiente manera:

*330 W. 34th St.*

Para mostrar una dirección completa, usa el número, seguido del nombre de la calle, seguido de la ciudad, estado y código postal. No es necesaria una coma entre el estado y el código postal.

*330 W. 34th St., New York, NY 10001*

#### Etiquetas de botones {#buttons-labels}

Las etiquetas de botones deben ser claras y predecibles: el usuario debe saber qué acción ocurre al seleccionar el botón. Usa capitalización de oración para las etiquetas de botones y comienza con un verbo fuerte. Si puede no estar claro a qué se refiere el verbo, usa el formato [verbo] + [sustantivo].

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Registrarse</td><td style="width: 50%;">REGISTRARSE</td></tr>
<tr><td style="width: 50%;">Iniciar sesión</td><td style="width: 50%;">INICIAR SESIÓN</td></tr>
<tr><td style="width: 50%;">Suscribirse</td><td style="width: 50%;">SUSCRIBIRSE</td></tr>
<tr><td style="width: 50%;">Más información</td><td style="width: 50%;">Más</td></tr>
</tbody>
</table>
{:/}

Omite palabras y artículos innecesarios, como "un", "una" o "el/la".

#### Alertas y llamadas de atención {#callouts-and-alerts}

Las alertas, también conocidas como llamadas de atención, se usan para llamar la atención sobre información que es útil para el lector. Hay cuatro tipos de alertas que se usan en nuestra documentación:

* Importante
* Nota
* Consejo
* Advertencia

Usa alertas con moderación a lo largo de los artículos. Para más información, consulta las [mejores prácticas de alertas]({{site.baseurl}}/contributing/style_guide/alerts/).

#### Código en texto {#code-in-text}

Hay algunos escenarios donde debes usar fuente de código para formatear texto dentro de una oración. Aquí hay una lista incompleta de elementos que deben estar en fuente de código:

* Nombres y valores de atributos
* Parámetros de solicitud de API
* Nombres de archivo
* Rutas de archivo
* Nombres de métodos, variables o parámetros
* Nombres de elementos HTML y XML
* Códigos de estado HTTP
* Texto ingresado en una terminal

Para crear texto de código en línea en la documentación de Braze, rodea el texto con acentos graves (`).

#### Muestras de código {#code-samples}

Las muestras de código se refieren a bloques de texto de código que muestran un fragmento de código de ejemplo. Por razones de accesibilidad, introduce la muestra de código con una oración explicativa cuando sea posible.

Para asegurarte de que tus muestras de código sean legibles, indenta cada línea con dos espacios por nivel de indentación. Si tienes problemas para formatear tus muestras de código, intenta embellecer tu código usando un formateador de impresión bonita, como [JSON Formatter](https://jsonformatter.org/json-pretty-print).

Para crear bloques de código en la documentación de Braze, consulta [Prueba de fragmento de código](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test). Recuerda que los bloques de código deben especificar el tipo de lenguaje para asegurar el resaltado de sintaxis adecuado.

#### Fechas y horas {#dates-and-times}

Escribe el mes y los días de la semana completos. Evita abreviaturas cuando sea posible. Para instancias donde abreviar meses es necesario, solo abrevia los siguientes:

* ene.
* feb.
* ago.
* sept.
* oct.
* nov.
* dic.

Usa una [coma](#commas) para separar la fecha del año. Si se usa un día de la semana con la fecha, agrégalo antes del mes.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa el formato de fecha preferido.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">septiembre de 2021</td></tr>
<tr><td style="width: 100%;">15 de septiembre de 2021</td></tr>
<tr><td style="width: 100%;">miércoles, 15 de septiembre de 2021</td></tr>
</tbody>
</table>
{:/}

Para rangos de fechas, usa una [semirraya](#en-dash).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

Usa una semirraya para rangos de fechas.

Usa números con am o pm, seguidos de un espacio, seguido del momento del día (am o pm). Elimina los minutos de las horas en punto.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa números con am o pm.</em></th><th style="width: 50%;">Incorrecto: <em>Usar minutos para horas en punto (a menos que sea un rango).</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

Para rangos de tiempo, usa una semirraya para separar. No agregues espacios antes o después de la semirraya.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa una semirraya para rangos de tiempo.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–2:30 pm</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto: <em>Usa minutos para rangos de tiempo.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00 am–2:30 pm</td></tr>
</tbody>
</table>
{:/}

Para referencia en instancias donde se incluyen partes de otras zonas horarias (como seminarios web, reuniones o eventos), indica la zona horaria como se indica a continuación:

* Hora estándar del este: EST
* Hora estándar central: CST
* Hora estándar de montaña: MST
* Hora estándar del Pacífico: PST
* Hora del meridiano de Greenwich: GMT
* Tiempo universal coordinado: UTC
* Hora de Europa Central: CET
* Hora de Europa del Este: EET
* Hora de Europa Occidental: WET
* Hora de Singapur: SGT
* Hora estándar de China: CST

#### Emojis {#emojis}

Aunque somos un grupo informal, evita usar emojis en contenido de aprendizaje ya que pueden interpretarse de diferentes maneras y a menudo se perciben como poco profesionales.

Las excepciones incluyen los siguientes escenarios:

* Cuando se usan ✅ y ❌ en tablas para indicar contenido que es compatible versus no compatible, o recomendado versus no recomendado
* Cuando se usan en texto de ejemplo para un mensaje de campaña o Canvas

#### Nombres de ejemplo {#example-names}

Nunca uses nombres reales, direcciones de correo electrónico ni ninguna otra información de identificación personal (PII). En su lugar, usa ejemplos ficticios o [texto de marcador de posición](#placeholder-text).

Cuando necesites incluir nombres en tu redacción, consulta la lista de Wikipedia de [nombres unisex](https://en.wikipedia.org/wiki/Unisex_name). Usa los pronombres "ellos", "su" y "suyo" cuando sea posible, y evita usar ejemplos que estén limitados a un género específico.

##### Direcciones de correo electrónico de ejemplo

Usa el formato "nombre@example.com" para direcciones de correo electrónico genéricas. Reemplaza "nombre" con un nombre de ejemplo. Por ejemplo:

* alex@example.com
* lee@example.com
* yuri@example.com

#### Figuras y otras imágenes {#figures-and-other-images}

Al crear figuras e imágenes, consulta la [guía de estilo de imágenes]({{site.baseurl}}/contributing/style_guide/image_style_guide/). Nunca incluyas información de identificación personal (PII) en figuras o imágenes.

##### Texto alternativo {#alt-text}

Siempre incluye texto alternativo con las imágenes. Los lectores de pantalla anuncian el texto alternativo para explicar las imágenes a personas con pérdida de visión. Como tal, tu texto alternativo debe transmitir toda la información clave representada en la imagen.
Usa las siguientes directrices al escribir texto alternativo:

* Usa [lenguaje sencillo](https://www.plainlanguage.gov/guidelines/).
* Escribe en oraciones completas y usa capitalización de oración.
* Omite palabras innecesarias.
* No incluyas "imagen de" o "foto de". Ya se entiende que te refieres a una imagen.
* No incluyas caracteres especiales. Por ejemplo, en lugar de ampersands (&), usa la palabra "y" escrita.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Página de configuración de Eventos personalizados en el panel de Braze con Agregar informe resaltado.</td><td style="width: 50%;">Una captura de pantalla de la página Manage Settings > Custom Events en el panel de Braze con la opción de agregar un informe resaltada.</td></tr>
</tbody>
</table>
{:/}

Deja las etiquetas alt explícitamente vacías (alt="") si la imagen agrega un componente visual redundante a lo que se explica en el texto.

Agregar texto alternativo a cada imagen no hace automáticamente que el contenido de la página web sea fácil de navegar y consumir. Los elementos visuales redundantes son poderosos para los usuarios videntes porque la información visual es fácil de entender y recordar. Sin embargo, el texto alternativo que describe imágenes redundantes puede ser innecesario para los usuarios que no pueden ver la imagen porque cada elemento de la página demanda igual atención de los usuarios de lectores de pantalla para determinar si es útil para su tarea.

##### Nombres de empresas de ejemplo

Si es posible, toma capturas de pantalla de [dashboard-06](https://dashboard-06.braze.com/) para que estés usando uno de los nombres de empresa de FakeBrandz.

#### Tipos de archivo y nombres de archivo {#file-types-and-filenames}

Cuando te refieras a un tipo de archivo, usa el nombre estándar del tipo. Si el tipo de archivo es un acrónimo, refiere al tipo de archivo en mayúsculas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Usa el nombre estándar del tipo de archivo</em></th><th style="width: 50%;">Incorrecto: <em>Usar la extensión de archivo</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">archivo ejecutable</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">archivo Python</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">archivo Bash</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">archivo de texto</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

Cuando te refieras al nombre de un archivo, formatea el nombre del archivo como texto de código. Para más información, consulta la sección [Código en texto](#code-in-text).

Al nombrar archivos en la documentación de Braze, como archivos de artículos o imágenes, usa todo en minúsculas y separa las palabras con guiones bajos, no guiones. Para más información, consulta [Crear archivos y carpetas](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders) en GitHub.

#### Notas al pie {#footnotes}

Las notas al pie son anotaciones que proporcionan información adicional y generalmente se colocan al final de una página. Debido al formato de nuestro texto, las notas al pie no son óptimas para la mayoría de los casos de uso. Lo siguiente describe cuándo usar notas al pie versus otros métodos de atribución:

* Si estás presentando una lista de estadísticas u otra información densa que necesita ser atribuida a fuentes, usa notas al pie.
* Si estás presentando una o dos piezas de información, usa un enlace o una alerta.
* Si necesitas proporcionar información adicional a elementos en una tabla, usa un símbolo de asterisco (*) junto al elemento de la tabla y presenta la información después de la tabla.

#### Formato de texto en instrucciones {#formatting-text-in-instructions}

Usa formato de texto consistente para ayudar a los lectores a encontrar e interpretar información. Esta sección proporciona directrices sobre qué formato usar al describir o referirte a diferentes elementos de texto en tus instrucciones.

Esta sección cubre los siguientes elementos:

* [Botones](#buttons)
* [Casillas de verificación](#checkboxes)
* [Comandos y opciones de línea de comandos](#command-line-commands-and-options)
* [Cuadros de diálogo](#dialog-boxes-(modals))
* [Mensajes de error](#error-messages)
* [Nombres de filtros y operadores](#filter-and-operator-names)
* [Nombres de carpetas y archivos](#folder-and-filenames)
* [Nombres de teclas y combinaciones](#key-names-and-combinations)
* [Métricas](#metrics)
* [Páginas](#pages)
* [Nombres de permisos](#permission-names)
* [Pestañas](#tabs-1)
* [Entrada de texto](#text-input)

##### Botones {#buttons}

Al referirte a un botón, usa texto en negrita para la etiqueta del botón. En la mayoría de los casos, usa la misma capitalización de la interfaz. Para botones donde la etiqueta está toda en mayúsculas (excepto botones OK), usa capitalización de oración en su lugar.

Para referirte a un botón, usa solo la etiqueta del botón. No te refieras a un botón como "el botón [etiqueta]".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecciona <strong>Add Languages</strong>.</td><td style="width: 50%;">Selecciona el botón <strong>Add Languages</strong>. <br><br> Selecciona "Add Languages".</td></tr>
</tbody>
</table>
{:/}

Si la etiqueta termina con dos puntos o puntos suspensivos, omite la puntuación final.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecciona <strong>Save as</strong></td><td style="width: 50%;">Selecciona <strong>Save as…</strong></td></tr>
</tbody>
</table>
{:/}

Si un botón es un ícono, incluye el nombre del botón como se muestra en la información sobre herramientas. Si un botón con un ícono no incluye una información sobre herramientas, envía una solicitud para que se agregue una.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecciona ➕ <strong>Add</strong>.</td><td style="width: 50%;">Selecciona el ícono ➕.</td></tr>
</tbody>
</table>
{:/}

##### Casillas de verificación {#checkboxes}

Al referirte a una casilla de verificación, usa texto en negrita para la etiqueta de la casilla. No incluyas la palabra "casilla de verificación" a menos que se necesite claridad. Prefiere los términos "seleccionar/desmarcar" en lugar de "marcar/desmarcar".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecciona <strong>Send campaign to users in their local time zone</strong>.</td><td style="width: 50%;">Marca <strong>Send campaign to users in their local time zone</strong>.</td></tr>
<tr><td style="width: 50%;">Desmarca la casilla de verificación <strong>Exit</strong>.</td><td style="width: 50%;">Desmarca la casilla <strong>Exit</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Comandos y opciones de línea de comandos {#command-line-commands-and-options}

Al referirte a comandos u opciones de línea de comandos, usa formato de código. Usa la misma capitalización que aparece o como debe escribirse.

##### Cuadros de diálogo (modales) {#dialog-boxes-(modals)}

Evita referirte a los cuadros de diálogo por nombre a menos que se necesite claridad. En su lugar, describe lo que el lector necesita hacer. Si te refieres a un cuadro de diálogo, usa texto en negrita para el nombre del cuadro de diálogo y usa la misma capitalización de la interfaz.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecciona <strong>Upload</strong> y luego selecciona un archivo para subir.</td><td style="width: 50%;">Selecciona <strong>Upload</strong> y usa el cuadro de diálogo <strong>File Upload</strong> para seleccionar un archivo para subir.</td></tr>
</tbody>
</table>
{:/}

##### Mensajes de error {#error-messages}

Al referirte a mensajes de error que un lector puede encontrar, encapsula el mensaje de error entre comillas. Para mensajes de error más largos, usa una cita en bloque.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">"Push Bounced: MismatchSenderId"</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### Nombres de filtros y operadores {#filter-and-operator-names}

Al referirte a los nombres de filtros y operadores para segmentos u otras áreas del dashboard, usa texto de código. Usa la misma capitalización de la interfaz, incluyendo elementos que están en mayúsculas como los operadores `OR` y `AND`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecciona el filtro <code>First Used App</code> y…</td><td style="width: 50%;">Selecciona el filtro <strong>First Used App</strong> y…</td></tr>
<tr><td style="width: 50%;">Combina filtros con el operador <code>OR</code>.</td><td style="width: 50%;">Combina filtros con el operador "OR".</td></tr>
</tbody>
</table>
{:/}

##### Nombres de carpetas y archivos {#folder-and-filenames}

Al referirte a nombres de carpetas y archivos, usa texto de código.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Abre el archivo <code>braze.xml</code>.</td><td style="width: 50%;">Abre el archivo <strong>braze.xml</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Nombres de teclas y combinaciones {#key-names-and-combinations}

Al referirte a nombres de teclas o combinaciones de teclas, usa la [etiqueta HTML `<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd). Esto denota la entrada de texto del usuario desde un teclado, entrada de voz o cualquier otro dispositivo de entrada de texto. Si estás trabajando en un editor que no soporta HTML personalizado, usa [texto de código](#code-in-text) en su lugar.

Escribe los nombres de las teclas como Command, Control, Option y Shift. No uses símbolos para esas teclas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Presiona <strong>Option</strong>.</td><td style="width: 50%;">Presiona ⌥.</td></tr>
</tbody>
</table>
{:/}

Para combinaciones de teclas, usa un signo más (+) entre las teclas, pero omite el signo más de cualquier formato especial.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Presiona <strong>Option + F12</strong>.</td><td style="width: 50%;">Presiona ⌥ + F12.</td></tr>
</tbody>
</table>
{:/}

Por ejemplo, así es como aparecen las etiquetas de teclado en la documentación de Braze:
Para detener el comando, presiona **Control + C**.

##### Métricas {#metrics}

Al referirte a una métrica en una tabla o entrada de glosario, usa mayúsculas iniciales sin formato especial. Al referirte a una métrica en una oración, usa mayúsculas iniciales con cursiva (como *Machine Opens*).

##### Páginas

Usa el término página al referirte a una página web en general, o a una página específica en el panel de Braze. Al referirte al nombre de una página, usa el formato "la página [etiqueta]" y pon en negrita el nombre de la página.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Ve a la página Segments.</td><td style="width: 50%;">Ve a la página "Segments".</td></tr>
</tbody>
</table>
{:/}

##### Nombres de permisos {#permission-names}

Al referirte a nombres de permisos de usuario dentro del dashboard, encierra el nombre del permiso entre comillas.

{% alert note %}

Actualmente estamos usando capitalización de título para coincidir con el formato del dashboard. Hay un plan para actualizar los nombres de permisos dentro de la interfaz a capitalización de oración para coincidir con nuestros estándares.

{% endalert %}

##### Pestañas {#tabs-1}

Al referirte a una pestaña, usa el formato "la pestaña [etiqueta]" y pon en negrita el nombre de la pestaña.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Ve a la página <strong>Manage Settings</strong> y selecciona la pestaña <strong>Tags</strong>.</td><td style="width: 50%;">Ve a la página "Manage Settings" y selecciona la pestaña "Tags".</td></tr>
</tbody>
</table>
{:/}

##### Entrada de texto {#text-input}

Al instruir a un lector para que escriba una cadena de texto específica, encierra el texto entre comillas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">En el campo <strong>Name</strong>, ingresa "Lapsing Users"</td><td style="width: 50%;">En el campo <strong>Name</strong>, ingresa <code>Lapsing Users</code>.</td></tr>
</tbody>
</table>
{:/}

#### Preguntas frecuentes (FAQ) {#frequently-asked-questions-faqs}

Ordena las preguntas frecuentes comenzando con la información que las personas más quieren o necesitan saber, y luego organiza las preguntas frecuentes por categoría de problema si hay varias.

Para cada pregunta frecuente, comienza respondiendo directamente la pregunta, luego entra en detalle. Usa preguntas reales que coincidan con consultas de búsqueda típicas y el vocabulario del usuario, lo que ayuda con la encontrabilidad de las preguntas frecuentes. Incluye enlaces a recursos que el usuario pueda encontrar útiles, como artículos relacionados, instrucciones para contactar soporte y materiales de enseñanza (guías prácticas, tutoriales y otros) cuando estén disponibles.

#### Geografía {#geography}

##### Ciudades

Escribe todos los nombres de ciudades completos en la primera mención en el texto. Después de eso, está bien abreviar nombres de ciudades bien conocidas como NYC o LA.

**Primera mención:** San Francisco
**Segunda mención:** SF

Para ciudades bien conocidas como Londres o Tokio, está bien presentarlas sin una coma seguida del estado, provincia o país.

Para ciudades o pueblos que puedan ser desconocidos para tu audiencia, incluye el estado, provincia o país.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Correcto</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Amberes, Bélgica</td></tr>
</tbody>
</table>
{:/}

##### Países

Capitaliza los nombres de todos los países. Para abreviar el nombre de un país, escríbelo completo en la primera mención, seguido de las iniciales en adelante.

**Primera mención:** Estados Unidos
**Segunda mención:** EE. UU.

No coloques puntos entre los nombres de países abreviados.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### Regiones

Capitaliza tanto la región como el modificador direccional.

**Ejemplo:** Norte de California, Europa del Este

Capitaliza los nombres propios que describen una región o lugar específico.

**Ejemplo:** West Midlands, Sudamérica, South Chicago

##### Estados y provincias

Capitaliza todos los estados y provincias.

**Ejemplo:** Nueva York, Quebec

#### Encabezados y títulos {#headings-and-titles}

Para encabezados y títulos de artículos, usa capitalización de oración. Sé descriptivo al escribir encabezados y títulos, y céntrate en el propósito principal del contenido según el tipo de artículo. No uses ampersands en lugar de la palabra "y".

Para títulos de artículos, cuando sea posible, evita gerundios (verbos que terminan en *-ando/-endo/-iendo*) en favor de verbos imperativos. Mantén los títulos de artículos concisos y asegúrate de que sean apropiados para el contenido. Por ejemplo, un artículo de referencia sobre mensajes SMS podría titularse "Acerca de SMS".

Para encabezados de artículos, sé conciso y consistente entre los títulos de encabezados. Por ejemplo, si el estilo de Encabezado 1 del artículo define cada paso (ej. **Paso 1: Crear una nueva campaña push**), entonces mantén este formato en todos los encabezados del artículo para consistencia.

Para ayuda con el estilo en Braze Docs, consulta la página de contribución para [ejemplos de estilo]({{site.baseurl}}/contributing/styling_examples/?tab=markdown).

##### Subtareas numéricas

Para encabezados que describen pasos ordenados, usa números en los encabezados de subtareas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Paso 2: Crear una campaña SMS <br><br> Paso 2.1: Redactar tu mensaje <br><br> Paso 2.2: Programar la entrega</td><td style="width: 50%;">Paso 2: Crear una campaña SMS <br><br> Paso 2a: Redactar tu mensaje <br><br> Paso 2b: Programar la entrega</td></tr>
</tbody>
</table>
{:/}

#### Introducciones {#introductions}

Las introducciones sirven como una verificación rápida para los usuarios que se preguntan:

* ¿Estoy en el documento correcto? ¿Es esto relevante para mí?
* ¿Qué aprenderé si invierto tiempo en leer este documento?
* ¿Siento que estoy siguiendo un recorrido claro de integración o configuración para SMS, correo electrónico, IAM u otro (a pesar de no especificar a qué documento debe ir el usuario a continuación)?

Las siguientes son directrices generales para introducciones. Consulta las directrices específicas de cada sección para casos de uso más específicos.

* Las introducciones pueden tener de 1 a 5 oraciones
* Las introducciones deben dar una descripción general del contenido del documento o ser una apertura para el tema
* Usa citas en bloque
* Coloca las introducciones bajo el encabezado H1 del artículo

##### Socios

Incluye una descripción general del socio y una breve descripción de la empresa. También incluye un enlace al sitio del socio.

##### API

Incluye solo la oración "Usa este punto final para..." en la introducción. Queremos mantener los puntos finales de API lo más fáciles de navegar posible. Para más información sobre la estructura y formato de puntos finales de API, consulta las [directrices de documentación de puntos finales de API]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

##### Guía de usuario y guía de desarrollador

Los párrafos de introducción deben escribirse de una de dos maneras:

1. Con un párrafo introductorio o apertura para el tema
2. Una declaración de lo que contiene el artículo. Esto a menudo se ve como "Este artículo de referencia....".

Aunque los pasos en la guía de usuario y la guía de desarrollador hacen que los usuarios dependan en gran medida de las pistas de la navegación a lo largo de su recorrido como cliente, aunque a veces sea redundante, es útil decir explícitamente el valor del documento justo al principio.

Por ejemplo, si un usuario estuviera recorriendo la guía de desarrollador integrando Unity. Esta página con el título "Integración" no sería suficiente sin incluir la oración de introducción.

#### Listas {#lists}

Las listas se usan mejor para formatear información relacionada. No uses una lista para mostrar solo un elemento. Si quieres separar un solo elemento del texto circundante, usa algún otro formato.

Hay tres tipos de listas: con viñetas, con letras y numeradas. Incluye una oración introductoria completa que pueda terminar con dos puntos o punto.

* Las listas con viñetas organizan información que no necesita estar en un orden específico.
* Las listas con letras se usan para definir opciones mutuamente excluyentes.
* Las listas numeradas indican una secuencia de pasos ordenados.

Usa la misma sintaxis para todos los elementos de la lista si es posible.

Para la capitalización de elementos de lista, comienza cada elemento con mayúscula. Para la puntuación final de elementos de lista, no uses puntuación final en los siguientes escenarios:

* Si el elemento de la lista es una sola palabra u oración incompleta
* Si el elemento de la lista no incluye un verbo
* Si el elemento de la lista está en fuente de código
* Si el elemento de la lista es un enlace o título de documento

#### Formato de medios {#media-formatting}

Esta sección incluye directrices generales para formatear imágenes y GIF en tu contenido. Para más información, incluyendo capturas de pantalla de ejemplo, consulta la [guía de estilo de imágenes]({{site.baseurl}}/contributing/style_guide/image_style_guide/).

| **Correcto** | {::nomarkdown}<ul><li>Recorta ajustadamente a la función o componente mencionado.</li><li>Toma capturas de pantalla de alta calidad, preferiblemente en un monitor retina (pantalla de MacBook).</li><li>Crea un GIF de una interacción o flujo de trabajo.</li><li>Ten en cuenta que los usuarios no pueden pausar o avanzar en un GIF para ver detalles.</li><li>Pasa las imágenes por un optimizador para reducir el tamaño del archivo (ImageOptim, TinyPNG o Ezgif).</li><li>Apunta a un alto contraste entre elementos para accesibilidad.</li><li>Redimensiona las imágenes por porcentajes de altura en lugar de valores de píxeles distintos.</li></ul>{:/} |
| **Incorrecto** | {::nomarkdown}<ul><li>No incluyas el encabezado o la barra lateral del dashboard, ya que estos pueden explicarse en una oración simple.</li><li>No incluyas todo el dashboard.</li><li>No incluyas información de identificación personal (a menos que esté difuminada o sea de un usuario de demostración).</li><li>No incluyas el marco del navegador (campo de URL, marcadores, pestañas, etc.).</li><li>No incluyas dashboards de socios tecnológicos.</li><li>No agregues borde o sombra a las imágenes.</li></ul>{:/} |

#### Números {#numbers}

Nunca comiences una oración con un número. La excepción es cuando te refieres a un año (ejemplo: "2019 fue un año para recordar").

Escribe los números del uno al nueve. Para unidades de medida o números de 10 o más, usa el número. Para números de más de tres dígitos, usa una coma. Escribe los números más grandes.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1,000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200,000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1,000,000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 mil millones</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 MB</td><td style="width: 50%;">cinco MB</td></tr>
</tbody>
</table>
{:/}

##### Moneda

Siempre indica a qué moneda te refieres usando el símbolo de moneda antes de la cantidad o deletréala (ejemplo: pesos, euros, libras, etc.).

Usa el decimal para cantidades donde el número de centavos es mayor que cero. Para sumas mayores de tres dígitos, usa una coma. No incluyas ".00" en sumas de dinero.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US $20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### Números de teléfono

Cuando se hace referencia a un número de teléfono, coloca guiones entre los dígitos. No coloques el código de área entre paréntesis.

Al formatear números de teléfono con un código de país, usa un signo más (+) antes del código de país y coloca el código de área entre paréntesis.

Proporciona un número con código de país de la siguiente manera: +1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### Fracciones

Escribe las fracciones y usa un guion entre el numerador y el denominador. No uses números separados por una barra.

En algunos casos cuando expresar una fracción como decimal es necesario, agrega un cero antes del punto decimal para fracciones menores que uno.

Al expresar sistemas de calificación usando fracciones, usa números para deletrear la clasificación.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0.5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">un tercio</td><td style="width: 50%;">un-tercio</td></tr>
<tr><td style="width: 50%;">9 de 10</td><td style="width: 50%;">nueve de diez</td></tr>
</tbody>
</table>
{:/}

##### Porcentajes

Usa números y un signo de porcentaje (%) sin espacio entre ellos. Sin embargo, si el porcentaje comienza la oración, entonces escribe el porcentaje completo (número y porcentaje).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Veinte por ciento de los usuarios de la empresa son...</td><td style="width: 50%;">20% de los usuarios de la empresa son...</td></tr>
</tbody>
</table>
{:/}

##### Rangos

Usa un guion para indicar un rango de números. No uses una semirraya para separar números en un rango.

Para rangos de números con unidades, repite la unidad de medida después del número. Esto no incluye repetir sustantivos. Usa la palabra "a" entre los números del rango para evitar confusión.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 a 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C a 50°C</td><td style="width: 50%;">-10°C-50°C</td></tr>
</tbody>
</table>
{:/}

#### Texto de marcador de posición {#placeholder-text}

Usa texto de marcador de posición para indicar dónde el lector debe proporcionar el valor relevante. El texto de marcador de posición debe indicar el contenido que se está representando. Por ejemplo, *YOUR_API_KEY* indica la clave de API del lector.

##### Escribir marcadores de posición

Al crear texto de marcador de posición, consulta las siguientes directrices:

| Directriz | Ejemplo |
| :---- | :---- |
| Usa letras mayúsculas y separa las palabras con guiones bajos (_). | `PLACEHOLDER_VARIABLE` |
| Para texto de marcador de posición en línea, usa cursiva. | *`PLACEHOLDER_VARIABLE`* |
| Para texto de marcador de posición en bloques de código de API (donde no puedes usar cursiva), encierra los marcadores de posición entre llaves ({}). | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| Para texto de marcador de posición en bloques de código Liquid (donde no puedes usar cursiva), usa letras mayúsculas. | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}` |
| No sacrifiques claridad por brevedad. Usa tantas palabras como sean necesarias para representar un marcador de posición. | **Correcto:** `CAMPAIGN_NAME` <br> **Incorrecto**: _`NAME`_|

##### Usar marcadores de posición

Al introducir o explicar un marcador de posición, consulta las siguientes directrices:

| Directriz | Ejemplo |
| :---- | :---- |
| Señala los marcadores de posición inmediatamente después del marcador. | Reemplaza `<YOUR_APP_IDENTIFIER_API_KEY>` con tu [clave de API del identificador de aplicación]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), que puedes encontrar en la página **Settings**. |
| Para señalar dos o más marcadores de posición a la vez, usa una lista con viñetas. Lista cada marcador en el orden en que aparecen en el código. | Reemplaza lo siguiente: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: una descripción de lo que representa el marcador de posición</li><li><code>PLACEHOLDER_VARIABLE</code>: una descripción de lo que representa el marcador de posición</li></ul>{:/} |
| Refiere al marcador de posición con el mismo formato en que se muestra en el texto o código. | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> Reemplaza `<YOUR_APP_TARGET>` con el nombre de tu aplicación objetivo. |

#### Productos {#products}

Al referirte a Braze y sus funciones, usa los nombres completos de productos y funciones, y capitalízalos según la interfaz. No capitalices plantillas o funciones comunes. Para una lista de nombres de productos y su ortografía, consulta el [glosario](#glossary).

No abrevies nombres de productos o funciones excepto en los siguientes casos:

* Para coincidir con la interfaz
* Para cumplir con restricciones de espacio limitado

Nunca uses nombres de productos o funciones como verbos.

Nunca uses un apóstrofo después de Braze (ejemplo: "Braze's"). Suena extraño. En su lugar, forma posesivos usando una preposición ("a, de, desde") seguida del nombre de la empresa.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">La actualización de producto más reciente de Braze</td><td style="width: 50%;">La actualización de producto más reciente de Braze's</td></tr>
<tr><td style="width: 50%;">Esa es una de las características definitorias de Braze.</td><td style="width: 50%;">Esa es una de las características definitorias de Braze's</td></tr>
</tbody>
</table>
{:/}

Refiere a "Braze" como "nosotros/nuestro". Nunca "ello/su/ellos/su".

#### Tablas {#tables}

Usar tablas puede ser una forma útil y organizada de mostrar información. Asegúrate de tener encabezados claros y descriptivos y datos relevantes dentro de las columnas y filas respectivas.

Siempre usa una oración introductoria para describir el propósito de la tabla. Evita usar tablas en medio de procedimientos numerados. En su lugar, considera usar una lista.

#### Unidades de medida {#units-of-measurement}

Para HTML y Markdown, usa un espacio de no separación (&nbsp) entre el número y la unidad al especificar una unidad de medida. Esto incluye la mayoría de las unidades de medida como distancia, píxeles, puntos, peso y grados de temperatura (entre el grado y la unidad de medida).

Para moneda, porcentaje o grados de un ángulo, no uses un espacio entre el número y la unidad.

Para rangos de números con unidades, repite la unidad para cada número. De manera similar, para tasas, usa "por" en lugar de una barra (/).

### Enlaces {#linking}

#### Enlaces de referencia cruzada {#cross-reference-links}

Usa referencias cruzadas para guiar a los usuarios a recursos adicionales. En la documentación de Braze, usa URLs relativas a la raíz del sitio para enlazar a otros documentos de Braze (reemplaza "www.braze.com/docs" con "{{site.baseurl}}").

Evita agregar múltiples enlaces al mismo documento dentro de una página dada, ya que esto puede causar fatiga de enlaces. Los enlaces duplicados están bien con moderación si estás enlazando a una sección específica en otra página, o si la página desde la que estás enlazando es larga.

#### Incrustar videos {#embedding-videos}

Similar a las imágenes, usa videos para crear variedad en tus materiales de aprendizaje. La mayoría de las personas aprenden mejor con una combinación de medios, así que asegúrate de que cualquier contenido que incluyas en un video también esté cubierto en el artículo o lección.

Para incrustar un video en la documentación de Braze, consulta [Prueba de video incrustado]({{site.baseurl}}/home/styling_test_page/#embedded-video-test).

#### Encabezados como destinos de enlace {#headings-as-link-targets}

En la documentación de Braze, los anclajes se crean automáticamente para los encabezados. Sin embargo, puede que quieras agregar un anclaje personalizado a un encabezado si:

* Tu anclaje generado automáticamente es muy largo.
* Tu encabezado puede ser enlazado frecuentemente. Agregar un anclaje personalizado reduce la probabilidad de romper enlaces si el texto del encabezado se cambia después.

Para agregar un anclaje a un encabezado en la documentación de Braze, consulta [Anclajes personalizados]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Texto de enlace {#link-text}

El texto de enlace efectivo ayuda a mejorar la encontrabilidad, descubribilidad y accesibilidad de tu contenido.

##### Estructurar enlaces {#structuring-links}

Usa uno de los siguientes formatos al escribir enlaces:

* Haz coincidir el texto del enlace con el título o encabezado del destino del enlace.
* Usa una descripción del destino del enlace como texto del enlace.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Haz coincidir el texto del enlace con el título o encabezado del destino del enlace.</em></th><th style="width: 50%;">Correcto: <em>Usa una descripción del destino del enlace como texto del enlace.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Comienza con el <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">Web SDK</a> de Braze.</td><td style="width: 50%;">Para conocer tu clúster o punto final específico, <a href="{{site.baseurl}}/braze_support/">contacta a soporte</a>.</td></tr>
<tr><td style="width: 50%;">Para más información, consulta <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Cancelar mensajes Liquid</a>.</td><td style="width: 50%;">En caso de duda, siempre puedes <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">restablecer tu contraseña</a>.</td></tr>
</tbody>
</table>
{:/}

Puede que necesites reformular una oración para crear un buen texto de enlace.

Si estás enlazando a una sección en la misma página, usa una frase estándar que indique esta acción. Por ejemplo:

* En esta página, consulta [encabezado].
* En este documento, consulta [encabezado].
* Para más información, consulta la sección [encabezado].

##### Redacción de enlaces {#writing-links}

Aplica las siguientes directrices al escribir texto de enlace:

* Coloca el enlace en las palabras clave relevantes.
* Si estás escribiendo una oración completa que refiere al lector a otro artículo, usa la frase "Para más información, consulta" o "Para más información sobre [tema], consulta".
* Solo agrega una oración "Más información..." si el texto de ayuda aborda más de un concepto, cada uno de los cuales podría enlazarse a su propio documento de ayuda. En esta situación, elige el enlace más apropiado y contextualízalo con "Más información..."
* Para mantener un tono informal, no uses "por favor" para introducir texto de enlace. Por ejemplo, evita la frase "Por favor consulta", "Por favor ve" y "Por favor contacta".
* Escribe texto de enlace único y descriptivo que tenga sentido sin el texto circundante. La investigación del [Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone) (NN/g) muestra que los lectores escanean en busca de información relevante en una página, así que asegúrate de que los enlaces puedan sostenerse por sí solos.
* No uses las siguientes palabras o frases para texto de enlace. Son malas para la accesibilidad y la escaneabilidad.
 * Más información (por sí solo)
 * Haz clic aquí
 * aquí
 * este documento
 * este artículo

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Asegúrate de que el texto del enlace tenga sentido sin el texto circundante</em></th><th style="width: 50%;">Incorrecto: <em>Usar texto de enlace vago o no descriptivo</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Para más información sobre la importación de datos de clientes, consulta <a href="{{site.baseurl}}">Importación de usuarios</a>.</td><td style="width: 50%;">Para más información, <a href="{{site.baseurl}}">haz clic aquí</a>.</td></tr>
<tr><td style="width: 50%;">Esta función se conecta al punto final <a href="{{site.baseurl}}">Rastrear usuarios</a>.</td><td style="width: 50%;">Consulta <a href="{{site.baseurl}}">este artículo</a>.</td></tr>
<tr><td style="width: 50%;">Obtén más información sobre <a href="{{site.baseurl}}">las novedades en Android SDK 16.0.0</a>.</td><td style="width: 50%;">Sigue las instrucciones <a href="{{site.baseurl}}">aquí</a>.</td></tr>
<tr><td style="width: 50%;">Obtén más información sobre la <a href="https://www.braze.com/product">plataforma de Braze</a>.</td><td style="width: 50%;">Para los pasos, consulta <a href="{{site.baseurl}}">este documento</a>. <a href="{{site.baseurl}}">Más información</a>.</td></tr>
<tr><td style="width: 50%;">Las claves de API de Storefront son únicas por tienda Hydrogen, pero sus alcances de permisos son compartidos por todas las tiendas Hydrogen. Obtén más información sobre los <a href="{{site.baseurl}}">tokens de API de Storefront.</a></td><td style="width: 50%;">Los <a href="{{site.baseurl}}">tokens de API de Storefront</a> son únicos por <a href="{{site.baseurl}}">tienda Hydrogen</a>, pero sus <a href="{{site.baseurl}}">alcances de permisos</a> son compartidos entre todas las tiendas Hydrogen.</td></tr>
</tbody>
</table>
{:/}

#### Enlaces para puntos finales {#links-for-endpoints}

Al referenciar artículos de puntos finales, asegúrate de usar [texto de enlace significativo](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog) que pueda tener sentido fuera de contexto. Si estás usando la ruta del punto final como enlace, asegúrate de proporcionar detalles en el texto circundante ya que la ruta puede no comunicar claramente la función del punto final.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Elimina perfiles de usuario usando el <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">punto final Eliminar usuario</a> de Braze.</td><td style="width: 50%;">Elimina perfiles de usuario usando el punto final <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Eliminar usuario</a> de Braze.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/">punto final <code>/users/export/id</code></a></td><td style="width: 50%;">punto final <a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a></td></tr>
</tbody>
</table>
{:/}

#### Enlaces para descarga de archivos {#links-for-file-download}

Si un enlace descarga un archivo, deja eso claro en el texto del enlace y menciona el tipo de archivo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto: <em>Asegúrate de que el texto del enlace comunique que al seleccionarlo se descarga un archivo</em></th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Para consejos, descarga el <a href="{{site.baseurl}}">PDF de hoja de referencia de Regex</a>.</td><td style="width: 50%;">Consulta nuestra <a href="{{site.baseurl}}">hoja de referencia de RegEx</a>.</td></tr>
<tr><td style="width: 50%;">Para más información, descarga el <a href="{{site.baseurl}}">PDF del manual de servicios de éxito y soporte</a>.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Manual de servicios de éxito y soporte</a></td></tr>
</tbody>
</table>
{:/}

#### Enlaces a otros sitios {#links-to-other-sites}

Como regla general, no enlaces a otro sitio si puedes cubrir la información con una breve explicación. No podemos rastrear cuándo cambia el contenido en otro sitio.

Si enlazas a un sitio externo, asegúrate de que el sitio al que enlazas sea de alta calidad, confiable y respetable. Si es posible, enlaza al encabezado más relevante en una página.

Usa un ícono de enlace externo para indicar que el enlace va a un dominio diferente. Para la documentación de Braze, esto se aplica automáticamente a los enlaces externos.

#### URLs para imágenes {#urls-for-images}

En la documentación de Braze, usa URLs relativas a la raíz del sitio para enlazar a imágenes. Para más información, consulta [Agregar y editar imágenes](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images).

### Glosario {#glossary}

⚠️ = Usa con precaución, consulta las notas relevantes
⛔️ = No usar

#### Números

**24/7**
Usa guion (24-7) solo cuando se usa como modificador antes de un sustantivo.

**2D / bidimensional**

**3D / tridimensional**

#### A

**pruebas A/B**

⚠️ **abort**
Evita usarlo a menos que te refieras a un proceso específicamente nombrado. En su lugar, usa palabras como "detener", "salir", "cancelar" o "terminar".

**botones de acción**

**entrega basada en acciones**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

⛔️ **ad hoc**
No usar. Usa "puntual" o similar.

**AI**
Preferido sobre "inteligencia artificial" después de la primera mención.

**AI item recommendation**

**Alloys / Braze Alloys**
Siempre capitalizado.

**alfanumérico**
No uses guion.

**always-on**

**am**
En minúsculas cuando se usa para la hora (por ejemplo, "10 am"). Ver también [pm](#glossary).

**Amazon S3**

**Amazon Web Services (AWS)**
Siempre capitalizado. Deletrea en la primera mención, luego está bien usar el acrónimo.

**AMP for Email / Braze AMP for Email**

**Android**

**API / Application Programming Interface**
Deletrea en la primera mención, luego está bien usar el acrónimo.

**API key**

**APNs / Apple Push Notification service**

**⛔️ grupo de aplicaciones**
No usar. Grupo de aplicaciones ha sido renombrado a espacio de trabajo.

**Apple iOS platform**

**AppleWatch**

**.avro**

#### B

**behavior, behaviors**

**Benchmarks**

**beta**

**BI Insights**

**bingeing**

**Binge-watch**

**Bonfire / Bonfire community / Braze Bonfire community**
Usa "Braze Bonfire community" en la primera mención, luego está bien usar solo "Bonfire" o "Bonfire community".

**boolean**

⛔️ **lista negra**
No usar. En su lugar, usa "blocklist" o "denylist". Para la forma verbal de estas palabras, considera reformular la oración para eliminar el término problemático. Por ejemplo:

>✅ **Recomendado:** Para bloquear una propiedad existente para que no se use en nuevos mensajes, selecciona **Manage Properties**. <br>
>⛔️ **No recomendado:** Para poner en lista negra una propiedad existente, selecciona **Manage Properties**.

**Braze-to-Braze webhook**

**Business Intelligence (BI)**
Deletrea en la primera mención, luego está bien usar el acrónimo.

#### C

**California Consumer Privacy Act (CCPA)**
Deletrea en la primera mención, luego está bien usar el acrónimo. Ver también [CCPA compliance (noun) / CCPA-compliant (adjective)](#ccpa-compliance)

**can**
Usa "can" para referirte a una acción u resultado opcional. Por ejemplo:

> ✅ **Recomendado:** También puedes subir y actualizar perfiles de usuario con archivos CSV.
> ✅ **Recomendado:** El proceso de importación puede tardar unos minutos.

No uses "can" para instrucciones. En su lugar, prefiere el verbo imperativo. Para ejemplos, consulta [Segunda persona y primera persona](#second-person-and-first-person).

**Canvas**
Siempre capitalizado. El plural es "Canvases".

**Canvas Flow**
Usa cuando diferencies entre el editor original de Canvas y Canvas Flow. De lo contrario, usa "Canvas".

**campaña**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**capacidad**
Usa cuando te refieras a límites de datos personalizados en lugar de la palabra "límite".

**catálogo**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**CCPA compliance (noun) / CCPA-compliant (adjective)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**churn**
Usa para referirte a la rotación o pérdida de clientes.

**churn prediction**
En minúsculas excepto cuando te refieras a la interfaz.

**checkbox**

**Check-in (sustantivo) / check in (verbo)**

**City x City**

**Cofounder**

**Content Cards / Braze Content Cards**

**Content Blocks**

**grupo de control**

**conversión**

**conversion group analysis**
En minúsculas.

**Cordova**

**Currents / Braze Currents**
Siempre capitalizado.

**CRM / customer relationship management**
Deletrea en la primera mención, luego está bien usar el acrónimo.

**mensajería de canales cruzados / personalización de canales cruzados**

**C-suite**

**CSV / comma-separated values**

**atributos personalizados**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**eventos personalizados**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**atributos del cliente**

**comportamiento del cliente**

**plataforma de datos de los clientes (CDP)**
En minúsculas.

**interacción con los clientes**

**eventos del cliente**

**recorrido del cliente**

**permisos del cliente**

**retención de clientes**

#### D

**Dark Mode theme / Dark Mode Preview / concepto de modo oscuro**

**dashboard / panel de Braze**
Usa para referirte a Braze como plataforma. Usa minúsculas (dashboard, no Dashboard).

**basado en datos (adjetivo)**

**privacidad de datos**

**data sheet**

**transmisión de datos**

**DAU / Daily Active Users**

**Decision Splits**

**vinculación en profundidad**

**Delay Messages**

**Downtime**

**arrastrar y soltar (verbo) / arrastrar y soltar (adjetivo)** {#drag-and-drop}
Usa cuando te refieras a arrastrar archivos a una zona de carga.

**Editor de arrastrar y soltar**
Usa capitalización de título cuando te refieras a la función en la interfaz. De lo contrario, usa minúsculas (editor de arrastrar y soltar). Usa el verbo cuando hagas referencia a cómo los clientes pueden [arrastrar y soltar](#drag-and-drop) elementos en el editor.

**drill down (verbo) / drilldown (sustantivo o adjetivo)**
Usa en contenido sobre datos y los informes generados a partir de ellos.

**DTC / direct to consumer**

**contenido dinámico**

#### E

**acceso anticipado**

⛔️ **e.g.**
No usar. Usa las frases "por ejemplo", "como" o similar.

**eBook**

**comercio electrónico**
No "ecommerce" ni "e-commerce".

**ecosistema**

**correo electrónico**
No "Email" ni "e-mail".

**capacidad de entrega de correo electrónico**

**reputación de correo electrónico**

**EMEA (Europa, Oriente Medio y Asia)**

**emoji**
Forma singular y plural.

**end user (sustantivo) / end-user (adjetivo)**
Prefiere "tus usuarios" sobre "usuarios finales".

⚠️ **ensure**
Evita usarlo cuando hables de lo que hace una función. Consulta [Evita garantías](#avoid-guarantees) para más información.

**ESP / email service provider**

**predicción de eventos**

**propiedades del evento / propiedades de eventos personalizados**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**eventos de excepción**

**extraer**
Usa "extraer" en lugar de "descomprimir" para referirte a extraer archivos de una carpeta comprimida.

**ID externo**
No "External ID". Cuando hagas referencia a fragmentos de código, usa external_id.

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [AÑO]**

**limitación de frecuencia**

**Fullscreen**
Cuando se usa como adjetivo (por ejemplo, "mensajes dentro de la aplicación Fullscreen"), escribe sin guion.

#### G

**GDPR / General Data Protection Regulation**
Deletrea en la primera mención, luego está bien usar el acrónimo.

**GDPR compliance (sustantivo) / GDPR-compliant (adjetivo)**

**geofence**

**GIF**

**GitHub**
No "Github" ni "github".

**Google / google-able**

#### H

**High-performance**

**High-Value Actions**

**HQ / headquarters**

**HTML Email Editor**

**HTTP**

#### I

⛔️ **i.e.**
No usar. Usa la frase "es decir" o similar.

**mensajes dentro de la aplicación**

**mensaje en el explorador (IBM)**

**infografía**

**atribución de instalación**

**integer**

**Intelligence Suite**
Usa capitalización de título.

**Intelligent Channel**
Usa capitalización de título.

**Intelligent Selection**
Usa capitalización de título.

**Intelligent Timing**
Usa capitalización de título.

⛔️ **Internet of things**
No usar.

**iOS**

**calentamiento de IP**

**iPad**

**iPhone**

**IT**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (programa) / keynote (sustantivo)**

**kick off (verbo) / kickoff (sustantivo)**

⚠️ **kill**
Evita usarlo a menos que te refieras a un proceso específicamente nombrado. En su lugar, usa palabras como "detener", "salir", "cancelar" o "terminar".

**KPI / indicador clave de rendimiento**

#### L

**página de inicio**

**ciclo de vida**

**Lift-rate**

**LinkedIn**

**Liquid**
Siempre capitalizado.

**Live Preview**

**largo plazo (sustantivo) / a largo plazo (adjetivo)**

**LTV / valor de duración del ciclo de vida**

#### M

**tecnología de marketing**
Preferido sobre "martech".

**MAU / usuarios activos al mes**

**máximo**
No "max".

**biblioteca de medios**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**Microsoft**

**Microsoft Azure**

**ML / aprendizaje automático**

**marketing móvil**

**automatización del marketing móvil**

**momento de uso del marketing móvil**

**teléfono móvil**

**campaña multicanal**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado. Sin guion.

**soporte multilingüe**

**pruebas multivariante**

#### N

**N/A**
No "NA". Usa "N/A" según sea necesario en tablas para indicar contenido de columna o fila que no aplica a una celda particular. En texto en línea, prefiere "no disponible" o "no aplica" para mayor claridad.

⚠️ **nuevo**
Evita usarlo en documentación de producto y material de aprendizaje, ya que esto puede fechar rápidamente tu contenido. Para más información, consulta [Funciones futuras](#describing-limitations).

**NRT / near real-time (adjetivo) / near real time (sustantivo)**

**NYC / New York City**

#### O

**bajo demanda**

**incorporación**

**once**
Usa para referirte a realizar una acción una sola vez. No uses "once" en lugar de "después" o "cuando".

**tarifa abierta (OR)**

**mensaje de adhesión voluntaria**

**orquestación**

**OS / sistema operativo**

**OTT / Over-the-top media services**

⛔️ **out-of-the-box**
No usar. En su lugar, usa una alternativa como "predeterminado".

#### P

**socio, socios, asociación**

**persona (singular) / personas (plural)**

**personalización**

**información de identificación personal (PII)**

**Personalized Path**
Usa capitalización de título.

**Personalized Variant**
Usa capitalización de título.

**PhD / PhDs**

**pm**
En minúsculas cuando se usa para la hora (por ejemplo, "10 pm"). Ver también [am](#glossary).

**precedente**

**predicción**
En minúsculas a menos que esté precedido por "Braze", como "Una predicción de Braze es…".

**análisis predictivo**

**Predictive Churn**
Usa capitalización de título. Predictive Churn es el nombre del producto, mientras que los clientes crean una [predicción de abandono](#glossary).

**Predictive Events**
Usa capitalización de título.

**Predictive Purchases**
Usa capitalización de título. Predictive Purchases es el nombre del producto, mientras que los clientes crean una [predicción de compra](#glossary).

**Predictive Suite**
Usa capitalización de título.

**centro de preferencias**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**preparación para la ubicación**

**preparación para las notificaciones push**

**código promocional**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado. No uses "código promo".

**predicción de compra**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**propiedades de la compra**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**botones de acción para notificación push**

**Push Max**
Usa capitalización de título.

**notificación push**

**Push Stories**
Usa capitalización de título.

#### Q

**Q&A**

⛔️ **QA (quality assurance)**
No uses el acrónimo como verbo. En su lugar, reformula como "realizar aseguramiento de calidad".

**horas tranquilas**
Usa "Horas tranquilas" al inicio de oración y "horas tranquilas" a mitad de oración. No uses capitalización de título "Horas Tranquilas" porque no es una función de marca.

⚠️ **rápido / rápidamente**
Evita usarlo. Lo que es rápido para ti puede no serlo para otros. Para directrices relacionadas, consulta [Lenguaje condescendiente](#condescending-language).

#### R

**límite de velocidad**

**tiempo real (sustantivo) / en tiempo real (adjetivo)**

**reactivación de la interacción**

⚠️ **expresión regular / regex**
Prefiere la versión completa sobre su abreviatura "regex". No uses "RegEx".

**marketing relacional**

**retargeting**

**retención**

**notificaciones push enriquecidas**

**clic derecho**

**deslizar a la derecha**

**ROI / retorno de la inversión**

#### S

**Sage AI by Braze™**

⛔️ **sanity check**
No usar. En su lugar, usa un término como "verificación rápida" o "verificación preliminar". Alternativamente, introduce instrucciones de verificación con una frase como "Verifiquemos que todo esté funcionando".

**entrega programada**
En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**captura de pantalla**

**captura de pantalla**

**SDK / Software Developer Kit**

**segmento (audiencia)**

**Segment Extensions**
Usa capitalización de título.

**Segment Insights**
Usa capitalización de título.

**segmentación**

**selección**
Como en, la función dentro de catálogos. En minúsculas excepto cuando te refieras a un elemento de la interfaz que esté capitalizado.

**SF / San Francisco**

**Silicon Valley**

**silo, silos, aislado**

**encuesta simple**

**presentación de diapositivas**

**Smartphone**

**Smartwatch**

**SMS**

**software como servicio (SaaS)**
Deletrea en la primera mención, luego está bien usar el acrónimo.

**pruebas de correo no deseado**

**SQL / structured query language**

**SQL Segment Extensions**
Usa capitalización de título.

**adherencia**

**streaming**

**string**
Para audiencias no técnicas, define un string como texto que contiene "caracteres alfanuméricos". Para audiencias técnicas, está bien no definir este término.

**grupo de suscripción**

**sunset, sunsetting**

#### T

**respuesta dirigida**

⚠️ **terminate**
Evita usarlo a menos que te refieras a un proceso específicamente nombrado. En su lugar, usa palabras como "detener", "salir", "cancelar" o "terminar".

**de terceros**

**zona horaria**
No "timezone".

**marca de tiempo**

**pantalla táctil**

**mensaje desencadenado**

**Twitter**

#### U

**UK / United Kingdom**

⛔️ **unzip**
No usar. En su lugar, usa "extraer".

**URL**
Se pronuncia como las letras individuales U-R-L, así que escribe "una URL" en lugar de "un URL". Usa mayúsculas. Para plurales, usa URLs.

**US / USA**
Sin puntos.

**casos de uso**

**atributos de usuario / atributos de usuario predeterminados**
Usa para referirte a datos de usuario capturados automáticamente por Braze.

**perfil de usuario**

**nombre de usuario**

⚠️ **utilizar**
No uses "utilizar" cuando quieras decir "usar". Usa "utilizar" para referirte a algo que se usa más allá de su propósito original previsto.

#### V

**variante**

⛔️ **vía**
No usar. En su lugar, usa términos como "a través de" o frases como "por medio de".

⛔️ **viceversa**
No usar. En su lugar, usa términos como "a la inversa" o una frase como "al revés".

**solo lectura**

⚠️ **vs.**
No uses "vs." como abreviatura de "versus". En su lugar, escribe la palabra completa.

#### W

**mensajería web**

**web push**

**webhook**

**seminario web**

**etiqueta sin marca**

⛔️ **lista blanca**
No usar a menos que te refieras a la interfaz. En su lugar, usa "allowlist" o "safelist". Para la forma verbal de estas palabras, considera reformular la oración para eliminar el término problemático. Para ejemplos, consulta [lista negra](#glossary).

⚠️ **Wi-Fi**
No uses "WiFi", "wi-fi" ni "wifi".

**will**
Evita usar "will" o "would". Consulta [Tiempo presente](#present-tense).

**Winning Path**
Usa capitalización de título.

**Winning Variant**
Usa capitalización de título.

⛔️ **wizard**
No usar. En su lugar, usa "compositor".

**WordPress**

**espacio de trabajo**

**www**

#### Y

**YAML**
No uses una extensión de archivo para referirte al tipo de archivo. Por ejemplo, usa "archivo YAML" en lugar de "archivo .yaml".

**YouTube**

#### Z

**código postal**

**archivo zip / archivos comprimidos**

**ZIP**
No uses una extensión de archivo para referirte al tipo de archivo. Por ejemplo, usa "archivo ZIP" en lugar de "archivo .zip".