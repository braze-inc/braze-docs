---
nav_title: Validación del correo electrónico
article_title: Validación de correo electrónico
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre las reglas de validación de la parte local y del host para las direcciones de correo electrónico."
channel: email

---

# Validación del correo electrónico

> Este artículo de referencia cubre las reglas de validación de la parte local y del host para las direcciones de correo electrónico. La validación se utiliza para las direcciones de correo electrónico del panel, las direcciones de correo electrónico del usuario final (tus clientes) y las direcciones de origen y de respuesta a de un mensaje de mensajería.

## Cómo funciona

Braze valida una dirección de correo electrónico cuando se actualiza, importa por API, carga CSV, SDK o modifica en el panel. Las direcciones de correo electrónico no pueden incluir espacios en blanco. Si utilizas la API, los espacios en blanco devuelven un error `400`.

Braze rechaza ciertos caracteres y marca la dirección como no válida. Si un correo electrónico rebota, Braze marca la dirección como no válida y no cambia el estado de la suscripción. Si el cuerpo del correo electrónico contiene caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII) no estándar, Braze no envía el correo electrónico.

{% details Accepted characters %}
- Letras (A-Z)
- Números (0-9)
- Símbolos
	- -
	- ^
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- \`
	- \|
	- ~
	- ¡!
	- ?
	- . (sólo entre letras u otros caracteres)
{% enddetails %}

{% details Unaccepted characters %}
- Espacios en blanco (ASCII y Unicode)
{% enddetails %}

Esta validación es una comprobación sintáctica, no un servicio de validación. Uno de los objetivos de este proceso es admitir caracteres internacionales (como UTF-8) en la parte local de la dirección de correo electrónico.

Braze valida la sintaxis de las partes local y host de una dirección de correo electrónico. La parte local es todo lo que va antes del asperando (@); la parte host es todo lo que va después. La parte local puede empezar y terminar con cualquier carácter permitido, excepto un punto (.). Este proceso no tiene en cuenta si el dominio tiene un servidor MX válido o si existe un usuario en ese dominio.

{% alert important %}
Si la parte del dominio contiene caracteres ASCII no estándar, habrá que [codificarla con Punycode](https://www.punycoder.com/) antes de suministrársela a Braze.
{% endalert %}

Si Braze recibe una solicitud para añadir un usuario con una dirección de correo electrónico no válida, la API devuelve un error. Para una carga CSV, Braze crea el usuario pero omite la dirección de correo electrónico no válida.

## Reglas locales de validación de piezas

### Validación general del correo electrónico

Para la mayoría de los dominios, la parte local debe seguir estos parámetros:
- Puede contener cualquier letra, número, incluidas las letras y números Unicode, así como los siguientes caracteres: (+) (&) (#) (_) (-) (^) o (/)
- Puede contener el carácter siguiente, pero no puede empezar ni terminar con él: (.)
- No puede contener comillas dobles (")
- Debe tener entre 1 y 64 caracteres

La siguiente expresión regular puede utilizarse para validar si una dirección de correo electrónico se considerará válida:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Direcciones de Gmail

Si la parte del dominio es Gmail, la parte local debe tener al menos dos caracteres y seguir la validación de expresión regular indicada anteriormente.

### Dominios Microsoft

Si el dominio del host incluye "msn", "hotmail", "outlook" o "en vivo", Braze utiliza la siguiente expresión regular para validar la parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La parte local de la dirección Microsoft debe seguir estos parámetros:

- Puede empezar por un carácter (a-z), un guión bajo (_), o un número (0-9).  
- Puede contener cualquier carácter alfanumérico (a-z o 0-9) o un guión bajo (_)
- Puede contener los siguientes caracteres: (.) o (-)
- No puede empezar por punto (.)
- No puede contener dos o más puntos consecutivos (.)
- No puede terminar con un punto (.)

La prueba de validación comprueba si la parte local que precede al "+" coincide con la expresión regular.

## Reglas de validación de la parte anfitriona

La parte del host no puede ser una dirección IPv4 o IPv6. El dominio de primer nivel (como .com, .org, .net) no puede ser totalmente numérico.

La siguiente expresión regular se utiliza para validar el dominio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

El nombre de dominio debe cumplir estos parámetros:

- Consta de dos o más etiquetas separadas por puntos
	- Cada parte de un nombre de dominio se denomina "etiqueta". Por ejemplo, el nombre de dominio "example.com" está formado por la etiqueta "ejemplo" y la etiqueta "com".
- Debe contener al menos un punto (.)
- No puede contener dos o más periodos consecutivos
- Cada etiqueta separada por puntos debe:
	- Sólo contiene caracteres alfanuméricos (a-z o 0-9) y el guión (-)
	- Empieza por un carácter alfanumérico (a-z o 0-9)
	- Terminar con un carácter alfanumérico (a-z o 0-9)
	- Contiene de 1 a 63 caracteres

### Se requiere validación adicional

La etiqueta final del dominio debe ser un dominio de nivel superior (TLD) válido, determinado por cualquier cosa después del punto final (.). Este TLD debería aparecer en [la lista de TLD de la ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). El validador de Braze sólo comprueba la sintaxis. No detecta errores tipográficos ni direcciones inexistentes.

{% alert important %}
Unicode sólo se acepta para la parte local de la dirección de correo electrónico. No se acepta Unicode para la parte del dominio, pero puede codificarse en Punycode.
{% endalert %}

