---
nav_title: Modifier les toiles après le lancement
article_title: Modifier les toiles après le lancement
page_order: 0
description: "Cet article de référence couvre les différents aspects d'un canvas qui peuvent être modifiés après le lancement initial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Modifier les toiles après le lancement

> Cet article de référence traite des modifications qui peuvent être apportées à un canvas après son lancement initial.

Vous pouvez modifier vos toiles après leur lancement :

* Insérer de nouvelles étapes du canvas dans le parcours de l'utilisateur
* Ajout de nouvelles variantes et connexions
* Adjusting variante distribution
* Arrêt ou reprise de toutes les étapes du canvas

{% alert note %}
La distribution des variantes de contrôle ne peut être diminuée qu'après le lancement.
{% endalert %}

Gardez à l'esprit les modifications suivantes autorisées après le lancement du canvas, en fonction du flux de travail avec lequel votre canvas a été créé. Si votre Canvas utilise le flux de travail Canvas d'origine, vous devrez d'abord cloner vers Canvas Flow afin d'effectuer des modifications après le lancement.

Vous pouvez supprimer n'importe lequel des éléments suivants dans votre parcours utilisateur :

- [Les étapes du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes du canvas 
- Liens entre les étapes du canvas

Si vous souhaitez modifier ou ajouter des étapes à votre parcours utilisateur Canvas, les détails suivants s'appliquent :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles pour toutes les étapes nouvellement créées. 
- Si vos paramètres de saisie dans Canvas autorisent les utilisateurs à revenir sur des étapes, les utilisateurs qui ont déjà passé des étapes nouvellement créées sont autorisés à revenir sur ces étapes.
- Les utilisateurs qui se trouvent actuellement dans un Canvas lancé, mais qui n'ont pas atteint les points du parcours de l'utilisateur où de nouvelles étapes sont ajoutées, sont éligibles pour recevoir ces étapes nouvellement ajoutées. 

Si vous supprimez une étape [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), vous pouvez éventuellement rediriger les utilisateurs en attente dans l'étape vers une autre étape du canvas. Pour les retards, les utilisateurs resteront dans l'étape jusqu'à la fin de la période de retard. Pour les parcours d'action, les utilisateurs resteront dans l'étape jusqu'à la fin de la fenêtre d'évaluation.

Notez que lorsque vous lancez un Canvas initialement, Braze met en file d'attente les utilisateurs pour l'étape du message à laquelle ils se trouvent, et non pour tous les messages suivants dans le Canvas. Si vous modifiez le canvas après le lancement, certains utilisateurs seront déjà en file d'attente et ne prendront pas en compte les modifications. Si vous arrêtez le Canvas, le dupliquez, puis le modifiez et lancez cette nouvelle version, le Canvas réévaluera à nouveau tous les utilisateurs, et pas seulement ceux qui n'ont pas encore été mis en file d'attente.

Consultez la section " [Meilleures pratiques"](#best-practices) pour connaître les cas d'utilisation spécifiques en matière de modification. En général, il est préférable d'éviter de modifier les lignes/en production/instantanées, car il peut y avoir des comportements inattendus.

{% details Expand for original Canvas editor details %}

Vous ne pouvez pas modifier ou supprimer les connexions existantes, et vous ne pouvez pas insérer une étape entre des étapes connectées existantes. Si vous souhaitez modifier ou ajouter des étapes à votre parcours utilisateur Canvas, les détails suivants s'appliquent :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles pour toutes les étapes nouvellement créées. 
- Si vos paramètres de saisie dans Canvas autorisent les utilisateurs à revenir sur des étapes, les utilisateurs qui ont déjà passé des étapes nouvellement créées sont autorisés à revenir sur ces étapes.
- Les utilisateurs qui se trouvent actuellement dans un Canvas lancé, mais qui n'ont pas atteint les étapes nouvellement ajoutées dans le parcours de l'utilisateur, sont éligibles pour recevoir ces étapes nouvellement ajoutées.
- Si une étape de délai est la dernière étape du canvas, les utilisateurs qui atteignent cette étape sont automatiquement avancés hors du canvas et ne recevront pas de nouvelles étapes créées.

{% alert important %}
Si vous mettez à jour les paramètres de **délai** ou de **fenêtre** pour une étape du canvas, les utilisateurs qui se trouvent actuellement dans cette étape au moment de la mise à jour respecteront le délai qui leur a été attribué lorsqu'ils y sont entrés à l'origine. Seuls les nouveaux utilisateurs entrant dans le Canvas et ceux qui n'ont pas encore été mis en file d'attente pour cette étape recevront le message au moment de la mise à jour.
{% endalert %}

L'arrêt d'un canvas n'entraîne pas la sortie des utilisateurs qui attendent de recevoir un message. Si vous réactivez le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (sauf si la date à laquelle le message aurait dû leur être envoyé est passée, auquel cas ils ne le recevront pas).

{% enddetails %}

## Détails de la toile

Vous pouvez modifier les paramètres et les informations suivants de Canvas après le lancement d'un Canvas :

* Nom et description du canvas
* Teams et tags
* Type d'entrée, planification et contrôles
* Statut de l'abonnement
* Limite de débit
* Limitation de fréquence
* Heures calmes
* L'audience ciblée

Après le lancement d'une toile :

- Les événements de conversion ne peuvent pas être modifiés. 
- Les étapes suivantes ne peuvent pas être ajoutées ou supprimées, et ne peuvent pas être réordonnées pour ajuster le classement : [Les parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), les [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) et les [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Solution 1 :** Créez un nouveau parcours d'audience, un nouveau parcours d'action ou un nouveau chemin d'expérience et reconfigurez les chemins vers cette nouvelle étape.
  - **Solution 2 :** Dupliquez le canvas pour le modifier.

### Démarches individuelles

Pour les différentes étapes du canvas, vous pouvez modifier les détails suivants après le lancement :

* Nom
* Contenu du message
* Déclencheurs
* L'audience
* Événements d'exception
* Retards

Cependant, le type de planification et les pourcentages de contrôle de l'étape ne sont pas modifiables après le lancement. Pour les parcours d'action et les parcours d'audience, les classements ne sont pas modifiables après le lancement.

### Pourcentages de variante du canvas

Après le lancement d'une Canvas, vous ne pouvez que diminuer les pourcentages de la variante de contrôle. Si le pourcentage d'une variante est modifié dans Canvas, vous constaterez que vos utilisateurs peuvent être redistribués vers d'autres variantes.

Dans un premier temps, ces utilisateurs se voient attribuer au hasard une variante particulière avant de recevoir une campagne pour la première fois. Dès lors, chaque fois que la campagne sera reçue (ou que l'utilisateur entrera à nouveau dans une variante du canvas), il recevra la même variante, à moins que les pourcentages de la variante ne soient modifiés.

Si les pourcentages des variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes. Les utilisateurs resteront dans ces variantes jusqu'à ce que les pourcentages soient à nouveau modifiés. Notez que pour les Canvas utilisant des branchements avec des filtres `NOT` avec des numéros de compartiment aléatoires, les utilisateurs peuvent ne pas recevoir le même branchement à chaque fois dans leur parcours d'utilisateur lorsqu'ils réintègrent le Canvas.

#### Groupes de contrôle

Les groupes de contrôle restent cohérents si le pourcentage de variante est inchangé. Si le pourcentage d'un groupe de contrôle est diminué ou augmenté, les utilisateurs qui ont précédemment reçu des messages ne pourront pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne recevra jamais de message.

### Heure d'envoi local

Les toiles planifiées pour être lancées à une heure d'envoi locale peuvent être modifiées jusqu'à 24 heures avant l'heure d'envoi prévue. Cette fenêtre est appelée "zone de sécurité". 

{% alert tip %}
Si vous avez l'intention de faire des modifications plus importantes qui conduisent à la création d'une nouvelle copie de Canvas, n'oubliez pas d'exclure les utilisateurs qui ont reçu le premier Canvas et de réajuster les heures de planification de Canvas pour tenir compte de l'envoi par fuseau horaire.
{% endalert %}

### Suppression de variantes

Lorsque des variantes sont supprimées d'un Canvas, il se produit ce qui suit :

- Les étapes de la variante (y compris celles qui sont partagées par d'autres variantes) seront supprimées. 
- Les analyses d'étapes et les analyses de haut niveau pour le canvas, telles que le _nombre total d'entrées_, le _nombre total de sorties_ et le _taux de conversion_, seront supprimées.
- Les utilisateurs des variantes supprimées sont exclus des étapes et les messages suivants ne sont pas envoyés.

### Propriétés de l'entrée dans le canevas

Les propriétés d'entrée des canvas ne sont pas modélisées en étapes lors de l'envoi. Cela signifie que lorsque les propriétés d'entrée d'un canvas sont modifiées après le lancement d'un canvas, ces changements ne s'appliqueront qu'aux nouveaux utilisateurs qui entrent dans le canvas. Si votre Canvas permet aux utilisateurs d'entrer à nouveau dans le Canvas, tous les utilisateurs qui entrent à nouveau dans le Canvas seront déterminés par les propriétés d'entrée du Canvas mises à jour.

## Meilleures pratiques

Consultez ces bonnes pratiques à garder à l'esprit lorsque vous modifiez ou ajoutez des éléments à votre Canvas après son lancement.

{% alert important %}
En général, évitez d'apporter des modifications lorsque le Canvas est actif et qu'il met les utilisateurs en file d'attente.
{% endalert %}

### Marches déconnectées

Vous pouvez lancer votre Canvas avec des étapes déconnectées et également enregistrer ces Canvas après le lancement. Avant de déconnecter une étape de votre flux de travail, nous vous recommandons de vérifier la vue analyse/analytique des étapes pour les utilisateurs en attente.

Supposons qu'un utilisateur se trouve à une étape déconnectée de votre flux de travail Canvas. Cet utilisateur passera à l'étape suivante s'il y en a une. Les paramètres de l'étape déterminent la manière dont l'utilisateur doit avancer. 

En créant ou en modifiant des étapes déconnectées, vous pouvez apporter des modifications à ces étapes indépendantes sans avoir à les relier directement au reste de votre Canvas. Cela permet de tester vos étapes avant de lancer à nouveau votre Canvas. 

### Étape des chemins d'expérience d'une étape

Si votre Canvas comporte une expérience de chemin gagnant ou de chemin personnalisé active ou en cours et que vous mettez à jour le Canvas actif, que vous mettiez ou non à jour l'étape des chemins d'expérience elle-même, l'expérience en cours prendra fin et l'étape de l'expérience ne permettra pas de déterminer un chemin gagnant ou des chemins personnalisés. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. Dans le cas contraire, les utilisateurs suivront le chemin d'expérience comme si aucune méthode d'optimisation n'avait été sélectionnée.

### Délais

Modifier des toiles avec des délais peut s'avérer un peu délicat ! Gardez donc à l'esprit les détails suivants lorsque vous modifiez vos toiles.

Si vous mettez à jour le délai dans une étape ou une fenêtre d'évaluation de l'étape Chemins d'action, seuls les nouveaux utilisateurs entrant dans le Canvas et les utilisateurs qui n'ont pas été mis en file d'attente pour cette étape recevront le message au délai mis à jour.

Si vous supprimez une étape dotée d'un délai (telle que Délai ou Parcours d'action) et que vous décidez de rediriger ces utilisateurs vers une autre étape du canvas, les utilisateurs ne seront redirigés qu'une fois le délai de l'étape écoulé. Par exemple, supposons que vous supprimiez une étape Délai avec un délai d'un jour et que vous redirigiez ces utilisateurs vers une étape Message. Dans ce cas, les utilisateurs ne seront redirigés qu'après un délai d'un jour.

Si votre Canvas comporte une ou plusieurs étapes des chemins d'expérience, la suppression d'étapes pourrait invalider les résultats de cette étape.

### Arrêter les toiles

L'arrêt d'un canvas n'entraînera pas la sortie des utilisateurs qui attendent dans une étape. Si vous réactivez le canvas et que les utilisateurs attendent toujours, ils termineront l'étape et passeront à l'étape suivante. Cependant, si le temps que l'utilisateur aurait dû passer à l'étape suivante s'est écoulé, il quittera le canvas. 

Par exemple, disons que vous avez un Canvas créé à l'aide du flux de travail Canvas Flow défini pour être lancé à 14 heures avec une variante du canvas avec deux étapes : une étape Délai avec un délai d'une heure qui va dans une étape Message. 

Un utilisateur entre dans ce Canvas à 14h01 et entre dans l'étape du canvas au même moment. Cela signifie que l'utilisateur sera planifié pour passer à l'étape suivante du parcours de l'utilisateur (l'étape Message) à 15h01. Si vous arrêtez le canvas à 14h30 et que vous le réactivez à 15h30, l'utilisateur quittera le canvas puisqu'il est plus de 15h01. Toutefois, si vous réactivez le Canvas à 14h40, l'utilisateur passera comme prévu à l'étape du message à 15h01.

## Ce qu'il faut savoir

Les problèmes courants suivants peuvent être déclenchés par la modification ou l'ajout de composants à tout autre composant d'un canvas après son lancement. 

{% alert important %}
Les problèmes suivants peuvent être évités. Si vous devez modifier un canvas après son lancement, nous vous recommandons de vérifier d'abord que tous les utilisateurs qui sont déjà entrés dans le canvas ont terminé leur parcours. En outre, nous vous suggérons de ne pas supprimer les étapes qui ont déjà traité au moins un utilisateur.
{% endalert %}

- Données d'envoi manquantes (lorsque des variantes de messages sont supprimées et réajoutées)
- Les utilisateurs ne suivent pas le chemin prévu
- Les messages sont envoyés à des moments inattendus
- Les modifications n'écrasent pas les données actuelles, de sorte que vous pouvez constater des différences entre les étapes du canvas (par exemple `canvas_step_ids` qui n'existe pas dans le canvas en raison d'une suppression).
- Les utilisateurs peuvent recevoir deux fois le même message
- Les utilisateurs ne peuvent pas recevoir de messages en raison de la limite de débit existante.
  - Lorsque des utilisateurs sont envoyés dans un Canvas, la limite de débit appliquée au Canvas lors de l'envoi d'un utilisateur est appliquée à l'utilisateur. Une fois le canvas envoyé, la limite de débit ne peut plus être modifiée pour cet utilisateur, de sorte que l'augmentation ou la diminution de la limite de débit après le lancement n'affectera pas les utilisateurs qui ont déjà été envoyés.