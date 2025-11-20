---
nav_title: "Reguläre Ausdrücke"
article_title: Reguläre Ausdrücke
page_order: 10

description: "In diesem Referenzartikel erfahren Sie, was reguläre Ausdrücke (Regex) sind, wie Sie sie verwenden können und welche Debugger-Funktionen zum Überprüfen und Testen regulärer Ausdrücke zur Verfügung stehen."
page_type: reference
tool:
  - Testing Tools
  
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Reguläre Ausdrücke

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> Ein regulärer Ausdruck, allgemein als Regex bekannt, ist eine Zeichenfolge, die ein Suchmuster definiert. Mit regulären Ausdrücken können Sie Textgruppierungen validieren und Such- und Ersetzungsaktionen durchführen. Bei Braze nutzen wir reguläre Ausdrücke, um Ihnen eine flexiblere Lösung für den String-Abgleich bei der Segmentierung und dem Filtern von Kampagnen für Ihre Zielgruppe zu bieten.<br><br>Diese Seite befasst sich mit regulären Ausdrücken (regex), ihrer Verwendung, häufig gestellten Fragen und bietet einen regex Debugger zum Testen regulärer Ausdrücke.

In dem verlinkten Kurs von Braze Learning zeigen wir Ihnen, wie reguläre Ausdrücke auf [Regex101](https://regex101.com/) verwendet und getestet werden können. Wir bieten auch einen [internen Regex-Tester](#regex-debugger), eine hilfreiche Referenzseite, Beispieldaten, auf die im Regex-Braze-Lernvideo verwiesen wird, sowie einige häufig gestellte Fragen.

## Ressourcen

- [Grundlagen regulärer Ausdrücke](https://learning.braze.com/regular-expression-basics-for-braze) Braze-Lernkurs
- [Kurzübersicht über reguläre Ausdrücke]({{site.baseurl}}/regex_cheat_sheet/)
- [Beispieldaten RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Regex Debugger

{% alert important %}
Dieses Tool dient nur als Referenz und garantiert nicht, dass die Regex zu 100 % mit der Braze-Plattform übereinstimmt. Reguläre Ausdrücke in Braze für Segmentierung und Filter fügen automatisch den Modifikator `/gi` hinzu. Der [gi-Modifikator](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) wird verwendet, um alle Vorkommen eines regulären Ausdrucks in einer Zeichenfolge unabhängig von der Groß-/Kleinschreibung zu durchsuchen.  
<br>
Reguläre Ausdrücke für angepasste Event-Eigenschaften und Trigger-Filter verwenden den `/g`-Modifikator (Groß-/Kleinschreibung beachten, siehe [g-Modifikator](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) und verwenden nicht den `/i`-Modifikator. Um die Groß-/Kleinschreibung bei angepassten Event-Eigenschaften und Trigger-Filtern nicht zu beachten, verwenden Sie stattdessen `(?i)`. Zum Beispiel fängt `Matches regex (?i)STOP(?-i)` jede Verwendung von „STOP“ in jedem Fall ab (z. B. „stopp“, „bitte aufhören“ und „hör nie auf, mir Nachrichten zu schicken“).
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
Dieses Formular ermöglicht die grundlegende Validierung und das Testen von regulären Ausdrücken.
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
Wert(e) prüfen: <textarea style="" placeholder="String abgleichen" id="regex_text"></textarea><br /><br />
​
Abgestimmte Ergebnisse<span id="reg_count"></span>: <div id="regex_results"></div>
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

## Häufig gestellte Fragen

#### Schließt der `does not match regex` Filter auch leere Werte ein?

Nein. Wenn der Wert leer ist, wird der oder die Nutzer:in nicht in den Filter von `does not match regex` aufgenommen.

#### Wie kann ich bei der Segmentierung nach posteingangsspezifischen E-Mail-Adressen filtern?

{% raw %}
Verwenden Sie den Filter für E-Mail-Adressen, setzen Sie ihn auf `matches regex`. Verweisen Sie dann auf die Regex für E-Mail-Adressen:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Wir können diese Regex in die folgenden drei Teile zerlegen:

- `[a-zA-Z0-9.+_-]+` ist der Anfang der E-Mail Adresse vor dem `@`-Zeichen. Also der „Name“ in „name@example.com“.
- `[a-zA-Z0-9.-]+` ist der erste Teil der Domäne. Also das "Beispiel" in "name@example.com".
- `[a-zA-Z.-]+` ist der letzte Teil der Domäne. Also das "com" in "name@example.com".

{% endraw %}

#### Wie kann ich nach E-Mail-Adressen filtern, die mit einer bestimmten Domain verbunden sind?

Angenommen, Sie möchten nach E-Mails filtern, die mit "@braze.com" enden. Sie würden den Filter für E-Mail-Adressen verwenden, ihn auf `matches regex` einstellen und „@braze.com“ in das Regex-Feld eingeben. Dasselbe gilt für jede andere E-Mail-Domäne.

![Filter für eine E-Mail Adresse, die dem Regex von "@braze.com" entspricht.]({% image_buster /assets/img/regex/regeximg1.png %})

#### Wie kann ich Filterzahlen-Strings für Werte ≥ x oder ≤ x verwenden?

Wenn Sie nach Werten suchen, die größer als oder gleich (≥) x sind, verwenden Sie die folgende Regex:

```
^([x-y]|\d{z,})$
```

Dabei ist `x-y` der Zahlenbereich (0–9) der ersten Ziffer und `z` ist die Anzahl der Ziffern von x. Für Werte größer oder gleich 50 wäre die Regex dann zum Beispiel `^([5-9][0-9]|\d{3,})$`.

Wenn Sie nach Werten suchen, die kleiner oder gleich (≤) x sind, verwenden Sie die folgende Regex:

```
^([x-y]|[a-b])$
```

Dabei ist `x-y` der Zahlenbereich (0-9) der ersten Ziffer und `a-b` ist der untere Grenzbereich von x. Für Werte kleiner oder gleich 50 wäre die Regex dann zum Beispiel `^([5-9][0-9]|[0-4][0-9])$`.

#### Wie kann ich angepasste Attribute filtern, die mit einem bestimmten String beginnen?

Verwenden Sie das Caret-Symbol (`^`), um zu kennzeichnen, womit der String beginnt, und geben Sie dann den Namen des angepassten Attributs ein, das Sie angeben möchten.

Wenn Sie beispielsweise versuchen, Nutzer:innen zusammenzustellen, die in Städten leben, die mit „San“ beginnen, würde Ihre Regex `^San \w` lauten. Mit dieser Regex würden Sie erfolgreich Nutzer:innen aus Städten wie San Francisco, San Diego, San Jose usw. zusammenstellen.

![Filter für einen Ort, der der Regex von "^San \\w" entspricht.]({% image_buster /assets/img/regex/regeximg2.png %})

#### Wie kann ich nach bestimmten Telefonnummern filtern?

Bevor Sie Regex zum Filtern von Telefonnummern verwenden, denken Sie daran, dass die für Nutzerprofile protokollierten Nummern im [E.164](https://en.wikipedia.org/wiki/E.164)-Format sein müssen, wie unter [Nutzertelefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) angegeben.

Angenommen, Sie suchen nach US-Telefonnummern, verwenden Sie das Regex-Format `1?\d\d\d\d\d\d\d\d\d\d`, wobei jede Wiederholung von `\d` eine Ziffer ist, die Sie angeben möchten. Die ersten drei Ziffern sind die Ortsvorwahl.

Ebenso ist das Format für britische Telefonnummern `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Für jedes andere Land wird der entsprechende Ländercode verwendet, gefolgt von der erforderlichen Anzahl von `\d` Wiederholungen für jede verbleibende Ziffer. Im Fall von Litauen mit dem Code „3“ würde die Regex also `^\+3\d\d\d\d\d\d\d\d\d\d` lauten.

Nehmen wir zum Beispiel an, Sie möchten Nutzer:innen nach Telefonnummer für eine bestimmte Vorwahl, „718“, filtern. Verwenden Sie den Filter für Telefonnummern, setzen Sie ihn auf `matches regex` und geben Sie die folgende Regex ein:

```
^1?718\d\d\d\d\d\d\d
```

![Filter für eine Telefonnummer, die mit der Regex von "^1?718\\d\\d\\d\\d\\d\\d\\d" übereinstimmt.]({% image_buster /assets/img/regex/regeximg3.png %})


