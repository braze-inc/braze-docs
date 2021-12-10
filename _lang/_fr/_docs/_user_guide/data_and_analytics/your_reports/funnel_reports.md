---
nav_title: Rapports de l'entonnoir
article_title: Rapports d'entonnoirs pour les campagnes et les toiles
page_order: 6
page_type: Référence
description: "Cet article de référence couvre les avantages des rapports sur les entonnoirs, la façon de les mettre en place, ainsi que la façon d'interpréter votre rapport."
tool: Rapports
---

# Rapports d'entonnoirs pour les campagnes et les toiles

> Cet article de référence explique comment utiliser les Rapports sur les entonnoirs pour analyser les trajets que vos clients effectuent après avoir reçu une campagne ou un Canvas. !\[Funnel Report 2\]\[2\]{: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Les rapports sur les entonnoirs offrent un rapport visuel qui vous permet d'analyser les trajets que vos clients effectuent après avoir reçu une campagne ou un Canvas. Si votre campagne ou Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pouvez comprendre comment les différentes variantes ont influencé l'entonnoir de conversion à un niveau plus granulaire et optimiser en fonction de ces données.

!\[Funnel Report 1\]\[1\]{: style="max-width:80%;"}

## Configuration du rapport de l'entonnoir

!\[Funnel Report 5\]\[5\]{: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Vous pouvez exécuter des rapports sur les entonnoirs pour les campagnes actives existantes et les canvases. Ces rapports montrent une série d'événements que le bénéficiaire de la campagne poursuit sur une période de 1 à 30 jours à compter de la date de réception du message. Un utilisateur est considéré comme converti à travers une étape dans l'entonnoir s'il effectue l'événement dans l'ordre spécifié.

Le rapport de l'entonnoir est disponible à partir des emplacements suivants dans le tableau de bord :

- La page **Analyses de campagne** pour une campagne spécifique
- La page **Détails sur le canevas** pour une toile spécifique, via le bouton **Analyser les variantes**

{% alert important %}
Les rapports sur les entonnoirs ne sont pas disponibles pour les campagnes déclenchées par l'API.
{% endalert %}

### Étape 1 : Sélectionnez une plage de dates

Vous pouvez sélectionner une période de temps pour votre rapport (au cours des 6 derniers mois), et affiner les données pour voir les utilisateurs qui, à l'entrée de la campagne ou de Canvas, a terminé les événements d'entonnoir dans une fenêtre fixe (maximum de 30 jours). Dans l'exemple ci-dessous, votre entonnoir chercherait les utilisateurs qui ont reçu cette campagne ou Canvas dans les 7 derniers jours et qui ont terminé l'entonnoir dans les 3 jours.

{% alert note %}
Si vous réglez la fenêtre pour compléter l'entonnoir à 1 jour, l'événement de l'entonnoir doit avoir lieu dans les 24 heures suivant la réception du message. Cependant, si vous sélectionnez plusieurs jours, la fenêtre de chronométrage est alors comptée comme jours de calendrier dans le fuseau horaire de la société.
{% endalert %}

!\[Funnel Report 5\]\[6\]{: style="max-width:90%;"}

### Étape 2 : Sélectionnez les événements pour les étapes de l'entonnoir

Pour chaque rapport d'entonnoir, le premier événement est lorsque l'utilisateur reçoit votre message. À partir de là, les événements suivants que vous choisissez entonnoir le nombre d'utilisateurs qui ont effectué ces événements, ainsi que les événements précédents. Les événements de rapport de l’entonnoir pour la campagne et les entonnoirs de Canvases permettent de démarrer la session, faire un achat et des événements personnalisés, alors que les entonnoirs de campagne ne comprennent que les événements de participation aux messages.

!\[Funnel Report 3\]\[3\]{: style="max-width:80%;"}

Les rapports d'entonnoir vous permettent de comparer le succès de vos messages au-delà des événements de conversion ou des événements d'engagement de messages que vous avez initialement mis en place. Donc, s’il y a un événement de conversion que vous n’avez pas ajouté initialement, vous pouvez toujours suivre les conversions pour cet événement en utilisant un entonnoir.

Par exemple, si vous sélectionnez une période de 14 jours, suivi des événements `Ajoutés au panier` et `Achat Made`, vous verrez à la fois le nombre d'utilisateurs qui ont ajouté au panier dans les 14 jours suivant la réception du message et le nombre d'utilisateurs qui ont ajouté au panier et ont ensuite effectué un achat dans les 14 jours suivant la réception de la campagne.

Comme autre exemple, vous pouvez vouloir voir le pourcentage d'utilisateurs qui ont converti sur un e-mail après avoir cliqué dessus. Pour calculer cela, vous pouvez créer un rapport où le deuxième événement cliquera sur votre adresse e-mail et le troisième événement effectuera votre événement de conversion.

Après avoir cliqué sur **Rapport de construction**, le rapport d'entonnoir peut prendre plusieurs minutes. Pendant cette période, vous pouvez vous éloigner du rapport vers d'autres pages du tableau de bord. Vous recevrez une notification dans le tableau de bord lorsque votre rapport sera prêt.

## Interprétation de votre rapport d'entonnoir

Dans votre rapport d'entonnoir, vous pouvez comparer directement le groupe de contrôle avec les variantes que vous avez mises en place. Chaque événement consécutif montrera quel pourcentage des utilisateurs précédents ont terminé cette action et converti à travers l'entonnoir.

### Composants de rapport de l'entonnoir

- __Axe horizontal__: Affiche le pourcentage de destinataires du message qui ont effectué ces actions.
- __Graphique__: Affiche le nombre de messages reçus, le nombre d'utilisateurs qui ont effectué les actions précédentes ainsi que l'action que vous avez choisie, le taux de conversion et le pourcentage de changement de contrôle.
- __Option de génération__: vous permet de régénérer votre rapport et vos notes lorsque le rapport actuel a été généré pour la dernière fois.
- __Variantes__: Désignées par des colonnes colorées, le rapport en entonnoir permet jusqu'à 8 variantes et un groupe de contrôle. Par défaut, le graphique ____ n'affichera que trois variantes. Pour en voir plus, vous pouvez sélectionner manuellement le reste des variantes.

!\[Rapport Funnel 4\]\[4\]

__Pour les campagnes avec plusieurs variantes__: Braze affichera un tableau qui affiche les métriques pour chaque événement et variante, ainsi que le pourcentage de changement du contrôle. Le taux de conversion est le nombre d'utilisateurs qui ont effectué l'événement (et ceux qui ont suivi) par destinataire.

__Pour les campagnes avec rééligibilité__: Si un utilisateur reçoit la campagne plus d'une fois dans la fenêtre de temps du rapport, Braze déterminera si l'utilisateur doit être inclus dans l'entonnoir en fonction des actions prises par cet utilisateur après la première fois qu'il a reçu la campagne dans la fenêtre de temps.

__Pour les campagnes multivariantes avec rééligibilité__: Si un utilisateur reçoit plusieurs variantes de la campagne pendant la fenêtre de temps du rapport, Braze déterminera s'ils doivent être inclus dans l'entonnoir de variante en fonction des actions prises par cet utilisateur après la première fois qu'ils ont reçu la variante de la campagne. Cela signifie que le même utilisateur pourrait compter pour plusieurs variantes différentes s'il recevait plusieurs variantes dans la fenêtre de temps de l'entonnoir.
[1]:{% image_buster /assets/img/funnel_report/funnel_report1.jpg %} [2]:{% image_buster /assets/img/funnel_report/funnel_report2.png %} [3]:{% image_buster /assets/img/funnel_report/funnel_report3 ng %} [4]:{% image_buster /assets/img/funnel_report/funnel_report4.jpg %} [5]:{% image_buster /assets/img/funnel_report/canvas_campaign.png %} [6]:{% image_buster /assets/img/funnel_report/funnel_report5.png %}
