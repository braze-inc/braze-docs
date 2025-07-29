---
nav_title: Validación de correo electrónico 
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

La validación del correo electrónico se realiza cuando la dirección de correo electrónico de un usuario se ha actualizado o se está importando a Braze mediante API, carga CSV o SDK, o se ha modificado en el panel de control. Tenga en cuenta que sus direcciones de correo electrónico no pueden incluir espacios en blanco. Si utilizas la API, los espacios en blanco provocarán un error en `400`.

Braze no acepta ciertos caracteres y los reconoce como no válidos. Si un correo electrónico es rebotado, Braze marca el correo electrónico como no válido y el estado de la suscripción no se modifica.  

{% details Caracteres aceptados %}
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

{% details Caracteres no aceptados %}
- Espacios en blanco (ASCII y Unicode)
{% enddetails %}

Esta validación no debe confundirse con un servicio de validación como Briteverify. Se trata de una comprobación para verificar que la sintaxis de una dirección de correo electrónico es correcta. Uno de los principales motivos para utilizar este proceso de validación es admitir caracteres internacionales (como UTF-8) en la parte local de la dirección de correo electrónico.

La validación de la sintaxis del correo electrónico examina tanto la parte local como la parte de host de una dirección de correo electrónico. La parte local es cualquier cosa antes del asperando (@), y la parte host es cualquier cosa después del asperando. Por ejemplo, esta parte local de una dirección de correo electrónico puede empezar y terminar con cualquiera de los caracteres permitidos excepto un punto (.). Tenga en cuenta que este proceso sólo valida la sintaxis de la dirección de correo electrónico y no tiene en cuenta si el dominio tiene un servidor MX válido o si el usuario existe en el dominio indicado.

{% alert note %}
Si la parte del dominio contiene caracteres no [ASCII](https://en.wikipedia.org/wiki/ASCII), deberá [codificarse con Punycode](https://www.punycoder.com/) antes de enviarla a Braze.
{% endalert %}

Si Braze recibe una solicitud para añadir un usuario y la dirección de correo electrónico se considera no válida, verá una respuesta de error en la API. Al cargar mediante CSV, se creaba un usuario, pero no se añadía la dirección de correo electrónico.

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

Si la parte del dominio es una dirección de Gmail, la parte local debe tener al menos dos caracteres y debe seguir la validación de expresión regular indicada anteriormente.

### Dominios Microsoft

Si el dominio del host incluye "msn", "hotmail", "outlook" o "live", se utilizará la siguiente expresión regular para validar la parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La parte local de la dirección Microsoft debe seguir estos parámetros:

- Puede empezar por un carácter (a-z), un guión bajo (_) o un número (0-9).  
- Puede contener cualquier carácter alfanumérico (a-z o 0-9) o un guión bajo (_)
- Puede contener los siguientes caracteres: (.) o (-) o (+) o (^)
- No puede empezar por punto (.)
- No puede contener dos o más puntos consecutivos (.)
- No puede terminar con un punto (.)

Tenga en cuenta que la prueba de validación comprueba si la parte local, que precede al "+", coincide con la expresión regular.

## Reglas de validación de la parte anfitriona

Las direcciones IPv4 o IPv6 no están permitidas en la parte del host de una dirección de correo electrónico. El dominio de primer nivel (como .com, .org, .net, etc.) puede no ser totalmente numérico.

La siguiente expresión regular se utiliza para validar el dominio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

El nombre de dominio debe seguir estos parámetros:

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

La etiqueta final del dominio debe ser un dominio de nivel superior (TLD) válido, que viene determinado por todo lo que aparece después del punto final (.). Este TLD debería estar en [la lista de TLD de ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). El validador de correo electrónico Braze sólo comprueba que la sintaxis del correo electrónico sea correcta según la expresión regular indicada en esta sección. No detecta errores tipográficos ni direcciones que no existen.

{% alert important %}
Unicode sólo se acepta para la parte local de la dirección de correo electrónico. No se acepta Unicode para la parte del dominio, pero puede codificarse en Punycode.
{% endalert %}

