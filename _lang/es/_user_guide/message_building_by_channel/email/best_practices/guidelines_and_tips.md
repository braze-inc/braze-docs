---
nav_title: Directrices para el correo electrónico
article_title: Directrices para el correo electrónico
page_order: 1
page_type: reference
description: "Este artículo trata de consejos y trucos generales que debes tener en cuenta a la hora de crear campañas de correo electrónico para diversos casos de uso y temas."
channel: email

---

# Directrices para el correo electrónico

> Al crear tu campaña de correo electrónico, es importante que tengas en cuenta cómo se reciben tus mensajes de mensajería entre tus distintos usuarios y proveedores de servicios de correo electrónico (ESP). 

He aquí algunos consejos rápidos que debes tener en cuenta al elaborar tu contenido:

- Cuando formatees tu correo electrónico, utiliza hojas de estilo en línea como CSS.
- Para utilizar una plantilla de correo electrónico tanto para la versión móvil como para la de escritorio, mantén la anchura por debajo de 500 píxeles.
- Las imágenes cargadas en la plantilla de correo electrónico deben ocupar menos de 5 MB. Los formatos admitidos son PNG, JPEG y GIF.
- No establezcas alturas y anchuras para las imágenes, ya que esto provocará espacios en blanco innecesarios en un correo electrónico degradado.
- `div` ya que la mayoría de los clientes de correo electrónico no admiten su uso. En su lugar, utiliza tablas anidadas.
- Evita utilizar JavaScript porque no funciona con ningún ESP.
- Braze mejora los tiempos de carga utilizando una CDN global para alojar todas las imágenes de correo electrónico.

### Implementar texto alternativo

Dado que los filtros de correo no deseado buscan tanto la versión HTML como la de texto sin formato de un mensaje, utilizar alternativas de texto sin formato es una forma estupenda de reducir tu puntuación de correo no deseado. Además, el texto alternativo `(alt="")` puede servir para complementar y, en algunos casos, sustituir a las imágenes incluidas en el cuerpo de tu correo electrónico que puedan haber sido filtradas por el proveedor de correo electrónico del usuario. Los lectores de pantalla anuncian el texto alternativo para explicar las imágenes, por lo que ésta es una oportunidad para utilizar el lenguaje llano para proporcionar información clave sobre una imagen.

### Validación del correo electrónico

{% alert important %}
La validación se utiliza para las direcciones de correo electrónico del panel de control, las direcciones de correo electrónico del usuario final (tus clientes) y las direcciones de origen y de respuesta a de un mensaje de mensajería.
{% endalert %}

La validación del correo electrónico se realiza cuando se ha actualizado la dirección de correo electrónico de un usuario o se está importando a Braze mediante API, carga CSV, SDK o modificando en el panel. Ten en cuenta que tus direcciones de correo electrónico no pueden incluir espacios en blanco, y si se envían utilizando la API, los espacios en blanco provocarán un error 400.

Las direcciones de correo electrónico dirigidas a través de los servidores Braze deben validarse según las normas [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822), Braze no acepta determinados caracteres y los reconoce como no válidos. Si un correo electrónico es rebotado, Braze marca el correo electrónico como no válido y el estado de la suscripción no se modifica. 

{% details Unaccepted characters outside of RFC standards %}
- *
- /
- ?
- ¡!
- $
- #
- %
- ^
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

### Configuración de las direcciones de origen y de respuesta a

Cuando configures tus direcciones "de", asegúrate de que tu dominio de correo electrónico "de" coincide con tu dominio de envío (como `marketing.yourdomain.com`). Si no lo haces, puede producirse una desalineación entre SPF y DKIM. Todos los correos electrónicos de respuesta se pueden configurar en tu dominio raíz.

{% alert note %}
No se admite la codificación Unicode en las direcciones "de".
{% endalert %}

### Comprobar detalles HTML

Ten en cuenta que algunas etiquetas y atributos HTML no están permitidos, ya que podrían permitir la ejecución de código malicioso en el navegador.

Consulta las siguientes listas de etiquetas y atributos HTML que no están permitidos en tus correos electrónicos:
{% details Expand for disallowed HTML tags %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Expand for disallowed HTML attributes %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}



