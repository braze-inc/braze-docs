---
nav_title: Opérateurs
article_title: Opérateurs Liquid
page_order: 2
description: "Cette page de référence indique les opérateurs compatibles Liquid, ainsi que les exemples pertinents."

---

# Opérateurs

> Liquid prend en charge de nombreux [opérateurs][25] qui peuvent être utilisés dans vos instructions conditionnelles. Cette page présente les opérateurs pris en charge par Liquid et fournit des exemples d'utilisation dans vos messages.

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

## Cas d’utilisation

Voici quelques cas d'utilisation de ces opérateurs qui pourraient être utiles à vos campagnes marketing :

### Choisir un message avec un attribut personnalisé de type entier

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

Dans ce cas d'utilisation, si l'attribut personnalisé "Dépenses totales" d'un client est supérieur à `0`, il recevra le message :

```
Thanks for purchasing! Here's another 10% off!
```
Si l’attribut personnalisé « Total des dépenses » d’un client n’existe pas ou est égal à `0`, il reçoit le message suivant :

```
Buy now! Would 5% off convince you?
```

### Choisir un message avec une chaîne de caractères attribut personnalisé

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == 'Game1' %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == 'Game2' %}
You played our other Game! Woop!{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

Dans ce cas d'utilisation, si vous avez joué à un certain jeu, vous recevrez le message suivant :

```
You played our Game! We're so happy!
```

Si vous avez joué à un autre jeu spécifié :

```
You played our other Game! Woop!
```

Si vous n’avez pas joué à des jeux ou que l’attribut personnalisé n’existe pas sur votre profil, vous obtenez le message suivant :

```
Hey! Get in here and play this Game!
```

### Abandon du message en fonction du lieu

Vous pouvez abandonner un message pour presque tous les motifs. L’exemple suivant montre comment vous pouvez abandonner un message si un utilisateur n’est pas situé dans une zone spécifiée, car il n’est peut-être pas admissible à la promotion, au spectacle ou à la livraison.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

Vous pouvez également [interrompre les messages][1] en fonction du contenu connecté.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
Il y a [25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
