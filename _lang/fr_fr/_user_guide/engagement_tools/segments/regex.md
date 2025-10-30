---
nav_title: "Expressions régulières"
article_title: Expressions régulières
page_order: 10

description: "Cet article de référence explique ce que sont les expressions régulières (regex), comment commencer à les utiliser et propose une fonctionnalité de débogage pour valider et tester les expressions régulières."
page_type: reference
tool:
  - Testing Tools
  
---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Expressions régulières

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> Une expression régulière, communément appelée "regex", est une séquence de caractères qui définit un motif de recherche. Les expressions régulières vous permettent de valider des groupes de texte et d'effectuer des opérations de recherche et de remplacement. Chez Braze, nous exploitons les expressions régulières pour vous offrir une solution de correspondance de chaînes de caractères plus flexible dans votre segmentation et votre filtrage de campagne pour votre audience cible.<br><br>Cette page traite des expressions régulières (regex), de leur utilisation, des questions fréquemment posées et propose un débogueur regex pour tester les expressions régulières.

Dans le cours d'apprentissage de Braze lié, nous vous montrons comment les expressions régulières peuvent être utilisées et testées sur [Regex101](https://regex101.com/). Nous vous proposons également un [testeur de regex interne](#regex-debugger), une page de référence utile, des exemples de données référencées dans la vidéo sur l'expression régulière Braze, ainsi qu'une foire aux questions.

## Ressources

- [Les bases des expressions régulières](https://learning.braze.com/regular-expression-basics-for-braze) Cours d'apprentissage de Braze
- [Aide-mémoire sur les expressions régulières]({{site.baseurl}}/regex_cheat_sheet/)
- [Exemple de données RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Débogueur d'expressions régulières

{% alert important %}
Cet outil n'est qu'une référence et ne garantit pas que l'expression régulière corresponde à 100 % à la plateforme Braze. Les expressions régulières utilisées dans Braze pour la segmentation et les filtres ajoutent automatiquement le modificateur `/gi`. Le [modificateur gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) est utilisé pour effectuer une recherche insensible à la casse sur toutes les occurrences d'une expression régulière dans une chaîne de caractères.  
<br>
Les expressions régulières pour les propriétés d'événements personnalisés d'un déclencheur et les filtres de déclencheurs utilisent le modificateur `/g` (sensible à la casse, voir le [modificateur g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) et n'utilisent pas le modificateur `/i`. Pour que les propriétés d'un déclencheur d'événement personnalisé et les filtres de déclencheur ne soient pas sensibles à la casse, utilisez plutôt `(?i)`. Par exemple, `Matches regex (?i)STOP(?-i)` attrape toute utilisation de "STOP" dans tous les cas (tels que "stop", "veuillez arrêter" et "n'arrêtez jamais de m'envoyer des messages").
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
Ce formulaire permet de valider et de tester les expressions régulières.
​
Expression régulière :
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
Résultats appariés<span id="reg_count"></span>: <div id="regex_results"></div>
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

## Questions fréquemment posées

#### Le filtre `does not match regex` inclut-il des valeurs vides ?

Non. Si la valeur est vide, l'utilisateur ne sera pas inclus dans le filtre `does not match regex`.

#### Comment filtrer les adresses e-mail spécifiques à une boîte de réception lors de la segmentation ?

{% raw %}
Utilisez le filtre d'adresses e-mail, réglez-le sur `matches regex`. Faites ensuite référence à l'expression régulière pour les adresses e-mail :

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Nous pouvons décomposer cette expression régulière en trois parties :

- `[a-zA-Z0-9.+_-]+` est le début de l'adresse e-mail avant le caractère at `@`. Ainsi, le "nom" dans "name@example.com".
- `[a-zA-Z0-9.-]+` est la première partie du domaine. Ainsi, l'"exemple" de "name@example.com".
- `[a-zA-Z.-]+` est la dernière partie du domaine. Ainsi le "com" dans "name@example.com".

{% endraw %}

#### Comment filtrer les adresses e-mail associées à un domaine spécifique ?

Supposons que vous souhaitiez filtrer les e-mails se terminant par "@braze.com". Vous devez utiliser le filtre d'adresses e-mail, le définir sur `matches regex`, et saisir "@braze.com" dans le champ de l'expression régulière. Il en va de même pour tout autre domaine d'e-mail.

\![Filtre pour une adresse e-mail qui correspond à l'expression régulière de "@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})

#### Comment puis-je utiliser les chaînes de caractères des nombres filtres pour des valeurs ≥ x ou ≤ x ?

Si vous recherchez des valeurs supérieures ou égales à (≥) x, utilisez l'expression régulière suivante :

```
^([x-y]|\d{z,})$
```

Où `x-y` est la plage de nombres (0-9) du premier chiffre, et `z` est le plus grand nombre de chiffres de x. Par exemple, pour les valeurs supérieures ou égales à 50, l'expression régulière serait alors `^([5-9][0-9]|\d{3,})$`.

Si vous recherchez des valeurs inférieures ou égales à (≤) x, utilisez l'expression régulière suivante :

```
^([x-y]|[a-b])$
```

Où `x-y` est la plage de nombres (0-9) du premier chiffre, et `a-b` est la limite inférieure de la plage de x. Par exemple, pour les valeurs inférieures ou égales à 50, l'expression régulière serait alors `^([5-9][0-9]|[0-4][0-9])$`.

#### Comment filtrer les attributs personnalisés qui commencent par une chaîne de caractères spécifique ?

Utilisez le symbole de la carotte (`^`) pour indiquer le début de la chaîne de caractères, puis saisissez le nom de l'attribut personnalisé que vous souhaitez spécifier.

Par exemple, si vous essayez de cibler les utilisateurs qui vivent dans des villes commençant par "San", votre expression régulière serait `^San \w`. Avec cette expression régulière, vous parviendrez à cibler les utilisateurs de villes telles que San Francisco, San Diego, San Jose, etc.

\![Filtre pour une ville qui correspond à l'expression régulière de "^San \\w".]({% image_buster /assets/img/regex/regeximg2.png %})

#### Comment puis-je filtrer des numéros de téléphone spécifiques ?

Avant d'utiliser une expression régulière pour filtrer les numéros de téléphone, n'oubliez pas que les numéros enregistrés pour les profils utilisateurs doivent être au format [E.164](https://en.wikipedia.org/wiki/E.164) comme spécifié dans [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/).

Si vous recherchez des numéros de téléphone américains, utilisez le format d'expression régulière `1?\d\d\d\d\d\d\d\d\d\d`, où chaque répétition de `\d` est un chiffre que vous souhaitez spécifier. Les trois premiers chiffres correspondent au code régional.

De même, le format des numéros de téléphone britanniques est `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Pour tout autre pays, le code du pays concerné est indiqué, suivi du nombre nécessaire de répétitions de `\d` pour chaque chiffre restant. Ainsi, dans le cas de la Lituanie, dont le code pays est "3", l'expression régulière serait `^\+3\d\d\d\d\d\d\d\d\d\d`.

Par exemple, supposons que vous souhaitiez filtrer les utilisateurs par numéro de téléphone pour un code régional spécifique, "718". Utilisez le filtre de numéro de téléphone, réglez-le sur `matches regex`, et entrez l'expression régulière suivante :

```
^1?718\d\d\d\d\d\d\d
```

\![Filtre pour un numéro de téléphone qui correspond à l'expression régulière de "^1?718\\d\\d\\d\\d\\d\\d".]({% image_buster /assets/img/regex/regeximg3.png %})


