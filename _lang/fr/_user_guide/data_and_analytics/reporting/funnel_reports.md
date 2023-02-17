---
nav_title: Rapports d'entonnoir
article_title: Rapports d’entonnoir pour campagnes et Canvas
page_order: 6
page_type: reference
description: "Cet article de référence décrit les avantages des rapports d’entonnoir, explique comment les configurer et comment interpréter les rapports."
tool: Rapports
---

# Rapports d’entonnoir pour campagnes et Canvas

> Cet article de référence explique comment utiliser les rapports d’entonnoir pour analyser les parcours de vos clients après la réception d’une campagne ou d’un Canvas. ![Rapport d’entonnoir 2][2]{: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Le rapport d’entonnoir offre un rapport visuel qui vous permet d’analyser les parcours de vos clients après la réception d’une campagne ou d’un Canvas. Si votre campagne ou votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre de façon plus granulaire comment les différentes variantes ont impacté l’entonnoir de conversion, et vous pourrez l’optimiser en fonction de ces données.

![Rapport d’entonnoir 1][1]{: style="max-width:80%;"}

## Configuration d’un rapport entonnoir

![Rapport d’entonnoir 5][5]{: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Vous pouvez exécuter des rapports d’entonnoir pour les campagnes et les Canvas actifs et existants. Ces rapports montrent une série d’événements par lesquels passe un destinataire de campagne sur une période de 1 à 30 jours à compter de la date à laquelle il a reçu le message. Un utilisateur est considéré comme converti pour une étape dans l’entonnoir s’il exécute l’événement dans l’ordre spécifié.

Les rapports d’entonnoir sont disponibles dans les emplacements suivants du tableau de bord :

- La page **Campaign Analytics (Analyse de campagne)** pour une campagne spécifique
- La page **Canvas Details (Détails Canvas)** pour un Canvas spécifique, via le bouton **Analyze Variants (Analyser les variantes)** 

{% alert important %}
Les rapports d’entonnoir ne sont pas disponibles pour les [campagnes API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Étape 1 : Sélectionner une plage de dates

Vous pouvez sélectionner une période pour votre rapport (dans les 6 derniers mois), et affiner les données pour voir les utilisateurs qui, en entrant dans la campagne ou le Canvas, ont terminé les événements d’entonnoir dans un délai défini (30 jours maximum). Dans l’exemple suivant, votre entonnoir rechercherait les utilisateurs qui ont reçu cette campagne ou Canvas au cours des 7 derniers jours et qui ont terminé l’entonnoir dans les 3 jours.

{% alert note %}
Si vous définissez la fenêtre d’accomplissement de l’entonnoir sur 1 jour, l’événement d’entonnoir doit avoir lieu dans les 24 heures suivant la réception du message. Cependant, si vous sélectionnez plusieurs jours, la fenêtre de timing est alors comptée comme jours calendaires dans le fuseau horaire de l’entreprise.
{% endalert %}

![Rapport d’entonnoir 5][6]{: style="max-width:90%;"}

### Étape 2 : Sélectionner les événements pour les étapes d’entonnoir

Pour chaque rapport d’entonnoir, le premier événement est la réception de votre message par l’utilisateur. Les événements que vous choisissez ensuite feront passer par l’entonnoir les utilisateurs qui ont effectué ces événements, ainsi que les événements précédents. Les événements de rapport entonnoir pour les entonnoirs de campagnes et de Canvas permettent de démarrer la session, d’effectuer un achat et d’organiser des événements personnalisés, alors que seuls les entonnoirs de campagne ont des événements d’engagement sur les messages.

![Rapport d’entonnoir 3][3]{: style="max-width:80%;"}

Les rapports d’entonnoir vous permettent de comparer le succès de vos messages au-delà des événements de conversion ou des événements d’engagement que vous avez initialement configurés. Donc s’il y a un événement de conversion que vous avez oublié au départ, vous pouvez quand même suivre les conversions pour cet événement en utilisant un entonnoir.

Par exemple, si vous sélectionnez une fenêtre de temps de 14 jours pour le rapport, suivie des événements `Ajouté au panier` et `A effectué un achat`, vous verrez le nombre d’utilisateurs qui ont mis dans le panier dans les 14 jours suivant la réception du message et le nombre d’utilisateurs qui ont mis dans le panier, puis finalisé un achat dans les 14 jours suivant la réception de la campagne.

Par exemple, vous pouvez voir le pourcentage d’utilisateurs convertis après avoir cliqué sur un e-mail. Pour le calculer, vous pouvez créer un rapport dans lequel le second événement est le clic sur votre e-mail et le troisième événement est votre événement de conversion.

Après avoir cliqué sur **Build Report (Générer le rapport)**, le rapport d’entonnoir peut mettre plusieurs minutes avant d’être créé. Pendant cette période, vous pouvez quitter le rapport pour aller sur d’autres pages du tableau de bord. Vous recevrez une notification sur le tableau de bord quand le rapport sera prêt.

## Interprétation de votre rapport d’entonnoir

Dans votre rapport d’entonnoir, vous pouvez comparer directement le groupe de contrôle aux variantes que vous avez configurées. Chaque événement consécutif indiquera quel pourcentage des utilisateurs précédents a terminé cette action et converti en passant par l’entonnoir.

### Composants du rapport entonnoir

- **Horizontal axis (Axe horizontal)**: Affiche le pourcentage de destinataires des messages qui ont effectué ces actions. 
- **Chart (Graphique)** : Affiche le nombre de messages reçus, le nombre d’utilisateurs ayant effectué les actions précédentes ainsi que l’action que vous avez choisie, le taux de conversion et le pourcentage d’écart par rapport au contrôle.
- **Regenerate Option (Option de régénération)**: Vous permet de régénérer votre rapport et note la date de la dernière exécution du rapport. 
- **Variants (Variantes)** : Les rapports d’entonnoir permettent de définir jusqu’à 8 variantes et un groupe de contrôle. Par défaut, le **chart (graphique)** ne montrera que trois variantes. Pour en voir davantage, vous pouvez sélectionner manuellement le reste des variantes.

![Rapport d’entonnoir 4][4]

**For campaigns with multiple variants (Pour les campagnes avec plusieurs variantes)**: Braze affiche un tableau qui affiche les métriques pour chaque événement et variante, ainsi que le pourcentage d’écart par rapport au contrôle. Le taux de conversion est le nombre d’utilisateurs qui ont effectué l’événement (et ceux qui suivent) par destinataires de message.

**For campaigns with re-eligibility (Pour les campagnes avec rééligibilité)**: Si un utilisateur reçoit la campagne plusieurs fois dans la fenêtre du rapport, Braze déterminera s’il doit être inclus dans l’entonnoir en fonction des actions que cet utilisateur a effectué après avoir reçu la campagne pour la première fois dans la fenêtre de temps.
- Prenez en compte le fait qu’il peut exister des divergences entre les valeurs d’entonnoir et de conversion standard étant donné que les utilisateurs peuvent se convertir plus d’une fois en cas de nouvelle éligibilité, mais les rapports d’entonnoir convertirons une seule fois maximum, même si un utilisateur effectue l’événement plus d’une fois. 

**Pour les campagnes multivariantes avec rééligibilité**: Si un utilisateur reçoit plusieurs variantes de la campagne pendant la fenêtre du rapport, Braze déterminera s’il doit être inclus dans l’entonnoir de variante en fonction des actions que cet utilisateur a effectué après avoir reçu la variante de la campagne pour la première fois. Cela signifie que le même utilisateur peut être comptabilisé dans plusieurs variantes différentes s’il a reçu plusieurs variantes pendant la période de l’entonnoir.

[1]:{% image_buster /assets/img/funnel_report/funnel_report1.jpg %}
[2]:{% image_buster /assets/img/funnel_report/funnel_report2.png %}
[3]:{% image_buster /assets/img/funnel_report/funnel_report3.png %}
[4]:{% image_buster /assets/img/funnel_report/funnel_report4.jpg %}
[5]:{% image_buster /assets/img/funnel_report/canvas_campaign.png %}
[6]:{% image_buster /assets/img/funnel_report/funnel_report5.png %}
