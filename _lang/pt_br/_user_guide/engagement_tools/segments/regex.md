---
nav_title: "Expressões regulares"
article_title: Expressões regulares
page_order: 10

description: "Este artigo de referência aborda o que são expressões regulares (regex), como começar a usá-las e oferece a funcionalidade do depurador para validar e testar expressões regulares."
page_type: reference
tool:
  - Testing Tools
  
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Expressões regulares

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> A expressão regular, comumente conhecida como regex, é uma sequência de caracteres que define um padrão de pesquisa. As expressões regulares permitem que você valide agrupamentos de texto e execute ações de localização e substituição. Na Braze, utilizamos expressões regulares para oferecer a você uma solução mais flexível de correspondência de strings em sua segmentação e filtragem de campanhas para seu público-alvo.<br><br>Esta página aborda expressões regulares (regex), como usá-las, perguntas frequentes e fornece um depurador de regex para testar expressões regulares.

No curso vinculado do Braze Learning, mostramos a você como as expressões regulares podem ser usadas e testadas no [Regex101](https://regex101.com/). Também oferecemos um [testador de regex interno](#regex-debugger), uma página de referência útil, dados de amostra referenciados no vídeo do Braze Learning sobre regex, bem como algumas perguntas frequentes.

## Recursos

- Noções [básicas de expressões regulares](https://learning.braze.com/regular-expression-basics-for-braze) Curso do Braze Learning
- [Folha de dicas de Regex]({{site.baseurl}}/regex_cheat_sheet/)
- [Dados de amostra RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Depurador de regex

{% alert important %}
Essa ferramenta serve apenas como referência e não garante que a regex corresponda 100% à plataforma Braze. As expressões regulares no Braze para segmentação e filtros adicionam automaticamente o modificador `/gi`. O [modificador gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) é usado para fazer uma pesquisa sem distinção entre maiúsculas e minúsculas de todas as ocorrências de uma expressão regular em uma cadeia de caracteres.  
<br>
As expressões regulares para propriedades de acionadores de eventos personalizados e filtros de acionadores usam o modificador `/g` (sensível a maiúsculas e minúsculas, consulte o [modificador g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) e não usam o modificador `/i`. Para não haver distinção entre maiúsculas e minúsculas nas propriedades e nos filtros de acionamento de eventos personalizados, use `(?i)`. Por exemplo, o site `Matches regex (?i)STOP(?-i)` captura qualquer uso de "STOP" em qualquer caso (como "stop", "please stop" e "never stop sending me messages").
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
Esse formulário permite a validação básica e o teste de expressões regulares.
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
Valor(es) de verificação: <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
​
Resultados combinados<span id="reg_count"></span>: <div id="regex_results"></div>
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

## Perguntas frequentes

#### O filtro `does not match regex` inclui valores em branco?

Não. Se o valor estiver em branco, o usuário não será incluído no filtro `does not match regex`.

#### Como faço para filtrar endereços de e-mail específicos da caixa de entrada ao segmentar?

{% raw %}
Use o filtro de endereço de e-mail e defina-o como `matches regex`. Em seguida, faça referência ao regex para endereços de e-mail:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Podemos dividir esse regex nas três partes a seguir:

- `[a-zA-Z0-9.+_-]+` é o início do endereço de e-mail antes do caractere `@`. Portanto, o "nome" em "name@example.com".
- `[a-zA-Z0-9.-]+` é a primeira parte do domínio. Portanto, o "exemplo" em "name@example.com".
- `[a-zA-Z.-]+` é a última parte do domínio. Portanto, o "com" em "name@example.com".

{% endraw %}

#### Como faço para filtrar os endereços de e-mail associados a um domínio específico?

Digamos que você queira filtrar os e-mails que terminam com "@braze.com". Você usaria o filtro de endereço de e-mail, o definiria como `matches regex` e digitaria "@braze.com" no campo regex. O mesmo se aplica a qualquer outro domínio de e-mail.

\![Filtro para um endereço de e-mail que corresponda ao regex de "@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})

#### Como posso usar cadeias de números de filtro para valores ≥ x ou ≤ x?

Se estiver pesquisando valores maiores ou iguais a (≥) x, use a seguinte regex:

```
^([x-y]|\d{z,})$
```

Em que `x-y` é o intervalo de números (0-9) do primeiro dígito e `z` é o número de dígitos a mais de x. Por exemplo, para valores maiores ou iguais a 50, o regex seria `^([5-9][0-9]|\d{3,})$`.

Se estiver pesquisando valores menores ou iguais a (≤) x, use a seguinte regex:

```
^([x-y]|[a-b])$
```

Onde `x-y` é o intervalo de números (0-9) do primeiro dígito e `a-b` é o intervalo de limite inferior de x. Por exemplo, para valores menores ou iguais a 50, o regex seria `^([5-9][0-9]|[0-4][0-9])$`.

#### Como faço para filtrar atributos personalizados que começam com uma cadeia de caracteres específica?

Use o símbolo do cursor (`^`) para indicar com o que a string começa e, em seguida, digite o nome do atributo personalizado que você deseja especificar.

Por exemplo, se você estiver tentando segmentar usuários que moram em cidades que começam com "San", seu regex seria `^San \w`. Com essa regex, você segmentaria com sucesso usuários de cidades como São Francisco, San Diego, San Jose e assim por diante.

\![Filtro para uma cidade que corresponda ao regex de "^San \\w".]({% image_buster /assets/img/regex/regeximg2.png %})

#### Como faço para filtrar números de telefone específicos?

Antes de usar regex para filtrar números de telefone, lembre-se de que os números registrados nos perfis de usuário devem estar no formato [E.164](https://en.wikipedia.org/wiki/E.164) conforme especificado em [Números de telefone do usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/).

Supondo que você esteja pesquisando números de telefone dos EUA, use o formato regex `1?\d\d\d\d\d\d\d\d\d\d`, em que cada repetição de `\d` é um dígito que você deseja especificar. Os três primeiros dígitos são o código de área.

Da mesma forma, o formato dos números de telefone do Reino Unido é `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Qualquer outro país teria o código do respectivo país, seguido do número necessário de `\d` repetições para cada dígito restante. Portanto, no caso da Lituânia, com um código de país "3", o regex seria `^\+3\d\d\d\d\d\d\d\d\d\d`.

Por exemplo, digamos que você queira filtrar os usuários por número de telefone para um código de área específico, "718". Use o filtro de número de telefone, defina-o como `matches regex` e digite a seguinte regex:

```
^1?718\d\d\d\d\d\d\d
```

\![Filtro para um número de telefone que corresponda ao regex de "^1?718\\d\\d\\d\\d\\d\\d\\d\\d\\d".]({% image_buster /assets/img/regex/regeximg3.png %})


