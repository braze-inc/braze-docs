---
nav_title: Directrices de correo electrónico
article_title: Directrices de correo electrónico
page_order: 1
page_type: reference
description: "En este artículo se incluyen consejos y trucos generales que debe tener en cuenta a la hora de crear campañas de correo electrónico para distintos casos de uso y temas."
channel: email

---

# Directrices de correo electrónico

> A la hora de crear una campaña de correo electrónico, es importante tener en cuenta cómo se reciben los mensajes en los distintos usuarios y proveedores de servicios de correo electrónico (ESP). 

Estos son algunos consejos rápidos que debes tener en cuenta al elaborar tu contenido:

- Cuando formatees tu correo electrónico, utiliza hojas de estilo en línea como CSS.
- Para utilizar una plantilla de correo electrónico para las versiones móvil y de escritorio, mantenga la anchura por debajo de 500 píxeles.
- Las imágenes cargadas en la plantilla de correo electrónico deben ocupar menos de 5 MB. Los formatos admitidos son PNG, JPEG y GIF.
- No establezcas alturas y anchuras para las imágenes, ya que esto provocará espacios en blanco innecesarios en un correo electrónico degradado.
- No se deberían usar etiquetas `div` ya que la mayoría de los clientes de correo electrónico no admiten su uso. En su lugar, utilice tablas anidadas.
- Evita utilizar JavaScript porque no funciona con ningún ESP.
- Braze mejora los tiempos de carga utilizando una CDN global para alojar todas las imágenes de correo electrónico.

### Implementar texto alternativo

Dado que los filtros de spam buscan tanto una versión HTML como una versión en texto plano de un mensaje, utilizar alternativas en texto plano es una buena forma de reducir la puntuación de spam. Además, el texto alternativo `(alt="")` puede servir para complementar y, en algunos casos, sustituir a las imágenes incluidas en el cuerpo del mensaje que hayan sido filtradas por el proveedor de correo electrónico del usuario. Los lectores de pantalla anuncian el texto alternativo para explicar las imágenes, por lo que se trata de una oportunidad para utilizar el lenguaje llano para proporcionar información clave sobre una imagen.

### Validación del correo electrónico

{% alert important %}
La validación se utiliza para las direcciones de correo electrónico del panel de control, las direcciones de correo electrónico de los usuarios finales (sus clientes) y las direcciones de remitente y destinatario de respuesta de un mensaje de correo electrónico.
{% endalert %}

La validación del correo electrónico se realiza cuando la dirección de correo electrónico de un usuario se ha actualizado o se está importando en Braze a través de la API, la carga CSV, el SDK o se ha modificado en el panel de control. Tenga en cuenta que sus direcciones de correo electrónico no pueden incluir espacios en blanco, y si se envían utilizando la API, los espacios en blanco darán lugar a un error 400.

Las direcciones de correo electrónico dirigidas a través de los servidores Braze deben ser validadas según las normas [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822), Braze no acepta ciertos caracteres y los reconoce como no válidos. Si un correo electrónico es rebotado, Braze marca el correo electrónico como no válido y el estado de la suscripción no se modifica. 

{% details Caracteres no aceptados fuera de las normas RFC %}
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

### Establecer direcciones de origen y de respuesta

Cuando configure sus direcciones "de", asegúrese de que su dominio de correo electrónico "de" coincide con su dominio de envío (como `marketing.yourdomain.com`). Si no lo hace, puede producirse una desalineación entre SPF y DKIM. Todos los correos electrónicos de respuesta se pueden configurar en tu dominio raíz.

{% alert note %}
No se admite la codificación Unicode en las direcciones "de".
{% endalert %}

### Comprobación de los detalles HTML

Tenga en cuenta que algunas etiquetas y atributos HTML no están permitidos, ya que pueden permitir la ejecución de código malicioso en el navegador.

Consulte las siguientes listas de etiquetas y atributos HTML que no están permitidos en sus mensajes de correo electrónico:
{% details Ampliar para etiquetas HTML no permitidas %}
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

{% details Ampliar para atributos HTML no permitidos %}
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



