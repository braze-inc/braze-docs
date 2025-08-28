---
nav_title: Opérateurs
article_title: Opérateurs Liquid
page_order: 2
description: "Cette page de référence indique les opérateurs compatibles Liquid, ainsi que les exemples pertinents."

---

# Opérateurs

> Liquid prend en charge de nombreux [opérateurs](https://docs.shopify.com/themes/liquid/basics/operators) qui peuvent être utilisés dans vos instructions conditionnelles. Cette page présente les opérateurs pris en charge par Liquid et fournit des exemples d'utilisation dans vos messages.

Ce tableau énumère les opérateurs pris en charge. Notez que les parenthèses sont des caractères non valides dans Liquid et qu'elles empêchent vos étiquettes de fonctionner.

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

## Tutoriels

Passons en revue quelques tutoriels pour apprendre à utiliser ces opérateurs pour vos campagnes marketing :

### Choisir un message avec un attribut personnalisé de type entier

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

{% details Code complet du liquide %}
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

Désormais, si l'attribut personnalisé "Dépenses totales" d'un utilisateur est supérieur à `0`, il recevra un message :

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Si l'attribut personnalisé "Dépenses totales" d'un utilisateur n'existe pas ou est égal à `0`, il recevra le message suivant :

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Choisir un message avec une chaîne de caractères attribut personnalisé

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
3\. Utilisez l'étiquette `elsif` avec les opérateurs does not equal (`!=`) et "and" (`&&`) pour vérifier que l'utilisateur a un jeu récent (c'est-à-dire que la valeur n'est pas vide) et que le jeu n'est pas *Awkward Dinner Party (dîner gênant* ) ou *Proxy War 3 (guerre par procuration) : La guerre de la soif*. Créez ensuite un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
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

{% details Code complet du liquide %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
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

{% details Code complet du liquide %}
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


