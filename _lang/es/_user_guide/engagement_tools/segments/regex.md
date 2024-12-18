---
nav_title: "Expresiones regulares"
article_title: Expresiones regulares
page_order: 6

description: "Este artículo de referencia explica qué son las expresiones regulares (regex), cómo empezar a utilizarlas y ofrece funciones de depuración para validar y probar las expresiones regulares."
page_type: reference
tool:
  - Testing Tools
  
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Expresiones regulares

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> Una expresión regular, conocida comúnmente como regex, es una secuencia de caracteres que define un patrón de búsqueda. Las expresiones regulares permiten validar agrupaciones de texto y realizar acciones de búsqueda y sustitución. En Braze, aprovechamos las expresiones regulares para ofrecerle una solución de concordancia de cadenas más flexible en su segmentación y filtrado de campañas para su público objetivo.<br><br>Esta página trata de las expresiones regulares (regex), cómo utilizarlas, las preguntas más frecuentes, y proporciona un depurador regex para probar las expresiones regulares.

En el curso Braze Learning vinculado, le mostramos cómo se pueden utilizar y probar las expresiones regulares en [Regex101][regex]. También ofrecemos un [comprobador interno de regex](#regex-debugger), una útil página de referencia, datos de muestra a los que se hace referencia en el video Braze Learning sobre regex, así como algunas preguntas frecuentes.

## Recursos

- [Conceptos básicos de expresiones regulares](https://learning.braze.com/regular-expression-basics-for-braze) Curso Braze Learning
- [Hoja de referencia de regex]({{site.baseurl}}/regex_cheat_sheet/)
- [Datos de muestra RTF][dummydata]

## Depurador regex

{% alert important %}
Esta herramienta sólo sirve de referencia y no garantiza que la expresión regular coincida al 100% con la plataforma Braze. Las expresiones regulares en Braze para segmentar y filtrar añaden automáticamente el modificador `/gi`. El [modificador gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) se utiliza para realizar una búsqueda sin distinción entre mayúsculas y minúsculas de todas las apariciones de una expresión regular en una cadena.  
<br>
Las expresiones regulares para las propiedades del evento personalizado y los filtros de desencadenamiento utilizan el modificador `/g` (distingue entre mayúsculas y minúsculas, consulta el [modificador g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) y no utilizan el modificador `/i`. Para no distinguir entre mayúsculas y minúsculas en las propiedades del evento personalizado que lo desencadenan y en los filtros de desencadenamiento, utiliza `(?i)`. Por ejemplo, `Matches regex (?i)STOP(?-i)` capta cualquier uso de "STOP" en cualquier caso (como "para", "por favor, para" y "nunca dejes de enviarme mensajes").
{% endalert %}

{% tabs %}
{% tab Depurador regex %}
<div>
Este formulario permite la validación básica y la comprobación de expresiones regulares.
​
Regex:
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
Comprobar valor(es): <textarea style="" placeholder="cadena coincidente" id="regex_text"></textarea><br /><br />
​
Resultados emparejados<span id="reg_count"></span>: <div id="regex_results"></div>
</div>
<style type="text/css">
#regex_text {
  -moz-appearance: textfield-multiline;
  -webkit-appearance: textarea;
  border: 1px solid #ced4da !important;
  overflow: auto;
  padding: 2px;
  resize: both;
  white-space: pre-wrap;
  width:100%;
  height: 250px;
  padding: 5px 15px 5px 1.2em;
  border-radius: 0.25rem;
}
#regex_input {
  border: 1px solid #ced4da !important;
  padding: 0 15px 0 5px;
}
#regex_input.invalid {
  background-color: #f8eef7;
}
.regex_highlight {
  background-color: #66d4b333;
}
#regex_results {
  width: 100%;
  min-height: 2em;
  padding: 5px 15px 5px 0.2em;
}
</style>
<script type="text/javascript">
$( document ).ready(function() {
  function update_inputmatch() {
    var tomatch = $('#regex_input').val();
    var validreg = true;
    $('#regex_input').removeClass('invalid');
    try {
      var regex = new RegExp(tomatch,'gi');
      $('#regex_results').html('');
    } catch(e) {
      $('#regex_input').addClass('invalid');
      validreg = false;
      $('#regex_results').html('Invalid Regular Expression').prepend('&nbsp;&nbsp;&nbsp;');
    }
    if (validreg){
      if ($('#regex_text').val() ) {
        if (tomatch) {
          var input_str = $('#regex_text').val().split(/\r?\n/);
          var input_replaced = [];
          var reg_count = 0;
          for (var i = 0; i < input_str.length; i++) {
            var inp_rep = ''
            var matched = input_str[i].match(regex);
            if (matched) {
              inp_rep = '<i class="far fa-check-square"></i> ';
              reg_count++;
            }
            else {
              inp_rep = '<i class="far fa-square"></i> ';
            }
            inp_rep += input_str[i].replace(regex,'<span class="regex_highlight">$&</span>');
            input_replaced.push(inp_rep)
          }
          if (reg_count) {
            $('#reg_count').html(' (' + reg_count + ')');
          }
          else {
            $('#reg_count').html('');
          }
          $('#regex_results').html(input_replaced.join('<br />'));
        }
      }
      else {
        $('#regex_results').html('');
      }
    }
  }
  $('#regex_input, #regex_text').keyup(function(k){
    update_inputmatch();
  });
});
</script>

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes

#### ¿Incluye el filtro `does not match regex` los valores en blanco?

No. Si el valor está en blanco, el usuario no se incluirá en el filtro `does not match regex`.

#### ¿Cómo filtro las direcciones de correo electrónico específicas de la bandeja de entrada al segmentar?

{% raw %}
Utilice el filtro de direcciones de correo electrónico, configúrelo en `matches regex`. A continuación, haga referencia a la expresión regular para las direcciones de correo electrónico:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Podemos dividir esta expresión regular en las tres partes siguientes:

- `[a-zA-Z0-9.+_-]+` es el comienzo de la dirección de correo electrónico antes del carácter at `@`. Así que el "nombre" en "name@example.com".
- `[a-zA-Z0-9.-]+` es la primera parte del dominio. Así que el "ejemplo" en "name@example.com".
- `[a-zA-Z.-]+` es la última parte del dominio. Así que la "com" en "name@example.com".

{% endraw %}

#### ¿Cómo puedo filtrar las direcciones de correo electrónico asociadas a un dominio específico?

Digamos que desea filtrar los correos electrónicos que terminan en "@braze.com". Utilice el filtro de direcciones de correo electrónico, configúrelo en `matches regex` e introduzca "@braze.com" en el campo regex. Lo mismo se aplica a cualquier otro dominio de correo electrónico.

![Filtrar una dirección de correo electrónico que coincida con el regex de "@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})

#### Cómo puedo utilizar cadenas de números de filtro para valores ≥ x o ≤ x?

Si buscas valores mayores o iguales que (≥) x, utiliza la siguiente expresión regular:

```
^([x-y]|\d{z,})$
```

Donde `x-y` es el rango de números (0-9) del primer dígito, y `z` es el más el número de dígitos de x. Por ejemplo, para valores mayores o iguales que 50, el regex sería `^([5-9][0-9]|\d{3,})$`.

Si buscas valores menores o iguales que (≤) x, utiliza la siguiente expresión regular:

```
^([x-y]|[a-b])$
```

Donde `x-y` es el rango de números (0-9) del primer dígito, y `a-b` es el rango del límite inferior de x. Por ejemplo, para valores mayores o iguales que 50, el regex sería `^([5-9][0-9]|[0-4][0-9])$`.

#### ¿Cómo puedo filtrar los atributos personalizados que empiezan por una cadena determinada?

Utilice el símbolo de intercalación (`^`) para indicar el comienzo de la cadena y, a continuación, introduzca el nombre del atributo personalizado que desea especificar.

Por ejemplo, si intenta dirigirse a usuarios que viven en ciudades que empiezan por "San", su regex sería `^San \w`. Con esta expresión regular, podrá dirigirse a usuarios de ciudades como San Francisco, San Diego, San José, etc.

![Filtrar por una ciudad que coincida con el regex de "^San \\w".]({% image_buster /assets/img/regex/regeximg2.png %})

#### ¿Cómo puedo filtrar por números de teléfono específicos?

Antes de utilizar regex para filtrar números de teléfono, recuerde que los números registrados para perfiles de usuario deben tener el formato [E.164](https://en.wikipedia.org/wiki/E.164) tal y como se especifica en [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/).

Suponiendo que busques números de teléfono de EE.UU., utiliza el formato regex `1?\d\d\d\d\d\d\d\d\d\d`, donde cada repetición de `\d` es un dígito que quieres especificar. Los tres primeros dígitos son el prefijo.

Asimismo, el formato de los números de teléfono del Reino Unido es `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Cualquier otro país sería el código de país respectivo, seguido del número necesario de repeticiones `\d` para cada dígito restante. Así, en el caso de Lituania, con un código de país "3", su regex sería `^\+3\d\d\d\d\d\d\d\d\d\d`.

Por ejemplo, supongamos que desea filtrar usuarios por número de teléfono para un código de área específico, "718". Utilice el filtro de número de teléfono, configúrelo en `matches regex` e introduzca la siguiente expresión regular:

```
^1?718\d\d\d\d\d\d\d
```

![Filtrar un número de teléfono que coincida con la regex de "^1?718\\d\\d\\d\\d\\d\\d".]({% image_buster /assets/img/regex/regeximg3.png %})


[regex]: https://regex101.com/
[dummydata]: {% image_buster /assets/download_file/regex-dummy-data.rtf %}
