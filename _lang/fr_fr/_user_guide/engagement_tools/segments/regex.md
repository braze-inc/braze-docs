---
nav_title: "Expressions régulières"
article_title: Expressions régulières
page_order: 10

description: "Cet article de référence explique ce que sont les expressions régulières et comment les utiliser, tout en proposant des solutions pour valider et tester des expressions régulières."
page_type: reference
tool:
  - Testing Tools
  
---

# [![Cours d'apprentissage ]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}[Braze](https://learning.braze.com/regular-expression-basics-for-braze) Expressions régulières

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> Une expression régulière, connue sous le nom de « regex » en anglais, est une séquence de caractères qui définit un modèle de recherche. Les expressions régulières vous permettent de valider des groupements de texte et d’effectuer des recherches et des remplacements. Chez Braze, nous exploitons des expressions régulières pour vous proposer une solution de correspondance de chaîne de caractères plus flexible afin de vous aider à filtrer vos segments et campagnes pour votre audience cible.<br><br>Cette page traite des expressions régulières (regex), de leur utilisation, des questions fréquemment posées et fournit un débogueur regex pour tester les expressions régulières.

Dans le cours d'apprentissage de Braze lié, nous vous montrons comment les expressions régulières peuvent être utilisées et testées sur [Regex101\.](https://regex101.com/) Nous proposons également un [testeur d’expression régulière interne](#regex-debugger), une page de références utiles, des données d’échantillon référencées dans la vidéo d’apprentissage de Braze sur les expressions régulières, ainsi que des réponses à certaines questions fréquemment posées.

## Ressources

- [Les bases des expressions régulières](https://learning.braze.com/regular-expression-basics-for-braze) Cours d'apprentissage de Braze
- [Aide-mémoire sur les expressions régulières]({{site.baseurl}}/regex_cheat_sheet/)
- [Exemple de données RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Débogueur des expressions régulières

{% alert important %}
Cet outil est uniquement fourni à titre de référence et ne garantit pas que l’expression régulière corresponde à 100 % à la plateforme Braze. Les expressions régulières de Braze utilisées pour la segmentation et les filtres ajoutent automatiquement le modificateur `/gi`. Le [modificateur gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) est utilisé pour effectuer une recherche qui ne respecte pas la casse de toutes les occurrences d’une expression régulière dans une chaîne de caractères.  
<br>
Les expressions régulières pour les propriétés de déclenchement d'événements personnalisés et les filtres de déclenchement utilisent le`/g`modificateur (sensible à la casse, voir [le modificateur g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) et n'utilisent pas le`/i`modificateur. Pour ignorer la casse dans les propriétés de déclencheur d'événements personnalisés et les filtres de déclencheur, veuillez utiliser`(?i)`à la place. Par exemple,`Matches regex (?i)STOP(?-i)`détecte toute utilisation du mot « STOP » dans tous les cas (comme « stop », « veuillez arrêter » et « cessez d'envoyer des messages à mon adresse »).
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
Ce formulaire permet d’effectuer des validations et des tests de base des expressions régulières.
​
Expression régulière :
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="expression régulière" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
Valeur(s) de contrôle : <textarea style="" placeholder="chaîne de caractères" id="regex_text"></textarea><br /><br />
​
Résultats correspondants<span id="reg_count"></span> :  <div id="regex_results"></div>
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

## Foire aux questions

#### Le filtre `does not match regex` inclut-il des valeurs vides ?

Non. Si la valeur est vide, l'utilisateur ne sera pas inclus dans le filtre `does not match regex`.

#### Comment filtrer des adresses e-mail spécifiques à une boîte de réception lorsque je segmente mes utilisateurs ?

{% raw %}
Vous pouvez utiliser le filtre d’adresse e-mail en le définissant sur `matches regex`. Ensuite, reportez-vous à l’expression régulière pour les adresses e-mail :

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Cette expression régulière peut être divisée en trois parties :

- `[a-zA-Z0-9.+_-]+` correspond au début de l’adresse e-mail, qui se trouve avant le caractère `@`. Ainsi, le "nom" dans "name@example.com".
- `[a-zA-Z0-9.-]+` correspond à la première partie du domaine. Ainsi, l'"exemple" de "name@example.com".
- `[a-zA-Z.-]+` correspond à la dernière partie du domaine. Ainsi le "com" dans "name@example.com".

{% endraw %}

#### Comment filtrer les adresses e-mail associées à un domaine spécifique ?

Supposons que vous souhaitiez filtrer les e-mails se terminant par "@braze.com". Vous devez utiliser le filtre d'adresses e-mail, le définir sur `matches regex`, et saisir "@braze.com" dans le champ de l'expression régulière. Il en va de même pour tout autre domaine e-mail.

![Veuillez filtrer les adresses e-mail qui correspondent à l'expression régulière « @ braze.com».]({% image_buster /assets/img/regex/regeximg1.png %})

#### Comment utiliser les chaînes de numéros de filtre pour les valeurs ≥ x et ≤ x ?

Si vous recherchez des valeurs supérieures ou égales à (≥) x, utilisez l’expression régulière suivante :

```
^([x-y]|\d{z,})$
```

Si `x-y` est la plage (de 0 à 9) du premier chiffre, et `z` est le nombre premier, plus le nombre de chiffres de x. Par exemple, pour des valeurs supérieures ou égales à 50, l’expression régulière serait `^([5-9][0-9]|\d{3,})$`.

Si vous recherchez des valeurs inférieures ou égales à (≤) x, utilisez l’expression régulière suivante :

```
^([x-y]|[a-b])$
```

Si `x-y` est la plage (de 0 à 9) du premier chiffre, et `a-b` est la plage inférieure de x. Par exemple, pour les valeurs inférieures ou égales à 50, l'expression régulière serait `^([5-9][0-9]|[0-4][0-9])$`.

#### Comment filtrer des attributs personnalisés qui commencent par une chaîne de caractères spécifique ?

Utilisez l’accent circonflexe (`^`) pour indiquer ce par quoi la chaîne de caractères commence, puis saisissez le nom de l’attribut personnalisé que vous souhaitez spécifier.

Par exemple, si vous essayez de cibler des utilisateurs qui vivent dans des villes commençant par « San », votre expression régulière sera `^San \w`. Cette expression régulière vous permettra de cibler des utilisateurs dans de villes telles que San Francisco, San Diego, San Jose, etc.

![Filtrez les villes qui correspondent à l'expression régulière « ^San \\w ».]({% image_buster /assets/img/regex/regeximg2.png %})

#### Comment filtrer des numéros de téléphone spécifiques ?

Avant d'utiliser une expression régulière pour filtrer les numéros de téléphone, n'oubliez pas que les numéros enregistrés pour les profils utilisateurs doivent être au format [E.164](https://en.wikipedia.org/wiki/E.164) comme spécifié dans [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/).

En supposant que vous recherchez des numéros de téléphone aux États-Unis, utilisez le format d’expression régulière `1?\d\d\d\d\d\d\d\d\d\d`, dans lequel chaque répétition de `\d` est un chiffre que vous souhaitez spécifier. Les trois premiers chiffres correspondent à l’indicatif régional.

De même, le format des numéros de téléphone britanniques est `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Pour tout autre pays, il convient d'utiliser le code du pays concerné, suivi du nombre de`\d`répétitions nécessaires pour chaque chiffre restant. Ainsi, dans le cas de la Lituanie, dont l’indicatif national est « 3 », l’expression régulière serait `^\+3\d\d\d\d\d\d\d\d\d\d`.

Supposons par exemple que vous souhaitiez filtrer les utilisateurs par numéro de téléphone avec l’indicatif régional « 718 ». Utilisez le filtre de numéro de téléphone, définissez-le sur `matches regex` et entrez l’expression régulière ci-dessous :

```
^1?718\d\d\d\d\d\d\d
```

![Filtrez les numéros de téléphone qui correspondent à l'expression régulière « ^1?718\\d\\d\\d\\d\\d\\d\\d ».]({% image_buster /assets/img/regex/regeximg3.png %})


