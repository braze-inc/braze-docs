---
nav_title: Campagnes d’utilisateurs actifs
article_title: Campagnes d’utilisateurs actifs
page_order: 0.5
page_type: tutorial
description: "Le présent article pratique décrit les campagnes d’utilisateurs actifs dans le tableau de bord de Braze et les étapes à suivre pour en créer et en configurer une."
tool: 
  - Campaigns

---

# Campagnes d’utilisateurs actifs

> Le présent article abordera les avantages des campagnes d’utilisateurs actifs dans le tableau de bord de Braze, ainsi que de la manière d’identifier et de contacter vos meilleurs utilisateurs.
> <br>
> <br>
> Identifier vos utilisateurs actifs peut vous aider à créer des campagnes sur mesure et à récompenser ceux qui fréquentent votre plateforme. 

Contacter les utilisateurs déjà actifs de votre application peut être un outil puissant pour vous aider à créer un ensemble d’utilisateurs assidus de votre application. Un peu de reconnaissance personnalisée pour vos utilisateurs moteurs peut les transformer en apôtres de votre application.

Vous pouvez également consulter notre [Cours d’apprentissage de Braze](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sur la stratégie marketing pour les e-mails et les campagnes basées sur le cycle de vie client recommandées !

## Comprendre les utilisateurs actifs

Braze définit un « utilisateur actif » pendant une période donnée comme tout utilisateur qui a une session dans cette période.

Si un utilisateur perd la connectivité, nous mettrons les données de session en cache localement et les enverrons lorsque l’utilisateur retrouve une connexion réseau. Ces sessions seront également appliquées au nombre d’utilisateurs actifs. De plus, si votre application a un processus d’inscription, Braze comptera tous les utilisateurs comme actifs, qu’ils soient enregistrés ou non.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu’un nouvel utilisateur se connecte, il sera compté comme un utilisateur actif séparé. Les utilisateurs mis à jour via l’API seront également comptés comme utilisateurs actifs dans la période où ils ont été mis à jour.

## Étape 1 : Identifier vos meilleurs utilisateurs

Grâce à la sélection de filtres de Braze, créez un segment d’utilisateur qui vous semble comprendre votre base utilisateur la plus fidèle et la plus régulière. L’exemple de segment suivant définit les meilleurs utilisateurs.

![][1]

De plus, vous n’aurez pas à continuer à mettre à jour ce segment car les utilisateurs qui rentrent ou sortent des restrictions de la campagne seront ciblés ou enlevés en fonction.

{% alert note %}
L’exemple précédent segmente les utilisateurs selon leur utilisation générale de l’application. Dans la plupart des cas, l’assortiment complet de filtres nécessaires pour définir votre segment de meilleurs utilisateurs sera en grande partie défini par les spécificités de votre application.
{% endalert %}

## Étape 2 : Contacter vos meilleurs utilisateurs

### Faites en sorte que vos utilisateurs se sentent appréciés

Faites en sorte que vos utilisateurs se sentent appréciés en remerciant leur fidélité et leur dévouement à votre application. Donnez à vos utilisateurs des raisons supplémentaires de revenir à votre application pour encourager une activité supplémentaire. Cela peut prendre la forme d’offres spéciales ou de primes réservées à vos meilleurs utilisateurs. 

Les récompenses inattendues peuvent être plus efficaces pour encourager des actions continues des utilisateurs que si vous les aviez promis dès le début !

![Une campagne dans l’étape Composer avec une notification enrichie iOS qui affiche : « Merci encore d’avoir acheté chez nous ! Pour montrer notre reconnaissance, nous vous offrons une livraison gratuite lors de votre prochain achat. »][2]

### Surveiller vos résultats

Suivez les ouvertures pour vous assurer de cibler l’ensemble approprié d’utilisateurs avec le type de message optimal. De plus, maintenez un suivi de tout désabonnement aux notifications push et évitez de perdre ces utilisateurs cruciaux.

[1]: {% image_buster /assets/img_archive/define_top_users.png %} "Define your top users"
[2]: {% image_buster /assets/img/congratulations_push.jpg %}