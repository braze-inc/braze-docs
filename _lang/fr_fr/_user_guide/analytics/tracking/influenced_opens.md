---
nav_title: Ouvertures influencées
article_title: Ouvertures influencées
page_order: 7
page_type: reference
description: "Cet article de référence explique les ouvertures influencées et comment vous pouvez les suivre pour fournir un niveau de détail plus riche à vos campagnes push."
channel: push

---

# Ouvertures influencées

> Lorsqu'un utilisateur sélectionne une notification push et est envoyé à votre application, Braze l'enregistre comme une ouverture directe. Lorsque les utilisateurs ne sélectionnent pas la notification mais peuvent encore être influencés par la notification push, Braze l'enregistre comme une ouverture influencée. Ceci permet d'obtenir un niveau de détail plus riche sur l'effet de vos campagnes de notifications push.

## Fonctionnement

À leur base, les ouvertures influencées mesurent le nombre d'utilisateurs qui ouvrent l'application après avoir reçu une notification sans sélectionner la notification. Parce qu'il n'y a pas d'action directe reliant la notification à l'ouverture de l'application, une ouverture influencée est enregistrée si l'utilisateur ouvre l'application moins de trente minutes après avoir reçu la notification push ou moins de la moitié du temps moyen écoulé depuis la dernière session de cet utilisateur.

Par exemple, disons que vous envoyez une notification push à vos utilisateurs d'application. Si un utilisateur qui ouvre normalement l'application 30 fois par jour ouvre votre application six heures après avoir reçu la notification push, la notification push reçoit peu ou pas de crédit pour avoir influencé l'ouverture. Cependant, si un utilisateur qui utilise normalement l'application une fois par mois ouvre l'application six heures après avoir reçu la notification push, l'ouverture a beaucoup plus de chances d'être comptée comme une ouverture influencée. 

Ce n’est pas la même chose que de définir les ouvertures d’application en tant qu’événement de conversion d’une campagne de notification push. Pour les conversions, toutes les ouvertures de la fenêtre de conversion seront attribuées à la campagne. Les ouvertures influencées définissent une fenêtre temporelle et un crédit d’attribution en fonction du comportement d’un utilisateur individuel.

## Affichage des ouvertures influencées d'une campagne

Les ouvertures influencées sont ajoutées aux ouvertures directes d’une campagne pour donner un nombre total de visites. Ceci est affiché sur la page **Analytique de campagne** d'une campagne push. Le nombre total d'ouvertures et d'ouvertures directes est affiché dans les sections performance du message et **Performance Historique**. Les ouvertures influencées sont la différence entre les deux mesures.

![Influencé ouvre des statistiques sur la page Détails de la campagne pour une campagne]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Pour plus d'informations sur le suivi des ouvertures, consultez la section correspondante de nos [bonnes pratiques pour les notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

