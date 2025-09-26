---
nav_title: Modification de Canvas après le lancement
article_title: Modification de Canvas après le lancement
page_order: 0
description: "Cet article de référence aborde les différents aspects d’un Canvas, pouvant être modifié après le lancement initial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Modification de Canvas après le lancement

> Cet article de référence aborde les éléments qui peuvent être modifiés sur un Canvas après le lancement initial.

Vous pouvez modifier vos toiles après leur lancement :

* Insérant de nouvelles étapes de canvas dans le parcours utilisateur
* Ajoutant de nouvelles variantes et connexions
* Ajustant la distribution des variantes
* Arrêtant ou relançant toutes les étapes de Canvas

{% alert note %}
La répartition de variante de contrôle peut être uniquement réduite après le lancement.
{% endalert %}

Gardez à l'esprit les modifications suivantes autorisées après le lancement du canvas, en fonction du flux de travail avec lequel votre canvas a été créé. Si votre Canvas utilise le flux de travail Canvas d’origine, vous devrez le dupliquer vers Canvas Flow pour pouvoir effectuer des éditions après le lancement.

Vous pouvez supprimer tous les éléments suivants au sein de votre parcours utilisateur :

- [Étapes du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes de Canvas 
- Connexions entre les étapes de Canvas

Si vous souhaitez modifier ou ajouter des étapes à votre parcours utilisateur Canvas, les détails suivants s'appliquent :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles pour toutes les étapes nouvellement créées. 
- Si vos paramètres d’entrée Canvas autorisent les utilisateurs à pouvoir accéder à nouveau aux étapes, les utilisateurs ayant déjà dépassé les étapes nouvellement créées y seront à nouveau éligibles.
- Les utilisateurs d’un Canvas actuellement déployé, mais n’ayant pas atteint les points du parcours utilisateur où ont été ajoutées de nouvelles étapes, seront éligibles pour recevoir ces nouvelles étapes. 

Si vous supprimez une étape [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), vous pouvez éventuellement rediriger les utilisateurs en attente dans l'étape vers une autre étape du canvas. Pour les délais, les utilisateurs resteront dans l’étape jusqu’à la fin de la période en question. Pour les parcours d’action, les utilisateurs resteront dans l’étape jusqu’à la fin de la fenêtre d’évaluation.

Notez que lorsque vous lancez un Canvas initialement, Braze met en file d'attente les utilisateurs pour l'étape du message à laquelle ils se trouvent, et non pour tous les messages suivants dans le Canvas. Si vous modifiez le canvas après le lancement, certains utilisateurs seront déjà en file d'attente et ne prendront pas en compte les modifications. Si vous arrêtez le Canvas, le dupliquez, puis le modifiez et lancez cette nouvelle version, le Canvas réévaluera à nouveau tous les utilisateurs, et pas seulement ceux qui n'ont pas encore été mis en file d'attente.

Consultez la section " [Meilleures pratiques"](#best-practices) pour connaître les cas d'utilisation spécifiques en matière de modification. En général, il vaut mieux éviter de modifier les canvas en ligne, car cela peut entraîner certains comportements inattendus.

{% details Editeur de canevas original %}

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos toiles dans Canvas Flow.]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)
{% endalert %}

Vous ne pouvez pas modifier ou supprimer les connexions existantes, et vous ne pouvez pas insérer une étape entre des étapes connectées existantes. Si vous souhaitez modifier ou ajouter des étapes à votre parcours utilisateur Canvas, les détails suivants s'appliquent :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles pour toutes les étapes nouvellement créées. 
- Si vos paramètres d’entrée Canvas autorisent les utilisateurs à pouvoir accéder à nouveau aux étapes, les utilisateurs ayant déjà dépassé les étapes nouvellement créées y seront à nouveau éligibles.
- Les utilisateurs d’un Canvas actuellement déployé, mais n’ayant pas atteint les points du parcours utilisateur où ont été ajoutées de nouvelles étapes, seront éligibles pour recevoir les nouvelles étapes.
- Si une étape de délai est la dernière étape du canvas, les utilisateurs qui atteignent cette étape sont automatiquement avancés hors du canvas et ne recevront pas de nouvelles étapes créées.

{% alert important %}
Si vous mettez à jour les paramètres de **délai** ou de **fenêtre** pour une étape du canvas, les utilisateurs qui se trouvent actuellement dans cette étape au moment de la mise à jour respecteront le délai qui leur a été attribué lorsqu'ils y sont entrés à l'origine. Seuls les nouveaux utilisateurs entrant dans le Canvas et ceux qui n'ont pas encore été mis en file d'attente pour cette étape recevront le message au moment de la mise à jour.
{% endalert %}

Arrêter un Canvas ne fera pas sortir les utilisateurs qui attendent de recevoir un message. Si vous activez à nouveau le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (à moins que le temps d’envoi du message se soit écoulé, dans ce cas, ils ne le recevront pas).

{% enddetails %}

## Informations relatives au Canvas

Vous pouvez modifier les paramètres et les informations suivants de Canvas après le lancement d'un Canvas :

* Nom et description du Canvas
* Teams et Tags
* Type d’entrée, planification et contrôles
* Statut d’abonnement
* Limitation du taux
* Limite de fréquence
* Heures calmes
* Audience cible

Après le lancement d'une toile :

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
* Délais

En revanche, le type de planification et les pourcentages de contrôle de l'étape ne sont pas modifiables après le lancement. Pour les parcours d'action et les parcours d'audience, les classements ne sont pas modifiables après le lancement.

### Pourcentages Canvas Variant

Après le lancement d'un Canvas, vous pouvez uniquement diminuer les pourcentages des variantes de contrôle. Si un pourcentage de variante est modifié dans Canvas, vous pourrez voir que les utilisateurs peuvent être répartis sur d’autres variantes.

Initialement, une variante spécifique est affectée de manière aléatoire à ces utilisateurs, avant qu’ils reçoivent une campagne pour la première fois. À partir de ce moment-là, à chaque réception de campagne (ou lorsque l’utilisateur entre à nouveau une Canvas Variant), ils recevront la même variante à moins que les pourcentages de variante soient modifiés.

Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes. Les utilisateurs resteront dans ces variantes jusqu’à ce que les pourcentages soient à nouveau modifiés. Notez que pour des Canvas utilisant un raccord aux filtres `NOT` avec des numéros de compartiment aléatoires, il est possible que les utilisateurs ne reçoivent pas la même branche chaque fois dans leur parcours utilisateur lorsqu’ils accèdent à nouveau au Canvas.

#### Groupes de contrôles

Les groupes de contrôles restent uniformes si le pourcentage de variantes est inchangé. Si le pourcentage d'un groupe de contrôle est diminué ou augmenté, les utilisateurs qui ont précédemment reçu des messages ne pourront pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne recevra jamais de message.

### Heure locale d’envoi

Les Canvas planifiés pour être lancés à l’heure locale d’envoi peuvent être modifiés jusqu’à 24 heures avant l’heure d’envoi planifiée. On appelle cette fenêtre la « Zone sécurisée ». 

{% alert tip %}
Si vous prévoyez d’apporter des modifications plus importantes entraînant la création intégrale d’un nouveau Canvas, pensez à exclure les utilisateurs qui ont reçu le premier Canvas et à ajuster à nouveau les heures de planification de Canvas pour permettre l’envoi pour le fuseau horaire.
{% endalert %}

### Suppression de variantes

Lorsque des variantes sont supprimées d'un Canvas, il se produit ce qui suit :

- Les étapes de la variante (y compris celles qui sont partagées par d'autres variantes) seront supprimées. 
- Les analyses d'étapes et les analyses de haut niveau pour le canvas, telles que le _nombre total d'entrées_, le _nombre total de sorties_ et le _taux de conversion_, seront supprimées.
- Les utilisateurs des variantes supprimées sont exclus des étapes et les messages suivants ne sont pas envoyés.

### Propriétés d’entrées de Canvas

Les propriétés d'entrée des canvas ne sont pas modélisées en étapes lors de l'envoi. Cela signifie que lorsque les propriétés d'entrée d'un canvas sont modifiées après le lancement d'un canvas, ces changements ne s'appliqueront qu'aux nouveaux utilisateurs qui entrent dans le canvas. Si votre Canvas permet aux utilisateurs d'entrer à nouveau dans le Canvas, tous les utilisateurs qui entrent à nouveau dans le Canvas seront déterminés par les propriétés d'entrée du Canvas mises à jour.

## Bonnes pratiques

Consultez ces bonnes pratiques à garder à l'esprit lorsque vous modifiez ou ajoutez des éléments à votre Canvas après son lancement.

### Étapes déconnectées

Vous pouvez déployer vos Canvas avec des étapes déconnectées ainsi que les sauvegarder après lancement. Avant de déconnecter une étape de votre flux de travail, nous vous recommandons de vérifier la vue analytique des étapes afin de voir les utilisateurs en attente.

Supposons qu'un utilisateur se trouve à une étape déconnectée de votre flux de travail Canvas. Cet utilisateur passera à l’étape suivante s’il en existe une. Les paramètres de l’étape dicteront la manière dont l’utilisateur avancera. 

En créant ou en modifiant des étapes déconnectées, vous pouvez apporter des modifications à ces étapes indépendantes sans avoir à les relier directement au reste de votre Canvas. Cela permet de tester vos étapes avant de lancer à nouveau votre Canvas. 

### Étape Chemin d’expérience

Si votre Canvas comporte une expérience active ou en cours et que vous mettez à jour le Canvas actif (même si ce n'est pas à l'étape des chemins chemins d'expérience), l'expérience en cours prendra fin. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau.

### Délais temporels

Il peut être un peu difficile d’modifier des Canvas présentant des délais temporels ! Gardez donc à l’esprit les détails suivants lorsque vous effectuerez des modifications à vos Canvas.

Si vous mettez à jour le délai dans une étape ou une fenêtre d'évaluation de l'étape Chemins d'action, seuls les nouveaux utilisateurs entrant dans le Canvas et les utilisateurs qui n'ont pas été mis en file d'attente pour cette étape recevront le message au délai mis à jour.

Si vous supprimez une étape dotée d'un délai (telle que Délai ou Parcours d'action) et que vous décidez de rediriger ces utilisateurs vers une autre étape du canvas, les utilisateurs ne seront redirigés qu'une fois le délai de l'étape écoulé. Par exemple, supposons que vous supprimiez une étape Délai avec un délai d'un jour et que vous redirigiez ces utilisateurs vers une étape Message. Dans ce cas, les utilisateurs ne seront redirigés que lorsque le délai d’un jour est écoulé.

Si votre Canvas comporte une ou plusieurs étapes des chemins d'expérience, la suppression d'étapes pourrait invalider les résultats de cette étape.

### Arrêter des Canvas

L'arrêt d'un canvas n'entraînera pas la sortie des utilisateurs qui attendent dans une étape. Si vous réactivez le canvas et que les utilisateurs attendent toujours, ils termineront l'étape et passeront à l'étape suivante. Cependant, si le délai durant lequel l’utilisateur aurait dû passer à l’étape suivante est dépassé, il quittera le canvas. 

Par exemple, imaginons que vous disposiez d’un canvas créé à l'aide du flux de travail Canvas Flow, défini pour être lancé à 14 h, avec une variante du canvas comportant deux étapes : une étape Délai avec un délai d'une heure qui débouche dans une étape Message. 

Un utilisateur entre dans ce canvas à 14 h 01 et entre dans l'étape Délai au même moment. Cela signifie que l'utilisateur sera planifié pour passer à l'étape suivante du parcours utilisateur (l'étape Message) à 15 h 01. Si vous arrêtez le Canvas à 14 h 30 et que vous le réactivez à 15 h 30, l’utilisateur quittera Canvas puisque 15 h 01 est passée. Toutefois, si vous réactivez le canvas à 14 h 40, l'utilisateur passera comme prévu à l'étape Message à 15 h 01.
