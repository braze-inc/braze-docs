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

- [Personnalisation des messages en fonction de l'année d'anniversaire de l'utilisateur](#anniversary-year)
- [Personnalisation des messages en fonction de la semaine d'anniversaire de l'utilisateur](#birthday-week)
- [Envoyez des campagnes aux utilisateurs au cours de leur mois d'anniversaire](#birthday-month)
- [Évitez d'envoyer des messages les jours fériés.](#holiday-avoid)

### Personnaliser les messages en fonction de l’année anniversaire d’un utilisateur {#anniversary-year}

Ce scénario d’utilisation montre comment calculer l’anniversaire d’utilisation d’une application d’un utilisateur en fonction de sa date d’inscription initiale et afficher différents messages en fonction du nombre d’années célébrées.

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

**Explication :** Ici, nous utilisons la variable réservée `now` pour introduire la date et l'heure actuelles au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). Les filtres `%B` (mois comme « mai ») et `%d` (jour comme « 18 ») formatent le mois et le jour actuels. Nous utilisons ensuite les mêmes filtres de date et de temps sur les valeurs `signup_date` pour nous assurer de comparer les deux valeurs à l’aide des balises conditionnelles et de la logique.

Ensuite, nous renouvelons trois autres instructions variables pour obtenir `%B` et `%d` pour la `signup_date`, mais ajoutons également `%Y` (année comme « 2021 »). Ceci compose la date et de l’heure de la `signup_date` sous forme d’année. Connaître le jour et le mois nous permet de vérifier si l’anniversaire de l’utilisateur est aujourd’hui, et en sachant que l’année nous dit combien d’années ont passées, ce qui nous permet de savoir pour combien d’années le féliciter !

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

**Explication :** Comme dans le cas de l' [année d'anniversaire](#anniversary-year), nous prenons ici la variable réservée `now` et utilisons le filtre `%W` (semaine telle que la semaine 12 sur les 52 de l'année) pour obtenir le numéro de la semaine de l'année dans laquelle tombe l'anniversaire de l'utilisateur. Si la semaine d’anniversaire de l’utilisateur correspond à la semaine en cours, nous lui envoyons un message de félicitations ! 

Nous incluons également des instructions pour `last_week` et `next_week` pour personnaliser votre envoi de messages.

### Envoyer des campagnes aux utilisateurs pendant leur mois d’anniversaire {#birthday-month}

Ce scénario d’utilisation indique comment calculer le mois d’anniversaire d’un utilisateur, vérifier si son anniversaire tombe pendant le mois en cours et, si tel est le cas, envoyer un message spécial.

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

**Explication :** Similaire au cas d'utilisation de la [semaine d'anniversaire](#birthday-week), sauf qu'ici nous utilisons le filtre `%B` (mois comme "mai") pour calculer quels utilisateurs ont un anniversaire ce mois-ci. Une application potentielle pourrait traiter les utilisateurs ayant un anniversaire dans un e-mail mensuel.

### Évitez d’envoyer des messages lors des fêtes principales {#holiday-avoid}

Ce scénario d’utilisation indique comment envoyer des messages pendant la période des fêtes tout en évitant les jours fériés principaux, lorsque l’engagement est susceptible d’être faible.

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

**Explication :** Ici, nous assignons le terme `today` à la variable réservée `now` (la date et l'heure actuelles), en utilisant les filtres `%Y` (année comme "2023"), `%m` (mois comme "12") et `%d` (jour comme "25") pour formater la date. Nous exécutons ensuite notre instruction conditionnelle pour dire que si la variable `today` correspond aux jours fériés de votre choix, le message sera abandonné. 

L’exemple présenté correspond à la veille de Noël, le jour de Noël et le lendemain de Noël.

{% endapi %}

{% api %}

## Utilisation de l’application

{% apitags %}
Utilisation de l’application
{% endapitags %}

- [Envoyez des messages dans la langue de l'utilisateur s'il a ouvert une session.](#app-session-language)
- [Personnaliser les messages en fonction de la date à laquelle l'utilisateur a ouvert l'application pour la dernière fois.](#app-last-opened)
- [Afficher un message différent si la dernière utilisation de l'application remonte à moins de trois jours.](#app-last-opened-less-than)

### Envoyer des messages dans la langue d’un utilisateur s’il s’est connecté à une session {#app-session-language}

Ce scénario d’utilisation vérifie si un utilisateur s’est connecté à une session et, si ce n’est pas le cas, inclut une logique d’affichage d’un message reposant sur la langue collecté manuellement via un attribut personnalisé, le cas échéant. S’il n’y a pas d’informations de langue liées au compte, il affiche le message dans la langue par défaut. Si un utilisateur s’est connecté à une session, il extrait toutes les informations de langue liées à l’utilisateur et affiche le message approprié. 

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
**Explication :** Ici, nous utilisons deux instructions `if` regroupées, imbriquées. La première instruction `if` vérifie si l’utilisateur a démarré une session en vérifiant si `last_used_app_date` est `nil`. En effet, `{{${language}}}` est automatiquement collecté par le SDK lorsqu’un utilisateur se connecte à une session. Si l’utilisateur ne s’est pas connecté à une session, nous n’avons pas encore sa langue, donc cette vérification s’effectue si des attributs personnalisés liés à la langue ont été enregistrés et, sur la base de ces informations, affiche un message dans cette langue, si possible.
{% endraw %}

Le second énoncé `if` vérifie l’attribut de base (par défaut), car l’utilisateur n’a pas `nil` pour la `last_used_app_date`, ce qui signifie qu’il s’est connecté à une session et que nous avons sa langue.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) est une variable réservée qui est renvoyée lorsque le code Liquid ne donne aucun résultat. `Nil` est traité comme `false` dans un bloc `if`.
{% endalert %}

### Personnaliser les messages en fonction du moment où un utilisateur a ouvert l’application {#app-last-opened}

Ce scénario d’utilisation calcule la dernière ouverture de l’application par l’utilisateur et affiche un message personnalisé différent selon la durée.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
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
- [Créer un compte à rebours pour les dates et priorités d’expédition spécifiques](#countdown-shipping-options)
- [Créer un compte à rebours en jours](#countdown-days)
- [Créer un compte à rebours de jours, d'heures et de minutes](#countdown-dynamic)
- [Indiquer le nombre de jours restants jusqu'à une certaine date](#countdown-future-date)
- [Afficher le nombre de jours restants avant l'arrivée d'un attribut personnalisé de la date](#countdown-custom-date-attribute)
- [Afficher le temps restant et interrompre le message s’il n’y a que X temps restant](#countdown-abort-window)
- [Message in-app à envoyer X jours avant la fin de l’abonnement de l’utilisateur](#countdown-membership-expiry)
- [Personnaliser les messages in-app en fonction de la date et de la langue de l'utilisateur.](#countdown-personalize-language)
- [Modèle de date dans 30 jours, formaté en tant que mois et jour](#countdown-template-date)

### Ajouter X jours à partir de date d’aujourd’hui {#countdown-add-x-days}

Ce scénario d’utilisation ajoute un nombre spécifique de jours à la date actuelle à référencer et ajouter dans les messages. Par exemple, vous pouvez envoyer en milieu de semaine un message indiquant les événements prévus dans la région pour le week-end.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

La `plus` valeur sera toujours en secondes, donc nous finissons par le filtre `%F` pour traduire les secondes en jours.

{% alert important %}
Vous pouvez inclure une URL ou un lien profond vers une liste d’événements dans votre message afin d’envoyer l’utilisateur une liste d’actions qui se produisent à l’avenir.
{% endalert %}

### Calculer un compte à rebours à partir d’un point dans le temps {#countdown-difference-days}

Ce scénario d’utilisation calcule la différence de jours entre une date spécifique et la date actuelle. Cette différence peut servir à afficher un compte à rebours à vos utilisateurs.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Créer un compte à rebours pour les dates et priorités d’expédition spécifiques {#countdown-shipping-options}

Ce scénario d’utilisation capture différentes options d’expédition, calcule la durée nécessaire à la réception et affiche des messages encourageant les utilisateurs à acheter à temps pour recevoir leur colis à une date donnée.

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

Ce scénario d’utilisation calcule le temps restant entre un événement spécifique et la date actuelle et affiche le nombre de jours restants jusqu’à l’événement.

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
Vous aurez besoin d’un champ d’attribut personnalisé avec une valeur `date`.
{% endalert %}

### Créer un compte à rebours de jours à heures à minutes {#countdown-dynamic}

Ce scénario d’utilisation calcule le temps restant entre un événement spécifique et la date actuelle. En fonction du temps restant jusqu’à l’événement, il modifie la valeur de temps (jours, heures, minutes) pour afficher différents messages personnalisés.

Par exemple, s’il y a reste deux jours jusqu’à ce que la commande d’un client arrive, vous pourriez dire : « Votre commande arrivera dans 2 jours ». En revanche, s'il reste moins d'un jour, vous pourriez indiquer plutôt « Votre commande arrivera dans 17 heures ».

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
Vous aurez besoin d’un champ d’attribut personnalisé avec une valeur `date`. Vous devrez également définir des seuils de temps lorsque vous voulez afficher le temps en jours, heures et minutes.
{% endalert %}

### Affiche le nombre de jours restant avant une date donnée {#countdown-future-date}

Ce scénario d’utilisation calcule le temps restant entre un événement spécifique et la date actuelle et affiche un message indiquant le nombre de jours restants jusqu’à l’événement.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
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
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Afficher le temps restant et interrompre le message s’il n’y a que X temps restant {#countdown-abort-window}

Ce cas d’utilisation calcule la durée jusqu’à une certaine date et, en fonction de la longueur (saut d’envoi de messages si la date est trop courte), affiche différents messages personnalisés. 

Par exemple, « Vous avez x heures restantes pour acheter pour acheter votre billet pour Londres », mais le message n’est pas envoyé dans les deux heures qui précèdent l’heure de vol pour Londres.

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

{% alert important %} Vous aurez besoin de créer une propriété d’événement personnalisé. {% endalert %}

### Messages in-app pour envoyer X jours avant la fin de l’abonnement de l’utilisateur {#countdown-membership-expiry}

Ce scénario d’utilisation capture la date d’expiration de votre abonnement, calcule la durée jusqu’à ce qu’elle expire et affiche différents messages en fonction du délai d’expiration de votre abonnement.

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

### Personnaliser les messages dans l’appli en fonction de la date et de la langue de l’utilisateur {#countdown-personalize-language}

Ce scénario d’utilisation calcule un compte à rebours jusqu’à un événement et, en fonction du paramètre de langue d’un utilisateur, affiche le compte à rebours dans sa langue.

Par exemple, vous pouvez envoyer une série de messages incitatifs aux utilisateurs une fois par mois pour leur indiquer combien de temps une offre reste valide avec quatre messages in-app :

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
Vous devrez attribuer une valeur `date` et inclure la logique d’abandon si la date donnée tombe en dehors de la plage de dates. Pour les calculs de jour exacts, la date de fin attribuée doit inclure 23:59:59.
{% endalert %}

### Modèle de date 30 jours à partir d’aujourd’hui, formaté en tant que mois et jour {#countdown-template-date}

Ce scénario d’utilisation affiche la date 30 jours à partir de maintenant à utiliser dans les envois de messages.

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

- [Personnaliser un message en fonction d'attributs personnalisés](#attribute-matching)
- [Soustraire deux attributs personnalisés pour afficher la différence sous la forme d'une valeur monétaire](#attribute-monetary-difference)
- [Référence le prénom d'un utilisateur si son nom complet est stocké dans le champ first_name ](#attribute-first-name)

### Personnaliser un message en fonction des attributs personnalisés correspondants {#attribute-matching}

Ce scénario d’utilisation vérifie si un utilisateur a des attributs personnalisés spécifiques et, le cas échéant, affiche différents messages personnalisés. 

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

### Soustraire deux attributs personnalisés pour afficher la différence en valeur monétaire {#attribute-monetary-difference}

Ce scénario d’utilisation capture deux attributs personnalisés monétaires, puis calcule et affiche la différence pour permettre aux utilisateurs de savoir combien de temps ils leur restent pour atteindre leur objectif.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Indiquer le prénom d’un utilisateur si son nom complet est stocké dans le champ first_name {#attribute-first-name}

Ce scénario d’utilisation capture le prénom d’un utilisateur (si le prénom et le nom sont stockés dans un champ unique), puis utilise ce prénom pour afficher un message de bienvenue.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explication :** Le filtre `split` transforme la chaîne de caractères contenue dans `{{${first_name}}}` en tableau. En utilisant `{{name[0]}}`, nous ne faisons alors référence qu’au premier élément du tableau, qui est le prénom de l’utilisateur. 

{% endraw %}
{% endapi %}

{% api %}

## Événement personnalisé

{% apitags %}
Événement personnalisé
{% endapitags %}

- [Abandonner la notification push si un événement personnalisé a lieu dans les deux heures qui suivent.](#event-abort-push)
- [Envoyez une campagne chaque fois qu'un utilisateur effectue un événement personnalisé à trois reprises.](#event-three-times)
- [Envoyez un message aux utilisateurs qui n'ont acheté que dans une seule catégorie.](#event-purchased-one-category)
- [Suivre le nombre de fois qu'un événement personnalisé s'est produit au cours du mois écoulé.](#track)


### Annuler la notification push si un événement personnalisé arrive dans les deux heures qui suivent {#event-abort-push}

Ce cas d’utilisation calcule le temps restant jusqu’à un événement et, selon le temps restant, affiche différents messages personnalisés.

Par exemple, vous souhaiterez peut-être empêcher l'envoi d'une notification push si une propriété d'événement personnalisé passe dans les deux prochaines heures. Cet exemple utilise le scénario d’un panier abandonné pour un billet de train.

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

### Envoyer une campagne à chaque fois qu’un utilisateur effectue un événement personnalisé trois fois {#event-three-times}

Ce scénario d’utilisation vérifie si un utilisateur a effectué un événement personnalisé trois fois et, si tel est le cas, affiche un message ou envoie une campagne. 

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

{% alert important %} Vous devez disposer d’une propriété de l’événement du nombre d’événements personnalisés ou utiliser un webhook sur votre endpoint Braze. Ceci permet d’incrémenter un attribut personnalisé (`example_event_count`) à chaque fois que l’utilisateur exécute l’événement. Cet exemple utilise une cadence de trois (1, 4, 7, 10, etc.). Pour démarrer la cadence à partir de zéro (0, 3, 6, 9, etc.), enlevez `minus: 1`.
{% endalert %}

### Envoyer un message aux utilisateurs qui n’ont acheté qu’une seule catégorie {#event-purchased-one-category}

Ce scénario d’utilisation capture une liste des catégories achetées par un utilisateur et, si une seule catégorie d’achat existe, elle affiche un message.

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

### Suivre combien de fois un événement personnalisé s’est produit au cours du dernier mois {#track}

Ce cas d’utilisation calcule le nombre de fois qu’un événement personnalisé a été enregistré entre le premier du mois en cours et le mois précédent. Vous pouvez alors exécuter un appel utilisateurs/suivi pour mettre à jour et enregistrer cette valeur en tant qu’attribut personnalisé. Prenez note du fait que cette campagne devra être exécutée pendant deux mois consécutifs avant que des données mensuelles puissent être utilisées.

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
- [Personnalisation des messages en fonction du jour de la semaine et de la langue de l'utilisateur](#language-personalize-message)

### Afficher les noms des mois dans une langue différente {#language-display-month}

Ce scénario d’utilisation affiche la date, le mois et l’année en cours, avec le mois dans une langue différente. L’exemple présenté est suédois.

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

### Afficher une image selon la langue d’un utilisateur {#language-image-display}

Ce cas d’utilisation affichera une image selon la langue d’un utilisateur. Notez que ce cas d'utilisation n'a été testé qu'avec des images téléchargées dans la bibliothèque multimédia de Braze.

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

### Personnaliser l’envoi de messages en fonction du jour de la semaine et de la langue de l’utilisateur {#language-personalize-message}

Ce scénario d’utilisation vérifie le jour actuel de la semaine et, en fonction du jour, si la langue de l’utilisateur est définie sur l’une des options de langue fournies, il affiche un message spécifique dans sa langue.

L’exemple fourni s’arrête mardi mais peut être répété pour chaque jour de la semaine.

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

- [Évitez d'envoyer des e-mails aux clients qui ont bloqué les e-mails marketing.](#misc-avoid-blocked-emails)
- [Utilisez l'état de l'abonnement d'un client pour personnaliser le contenu des messages.](#misc-personalize-content)
- [Mettez une majuscule à la première lettre de chaque mot d'une chaîne de caractères](#misc-capitalize-words-string)
- [Comparer la valeur d'un attribut personnalisé à un tableau](#misc-compare-array)
- [Créer un rappel d'événement à venir](#misc-event-reminder)
- [Recherche d'une chaîne de caractères dans un tableau](#misc-string-in-array)
- [Trouver la plus grande valeur d'un tableau](#misc-largest-value)
- [Trouver la plus petite valeur d'un tableau](#misc-smallest-value)
- [Interroger la fin d'une chaîne de caractères](#misc-query-end-of-string)
- [Interroger les valeurs d'un tableau à partir d'un attribut personnalisé à combinaisons multiples](#misc-query-array-values)
- [Formater une chaîne de caractères en numéro de téléphone](#phone-number)

### Éviter d’envoyer des e-mails aux clients qui ont bloqué des e-mails marketing {#misc-avoid-blocked-emails}

Ce cas d'utilisation prend une liste d'utilisateurs bloqués enregistrée dans un bloc de contenu et vérifie que ces utilisateurs bloqués ne sont pas communiqués ou ciblés dans les prochaines campagnes ou Canvases.

{% alert important %}
Pour utiliser ce Liquid, enregistrez d’abord la liste des e-mails bloqués dans un bloc de contenu. La liste ne doit pas comporter d'espaces ou de caractères supplémentaires entre les adresses e-mail (par exemple, `test@braze.com,abc@braze.com`).
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

**Explication :** Nous vérifions ici si l’e-mail de votre destinataire potentiel est dans cette liste en faisant référence au bloc de contenu des e-mails bloqués. Si l’e-mail est trouvé, le message ne s’affichera pas.

{% alert note %}
Les blocs de contenu ont une limite de taille de 5 Mo.
{% endalert %}

### Utiliser l’état d’abonnement d’un client pour personnaliser le contenu dans des messages {#misc-personalize-content}

Ce cas d’utilisation utilise l’état d’abonnement d’un client pour envoyer du contenu personnalisé. Les clients abonnés à un groupe d’abonnement spécifique recevront un message exclusif pour les groupes d’abonnement par e-mail.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Capitaliser la première lettre de chaque mot dans une chaîne de caractères {#misc-capitalize-words-string}

Ce scénario d’utilisation prend une chaîne de mots, les répartit dans un tableau et capitalise la première lettre de chaque mot.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Explication :** Ici, nous avons attribué une variable à notre attribut de chaîne de caractères choisi et utilisé le filtre `split` pour diviser la chaîne de caractères en un tableau. Nous avons ensuite utilisé la balise `for` pour attribuer la variable `words` à chacun des éléments de notre nouveau tableau, avant d’afficher ces mots avec le filtre `capitalize` et le filtre `append` pour ajouter des espaces entre chacun des termes.

### Comparer la valeur d’attribut personnalisé à un tableau {#misc-compare-array}

Ce scénario d’utilisation répertorie les boutiques favorites, vérifie si l’une des boutiques préférées d’un utilisateur figure dans cette liste et, si tel est le cas, affiche une offre spéciale pour ces boutiques.

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

{% alert important %} Cette séquence possède une balise `break` dans la déclaration conditionnelle principale. La boucle s’arrête alors lorsqu’une correspondance est trouvée. Si vous souhaitez afficher plusieurs ou toutes les correspondances, supprimez la balise `break`. {% endalert %}

### Créer un rappel d’événement à venir {#misc-event-reminder}

Ce scénario d’utilisation permet aux utilisateurs de configurer des rappels à venir en fonction des événements personnalisés. Le scénario exemple permet à un utilisateur de définir un rappel pour une date de renouvellement de police de 26 jours ou plus, dans lequel les rappels sont envoyés 26, 13, 7 ou 2 jours avant la date de renouvellement de la police.

Dans ce cas d'utilisation, les éléments suivants doivent figurer dans le corps d'une [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) ou d'une étape du canvas.

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

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
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

Vous aurez besoin d’un événement personnalisé `reminder_capture` et les propriétés d’événement personnalisé doivent inclure au moins :

- `reminder-id` : Identificateur de l’événement personnalisé
- `reminder_date` : Date d’envoi du rappel à l’utilisateur
- `message_personalisation_X` : Toutes les propriétés nécessaires pour personnaliser le message au moment de l’envoi

{% endalert %}

### Rechercher une chaîne de caractères dans un tableau {#misc-string-in-array}

Ce scénario d’utilisation vérifie si une matrice d’attributs personnalisée contient une chaîne de caractères spécifique et, si elle existe, affiche un message spécifique.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Rechercher la plus grande valeur dans un tableau {#misc-largest-value}

Ce scénario d’utilisation calcule la valeur la plus élevée dans un tableau d’attributs personnalisée donné à utiliser dans l’envoi de messages à l’utilisateur.

Par exemple, vous pouvez présenter le score le plus élevé actuel ou l’enchère la plus élevée d’un article à un utilisateur.

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

### Extraire la fin d’une chaîne de caractères{#misc-query-end-of-string}

Ce scénario d’utilisation interroge la fin d’une chaîne de caractères à utiliser dans l’envoi de messages.

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

### Interroger les valeurs d'un tableau à l'aide d’un attribut personnalisé avec plusieurs combinaisons {#misc-query-array-values}

Ce scénario d’utilisation prend une liste des spectacles qui ne seront bientôt plus à l’affiche, vérifie si l’un des spectacles favoris d’un utilisateur figure dans cette liste et, si tel est le cas, afficher un message informant l’utilisateur qu’il ne sera bientôt plus à l’affiche.

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

{% alert important %} Vous devrez d’abord trouver des correspondances entre les tableaux, puis créer une logique à la fin pour séparer les correspondances. {% endalert %}

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

- [Différencier la copie en fonction du système d'exploitation de l'appareil](#platform-device-os)
- [Cibler uniquement une plateforme spécifique](#platform-target)
- [Ciblez uniquement les appareils iOS dotés d'une version spécifique du système d'exploitation.](#platform-target-ios-version)
- [Cibler uniquement les navigateurs web](#platform-target-web)
- [Cibler un opérateur mobile spécifique](#platform-target-carrier)

### Différencier les copies par OS d’appareil {#platform-device-os}

Ce scénario d’utilisation vérifie la plate-forme sur laquelle un utilisateur est connecté et, en fonction de sa plateforme, affiche des envois de messages spécifiques.

Par exemple, vous pouvez montrer aux utilisateurs mobiles les versions plus courtes du texte du message tout en affichant aux autres utilisateurs la version classique et plus longue du texte. Vous pouvez également montrer aux utilisateurs mobiles certains envois de messages pertinents pour eux, mais qui ne seraient pas pertinents pour les utilisateurs Web. Par exemple, la communication iOS peut parler d’Apple Pay, mais les communications Android doivent mentionner Google Pay.

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

### Cibler uniquement une plate-forme spécifique {#platform-target}

Ce scénario d’utilisation capture la plate-forme de l’appareil des utilisateurs et, en fonction de la plateforme, affiche un message.

Par exemple, vous pouvez envoyer un message uniquement aux utilisateurs Android. Cette option peut être utilisée comme alternative à la sélection d’une application dans l’outil Segmentation.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

This is a message for an Android user! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Cibler uniquement les appareils avec une version d’OS spécifique {#platform-target-ios-version}

Ce scénario d’utilisation vérifie si la version OS d’un utilisateur appartient à un certain ensemble de versions et, si tel est le cas, affiche un message spécifique.

L’exemple utilisé envoie un avertissement aux utilisateurs sur une version d’OS 10.0 ou antérieure signalant qu’ils vont rendre obsolète la prise en charge du système d’exploitation de l’appareil de l’utilisateur.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler uniquement les navigateurs Web {#platform-target-web}

Ce scénario d’utilisation vérifie si l’appareil cible d’un utilisateur fonctionne sur Mac ou Windows et, le cas échéant, affiche un message spécifique.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

Le cas d’usage suivant vérifie si un utilisateur Web est sur iOS ou Android et, si oui, affichera un message particulier.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Cibler un opérateur mobile spécifique {#platform-target-carrier}

Ce scénario d’utilisation vérifie si le fournisseur d’accès d’un appareil d’un utilisateur est Verizon et, si tel est le cas, affiche un message spécifique.

Pour  les canaux de notifications push et de message in-app, vous pouvez spécifier le support de l’appareil dans votre corps de message en utilisant Liquid. Si le fournisseur d’accès de l’appareil du destinataire ne correspond pas, le message ne sera pas envoyé.

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [Répondre par différents messages en fonction du mot-clé du SMS entrant.](#sms-keyword-response)

### Répondre par différents messages en fonction du mot-clé du SMS entrant. {#sms-keyword-response}

Ce cas d'utilisation intègre le traitement dynamique des mots-clés SMS pour répondre à des messages entrants spécifiques avec des envois de messages différents. Par exemple, vous pouvez envoyer des réponses différentes lorsque quelqu'un envoie un message "START" ou "JOIN".

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Fuseau horaire

{% apitags %}
Fuseau horaire
{% endapitags %}

- [Personnaliser un message en fonction du fuseau horaire de l'utilisateur](#personalize-timezone)
- [Ajouter le fuseau horaire CST à un attribut personnalisé](#time-append-cst)
- [Insérer un horodatage](#time-insert-timestamp)
- [N'envoyez un push Canvas que pendant une fenêtre de temps dans le fuseau horaire local de l'utilisateur.](#time-canvas-window)
- [Envoyer une campagne de messages in-app récurrente dans une fenêtre de temps dans le fuseau horaire local d’un utilisateur](#time-reocurring-iam-window)
- [Envoyez des messages différents en semaine et le week-end dans le fuseau horaire local de l'utilisateur.](#time-weekdays-vs-weekends)
- [Envoyer des messages différents en fonction de l'heure de la journée dans le fuseau horaire local de l'utilisateur.](#time-of-day)

### Personnaliser un message selon le fuseau horaire d’un utilisateur {#personalize-timezone}

Ce cas d’utilisation affiche des messages différents selon le fuseau horaire de l’utilisateur.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{$time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### Ajouter le fuseau horaire CST à un attribut personnalisé {#time-append-cst}

Ce scénario d’utilisation affiche un attribut de date personnalisée dans un fuseau horaire donné.

Option 1 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Option 2 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Insérer un horodatage {#time-insert-timestamp}

Ce scénario d’utilisation affiche un message qui inclut un horodatage dans le fuseau horaire actuel de l’utilisateur.

L’exemple suivant indique la date YYYY-mm-dd HH:MM:SS, comme 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Envoyer une notification push de Canvas uniquement pendant une période de temps dans le fuseau horaire local d’un utilisateur {#time-canvas-window}

Ce scénario d’utilisation vérifie l’heure d’un utilisateur dans son fuseau horaire local et, s’il correspond à un horaire défini, il affiche un message spécifique.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### Envoyer une campagne de messages in-app récurrente entre une fenêtre de temps dans la zone horaire locale d’un utilisateur {#time-reoccurring-iam-window}

Ce scénario d’utilisation affiche un message si l’heure actuelle d’un utilisateur se trouve dans une fenêtre définie.

Par exemple, le scénario suivant permet à un utilisateur de savoir qu’une boutique est fermée.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %} 
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Envoyer différents messages en semaine par rapport aux week-ends dans le fuseau horaire local d’un utilisateur {#time-weekdays-vs-weekends}

Ce scénario d’utilisation vérifie si le jour actuel de la semaine d’un utilisateur est un samedi ou un dimanche et, en fonction de la journée, affiche différents messages.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
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
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} Ceci est le contraire des [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns). {% endalert %}

{% endapi %}

{% api %}

## Semaine/Jour/Mois

{% apitags %}
Semaine/Jour/Mois
{% endapitags %}

- [Insérer le nom du mois précédent dans un message](#month-name)
- [Envoyez une campagne à la fin de chaque mois](#month-end)
- [Envoyez une campagne le dernier (jour de la semaine) du mois](#day-of-month-last)
- [Envoyez un message différent chaque jour du mois](#day-of-month)
- [Envoyez un message différent chaque jour de la semaine](#day-of-week)

### Tirer le nom du mois précédent dans un message {#month-name}

Ce scénario d’utilisation prend le mois en cours et affiche le mois précédent à utiliser dans l’envoi de messages.

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
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

Vous pouvez également utiliser la méthode suivante pour obtenir le même résultat.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

### Envoyer une campagne à la fin de chaque mois {#month-end}

Ce scénario d’utilisation vérifiera si la date actuelle tombe dans une liste de dates et, en fonction de la date, affiche un message spécifique.

{% alert note %} Cela ne tient pas compte des années bissextiles (29 février). {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### Envoyer une campagne le dernier jour du mois {#day-of-month-last}

Ce scénario d’utilisation capture le mois et le jour en cours et calcule si le jour actuel tombe le dernier jour de la semaine du mois.

Par exemple, vous pouvez envoyer une enquête à vos utilisateurs le dernier mercredi du mois, demandant des commentaires sur les produits.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

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

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%} 
{% if diff_in_days <= 7 %} 
{% unless current_day_name == "Wed" %} 
{% abort_message("Wrong day of the week") %} 
{% endunless %} 
{% else %} 
{% abort_message("Not the last week of the month") %} 
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
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### Envoyer un message différent chaque jour de la semaine {#day-of-week}

Ce scénario d’utilisation vérifie le jour de la semaine et, en fonction du jour, affiche un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
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

{% alert note %}
Vous pouvez remplacer la ligne "default copy" par {% raw %}`{% abort_message() %}`{% endraw %} pour empêcher l'envoi du message si le jour de la semaine est inconnu.
{% endalert %}

{% endapi %}
