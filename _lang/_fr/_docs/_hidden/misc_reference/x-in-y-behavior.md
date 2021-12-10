---
nav_title: Comportement du filtre X en Y
permalink: /fr/x-in-y-behavior/
---

# Comportement du filtre X actuel en Y

Le comportement de ces filtres restera largement le même et sera défini par les caractéristiques suivantes :

- Exécutez en définissant les jours du calendrier (se terminant à minuit).
- Les "jours" sont définis comme en UTC.
- Le jour UTC actuel est défini comme "0".

{% détails Pourquoi la définition UTC est-elle passée de "1" à "0"? %}
La planification des fuseaux horaires locaux nécessite que les utilisateurs restent dans les segments pendant 24 heures. Dans le cas de Y = 1 jour, dans certains cas, nous évaluions moins de 24 heures de l’histoire de l’utilisateur pour déterminer qui doit être traité pour la campagne ou Canvas.

Le changement rendra le filtre plus intuitif et plus cohérent avec le comportement de notre autre fonctionnalité de calendrier, tels que nos options de planification pour l'envoi en 1 jour.
{% enddetails %}

<br>

## Exemple

La campagne présentée ci-dessous envoie à 21h00 le 16 avril. La segmentation du public est « Made more than 2 Purchase in the past 3 days ».

!\[Calendrier de la campagne\]\[1\]

21 h HE le 16 avril à 13 h 00 UTC le 17 avril.

Le 17 avril serait le jour "0", le 16 avril le jour "1", le 15 avril le jour "2", et le 14 avril le jour "3".

L'histoire de 12h00 UTC le 14 avril à l'heure actuelle (1:00AM UTC le 17 avril). Cela s'accumulerait dans une fenêtre qui inclurait 73 heures de l'historique de l'utilisateur.

## Sur les jours du calendrier

Les Jours Calendriers sont utilisés dans plus de capacités que dans les filtres "X in Y" :

- Planification des messages
- Plafond de fréquence
- Filtres "X in Y"

`Jours Calendrier` se réfèrent à la période de temps dans un jour numéroté, commençant à 00:00 et se terminant à 23:59PM ce même jour (12:00AM du 8 juin à 23:59PM du 8 juin serait un jour du calendrier unique.)

### Plafond de fréquence

Les jours du calendrier sont utilisés lorsque vous sélectionnez « jours» ou « semaines» sous `plafonnement de fréquence`.

- `Chaque 1 jour` limitera le plafonnement au jour du calendrier actuel dans l'heure locale de votre utilisateur (se terminant à minuit heure locale).
- `Tous les 2 jours` limitera le plafonnement aux jours de calendrier précédents et actuels dans l'heure locale de votre utilisateur (se terminant à minuit heure locale le jour du calendrier actuel).

### Entreprise & Heure locale

Le jour du calendrier actuel dans le fuseau horaire de l'entreprise compte comme le jour `0`.

`Envoyer en 1 jours de calendrier à 11:05AM heure de la société` ou `envoyer 1 jour de calendrier à 11:05AM heure locale` ajouterait `1` jour au jour du calendrier actuel dans le fuseau horaire de la société ou le fuseau horaire local. respectivement, puis programmez le message au prochain 11:05AM Entreprise à venir.

Si la compagnie ou l'heure locale est heure du Pacifique, et que l'utilisateur entre dans l'étape de Canvas à 20h00 PT le 4/13, Braze programmera cette étape de Canvas pour 11:05 h PT sur 4/14.

## Précédent X dans le comportement du filtre Y

Braze a une catégorie spécifique de filtres de segmentation appelée "X in Y Filters". Ces filtres ont chacun des fonctionnalités similaires définies par les caractéristiques suivantes :

- Exécutez en définissant les jours du calendrier (se terminant à minuit).
- Les "jours" sont définis comme en UTC.
- Le jour UTC actuel est défini comme "1".
[1]:{% image_buster /assets/img/campaign-schuedule-exemple.png %}
