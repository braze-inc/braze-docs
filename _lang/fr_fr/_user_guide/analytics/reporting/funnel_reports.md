---
nav_title: "Rapports d'entonnoir"
article_title: "Rapports d'entonnoir pour les campagnes et les toiles"
page_order: 6
page_type: reference
description: "Cette page présente les avantages des rapports d'entonnoir, la manière de les mettre en place et d'interpréter votre rapport."
tool: Reports
---

# Rapports d'entonnoir

> Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours de vos clients après avoir reçu une campagne ou un Canvas. !Rapport d'entonnoir 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si votre campagne ou Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pouvez comprendre comment les différentes variantes ont eu un impact sur l'entonnoir de conversion à un niveau plus granulaire et optimiser en fonction de ces données.

!Rapport d'entonnoir 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Mise en place de rapports d'entonnoirs

!Rapport d'entonnoir 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Vous pouvez exécuter des rapports d'entonnoir pour les campagnes actives existantes et les Canevas. Ces rapports présentent une série d'événements que le destinataire d'une campagne traverse sur une période de 1 à 30 jours à partir de la date de son entrée dans le Canvas ou la campagne. Un utilisateur est considéré comme converti à travers une étape de l'entonnoir s'il effectue l'événement dans l'ordre spécifié.

Les rapports d'entonnoir sont disponibles aux emplacements suivants du tableau/localisation :

- La page **Analyse/analytique de la campagne** (si utilisée comme une campagne spécifique)
- La page **Détails du canvas** pour un canvas spécifique, en sélectionnant le bouton **Analyser les variantes.**  

{% alert important %}
Les rapports d'entonnoir ne sont pas disponibles pour les [campagnes API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Étape 1 : Sélectionnez une plage de dates

Vous pouvez sélectionner une période pour votre rapport (au cours des six derniers mois), et affiner les données pour voir les utilisateurs qui, en entrant dans la campagne ou le Canvas, ont terminé les événements de l'entonnoir dans une fenêtre définie (maximum de 30 jours). Dans l'exemple suivant, votre entonnoir rechercherait les utilisateurs qui ont reçu cette campagne ou ce Canvas au cours des sept derniers jours et qui ont terminé l'entonnoir dans les trois jours.

{% alert note %}
Si vous avez fixé la fenêtre d'achèvement de l'entonnoir à un jour, l'événement de l'entonnoir doit se produire dans les 24 heures suivant la réception du message. Toutefois, si vous sélectionnez plusieurs jours, la fenêtre temporelle est comptée comme des jours calendaires dans le fuseau horaire de l'entreprise.
{% endalert %}

Rapport d'entonnoir pour un canvas avec "Last 7 Days" sélectionné dans le menu déroulant.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Étape 2 : Sélectionnez des événements pour les étapes de l'entonnoir

Pour chaque rapport d'entonnoir, le premier événement est le moment où l'utilisateur reçoit votre message. À partir de là, les événements ultérieurs que vous choisissez entonnent le nombre d'utilisateurs qui ont effectué ces événements, ainsi que les événements précédents. 

#### Événements disponibles pour le rapport d'entonnoir

| Vous avez reçu un message de la part d'une personne qui a commencé une session, a effectué un achat, a réalisé un événement custom, a envoyé un message à l'occasion d'un événement d'engagement.
| Canvas | Démarrage d'une session, achat, événement personnalisé, étape du canvas, interaction avec l'étape du canevas
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
L'événement de rapport **Interacted with Step** ne peut être utilisé qu'avec les étapes de Canvas qui utilisent les canaux d'envoi d'e-mails ou de messages push.
{% endalert %}

Rapport d'entonnoir pour un canvas avec une liste déroulante des événements de rapport disponibles.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Les rapports d'entonnoir vous permettent de comparer le succès de vos messages au-delà des seuls événements de conversion ou d'engagement des messages que vous avez initialement mis en place. Ainsi, s'il y a un événement de conversion que vous n'avez pas ajouté initialement, vous pouvez toujours suivre les conversions pour cet événement à l'aide d'un entonnoir.

Par exemple, si vous sélectionnez une fenêtre de rapport de 14 jours, suivie des événements `Added to cart` et `Made purchase`, vous verrez à la fois le nombre d'utilisateurs qui ont ajouté au panier dans les 14 jours suivant la réception du message et le nombre d'utilisateurs qui ont ajouté au panier puis effectué un achat dans les 14 jours suivant la réception de la campagne.

Autre exemple, vous souhaitez peut-être connaître le pourcentage d'utilisateurs qui ont converti sur un e-mail après avoir cliqué dessus. Pour calculer cela, vous pourriez créer un rapport où le deuxième événement est le fait de cliquer sur votre e-mail et le troisième événement est la réalisation de votre événement de conversion.

Après avoir sélectionné **Créer un rapport**, le rapport d'entonnoir peut prendre plusieurs minutes pour être généré. Pendant ce temps, vous pouvez naviguer entre le rapport et d'autres pages du tableau de bord. Vous recevrez une notification dans le tableau de bord lorsque votre rapport sera prêt.

## Interpréter votre rapport d'entonnoir

Dans votre rapport d'entonnoir, vous pouvez directement comparer le groupe de contrôle avec les variantes que vous avez mises en place. Chaque événement consécutif montrera quel pourcentage des utilisateurs précédents a effectué cette action et s'est converti à travers l'entonnoir.

### Composants du rapport d'entonnoir

- **Axe horizontal**: Affiche le pourcentage de destinataires du message qui ont effectué ces actions. 
- **Graphique**: Affiche le nombre d'envois reçus, le nombre d'utilisateurs ayant effectué les actions précédentes, ainsi que l'action que vous avez choisie, le taux de conversion et le pourcentage de changement par rapport au contrôle.
- **Option de régénération**: Vous permet de régénérer votre rapport et indique quand le rapport actuel a été généré pour la dernière fois. 
- **Variantes**: Désigné par des colonnes colorées, le rapport d'entonnoir permet d'inclure jusqu'à 8 variantes et un groupe de contrôle. Par défaut, le **graphique** n'affiche que trois variantes. Pour en voir plus, vous pouvez sélectionner manuellement le reste des variantes.

\![Graphique du rapport d'entonnoir.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Pour les campagnes comportant plusieurs variantes**: Braze affichera un tableau avec les indicateurs pour chaque événement et variante et le pourcentage de changement par rapport au contrôle. Le taux de conversion est le nombre d'utilisateurs ayant réalisé l'événement (et les suivants) par destinataire du message.

**Pour les campagnes avec rééligibilité**: Si un utilisateur reçoit la campagne plus d'une fois dans la fenêtre temporelle du rapport, Braze déterminera si l'utilisateur doit être inclus dans l'entonnoir sur la base des actions que cet utilisateur a effectuées après la première fois qu'il a reçu la campagne dans la fenêtre temporelle.
- Notez qu'il peut y avoir un écart entre les valeurs de conversion de l'entonnoir et les valeurs de conversion standard, car les utilisateurs peuvent se convertir plus d'une fois avec la rééligibilité, mais les rapports d'entonnoir ne convertiront qu'une seule fois au maximum, même si un utilisateur effectue l'événement plus d'une fois. 

**Pour les campagnes multivariées avec rééligibilité**: Si un utilisateur reçoit plusieurs variantes de la campagne pendant la fenêtre temporelle du rapport, Braze déterminera s'il doit être inclus dans l'entonnoir de variante en fonction des actions que cet utilisateur a effectuées après la première fois qu'il a reçu la variante de la campagne. Cela signifie qu'un même utilisateur pourrait compter pour plusieurs variantes différentes s'il a reçu plusieurs variantes pendant la fenêtre temporelle de l'entonnoir.

{% alert important %}
Les utilisateurs orphelins ne sont pas suivis dans les rapports d'entonnoirs. Lorsqu'un utilisateur anonyme entre dans un canvas ou une campagne et qu'il est ensuite identifié par la méthode `changeUser()`, son ID Braze change. Les rapports d'entonnoir ne suivent que les événements de suivi qui correspondent à l'ID de l'utilisateur au moment de l'entrée et ne tiennent pas compte des événements effectués par l'utilisateur après son changement d'ID. Cela signifie que les événements de conversion effectués par l'utilisateur après avoir été identifié ne seront pas inclus dans le rapport d'entonnoir.
{% endalert %}

