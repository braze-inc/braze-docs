---
nav_title: Ouvertures influencées
article_title: Ouvertures influencées
page_order: 7
page_type: reference
description: "Cet article de référence explique ce que sont les Ouvertures Influencées et comment vous pouvez les suivre pour obtenir des informations plus précises sur les effets de vos campagnes de notifications push."
channel: push

---

# Ouvertures influencées

> Les notifications push sont un bon moyen de capter l’attention des utilisateurs et d’améliorer l’engagement. C’est souvent via des ouvertures directes que les utilisateurs cliquent sur la notification et sont envoyés vers l’appli. Cependant, le comportement des utilisateurs qui ne cliquent pas sur le message peut toujours être influencé par vos campagnes de notification push. Braze fournit des données sur les ouvertures influencées pour fournir un niveau de détails plus élevé sur l’effet de vos campagnes de notification push. 

Essentiellement, les ouvertures influencées mesurent le nombre d’utilisateurs qui ouvrent l’application après avoir reçu une notification sans cliquer sur la notification. Comme il n’y a pas d’action directe reliant la notification à l’ouverture de l’appli, une ouverture influencée est comptée si l’utilisateur ouvre l’application dans les 30 minutes suivant la notification push, ou moins de la moitié du temps moyen depuis la dernière session de l’utilisateur.

À titre d’exemple, disons que vous envoyez une notification push aux utilisateurs d’une application de messagerie et que vous avez un groupe d’utilisateurs qui ne cliquent pas sur la notification. Si un utilisateur qui ouvre l’application normalement 30 fois par jour ouvre l’application 6 heures après avoir reçu la notification push, on considérera que la notification push a très peu influencé l’ouverture, voire pas du tout. Cependant, si un utilisateur qui utilise normalement l’application une fois par mois ouvre l’application 6 heures après avoir reçu la notification push, l’ouverture aura beaucoup plus de chances d’être comptée comme une ouverture influencée. 

Ce n’est pas la même chose que de définir les ouvertures d’application en tant qu’événement de conversion d’une campagne de notification push. Pour les conversions, toutes les ouvertures de la fenêtre de conversion seront attribuées à la campagne. Les ouvertures influencées définissent une fenêtre temporelle et un crédit d’attribution en fonction du comportement d’un utilisateur individuel.

## Détails de la campagne

Les ouvertures influencées sont ajoutées aux ouvertures directes d’une campagne pour donner un nombre total de visites. Vous pouvez le voir sur la page **Détails** d’une campagne de notification push. Les ouvertures totales et les ouvertures directes sont affichées dans les sections **Performance de message** et **Historique des Performances**. Les ouvertures influencées sont la différence entre les deux mesures.

![Statistiques sur les ouvertures influencées sur la page Campaign Details (Détails de la campagne) d’une campagne][1]

Pour plus d’informations sur le suivi, consultez la section Suivi des conversions dans nos [Bonnes pratiques pour les notifications push][bp].

[bp]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[1]: {% image_buster /assets/img_archive/Influenced_Opens2.png %}
