---
nav_title: Ouvertures influencées
article_title: Ouvertures influencées
page_order: 7
page_type: reference
description: "Cet article de référence explique les ouvertures influencées et la manière dont vous pouvez les suivre pour obtenir un niveau de détail plus riche dans vos campagnes push."
channel: push

---

# Ouvertures influencées

> Lorsqu'un utilisateur sélectionne une notification push et qu'il est envoyé vers votre appli, Braze l'enregistre comme une ouverture directe. Lorsque les utilisateurs ne sélectionnent pas la notification mais peuvent tout de même être influencés par la notification push, Braze l'enregistre comme une ouverture influencée. Cela permet d'obtenir un niveau de détail plus riche sur l'effet de vos campagnes de push.

## Comment cela fonctionne-t-il ?

À la base, les ouvertures influencées mesurent le nombre d'utilisateurs qui ouvrent l'application après avoir reçu une notification sans la sélectionner. Comme il n'y a pas d'action directe liant la notification à l'ouverture de l'application, une ouverture influencée est enregistrée si l'utilisateur ouvre l'application moins de trente minutes après avoir reçu la notification push ou moins de la moitié du temps moyen écoulé depuis la dernière session de l'utilisateur.

Par exemple, disons que vous envoyez une notification push aux utilisateurs de votre appli. Si un utilisateur qui ouvre normalement l'application 30 fois par jour ouvre votre application six heures après avoir reçu le push, ce dernier n'a que peu ou pas d'influence sur l'ouverture de l'application. En revanche, si un utilisateur qui utilise normalement l'application une fois par mois l'ouvre six heures après avoir reçu le push, l'ouverture a beaucoup plus de chances d'être comptabilisée comme une ouverture influencée. 

Cela diffère de la définition des ouvertures d'apps comme événement de conversion pour une campagne push. Pour les conversions, toutes les ouvertures dans la fenêtre de conversion seront attribuées à la campagne. Les ouvertures influencées définissent une fenêtre temporelle et un crédit d'attribution basés sur le comportement d'un utilisateur individuel.

## L'affichage de l'influence d'une campagne s'ouvre

Les ouvertures influencées sont ajoutées aux ouvertures directes d'une campagne pour donner un nombre d'ouvertures totales. Elle est affichée sur la page d' **analyse/analytique de campagne** d'une campagne push. Le nombre total d'ouvertures et les ouvertures directes sont indiqués dans les sections sur la performance des messages et la **performance historique.**  Les ouvertures influencées représentent la différence entre les deux mesures.

!L'influence ouvre les statistiques sur la page des détails d'une campagne]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Pour plus d'informations sur le suivi des ouvertures, consultez la section sur le suivi des conversions de nos [meilleures pratiques pour le push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)

