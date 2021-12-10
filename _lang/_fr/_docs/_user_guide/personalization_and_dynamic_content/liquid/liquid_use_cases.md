---
nav_title: Librairie de cas d'utilisation de liquide
article_title: Librairie de cas d'utilisation de liquide
page_order: 10
excerpt_separator: ""
page_type: glossary
layout: Verrouiller le glossaire
description: "Cette page d'accueil contient des exemples de cas d'utilisation des liquides organisés par catégorie, tels que Anniversaires, Utilisation de l'application, Compte à rebours et plus encore."
---

{% api %}

## Anniversaires et jours fériés

{% apitags %}
Anniversaires et jours fériés
{% endapitags %}

- [Personnaliser les messages en fonction de l'année anniversaire d'un utilisateur](#anniversary-year)
- [Personnaliser les messages en fonction de la semaine d'anniversaire d'un utilisateur](#birthday-week)
- [Envoyer des campagnes aux utilisateurs dans leur mois d'anniversaire](#birthday-month)
- [Éviter d'envoyer des messages lors des vacances majeures](#holiday-avoid)

### Personnaliser les messages en fonction de l'année anniversaire d'un utilisateur {#anniversary-year}

Ce cas d'utilisation montre comment calculer l'anniversaire de l'application d'un utilisateur en fonction de sa date initiale d'inscription et afficher différents messages en fonction du nombre d'années de célébration.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${signup_date}}} | date: "%B" %}
{% assignez anniversary_day = {{custom_attribute.${signup_date}}} | date: "%d" %}
{% assignez anniversary_year = {{custom_attribute.${signup_date}}} | date: "%Y" %}
{% if {{this_month}} == {{anniversary_month}} %}
{% if {{this_day}} == {{anniversary_day}} %}
{% if {{anniversary_year}} == '2021' %}
Joyeux anniversaire d'un an!
{% elsif {{anniversary_year}} == '2020' %}
Joyeux anniversaire de deux ans!
{% elsif {{anniversary_year}} == '2019' %}
Joyeux anniversaire de trois ans!
{% elsif {{anniversary_year}} == '2018' %}
Joyeux anniversaire de quatre ans!
{% elsif {{anniversary_year}} == '2017' %}
Joyeux anniversaire de cinq ans!
{% elsif {{anniversary_year}} == '2016' %}
Joyeux anniversaire de six ans!
{% elsif {{anniversary_year}} == '2015' %}
Joyeux anniversaire de sept ans!
{% else %}
{% abort_message(not same month) %}
{% else %}
{% abort_message(not same day) %}
{% else %}
{% abort_message(not same year) %}
{% endif %}
{% endif %}
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous utilisons la variable réservée `maintenant` pour le modèle dans la date et l'heure courante au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"). Les filtres `%B` (mois, c'est-à-dire "mai") et `%d` (jour, c'est-à-dire "18") formatent le mois et le jour en cours. Nous utilisons ensuite les mêmes filtres de date et heure sur les valeurs `signup_date` pour nous assurer que nous pouvons comparer les deux valeurs en utilisant des balises conditionnelles et la logique.

Ensuite, nous répétons trois instructions variables supplémentaires pour obtenir les `%B` et `%d` pour la `signup_date`, mais aussi l'ajout de `%Y` (année, i. ., "2021"). Ceci forme la date et l'heure de la `signup_date` en juste l'année. Connaître le jour et le mois nous permet de vérifier si l'anniversaire de l'utilisateur est aujourd'hui, et sachant que l'année nous dit combien d'années il a été — ce qui nous permet de savoir combien d'années il faut les féliciter !

{% alert tip %} Vous pouvez créer autant de conditions que des années que vous avez collecté les dates d'inscription. {% endalert %}

### Personnaliser les messages en fonction de la semaine d'anniversaire d'un utilisateur {#birthday-week}

Ce cas d'utilisation montre comment trouver l'anniversaire d'un utilisateur, le comparer à la date courante, puis afficher les messages d'anniversaire spéciaux avant, pendant et après leur semaine d'anniversaire.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Joyeux anniversaire pour cette semaine!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Joyeux anniversaire pour la semaine prochaine !
{% else %}
Aucun anniversaire pour vous !
{% endif %}
```
{% endraw %}

**Explication :** Similaire à l'année [anniversaire](#anniversary-year) du cas d'utilisation, ici nous prenons la variable réservée `maintenant` et utilisons le filtre `%W` (semaine, i. ., semaine 12 sur 52 dans l'année) pour obtenir le nombre de semaine de l'année où l'anniversaire de l'utilisateur tombe dedans. Si la semaine de l'anniversaire de l'utilisateur correspond à la semaine en cours, nous leur envoyons un message de félicitation!

Nous incluons également des instructions pour `la semaine dernière` et `la semaine prochaine` pour personnaliser davantage votre message.

### Envoyer des campagnes aux utilisateurs dans leur mois d'anniversaire {#birthday-month}

Ce cas d'utilisation montre comment calculer le mois d'anniversaire d'un utilisateur vérifiez si leur anniversaire tombe dans le mois en cours et, dans l'affirmative, envoyez un message spécial.

{% raw %}
```liquid
{% assign this_month = ‘now’ | date: “%B” %}
{% assigner birth_month = {{${date_of_birth}}} | date: “%B” %}
{% if {{this_month}} == {{birth_month}} %}
Corps du message 
{% else %} 
{% abort_message() %}
{% endif %}
```
{% endraw %}

**Explication :** Similaire à la [semaine d'anniversaire](#birthday-week) cas d'utilisation, sauf ici nous utilisons le filtre `%B` (mois, i. ., "Mai") pour calculer quels utilisateurs ont un anniversaire ce mois-ci. Une application potentielle pourrait s'adresser aux utilisateurs de l'anniversaire dans un courriel mensuel.

### Éviter d'envoyer des messages lors des vacances majeures {#holiday-avoid}

Ce cas d'utilisation montre comment envoyer des messages pendant la période de vacances tout en évitant les jours de vacances majeures, lorsque l'engagement est susceptible d'être faible.

{% raw %}
```liquid
{% assigner aujourd'hui = 'maintenant' | date: '%Y-%m-%d' %}
{% if today == "2021-12-24" or today == "2021-12-25" or today == "2021-12-26" %}
{% abort_message %}
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous assignons le terme `aujourd'hui` à la variable réservée `maintenant` (la date et l'heure actuelles), en utilisant les filtres `%Y` (année, i. ., "2021"), `%m` (mois, c.-à-d. "12"), et `%d` (jour, c'est-à-dire "25") pour formater la date. Nous exécutons alors notre instruction conditionnelle pour dire que si la variable `aujourd'hui` correspond aux jours de vacances de votre choix, alors le message sera abandonné.

L'exemple fourni utilise la veille de Noël, le jour de Noël et le jour de la boxe (le lendemain de Noël).

{% endapi %}

{% api %}

## Utilisation de l'application

{% apitags %}
Utilisation de l'application
{% endapitags %}

- [Envoyer des messages dans la langue d'un utilisateur s'il a enregistré une session](#app-session-language)
- [Personnaliser les messages en fonction de la dernière ouverture de l'application par un utilisateur](#app-last-opened)
- [Afficher un message différent si un utilisateur a utilisé l'application il y a moins de trois jours](#app-last-opened-less-than)

### Envoyer des messages dans la langue d'un utilisateur s'il n'a pas enregistré de session {#app-session-language}

Cette utilisation vérifie si un utilisateur a enregistré une session, et si ce n'est pas le cas, inclut la logique d'afficher un message basé sur la langue collectée manuellement via un attribut personnalisé, le cas échéant. S'il n'y a aucune information de langue liée à leur compte, elle affichera le message dans la langue par défaut. Si un utilisateur a enregistré une session, il tirera toutes les informations de langue liées à l'utilisateur et affichera le message approprié.

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'fr' %}
Message en anglais basé sur l'attribut personnalisé
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message en français basé sur l'attribut personnalisé
{% else %}
N'a pas de langue - Langue par défaut
{% endif %}
{% else %}
{% if ${language} == 'fr' %}
Message en anglais basé sur la langue
{% elsif ${language} == 'fr' %}
Message en français basé sur la langue
{% else %}
A la langue - Langue par défaut
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Explication :** Ici, nous utilisons deux groupes `si` instructions, imbriquées. La première instruction `if` vérifie si l'utilisateur a commencé une session en vérifiant si la `last_used_app_date` est `nil`. Ceci est dû au fait que `{{${language}}}` est automatiquement collecté par le SDK lorsqu'un utilisateur enregistre une session. Si l'utilisateur n'a pas enregistré de session, nous n'aurons pas encore sa langue, donc ceci vérifie si des attributs personnalisés liés à la langue ont été enregistrés, et sur la base de ces informations, affichera un message dans cette langue, si possible.
{% endraw %}

La seconde instruction `if` vérifie simplement l'attribut par défaut car l'utilisateur n'a pas `nil` pour la `last_used_app_date`, ce qui signifie qu'ils ont logué une session, et nous avons leur langue.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) est une variable réservée qui est retournée lorsque le code Liquid n'a aucun résultat. `Nil` est traité comme `faux` dans un bloc `si`.
{% endalert %}

### Personnaliser les messages en fonction de la dernière ouverture de l'application par un utilisateur {#app-last-opened}

Ce cas d'utilisation calcule la dernière fois qu'un utilisateur a ouvert votre application et affichera un message personnalisé différent en fonction de la durée.

{% raw %}
```liquid
{% assignez last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assignez maintenant = 'maintenant' | date: "%s" %}
{% assignez différence_in_days = {{now}} | moins : {{last_used_date}} | divisé par : 86400 %}
{% if {{difference_in_days}} < 3 %}
Heureux de vous revoir !
{% else %}
Ça faisait un certain temps ; voici quelques-unes de nos dernières mises à jour.
{% endif %}
```
{% endraw %}

### Afficher un message différent si un utilisateur a utilisé l'application il y a moins de trois jours {#app-last-opened-less-than}

Ce cas d'utilisation calcule combien de temps un utilisateur a utilisé votre application et affichera un message personnalisé différent en fonction de la durée.

{% raw %}
```liquid
{% assignez last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assignez maintenant = 'now' | date: "%s" %}
{% assignez différence_in_days = {{now}} | moins : {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message pour un utilisateur récemment actif
{% else %}
Message pour un utilisateur moins actif
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Compte à Rebours

{% apitags %}
Compte à Rebours
{% endapitags %}

- [Ajouter X jours à la date d'aujourd'hui](#countdown-add-x-days)
- [Calculer un compte à rebours à partir d'un point défini dans le temps](#countdown-difference-days)
- [Créer un compte à rebours pour les dates et priorités d'expédition spécifiques](#countdown-shipping-options)
- [Créer un compte à rebours en jours](#countdown-days)
- [Créer un compte à rebours de jours en heures](#countdown-dynamic)
- [Créer un compte à rebours à une date future](#countdown-future-date)
- [Afficher le nombre de jours restants jusqu'à ce qu'un attribut de date personnalisée arrive](#countdown-custom-date-attribute)
- [Afficher combien de temps restant, et annuler le message si il ne reste que X temps](#countdown-abort-window)
- [Message dans l'application pour envoyer X jours avant la fin de l'adhésion de l'utilisateur](#countdown-membership-expiry)
- [Personnaliser les messages dans l'application en fonction de la date et de la langue de l'utilisateur](#countdown-personalize-language)
- [Modèle dans la date dans 30 jours à partir de maintenant, formaté en mois et jour](#countdown-template-date)

### Ajouter x jours à la date d'aujourd'hui {#countdown-add-x-days}

Ce cas d'utilisation ajoute un nombre spécifique de jours à la date courante pour référencer et ajouter des messages. Par exemple, vous pouvez envoyer un message en milieu de semaine qui montre les événements dans la zone pour le week-end, comme “Voici les films que nous affichons en 3 jours!”

{% raw %}
```liquid
{{ “now” | date:‘%s’ | plus:259200 | date:“%F” }}
```
{% endraw %}

La valeur `plus` sera toujours en secondes, donc nous terminons avec le filtre `%F` pour traduire les secondes en jours.

{% alert important %}
Vous pouvez inclure une URL ou un lien profond vers une liste d'événements dans votre message afin que vous puissiez envoyer l'utilisateur à une liste d'actions qui se produisent dans le futur.
{% endalert %}

### Calculer un compte à rebours à partir d'un point défini dans le temps {#countdown-difference-days}

Ce cas d'utilisation calcule la différence entre une date spécifique et la date courante. Cette différence peut être utilisée pour afficher un compte à rebours pour vos utilisateurs.

{% raw %}
```liquid
{% assign event_date = '2020-08-19' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | moins : aujourd'hui %}
{% assign difference_days = difference | divided_by: 86400 %}
vous avez {{ difference_days }} days restants!
```
{% endraw %}

### Créer un compte à rebours pour les dates et priorités d'expédition spécifiques {#countdown-shipping-options}

Ce cas d'utilisation capture différentes options d'expédition, calcule la durée de réception, et affiche les messages encourageant les utilisateurs à acheter à temps pour recevoir leur paquet à une certaine date.

{% raw %}
```liquid
{% assign standard_shipping_start = "2019-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2019-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2019-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2019-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
difference s days: {{difference_s_days}}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
difference e days: {{difference_e_days}}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
Il reste {{difference_s_days}} jours pour commander avec la livraison standard, donc votre commande arrive ici à temps pour la veille de Noël !

{% else %}
Il reste {{difference_s_days}} jours pour commander avec la livraison standard donc votre commande arrive ici à temps pour la veille de Noël!
{% endif %}
{% elsif aujourd'hui > standard_shipping_end et aujourd'hui < express_shipping_end %}
{% if difference_e_days == 1 %}
Il reste {{difference_e_days}} jour à commander avec expédition expresse, pour que votre commande arrive ici à temps pour la veille de Noël!
{% else %}
Il reste {{difference_e_days}} jours pour commander avec livraison express donc votre commande arrive ici à temps pour la veille de Noël!
{% endif %}
{% elsif aujourd'hui >= express_shipping_end et aujourd'hui < nuit_shipping_end %}
C'est le dernier jour pour la livraison de nuit afin que votre commande arrive ici à l'heure pour la veille de Noël !
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Créer un compte à rebours en jours {#countdown-days}

Ce cas d'utilisation calcule le temps restant entre un événement spécifique et la date courante et affiche le nombre de jours restants jusqu'à l'événement.

{% raw %}
```liquid
{% assigner event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | moins : aujourd'hui %}
{% assign difference_days = difference | divided_by: 86400 %}
Votre commande arrivera dans {{ difference_days }} jours!
```
{% endraw %}

{% alert important %}
Vous aurez besoin d'un champ d'attribut personnalisé avec une valeur de `date`.
{% endalert %}

### Créer un compte à rebours de jours en heures {#countdown-dynamic}

Ce cas d'utilisation calcule le temps restant entre un événement spécifique et la date courante. Selon le temps restant jusqu'à l'événement, il changera la valeur de l'heure (jours, heures, minutes) pour afficher différents messages personnalisés.

Par exemple, s’il y a deux jours avant l’arrivée de la commande d’un client, vous pourriez dire: « Votre commande arrivera dans 2 jours ». Alors que s’il y a moins d’un jour, vous pouvez le changer en « Votre commande arrivera dans 17 heures».

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign scheme_finish = "2017-10-13T10:30" | date: "%s" %}
{% assign difference_seconds = scheme_finish | moins : aujourd'hui %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_days | difference_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
Il vous reste {{difference_hours}} heures jusqu'à votre commande arrive !
{% elsif {{difference_minutes}} < 59 %}
Il vous reste {{difference_minutes}} minutes avant l'arrivée de votre commande !
{% else %}
Il vous reste {{difference_days}} jours avant l'arrivée de votre commande!
{% endif %}
```
{% endraw %}

{% alert important %}
Vous aurez besoin d'un champ d'attribut personnalisé avec une valeur de `date`. Vous devrez également définir des seuils de temps lorsque vous voulez que le temps soit affiché en jours, heures et minutes.
{% endalert %}

### Créer un compte à rebours à une date future {#countdown-future-date}

Ce cas d'utilisation calcule la différence entre la date courante et la date future de l'événement et affiche un message indiquant combien de jours avant l'événement.

{% raw %}
```liquid
{% assign event_date = '2019-02-19' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | moins : aujourd'hui %}
{% assign difference_days = difference | divided_by: 86400 %}
Il y a {{difference_days}} jusqu'à votre anniversaire!
{% endif %}
```
{% endraw %}

### Afficher le nombre de jours restants jusqu'à ce qu'un attribut de date personnalisée arrive {#countdown-custom-date-attribute}

Ce cas d'utilisation calcule la différence en jours entre les dates actuelles et futures et affiche un message si la différence correspond à un nombre défini.

Dans cet exemple, un utilisateur recevra un message dans les deux jours suivant l'attribut de date personnalisée. Sinon, le message ne sera pas envoyé.

{% raw %}
```liquid
{% assigner aujourd'hui = 'maintenant' | date: '%j' | plus: 0 %}
{% assigner chirurgie_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Votre intervention est en 2 jours sur {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Afficher combien de temps est restant, et annuler le message s'il ne reste plus que x temps {#countdown-abort-window}

Ce cas d'utilisation va calculer combien de temps jusqu'à une certaine date, et en fonction de la longueur (sauter la messagerie si la date est trop tôt), affichera différents messages personnalisés.

Par exemple, « Vous avez encore x heures pour acheter votre billet pour Londres », mais n’envoyez pas le message si c’est dans les deux heures de vol pour Londres.

{% raw %}
```liquid
{% assigner aujourd'hui = 'maintenant' | date: "%s" %}
{% assigner dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assignez time_to_dep = dep_time | moins : aujourd'hui %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
N'oubliez pas d'acheter votre ticket à {{event_properties.${toStation}}} dans les prochaines 24 heures!
{% else %}
Vous continuez à vous rendre à {{event_properties.${toStation}}} en plus de 24 heures ? Réservez dès maintenant !
{% endif %}
```
{% endraw %}

{% alert important %} Vous aurez besoin d'une propriété d'événement personnalisée. {% endalert %}

### Message dans l'application à envoyer x jours avant la fin de l'adhésion des utilisateurs {#countdown-membership-expiry}

Ce cas d'utilisation capture la date d'expiration de votre adhésion, calcule combien de temps jusqu'à ce qu'il expire, et affiche différents messages en fonction de la durée de votre adhésion expirée.

{% raw %}
```liquid
{% assigner membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days in your trial, assurez-vous de mettre à jour !

{% elsif difference_days > 2 et difference_days <= 4 %}
HURRIE ! Il vous reste {{difference_days}} jours dans votre période d'essai, assurez-vous de passer à niveau!

{% elsif difference_days == 2 %}
DERNIÈRE CHANCE ! Il vous reste {{difference_days}} jours dans votre période d'essai. Assurez-vous de mettre à niveau !

{% else %}
Il vous reste quelques jours dans votre période d'essai. Assurez-vous de mettre à jour !
{% endif %}
```
{% endraw %}

### Personnaliser les messages dans l'application en fonction de la date et de la langue des utilisateurs {#countdown-personalize-language}

Ce cas d'utilisation calcule un compte à rebours pour un événement, et basé sur le paramétrage de langue d'un utilisateur, affichera le compte à rebours dans sa langue.

Par exemple, vous pouvez envoyer une série de messages de vente incitative aux utilisateurs une fois par mois pour leur dire combien de temps une offre est toujours valide avec quatre messages dans l'application:

- Initiale
- 2 jours restants
- Il reste 1 jour
- Dernier jour

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | moins : aujourd'hui %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, Die Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'fr' %}
L'offre est valide jusqu'au 16.04.

{% else %}
L'offre est valable jusqu'au 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Bonjour, l'offre n'est valable qu'aujourd'hui.
{% endif %}

{% else %}
{% abort_message('calculation failed') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Vous devrez assigner une valeur de `date` et inclure une logique d'abandon si la date donnée tombe en dehors de la plage de date. Pour le calcul exact du jour, la date de fin assignée doit comprendre 23:59:59.
{% endalert %}

### Modèle dans la date dans 30 jours à partir de maintenant, formaté en mois et jour {#countdown-template-date}

Ce cas d'utilisation affichera la date de 30 jours à utiliser dans la messagerie.

{% raw %}
```liquid
{% assignez aujourd'hui = 'maintenant' | date: "%s" %}
{% assignez trente jours = aujourd'hui | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Attribut personnalisé

{% apitags %}
Attribut personnalisé
{% endapitags %}

- [Personnaliser un message en fonction des attributs personnalisés correspondants](#attribute-matching)
- [Soustraire deux attributs personnalisés pour afficher la différence comme une valeur monétaire](#attribute-monetary-difference)
- [Référence au prénom d'un utilisateur si son nom complet est stocké dans le champ Prénom](#attribute-first-name)

### Personnaliser un message en fonction des attributs personnalisés correspondants {#attribute-matching}

Cette utilisation vérifie si un utilisateur a des attributs personnalisés spécifiques et, si c'est le cas, affichera différents messages personnalisés.

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true et custom_attribute.${VisitToGroundTooTough} > 0 %}
Le sol est très difficile. La route de la terre va vers l'Est.
{% elsif custom_attribute.${hasShovel} == vrai %}
La route de terre va à l'Est.
{% elsif custom_attribute.${VisitToStart} > 0 %}
La route de terre va vers l'Est.
La pelle ici.
{% else %}
Vous êtes dans une impasse sur une route sale. La route va vers l'est. Dans la distance, vous pouvez voir qu'il finira par s'éteindre. Les arbres sont ici des palmiers royaux très hauts, et ils sont espacés les uns des autres.
Il y a une pelle.
{% endif %}
```
{% endraw %}

### Soustraire deux attributs personnalisés pour afficher la différence comme une valeur monétaire {#attribute-monetary-difference}

Ce cas d'utilisation capture deux attributs personnalisés monétaires, puis calcule et affiche la différence pour indiquer aux utilisateurs jusqu'où ils ont à atteindre leur objectif.

{% raw %}
```liquid
{% assigner event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assigner current_raised = {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference = event_goal | minus: current_raised %}
Vous n'avez que ${{ difference | round: 0 | number_with_delimiter }} à soumettre!
{% endif %}
```
{% endraw %}

### Référence au prénom d'un utilisateur si son nom complet est stocké dans le champ Prénom {#attribute-first-name}

Ce cas d'utilisation capture le prénom d'un utilisateur (si le prénom et le nom de famille sont stockés dans un seul champ) puis utilise ce prénom pour afficher un message de bienvenue.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Bonjour {{name[0]}}, voici votre message!
```

**Explication :** Le filtre `split` transforme la chaîne contenue dans `{{${first_name}}}` en une tableau. En utilisant `{{name[0]}}`, nous ne faisons alors référence qu'au premier élément du tableau, qui est le prénom de l'utilisateur.

{% endraw %}
{% endapi %}

{% api %}

## Événement personnalisé

{% apitags %}
Événement personnalisé
{% endapitags %}

- [Annuler la notification push si un événement personnalisé est dans les deux heures](#event-abort-push)
- [Envoyer une campagne à chaque fois qu'un utilisateur effectue un événement personnalisé trois fois](#event-three-times)
- [Envoyer un message aux utilisateurs qui n'ont acheté qu'une seule catégorie](#event-purchased-one-category)

### Annuler la notification push si un événement personnalisé est dans les deux heures {#event-abort-push}

Ce cas d'utilisation calcule le temps jusqu'à ce qu'un événement, et selon le temps restant, affichera différents messages personnalisés.

Par exemple, vous voudrez peut-être empêcher un push de sortir si une propriété événement personnalisée passe dans les deux prochaines heures. Cet exemple utilise le scénario d'un chariot abandonné pour un billet de train.

{% raw %}
```liquid
{% assigner aujourd'hui = 'maintenant' | date: "%s" %}
{% assigner dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assignez time_to_dep = dep_time | moins : aujourd'hui %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 et {{time_to_dep}} < 86400 %}
N'oubliez pas d'acheter votre ticket à {{event_properties.${toStation}}} dans les prochaines 24 heures
{% else %}
Toujours en voyage à {{event_properties.${toStation}}} dans plus de 24 heures? Réservez maintenant
{% endif %}
```
{% endraw %}

### Envoyer une campagne à chaque fois qu'un utilisateur effectue un événement personnalisé trois fois {#event-three-times}

Cette utilisation vérifie si un utilisateur a effectué un événement personnalisé trois fois, et si c'est le cas, affichera un message ou enverra une campagne.

{% raw %}
```liquid
{% assigner cadence = custom_attribute.${example} | moins : 1 | modulo: 3 %}
{% if custom_attribute.${example} == vide %}
{% abort_message('error calculating cadence') %}
{% elsif cadence != 0 %}
{% abort_message('skip message') %}
{% endif %}
Avez-vous oublié quelque chose dans votre panier ?
```
{% endraw %}

{% alert important %} Vous devez avoir une propriété d'événement du nombre d'événements personnalisés ou utiliser un webhook à votre point de terminaison Braze. Ceci est pour incrémenter un attribut personnalisé (`example_event_count`) chaque fois que l'utilisateur effectue l'événement. Cet exemple utilise une cadence de trois (1, 4, 7, 10, etc.).{% endalert %}

### Envoyer un message aux utilisateurs qui n'ont acheté qu'une seule catégorie {#event-purchased-one-category}

Ce cas d'utilisation capture une liste des catégories achetées par un utilisateur, et si une seule catégorie d'achat existe, elle affichera un message.

{% raw %}
```liquid
{% assigner la catégorie = {{custom_attribute.${categories_purchased}}} %}
{% assigne uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Langue

{% apitags %}
Langue
{% endapitags %}

- [Afficher les noms de mois dans une langue différente](#language-display-month)
- [Personnaliser la messagerie en fonction du jour de la semaine et de la langue de l'utilisateur](#language-personalize-message)

### Afficher les noms de mois dans une langue différente {#language-display-month}

Ce cas d'utilisation affichera la date, le mois et l'année en cours, avec le mois dans une langue différente. L'exemple fourni utilise le suédois.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month)) == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month)) == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month)) == 'April' %}
{{day}} April {{year}}
{% elsif {{month)) == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month)) == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month)) == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month)) == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month)) == 'September' %}
{{day}} September {{year}}
{% elsif {{month)) == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month)) == 'November' %}
{{day}} November {{year}}
{% elsif {{month)) == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Personnaliser la messagerie en fonction du jour de la semaine et de la langue de l'utilisateur {#language-personalize-message}

Cette utilisation vérifie le jour actuel de la semaine et, sur la base du jour, si la langue de l'utilisateur est définie sur l'une des options de langue fournies, elle affichera un message spécifique dans sa langue.

L'exemple fourni s'arrête mardi mais peut être répété pour chaque jour de la semaine.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Achetez aujourd'hui et passez votre apprentissage de langue au niveau supérieur. 🚀

{% elsif ${language} == 'zh' %}
<unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> 🚀

{% else %}
C'est lundi, mais la langue ne correspond pas à 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
文<unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> <unk> 🔓

{% elsif ${language} == 'en' %}
N'oubliez pas de déverrouiller la version complète de votre langue. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
mardi par défaut
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Divers

{% apitags %}
Divers
{% endapitags %}

- [Évitez d'envoyer des e-mails aux clients qui ont bloqué les e-mails de marketing](#misc-avoid-blocked-emails)
- [Mettre en majuscule la première lettre de chaque mot dans une chaîne](#misc-capitalize-words-string)
- [Comparer la valeur de l'attribut personnalisé avec un tableau](#misc-compare-array)
- [Créer un rappel d'événement à venir](#misc-event-reminder)
- [Trouver une chaîne dans un tableau](#misc-string-in-array)
- [Trouver la plus grande valeur dans un tableau](#misc-largest-value)
- [Trouver la plus petite valeur dans un tableau](#misc-smallest-value)
- [Interroger la fin d'une chaîne](#misc-query-end-of-string)
- [Valeurs de requête dans un tableau à partir d'un attribut personnalisé avec plusieurs combinaisons](#misc-query-array-values)

### Évitez d'envoyer des e-mails aux clients qui ont bloqué les e-mails de marketing {#misc-avoid-blocked-emails}

Ce cas d'utilisation prend une liste d'utilisateurs bloqués enregistrés dans un bloc de contenu et s'assure que les utilisateurs bloqués ne sont pas communiqués ou ne sont pas ciblés dans les campagnes à venir ou dans les Canvases.

{% alert important %}
Pour utiliser ce Liquid, enregistrez d'abord la liste des emails bloqués dans un bloc de contenu. La liste ne doit pas avoir d'espaces ou de caractères supplémentaires insérés entre les adresses e-mail (par exemple, `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assigner des emails bloqués = {{content_blocks.${BlockedEmailList}}} | division: ', %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message('Email is blocked') %}
    {% break %}
    {% endif %}
{% endfor %} 
Votre message ici !
```
{% endraw %}

**Explication :** Ici, nous vérifions si l'e-mail de votre destinataire potentiel se trouve dans cette liste en référençant le bloc de contenu des e-mails bloqués. Si l'email est trouvé, le message ne sera pas envoyé.

{% alert note %}
Les blocs de contenu ont une taille limite de 5 Mo.
{% endalert %}

### Mettre en majuscule la première lettre de chaque mot dans une chaîne {#misc-capitalize-words-string}

Cette casse utilise une chaîne de mots, les sépare en un tableau, et capitalise la première lettre de chaque mot.

{% raw %}
```liquid
{% assignez words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% pour les mots dans {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Explication :** Ici, nous avons assigné une variable à notre attribut de chaîne de caractères choisi, et a utilisé le filtre `split` pour séparer la chaîne en un tableau. Nous avons ensuite utilisé la balise `for` pour assigner les mots de la variable `` à chacun des éléments de notre tableau nouvellement créé, avant d'afficher ces mots avec le filtre `majuscule` et le filtre `ajouter` pour ajouter des espaces entre chacun des termes.

### Comparer la valeur de l'attribut personnalisé avec un tableau {#misc-compare-array}

Ce cas d'utilisation prend une liste de boutiques favorites, vérifie si l'un des magasins favoris d'un utilisateur se trouve dans cette liste, et le cas échéant, affichera une offre spéciale de ces magasins.

{% raw %}
```liquid
{% assignez favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contient {{store}} %}
Offre d'aujourd'hui de {{store}}

{% break %}

{% else %}
{% abort_message("No Attribute Found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Cette séquence a une balise `break` dans l'instruction conditionnelle primaire. Cela provoque l'arrêt de la boucle lorsqu'une correspondance est trouvée. Si vous voulez afficher beaucoup ou toutes les correspondances, supprimez la balise `break`. {% endalert %}

### Créer un rappel d'événement à venir {#misc-event-reminder}

Ce cas d'utilisation permet aux utilisateurs de configurer des rappels à venir en fonction d'événements personnalisés. L'exemple de scénario permet à un utilisateur de définir un rappel pour une date de renouvellement de la politique qui est de 26 jours ou plus lorsque les rappels sont envoyés 26, 13, 7 ou 2 jours avant la date de renouvellement de la police.

{% raw %}
```liquid
{% comment %}
Selon la façon dont la propriété reminder_capture est passée au Brésil, avec/sans timestamp, le nombre de jours pourrait avoir un impact sur le fait qu'un utilisateur tombe de part et d'autre de la fenêtre 26/13/7/2 jours.
Une fois que les utilisateurs ont été assignés à un voyage ou un flux de rappel, ils sont ensuite programmés pour entrer dans une Canva subséquente.
Ce 'Écouteur d'événement' peut être utilisé pour scinder les utilisateurs en différents trajets en fonction des propriétés de l'événement personnalisé envoyé à Braze.
{% endcomment %}

{% comment %}
Lorsque vous testez, assurez-vous que l'ID de la campagne, le point de terminaison de l'API Campagne, l'ID de Canvas, le point d'extrémité de l'API Canvas sont entrés correctement. Dans cet exemple, Canvas ID et Canvas API endpoint ont été configurés pour le partage avec le client; en pratique, cela peut être testé en utilisant un ID de campagne et un point de terminaison d'API de campagne.
{% endcomment %}

{% comment %}
L'étape suivante calcule combien il y a entre la date d'aujourd'hui et la date de rappel comme 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: "%s" %}
{% assigner rappel_start_date = {{event_properties.${reminder_date}}} | date: "%s" %}
{% assigner time_to_reminder = reminder_start_date | moins : aujourd'hui %}

{% comment %}
L'étape suivante vérifie si le time_to_reminder est de plus de 26 jours de distance ; si c'est vrai, alors l'utilisateur est programmé pour entrer dans le Canvas suivant 26 jours avant la date de rappel.
L'heure est convertie de 'secondes à partir de 1970' à la date de rappel appropriée dans le format requis ISO 8601.
N.B. Des fuseaux horaires supplémentaires devraient être fournis en ajoutant une propriété API Schedule supplémentaire de "in_local_time"
{% endcomment %}

{% si {{time_to_reminder}} > 2246400 %}
{% assignez time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: "%Y-%m-%dT%H:%M" }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: "%Y-%m-%dT%H:%M:%S+0000" }}"
}
}

{% comment %}
L'étape suivante vérifie si le time_to_reminder est à moins de 26 jours mais à plus de 13 jours.
Les utilisateurs sont programmés pour entrer dans le voyage le 13.
{% endcomment %}

{% elsif 1123200 < {{time_to_reminder}} et {{time_to_reminder}} < 2246399 %}
{% assignez time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "2021-03-24T20:04:00+0000"
}
}

{% comment %}
L'étape suivante vérifie si le time_to_reminder est à moins de 13 jours mais à plus de sept jours de distance.
Les utilisateurs sont programmés pour entrer dans le voyage le jour 7.
{% endcomment %}

{% elsif 604800 < {{time_to_reminder}} et {{time_to_reminder}} < 1123199 %}
{% assignez time_to_first_message = reminder_start_date | plus : 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: "%Y-%m-%dT%H:%M:%S+0000" }}"
}
}

{% comment %}
L'étape suivante vérifie si le time_to_reminder est à moins de sept jours mais à plus de deux jours.
Les utilisateurs sont programmés pour entrer dans le voyage le deuxième jour.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 et {{time_to_reminder}} > 172860 %}
{% assignez time_to_first_message = reminder_start_date | plus : 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: "%Y-%m-%dT%H:%M:%S+0000}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_x}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: "%Y-%m-%dT%H:%M:%S+0000" }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %}

Vous aurez besoin d'un événement personnalisé `reminder_capture`, et les propriétés de l'événement personnalisé doivent inclure au moins :

- `rappel-id`: Identifiant de l'événement personnalisé
- `rappel_date`: date de soumission par l'utilisateur lorsque son rappel est dû
- `message_personalisation_X`: Toute propriété nécessaire pour personnaliser le message lors de l'envoi

{% endalert %}

### Trouver une chaîne dans un tableau {#misc-string-in-array}

Cette utilisation vérifie si un tableau d'attributs personnalisés contient une chaîne spécifique, et s'il existe, affichera un message spécifique.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contient 'Hertz' %}
Liez votre compte Hertz pour utiliser la Voie Rapide Hertz.

{% elsif custom_attribute.${airportCompleted} == false %}
Clear vous aide à passer par la sécurité de l'aéroport. Complétez votre installation unique en personne la prochaine fois que vous serez à l'aéroport. Cela ne prend que 5 minutes.

{% else %}
Votre compte est entièrement configuré
{% endif %}
```
{% endraw %}

### Trouver la plus grande valeur dans un tableau {#misc-largest-value}

Ce cas d'utilisation calcule la valeur la plus élevée dans un tableau d'attributs personnalisés à utiliser dans la messagerie utilisateur.

Par exemple, vous pouvez montrer à un utilisateur quel est le meilleur score actuel ou l'enchère la plus élevée sur un objet.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% pour l'attribut dans {{custom_attribute.${array_attribute}}} %}
{% assigner compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Vous devez utiliser un attribut personnalisé qui a une valeur entière et fait partie d'un tableau (liste). {% endalert %}

### Trouver la plus petite valeur dans un tableau {#misc-smallest-value}

Ce cas d'utilisation calcule la valeur la plus basse dans un tableau d'attributs personnalisés à utiliser dans la messagerie utilisateur.

Par exemple, vous voudrez peut-être montrer à un utilisateur quel est le score le plus bas ou l'article le moins cher.

{% raw %}
```liquid
{% assigner minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% pour l'attribut dans {{custom_attribute.${array_attribute}}} %}
{% assigner compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Vous devez utiliser un attribut personnalisé qui a une valeur entière et fait partie d'un tableau (liste). {% endalert %}

### Interroger la fin d'une chaîne {#misc-query-end-of-string}

Utilise des requêtes de cas à la fin d'une chaîne de caractères à utiliser dans la messagerie.

{% raw %}
```liquid
{% assigne d'intérêt = {{custom_attribute.{Buyer Interest}} | premier } %}
{% assign marketplace = {{{{interest}} | division: "" | reverse | join: "" | truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Votre dernière recherche sur le marché était sur {{custom_attribute.{Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Découvrez toutes nos nouvelles offres.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Valeurs de requête dans un tableau à partir d'un attribut personnalisé avec plusieurs combinaisons {#misc-query-array-values}

Ce cas d'utilisation prend une liste de séries bientôt expirées, vérifie si l'une des séries favorites d'un utilisateur se trouve dans cette liste, et si c'est le cas, affichera un message avertissant l'utilisateur qu'il expirera bientôt.

{% raw %}
```liquid
{% assigner expired_shows = 'Famille moderne,The Rookie,Body of Preof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.{Favorite Shows}}} contient {{show}} %}
{% assignez new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assignez new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

Tous les épisodes de {{new_shows_clean | join: ', ' }} expirent le 9/8 - regardez-les maintenant avant leur disparition !

{% else %}
{% abort_message("Not Found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Vous devrez d'abord trouver des correspondances entre les tableaux, puis construire une logique à la fin pour séparer les parties. {% endalert %}


{% endapi %}

{% api %}

## Ciblage de la plateforme

{% apitags %}
Ciblage de la plateforme
{% endapitags %}

- [Différencier la copie de message dans l'application par le système d'exploitation de l'appareil](#platform-device-os)
- [Ciblez uniquement une plateforme spécifique](#platform-target)
- [Cibler uniquement les appareils iOS avec une version d'OS spécifique](#platform-target-ios-version)
- [Cible uniquement pour les navigateurs Web](#platform-target-web)
- [Cibler un opérateur mobile spécifique](#platform-target-carrier)

### Différencier la copie de message dans l'application par le système d'exploitation de l'appareil {#platform-device-os}

Cette utilisation vérifie la plate-forme sur laquelle un utilisateur se trouve, et en fonction de sa plate-forme, affichera un message spécifique.

Par exemple, vous pouvez montrer aux utilisateurs mobiles des versions plus courtes de la copie des messages tout en montrant aux autres utilisateurs la version régulière et plus longue de la copie. Vous pouvez également montrer aux utilisateurs mobiles certains messages pertinents pour eux mais qui ne seraient pas pertinents pour les utilisateurs du Web. Par exemple, la messagerie iOS peut parler d'Apple Pay, mais la messagerie Android devrait mentionner Google Pay.

{% raw %}
```liquid
{% si ciblé_device.${platform} == "ios" ou ciblé_device.${platform} == "android" %}
Ceci est une copie plus courte.

{% else %}
Ceci est la copie régulière et beaucoup plus longue que la version courte. 
{% endif %}
```
{% endraw %}

{% alert note %}
Le liquide est sensible à la casse, `ciblé_device.${platform}` renvoie la valeur en minuscules.
{% endalert %}

### Ciblez uniquement une plateforme spécifique {#platform-target}

Ce cas d'utilisation capturera la plate-forme de l'appareil des utilisateurs, et en fonction de la plate-forme, affichera un message.

Par exemple, vous pouvez seulement envoyer un message aux utilisateurs Android. Cela peut être utilisé comme alternative à la sélection d'une application dans l'outil Segmentation.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

Ceci est un message pour un utilisateur Android ! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Cibler uniquement les appareils iOS avec une version d'OS spécifique {#platform-target-ios-version}

Cette utilisation vérifie si la version de l'OS d'un utilisateur tombe dans un certain ensemble de versions et, si c'est le cas, affichera un message spécifique.

L'exemple utilisé envoie un avertissement aux utilisateurs sur iOS 10.0 ou moins qu'ils sont en train de supprimer le support du périphérique OS de l'utilisateur.

{% raw %}
```liquid
{% si {{targeted_device.${os}}} == "10.0" ou {{targted_device.${os}}} == "10.0.1" ou {{targted_device.${os}}} == "10.0.2" ou {{targeted_device.${os}}} == "10.0.3" ou {{targeted_device.${os}}} == “10.1” ou {{targeted_device.${os}}} == “10.2” ou {{targeted_device.${os}}} == “10.2.${os}}} == « 10.3 » ou {{targted_device.${os}}} == « 10.3 » ou {{targted_device. ${os} }} == « 10.3.1 » ou {{targeted_device.${os}}} == « 10.3.2 » ou {{targeted_device.${os}}} == « 10.3.3 » ou {{targeted_device.${os}}} == « 10. .4 ou {{targeted_device.${os}}} == “9.3.1” ou {{targeted_device.${os}}} == “9.3. » ou {{targted_device.${os}}} == “9.3.3” ou {{targted_device.${os}}} == “9.3.4” ou {{targeted_device.${os}}} == "9.3.5" %}

Nous sommes en train de supprimer le support du système d'exploitation de votre appareil. Assurez-vous de mettre à jour le logiciel le plus récent pour la meilleure expérience de l'application.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cible uniquement pour les navigateurs web {#platform-target-web}

Ce cas d'utilisation vérifie si le périphérique cible d'un utilisateur s'exécute sur Mac ou Windows et, dans l'affirmative, affichera un message spécifique.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' OU {{targeted_device.${os}}} == 'Windows' %}

Ce message s'affichera sur votre navigateur web de bureau.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler un opérateur mobile spécifique {#platform-target-carrier}

Cette utilisation vérifie si le transporteur de l'appareil d'un utilisateur est Verizon, et si c'est le cas, affichera un message spécifique.

Pour les notifications push et les canaux de messages intégrés à l’application, vous pouvez spécifier l’opérateur de l’appareil dans le corps de votre message en utilisant Liquid. Si le transporteur de l'appareil du destinataire ne correspond pas, le message ne sera pas envoyé.

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contient "verizon" ou {targeted_device.${carrier}} contient "Verizon" %}

Ceci est un message pour les utilisateurs de Verizon !

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Fuseaux horaires

{% apitags %}
Fuseaux horaires
{% endapitags %}

- [Ajouter le fuseau horaire CST à un attribut personnalisé](#time-append-cst)
- [Insérer un horodatage](#time-insert-timestamp)
- [Envoyer un push Canvas uniquement pendant une fenêtre de temps dans le fuseau horaire local d'un utilisateur](#time-canvas-window)
- [Envoyer une campagne de messages récurrents dans l'application entre une fenêtre d'heure dans le fuseau horaire local d'un utilisateur](#time-reocurring-iam-window)
- [Envoyer des messages différents les jours de la semaine et les week-ends dans le fuseau horaire local de l'utilisateur](#time-weekdays-vs-weekends)
- [Envoyer différents messages en fonction de l'heure dans le fuseau horaire local d'un utilisateur](#time-of-day)

### Ajouter le fuseau horaire CST à un attribut personnalisé {#time-append-cst}

Ce cas d'utilisation affiche un attribut de date personnalisé dans un fuseau horaire donné.

Option 1 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Option 2 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'Amérique/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Insérer un horodatage {#time-insert-timestamp}

Ce cas d'utilisation affiche un message qui inclut un horodatage dans leur fuseau horaire actuel.

L'exemple fourni ci-dessous affichera la date comme AAAA-mm-jj HH:MM:SS, comme 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | par défaut: 'Vous'}} a reçu une campagne, affichée à ({{ "maintenant" | fuseau horaire: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Envoyer un push Canvas uniquement pendant une fenêtre de temps dans le fuseau horaire local d'un utilisateur {#time-canvas-window}

Cette utilisation vérifie l'heure d'un utilisateur dans son fuseau horaire local, et si elle tombe dans une heure définie, elle affichera un message spécifique.

{% raw %}
```liquid
{% assigner heure = 'maintenant' | fuseau horaire : ${time_zone} %}
{% assigner heure = heure | date: '%H' | plus: 0 %}
{% si heure > 20 ou heure < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Voici un message qui va être envoyé entre 8 h et 8 h !
```
{% endraw %}

### Envoyer une campagne de messages récurrents dans l'application entre une fenêtre d'heure dans le fuseau horaire local d'un utilisateur {#time-reocurring-iam-window}

Ce cas d'utilisation affichera un message si l'heure actuelle d'un utilisateur tombe dans une fenêtre définie.

Par exemple, le scénario ci-dessous fait savoir à un utilisateur qu'une boutique est fermée.

{% raw %}
```liquid
{% assigner temps = 'maintenant' | fuseau horaire : ${time_zone} %} 
{% assigner heure = heure | date: '%H' | plus: 0 %}
{% si heure > 21 ou heure < 10 %}

Les magasins sont fermés. Revenez entre 11h et 21h !

{% else %} 
{% abort_message("not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Envoyer des messages différents les jours de la semaine et les week-ends dans le fuseau horaire local de l'utilisateur {#time-weekdays-vs-weekends}

Ce cas d'utilisation vérifiera si le jour actuel de la semaine d'un utilisateur est le samedi ou le dimanche, et selon le jour, affichera différents messages.

{% raw %}
```liquid
{% assigne aujourd'hui = 'maintenant' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Samedi' or {{today}} == 'Dimanche' %}
C'est {{today}}, pourquoi ne pas ouvrir l'application pour vos transactions ?

{% else %}
C'est {{today}}, pourquoi ne pas visiter le magasin ?
{% endif %}
```
{% endraw %}

### Envoyer différents messages en fonction de l'heure dans le fuseau horaire local d'un utilisateur {#time-of-day}

Ce cas d'utilisation affichera un message si l'heure actuelle d'un utilisateur tombe en dehors d'une fenêtre définie.

Par exemple, vous voudrez peut-être parler à un utilisateur d'une opportunité qui dépend de l'heure de la journée.

{% raw %}
```liquid
{% assigner temps = 'maintenant' | fuseau horaire : ${time_zone} %}
{% assigner heure = heure | date: '%H' | plus: 0 %}
{% si heure > 20 ou heure < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Découvrez ce nouveau bar après travail aujourd'hui. Spéciaux HH !
```
{% endraw %}

{% alert note %} C'est l'inverse de [heures silencieuses]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns). {% endalert %}

{% endapi %}

{% api %}

## Semaine/Jour/Mois

{% apitags %}
Semaine/Jour/Mois
{% endapitags %}

- [Insérez le nom du mois précédent dans un message](#month-name)
- [Envoyer une campagne à la fin de chaque mois](#month-end)
- [Envoyer une campagne le dernier (semaine) du mois](#day-of-month-last)
- [Envoyer un message différent chaque jour du mois](#day-of-month)
- [Envoyer un message différent chaque jour de la semaine](#day-of-week)

### Insérez le nom du mois précédent dans un message {#month-name}

Ce cas d'utilisation prendra le mois courant et affichera le mois précédent pour être utilisé dans la messagerie.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 12 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

### Envoyer une campagne à la fin de chaque mois {#month-end}

Ce cas d'utilisation vérifiera si la date courante tombe dans une liste de dates, et selon la date, affichera un message spécifique.

{% alert note %} Cela ne tient pas compte des années bissextiles (29 février). {% endalert %}

{% raw %}
```liquid
{% assigner current_date = 'maintenant' | date : '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

La date est correcte

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Envoyer une campagne le dernier (semaine) du mois {#day-of-month-last}

Ce cas d'utilisation capture le mois et le jour en cours et calcule si le jour actuel tombe dans le dernier jour de la semaine du mois.

Par exemple, vous voudrez peut-être envoyer une enquête à vos utilisateurs le dernier mercredi du mois pour demander des commentaires sur le produit.

{% raw %}
```liquid
{% comment %}Tirez le jour, le nom, le mois et l'année à partir de la date d'aujourd'hui.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assignez le nombre de jours correct pour le mois en cours.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assignez le nombre de jours correct si le mois actuel est février, en tenant compte des années bissextiles.{% endcomment %}

{% assigner leap_year_remainder = {{current_year | modulo: 4 }} ! "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Vérifiez que la date d'aujourd'hui est dans la semaine du dernier jour du mois. Si ce n'est pas le cas, annulez le message. Dans l'affirmative, vérifiez que nous sommes mercredi. Si ce n'est pas le cas, annulez le message.{% endcomment %}

{% assignez diff_in_days = last_day_of_month | moins : current_day | plus: 1%}
{% if diff_in_days <= 7 %}
{% unless current_day_name == "Wed" %}
{% abort_message() %}
{% endunless %}
{% else %}
{% abort_message() %}
{% endif %}


```
{% endraw %}

### Envoyer un message différent chaque jour du mois {#day-of-month}

Cette utilisation vérifie si la date courante correspond à une date sur une liste, et selon le jour, affichera un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Envoyer un message différent chaque jour de la semaine {#day-of-week}

Cette utilisation vérifie le jour de la semaine en cours et, selon le jour, affichera un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case 'today' %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %} Vous pouvez remplacer la ligne "copie par défaut" par {% raw %}`{% abort_message() %}`{% endraw %} pour empêcher l'envoi du message si le jour de la semaine est inconnu. {% endalert %}

{% endapi %}
