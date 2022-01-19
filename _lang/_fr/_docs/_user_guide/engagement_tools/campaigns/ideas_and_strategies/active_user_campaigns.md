---
nav_title: Campagnes d'utilisateurs actifs
article_title: Campagnes d'utilisateurs actifs
page_order: 0
page_type: tutoriel
description: "Cet article décrit les campagnes d'utilisateurs actifs dans le tableau de bord de Braze et les étapes pour en créer et en configurer."
tool:
  - Campagnes
---

# Campagnes utilisateur actives

> Cet article discutera des avantages des campagnes d'utilisateurs actives dans le tableau de bord de Braze, ainsi que la façon d'identifier et de contacter vos meilleurs utilisateurs. <br> <br> Identifier vos utilisateurs actifs peut vous aider à créer des campagnes sur mesure et récompenser ceux qui fréquentent votre plateforme.

Atteindre des utilisateurs déjà actifs de votre application peut être un outil puissant pour aider à construire une suite dédiée aux utilisateurs cohérents de l'application. Un peu de reconnaissance personnalisée de vos utilisateurs de puissance peut les transformer en évangélistes pour votre application.

Vous pouvez également consulter [notre cours LAB](http://lab.braze.com/quick-overview-segment-and-campaign-setup) sur la stratégie de marketing pour les campagnes de cycle de vie recommandées !

## Comprendre les utilisateurs actifs

Braze définit un "utilisateur actif" pour une période donnée comme tout utilisateur ayant une session pendant cette période.

Si un utilisateur perd la connectivité, nous mettrons en cache les données de session localement et les chargerons lorsque l'utilisateur retrouvera une connexion réseau. Ces sessions seront également appliquées au nombre d'utilisateurs actifs. De plus, si votre application a un processus d'inscription, Braze comptera tous les utilisateurs comme actifs, enregistrés ou non enregistrés.

Si vous définissez les identifiants d'utilisateur pour identifier les utilisateurs lorsqu'un nouvel utilisateur se connecte, ils seront comptés comme un utilisateur actif séparé. Les utilisateurs qui sont mis à jour via l'API seront également comptés comme un utilisateur actif dans la période de temps où ils sont mis à jour.

## Étape 1 : Identifier vos meilleurs utilisateurs

En utilisant la sélection de filtres de Braze, créez un segment utilisateur qui correspond à votre base d'utilisateurs la plus fidèle et la plus cohérente. Un exemple de segment pour définir vos meilleurs utilisateurs est affiché ci-dessous.

!\[Définir les meilleurs utilisateurs\]\[1\]

De plus, vous n'aurez pas à continuer à mettre à jour ce segment, que les utilisateurs qui passent ou ne respectent pas les restrictions de la campagne seront ciblés ou rejetés en conséquence.

{% alert note %}
L'exemple ci-dessus segmente les utilisateurs par utilisation générale de l'application. Dans la plupart des cas, la collection totale de filtres nécessaires à la définition de votre segment utilisateur haut de gamme sera largement définie par les spécificités de votre application.
{% endalert %}

## Étape 2 : Atteignez vos meilleurs utilisateurs

### Faites que vos utilisateurs se sentent appréciés

Rendez vos utilisateurs appréciés en les remerciant pour leur fidélité et leur dévouement à votre application. Donnez à vos utilisateurs plus de raisons de revenir à votre application pour encourager d'autres activités. Cela peut prendre la forme d'offres spéciales ou de bonus exclusivement pour vos meilleurs utilisateurs.

Les récompenses inattendues peuvent être plus efficaces pour encourager la poursuite des actions des utilisateurs que si vous leur aviez promis dès le début!

!\[Brats Push\]\[2\]

### Garder une trace de vos résultats

Gardez une trace des ouvertures afin de vous assurer que vous ciblez la bonne collection d'utilisateurs avec le type de message optimal. De plus, gardez une trace de toutes les opt-outs de push et soyez prudent de perdre ces utilisateurs cruciaux.
[1]: {% image_buster /assets/img_archive/define_top_users.png %} "Définissez vos meilleurs utilisateurs" [2]: {% image_buster /assets/img/congratulations_push.jpg %}