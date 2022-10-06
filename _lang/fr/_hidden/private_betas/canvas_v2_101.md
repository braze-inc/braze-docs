---
nav_title: Canvas V2 101
permalink: /canvas_v2_101/
description: "Cet article décrit à quoi s’attendre en utilisant Canvas V2, notamment les différences entre les versions V1 et V2 de Canvas."
hidden: true
---

# Canvas V2 101

## Qu’est-ce que Canvas V2 ?

Le workflow Canvas V2 est la nouvelle expérience d'édition améliorée qui simplifie la façon dont les spécialistes du marketing peuvent développer et gérer leurs parcours d'utilisateur Canvas. Avec Canvas V2, vous pouvez facilement voir et utiliser les [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components) dans le générateur de Canvas 

{% alert important %}
Canvas V2 est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## À quoi dois-je m’attendre ?

Lorsque vous utilisez Canvas V2, vous pouvez :
* Étapes complètes à remplacer par des composants Canvas légers
* Les [propriétés d’entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) sont disponibles pour la personnalisation des messages tout au long du parcours utilisateur
* Après le lancement, de nouvelles fonctions de modification permettront de modifier les connexions entre les étapes, de supprimer les étapes et les variantes, et de rediriger les utilisateurs vers différentes étapes
* Une nouvelle barre d’outils Canvas qui affiche tous les composants Canvas
* Un [outil de clonage]({{site.baseurl}}/cloning_canvases/) qui vous permet de cloner vos dessins interrompus vers Canvas V2. Les Canvas existants dans V1 ne seront pas modifiés ni supprimés.
* **Bientôt disponible :** Une nouvelle façon de faire un zoom avant et arrière entre les vues complètes et des icônes de Canvas

Pour utiliser le workflow Canvas V2, allez dans **Canvas** dans l’onglet **Engagement**. Cliquez sur <i class="fas fa-plus"></i> **Create Canvas** (Créer un Canvas). Ensuite, vous aurez la possibilité de générer avec Canvas V2 ou d’essayer l’expérience Canvas originale. Sélectionnez **Worflow Canvas V2** et commencez à créer votre Canvas comme vous le feriez normalement !

![][1]{: style="max-width:85%"}

Lorsque vous générez ou modifiez votre Canvas, si vous souhaitez revenir à Canvas V1, cliquez sur **Switch to Canvas V1 Workflow** (Basculer sur le workflow Canvas V1) en bas de l’éditeur Canvas ou en haut du générateur de Canvas. 

{% alert note %}
Basculer de Canvas V2 à V1 est possible uniquement si vous n’utilisez pas les fonctions Canvas V2. Basculer de Canvas V1 à V2 ne fonctionnera que s’il n’y a aucune Étapes complètes dans votre Canvas V1.
{% endalert %}

## Qu’adviendra-t-il de mes Canvas créées à l’aide de Canvas V1 ?

Tous vos Canvas existants et la version actuelle de Canvas (Canvas V1) continueront d’exister et seront pris en charge par Braze. Les clients qui choisissent de rejoindre Canvas V2 en accès anticipé auront la possibilité de créer un Canvas en utilisant le workflow Canvas V1 ou V2.

## Quelles sont les principales différences entre Canvas V2 et Canvas V1 ?

### Barre d’outils de Canvas Step

Auparavant avec le workflow Canvas V1, une étape complète était ajoutée par défaut chaque fois que vous ajoutiez une étape dans votre parcours utilisateur. Maintenant avec Canvas V2, ces étapes complètes sont remplacées par différents composants Canvas, vous offrant ainsi une meilleure visibilité et personnalisation pour apporter des modifications. Vous pouvez immédiatement voir tous vos composants Canvas dans la barre d’outils de Canvas Step.

### Création de branche

Les étapes dans Canvas V2 peuvent [créer des branches]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/branching/), ou se diviser en plusieurs étapes, uniquement en utilisant des étapes de parcours telles que [Parcours d’audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) ou [Parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Ces étapes ont une taille maximale de branche de sept groupes et un groupe Tout le monde. Pour plus de sept groupes, créez simplement une autre étape de parcours connectée au groupe Tout le monde.

### Comportement des étapes

Auparavant avec le workflow Canvas V1, chaque étape complète comprenait des informations telles que les paramètres de délai et de planification, les événements d’exception, les filtres d’audience, la configuration des messages et les options d’avancement des messages en une seule étape. Plus tard, ces paramètres seront séparés. Cela rend votre expérience de création d’étape Canvas plus personnalisable et vous propose également des différences de fonctionnalité.

### Avancement de l’étape Message

Les [étapes Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) font progresser tous les utilisateurs qui franchissent l’étape. Il n’est pas nécessaire de spécifier le comportement d’avancement des messages, ce qui facilite la configuration de l’étape. Si vous souhaitez implémenter l’option **Avancement lors de l’envoi du message**, ajoutez une étape de parcours d’audience distincte pour filtrer les utilisateurs qui n’ont pas reçu l’étape précédente.  

### Délai du comportement « dans »

[Étapes de délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) attendra l’intégralité du délai avant de passer à l’étape suivante. 

Par exemple, le 12 avril, nous avons une étape de délai avec un délai défini de sorte que l’utilisateur est transféré sur l’étape suivante un jour plus tard, à 14h00. Un utilisateur saisit l’étape à 14h01 le 13 avril. 
- Pour Canvas V1, l’utilisateur passe à l’étape suivante à 14h00 le 14 avril, moins d’un jour après l’entrée. 
- Pour Canvas V2, l’utilisateur passera à l’étape suivante à 14h00 le 15 avril. Notez qu’il s’agit de la même heure, mais plus d’un jour après l’heure d’entrée. 

### Comportement du Timing Intelligent

Puisque [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) est stocké dans l’étape Message, les délais seront appliqués avant les calculs Timing Intelligent. Cela signifie que, en fonction de l’heure à laquelle l’utilisateur accède à l’étape, il peut recevoir le message plus tard que dans un Canvas V1.

Pour Canvas V2, l’étape de délai retardera d’abord le message en fonction du nombre de jours préalablement défini. Ensuite, dès que le nombre de jours est écoulé, l’utilisateur commencera à recevoir des messages à partir du Timing Intelligent défini. Par exemple, si votre étape de délai a une durée définie sur deux jours et vous utilisez la fonctionnalité Timing Intelligent, il faut 48 heures pour que le Timing intelligent s’applique et pour que l’envoi des messages commence. Pour Canvas V1, si l’étape complète inclut un délai d’un jour, le message sera envoyé le deuxième jour à l’heure définie par le Timing Intelligent. 

Par exemple, le 12 avril, nous avons une étape de délai définie pour transférer un utilisateur sur l’étape suivante, après un jour avec Timing Intelligent. Un utilisateur saisit l’étape à 14h01 le 13 avril et le timing intelligent pour le canal de communication donné est 14h00. 
- Pour Canvas V1, l’utilisateur reçoit le message à 14h00 le 14 avril, moins d’un jour après l’entrée. 
- Pour Canvas V2, l’utilisateur reçoit le message à 14h00 le 15 avril, plus d’un jour après l’entrée.

### Événements d'exception

#### Heures calmes

La fonctionnalité d’événement d’exception dans Canvas V2 fonctionne avec les parcours d’action, distincts des étapes Message. Les heures calmes sont appliquées dans l’étape Message. Cela signifie que si un utilisateur a déjà franchi l'étape du parcours d'action (et n'a pas été exclu par l'événement d'exception à cet endroit), qu'il a atteint les heures calmes lorsqu'il est arrivé à l'étape Message, et que son Canvas a été configuré de telle sorte que le message soit renvoyé après la période des heures calmes, l'événement d'exception ne sera plus appliqué. Notez que ce cas d’utilisation n’est pas fréquent.

Pour les segments et filtres, l’étape Message Canvas V2 comporte une nouvelle fonction appelée Validations de livraison qui permet aux utilisateurs de configurer des segments supplémentaires et des filtres validés au moment de l’envoi. Cela empêche le cas susmentionné avec les heures calmes.

#### Réglage de la planification « dans » ou « suivant »/« prochain »

Les événements d’exception dans Canvas V2 sont créés avec des parcours d’action. Les chemins d’action prennent uniquement en charge « après une fenêtre X temps » et non « dans X temps » ou « le X suivant/prochain ».


[1]: {% image_buster /assets/img_archive/canvas_v2_experience.png %}
