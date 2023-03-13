---
nav_title: Modification de Canvas après le lancement
article_title: Modification de Canvas après le lancement
page_order: 1
description: "Cet article de référence aborde les différents aspects d’un Canvas, pouvant être modifié après le lancement initial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Modification de Canvas après le lancement

> Cet article de référence aborde les éléments qui peuvent être modifiés sur un Canvas après le lancement initial.

Pour les Canvas lancés avec Canvas Flow ou l’éditeur d’origine, vous pouvez éditer vos Canvas après leur lancement en :
* Insérant de nouveaux composants de Canvas dans le parcours utilisateur
* Ajoutant de nouvelles variantes et connexions
* Ajustant la distribution des variantes
* Arrêtant ou relançant toutes les étapes de Canvas

{% alert note %}
La répartition de variante de contrôle peut être uniquement réduite après le lancement.
{% endalert %}

Gardez à l’esprit les éditions Canvas après lancement autorisées en fonction du flux de travail avec lequel votre Canvas a été créé. Si votre Canvas utilise le flux de travail Canvas d’origine, vous devrez le dupliquer vers Canvas Flow pour pouvoir effectuer des éditions après le lancement.

{% tabs local %}
{% tab Canvas Flow %}

Vous pouvez supprimer tous les éléments suivants au sein de votre parcours utilisateur :

- [Composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components)
- Variantes de Canvas 
- Connexions entre les étapes de Canvas

Si vous souhaitez modifier ou ajouter des composants aux parcours utilisateurs de votre Canvas, les détails suivants s’appliqueront :

- Les utilisateurs qui n’ont pas encore accédé au Canvas seront éligibles pour tous les nouveaux composants créés. 
- Si vos paramètres d’entrée Canvas autorisent les utilisateurs à pouvoir accéder à nouveau aux étapes, les utilisateurs ayant déjà dépassé les étapes nouvellement créées y seront à nouveau éligibles.
- Les utilisateurs d’un Canvas actuellement déployé, mais n’ayant pas atteint les points du parcours utilisateur où ont été ajoutées de nouvelles étapes, seront éligibles pour recevoir ces nouvelles étapes. 

Si vous supprimez un composant de [délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou de [parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), vous pouvez éventuellement rediriger les utilisateurs actuellement en attente dans l’étape vers une autre étape Canvas. Pour les délais, les utilisateurs resteront dans l’étape jusqu’à la fin de la période en question. Pour les parcours d’action, les utilisateurs resteront dans l’étape jusqu’à la fin de la fenêtre d’évaluation.

Consultez la section [Canvas Flow](#best-practices) pour y trouver certaines bonnes pratiques pour des cas d’utilisation d’édition donnés. 

{% endtab %}

{% tab Original Canvas Editor %}

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos Canvas en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

Vous ne pouvez ni éditer ni supprimer des connexions existantes et vous ne pouvez pas non plus insérer un composant entre des étapes connectées existantes. 

Si vous souhaitez modifier ou ajouter des composants aux parcours utilisateurs de votre Canvas, les détails suivants s’appliqueront :

- Les utilisateurs qui n’ont pas encore accédé au Canvas seront éligibles pour tous les nouveaux composants créés. 
- Si vos paramètres d’entrée Canvas autorisent les utilisateurs à pouvoir accéder à nouveau aux étapes, les utilisateurs ayant déjà dépassé les étapes nouvellement créées y seront à nouveau éligibles.
- Les utilisateurs d’un Canvas actuellement déployé, mais n’ayant pas atteint les points du parcours utilisateur où ont été ajoutées de nouvelles étapes, seront éligibles pour recevoir les nouvelles étapes.

Si vous mettez à jour les options **Délai** ou **Fenêtre** pour une étape Canvas, seuls les nouveaux utilisateurs accédant au Canvas et les utilisateurs n’ayant pas été mis en file d’attente pour cette étape recevront les messages une fois le délai mis à jour. Si un composant de délai est la dernière étape du Canvas, les utilisateurs atteignant cette étape sont automatiquement sortis du Canvas et ne recevront plus les étapes nouvellement créées. 

{% alert note %}
Arrêter un Canvas ne fera pas sortir les utilisateurs qui attendent de recevoir un message. Si vous activez à nouveau le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (à moins que le temps d’envoi du message se soit écoulé, dans ce cas, ils ne le recevront pas).
{% endalert %}

{% endtab %}
{% endtabs %}

## Informations relatives au Canvas

Vous pouvez éditer ces paramètres de Canvas ainsi que ses informations après le lancement en utilisant un des deux éditeurs (celui d’origine ou Canvas Flow) : 
* Nom et description du Canvas
* Teams et Tags
* Type d’entrée, planification et contrôles
* Statut d’abonnement
* Limitation du taux
* Limite de fréquence
* Heures calmes
* Audience cible

Vous ne pouvez pas éditer les événements de conversion après le lancement d’un Canvas.

### Composants individuels

Concernant les composants de Canvas individuels, vous pouvez éditer les éléments suivants après le lancement :
* Nom
* Contenu du message
* Déclencheurs
* Audience
* Événements d'exception
* Délais

Cependant, le type de planification du composant et les pourcentages de contrôle ne peuvent pas être édités après le lancement.

### Pourcentages Canvas Variant

Si un pourcentage de variante est modifié dans Canvas, vous pourrez voir que les utilisateurs peuvent être répartis sur d’autres variantes.

Initialement, une variante spécifique est affectée de manière aléatoire à ces utilisateurs, avant qu’ils reçoivent une campagne pour la première fois. À partir de ce moment-là, à chaque réception de campagne (ou lorsque l’utilisateur entre à nouveau une Canvas Variant), ils recevront la même variante à moins que les pourcentages de variante soient modifiés.

Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes. Les utilisateurs resteront dans ces variantes jusqu’à ce que les pourcentages soient à nouveau modifiés. Notez que pour des Canvas utilisant un raccord aux filtres `NOT` avec des numéros de compartiment aléatoires, il est possible que les utilisateurs ne reçoivent pas la même branche chaque fois dans leur parcours utilisateur lorsqu’ils accèdent à nouveau au Canvas.

#### Groupes de contrôles

Les groupes de contrôles restent uniformes si le pourcentage de variantes est inchangé. Les utilisateurs ayant précédemment reçu des messages ne peuvent pas accéder à un groupe de contrôle lors d’un envoi ultérieur, tout comme un utilisateur du groupe de contrôle ne peut recevoir un message.

### Heure locale d’envoi

Les Canvas planifiés pour être lancés à l’heure locale d’envoi peuvent être modifiés jusqu’à 24 heures avant l’heure d’envoi planifiée. On appelle cette fenêtre la « Zone sécurisée ». 

{% alert tip %}
Si vous prévoyez d’apporter des modifications plus importantes entraînant la création intégrale d’un nouveau Canvas, pensez à exclure les utilisateurs qui ont reçu le premier Canvas et à ajuster à nouveau les heures de planification de Canvas pour permettre l’envoi pour le fuseau horaire.
{% endalert %}

## Bonnes pratiques

Consultez ces bonnes pratiques à garder en mémoire lorsque vous éditez ou ajoutez des éléments à votre Canvas après qu’il ait été lancé en utilisant Canvas Flow. 

### Étapes déconnectées

Vous pouvez déployer vos Canvas avec des étapes déconnectées ainsi que les sauvegarder après lancement. Avant de déconnecter une étape de votre flux de travail, nous vous recommandons de consulter l’affichage analytique du composant concernant les utilisateurs en attente.

Imaginons qu’un utilisateur se situe dans une étape déconnectée du flux de travail de votre Canvas Flow. Cet utilisateur passera à l’étape suivante s’il en existe une. Les paramètres de l’étape dicteront la manière dont l’utilisateur avancera. 

En créant ou éditant les étapes déconnectées, vous pouvez effectuer des changements à ces composants individuels sans avoir à les connecter directement au reste de votre Canvas. Ceci vous aidera à tester vos composants avant de procéder au nouvel envoi de votre Canvas. 

### Délais temporels

Il peut être un peu difficile d’éditer des Canvas présentant des délais temporels ! Gardez donc à l’esprit les détails suivants lorsque vous effectuerez des modifications à vos Canvas.

Si vous mettez à jour le délai dans un composant de délai ou dans la fenêtre d’évaluation dans le composant de parcours d’action, seuls les nouveaux utilisateurs accédant au Canvas et les utilisateurs n’ayant pas été mis en file d’attente pour cette étape recevront les messages une fois le délai temporel mis à jour.

Si vous supprimez un composant avec un délai temporel (par ex., délai ou parcours d’action) et décidez de rediriger ces utilisateurs sur un autre composant Canvas, les utilisateurs ne seront redirigés que lorsque le délai de l’étape sera écoulé. Supposons que vous supprimiez un composant de délai d’un jour et redirigiez ces utilisateurs sur un composant de Message. Dans ce cas, les utilisateurs ne seront redirigés que lorsque le délai d’un jour est écoulé.

Si votre Canvas contient un ou plusieurs composants de [Chemins d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/), supprimer des composants peut invalider les résultats de ce composant.

### Arrêter des Canvas

Arrêter un Canvas ne fera pas sortir les utilisateurs qui attendent dans une étape. Si vous réactivez le Canvas et que les utilisateurs attendent toujours, ils finiront l’étape et passeront au composant suivant. Cependant, si le délai durant lequel l’utilisateur aurait dû passer au composant suivant est dépassé, il quittera le Canvas. 

Supposons que vous avez créé un Canvas créé à l’aide du workflow Canvas Flow, paramétré pour être exécuté à 14 h 00 avec une variante et deux étapes : un composant de délai d’une heure, puis une étape de Message. 

Un utilisateur entre dans ce Canvas à 14 h 01 et entre dans le composant de délai en même temps. Cela signifie que l’utilisateur sera planifié pour passer à l’étape suivante du parcours utilisateur (le composant de message) à 15 h 01. Si vous arrêtez le Canvas à 14 h 30 et que vous le réactivez à 15 h 30, l’utilisateur quittera Canvas puisque 15 h 01 est passée. Cependant, si vous réactivez le Canvas à 14 h 40, l’utilisateur passera au composant de message, comme prévu, à 15 h 01.
