---
nav_title: Définition des valeurs par défaut
article_title: Réglage des valeurs par défaut des liquides
page_order: 5
description: "Cet article de référence explique comment définir des valeurs de repli par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages."

---

# Définition des valeurs par défaut

{% raw %}

> Des valeurs de repli par défaut peuvent être définies pour tout attribut de personnalisation utilisé dans vos messages. Cet article explique comment fonctionnent les valeurs par défaut, comment les configurer et comment les utiliser dans vos messages.

## Comment ils fonctionnent

Des valeurs par défaut peuvent être ajoutées en spécifiant un [filtre liquide](http://docs.shopify.com/themes/liquid-documentation/filters) (utilisez `|` pour distinguer le filtre en ligne, comme indiqué) avec le nom "default".

```
| default: 'Insert Your Desired Default Here'
```

Si une valeur par défaut n'est pas fournie et que le champ est manquant ou n'est pas défini pour l'utilisateur, le champ sera vide dans le message.

L'exemple suivant montre la syntaxe correcte pour ajouter une valeur par défaut. Dans ce cas, la mention "Valued User" remplacera l'attribut `{{ ${first_name} }}` si le champ `first_name` d'un utilisateur est vide ou indisponible.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Pour un utilisateur nommé Janet Doe, le message apparaîtra comme suit :

```
Hi Janet, thanks for using the App!
```

Ou bien...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
La valeur par défaut s'affiche pour les valeurs vides, mais pas pour les valeurs en blanc. Une valeur vide ne contient rien, tandis qu'une valeur vierge contient des caractères d'espacement (tels que des espaces) et aucun autre caractère. Par exemple, une chaîne vide peut ressembler à `""` et une chaîne vierge à `" "`.
{% endalert %}

## Définition de valeurs par défaut pour différents types de données

L'exemple ci-dessus montre comment définir une valeur par défaut pour une chaîne de caractères. Vous pouvez définir des valeurs par défaut pour tout type de données Liquid ayant la valeur `empty`, `nil` (non défini) ou `false`, ce qui inclut les chaînes, les booléens, les tableaux, les objets et les nombres.

### Cas d'utilisation : Booléens

Imaginons que vous disposiez d'un attribut personnalisé booléen appelé `premium_user` et que vous souhaitiez envoyer un message personnalisé en fonction du statut premium de l'utilisateur. Certains utilisateurs n'ont pas de statut premium, vous devrez donc définir une valeur par défaut pour capturer ces utilisateurs.

1. Vous attribuerez une variable appelée `is_premium_user` à l'attribut `premium_user` avec une valeur par défaut de `false`. Cela signifie que si `premium_user` est `nil`, la valeur de `is_premium_user` sera par défaut `false`. 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2\. Ensuite, utilisez la logique conditionnelle pour spécifier le message à envoyer si `is_premium_user` est `true`. En d'autres termes, que faut-il envoyer si `premium_user` est `true`. Vous attribuerez également une valeur par défaut au prénom de l'utilisateur, au cas où nous n'aurions pas le nom de l'utilisateur.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3\. Enfin, indiquez quel message envoyer si `is_premium_user` est `false` (ce qui signifie que `premium_user` est `false` ou `nil`). Ensuite, vous fermerez la logique conditionnelle.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Cas d'utilisation : Chiffres

Imaginons que vous disposiez d'un attribut personnalisé numérique appelé `reward_points` et que vous souhaitiez envoyer un message contenant les points de récompense de l'utilisateur. Certains utilisateurs n'ont pas de points de récompense, vous devrez donc définir une valeur par défaut pour tenir compte de ces utilisateurs.

1. Commencez le message en vous adressant au prénom de l'utilisateur ou à une valeur par défaut de `Valued User`, au cas où vous n'auriez pas son nom.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Terminez le message en indiquant le nombre de points de récompense dont dispose l'utilisateur en utilisant l'attribut personnalisé appelé `reward_points` et en utilisant la valeur par défaut de `0`. Tous les utilisateurs dont le site `reward_points` a une valeur `nil` auront des points de récompense `0` dans le message.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Cas d'utilisation : Objets

Supposons que vous ayez un objet d'attribut personnalisé imbriqué appelé `location` qui contient les propriétés `city` et `state`. Si l'une de ces propriétés n'est pas définie, vous devez encourager l'utilisateur à la fournir.

1. Adressez-vous à l'utilisateur par son prénom et incluez une valeur par défaut, au cas où vous n'auriez pas son nom.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Rédigez un message indiquant que vous souhaitez confirmer l'emplacement/localisation de l'utilisateur.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3\. Insérez l'emplacement/localisation de l'utilisateur dans le message et attribuez des valeurs par défaut lorsque la propriété address n'est pas définie.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Cas d'utilisation : Tableaux

Supposons que vous disposiez d'un attribut personnalisé de type tableau appelé `upcoming_trips` qui contient des voyages avec les propriétés `destination` et `departure_date`. Vous souhaitez envoyer aux utilisateurs des messages personnalisés en fonction de la planification de leurs déplacements.

1. Écrivez une logique conditionnelle pour spécifier qu'un message ne doit pas être envoyé si `upcoming_trips` est `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2\. Indiquez le message à envoyer si `upcoming_trips` a un contenu :<br><br>**2a.** Adressez-vous à l'utilisateur et incluez une valeur par défaut, au cas où vous n'auriez pas son nom. <br>**2b.** Utilisez une étiquette `for` pour spécifier que vous allez extraire des propriétés (ou des informations) pour chaque voyage contenu dans `upcoming_trips`. <br>**2c.** Listez les propriétés dans le message et incluez une valeur par défaut si l'adresse `departure_date` n'est pas définie. (Supposons qu'une adresse `destination` soit requise pour la création d'un voyage, il n'est donc pas nécessaire de définir une valeur par défaut pour cela).<br>**2d.** Fermez l'étiquette `for`, puis la logique conditionnelle.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
