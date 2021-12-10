---
nav_title: Opérateurs
article_title: Opérateurs Liquid
page_order: 2
description: "Cette page de référence note les opérateurs que Liquid supporte, ainsi que les exemples pertinents."
---

# Opérateurs

Liquid prend en charge de nombreux [opérateurs][25] qui peuvent être utilisés dans vos instructions conditionnelles.

| Syntaxe  | Description de l'opérateur                                                                        |
| -------- | ------------------------------------------------------------------------------------------------- |
| ==       | est égal à                                                                                        |
| !=       | n'est pas égal à                                                                                  |
| >        | supérieur à                                                                                       |
| <        | inférieur à                                                                                       |
| >=       | supérieur ou égal à                                                                               |
| <=       | inférieur ou égal à                                                                               |
| ou       | condition A ou condition B                                                                        |
| et       | condition A et condition B                                                                        |
| contient | vérifie si une chaîne de caractères ou une chaîne de caractères contient une chaîne de caractères |
{: .reset-td-br-1 .reset-td-br-2}

## Exemples d'opérateur

Voici quelques exemples de la manière dont ces opérateurs pourraient être utiles pour vos campagnes de marketing:

### Choisir un message via un attribut personnalisé entier

!\[Total Spend\]\[13\]{: width="100%"}

Dans cet exemple, si l'attribut personnalisé "Total Dépend" d'un client est supérieur à `0`, il recevra le message :

```
Merci pour votre achat! Voici encore 10% de réduction !
```
Si l'attribut personnalisé "Total Dépend" d'un client n'existe pas ou est égal à `0`, il recevra le message suivant :

```
Achetez maintenant ! 5% de réduction vous convaincraient-ils?
```

{% details Copyable Code for this Example: %}
{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == Game1 %}
Vous avez joué à notre jeu! Nous sommes tellement heureux!
{% else %}
Hé ! Entrez ici et jouez à ce jeu!
{% endif %}
```
{% endraw %}

{% enddetails %}

<br>

### Choisir un message via un attribut personnalisé de chaîne de caractères

!\[Jeux joués\]\[14\]

Dans cet exemple, si vous avez joué à un certain jeu, vous recevrez le message suivant :

```
Vous avez joué à notre jeu! Nous sommes tellement heureux!
```

Si vous avez joué à une autre partie spécifiée:

```
Vous avez joué à notre autre jeu! Oups !
```

Si vous n’avez joué à aucun jeu, ou que cet attribut personnalisé n’existe pas sur votre profil, vous recevrez le message suivant :

```
Hé ! Entrez ici et jouez à ce jeu!
```

{% details Copyable Code for this Example: %}

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == Game1 %}
Vous avez joué à notre jeu! Nous sommes tellement heureux!
{% elsif{{custom_attribute.${Game}}} == Game2 %}
Vous avez joué à notre autre jeu! Oups !
{% else %}
Hé ! Entrez ici et jouez à ce jeu!
{% endif %}
```
{% endraw %}

{% enddetails %}
<br>

### Annuler le message en fonction de l'emplacement

Vous pouvez annuler un message basé sur n'importe quoi. L'exemple ci-dessous montre comment vous pouvez annuler un message si un utilisateur n'est pas basé dans une zone spécifiée, étant donné qu'ils ne sont pas admissibles à la promotion, à la présentation ou à la livraison.

!\[Message d'Abort If\]\[26\]

Vous pouvez aussi [annuler les messages en fonction du contenu connecté][1].

{% details Copyable Code for this Example: %}
{% raw %}
```liquid
{% if {{{time_zone.$}}} $ =='Amérique/Los_Angeles' %}
Stream now !
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% enddetails %}
<br>
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %} [14]: {% image_buster /assets/img/liquid-if-elsif-games.png %} [26]: {% image_buster /assets/img/abort-if.png %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[25]: https://docs.shopify.com/themes/liquid/basics/operators
