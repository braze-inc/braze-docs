---
nav_title: Modifier les toiles après le lancement
article_title: Modifier les toiles après le lancement
page_order: 0
description: "Cet article de référence aborde les différents aspects d’un Canvas, pouvant être modifié après le lancement initial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Modifier les toiles après le lancement

> Cet article de référence aborde les éléments qui peuvent être modifiés sur un Canvas après le lancement initial.

Vous pouvez modifier vos toiles après leur lancement en procédant comme suit :

* Insérant de nouvelles étapes de canvas dans le parcours utilisateur
* Ajoutant de nouvelles variantes et connexions
* Ajustant la distribution des variantes
* Arrêtant ou relançant toutes les étapes de Canvas

{% alert note %}
La répartition de variante de contrôle peut être uniquement réduite après le lancement.
{% endalert %}

Vous pouvez supprimer tous les éléments suivants au sein de votre parcours utilisateur :

- [Étapes du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes de Canvas 
- Connexions entre les étapes de Canvas

Si vous souhaitez modifier ou ajouter des étapes à votre parcours utilisateur Canvas, veuillez tenir compte des informations suivantes :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles pour toutes les étapes nouvellement créées. 
- Si vos paramètres d’entrée Canvas autorisent les utilisateurs à pouvoir accéder à nouveau aux étapes, les utilisateurs ayant déjà dépassé les étapes nouvellement créées y seront à nouveau éligibles.
- Les utilisateurs d’un Canvas actuellement déployé, mais n’ayant pas atteint les points du parcours utilisateur où ont été ajoutées de nouvelles étapes, seront éligibles pour recevoir ces nouvelles étapes. 

Si vous supprimez une étape [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), vous pouvez éventuellement rediriger les utilisateurs en attente dans l'étape vers une autre étape du canvas. En cas de retard, les utilisateurs restent dans l'étape jusqu'à la fin de la période de retard. Pour les parcours d’action, les utilisateurs restent dans l'étape jusqu'à la fin de la fenêtre d'évaluation.

Notez que lorsque vous lancez un Canvas initialement, Braze met en file d'attente les utilisateurs pour l'étape du message à laquelle ils se trouvent, et non pour tous les messages suivants dans le Canvas. Si vous modifiez le canvas après son lancement, certains utilisateurs peuvent déjà être en attente et ne pas bénéficier des modifications. Si vous arrêtez le canvas, le dupliquez, puis le modifiez et lancez cette nouvelle version, le canvas réévalue à nouveau tous les utilisateurs, et pas seulement ceux qui n'ont pas encore été mis en file d'attente.

Consultez la section " [Meilleures pratiques"](#best-practices) pour connaître les cas d'utilisation spécifiques en matière de modification. En général, il vaut mieux éviter de modifier les canvas en ligne, car cela peut entraîner certains comportements inattendus.

{% details Expand for original Canvas editor details %}

Gardez à l'esprit les modifications suivantes autorisées après le lancement du canvas, en fonction du flux de travail avec lequel votre canvas a été créé. Si votre canvas utilise le flux de travail Canvas d'origine, il sera nécessaire de le cloner d'abord dans Canvas Flow afin de pouvoir modifier le contenu après le lancement.

Vous ne pouvez pas modifier ou supprimer les connexions existantes, et vous ne pouvez pas insérer une étape entre des étapes connectées existantes. Si vous souhaitez modifier ou ajouter des étapes à votre parcours utilisateur Canvas, veuillez tenir compte des informations suivantes :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles pour toutes les étapes nouvellement créées. 
- Si vos paramètres d’entrée Canvas autorisent les utilisateurs à pouvoir accéder à nouveau aux étapes, les utilisateurs ayant déjà dépassé les étapes nouvellement créées y seront à nouveau éligibles.
- Les utilisateurs d’un Canvas actuellement déployé, mais n’ayant pas atteint les points du parcours utilisateur où ont été ajoutées de nouvelles étapes, seront éligibles pour recevoir les nouvelles étapes.
- Si une étape de délai est la dernière étape du canvas, les utilisateurs qui atteignent cette étape sont automatiquement avancés hors du canvas et ne recevront pas de nouvelles étapes créées.

{% alert important %}
Si vous modifiez les paramètres **Délai** ou **Fenêtre** d'une étape du canvas, les utilisateurs qui se trouvent actuellement dans cette étape au moment de la mise à jour respectent le délai qui leur a été attribué lorsqu'ils y sont entrés initialement. Seuls les nouveaux utilisateurs qui accèdent à Canvas et ceux qui ne sont pas encore dans la file d'attente pour cette étape recevront le message à l'heure mise à jour.
{% endalert %}

L'arrêt d'un canvas ne déconnecte pas les utilisateurs qui attendent de recevoir un message. Si vous réactivez Canvas et que les utilisateurs attendent toujours le message, ils le recevront (à moins que le délai d'envoi du message soit dépassé, auquel cas ils ne le recevront pas).

{% enddetails %}

## Informations relatives au Canvas

Vous pouvez modifier les paramètres et détails suivants après avoir lancé un canvas :

* Nom et description du Canvas
* Teams et Tags
* Type d’entrée, planification et contrôles
* Statut d’abonnement
* Limitation du taux
* Limite de fréquence
* Heures calmes
* Audience cible

Après le lancement d'un canvas :

- Les événements de conversion ne peuvent pas être modifiés. 
- Les étapes suivantes ne peuvent pas être ajoutées ou supprimées, et ne peuvent pas être réordonnées pour ajuster le classement : [Les parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), les [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) et les [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Solution 1 :** Créez un nouveau parcours d'audience, un nouveau parcours d'action ou un nouveau chemin d'expérience et reconfigurez les chemins vers cette nouvelle étape.
  - **Solution 2 :** Dupliquez le canvas pour le modifier.

### Démarches individuelles

Concernant les différentes étapes du canvas, vous pouvez modifier les éléments suivants après le lancement :

* Nom
* Contenu du message
* Déclencheurs
* Audience
* Événements d'exception
* Retards (uniquement pour les étapes Retard)

En revanche, le type de planification et les pourcentages de contrôle de l'étape ne sont pas modifiables après le lancement. Pour les étapes « Parcours d’action » et « Parcours d’audience », les classements et les fenêtres d’évaluation ne sont pas modifiables après le lancement.

### Pourcentages Canvas Variant

Après le lancement d'un Canvas, vous pouvez uniquement diminuer les pourcentages des variantes de contrôle. Si un pourcentage de variante est modifié dans Canvas, vous pourrez voir que les utilisateurs peuvent être répartis sur d’autres variantes.

Initialement, une variante spécifique est affectée de manière aléatoire à ces utilisateurs, avant qu’ils reçoivent une campagne pour la première fois. À partir de ce moment, chaque fois que la campagne est reçue (ou que l'utilisateur accède à nouveau à une variante du canvas), il reçoit la même variante, sauf si les pourcentages des variantes sont modifiés.

Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes. Les utilisateurs restent dans ces variantes jusqu’à ce que les pourcentages soient à nouveau modifiés. Notez que pour des Canvas utilisant un raccord aux filtres `NOT` avec des numéros de compartiment aléatoires, il est possible que les utilisateurs ne reçoivent pas la même branche chaque fois dans leur parcours utilisateur lorsqu’ils accèdent à nouveau au Canvas.

#### Groupes de contrôles

Les groupes de contrôles restent uniformes si le pourcentage de variantes est inchangé. Si le pourcentage d'un groupe de contrôle est diminué ou augmenté, les utilisateurs qui ont précédemment reçu des messages ne pourront pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne recevra jamais de message.

### Heure locale d’envoi

Les canevas dont l'envoi est prévu dans le cadre de la planification à une heure locale peuvent être modifiés jusqu'à 24 heures avant l'heure d'envoi prévue. On appelle cette fenêtre la « Zone sécurisée ». 

{% alert tip %}
Si vous prévoyez d’apporter des modifications plus importantes entraînant la création intégrale d’un nouveau Canvas, pensez à exclure les utilisateurs qui ont reçu le premier Canvas et à ajuster à nouveau les heures de planification de Canvas pour permettre l’envoi pour le fuseau horaire.
{% endalert %}

Lorsqu'une planification d'entrée est configurée pour accueillir les utilisateurs immédiatement après le lancement, Canvas démarre à l'heure la plus proche, par incréments de 5 minutes. Par exemple, si vous mettez à jour un canvas pour que les utilisateurs y accèdent immédiatement à 8 h 31 PST, l'heure de lancement est définie à 8 h 30 PST et dans le fuseau horaire de l'entreprise.

### Suppression de variantes

Lorsque des variantes sont supprimées d'un canvas, les événements suivants se produisent :

- Les étapes de la variante (y compris celles partagées par d'autres variantes) sont supprimées. 
- Les analyses par étape et les analyses de haut niveau pour Canvas, telles que _le nombre total d'entrées_, _le nombre total de sorties_ et _le taux de conversion_, sont supprimées.
- Les utilisateurs des variantes supprimées sont retirés des étapes et aucun message suivant n'est envoyé.

### Propriétés d’entrées de Canvas

Les propriétés d'entrée des canvas ne sont pas modélisées en étapes lors de l'envoi. Cela signifie que lorsque les propriétés d'entrée d'un canvas sont modifiées après le lancement de celui-ci, ces modifications ne s'appliquent qu'aux nouveaux utilisateurs qui accèdent au canvas. Si votre canvas autorise les utilisateurs à y revenir, ceux qui reviennent sont déterminés par les propriétés d'entrée mises à jour du canvas.

## Bonnes pratiques

Consultez ces bonnes pratiques à garder à l'esprit lorsque vous modifiez ou ajoutez des éléments à votre Canvas après son lancement.

{% alert important %}
En règle générale, il est recommandé d'éviter d'effectuer des modifications lorsque le canvas est actif et en train de mettre des utilisateurs en file d'attente.
{% endalert %}

### Étapes déconnectées

Vous pouvez déployer vos Canvas avec des étapes déconnectées ainsi que les sauvegarder après lancement. Avant de déconnecter une étape de votre flux de travail, nous vous recommandons de vérifier la vue analytique des étapes afin de voir les utilisateurs en attente.

Supposons qu'un utilisateur se trouve à une étape déconnectée de votre flux de travail Canvas. Cet utilisateur effectue l'avancement vers l'étape suivante, le cas échéant. Les paramètres de l'étape déterminent la manière dont l'utilisateur doit procéder pour l'avancement. 

En créant ou en modifiant des étapes déconnectées, vous pouvez apporter des modifications à ces étapes indépendantes sans avoir à les relier directement au reste de votre Canvas. Cela vous aidera à tester vos étapes avant de relancer votre Canvas. 

### Étape Chemin d’expérience

Si votre Canvas comporte une expérience Winning Path ou Personalized Path active ou en cours et que vous mettez à jour le Canvas actif (que vous mettiez à jour ou non l'étape du chemin d’expérience elle-même), l'expérience en cours prend fin et l'étape des chemins d'expérience ne détermine pas de chemin gagnant ni de chemins personnalisés. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. Dans le cas contraire, les utilisateurs suivent le chemin d’expérience comme si aucune méthode d’optimisation n’avait été sélectionnée.

### Délais temporels

La modification des canevas avec des délais peut s'avérer quelque peu délicate. Veuillez donc garder à l'esprit les détails suivants lorsque vous modifiez vos canevas :

- Si vous mettez à jour le délai dans une étape Délai, seuls les nouveaux utilisateurs qui accèdent au canvas et les utilisateurs qui n'ont pas été mis en file d'attente pour cette étape recevront le message au délai mis à jour.
- Si vous supprimez une étape avec un délai (telle que Délai ou parcours d’action) et décidez de rediriger ces utilisateurs vers une autre étape du canvas, les utilisateurs ne seront redirigés qu'une fois le délai de l'étape écoulé. Par exemple, supposons que vous supprimiez une étape « Délai » avec un délai d'un jour et que vous redirigiez ces utilisateurs vers une étape « Message ». Dans ce cas, les utilisateurs ne sont redirigés qu'après expiration du délai d'un jour.
- Si votre Canvas comporte une ou plusieurs étapes des chemins d’expérience, la suppression d’étapes pourrait invalider les résultats de cette étape.

### Arrêter des Canvas

L'arrêt d'un canvas ne met pas fin à la session des utilisateurs qui sont en attente dans une étape du canvas. Si vous réactivez le canvas et que les utilisateurs sont toujours en attente, ils terminent l'étape et passent à l'étape suivante. Toutefois, si le délai dans lequel l'utilisateur aurait dû passer à l'étape suivante est dépassé, il quitte alors le canvas. 

Par exemple, supposons que vous disposiez d'un Canvas créé à l'aide du workflow Canvas Flow, configuré pour se lancer à 14 h avec une variante en deux étapes : une étape Delay avec un délai d'une heure qui mène à une étape Message. 

Un utilisateur entre dans ce canvas à 14 h 01 et entre dans l'étape Délai au même moment. Cela signifie que la planification prévoit que l'utilisateur passe à l'étape suivante du parcours utilisateur (l'étape Message) à 15 h 01. Si vous désactivez canvas à 14 h 30 et le réactivez à 15 h 30, l'utilisateur quittera canvas, car il est alors 15 h 01. Cependant, si vous réactivez le canvas à 14 h 40, l'utilisateur passe à l'étape du message comme prévu à 15 h 01.

## Choses à savoir

Les problèmes courants suivants peuvent être déclenchés lors de la modification ou de l'ajout de composants à tout autre composant dans un canvas après son lancement. 

{% alert important %}
Les problèmes suivants peuvent être évités. Si vous devez modifier un canvas après son lancement, nous vous recommandons de vérifier au préalable que tous les utilisateurs qui ont déjà accédé au canvas ont terminé leur parcours utilisateur. De plus, nous vous recommandons de ne pas supprimer les étapes qui ont déjà été traitées par au moins un utilisateur.
{% endalert %}

- Données de rapport manquantes (lorsque des variantes de message sont supprimées puis rajoutées)
- Les utilisateurs ne suivent pas le chemin prévu.
- Les messages sont envoyés à des moments imprévus.
- Les modifications n'écrasent pas les données Currents, vous pouvez donc remarquer des divergences entre les étapes du canvas (telles que`canvas_step_ids`celles qui n'existent pas dans le canvas en raison d'une suppression).
- Les utilisateurs peuvent recevoir le même message à deux reprises.
- Les utilisateurs ne recevront pas de messages en raison de la limite de débit existante.
  - Lorsque vous mettez à jour la limite de débit sur un canvas actif, la nouvelle limite s'applique à tous les envois de messages futurs, y compris aux utilisateurs déjà présents dans le canvas. Cependant, en raison de la mise en cache interne (jusqu'à 30 secondes), il peut y avoir un léger délai avant que la nouvelle limite de débit ne soit pleinement appliquée. Veuillez noter que Braze met en file d'attente les utilisateurs pour l'étape Message à laquelle ils se trouvent actuellement, de sorte que la limite de débit en vigueur au moment où le message de chaque étape est effectivement envoyé est celle qui s'applique.
- Lorsqu'un canvas est [automatiquement arrêté]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#available-statuses), les brouillons post-lancement du canvas sont également supprimés.
