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

La validación del correo electrónico se realiza cuando la dirección de correo electrónico de un usuario se ha actualizado o se está importando a Braze mediante la API, la carga CSV o el SDK, o se ha modificado en el panel. Ten en cuenta que tus direcciones de correo electrónico no pueden incluir espacios en blanco. Si utilizas la API, los espacios en blanco provocarán un error en `400`.

Braze no acepta ciertos caracteres y los reconoce como no válidos. Si un correo electrónico es rebotado, Braze marca el correo electrónico como no válido, y el estado de la suscripción no se modifica. Ten en cuenta que si hay caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII) no estándar en el cuerpo del correo electrónico, éste no se enviará.

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

Esta validación no debe confundirse con un servicio de validación. Se trata de una comprobación para verificar que la sintaxis de una dirección de correo electrónico es correcta. Uno de los principales motivos para utilizar este proceso de validación es admitir caracteres internacionales (como UTF-8) en la parte local de la dirección de correo electrónico.

La validación sintáctica del correo electrónico examina las partes local y host de una dirección de correo electrónico. La parte local es todo lo que va antes del asperando (@), y la parte host es todo lo que va después del asperando. Por ejemplo, esta parte local de una dirección de correo electrónico puede empezar y terminar con cualquiera de los caracteres permitidos, excepto un punto (.). Ten en cuenta que este proceso sólo valida la sintaxis de la dirección de correo electrónico y no tiene en cuenta si el dominio tiene un servidor MX válido o si el usuario existe en el dominio indicado.

{% alert important %}
Si la parte del dominio contiene caracteres ASCII no estándar, habrá que [codificarla con Punycode](https://www.punycoder.com/) antes de suministrársela a Braze.
{% endalert %}

Si Braze recibe una solicitud para añadir un usuario y la dirección de correo electrónico se considera no válida, verás una respuesta de error en la API. Al cargar con un archivo CSV, se creaba un usuario, pero no se añadía la dirección de correo electrónico.

## Reglas locales de validación de piezas

### Validación general del correo electrónico

Para la mayoría de los dominios, la parte local debe seguir estos parámetros:
- Puede contener cualquier letra, número, incluidas las letras y números Unicode, así como los siguientes caracteres: (+) (&) (#) (_) (-) (^) o (/)
- Puede contener, pero no empezar ni terminar con el siguiente carácter: (.)
- No puede contener comillas dobles (")
- Debe tener entre 1 y 64 caracteres

La siguiente expresión regular puede utilizarse para validar si una dirección de correo electrónico se considerará válida:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Direcciones de Gmail

Si la parte del dominio es una dirección de Gmail, la parte local debe tener al menos dos caracteres y debe seguir la validación de expresión regular indicada anteriormente.

### Dominios Microsoft

Si el dominio del host incluye "msn", "hotmail", "outlook" o "en vivo", se utilizará la siguiente expresión regular para validar la parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La parte local de la dirección de Microsoft debe seguir estos parámetros:

- Puede empezar por un carácter (a-z), un guión bajo (_), o un número (0-9).  
- Puede contener cualquier carácter alfanumérico (a-z o 0-9) o un guión bajo (_)
- Puede contener los siguientes caracteres: (.) o (-)
- No puede empezar con un punto (.)
- No puede contener dos o más puntos consecutivos (.)
- No puede terminar con un punto (.)

Observa que la prueba de validación comprueba si la parte local, que precede al "+", coincide con la expresión regular.

## Reglas de validación de la parte anfitriona

Las direcciones IPv4 o IPv6 no están permitidas en la parte del host de una dirección de correo electrónico. El dominio de primer nivel (como .com, .org, .net, etc.) puede no ser totalmente numérico.

La siguiente expresión regular se utiliza para validar el dominio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

El nombre del dominio debe seguir estos parámetros:

- Consta de dos o más etiquetas separadas por puntos
	- Cada parte de un nombre de dominio se denomina "etiqueta". Por ejemplo, el nombre de dominio "example.com" está formado por la etiqueta "ejemplo" y la etiqueta "com".
- Debe contener al menos un punto (.)
- No puede contener dos o más periodos consecutivos
- Cada etiqueta separada por puntos debe
	- Sólo contiene caracteres alfanuméricos (a-z o 0-9) y el guión (-)
	- Empieza con un carácter alfanumérico (a-z o 0-9)
	- Termina con un carácter alfanumérico (a-z o 0-9)
	- Contienen de 1 a 63 caracteres

### Se requiere validación adicional

La etiqueta final del dominio debe ser un dominio de nivel superior (TLD) válido, que viene determinado por todo lo que aparece después del punto final (.). Este TLD debería estar en [la lista de TLD de la ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). El validador de correo electrónico Braze sólo comprueba que la sintaxis del correo electrónico sea correcta de acuerdo con la expresión regular indicada en esta sección. No detecta erratas ni direcciones que no existen.

{% alert important %}
Sólo se acepta Unicode para la parte local de la dirección de correo electrónico. No se acepta Unicode para la parte del dominio, pero puede codificarse en Punycode.
{% endalert %}

