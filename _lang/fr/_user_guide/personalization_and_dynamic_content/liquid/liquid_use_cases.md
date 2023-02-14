---
nav_title: Bibliothèque de scénarios d’utilisation de Liquid
article_title: Bibliothèque de scénarios d’utilisation de Liquid
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Cette page d’accueil est une présentation des scénarios d’utilisation de Liquid organisés par catégorie, tels que les anniversaires, l’utilisation d’applications, les comptes à rebours, etc."

---

{% api %}

## Anniversaires et fêtes

{% apitags %}
Anniversaires et fêtes
{% endapitags %}

- [Personnaliser les messages en fonction de l’année anniversaire d’un utilisateur](#anniversary-year)
- [Personnaliser les messages en fonction de la semaine d’anniversaire d’un utilisateur](#birthday-week)
- [Envoyer des campagnes aux utilisateurs pendant leur mois d’anniversaire](#birthday-month)
- [Évitez d’envoyer des messages lors des fêtes principales](#holiday-avoid)

### Personnaliser les messages en fonction de l’année anniversaire d’un utilisateur {#anniversary-year}

Ce scénario d’utilisation montre comment calculer l’anniversaire d’utilisation d’une application d’un utilisateur en fonction de sa date d’inscription initiale et afficher différents messages en fonction du nombre d’années célébrées.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %} 
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %} 
{% if this_day == anniversary_day %} 
{% if anniversary_year == '2021' %}
Il y a exactement un an, nous avons rencontré pour la première fois !

{% elsif anniversary_year == '2020' %}
Il y a exactement deux ans, nous nous sommes rencontrés pour la première fois !

{% elsif anniversary_year == '2019' %}
Il y a exactement trois ans, nous nous sommes rencontrés pour la première fois !

{% else %}
{% abort_message(pas la même année) %}
{% endif %}

{% else %} 
{% abort_message(pas le même jour) %} 
{% endif %}

{% else %}
{% abort_message(pas le même mois) %}
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous utilisons la variable réservée `now` (maintenant) pour modéliser la date et l’heure actuelles au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"). Les filtres `%B` (mois, p ex., « mai ») et `%d` (jour, p ex., format « 18 ») formatent le mois et le jour en cours. Nous utilisons ensuite les mêmes filtres de date et de temps sur les valeurs `signup_date` pour nous assurer de comparer les deux valeurs à l’aide des balises conditionnelles et de la logique.

Ensuite, nous renouvelons trois autres énoncés variables pour obtenir `%B` et `%d` pour le `signup_date`, mais ajoutons également `%Y` (année, p ex., « 2021 »). Ceci compose la date et de l’heure du `signup_date` sous forme d’année. Connaître le jour et le mois nous permet de vérifier si l’anniversaire de l’utilisateur est aujourd’hui, et en sachant que l’année nous dit combien d’années ont passées, ce qui nous permet de savoir pour combien d’années le féliciter !

{% alert tip %} Vous pouvez créer autant de conditions que d’années au cours desquelles vous avez collecté des dates d’inscription. {% endalert %}  

### Personnaliser les messages en fonction de la semaine d’anniversaire d’un utilisateur {#birthday-week}

Ce scénario d’utilisation présente comment trouver l’anniversaire d’un utilisateur, le comparer à la date actuelle, puis afficher des messages d’anniversaire spéciaux avant, pendant et après la semaine d’anniversaire.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Joyeux anniversaire pour la semaine dernière !
{% elsif {{birthday_week}} == {{this_week}} %}
Joyeux anniversaire pour cette semaine !
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Joyeux anniversaire pour la semaine prochaine !
{% else %}
Pas d’anniversaire pour vous !
{% endif %}
```
{% endraw %}

**Explication :** Similaire au scénario d’utilisation de l’[année anniversaire](#anniversary-year), nous prenons ici la variable réservée `now` et utilisons le filtre `%W` (semaine, p ex., semaine 12 sur 52 dans un an) pour obtenir la semaine de l’année à laquelle correspond l’anniversaire d’inscription de l’utilisateur. Si la semaine d’anniversaire de l’utilisateur correspond à la semaine en cours, nous lui envoyons un message de félicitations ! 

Nous incluons également des déclarations pour `last_week` et `next_week` pour personnaliser votre message.

### Envoyer des campagnes aux utilisateurs pendant leur mois d’anniversaire {#birthday-month}

Ce scénario d’utilisation indique comment calculer le mois d’anniversaire d’un utilisateur, vérifier si son anniversaire tombe pendant le mois en cours et, si tel est le cas, envoyer un message spécial.

{% raw %}
```liquid
{% assign this_month = ‘now’ | date: “%B” %}
{% assign birth_month = {{${date_of_birth}}} | date: “%B” %}
{% if {{this_month}} == {{birth_month}} %}
Corps du message 
{% else %} 
{% abort_message() %}
{% endif %}
```
{% endraw %}

**Explication :** Similaire au scénario d’utilisation de la [semaine anniversaire](#birthday-week) , néanmoins, ici nous utilisons le filtre `%B` (mois, p ex., « mai ») pour calculer les utilisateurs dont l’anniversaire intervient ce mois-ci. Une application potentielle pourrait traiter les utilisateurs ayant un anniversaire dans un e-mail mensuel.

### Évitez d’envoyer des messages lors des fêtes principales {#holiday-avoid}

Ce scénario d’utilisation indique comment envoyer des messages pendant la période des fêtes tout en évitant les jours fériés principaux, lorsque l’engagement est susceptible d’être faible.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2021-12-24" or today == "2021-12-25" or today == "2021-12-26” %}
{% abort_message %}
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous attribuons le terme `today` (aujourd’hui) à la variable réservée `now` (la date et l’heure actuelles), à l’aide des filtres ` %Y(année, p ex., « 2021 »), ` (mois, p ex., « 12 »), et  (jour, p ex., « 25 »)`%m` pour formater la date.`%d` Nous exécutons ensuite notre déclaration conditionnelle pour dire que si la variable `today` correspond aux jours fériés de votre choix, le message sera abandonné. 

L’exemple présenté correspond à la veille de Noël, le jour de Noël et le lendemain de Noël.

{% endapi %}

{% api %}

## Utilisation de l’application

{% apitags %}
Utilisation de l’application
{% endapitags %}

- [Envoyer des messages dans la langue d’un utilisateur s’il s’est connecté à une session](#app-session-language)
- [Personnaliser les messages en fonction du moment où un utilisateur a ouvert l’application](#app-last-opened)
- [Afficher un message différent si un utilisateur a utilisé l’application il y a moins de trois jours](#app-last-opened-less-than)

### Envoyer des messages dans la langue d’un utilisateur s’il s’est connecté à une session {#app-session-language}

Ce scénario d’utilisation vérifie si un utilisateur s’est connecté à une session, et si ce n’est pas le cas, inclut une logique d’affichage d’un message reposant sur la langue collecté manuellement via un attribut personnalisé, le cas échéant. S’il n’y a pas d’informations de langue liées au compte, il affiche le message dans la langue par défaut. Si un utilisateur s’est connecté à une session, il extrait toutes les informations de langue liées à l’utilisateur et affiche le message approprié. 

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message en Anglais basé sur un attribut personnalisé
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message en Français basé sur un attribut personnalisé
{% else %}
Pas de langue définie - Langue par défaut
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message en Anglais basé sur la langue
{% elsif ${language} == 'fr' %}
Message en Français basé sur la langue
{% else %}
Une langue est définie - Langue par défaut
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Explication :** Ici, nous utilisons deux `if` (si) énoncés regroupés, imbriqués. Le premier énoncé `if` vérifie si l’utilisateur a démarré une session en vérifiant si le `last_used_app_date` est `nil` (nul). En effet, `{{${language}}}` est automatiquement collecté par le SDK lorsqu’un utilisateur se connecte à une session. Si l’utilisateur ne s’est pas connecté à une session, nous n’avons pas encore sa langue, donc cette vérification s’effectue si des attributs personnalisés liés à la langue ont été enregistrés et, sur la base de ces informations, affiche un message dans cette langue, si possible. 
{% endraw %}

Le second énoncé `if` vérifie l’attribut de base (par défaut), car l’utilisateur n’a pas `nil` pour le `last_used_app_date`, ce qui signifie qu’il s’est connecté à une session et que nous avons sa langue.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) est une variable réservée qui est retournée lorsque le code Liquid n’a aucun résultat. `Nil` est traité comme `false` dans un bloc `if`.
{% endalert %}

### Personnaliser les messages en fonction du moment où un utilisateur a ouvert l’application {#app-last-opened}

Ce scénario d’utilisation calcule la dernière fois la dernière ouverture de l’application par l’utilisateur et affiche un message personnalisé différent selon la durée.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Contents de vous revoir !
{% else %}
Cela faisait longtemps. Voici quelques-unes de nos dernières mises à jour.
{% endif %}
```
{% endraw %}

### Afficher un message différent si un utilisateur a utilisé l’application il y a moins de trois jours {#app-last-opened-less-than}

Ce cas d'utilisation calcule depuis combien de temps un utilisateur a utilisé votre application et, en fonction de la durée, affiche un message personnalisé différent.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message pour un utilisateur récemment actif
{% else %}
Message pour un utilisateur moins actif
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Comptes à rebours

{% apitags %}
Comptes à rebours
{% endapitags %}

- [Ajouter X jours à partir de date d’aujourd’hui](#countdown-add-x-days)
- [Calculer un compte à rebours à partir d’un point dans le temps](#countdown-difference-days)
- [Créer un compte à rebours pour les dates et priorités d’expédition spécifiques](#countdown-shipping-options)
- [Créer un compte à rebours en jours](#countdown-days)
- [Créer un compte à rebours de jours à heures à minutes](#countdown-dynamic)
- [Affiche le nombre de jours restant avant une date donnée](#countdown-future-date)
- [Afficher le nombre de jours restants jusqu’à ce qu’un attribut de date personnalisée arrive](#countdown-custom-date-attribute)
- [Afficher le temps restant et interrompre le message s’il n’y a que X temps restant](#countdown-abort-window)
- [Messages in-app pour envoyer X jours avant la fin de l’abonnement de l’utilisateur](#countdown-membership-expiry)
- [Personnaliser les messages in-app en fonction de la date et de la langue de l’utilisateur](#countdown-personalize-language)
- [Modèle de date 30 jours à partir d’aujourd’hui, formaté en tant que mois et jour](#countdown-template-date)

### Ajouter X jours à partir de date d’aujourd’hui {#countdown-add-x-days}

Ce scénario d’utilisation ajoute un nombre spécifique de jours à la date actuelle à référencer et ajouter dans les messages. Par exemple, vous pouvez envoyer un message de milieu de semaine qui présente des événements dans la région pendant le week-end, comme « Voici les films que nous présenterons dans 3 jours ! »

{% raw %}
```liquid
{{ "maintenant » | date : « %s » | plus : 259200 | date :« %F » }}
```
{% endraw %}

La valeur `plus` sera toujours en secondes, donc nous finissons par le filtre `%F` pour traduire les secondes en jours.

{% alert important %}
Vous pouvez inclure une URL ou un lien profond vers une liste d’événements dans votre message afin d’envoyer l’utilisateur une liste d’actions qui se produisent à l’avenir. 
{% endalert %}

### Calculer un compte à rebours à partir d’un point dans le temps {#countdown-difference-days}

Ce scénario d’utilisation calcule la différence de jours entre une date spécifique et la date actuelle. Cette différence peut servir à afficher un compte à rebours à vos utilisateurs.

{% raw %}
```liquid
{% assign event_date = '2020-08-19' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
il vous reste {{ difference_days }} jours !
```
{% endraw %}

### Créer un compte à rebours pour les dates et priorités d’expédition spécifiques {#countdown-shipping-options}

Ce scénario d’utilisation capture différentes options d’expédition, calcule la durée nécessaire à la réception et affiche des messages encourageant les utilisateurs à acheter à temps pour recevoir leur colis à une date donnée.

{% raw %}
```liquid
{% assign standard_shipping_start = "2019-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2019-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2019-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2019-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
jours de différence s : {{difference_s_days}}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
jours de différence e : {{difference_e_days}}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
C'est le dernier jour de commande avec l'expédition standard pour que votre commande arrive à temps pour la veille de Noël !
{% elsif difference_s_days == 1 %}
Il reste {{difference_s_days}} jour de commande avec l'expédition standard pour que votre commande arrive à temps pour la veille de Noël !

{% else %}
Il reste {{difference_s_days}} jours de commande avec l'expédition standard pour que votre commande arrive à temps pour la veille de Noël !
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
Il reste {{difference_e_days}} jour de commande avec l'expédition express pour que votre commande arrive à temps pour la veille de Noël !
{% else %}
Il reste {{difference_e_days}} jours de commande avec l'expédition express pour que votre commande arrive à temps pour la veille de Noël !
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
C'est le dernier jour de commande avec l'expédition de nuit pour que votre commande arrive à temps pour la veille de Noël !
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Créer un compte à rebours en jours {#countdown-days}

Ce scénario d’utilisation calcule le temps restant entre un événement spécifique et la date actuelle et affiche le nombre de jours restants jusqu’à l’événement.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Votre commande arrivera dans {{ difference_days }} jours !
```
{% endraw %}

{% alert important %}
Vous aurez besoin d’un champ d’attribut personnalisé avec une valeur de `date`.
{% endalert %}

### Créer un compte à rebours de jours à heures à minutes {#countdown-dynamic}

Ce scénario d’utilisation calcule le temps restant entre un événement spécifique et la date actuelle. En fonction du temps restant jusqu’à l’événement, il modifie la valeur de temps (jours, heures, minutes) pour afficher différents messages personnalisés.

Par exemple, s’il y a reste deux jours jusqu’à ce que la commande d’un client arrive, vous pourriez dire : « Votre commande arrivera dans 2 jours. » Alors que s’il reste moins d’un jour, vous pouvez le modifier « Votre commande arrivera dans 17 heures ».

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
Il vous reste {{difference_hours}} heures avant l'arrivée de votre commande !
{% elsif {{difference_minutes}} < 59 %}
Il vous reste {{difference_minutes}} minutes avant l'arrivée de votre commande !
{% else %}
Il vous reste {{difference_days}} jours avant l'arrivée de votre commande !
{% endif %}
```
{% endraw %}

{% alert important %}
Vous aurez besoin d’un champ d’attribut personnalisé avec une valeur de `date`. Vous devrez également définir des seuils de temps lorsque vous voulez afficher le temps en jours, heures et minutes.
{% endalert %}

### Affiche le nombre de jours restant avant une date donnée {#countdown-future-date}

Ce scénario d’utilisation calcule le temps restant entre un événement spécifique et la date actuelle et affiche un message indiquant le nombre de jours restants jusqu’à l’événement.

{% raw %}
```liquid
{% assign event_date = '2019-02-19' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Il y a {{difference_days}} jusqu'à votre anniversaire !
{% endif %}
```
{% endraw %}

### Afficher le nombre de jours restants jusqu’à ce qu’un attribut de date personnalisée arrive {#countdown-custom-date-attribute}

Ce scénario d’utilisation calcule la différence en jours entre les dates actuelles et futures et affiche un message si la différence correspond à un nombre défini.

Dans cet exemple, un utilisateur recevra un message dans les deux jours suivant l’attribut de date personnalisée. Sinon, le message ne sera pas envoyé.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Votre opération est dans 2 jours le {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Afficher le temps restant et interrompre le message s’il n’y a que X temps restant {#countdown-abort-window}

Ce cas d’utilisation calcule la durée jusqu’à une certaine date et, en fonction de la longueur (saut de message si la date est trop courte), affiche différents messages personnalisés. 

Par exemple, « Vous avez x heures restantes pour acheter pour acheter votre billet pour Londres », mais ne pas envoyez le message dans les deux heures qui précèdent l’heure de vol pour Londres.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate moins de 2 heures") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
N'oubliez pas d'acheter votre billet pour {{event_properties.${toStation}}} dans les 24 prochaines heures !
{% else %}
Vous partez toujours en voyage pour {{event_properties.${toStation}}} dans plus de 24 heures ? Réservez maintenant !
{% endif %}
```
{% endraw %}

{% alert important %} Vous aurez besoin de créer de événements personnalisés. {% endalert %}

### Messages in-app pour envoyer X jours avant la fin de l’abonnement de l’utilisateur {#countdown-membership-expiry}

Ce scénario d’utilisation capture la date d’expiration de votre abonnement, calcule la durée jusqu’à ce qu’elle expire et affiche différents messages en fonction du délai d’expiration de votre abonnement.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
Il vous reste {{difference_days}} jours d'essai, assurez-vous d'effectuer la mise à niveau !

{% elsif difference_days > 2 and difference_days <= 4 %}
DÉPÊCHEZ-VOUS ! Il vous reste {{difference_days}} jours d'essai, assurez-vous d'effectuer la mise à niveau !

{% elsif difference_days == 2 %}
DERNIÈRE CHANCE ! Il vous reste {{difference_days}} jours d'essai. Assurez-vous d'effectuer la mise à niveau !

{% else %}
Il vous reste quelques jours d'essai. Assurez-vous d'effectuer la mise à niveau !
{% endif %}
```
{% endraw %}

### Personnaliser les messages dans l’appli en fonction de la date et de la langue de l’utilisateur {#countdown-personalize-language}

Ce scénario d’utilisation calcule un compte à rebours jusqu’à un événement et, en fonction du paramètre de langue d’un utilisateur, affiche le compte à rebours dans sa langue.

Par exemple, vous pouvez envoyer une série de messages incitatifs aux utilisateurs une fois par mois pour leur indiquer combien de temps une offre reste valide avec quatre messages dans l’application :

- Initial
- 2 jours restants
- 1 jour restant
- Dernier jour

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16,04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16,04.

{% elsif ${language} == 'en' %}
L'offre est valable jusqu'au 16/04.

{% else %}
L'offre est valable jusqu'au 16/04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSÉRER UN MESSAGE

{% elsif ${language} == 'ch' %}
INSÉRER UN MESSAGE

{% elsif ${language} == 'en' %}
INSÉRER UN MESSAGE

{% else %}
INSÉRER UN MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSÉRER UN MESSAGE

{% elsif ${language} == 'ch' %}
INSÉRER UN MESSAGE

{% elsif ${language} == 'en' %}
INSÉRER UN MESSAGE

{% else %}
INSÉRER UN MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Bonjour, l'offre n'est valable qu'aujourd'hui.
{% endif %}

{% else %}
{% abort_message('échec du calcul') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Vous devrez attribuer une valeur `date` et inclure la logique d’abandon si la date donnée tombe en dehors de la plage de dates. Pour les calculs de jour exacts, la date de fin attribuée doit inclure 23:59:59.
{% endalert %}

### Modèle de date 30 jours à partir d’aujourd’hui, formaté en tant que mois et jour {#countdown-template-date}

Ce scénario d’utilisation affiche la date 30 jours à partir de maintenant à utiliser dans les messages.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Attribut personnalisé

{% apitags %}
Attribut personnalisé
{% endapitags %}

- [Personnaliser un message en fonction des attributs personnalisés correspondants](#attribute-matching)
- [Soustrayez deux attributs personnalisés pour afficher la différence en valeur monétaire](#attribute-monetary-difference)
- [Indiquez le prénom d’un utilisateur si son nom complet est stocké dans le first_name champ](#attribute-first-name)

### Personnaliser un message en fonction des attributs personnalisés correspondants {#attribute-matching}

Ce scénario d’utilisation vérifie si un utilisateur a des attributs personnalisés spécifiques et, le cas échéant, affiche différents messages personnalisés. 

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
Le sol est très dur. Le chemin de terre va vers l'est.
{% elsif custom_attribute.${hasShovel} == true %}
Le chemin de terre va vers l'est.
{% elsif custom_attribute.${VisitToStart} > 0 %}
Le chemin de terre va vers l'est.
La pelle est ici.
{% else %}
Vous êtes dans une impasse sur un chemin de terre. La route va vers l'est. Au loin, on voit qu'elle finira par se diviser. Les arbres sont ici de très hauts palmiers royaux, espacés les uns des autres à égale distance.
Il y a une pelle ici.
{% endif %}
```
{% endraw %}

### Soustrayez deux attributs personnalisés pour afficher la différence en valeur monétaire {#attribute-monetary-difference}

Ce scénario d’utilisation capture deux attributs personnalisés monétaires, puis calcule et affiche la différence pour permettre aux utilisateurs de savoir combien de temps ils leur restent pour atteindre leur objectif.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
Vous n'avez qu'une différence de ${{ | Arrondi : 0 | number_with_delimiter }} restant à soulever !
{% endif %}
```
{% endraw %}

### Indiquez le prénom d’un utilisateur si son nom complet est stocké dans le first_name champ {#attribute-first-name}

Ce scénario d’utilisation capture le prénom d’un utilisateur (si le prénom et le nom sont stockés dans un champ unique), puis utilise ce prénom pour afficher un message de bienvenue.

{% raw %}
```liquid
{{${first_name} | truncatewords : 1, "" | default : « bonjour »}}
{% assign name = {{${first_name}}} | split: ' ' %}
Bonjour {{name[0]}} (nom), voici un message pour vous !
```

**Explication :** Le filtre `split` (diviser) transforme la chaîne de caractères contenue dans `{{${first_name}}}` en tableau. En utilisant `{{name[0]}}`, nous ne faisons alors référence qu’au premier élément du tableau, qui est le prénom de l’utilisateur. 

{% endraw %}
{% endapi %}

{% api %}

## Événement personnalisé

{% apitags %}
Événement personnalisé
{% endapitags %}

- [Annuler la notification push si un événement personnalisé arrive dans les deux heures qui suivent](#event-abort-push)
- [Envoyer une campagne à chaque fois qu’un utilisateur effectue un événement personnalisé trois fois](#event-three-times)
- [Envoyer un message aux utilisateurs qui n’ont acheté qu’une seule catégorie](#event-purchased-one-category)
- [Suivre combien de fois un événement personnalisé s’est produit au cours du dernier mois](#track)


### Annuler la notification push si un événement personnalisé arrive dans les deux heures qui suivent {#event-abort-push}

Ce cas d’utilisation calcule le temps restant jusqu’à un événement et, selon le temps restant, affiche différents messages personnalisés.

Par exemple, vous souhaiterez peut-être empêcher l'envoi d'une notification push si une propriété d'événement personnalisé passe dans les deux prochaines heures. Cet exemple utilise le scénario d’un panier abandonné pour un billet de train.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate moins de 2 heures") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
N'oubliez pas d'acheter votre billet pour {{event_properties.${toStation}}} dans les 24 prochaines heures
{% else %}
Vous partez toujours en voyage pour {{event_properties.${toStation}}} dans plus de 24 heures ? Réservez maintenant
{% endif %}
```
{% endraw %}

### Envoyer une campagne à chaque fois qu’un utilisateur effectue un événement personnalisé trois fois {#event-three-times}

Ce scénario d’utilisation vérifie si un utilisateur a effectué un événement personnalisé trois fois et, si tel est le cas, affiche un message ou envoie une campagne. 

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message('erreur de calcul de cadence') %}
{% elsif cadence != 0 %}
{% abort_message('ignorer le message') %}
{% endif %}
As-tu oublié quelque chose dans ton panier ?
```
{% endraw %}

{% alert important %} Vous devez disposer d’une propriété de l’événement du nombre d’événements personnalisés ou utiliser un webhook sur votre endpoint Braze. Ceci permet d’incrémenter un attribut personnalisé (`example_event_count`) à chaque fois que l’utilisateur exécute l’événement. Cet exemple utilise une cadence de trois (1, 4, 7, 10, etc.).{% endalert %}

### Envoyer un message aux utilisateurs qui n’ont acheté qu’une seule catégorie {#event-purchased-one-category}

Ce scénario d’utilisation capture une liste des catégories achetées par un utilisateur et, si une seule catégorie d’achat existe, elle affiche un message.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Suivre combien de fois un événement personnalisé s’est produit au cours du dernier mois {#track}

Ce cas d’utilisation calcule le nombre de fois qu’un événement personnalisé a été enregistré entre le premier du mois en cours et le mois précédent. Vous pouvez alors exécuter un appel utilisateurs/suivi pour mettre à jour et enregistrer cette valeur en tant qu’attribut personnalisé. Prenez note du fait que cette campagne devra être exécutée pendant deux mois consécutifs avant que des données mensuelles puissent être utilisées.

{% raw %}
```liquid
{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} Le nom d'événement personnalisé suivant devra être modifié pour l'événement personnalisé cible. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = '"now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}Le nom de l'événement personnalisé faisant l'objet d'un suivi devra être modifié pour l'événement personnalisé cible dans le champ Attribute Name (Nom d'attribut) ci-dessous. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## Langue

{% apitags %}
Langue
{% endapitags %}

- [Afficher les noms des mois dans une langue différente](#language-display-month)
- [Afficher une image selon la langue d’un utilisateur](#language-image-display)
- [Personnaliser la messagerie en fonction du jour de la semaine et de la langue de l’utilisateur](#language-personalize-message)

### Afficher les noms des mois dans une langue différente {#language-display-month}

Ce scénario d’utilisation affiche la date, le mois et l’année en cours, avec le mois dans une langue différente. L’exemple présenté est suédois.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Janvier {{year}}
{% elsif {{month)) == 'February' %}
{{day}} Février {{year}}
{% elsif {{month)) == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month)) == 'April' %}
{{day}} Avril {{year}}
{% elsif {{month)) == 'May' %}
{{day}} Mai {{year}}
{% elsif {{month)) == 'June' %}
{{day}} Juin {{year}}
{% elsif {{month)) == 'July' %}
{{day}} Juillet {{year}}
{% elsif {{month)) == 'August' %}
{{day}} Août {{year}}
{% elsif {{month)) == 'September' %}
{{day}} Septembre {{year}}
{% elsif {{month)) == 'October' %}
{{day}} Octobre {{year}}
{% elsif {{month)) == 'November' %}
{{day}} Novembre {{year}}
{% elsif {{month)) == 'December' %}
{{day}} Décembre {{year}}
{% endif %}
```
{% endraw %}

### Afficher une image selon la langue d’un utilisateur {#language-image-display}

Ce cas d’utilisation affichera une image selon la langue d’un utilisateur. Prenez note du fait que ce cas d’utilisation n’a été testé qu’avec des images chargées dans la bibliothèque média de Braze.

{% raw %}
```liquid
{% if ${language} == 'en' %}
URL de l'image en Anglais (par exemple, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
URL de l'image en Russe
{% elsif ${language} == 'es' %}
URL de l'image en Espagnol
{% else %}
URL de l'image de remplacement
{% endif %}
```
{% endraw %}

### Personnaliser la messagerie en fonction du jour de la semaine et de la langue de l’utilisateur {#language-personalize-message}

Ce scénario d’utilisation vérifie le jour actuel de la semaine et, en fonction du jour, si la langue de l’utilisateur est définie sur l’une des options de langue fournies, il affiche un message spécifique dans sa langue.

L’exemple fourni s’arrête mardi mais peut être répété pour chaque jour de la semaine.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Achetez dès aujourd'hui et faites passer votre apprentissage des langues au niveau supérieur. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
C'est lundi, mais la langue ne correspond pas 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
N'oubliez pas de déverrouiller la version complète de votre langue. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

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

- [Évitez d’envoyer des e-mails aux clients qui ont bloqué des e-mails marketing](#misc-avoid-blocked-emails)
- [Utiliser l’état d’abonnement d’un client pour personnaliser le contenu dans des messages](#misc-personalize-content)
- [Capitaliser la première lettre de chaque mot dans une chaîne de caractères](#misc-capitalize-words-string)
- [Comparer la valeur d’attribut personnalisée à un tableau](#misc-compare-array)
- [Créer un rappel d’événement à venir](#misc-event-reminder)
- [Rechercher une chaîne de caractères dans un tableau](#misc-string-in-array)
- [Rechercher la plus grande valeur dans un tableau](#misc-largest-value)
- [Rechercher la plus petite valeur dans un tableau](#misc-smallest-value)
- [Interroger la fin d’une chaîne de caractères](#misc-query-end-of-string)
- [Valeurs de requête dans un tableau à partir d’un attribut personnalisé avec plusieurs combinaisons](#misc-query-array-values)
- [Formater une chaîne de caractères pour en faire un numéro de téléphone](#phone-number)

### Évitez d’envoyer des e-mails aux clients qui ont bloqué des e-mails marketing {#misc-avoid-blocked-emails}

Ce scénario d’utilisation prend une liste des utilisateurs bloqués enregistrés dans un bloc de contenu et garantit que les utilisateurs bloqués ne sont pas communiqués ou ciblés dans des campagnes ou des canevas à venir.

{% alert important %}
Pour utiliser ce Liquid, enregistrez d’abord la liste des e-mails bloqués dans un bloc de contenu. La liste ne doit pas comporter d’espaces ni de caractères supplémentaires insérés entre les adresses e-mail (par ex., `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message('Le courrier électronique est bloqué') %}
    {% break %}
    {% endif %}
{% endfor %} 
Votre message ici !
```
{% endraw %}

**Explication :** Nous vérifions ici si l’e-mail de votre destinataire potentiel est dans cette liste en faisant référence au bloc de contenu des e-mails bloqués. Si l’e-mail est trouvé, le message ne s’affichera pas.

{% alert note %}
Les blocs de contenu ont une limite de taille de 5 Mo.
{% endalert %}

### Utiliser l’état d’abonnement d’un client pour personnaliser le contenu dans des messages {#misc-personalize-content}

Ce cas d’utilisation utilise l’état d’abonnement d’un client pour envoyer du contenu personnalisé. Les clients abonnés à un groupe d’abonnement spécifique recevront un message exclusif pour les groupes d’abonnement par e-mail.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}}} == 'subscribed' %}
C'est un message exclusif pour les utilisateurs abonnés !
{% else %} Ceci est le message par défaut pour les autres utilisateurs.
{% endif %}
```
{% endraw %}

### Capitaliser la première lettre de chaque mot dans une chaîne de caractères {#misc-capitalize-words-string}

Ce scénario d’utilisation prend une série de mots, les répartit dans un tableau et capitalise la première lettre de chaque mot.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ mots | capitaliser | append : ' ' }}
{% endfor %} 
```
{% endraw %}

**Explication :** Ici, nous avons attribué une variable à notre attribut de chaîne de caractères choisi et utilisé le filtre  `split` pour divise la chaîne de caractères en un tableau. Nous avons ensuite utilisé la balise `for` (pour) pour attribuer la variable `words` (mots) à chacun des éléments de notre nouveau tableau, avant d’afficher ces mots avec le filtre `capitalize` (capitaliser) et le filtre `append` (ajouter) pour ajouter des espaces entre chacun des termes.

### Comparer la valeur d’attribut personnalisée à un tableau {#misc-compare-array}

Ce scénario d’utilisation répertorie les boutiques favorites, vérifie si l’une des boutiques préférées d’un utilisateur figure dans cette liste et, si tel est le cas, affiche une offre spéciale pour ces boutiques.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
L'offre du jour de {{store}}

{% break %}

{% else %}
{% abort_message("Aucun attribut trouvé") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Cette séquence possède une balise `break` (coupure) dans la déclaration conditionnelle principale. La boucle s’arrête alors lorsqu’une correspondance est trouvée. Si vous souhaitez afficher plusieurs ou toutes les correspondances, supprimez la balise `break`. {% endalert %}

### Créer un rappel d’événement à venir {#misc-event-reminder}

Ce scénario d’utilisation permet aux utilisateurs de configurer des rappels à venir en fonction des événements personnalisés. Le scénario exemple permet à un utilisateur de définir un rappel pour une date de renouvellement de police de 26 jours ou plus, dans lequel les rappels sont envoyés 26, 13, 7 ou 2 jours avant la date de renouvellement de la police.

Avec ce cas d’utilisation, le texte suivant devrait être placé dans le corps d’une [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) ou d’une Canvas Step.

{% raw %}
```liquid
{% comment %}
En fonction de la façon dont la propriété reminder_capture est passée à Braze, avec/sans horodatage, le nombre de jours peut avoir un impact si un utilisateur tombe de chaque côté des fenêtres de jours 26/13/7/2.
Une fois que les utilisateurs ont été affectés à un parcours/flux de rappel, ils sont programmés pour entrer un Canvas suivant.
Cet « Écouteur d'événement » peut être utilisé pour répartir les utilisateurs en différents parcours en fonction des propriétés d'événement personnalisées envoyées à Braze.
{% endcomment %}

{% comment %}
Lors du test, assurez-vous que l'ID de campagne, l’endpoint de l'API de campagne, l'ID de Canvas et l’endpoint de l'API de Canvas sont saisis correctement. Dans cet exemple, l'ID de Canvas et l’endpoint de l'API de Canvas ont été configurés pour le partage avec le client. En pratique, cela peut être testé à l'aide d'un ID de campagne et d'un endpoint de l'API de campagne.
{% endcomment %}

{% comment %}
L'étape suivante calcule le nombre de jours entre la date du jour et la date de rappel en tant que « time_to_reminder ».
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
L'étape suivante vérifie si time_to_reminder est à plus de 26 jours. Si c'est le cas, l'utilisateur est programmé pour entrer le Canvas suivant 26 jours avant le reminder_date.
L'heure est convertie de « secondes à partir de 1970 » à la date de rappel appropriée au format ISO 8601 requis.
N.B. Des fuseaux horaires supplémentaires doivent être pris en compte en ajoutant une propriété de planification API supplémentaire de « in_local_time »
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date : « %Y-%m-%d :%H:%M » }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
« Destinataires » : [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date : « %Y-%m-%dT%H:%M:%S+0000 »}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
« temps » : « {{ time_to_first_message | date : « %Y-%m-%dT%H:%M:%S+0000 » }}"
}
}

{% comment %}
L'étape suivante vérifie si time_to_reminder est à moins de 26 jours, mais à plus de 13 jours.
Les usagers doivent entrer dans le parcours le 13e jour.
{% endcomment %}

{% elsif 1123200 < {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
« Destinataires » : [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date : « %Y-%m-%dT%H:%M:%S+0000 »}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
« temps » : »2021-03-24T20:04:00+0000"
}
}

{% comment %}
L'étape suivante vérifie si time_to_reminder est à moins de 13 jours, mais à plus de 7 jours.
Les usagers doivent entrer dans le parcours le 7e jour.
{% endcomment %}

{% elsif 604800 < {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
« Destinataires » : [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date : « %Y-%m-%dT%H:%M:%S+0000 »}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
« temps » : « {{ time_to_first_message | date : « %Y-%m-%dT%H:%M:%S+0000 » }}"
}
}

{% comment %}
L'étape suivante vérifie si time_to_reminder est à moins de 7 jours, mais à plus de 2 jours.
Les usagers doivent entrer dans le parcours le 2e jour.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
« Destinataires » : [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date : « %Y-%m-%dT%H:%M:%S+0000 »}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
« temps » : « {{ time_to_first_message | date : « %Y-%m-%dT%H:%M:%S+0000 » }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %} 

Vous aurez besoin d’un événement personnalisé `reminder_capture` et les propriétés d’événement personnalisées doivent inclure au moins :

- `reminder-id` (id-rappel) : Identificateur de l’événement personnalisé
- `reminder_date` : Date d'échéance du rappel soumise par l'utilisateur
- `message_personalisation_X` : Toutes les propriétés nécessaires pour personnaliser le message au moment de l’envoi

{% endalert %}

### Rechercher une chaîne de caractères dans un tableau {#misc-string-in-array}

Ce scénario d’utilisation vérifie si une matrice d’attributs personnalisée contient une chaîne de caractères spécifique et, si elle existe, affiche un message spécifique.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Liez votre compte Hertz pour utiliser Hertz Fast Lane.

{% elsif custom_attribute.${airportCompleted} == false %}
Clear vous aide à traverser la sécurité de l'aéroport. Effectuez votre installation en personne la prochaine fois que vous serez à l'aéroport. Comptez 5 minutes de trajet.

{% else %}
Votre compte est entièrement configuré
{% endif %}
```
{% endraw %}

### Rechercher la plus grande valeur dans un tableau {#misc-largest-value}

Ce scénario d’utilisation calcule la valeur la plus élevée dans un tableau d’attributs personnalisée donnée à utiliser dans l’envoi de messages de l’utilisateur.

Par exemple, vous pouvez présenter le score le plus élevé actuel ou l’enchère la plus élevée d’un article à un utilisateur

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Vous devez utiliser un attribut personnalisé qui a une valeur entière et fait partie d’un tableau (liste). {% endalert %}

### Rechercher la plus petite valeur dans un tableau {#misc-smallest-value}

Ce scénario d’utilisation calcule la valeur la plus faible dans un tableau d’attributs personnalisée donnée à utiliser dans l’envoi de messages de l’utilisateur.

Par exemple, vous pouvez présenter le score le plus bas ou l’article le moins cher à un utilisateur.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Vous devez utiliser un attribut personnalisé qui a une valeur entière et fait partie d’un tableau (liste). {% endalert %}

### Interroger la fin d’une chaîne de caractères {#misc-query-end-of-string}

Ce scénario d’utilisation interroge la fin d’une chaîne de caractères à utiliser dans l’envoi de messages.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Votre dernière recherche sur le marché était sur {{custom_attribute.${Dernier intérêt de l'acheteur sur le marché} | date : « %d.%m.%Y »}}. Découvrez toutes nos nouvelles offres.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Valeurs de requête dans un tableau à partir d’un attribut personnalisé avec plusieurs combinaisons {#misc-query-array-values}

Ce scénario d’utilisation prend une liste de soon-to-be-expired spectacles, vérifie si l’un des spectacles favoris d’un utilisateur figure dans cette liste et, si tel est le cas, affiche un message informant l’utilisateur qu’il ne sera bientôt plus à l’affiche.

{% raw %} 
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

Tous les épisodes de {{new_shows_clean | join : « , » }} expirent le 9/8 - regardez-les maintenant avant qu'ils ne soit trop tard !

{% else %}
{% abort_message("Introuvable") %}
{% endif %}
```
{% endraw %}

{% alert important %} Vous devrez d’abord trouver des correspondances entre les baies, puis créer une logique à la fin pour fractionner les correspondances. {% endalert %}

### Formater une chaîne de caractères pour en faire un numéro de téléphone {#phone-number}

Ce cas d’utilisation vous montrera comment indexer le champ de profil utilisateur `phone_number` (par défaut formaté en tant que chaîne de caractères d’entiers) et le reformater selon vos normes locales de numéros de téléphone. Par exemple, 1234567890 vers (123)-456-7890.

{% raw %} 
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Ciblage de la plateforme

{% apitags %}
Ciblage de la plateforme
{% endapitags %}

- [Différencier les copies par OS d’appareil](#platform-device-os)
- [Cibler uniquement une plate-forme spécifique](#platform-target)
- [Cibler uniquement les périphériques iOS avec une version d’OS spécifique](#platform-target-ios-version)
- [Cibler uniquement les navigateurs Web](#platform-target-web)
- [Cibler un opérateur mobile spécifique](#platform-target-carrier)

### Différencier les copies par OS d’appareil {#platform-device-os}

Ce scénario d’utilisation vérifie la plate-forme sur laquelle un utilisateur est connecté et, en fonction de sa plateforme, affiche des envois de messages spécifiques.

Par exemple, vous pouvez montrer aux utilisateurs mobiles les versions plus courtes du texte du message tout en affichant aux autres utilisateurs la version classique et plus longue du texte. Vous pouvez également montrer aux utilisateurs mobiles certains envois de messages pertinents pour eux, mais qui ne seraient pas pertinents pour les utilisateurs Web. Par exemple, iOS l’envoi de messages peut parler d’Apple Pay, mais les messages Android doivent mentionner Google Pay.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
Il s’agit d’une version abrégée.

{% else %}
Il s’agit de la version normale et elle est plus longue que la version abrégée. 
{% endif %}
```
{% endraw %}

{% alert note %} 
Liquid est sensible à la casse, `targeted_device.${platform}` renvoie la valeur dans toutes les minuscules. 
{% endalert %}

### Cibler uniquement une plate-forme spécifique {#platform-target}

Ce scénario d’utilisation capture la plate-forme de l’appareil des utilisateurs et, en fonction de la plateforme, affiche un message.

Par exemple, vous pouvez envoyer un message uniquement aux utilisateurs Android. Cette option peut être utilisée comme alternative à la sélection d’une application dans l’outil Segmentation.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

Ce message est destiné à un utilisateur Android ! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Cibler uniquement les périphériques avec une version d’OS spécifique {#platform-target-ios-version}

Ce scénario d’utilisation vérifie si la version OS d’un utilisateur appartient à un certain ensemble de versions et, si tel est le cas, affiche un message spécifique.

L’exemple utilisé envoie un avertissement aux utilisateurs sur une version d’OS 10.0 ou antérieure signalant qu’ils vont rendre obsolète la prise en charge du système d’exploitation de l’appareil de l’utilisateur.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == “10.0.3” or {{targeted_device.${os}}} == “10.1” or {{targeted_device.${os}}} == “10.2” or {{targeted_device.${os}}} == “10.2.1” or {{targeted_device.${os}}} == “10.3” or {{targeted_device.${os}}} == “10.3.1” or {{targeted_device.${os}}} == “10.3.2” or {{targeted_device.${os}}} == “10.3.3” or {{targeted_device.${os}}} == “10.3.4” or {{targeted_device.${os}}} == “9.3.1” or {{targeted_device.${os}}} == “9.3.2” or {{targeted_device.${os}}} == “9.3.3” or {{targeted_device.${os}}} == “9.3.4” or {{targeted_device.${os}}} == "9.3.5" %}

Nous arrêtons progressivement L’assistance dédiée au système d’exploitation de votre périphérique. Assurez-vous de le mettre à jour vers la version la plus récente pour profiter de la meilleure expérience sur l'application possible.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler uniquement les navigateurs Web {#platform-target-web}

Ce scénario d’utilisation vérifie si l’appareil cible d’un utilisateur fonctionne sur Mac ou Windows et, le cas échéant, affiche un message spécifique.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' OR {{targeted_device.${os}}} == 'Windows' %}

Ce message s’affichera dans le navigateur Web de votre ordinateur de bureau.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

Le cas d’usage suivant vérifie si un utilisateur Web est sur iOS ou Android et, si oui, affichera un message particulier.

{% raw %}
```liquid
{% if {{targeted_device.${os} == 'Android'}} and {{targeted_device.${platform} == 'web'}} %}

Contenu pour Android

{% elsif {{targeted_device.${os} == 'iOS'}} and {{targeted_device.${platform} == 'web'}} %}

Contenu pour iOS

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler un opérateur mobile spécifique {#platform-target-carrier}

Ce scénario d’utilisation vérifie si le fournisseur d’accès d’un appareil d’un utilisateur est Verizon et, si tel est le cas, affiche un message spécifique.

Pour les notifications push et les canaux de message in-app, vous pouvez spécifier le support de l’appareil dans votre corps de message en utilisant Liquid. Si le fournisseur d’accès de l’appareil du destinataire ne correspond pas, le message ne sera pas envoyé.

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

Ce message est destiné aux utilisateurs Verizon !

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Fuseau horaire

{% apitags %}
Fuseau horaire
{% endapitags %}

- [Personnaliser un message selon le fuseau horaire d’un utilisateur](#personalize-timezone)
- [Ajouter le fuseau horaire CST à un attribut personnalisé](#time-append-cst)
- [Insérer un horodatage](#time-insert-timestamp)
- [Envoyer une notification push de Canvas uniquement pendant une période de temps dans le fuseau horaire local d’un utilisateur](#time-canvas-window)
- [Envoyer une campagne de messages dans l’application récurrente entre une fenêtre de temps dans la zone horaire locale d’un utilisateur](#time-reocurring-iam-window)
- [Envoyer différents messages en semaine par rapport aux week-ends dans le fuseau horaire local d’un utilisateur](#time-weekdays-vs-weekends)
- [Envoyer des messages différents en fonction de l’heure de la journée dans le fuseau horaire local d’un utilisateur](#time-of-day)

### Personnaliser un message selon le fuseau horaire d’un utilisateur {#personalize-timezone}

Ce cas d’utilisation affiche des messages différents selon le fuseau horaire de l’utilisateur.

{% raw %}
```liquid
{% if {{${time_zone}}} == ‘xx’ %}
Message pour le fuseau horaire xx.
{% elsif {{$time_zone}}} == ‘yy’ %}
Message pour le fuseau horaire yy.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Ajouter le fuseau horaire CST à un attribut personnalisé {#time-append-cst}

Ce scénario d’utilisation affiche un attribut de date personnalisée dans un fuseau horaire donné.

Option 1 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone : -0005 | date : « %B, %d %Y » }}
```
{% endraw %}

Option 2 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone : « Amérique/Chicago » | date : « %B %d %Y %z » }}
```
{% endraw %}

### Insérer un horodatage {#time-insert-timestamp}

Ce scénario d’utilisation affiche un message qui inclut un horodatage dans le fuseau horaire actuel de l’utilisateur.

L’exemple suivant indique la date AAAA-mm-jj HH : MM : SS, comme 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default : « Vous »}} avez reçu une campagne, rendue à ({{ "maintenant » | timezone : ${time_zone} | date : « %Y-%m-%d %H:%M:%S » }})
```
{% endraw %}

### Envoyer une notification push de Canvas uniquement pendant une période de temps dans le fuseau horaire local d’un utilisateur {#time-canvas-window}

Ce scénario d’utilisation vérifie l’heure d’un utilisateur dans son fuseau horaire local et, s’il correspond à un horaire défini, il affiche un message spécifique.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("En dehors de la fenêtre de temps autorisée") %}
{% endif %}

Voici un message qui sera envoyé entre 8 h et 20 h !
```
{% endraw %}

### Envoyer une campagne de messages dans l’application récurrente entre une fenêtre de temps dans la zone horaire locale d’un utilisateur {#time-reoccurring-iam-window}

Ce scénario d’utilisation affiche un message si l’heure actuelle d’un utilisateur se trouve dans une fenêtre définie.

Par exemple, le scénario suivant permet à un utilisateur de savoir qu’une boutique est fermée.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Le magasin est fermé. Revenez entre 11 h et 21 h !

{% else %} 
{% abort_message("non envoyé car le magasin est ouvert") %}
{% endif %}
```
{% endraw %}

### Envoyer différents messages en semaine par rapport aux week-ends dans le fuseau horaire local d’un utilisateur {#time-weekdays-vs-weekends}

Ce scénario d’utilisation vérifie si le jour actuel de la semaine d’un utilisateur est un samedi ou un dimanche et, en fonction de la journée, affiche différents messages.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
C’est {{today}}, et si vous ouvriez l’appli pour vos transactions ?

{% else %}
C’est {{today}},  et si vous visitiez le magasin ?
{% endif %}
```
{% endraw %}

### Envoyer des messages différents en fonction de l’heure de la journée dans le fuseau horaire local d’un utilisateur {#time-of-day}

Ce scénario d’utilisation affiche un message si l’heure actuelle d’un utilisateur se trouve dans une fenêtre définie.

Par exemple, vous pourriez souhaiter indiquer à un utilisateur une opportunité sensible au temps qui dépend de l’heure de la journée.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("En dehors de la fenêtre de temps autorisée") %}
{% endif %}

Essayez ce nouveau bar après le travail aujourd’hui. Offres spéciales HH !
```
{% endraw %}

{% alert note %} C’est le contraire des [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns). {% endalert %}

{% endapi %}

{% api %}

## Semaine/Jour/Mois

{% apitags %}
Semaine/Jour/Mois
{% endapitags %}

- [Tirer le nom du mois précédent dans un message](#month-name)
- [Envoyer une campagne à la fin de chaque mois](#month-end)
- [Envoyer une campagne le dernier jour du mois](#day-of-month-last)
- [Envoyer un message différent chaque jour du mois](#day-of-month)
- [Envoyer un message différent chaque jour de la semaine](#day-of-week)

### Tirer le nom du mois précédent dans un message {#month-name}

Ce scénario d’utilisation prend le mois en cours et affiche le mois précédent à utiliser dans les envois de messages.

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

Voici un aperçu de vos dépenses dans {{month}}.
```
{% endraw %}

### Envoyer une campagne à la fin de chaque mois {#month-end}

Ce scénario d’utilisation vérifier si la date actuelle tombe dans une liste de dates et, en fonction de la date, affiche un message spécifique.

{% alert note %} Cela ne tient pas compte des années bissextiles (29 février). {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

La date est correcte

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Envoyer une campagne le dernier jour du mois {#day-of-month-last}

Ce scénario d’utilisation capture le mois et le jour en cours et calcule si le jour actuel tombe le dernier jour de la semaine du mois.

Par exemple, vous pouvez envoyer une enquête à vos utilisateurs le dernier mercredi du mois, demandant des commentaires sur les produits.

{% raw %}
```liquid
{% comment %}Extrayez le jour, le nom du jour, le mois et l'année à partir de la date du jour.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Affectez le nombre correct de jours pour le mois en cours.{% endcomment %}

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

{% comment %}Affectez le nombre correct de jours si le mois en cours est février, en tenant compte des années bissextiles.{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Vérifiez que la date du jour est comprise dans la semaine qui suit le dernier jour du mois. Dans le cas contraire, ignorez le message. Si c'est le cas, vérifiez que nous sommes mercredi. Dans le cas contraire, ignorez le message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%}
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

Ce scénario d’utilisation vérifie si la date actuelle correspond à celle d’une liste et, en fonction du jour, affiche un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message pour 2019-12-01

{% elsif today == day_2 %}
Message pour 2019-12-02

{% elsif today == day_3%}
Message pour 2019-12-03

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Envoyer un message différent chaque jour de la semaine {#day-of-week}

Ce scénario d’utilisation vérifie le jour de la semaine et, en fonction du jour, affiche un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case ‘today' %}
{% when 'Monday' %}
La version du lundi

{% when 'Tuesday' %}
La version du mardi

{% when 'Wednesday' %}
La version du mercredi

{% when  'Thursday' %}
La version du jeudi

{% when  'Friday' %}
La version du vendredi

{% when 'Saturday' %}
La version du samedi

{% when 'Sunday' %}
La version du dimanche

{% else %}
La version par défaut
{% endcase %}
```
{% endraw %}

{% alert note %} Vous pouvez remplacer la ligne « copier par défaut » par {% raw %}`{% abort_message() %}`{% endraw %} pour empêcher le message d’être envoyé si le jour de la semaine est inconnu. {% endalert %}

{% endapi %}
