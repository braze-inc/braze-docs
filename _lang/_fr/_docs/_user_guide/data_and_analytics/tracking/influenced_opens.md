---
nav_title: Ouvertures influencées
article_title: Ouvertures influencées
page_order: 7
page_type: Référence
description: "Cet article de référence explique Influenced Ouens et comment vous pouvez les suivre pour fournir un niveau de détail plus riche dans l'effet de vos campagnes de push."
channel: Pousser
---

# Ouvertures influencées

Les notifications push sont un bon moyen d'attirer l'attention des utilisateurs et d'augmenter leur engagement. Souvent, cela passe par des ouvertures directes lorsque les utilisateurs cliquent sur la notification et sont envoyés à l'application. Cependant, le comportement des utilisateurs qui ne cliquent pas sur le message peut toujours être influencé par vos campagnes de push. Braze fournit des données sur Influenced Ouens pour fournir un niveau de détail plus riche dans l'effet de vos campagnes de push.

À leur base, les Ouvres Influencés mesurent le nombre d'utilisateurs qui ouvrent l'application après avoir reçu une notification sans cliquer sur la notification. Parce qu'il n'y a pas d'action directe liant la notification à l'application ouverte, un ouvert influencé est attribué si l'utilisateur ouvre l'application 30 minutes depuis que l'utilisateur a reçu la notification push, ou moins de la moitié du temps moyen depuis la dernière session de l'utilisateur.

Par exemple, dites que vous envoyez un push aux utilisateurs d'une application de messagerie, et vous avez un groupe d'utilisateurs qui ne cliquent pas à travers la notification. Si un utilisateur qui ouvre normalement l'application 30 fois par jour ouvre l'application 6 heures après avoir reçu le push, la poussée aurait peu à peu de crédit pour avoir influencé les ouverts. Cependant, si un utilisateur qui utilise normalement l'application une fois par mois ouvre l'application 6 heures après avoir reçu le push, l'ouverture, aurait une bien meilleure chance d'être compté comme un ouvert influencé. Cela diffère de la configuration de l'application s'ouvre comme un événement de conversion pour une campagne push. Pour les conversions, toutes les ouvertures dans la fenêtre de conversion seront attribuées à la campagne. Influencé Ouvre définit une fenêtre de temps et un crédit d'attribution en fonction du comportement d'un utilisateur individuel.

Les Ouvertures Influencées sont ajoutées aux ouvertures directes d'une campagne pour donner un certain nombre d'ouvertures totales. Ceci peut être vu sur la page Détails d'une campagne de push. Les ouvertures totales et les ouvertures directes sont affichées dans les sections Performance des messages et Performance historique. Les ouvertures influencées sont la différence entre les deux mesures.

!\[Influenced Open Details\]\[1\]

Pour plus d'informations sur les ouvertures de suivi, consultez la section de suivi des conversions de nos [meilleures pratiques pour pousser][bp].
[1]: {% image_buster /assets/img_archive/Influenced_Opens2.png %}

[bp]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
