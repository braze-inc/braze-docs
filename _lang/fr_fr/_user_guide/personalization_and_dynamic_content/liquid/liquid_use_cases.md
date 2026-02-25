---
nav_title: Bibliothèque de scénarios d'utilisation de Liquid
article_title: Bibliothèque de scénarios d'utilisation de Liquid
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Cette page d'accueil est une présentation des scénarios d'utilisation de Liquid organisés par catégorie, tels que les anniversaires, l'utilisation d'applications, les comptes à rebours, etc."

---

{% api %}

## Anniversaires et fêtes

{% apitags %}
Anniversaires et fêtes
{% endapitags %}

- [Personnaliser les messages en fonction de l'année d'anniversaire de l'utilisateur](#anniversary-year)
- [Personnaliser les messages en fonction de la semaine d'anniversaire de l'utilisateur](#birthday-week)
- [Envoyer des campagnes aux utilisateurs pendant leur mois d'anniversaire](#birthday-month)
- [Éviter d'envoyer des messages les jours fériés](#holiday-avoid)

### Personnaliser les messages en fonction de l'année d'anniversaire d'un utilisateur {#anniversary-year}

Ce scénario d'utilisation montre comment calculer l'anniversaire d'utilisation d'une application d'un utilisateur en fonction de sa date d'inscription initiale et afficher différents messages en fonction du nombre d'années célébrées.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %} 
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %} 
{% if this_day == anniversary_day %} 
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %} 
{% abort_message("Not same day") %} 
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous utilisons la variable réservée `now` pour insérer la date et l'heure actuelles au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). Les filtres `%B` (mois comme « mai ») et `%d` (jour comme « 18 ») formatent le mois et le jour actuels. Nous utilisons ensuite les mêmes filtres de date et d'heure sur les valeurs `signup_date` pour nous assurer de pouvoir comparer les deux valeurs à l'aide de balises conditionnelles et de logique.

Ensuite, nous répétons trois autres instructions de variables pour obtenir `%B` et `%d` pour la `signup_date`, en ajoutant également `%Y` (année comme « 2021 »). Cela réduit la date et l'heure de la `signup_date` à l'année uniquement. Connaître le jour et le mois nous permet de vérifier si l'anniversaire de l'utilisateur est aujourd'hui, et connaître l'année nous indique combien d'années se sont écoulées, ce qui nous permet de savoir pour combien d'années le féliciter !

{% alert tip %} Vous pouvez créer autant de conditions que d'années au cours desquelles vous avez collecté des dates d'inscription. {% endalert %}  

### Personnaliser les messages en fonction de la semaine d'anniversaire d'un utilisateur {#birthday-week}

Ce scénario d'utilisation montre comment trouver l'anniversaire d'un utilisateur, le comparer à la date actuelle, puis afficher des messages d'anniversaire spéciaux avant, pendant et après la semaine d'anniversaire.

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
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**Explication :** Comme dans le cas de l'[année d'anniversaire](#anniversary-year), nous prenons ici la variable réservée `now` et utilisons le filtre `%W` (semaine, par exemple la semaine 12 sur les 52 de l'année) pour obtenir le numéro de la semaine de l'année dans laquelle tombe l'anniversaire de l'utilisateur. Si la semaine d'anniversaire de l'utilisateur correspond à la semaine en cours, nous lui envoyons un message de félicitations ! 

Nous incluons également des instructions pour `last_week` et `next_week` afin de personnaliser davantage votre envoi de messages.

### Envoyer des campagnes aux utilisateurs pendant leur mois d'anniversaire {#birthday-month}

Ce scénario d'utilisation montre comment calculer le mois d'anniversaire d'un utilisateur, vérifier si son anniversaire tombe pendant le mois en cours et, si tel est le cas, envoyer un message spécial.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body 
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**Explication :** Similaire au cas d'utilisation de la [semaine d'anniversaire](#birthday-week), sauf qu'ici nous utilisons le filtre `%B` (mois comme « mai ») pour calculer quels utilisateurs ont un anniversaire ce mois-ci. Une application potentielle pourrait consister à s'adresser aux utilisateurs ayant un anniversaire dans un e-mail mensuel.

### Éviter d'envoyer des messages lors des fêtes principales {#holiday-avoid}

Ce scénario d'utilisation montre comment envoyer des messages pendant la période des fêtes tout en évitant les jours fériés principaux, lorsque l'engagement est susceptible d'être faible.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous assignons le terme `today` à la variable réservée `now` (la date et l'heure actuelles), en utilisant les filtres `%Y` (année comme « 2023 »), `%m` (mois comme « 12 ») et `%d` (jour comme « 25 ») pour formater la date. Nous exécutons ensuite notre instruction conditionnelle pour dire que si la variable `today` correspond aux jours fériés de votre choix, le message sera abandonné. 

L'exemple présenté correspond à la veille de Noël, au jour de Noël et au lendemain de Noël.

{% endapi %}

{% api %}

## Utilisation de l'application

{% apitags %}
Utilisation de l'application
{% endapitags %}

- [Envoyer des messages dans la langue de l'utilisateur s'il a ouvert une session](#app-session-language)
- [Personnaliser les messages en fonction de la date à laquelle l'utilisateur a ouvert l'application pour la dernière fois](#app-last-opened)
- [Afficher un message différent si la dernière utilisation de l'application remonte à moins de trois jours](#app-last-opened-less-than)

### Envoyer des messages dans la langue d'un utilisateur s'il ne s'est pas connecté à une session {#app-session-language}

Ce scénario d'utilisation vérifie si un utilisateur s'est connecté à une session et, si ce n'est pas le cas, inclut une logique d'affichage d'un message basée sur la langue collectée manuellement via un attribut personnalisé, le cas échéant. S'il n'y a pas d'informations de langue liées au compte, le message s'affiche dans la langue par défaut. Si un utilisateur s'est connecté à une session, toutes les informations de langue liées à l'utilisateur sont extraites et le message approprié est affiché. 

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Explication :** Ici, nous utilisons deux instructions `if` regroupées et imbriquées. La première instruction `if` vérifie si l'utilisateur a démarré une session en vérifiant si `last_used_app_date` est `nil`. En effet, `{{${language}}}` est automatiquement collecté par le SDK lorsqu'un utilisateur se connecte à une session. Si l'utilisateur ne s'est pas connecté à une session, nous n'avons pas encore sa langue, donc cette vérification porte sur les attributs personnalisés liés à la langue qui ont été enregistrés et, sur la base de ces informations, affiche un message dans cette langue, si possible.
{% endraw %}

La seconde instruction `if` vérifie simplement l'attribut standard (par défaut), car l'utilisateur n'a pas `nil` pour `last_used_app_date`, ce qui signifie qu'il s'est connecté à une session et que nous avons sa langue.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) est une variable réservée qui est renvoyée lorsque le code Liquid ne donne aucun résultat. `Nil` est traité comme `false` dans un bloc `if`.
{% endalert %}

### Personnaliser les messages en fonction du moment où un utilisateur a ouvert l'application pour la dernière fois {#app-last-opened}

Ce scénario d'utilisation calcule la dernière ouverture de l'application par l'utilisateur et affiche un message personnalisé différent selon la durée écoulée.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Afficher un message différent si un utilisateur a utilisé l'application il y a moins de trois jours {#app-last-opened-less-than}

Ce cas d'utilisation calcule depuis combien de temps un utilisateur a utilisé votre application et, en fonction de la durée, affiche un message personnalisé différent.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Comptes à rebours

{% apitags %}
Comptes à rebours
{% endapitags %}

- [Ajouter X jours à la date du jour](#countdown-add-x-days)
- [Calculer un compte à rebours à partir d'un point donné dans le temps](#countdown-difference-days)
- [Créer un compte à rebours pour des dates et priorités d'expédition spécifiques](#countdown-shipping-options)
- [Créer un compte à rebours en jours](#countdown-days)
- [Créer un compte à rebours de jours en heures en minutes](#countdown-dynamic)
- [Afficher le nombre de jours restants jusqu'à une certaine date](#countdown-future-date)
- [Afficher le nombre de jours restants avant l'arrivée d'un attribut de date personnalisé](#countdown-custom-date-attribute)
- [Afficher le temps restant et interrompre le message s'il ne reste que X temps](#countdown-abort-window)
- [Message in-app à envoyer X jours avant la fin de l'abonnement de l'utilisateur](#countdown-membership-expiry)
- [Personnaliser les messages in-app en fonction de la date et de la langue de l'utilisateur](#countdown-personalize-language)
- [Insérer la date dans 30 jours, formatée en mois et jour](#countdown-template-date)

### Ajouter X jours à la date du jour {#countdown-add-x-days}

Ce scénario d'utilisation ajoute un nombre spécifique de jours à la date actuelle pour les référencer et les ajouter dans les messages. Par exemple, vous pouvez envoyer en milieu de semaine un message indiquant les événements prévus dans la région pour le week-end.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

La valeur `plus` sera toujours en secondes, c'est pourquoi nous terminons par le filtre `%F` pour convertir les secondes en jours.

{% alert important %}
Vous pouvez inclure une URL ou un lien profond vers une liste d'événements dans votre message afin de diriger l'utilisateur vers une liste d'activités à venir.
{% endalert %}

### Calculer un compte à rebours à partir d'un point donné dans le temps {#countdown-difference-days}

Ce scénario d'utilisation calcule la différence en jours entre une date spécifique et la date actuelle. Cette différence peut servir à afficher un compte à rebours à vos utilisateurs.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Créer un compte à rebours pour des dates et priorités d'expédition spécifiques {#countdown-shipping-options}

Ce scénario d'utilisation capture différentes options d'expédition, calcule la durée nécessaire à la réception et affiche des messages encourageant les utilisateurs à acheter à temps pour recevoir leur colis à une date donnée.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### Créer un compte à rebours en jours {#countdown-days}

Ce scénario d'utilisation calcule le temps restant entre un événement spécifique et la date actuelle et affiche le nombre de jours restants jusqu'à l'événement.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
Vous aurez besoin d'un champ d'attribut personnalisé avec une valeur `date`.
{% endalert %}

### Créer un compte à rebours de jours en heures en minutes {#countdown-dynamic}

Ce scénario d'utilisation calcule le temps restant entre un événement spécifique et la date actuelle. En fonction du temps restant jusqu'à l'événement, il modifie la valeur de temps (jours, heures, minutes) pour afficher différents messages personnalisés.

Par exemple, s'il reste deux jours avant l'arrivée de la commande d'un client, vous pourriez dire : « Votre commande arrivera dans 2 jours ». En revanche, s'il reste moins d'un jour, vous pourriez indiquer plutôt « Votre commande arrivera dans 17 heures ».

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
Vous aurez besoin d'un champ d'attribut personnalisé avec une valeur `date`. Vous devrez également définir des seuils de temps pour déterminer quand afficher le temps en jours, heures et minutes.
{% endalert %}

### Afficher le nombre de jours restants jusqu'à une certaine date {#countdown-future-date}

Ce scénario d'utilisation calcule la différence entre la date actuelle et une date d'événement future et affiche un message indiquant le nombre de jours restants jusqu'à l'événement.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Afficher le nombre de jours restants avant l'arrivée d'un attribut de date personnalisé {#countdown-custom-date-attribute}

Ce scénario d'utilisation calcule la différence en jours entre les dates actuelle et future et affiche un message si la différence correspond à un nombre défini.

Dans cet exemple, un utilisateur recevra un message deux jours avant l'attribut de date personnalisé. Sinon, le message ne sera pas envoyé.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Afficher le temps restant et interrompre le message s'il ne reste que X temps {#countdown-abort-window}

Ce cas d'utilisation calcule la durée restante jusqu'à une certaine date et, en fonction de cette durée (en ignorant l'envoi si la date est trop proche), affiche différents messages personnalisés. 

Par exemple, « Il vous reste x heures pour acheter votre billet pour Londres », mais le message n'est pas envoyé s'il reste moins de deux heures avant l'heure de vol pour Londres.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} Vous aurez besoin d'une propriété d'événement personnalisé. {% endalert %}

### Message in-app à envoyer X jours avant la fin de l'abonnement de l'utilisateur {#countdown-membership-expiry}

Ce scénario d'utilisation capture la date d'expiration de votre abonnement, calcule la durée restante avant l'expiration et affiche différents messages en fonction du délai restant.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### Personnaliser les messages in-app en fonction de la date et de la langue de l'utilisateur {#countdown-personalize-language}

Ce scénario d'utilisation calcule un compte à rebours jusqu'à un événement et, en fonction du paramètre de langue de l'utilisateur, affiche le compte à rebours dans sa langue.

Par exemple, vous pouvez envoyer une série de messages incitatifs aux utilisateurs une fois par mois pour leur indiquer combien de temps une offre reste valide, avec quatre messages in-app :

- Initial
- 2 jours restants
- 1 jour restant
- Dernier jour

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

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
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
Vous devrez attribuer une valeur `date` et inclure une logique d'abandon si la date donnée tombe en dehors de la plage de dates. Pour les calculs de jour exacts, la date de fin attribuée doit inclure 23:59:59.
{% endalert %}

### Insérer la date dans 30 jours, formatée en mois et jour {#countdown-template-date}

Ce scénario d'utilisation affiche la date dans 30 jours à utiliser dans les envois de messages.

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

- [Personnaliser un message en fonction d'attributs personnalisés correspondants](#attribute-matching)
- [Soustraire deux attributs personnalisés pour afficher la différence sous forme de valeur monétaire](#attribute-monetary-difference)
- [Référencer le prénom d'un utilisateur si son nom complet est stocké dans le champ first_name](#attribute-first-name)

### Personnaliser un message en fonction d'attributs personnalisés correspondants {#attribute-matching}

Ce scénario d'utilisation vérifie si un utilisateur possède des attributs personnalisés spécifiques et, le cas échéant, affiche différents messages personnalisés. 

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### Soustraire deux attributs personnalisés pour afficher la différence sous forme de valeur monétaire {#attribute-monetary-difference}

Ce scénario d'utilisation capture deux attributs personnalisés monétaires, puis calcule et affiche la différence pour indiquer aux utilisateurs combien il leur reste pour atteindre leur objectif.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Référencer le prénom d'un utilisateur si son nom complet est stocké dans le champ first_name {#attribute-first-name}

Ce scénario d'utilisation capture le prénom d'un utilisateur (si le prénom et le nom sont stockés dans un champ unique), puis utilise ce prénom pour afficher un message de bienvenue.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explication :** Le filtre `split` transforme la chaîne de caractères contenue dans `{{${first_name}}}` en tableau. En utilisant `{{name[0]}}`, nous ne faisons référence qu'au premier élément du tableau, qui est le prénom de l'utilisateur. 

{% endraw %}
{% endapi %}

{% api %}

## Événement personnalisé

{% apitags %}
Événement personnalisé
{% endapitags %}

- [Annuler la notification push si un événement personnalisé a lieu dans les deux heures qui suivent](#event-abort-push)
- [Envoyer une campagne chaque fois qu'un utilisateur effectue un événement personnalisé trois fois](#event-three-times)
- [Envoyer un message aux utilisateurs qui n'ont acheté que dans une seule catégorie](#event-purchased-one-category)
- [Suivre le nombre de fois qu'un événement personnalisé s'est produit au cours du dernier mois](#track)


### Annuler la notification push si un événement personnalisé a lieu dans les deux heures qui suivent {#event-abort-push}

Ce cas d'utilisation calcule le temps restant jusqu'à un événement et, selon le temps restant, affiche différents messages personnalisés.

Par exemple, vous souhaiterez peut-être empêcher l'envoi d'une notification push si une propriété d'événement personnalisé arrive dans les deux prochaines heures. Cet exemple utilise le scénario d'un panier abandonné pour un billet de train.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### Envoyer une campagne chaque fois qu'un utilisateur effectue un événement personnalisé trois fois {#event-three-times}

Ce scénario d'utilisation vérifie si un utilisateur a effectué un événement personnalisé trois fois et, si tel est le cas, affiche un message ou envoie une campagne. 

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} Vous devez disposer d'une propriété d'événement du nombre d'événements personnalisés ou utiliser un webhook vers votre endpoint Braze. Ceci permet d'incrémenter un attribut personnalisé (`example_event_count`) à chaque fois que l'utilisateur effectue l'événement. Cet exemple utilise une cadence de trois (1, 4, 7, 10, etc.). Pour démarrer la cadence à partir de zéro (0, 3, 6, 9, etc.), supprimez `minus: 1`.
{% endalert %}

### Envoyer un message aux utilisateurs qui n'ont acheté que dans une seule catégorie {#event-purchased-one-category}

Ce scénario d'utilisation capture la liste des catégories dans lesquelles un utilisateur a acheté et, si une seule catégorie d'achat existe, affiche un message.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### Suivre le nombre de fois qu'un événement personnalisé s'est produit au cours du dernier mois {#track}

Ce cas d'utilisation calcule le nombre de fois qu'un événement personnalisé a été enregistré entre le premier du mois en cours et le mois précédent. Vous pouvez ensuite exécuter un appel users/track pour mettre à jour et enregistrer cette valeur en tant qu'attribut personnalisé. Notez que cette campagne devra être exécutée pendant deux mois consécutifs avant que les données mensuelles puissent être utilisées.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
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

- [Afficher les noms de mois dans une autre langue](#language-display-month)
- [Afficher une image en fonction de la langue de l'utilisateur](#language-image-display)
- [Personnaliser les messages en fonction du jour de la semaine et de la langue de l'utilisateur](#language-personalize-message)

### Afficher les noms de mois dans une langue différente {#language-display-month}

Ce scénario d'utilisation affiche la date, le mois et l'année en cours, avec le mois dans une langue différente. L'exemple présenté utilise le suédois.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Afficher une image en fonction de la langue d'un utilisateur {#language-image-display}

Ce cas d'utilisation affiche une image en fonction de la langue d'un utilisateur. Notez que ce cas d'utilisation n'a été testé qu'avec des images téléchargées dans la bibliothèque multimédia de Braze.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### Personnaliser l'envoi de messages en fonction du jour de la semaine et de la langue de l'utilisateur {#language-personalize-message}

Ce scénario d'utilisation vérifie le jour actuel de la semaine et, en fonction du jour, si la langue de l'utilisateur correspond à l'une des options de langue fournies, affiche un message spécifique dans sa langue.

L'exemple fourni s'arrête au mardi mais peut être répété pour chaque jour de la semaine.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
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

- [Éviter d'envoyer des e-mails aux clients qui ont bloqué les e-mails marketing](#misc-avoid-blocked-emails)
- [Utiliser l'état d'abonnement d'un client pour personnaliser le contenu des messages](#misc-personalize-content)
- [Mettre en majuscule la première lettre de chaque mot d'une chaîne de caractères](#misc-capitalize-words-string)
- [Comparer la valeur d'un attribut personnalisé à un tableau](#misc-compare-array)
- [Créer un rappel d'événement à venir](#misc-event-reminder)
- [Rechercher une chaîne de caractères dans un tableau](#misc-string-in-array)
- [Trouver la plus grande valeur d'un tableau](#misc-largest-value)
- [Trouver la plus petite valeur d'un tableau](#misc-smallest-value)
- [Interroger la fin d'une chaîne de caractères](#misc-query-end-of-string)
- [Interroger les valeurs d'un tableau à partir d'un attribut personnalisé avec plusieurs combinaisons](#misc-query-array-values)
- [Formater une chaîne de caractères en numéro de téléphone](#phone-number)

### Éviter d'envoyer des e-mails aux clients qui ont bloqué les e-mails marketing {#misc-avoid-blocked-emails}

Ce cas d'utilisation prend une liste d'utilisateurs bloqués enregistrée dans un bloc de contenu et vérifie que ces utilisateurs bloqués ne sont pas contactés ou ciblés dans les prochaines campagnes ou Canvas.

{% alert important %}
Pour utiliser ce Liquid, enregistrez d'abord la liste des e-mails bloqués dans un bloc de contenu. La liste ne doit pas comporter d'espaces ou de caractères supplémentaires entre les adresses e-mail (par exemple, `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %} 
Your message here!
```
{% endraw %}

**Explication :** Nous vérifions ici si l'e-mail de votre destinataire potentiel figure dans cette liste en faisant référence au bloc de contenu des e-mails bloqués. Si l'e-mail est trouvé, le message ne sera pas envoyé.

{% alert note %}
Les blocs de contenu ont une limite de taille de 5 Mo.
{% endalert %}

### Utiliser l'état d'abonnement d'un client pour personnaliser le contenu des messages {#misc-personalize-content}

Ce cas d'utilisation utilise l'état d'abonnement d'un client pour envoyer du contenu personnalisé. Les clients abonnés à un groupe d'abonnement spécifique recevront un message exclusif pour les groupes d'abonnement par e-mail.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Mettre en majuscule la première lettre de chaque mot d'une chaîne de caractères {#misc-capitalize-words-string}

Ce scénario d'utilisation prend une chaîne de mots, les répartit dans un tableau et met en majuscule la première lettre de chaque mot.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Explication :** Ici, nous avons attribué une variable à notre attribut de chaîne de caractères choisi et utilisé le filtre `split` pour diviser la chaîne de caractères en un tableau. Nous avons ensuite utilisé la balise `for` pour attribuer la variable `words` à chacun des éléments de notre nouveau tableau, avant d'afficher ces mots avec le filtre `capitalize` et le filtre `append` pour ajouter des espaces entre chacun des termes.

### Comparer la valeur d'un attribut personnalisé à un tableau {#misc-compare-array}

Ce scénario d'utilisation répertorie les boutiques favorites, vérifie si l'une des boutiques préférées d'un utilisateur figure dans cette liste et, si tel est le cas, affiche une offre spéciale de ces boutiques.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Cette séquence possède une balise `break` dans l'instruction conditionnelle principale. La boucle s'arrête alors lorsqu'une correspondance est trouvée. Si vous souhaitez afficher plusieurs ou toutes les correspondances, supprimez la balise `break`. {% endalert %}

### Créer un rappel d'événement à venir {#misc-event-reminder}

Ce scénario d'utilisation permet aux utilisateurs de configurer des rappels à venir en fonction d'événements personnalisés. Le scénario exemple permet à un utilisateur de définir un rappel pour une date de renouvellement de police à 26 jours ou plus, les rappels étant envoyés 26, 13, 7 ou 2 jours avant la date de renouvellement.

Dans ce cas d'utilisation, les éléments suivants doivent figurer dans le corps d'une [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) ou d'une étape du Canvas.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %} 

Vous aurez besoin d'un événement personnalisé `reminder_capture` et les propriétés d'événement personnalisé doivent inclure au moins :

- `reminder-id` : Identifiant de l'événement personnalisé
- `reminder_date` : Date à laquelle le rappel de l'utilisateur est dû
- `message_personalisation_X` : Toutes les propriétés nécessaires pour personnaliser le message au moment de l'envoi

{% endalert %}

### Rechercher une chaîne de caractères dans un tableau {#misc-string-in-array}

Ce scénario d'utilisation vérifie si un tableau d'attributs personnalisés contient une chaîne de caractères spécifique et, si elle existe, affiche un message spécifique.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Trouver la plus grande valeur d'un tableau {#misc-largest-value}

Ce scénario d'utilisation calcule la valeur la plus élevée dans un tableau d'attributs personnalisés donné pour l'utiliser dans l'envoi de messages à l'utilisateur.

Par exemple, vous pouvez présenter le score le plus élevé actuel ou l'enchère la plus élevée sur un article à un utilisateur.

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
Vous devez utiliser un attribut personnalisé qui a une valeur entière et fait partie d'un tableau (liste). {% endalert %}

### Trouver la plus petite valeur d'un tableau {#misc-smallest-value}

Ce scénario d'utilisation calcule la valeur la plus faible dans un tableau d'attributs personnalisés donné pour l'utiliser dans l'envoi de messages à l'utilisateur.

Par exemple, vous pouvez présenter le score le plus bas ou l'article le moins cher à un utilisateur.

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

{% alert important %} Vous devez utiliser un attribut personnalisé qui a une valeur entière et fait partie d'un tableau (liste). {% endalert %}

### Interroger la fin d'une chaîne de caractères {#misc-query-end-of-string}

Ce scénario d'utilisation interroge la fin d'une chaîne de caractères pour l'utiliser dans l'envoi de messages.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Interroger les valeurs d'un tableau à partir d'un attribut personnalisé avec plusieurs combinaisons {#misc-query-array-values}

Ce scénario d'utilisation prend une liste de spectacles qui ne seront bientôt plus disponibles, vérifie si l'un des spectacles favoris d'un utilisateur figure dans cette liste et, si tel est le cas, affiche un message informant l'utilisateur qu'ils ne seront bientôt plus disponibles.

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

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Vous devrez d'abord trouver les correspondances entre les tableaux, puis construire la logique à la fin pour séparer les correspondances. {% endalert %}

### Formater une chaîne de caractères en numéro de téléphone {#phone-number}

Ce cas d'utilisation vous montre comment indexer le champ de profil utilisateur `phone_number` (par défaut formaté en tant que chaîne de caractères d'entiers) et le reformater selon vos normes locales de numéros de téléphone. Par exemple, 1234567890 vers (123)-456-7890.

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

- [Différencier le texte en fonction du système d'exploitation de l'appareil](#platform-device-os)
- [Cibler uniquement une plateforme spécifique](#platform-target)
- [Cibler uniquement les appareils iOS dotés d'une version spécifique du système d'exploitation](#platform-target-ios-version)
- [Cibler uniquement les navigateurs web](#platform-target-web)
- [Cibler un opérateur mobile spécifique](#platform-target-carrier)

### Différencier le texte en fonction du système d'exploitation de l'appareil {#platform-device-os}

Ce scénario d'utilisation vérifie la plateforme sur laquelle se trouve un utilisateur et, en fonction de sa plateforme, affiche un message spécifique.

Par exemple, vous pouvez montrer aux utilisateurs mobiles des versions plus courtes du texte du message tout en affichant aux autres utilisateurs la version classique et plus longue. Vous pouvez également montrer aux utilisateurs mobiles certains messages pertinents pour eux, mais qui ne le seraient pas pour les utilisateurs Web. Par exemple, la communication iOS peut parler d'Apple Pay, tandis que la communication Android doit mentionner Google Pay.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version. 
{% endif %}
```
{% endraw %}

{% alert note %} 
Liquid est sensible à la casse, `targeted_device.${platform}` renvoie la valeur entièrement en minuscules. 
{% endalert %}

### Cibler uniquement une