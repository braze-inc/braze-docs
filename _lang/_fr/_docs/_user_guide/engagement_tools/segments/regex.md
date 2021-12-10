---
nav_title: "Expressions régulières"
article_title: Expressions régulières
page_order: 5
description: "Cet article de référence couvre ce que sont les expressions régulières, comment commencer à les utiliser, et offre des fonctionnalités de débogueur pour valider et tester les expressions régulières."
page_type: Référence
tool:
  - Outils de test
---

# Expressions régulières avec Braze

{% include video.html id="3h5Xbhl-TxE" align="right" %}

> Les expressions régulières, communément appelées regex, sont une séquence de caractères qui définissent un motif de recherche. Les expressions régulières vous permettent de valider le regroupement de texte et de trouver et de remplacer les actions. <br><br>Regex est utilisé à Braze pour vous donner une solution de correspondance de chaînes plus flexible dans votre segmentation et le filtrage de campagne pour votre public cible.

Dans la vidéo fournie, nous vous montrons comment les expressions régulières peuvent être utilisées et testées sur le site [Regex101][regex]. Ci-dessous, nous offrons également un testeur d'expressions régulières, une feuille de triche utile, des exemples de données référencées dans la vidéo Regex LAB, ainsi que des questions fréquemment posées.

\[Feuille de triche Regex téléchargeable PDF\]\[cheatsheet\]<br> \[Données téléchargeables RTF\]\[dummydata\]

{% tabs %}
{% tab Regex Debugger %}

Ce formulaire permet la validation et le test de base des expressions régulières. ​
<div class="alert alert-important" role="alert"><div class="alert-msg"> <b>importance: </b><br />
<p>Cet outil est uniquement conçu comme une référence, et ne garantit pas que le regex corresponde à 100% avec la plateforme de Braze. Expressions régulières dans Braze ajoute automatiquement le modificateur <code>gi</code>. Le modificateur <a href='https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm'>gi</a> est utilisé pour effectuer une recherche insensible à la casse de toutes les occurrences d'une expression régulière dans une chaîne. </p>
</div></div>
<div>
Regex:
 <unk>
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
Valeur(s) de contrôle : <textarea style="" placeholder="chaîne de correspondance" id="regex_text"></textarea><br /><br />
<unk>
Résultats correspondants<span id="reg_count"></span>: <div id="regex_results"></div>
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
{% tab Frequently Asked Questions %}

{% détails Comment puis-je filtrer les adresses e-mail spécifiques à la boîte de réception lors de la segmentation ? %}

Utilisez le filtre d'adresse de courriel, définissez-le à "correspond à l'expression régulière". Référez la regex pour les adresses emails, <font color="red">[a-zA-Z0-9.+_-]+ </font>@<font color="blue">[a-zA-Z0-9.-]+</font>\.<font color="green">[a-zA-Z.-]+</font> où:
- <font color="red">[a-zA-Z0-9.+_-]+</font> est le début de l'adresse e-mail avant le caractère '@'. Donc le "nom" dans "nom@exemple.com".
- <font color="blue">[a-zA-Z0-9.-]+</font> est la première partie du domaine. Donc l'"exemple" dans "nom@exemple.com".
- <font color="green">[a-zA-Z.-]+</font> est la dernière partie du domaine. Donc le "com" dans "name@example.com".

{% enddetails %}

{% détails Comment puis-je filtrer les adresses e-mail associées à un domaine spécifique ? %}

Dites que vous voulez filtrer pour les e-mails se terminant par @braze.com. Vous utiliserez le filtre d'adresse e-mail, le définissez comme correspondant à regex, et saisissez "@braze.com" dans le champ.

![image1]({% image_buster /assets/img/regex/regeximg1.png %})

{% enddetails%}

{% détails Comment puis-je utiliser des expressions rationnelles sur des chaînes de nombres pour filtrer les valeurs †x ou <unk> x? %}
Si vous recherchez des valeurs __†x__, la regex à utiliser serait __^([x-y]|\d{z, )$__ où x-y est l'intervalle des nombres (0-9) du premier chiffre, et z est le plus le nombre de chiffres de x.<br>__Example__<br> Pour les valeurs de †50, la regex sera alors ^(\[5-9\]\[0-9\]|\d{3,})$

Si vous recherchez des valeurs __<unk> x__, la regex serait __^([x-y]|[a-b])$__ où x-y est l'intervalle de nombres (0-9) du premier chiffre, et a-b est une limite inférieure de x.<br>__Example__<br> Pour les valeurs de la valeur "number@@050, la regex sera alors ^(\[5-9\]\[0-9\]|\[0-4\]\[0-9\])$
{% enddetails %}
{% details Comment filtrer les attributs personnalisés qui commencent par une chaîne spécifique ? %}
Utilisez le caractère __^__ pour indiquer par quoi commence la chaîne de caractères et entrez le nom que vous essayez de spécifier.

__Exemple__<br> Si vous essayez de cibler les utilisateurs qui vivent dans des villes commençant par "San", votre regex serait __^San \w__. Dans un tel cas, vous cibliez avec succès les utilisateurs de villes telles que San Francisco, San Diego, San Jose, etc.

![image2]({% image_buster /assets/img/regex/regeximg2.png %})
{% enddetails %}
{% details How to filter for certain phone numbers with regex %}

Avant d'utiliser regex pour filtrer les numéros de téléphone, veuillez prendre note que les numéros enregistrés pour les profils d'utilisateur devraient déjà être dans un [E. 64 format](https://en.wikipedia.org/wiki/E.164) comme spécifié dans notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/).

En supposant que les numéros de téléphone américains, la regex que vous voulez utiliser est au format __1? d\d\d\d\d\d\d\d\d\d\d__, où chaque "\d" est un chiffre que vous voulez spécifier - dont les 3 premiers seraient l'indicatif régional.

De même, le format de __numéros de téléphone au Royaume-Uni__ est __^\+4\d\d\d\d\d\d\d\d\d\d\d\d__ et tout autre pays serait l'indicatif de pays respectif __suivi du nombre nécessaire de caractères "\d" pour chaque chiffre restant__. Donc, dans le cas de la Lituanie avec le code pays 3, leur regex serait __^\+3\d\d\d\d\d\d\d\d\d\d\d\d\d.__

__Exemple__<br> Supposons que vous vouliez filtrer les utilisateurs par numéro de téléphone pour un indicatif régional spécifique, 718. Utilisez le filtre de numéro de téléphone, définissez-le à "correspond à regex", et entrez __^1?718\d\d\d\d\d\d\d\d__

![image3]({% image_buster /assets/img/regex/regeximg3.png %})
{% enddetails %}
<br><br>
{% endtab %}
{% endtabs %}
[cheatsheet]: {% image_buster /assets/download_file/regex-cheatsheet.pdf %} [dummydata]: {% image_buster /assets/download_file/regex-dummy-data.rtf %}

[regex]: https://regex101.com/
