---
nav_title: "Rapports d'entonnoir"
article_title: Rapports d’entonnoir pour campagnes et Canvas
page_order: 6
page_type: reference
description: "Cette page présente les avantages des rapports d'entonnoir, la manière de les mettre en place et d'interpréter votre rapport."
tool: Reports
---

# Rapports d'entonnoir

> Le rapport d’entonnoir offre un rapport visuel qui vous permet d’analyser les parcours de vos clients après la réception d’une campagne ou d’un Canvas. ![Rapport d'entonnoir 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si votre campagne ou votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre de façon plus granulaire comment les différentes variantes ont impacté le tunnel de conversion, et vous pourrez l’optimiser en fonction de ces données.

![Rapport d'entonnoir 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Mise en place de rapports d'entonnoirs

![Rapport d'entonnoir 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Vous pouvez exécuter des rapports d'entonnoir pour les campagnes actives existantes et les Canevas. Ces rapports présentent une série d'événements que le destinataire d'une campagne traverse sur une période de 1 à 30 jours à partir de la date de son entrée dans le Canvas ou la campagne. Un utilisateur est considéré comme converti pour une étape dans l’entonnoir s’il exécute l’événement dans l’ordre spécifié.

Les rapports d’entonnoir sont disponibles dans les emplacements suivants du tableau de bord :

- La page **Analyse/analytique de la campagne** (si utilisée comme une campagne spécifique)
- La page **Détails du canvas** pour un canvas spécifique, en sélectionnant le bouton **Analyser les variantes.**  

{% alert important %}
Les rapports d'entonnoir ne sont pas disponibles pour les [campagnes API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Étape 1 : Sélectionner une plage de dates

Vous pouvez sélectionner une période pour votre rapport (au cours des six derniers mois), et affiner les données pour voir les utilisateurs qui, en entrant dans la campagne ou le Canvas, ont terminé les événements de l'entonnoir dans une fenêtre définie (maximum de 30 jours). Dans l'exemple suivant, votre entonnoir rechercherait les utilisateurs qui ont reçu cette campagne ou ce Canvas au cours des sept derniers jours et qui ont terminé l'entonnoir dans les trois jours.

{% alert note %}
Si vous avez fixé la fenêtre d'achèvement de l'entonnoir à un jour, l'événement de l'entonnoir doit se produire dans les 24 heures suivant la réception du message. Toutefois, si vous sélectionnez plusieurs jours, la fenêtre de timing est comptée comme des jours calendaires dans le fuseau horaire de l'entreprise.
{% endalert %}

![Rapport d'entonnoir 5]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Étape 2 : Sélectionner les événements pour les étapes d’entonnoir

Pour chaque rapport d’entonnoir, le premier événement est la réception de votre message par l’utilisateur. Les événements que vous choisissez ensuite feront passer par l’entonnoir les utilisateurs qui ont effectué ces événements, ainsi que les événements précédents. Les événements de rapport entonnoir pour les entonnoirs de campagnes et de Canvas permettent de démarrer la session, d’effectuer un achat et d’organiser des événements personnalisés, alors que seuls les entonnoirs de campagne ont des événements d’engagement sur les messages.

![Rapport d'entonnoir 3]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Les rapports d’entonnoir vous permettent de comparer le succès de vos messages au-delà des événements de conversion ou des événements d’engagement que vous avez initialement configurés. Donc s’il y a un événement de conversion que vous avez oublié au départ, vous pouvez quand même suivre les conversions pour cet événement en utilisant un entonnoir.

Par exemple, si vous sélectionnez une fenêtre de temps de 14 jours pour le rapport, suivie des événements `Added to cart` et `Made purchase`, vous verrez le nombre d’utilisateurs qui ont mis dans le panier dans les 14 jours suivant la réception du message et le nombre d’utilisateurs qui ont mis dans le panier, puis finalisé un achat dans les 14 jours suivant la réception de la campagne.

Par exemple, vous pouvez voir le pourcentage d’utilisateurs convertis après avoir cliqué sur un e-mail. Pour le calculer, vous pouvez créer un rapport dans lequel le second événement est le clic sur votre e-mail et le troisième événement est votre événement de conversion.

Après avoir sélectionné **Créer un rapport**, le rapport d'entonnoir peut prendre plusieurs minutes pour être généré. Pendant cette période, vous pouvez quitter le rapport pour aller sur d’autres pages du tableau de bord. Vous recevrez une notification sur le tableau de bord quand le rapport sera prêt.

## Interprétation de votre rapport d’entonnoir

Dans votre rapport d’entonnoir, vous pouvez comparer directement le groupe de contrôle aux variantes que vous avez configurées. Chaque événement consécutif indiquera quel pourcentage des utilisateurs précédents a terminé cette action et converti en passant par l’entonnoir.

### Composants du rapport entonnoir

- **Axe horizontal**: Affiche le pourcentage de destinataires des messages qui ont effectué ces actions. 
- **Graphique** : Affiche le nombre d'envois reçus, le nombre d'utilisateurs ayant effectué les actions précédentes, ainsi que l'action que vous avez choisie, le taux de conversion et le pourcentage de changement par rapport au contrôle.
- **Option de régénération** : Vous permet de régénérer votre rapport et indique quand le rapport actuel a été généré pour la dernière fois. 
- **Variantes**: Les rapports d’entonnoir permettent de définir jusqu’à 8 variantes et un groupe de contrôle. Par défaut, le **graphique** n'affiche que trois variantes. Pour en voir davantage, vous pouvez sélectionner manuellement le reste des variantes.

![Rapport d'entonnoir 4]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Pour les campagnes comportant plusieurs variantes**: Braze affichera un tableau avec les indicateurs pour chaque événement et variante et le pourcentage de changement par rapport au contrôle. Le taux de conversion est le nombre d'utilisateurs ayant réalisé l'événement (et les suivants) par destinataire du message.

**Pour les campagnes avec rééligibilité**: Si un utilisateur reçoit la campagne plusieurs fois dans la fenêtre du rapport, Braze déterminera s’il doit être inclus dans l’entonnoir en fonction des actions que cet utilisateur a effectué après avoir reçu la campagne pour la première fois dans la fenêtre de temps.
- Notez qu'il peut y avoir un écart entre les valeurs de conversion de l'entonnoir et les valeurs de conversion standard, car les utilisateurs peuvent se convertir plus d'une fois avec la rééligibilité, mais les rapports d'entonnoir ne convertiront qu'une seule fois au maximum, même si un utilisateur effectue l'événement plus d'une fois. 

**Pour les campagnes multivariées avec rééligibilité** : Si un utilisateur reçoit plusieurs variantes de la campagne pendant la fenêtre du rapport, Braze déterminera s’il doit être inclus dans l’entonnoir de variante en fonction des actions que cet utilisateur a effectué après avoir reçu la variante de la campagne pour la première fois. Cela signifie qu'un même utilisateur pourrait compter pour plusieurs variantes différentes s'il a reçu plusieurs variantes pendant la fenêtre temporelle de l'entonnoir.

