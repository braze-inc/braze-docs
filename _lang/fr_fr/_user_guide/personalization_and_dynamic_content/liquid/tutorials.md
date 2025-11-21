---
nav_title: Tutoriels
article_title: "Tutoriels : Écrire du code liquide"
page_order: 11
description: "Cette page de référence contient des tutoriels pour débutants qui vous aideront à vous familiariser avec le code Liquid."
page_type: tutorial
---

# Tutoriels : Écrire du code liquide

> Nouveau pour Liquid ? Ces tutoriels vous aideront à commencer à écrire du code liquide pour des cas d'utilisation conviviaux pour les débutants. Chaque tutoriel couvre une combinaison différente d'objectifs d'apprentissage, tels que la logique conditionnelle et les opérateurs.

Lorsque vous aurez terminé ces tutoriels, vous serez en mesure de.. :

- Écrire du code liquide pour les cas d'utilisation courants
- Enchaîner des logiques conditionnelles liquides pour personnaliser les messages en fonction des données de l'utilisateur.
- Utilisez des variables et des filtres pour écrire des équations qui utilisent les valeurs des attributs.
- Reconnaître les commandes de base d'un code liquide et se faire une idée générale de ce que fait le code.

| Tutoriel | Objectifs d'apprentissage |
| --- | --- |
| [Personnaliser les messages pour les segments d'utilisateurs](#segments) | valeurs par défaut, logique conditionnelle |
| [Rappels concernant les paniers abandonnés](#reminders) | opérateurs, logique conditionnelle |
| [Compte à rebours de l'événement](#countdown) | variables, filtres de date |
| [Message mensuel d'anniversaire](#birthday) | variables, filtres de date, opérateurs |
| [Promouvoir un produit favori](#favorite-product) | variables, filtres de date, équations, opérateurs |
{: .reset-br-td-1 .reset-br-td-2}

## Messages personnalisés pour les segments d'utilisateurs {#segments}

Personnalisons les messages pour différents segments de messages, comme les clients VIP et les nouveaux abonnés.

1. Ouvrez le message avec des messages d'accueil personnalisés à envoyer lorsque vous avez ou n'avez pas le prénom d'un utilisateur. Pour ce faire, créez une étiquette Liquid qui inclut l'attribut `first_name` et une valeur par défaut à utiliser si `first_name` est vide. Dans ce scénario, nous utiliserons "voyageur" comme valeur par défaut.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\. Maintenant, fournissons le message à envoyer si l'utilisateur est un client VIP. Pour ce faire, nous devons utiliser une étiquette de logique conditionnelle : `if`. Cette étiquette indique que si l'attribut personnalisé `vip_status` est égal à `VIP`, le liquide suivant est exécuté. Dans ce cas, un message spécifique sera envoyé.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\. Envoyons un message personnalisé aux utilisateurs qui sont de nouveaux abonnés. Nous utiliserons l'étiquette de logique conditionnelle `elsif` pour spécifier que si l'adresse `vip_status` de l'utilisateur est `new`, le message suivant sera envoyé.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4\. Qu'en est-il des utilisateurs qui ne sont ni VIP ni nouveaux ? Nous pouvons envoyer un message à tous les autres utilisateurs avec l'étiquette `else`, qui spécifie que le message suivant doit être envoyé si les conditions précédentes ne sont pas remplies. Nous pouvons ensuite fermer la logique conditionnelle avec l'étiquette `endif`, puisqu'il n'y a plus de statut VIP à prendre en compte.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Rappels concernant les paniers abandonnés {#reminders}

Envoyons des messages personnalisés pour rappeler aux utilisateurs les articles restés dans leur panier. Nous les personnaliserons davantage pour qu'elles soient envoyées en fonction du nombre d'articles dans le panier, de sorte que s'il y a plus de trois articles ou moins, nous listerons tous les articles. S'il y a plus de trois éléments, nous enverrons un message plus concis.

1. Vérifions si le panier de l'utilisateur est vide en ouvrant une logique conditionnelle liquide avec l'opérateur `!=`, qui signifie "n'est pas égal". Dans ce cas, la condition est que l'attribut personnalisé `cart_items` ne soit pas égal à une valeur vide.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\. Nous devons ensuite restreindre notre champ d'action et vérifier si le panier contient plus de trois articles en utilisant l'opérateur \`>', qui signifie "plus grand que".

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\. Rédigez un message qui salue l'utilisateur par son prénom ou, si celui-ci n'est pas disponible, utilisez "là" comme valeur par défaut. Indiquez ce qu'il convient de mentionner s'il y a plus de trois articles dans le panier. Comme nous ne voulons pas submerger l'utilisateur avec une liste complète, nous nous contenterons d'énumérer les trois premiers `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4\. Utilisez l'étiquette `else` pour spécifier ce qui doit se passer si les conditions précédentes ne sont pas remplies (en d'autres termes, si `cart_items` est vide ou inférieur à trois), puis indiquez le message à envoyer. Comme trois éléments ne prennent pas beaucoup de place, nous pouvons les énumérer tous. Nous utiliserons l'opérateur Liquid `join` et `,` pour spécifier que les éléments doivent être listés en les séparant par une virgule. Fermez la logique avec `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Utilisez `else` puis `abort_message` pour indiquer au code Liquid de ne pas envoyer de message si le panier ne remplit aucune des conditions précédentes. En d'autres termes, si le panier est vide. Fermez la logique avec `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Compte à rebours de l'événement {#countdown}

Envoyons aux utilisateurs un message indiquant le nombre de jours restant avant une vente anniversaire. Pour ce faire, nous utiliserons des variables afin de créer des équations qui manipulent les valeurs des attributs.

1. Commençons par affecter la variable `sale_date` à l'attribut personnalisé `anniversary_date` et appliquons le filtre `date: "s"`. Cette opération convertit l'adresse `anniversary_date` en un format d'horodatage exprimé en secondes, puis attribue cette valeur à l'adresse `sale_date`.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\. Nous devons également assigner une variable pour capturer l'heure d'aujourd'hui. Assignons la variable `today` à `now` (la date et l'heure actuelles), puis appliquons le filtre `date: "%s"`.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\. Calculons maintenant le nombre de secondes qui nous séparent (`today`) de la vente anniversaire (`sale_date`). Pour ce faire, attribuez à la variable `difference` la valeur de `sale_date` moins `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4\. Nous devons maintenant convertir `difference` en une valeur à laquelle nous pourrons faire référence dans un message, car il n'est pas idéal d'indiquer à l'utilisateur le nombre de secondes qui le séparent d'une vente. Attribuons `difference_days` à `event_date` et divisons-le par `86400` pour obtenir le nombre de jours.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5\. Enfin, créons le message à envoyer.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Message mensuel d'anniversaire {#birthday}

Envoyons une promotion spéciale à tous les utilisateurs dont l'anniversaire tombe dans le mois d'aujourd'hui. Les utilisateurs qui n'ont pas d'anniversaire ce mois-ci ne recevront aucun message.

1. Tout d'abord, tirons le mois d'aujourd'hui. Nous assignerons la variable `this_month` à `now` (la date et l'heure actuelles), puis nous utiliserons le filtre `date: "%B"` pour spécifier que la variable doit être égale au mois.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\. Maintenant, nous allons extraire le mois de naissance de l'utilisateur à partir de `date_of_birth`. Nous assignerons la variable `birth_month` à `date_of_birth`, puis nous utiliserons le filtre `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\. Maintenant que nous disposons de deux variables dont la valeur est un mois, nous pouvons les comparer à l'aide de la logique conditionnelle. Fixons comme condition que `date_of_birth` soit égal à l'utilisateur `birth_month`.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4\. Créons le message à envoyer si ce mois est également le mois de naissance de l'utilisateur.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5\. Utilisez l'étiquette `else` pour spécifier ce qui se passe si la condition n'est pas remplie (parce que ce mois n'est pas le mois de naissance de l'utilisateur).

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6\. Nous ne voulons pas envoyer de message si le mois de naissance de l'utilisateur n'est pas ce mois-ci, nous utiliserons donc `abort_message` pour annuler le message, puis nous fermerons la logique conditionnelle avec `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Promotion de produit préférée {#favorite-product}

Mettons en avant le produit préféré d'un utilisateur si la date de son dernier achat remonte à plus de six mois.

1. Tout d'abord, nous utiliserons une logique conditionnelle pour vérifier si nous disposons du produit préféré de l'utilisateur et de la date de son dernier achat.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\. Ensuite, nous préciserons que si nous ne disposons pas du produit préféré de l'utilisateur ou de la date de son dernier achat, il ne faut pas envoyer de message.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\. Nous utiliserons `else` pour spécifier ce qui doit se passer si la condition ci-dessus n'est pas remplie (car nous _disposons_ du produit préféré de l'utilisateur et de la date de son dernier achat).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4\. Si nous disposons d'une date d'achat, nous devons l'affecter à une variable afin de pouvoir la comparer à la date d'aujourd'hui. Tout d'abord, créons une valeur pour la date d'aujourd'hui en affectant la variable `today` à `now` (la date et l'heure actuelles) et en utilisant le filtre `date: "%s"` pour convertir la valeur dans un format d'horodatage exprimé en secondes. Nous ajouterons le filtre `plus: 0` pour ajouter un "0" à l'horodatage. Cela ne modifie pas la valeur de l'horodatage, mais est utile pour utiliser l'horodatage dans des équations futures.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5\. Saisissons maintenant la date du dernier achat en secondes en affectant la variable `last_purchase_date` à l'attribut personnalisé `last_purchase_date` et en utilisant le filtre `date: "s"`. Nous ajouterons à nouveau le filtre `plus: 0`.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6\. Comme la date du dernier achat et la date d'aujourd'hui sont exprimées en secondes, nous devons calculer combien de secondes il y a dans six mois. Formons une équation (environ 6 mois * 30,44 jours * 24 heures * 60 minutes * 60 secondes) et affectons-la à la variable `six_months`. Nous utiliserons `times` pour spécifier la multiplication des unités de temps.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7\. Maintenant que toutes nos valeurs de temps sont exprimées en secondes, nous pouvons les utiliser dans des équations. Attribuons une variable appelée `today_minus_last_purchase_date` qui prend la valeur d'aujourd'hui et en soustrait la valeur `last_purchase_date`. Cela nous permet de savoir combien de secondes se sont écoulées depuis le dernier achat.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8\. Comparons maintenant directement nos valeurs temporelles en logique conditionnelle. Définissons la condition comme suit : `today_minus_last_purchase_date` est supérieur ou égal (`>=`) à six mois. En d'autres termes, la date du dernier achat remonte à au moins six mois.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\. Créons le message à envoyer si le dernier achat remonte à au moins six mois.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\. Nous utiliserons l'étiquette `else` pour spécifier ce qui doit se passer si la condition n'est pas remplie (parce que l'achat n'a pas eu lieu il y a au moins six mois).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\. Nous inclurons une adresse `abort_message` pour annuler le message.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\. Pour finir, nous terminerons le Liquid par deux étiquettes `endif`. Le premier `endif` ferme le contrôle conditionnel pour le produit préféré ou la date du dernier achat, et le second `endif` ferme le contrôle conditionnel pour la date du dernier achat datant d'au moins six mois.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}
