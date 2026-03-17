---
nav_title: Opérateurs
article_title: Opérateurs Liquid
page_order: 2
description: "Cette page de référence indique les opérateurs compatibles Liquid, ainsi que les exemples pertinents."

---

# Opérateurs

> Liquid prend en charge de nombreux [opérateurs](https://docs.shopify.com/themes/liquid/basics/operators) qui peuvent être utilisés dans vos instructions conditionnelles. Cette page présente les opérateurs pris en charge par Liquid et fournit des exemples d'utilisation dans vos messages.

Ce tableau répertorie les opérateurs pris en charge. Veuillez noter que les parenthèses sont des caractères non valides dans Liquid et empêchent vos tags de fonctionner.

|   Syntaxe| Description de l’opérateur|
|---------|-----------|
| ==  | est égal à        |
| !=  | n’est pas égal à|
|  >  | supérieur à  |
| <   | inférieur à     |
| >=| supérieur ou égal à|
| <= | Inférieure ou égale à |
| ou | condition A ou condition B|
| et | condition A et condition B|
| contient | vérifie si une chaîne de caractères ou un tableau de chaîne de caractères contient une chaîne de caractères|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Les opérateurs peuvent être utilisés dans les instructions conditionnelles (`if`, `elsif`, `unless`) mais pas dans`assign`les instructions ,`for`les boucles, les instructions`case``when` / ou les crochets d'accès aux tableaux. Pour obtenir une description complète, veuillez consulter [la section Où utiliser les opérateurs et les filtres]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Conditions de regroupement sans parenthèses

Liquid ne prend pas en charge les parenthèses pour regrouper des expressions. Pour évaluer une logique booléenne complexe telle que `(a and b) or c`, veuillez utiliser des `if`instructions imbriquées ou des variables intermédiaires.

Par exemple, pour vérifier si une valeur satisfait à une condition composée, attribuez une variable intermédiaire :

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutoriels

Passons en revue quelques tutoriels pour apprendre à utiliser ces opérateurs pour vos campagnes marketing :

### Veuillez sélectionner un message avec un attribut personnalisé entier.

Envoyons des notifications push avec des remises promotionnelles personnalisées aux utilisateurs qui ont ou n'ont pas effectué d'achats. La notification push utilisera un attribut personnalisé entier appelé `total_spend` pour vérifier les dépenses totales de l'utilisateur.

1. Rédigez une instruction conditionnelle utilisant l'opérateur plus grand que (`>`) pour vérifier si le total des dépenses d'un utilisateur est supérieur à `0`, ce qui indique qu'il a effectué un achat. Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. Ajoutez l'étiquette {% raw %}`{% else %}`{% endraw %} pour capturer les utilisateurs dont le total des dépenses est égal à `0` ou n'existe pas. Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\. Fermez la logique conditionnelle à l'aide de l'étiquette {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Un compositeur de notifications push avec le code Liquid complet du tutoriel.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Désormais, si l'attribut personnalisé « Total des dépenses » d'un utilisateur est supérieur à `0`, il recevra le message suivant :

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Si l'attribut personnalisé "Dépenses totales" d'un utilisateur n'existe pas ou est égal à `0`, il recevra le message suivant :

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Veuillez sélectionner un message avec un attribut personnalisé de type chaîne de caractères.

Envoyons des notifications push aux utilisateurs, et personnalisons le message en fonction du jeu le plus récemment joué par chaque utilisateur. Cet attribut utilise une chaîne personnalisée appelée `recent_game` pour vérifier le dernier jeu auquel l'utilisateur a joué.

1. Écrivez une instruction conditionnelle utilisant l'opérateur equals (`==`) pour vérifier si le jeu le plus récent d'un utilisateur est *Awkward Dinner Party.* Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. Utilisez l'étiquette `elsif` avec l'opérateur equals (`==`) pour vérifier si le jeu le plus récent de l'utilisateur est *Proxy War 3 : La guerre de la soif*. Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. Veuillez utiliser `elsif`l'étiquette avec les opérateurs « n'est pas égal à » (`!=`) et « et » (`and`) pour vérifier si l'utilisateur a une partie récente (c'est-à-dire que la valeur n'est pas vide) et que la partie n'est pas *Awkward Dinner Party* ou *Proxy War 3 : La guerre de la soif*. Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. Ajoutez l'étiquette {% raw %}`{% else %}`{% endraw %} pour capturer les utilisateurs qui n'ont pas de jeu récent. Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\. Fermez la logique conditionnelle à l'aide de l'étiquette {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un compositeur de notifications push avec le code Liquid complet du tutoriel.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Désormais, si un utilisateur a joué pour la dernière fois à *Awkward Dinner Party*, il recevra ce message :

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Si le jeu le plus récent d'un utilisateur est *Proxy War 3 : War of Thirst*, ils recevront ce message :

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Si un utilisateur a récemment joué à un jeu qui n'était pas *Awkward Dinner Party* ou *Proxy War 3 : War of Thirst*, ils recevront ce message :

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Si un utilisateur n'a joué à aucun jeu ou si cet attribut personnalisé n'existe pas dans son profil, il recevra ce message :

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Abandon du message en fonction du lieu

Vous pouvez abandonner un message pour presque tous les motifs. Annulons un message si un utilisateur n'est pas basé dans une zone spécifiée, car il risque de ne pas pouvoir bénéficier de la promotion, du spectacle ou de la réception/distribution.

1. Rédigez une instruction conditionnelle utilisant l'opérateur equals (`==`) pour vérifier si le fuseau horaire de l'utilisateur est `America/Los_Angeles`, puis créez un message à envoyer à ces utilisateurs. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. Pour éviter d'envoyer des messages à des utilisateurs situés en dehors du fuseau horaire `America/Los_Angeles`, entourez les tags {% raw %}`{% else %}`{% endraw %} et {% raw %}`{% endif %}`{% endraw %} d'une étiquette {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un compositeur de notifications push avec le code Liquid complet du tutoriel.]({% image_buster /assets/img/abort-if.png %})

Vous pouvez également [interrompre les messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) en fonction du contenu connecté.

## Résolution des problèmes

### L'aperçu peut contraindre de manière incorrecte les types de propriétés. 

Lors de la prévisualisation d'un message dans le tableau de bord, la plupart des variables (telles que les attributs personnalisés) sont converties au type approprié. Cependant, certaines variables n'ont pas de type défini que l'aperçu peut rechercher :

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Pour ces propriétés, l'aperçu tente de déduire le type à partir de la valeur. Cela signifie qu'une valeur que vous souhaitez utiliser comme **chaîne** de caractères pourrait être interprétée à tort comme un **nombre**. Par exemple, si la valeur d'une propriété est une chaîne de caractères`"3"`, l'aperçu peut la convertir en nombre entier`3`, ce qui peut entraîner un comportement inattendu dans les opérations sur les chaînes de caractères telles que`contains`ou `split`.

Si vous constatez des résultats d'aperçu inattendus lors de l'utilisation de ces types de propriétés, veuillez noter que l'inférence de type de l'aperçu peut ne pas correspondre à ce qui se produit au moment de l'envoi. Au moment de l'envoi, les types de données réels provenant du déclencheur ou de l'appel API sont conservés.

Pour imposer un type spécifique dans l'aperçu, vous pouvez explicitement convertir la valeur :

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}