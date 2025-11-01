---
nav_title: Campagnes auprès des utilisateurs actifs
article_title: Campagnes auprès des utilisateurs actifs
page_order: 0.5
page_type: tutorial
description: "Cet article pratique décrit les avantages des campagnes d'utilisateurs actifs dans le tableau de bord de Braze, ainsi que les étapes à suivre pour en créer et en implémenter une."
tool: 
  - Campaigns

---

# Campagnes auprès des utilisateurs actifs

> Identifiez vos utilisateurs actifs pour vous aider à faire des campagnes sur mesure et à récompenser ceux qui fréquentent votre plateforme. 

Tendre la main aux utilisateurs déjà actifs de votre application peut être un outil puissant pour aider à créer un public dévoué d'utilisateurs réguliers de l'application. Un peu de personnalisation de la reconnaissance de vos power users peut les transformer en évangélistes de votre appli.

Vous pouvez également consulter notre [cours d'apprentissage Braze](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sur la stratégie marketing pour l'e-mail et les campagnes basées sur le cycle de vie recommandées !

## Comprendre les utilisateurs actifs

Braze définit un "utilisateur actif" pour une période donnée comme tout utilisateur ayant une session au cours de cette période.

Si un utilisateur perd sa connexion, nous mettrons les données de session en cache localement et les téléchargerons lorsque l'utilisateur retrouvera une connexion réseau. Ces sessions seront également prises en compte dans le décompte des utilisateurs actifs. De plus, si votre application dispose d'un processus d'enregistrement, Braze comptera tous les utilisateurs comme actifs - enregistrés ou non.

Si vous définissez des ID pour identifier les utilisateurs, lorsqu'un nouvel utilisateur se connecte, il est compté comme un utilisateur actif distinct. Les utilisateurs qui sont mis à jour via l'API seront également comptés comme un utilisateur actif dans la période de temps où ils sont mis à jour.

## Étape 1 : Identifier vos meilleurs utilisateurs

À l'aide de notre sélection de filtres, créez un segment d'utilisateurs qui, selon vous, englobe votre base d'utilisateurs la plus fidèle et la plus cohérente. L'exemple de segmentation suivant définit les principaux utilisateurs.

\![]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

En outre, vous n'aurez pas besoin de continuer à mettre à jour ce segment, car les utilisateurs qui entrent ou sortent des restrictions de la campagne seront ciblés ou écartés en conséquence.

{% alert note %}
L'exemple précédent segmente les utilisateurs en fonction de l'utilisation générale de l'app. Dans la plupart des cas, la collection totale de filtres nécessaires pour définir votre segment d'utilisateurs supérieur sera largement définie par les spécificités de votre application.
{% endalert %}

## Étape 2 : Contactez vos principaux utilisateurs

### Faites en sorte que vos utilisateurs se sentent appréciés

Faites en sorte que vos utilisateurs se sentent appréciés en les remerciant de leur fidélité et de leur dévouement à votre application. Donnez à vos utilisateurs plus de raisons de revenir sur votre application pour les encourager à poursuivre leur activité. Cela peut prendre la forme d'offres spéciales ou de bonus réservés à vos meilleurs utilisateurs. 

Les récompenses inattendues peuvent être plus efficaces pour encourager les utilisateurs à poursuivre leurs actions que si vous les aviez promises dès le départ !

\![Une campagne à l'étape Composer avec une notification riche iOS qui se lit comme suit : "Merci encore d'avoir fait vos achats chez nous ! Pour vous remercier, nous vous offrons la livraison gratuite lors de votre prochain achat".]({% image_buster /assets/img/congratulations_push.jpg %})

### Suivez vos résultats

Suivez les ouvertures pour vous assurer que vous ciblez la bonne collection d'utilisateurs avec le type de message optimal. En outre, gardez une trace des éventuels abonnements push et prenez garde à ne pas perdre ces utilisateurs cruciaux.

