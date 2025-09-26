---
nav_title: AMP para correo electrónico
article_title: AMP para correo electrónico
alias: /amphtml/
page_order: 11
description: "Este artículo de referencia proporciona un resumen de AMP para correo electrónico y casos de uso comunes."
channel:
  - email

---

# AMP para correo electrónico

> Con [AMP para correo electrónico](https://amp.dev/about/email), puede añadir elementos interactivos a sus correos electrónicos y elevar sus comunicaciones con sus clientes, ofreciendo una experiencia completa directamente en la bandeja de entrada de su usuario. AMP lo hace posible mediante el uso de varios componentes que pueden utilizarse para crear ofertas de correo electrónico interesantes, como encuestas, cuestionarios de opinión, campañas de votación, reseñas, centros de suscripción y mucho más. Herramientas como éstas pueden ofrecer oportunidades para aumentar el compromiso y la retención.

## Requisitos

Braze no es responsable de que los usuarios se registren en Google ni de que cumplan los requisitos de seguridad necesarios. AMP para correo electrónico sólo está disponible para SparkPost y SendGrid.

| Requisito   | Descripción |
| --------------| ----------- |
| AMP para correo electrónico activado | AMP está disponible para todos los usuarios. |
| Habilitación de cuentas de Gmail | Consulta [Habilitar la cuenta de Gmail](#enabling-gmail-account). |
| Autenticación de remitentes de Google | Gmail [autentica al remitente](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) de los correos electrónicos AMP con DKIM, SPF y DMARC. Estos deben estar configurados para su cuenta. <br><br>- [Correo identificado por claves de dominio](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Marco de la política de remitentes](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Autenticación, notificación y conformidad de mensajes basados en dominios](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| Elementos de correo electrónico AMP | Un correo electrónico AMP convincente incluye el uso estratégico de varios componentes. Consulte la pestaña Esenciales en la sección [Componentes](#components) más abajo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clientes de correo electrónico compatibles

Antes de poder enviar correos electrónicos AMP a los usuarios, debes registrarte en nuestros clientes de correo electrónico. El proceso de registro implica el envío de un correo electrónico AMP HTML de prueba para obtener la aprobación. Los plazos de aprobación varían de un cliente a otro. Sigue los enlaces de inscripción para obtener más información.

| Cliente | Enlace de inscripción |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

Para obtener una lista completa de los clientes de correo electrónico compatibles, consulta [la documentación de AMP](https://amp.dev/support/faq/email-support).

### Habilitación de la cuenta de Gmail

Ve a la configuración de Gmail y selecciona **Activar correo electrónico dinámico** en **General**.

![Un ejemplo de configuración de Gmail con la casilla "Habilitar correo electrónico dinámico" seleccionada.]({% image_buster /assets/img/dynamic-content.png %})

## Uso de la API

También puedes utilizar AMP para el correo electrónico con nuestra API. Si utiliza cualquiera de los [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/) Braze para enviar un correo electrónico, añada `amp_body` como especificación de objeto, como se muestra a continuación.

### Especificación del objeto de correo electrónico

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Crear tu correo electrónico AMP

Primero, construye tu correo electrónico AMP utilizando [componentes](#components). A continuación, utiliza [la API de Braze](#api-usage) para enviar tu mensaje, asegurándote de incluir `amp_body` para tu AMP HTML.

Además del HTML AMP, requerimos una versión HTML normal `body` y sugerimos una versión `plaintext_body` de tu correo electrónico AMP. Todos los correos electrónicos AMP se envían en multiparte, lo que significa que Braze envía un correo electrónico que admite HTML, texto sin formato y AMP HTML. Esto resulta útil en caso de que el correo electrónico se envíe a través de un proveedor que aún no admita AMP para correo electrónico, ya que el correo electrónico adoptará automáticamente la versión adecuada en función del usuario y su dispositivo.

{% alert note %}
Cuando estés creando un correo electrónico AMP, comprueba que estás en el editor AMP, ya que el código AMP no debe añadirse al editor HTML.
{% endalert %}

Consulte estos recursos adicionales:

- [Tutorial de AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Código de ejemplo](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) para ver cómo debería ser el producto final. 
- [Biblioteca de componentes de correo electrónico AMP](https://amp.dev/documentation/components/?format=email/)

### Componentes

Cuando construyas los elementos AMP, te recomendamos que consultes con tu equipo de ingeniería e incluyas recursos y elementos de diseño para darles una capa extra de pulido.

{% tabs %}
  {% tab Esenciales %}

Cada uno de estos elementos es necesario en el cuerpo de su correo electrónico AMP.

| Componente | Descripción | Ejemplo |
|---------|--------------|---------|
| Identificación <br><br> `⚡4email` o `amp4email`| Identifica tu correo electrónico como un correo electrónico AMP HTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Carga el tiempo de ejecución de AMP <br><br> `<script>` | Permite ejecutar AMP en tu correo electrónico utilizando JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| Plantilla CSS | Oculta el contenido hasta que se carga AMP. <br> Los proveedores de correo electrónico que admiten mensajes AMP aplican controles de seguridad que sólo permiten ejecutar scripts AMP verificados en sus clientes. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab Dinámico %}

Utilice estos componentes para crear diseños y comportamientos dinámicos en sus correos electrónicos.

| Componente | Descripción | Guión requerido |
|---------|--------------|---------|
| [Acordeón](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permite a los usuarios ver el esquema del contenido y saltar a cualquier sección. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formularios](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Cree formularios para enviar campos de entrada en un documento AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Cualquier componente que requiera autenticar al usuario debe utilizar [tokens de acceso de Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) o [tokens de aserción de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creativo %}

  Sube la apuesta con los componentes de AMP que pueden ayudarte a adaptar tu correo electrónico a tu audiencia.

| Componente | Descripción | Guión requerido |
|---------|--------------|---------|
| [Imagen animada](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Muestra una imagen animada (normalmente un GIF) gestionada en tiempo de ejecución. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrusel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Muestra varios contenidos similares a lo largo de un eje horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Imagen](https://amp.dev/documentation/components/amp-img?format=email) | Un sustituto gestionado en tiempo de ejecución de la etiqueta HTML `img`. <br>  También puedes crear un [lightbox para tu imagen](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Cualquier componente que requiera autenticar al usuario debe utilizar [tokens de acceso de Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) o [tokens de aserción de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Otros %}

| Componente | Descripción |
|---------|--------------|
| [Vinculación de datos y expresiones](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Añade interactividad de estado personalizada a tus páginas AMP mediante la vinculación de datos y expresiones similares a JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Cualquier componente que requiera autenticar al usuario debe utilizar [tokens de acceso de Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) o [tokens de aserción de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Para obtener una lista completa de los componentes de AMP, consulta [la documentación de AMP](https://amp.dev/documentation/components/?format=email).  

### Casos de uso

{% tabs local %}
{% tab Encuestas interactivas %}

El componente `<amp-form>` permite crear encuestas interactivas que pueden completarse sin salir de la bandeja de entrada del correo electrónico. Esto se puede hacer utilizando `<amp-form>` para enviar la respuesta de la encuesta, y luego hacer que su backend suministre estos datos agregados. 

Algunos ejemplos son:
* Correo electrónico del cuestionario de la Conferencia
* Actualizar dinámicamente los elementos de la fuente
* Correo electrónico del marcador de artículos

Mediante este componente, los usuarios pueden enviar o borrar valores de campo. Además, dependiendo de cómo configures tu correo electrónico, puedes dar indicaciones adicionales a los usuarios, como si el envío del cuestionario se ha realizado correctamente o no, o mostrar las respuestas de tus usuarios mostrando los resultados del cuestionario (como en una campaña de votación).

{% endtab %}
{% tab Contenido plegable %}

Amplíe sus secciones de contenido utilizando el componente `<amp-accordion>`. Este componente le permite mostrar secciones de contenido desplegables y plegables para que los espectadores puedan echar un vistazo al esquema del contenido y saltar a cualquier sección. 

Si tiende a enviar largos artículos educativos o recomendaciones personalizadas, esto proporciona una forma de que los espectadores echen un vistazo al esquema del contenido y salten a cualquier sección o recomendación de producto específico para obtener más detalles. Esto puede ser especialmente útil para los usuarios de móviles, donde incluso unas pocas frases de una sección requieren desplazarse.
{% endtab %}
{% tab Correos con muchas imágenes %}

Si sueles enviar correos electrónicos con muchas fotos profesionales, como las marcas minoristas, puedes utilizar el componente `<amp-image-lightbox>` que permite a los usuarios interactuar con una imagen que les atraiga. Cuando el usuario hace clic en la imagen, este componente muestra la imagen en el centro del mensaje creando un efecto de lightbox. 

Además, el componente `<amp-image-lightbox>` permite al usuario ver una descripción detallada de la imagen. Puede utilizar el mismo componente para más de una imagen. Por ejemplo, si tiene varias imágenes incluidas en su correo electrónico, cuando el usuario hace clic en una de ellas, la imagen se muestra en el lightbox.

{% endtab %}
{% tab Correos electrónicos basados en fuentes %}

Para los mensajes de correo electrónico que se basan principalmente en la copia de texto, el componente `<amp-fit-text>` permite gestionar el tamaño y el ajuste del texto dentro de un área especificada.

Algunos ejemplos son:

- Escalar el texto para ajustarlo a un área
- Escalar el texto para que quepa en el área utilizando un tamaño de fuente máximo en el que puede establecer el tamaño de fuente máximo.
- Truncar el texto cuando el contenido desborda el área

{% endtab %}
{% endtabs %}

### Utilizar el componente amp-mustache

Al igual que Liquid, AMP admite un lenguaje de scripting para casos de uso más avanzados. Este componente se denomina [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Cuando incluyas cualquier lenguaje de marcado Mustache, tendrás que envolverlo con la etiqueta [`raw`](https://shopify.github.io/liquid/tags/raw/) de Liquid. Tenga en cuenta que Liquid y Mustache comparten el estilo sintáctico. 

Al envolver su contenido alrededor de la etiqueta `raw`, el motor de procesamiento Braze ignorará cualquier contenido entre las etiquetas `raw` y enviará la variable Mustache que su equipo necesite.

## Métricas y análisis

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Detalles</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de aperturas</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Aperturas totales' %} En el caso de los correos electrónicos AMP, se trata del total de aperturas de las versiones HTML y de texto sin formato.</td>
        </tr>
        <tr>
            <td class="no-split">Clics totales</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %} En el caso de los correos electrónicos AMP, se trata del total de clics en las versiones HTML y de texto sin formato.</td>
        </tr>
        <tr>
            <td class="no-split">Aperturas de páginas móviles aceleradas</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">Clics en páginas móviles aceleradas</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Pruebas y resolución de problemas

Tenga en cuenta que los clics totales y los clics únicos no tienen en cuenta los clics que se producen desde un mensaje AMP (sólo HTML y texto sin formato). Los clics específicos de AMP se atribuyen a la métrica *amp_click*.

Antes de enviar tu correo electrónico AMP, te recomendamos que realices una prueba siguiendo estas [directrices de Gmail](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

Para que tu correo electrónico AMP se entregue a cualquier cuenta de Gmail, el correo debe cumplir las siguientes condiciones:

- Deben cumplirse los requisitos de seguridad del AMP para el correo electrónico.
- La parte MIME de AMP debe contener un documento AMP válido.
- El correo electrónico debe incluir la parte MIME AMP antes de la parte MIME HTML.
- La parte MIME de AMP debe ser inferior a 100 KB.

Si ninguna de estas condiciones está causando el error, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/).

### Preguntas más frecuentes

#### ¿Debo segmentar con correos electrónicos AMP?

Abogamos por no segmentar para enviar a todos los tipos de usuarios. Esto se debe a que enviamos mensajes AMP en multiparte, teniendo diferentes versiones incluidas en el correo electrónico original. Si un usuario no puede ver la versión AMP, volverá predeterminada a HTML. 


