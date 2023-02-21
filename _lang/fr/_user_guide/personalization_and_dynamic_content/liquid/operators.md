---
nav_title: Opérateurs
article_title: Opérateurs de Liquid
page_order: 2
description: "Cette page de référence indique les opérateurs compatibles Liquid, ainsi que les exemples pertinents."

---

# Opérateurs

Liquid prend en charge de nombreux [opérateurs][25] qui peuvent être utilisés dans vos déclarations conditionnelles.

|   Syntaxe| Description de l’opérateur|
|---------|-----------|
| ==  | égal à        |
| !=  | n’est pas égal à|
|  >  | supérieur à  |
| <   | inférieur à     |
| >=| supérieur ou égal à|
| <= | Inférieure ou égale à |
| ou | condition A ou condition B|
| et | condition A et condition B|
| contient | vérifie si une chaîne de caractères ou une baie de chaîne de caractères contient une chaîne de caractères|
{: .reset-td-br-1 .reset-td-br-2}

## Exemples d’opérateurs

Voici quelques exemples de la manière dont ces opérateurs pourraient être utiles pour vos campagnes marketing :

### Choisir un message via un attribut personnalisé entier

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Merci d’avoir acheté ! Voici encore 10 % de réduction !
{% else %}
Achetez maintenant ! Seriez-vous convaincu par 5 % de réduction ?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

Dans cet exemple, si l’attribut personnalisé « Total des dépenses » d’un client est supérieur à `0`, il reçoit le message :

```
Merci d’avoir acheté ! Voici encore 10 % de réduction !
```
Si l’attribut personnalisé « Total des dépenses » d’un client n’existe pas ou est égal à `0`, il reçoit le message suivant :

```
Achetez maintenant ! Seriez-vous convaincu par 5 % de réduction ?
```


### Choisir un message via un attribut personnalisé de chaîne de caractères

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == Game1 %}
Vous avez joué à notre jeu ! Nous en sommes heureux !
{% elsif{{custom_attribute.${Game}}} == Game2 %}
Vous avez joué à notre autre jeu ! Génial !
{% else %}
Hé ! Venez ici jouer à ce jeu !
{% endif %}
```
{% endraw %}

![][14]

Dans cet exemple, si vous avez joué à un certain jeu, vous recevrez le message suivant :

```
Vous avez joué à notre jeu ! Nous en sommes heureux !
```

Si vous avez joué à un autre jeu spécifié :

```
Vous avez joué à notre autre jeu ! Génial !
```

Si vous n’avez pas joué à des jeux ou que l’attribut personnalisé n’existe pas sur votre profil, vous obtenez le message suivant :

```
Hé ! Venez ici jouer à ce jeu !
```

### Abandon du message en fonction du lieu

Vous pouvez abandonner un message pour presque tous les motifs. L’exemple suivant montre comment vous pouvez abandonner un message si un utilisateur n’est pas situé dans une zone spécifiée, car il n’est peut-être pas admissible à la promotion, au spectacle ou à la livraison.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Live en ce moment !
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

Vous pouvez également [interrompre des messages][1] en fonction du Contenu connecté.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
