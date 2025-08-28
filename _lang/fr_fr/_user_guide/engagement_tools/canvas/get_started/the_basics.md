---
nav_title: Fondamentaux de Canvas
article_title: Fondamentaux de Canvas
page_order: 1
page_type: reference
description: "Cet article de référence couvre les bases de Canvas, en abordant diverses questions que vous devriez vous poser lors de la configuration de votre premier Canvas."
tool: Canvas

---

# Fondamentaux de Canvas

> Cet article de référence couvre les bases de Canvas, en abordant diverses questions que vous devriez vous poser lors de la configuration de votre premier Canvas. Nous expliquerons également les cinq W (quoi, quand, qui, pourquoi et où) de la visualisation et comment cela peut façonner et définir comment vous pouvez construire votre Canvas.

## Comprendre la structure d’un Canvas

Avant de commencer avec les détails plus fins de [la configuration de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), identifions les éléments clés qui composent un Canvas.

{% tabs %}
  {% tab Canvas %}
  Canvas est une interface unifiée où les marketeurs conçoivent des campagnes avec plusieurs messages. C'est un peu comme un outil de programmation visuelle, vous permettant de créer un parcours utilisateur cohérent à partir d'une série d'étapes.

  ![Exemple d'un canvas avec une étape de l'arbre décisionnel en deux parcours utilisateurs différents selon que l'utilisateur est ou non "push enabled".]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Parcours %}

  Un parcours, généralement appelé « parcours client », désigne une expérience utilisateur spécifique dans le Canvas.<br><br> ![Un graphique présentant le parcours client d'un nouvel utilisateur. Un utilisateur anonyme installe une application, Kat crée un compte, Kat n'ouvre pas l'application pendant une semaine, une notification push ramène Kat à l'application, puis Kat utilise l'application régulièrement.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Générateur de canvas %}
  Le constructeur de Canvas cartographie les étapes à suivre lors de la création de votre Canvas. Il contient des bases comme le fait de donner un nom à votre Canvas et d’ajouter des équipes. Globalement, le générateur de canvas constitue la configuration fondamentale requise avant de commencer à créer votre canvas. Ici, vous pouvez contrôler la façon dont vos utilisateurs commencent et accomplissent leur parcours client avec des options pour modifier le [calendrier d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), [public cible]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) et [paramètres d'envoi]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings).<br><br> ![Le générateur de Canvas dans la section Basics pour un Canvas nommé "New Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variantes %}
  Une variante désigne le chemin que chaque utilisateur suit au cours de son parcours. Canvas prend en charge jusqu’à huit variantes avec un groupe de contrôle. Vous contrôlez quel segment de votre audience suivra chaque variante.<br><br> ![Sélectionnez le bouton "Ajouter une variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Étapes %}
  Une étape dans Canvas est un point de décision marketing : « si ceci, alors cela ». Tirez parti des [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) pour construire les étapes d'un parcours utilisateur.<br><br> ![Exemple d'ajout d'une étape de retardement à une toile.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Lorsqu'un utilisateur entre dans un canvas, il commence par la première étape. Chaque étape est assortie de conditions qui déterminent si l'utilisateur peut passer à l'étape suivante. Au sein d'une étape, vous pouvez définir des déclencheurs ou planifier la réception/distribution, affiner le ciblage en ajoutant des filtres ou en marquant des événements d'exception, et spécifier différents canaux comme les notifications push ou les événements webhook. Dans Canvas, les étapes se déroulent dans l'ordre, c'est-à-dire que la première étape se produit avant que la seconde ne puisse avoir lieu. Supposons que nous ayons un canvas avec les étapes suivantes : Retardez l'étape A avec un délai de 24 heures, envoyez un message à l'étape A avec un message push et envoyez un message in-app à l'étape B. L'utilisateur A est retenu dans un délai de 24 heures, puis, au bout de 24 heures, il recevra un message push, puis un message in-app.

  {% endtab %}
{% endtabs %}

## Création du parcours client

En utilisant les cinq W (quoi, quand, qui, pourquoi et où) de la visualisation, vous pouvez identifier vos stratégies d'engagement client pour créer un parcours de message personnalisé pour chacun de vos utilisateurs.

### Le « quoi » : Nommez votre Canvas

> Qu’essayez-vous de faire faire ou comprendre à votre utilisateur ?

Ne sous-estimez jamais le pouvoir du nom. Braze est conçu pour la collaboration, c’est donc le moment idéal pour évaluer la façon dont vous communiquez les objectifs à votre équipe.

Vous pouvez ajouter des balises et nommer les étapes et les variantes dans un Canvas. Pour en savoir plus sur les parcours client, consultez notre cours Braze Learning sur [la cartographie des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles).

### Le « pourquoi » : Identifier des événements de conversion

> En partant du « quoi », pourquoi construisez-vous ce Canvas ? 

Il est toujours important d’avoir un objectif défini en tête et Canvas vous permet de comprendre comment vous vous situez par rapport aux KPI tels que l’engagement de session, les achats et les événements personnalisés.

Sélectionner au moins un [événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) vous donnera la possibilité de comprendre comment optimiser les performances dans le Canvas. Et si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif.

* **Démarrer la session**: Je souhaite que mes utilisateurs reviennent et interagissent avec l’application.
* **Effectuer un achat** : Je souhaite que mes utilisateurs achètent.
* **Effectuer un événement personnalisé**: Je souhaite que mes utilisateurs effectuent une action spécifique pour laquelle je réalise un suivi comme événement personnalisé.
* **Mises à niveau d’application :** Je souhaite que mes utilisateurs mettent à niveau leur version d’application.

### Le « quand » : Créer des conditions de démarrage

> Quand (When) un utilisateur commencera-t-il cette expérience ?

Votre réponse va déterminer les détails : (quand et comment) votre Canvas va être livré à votre client. Les utilisateurs peuvent accéder à votre Canvas de deux façons : par une planification ou des déclencheurs basés sur un événement.

{% alert tip %}
Découvrez les [fonctionnalités basées sur le temps]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) pour Canvas pour plus de stratégies et de réponses aux questions courantes.
{% endalert %}

La livraison planifiée vous permet d’envoyer un Canvas immédiatement à votre audience cible. Vous pouvez aussi le faire envoyer régulièrement ou le planifier à une date précise dans l’avenir. Les Canvas par événement répondent à des comportements des clients spécifiques, lorsqu’ils se produisent. Par exemple, un déclencheur par événement peut inclure l’ouverture d’une application, un achat effectué, l’interaction avec une autre campagne ou le déclenchement d’un événement personnalisé. Au moment où l’événement se produit, le Canvas est envoyé à vos utilisateurs.

### Le « qui » : Sélectionnez une audience

> Qui (Who) essayez-vous de joindre ? 

Pour définir votre « qui », vous pouvez utiliser les segments prédéfinis disponibles dans Canvas. Vous pouvez également ajouter plus de filtres pour pouvoir mieux vous concentrer sur l’interaction avec votre audience cible. Après avoir créé ces segments, seuls les utilisateurs qui correspondent au critère d’audience cible peuvent entrer dans le parcours Canvas, ce qui entraîne une expérience plus personnalisée. Consultez ce tableau pour y trouver les filtres disponibles ainsi que la manière dont ils segmentent vos utilisateurs pour correspondre à votre cas d’utilisation.

| Filtre              | Description                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Données personnalisées         | Segmentez les utilisateurs en fonction d’événements et d’attributs que vous définissez. Vous pouvez utiliser des fonctionnalités spécifiques pour votre produit. |
| Activité de l’utilisateur       | Segmentez les clients sur la base de leurs actions et de leurs achats.                                             |
| Reciblage         | Segmentez des clients qui ont envoyé, reçu ou interagi avec des Canvas précédents.               |
| Activité de marketing  | Segmentez des clients selon des comportements universels, tels que le dernier engagement.                         |
| Attributs utilisateur     | Segmentez les clients en fonction de leurs caractéristiques et attributs constants.                                 |
| Attribution d’installation | Segmenter les clients par leur première source, groupe d'annonces, campagne ou annonce.                                 |

### Le « où » : Trouver mon audience

> Où puis-je atteindre au mieux mon audience ? 

C’est l’endroit où nous déterminons quels canaux de communication sont les plus pertinents pour votre parcours utilisateur. Nous voudrions, dans l’absolu, atteindre vos utilisateurs là où ils sont les plus actifs. En gardant cela à l’esprit, vous pouvez utiliser un des canaux suivants avec Canvas :
* [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [in-app Messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS ou MMS]({{site.baseurl}}/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### Le « comment » : Créer l’expérience complète

> Comment puis-je créer mon parcours Canvas après avoir identifié les cinq W ?

Le « comment » résume la manière dont vous allez créer votre Canvas et comment vous allez atteindre vos utilisateurs avec votre message. Par exemple, pour qu'un message soit efficace, vous devez optimiser le moment de votre message en fonction des fuseaux horaires de vos différents utilisateurs.

Répondre à "comment" détermine également la cadence d'envoi d'un Canvas à votre audience (par exemple, une fois par semaine ou toutes les deux semaines), et quels canaux de messagerie utiliser pour chaque Canvas que vous créez comme décrit avec le "où."

## Cas d’utilisation : flux d'onboarding des clients

Par exemple, disons que vous êtes un marketeur pour MovieCanon, une entreprise de services de streaming en ligne, et que vous êtes chargé de créer un flux d'intégration pour les nouveaux utilisateurs de votre application. En nous référant aux « cinq W », à savoir What (quoi), When (quand), Who (qui), Why (quand) et Where (où), nous pourrions créer le canvas de la manière suivante.

* **Quoi**: Notre nom de canvas sera « Nouveau parcours d’onboarding ».
* **Pourquoi**: Le but de notre Canvas est d'accueillir nos utilisateurs et de les inciter à continuer à s'engager avec l'application.
* **Quand**: Après qu'un utilisateur ouvre l'application pour la première fois, nous voulons lui envoyer un e-mail pour lui souhaiter la bienvenue. 
* **Qui**: Nous ciblons les nouveaux utilisateurs qui utilisent notre application pour la première fois.
* **Où**: Nous sommes convaincus que nous pouvons atteindre de nouveaux utilisateurs par le biais de leur e-mail, ce qui est la façon dont nous avons fait tous nos messages précédents.
* **Comment**: Nous voulons fixer un délai d'un jour afin de ne pas submerger nos nouveaux utilisateurs de notifications. Après ce délai, nous enverrons un e-mail avec une liste des films et émissions de télévision les plus populaires pour les inciter à continuer à utiliser l'application.

## Conseils généraux

### Déterminer quand et comment utiliser des étapes et des variantes

Chaque Canvas doit avoir au moins une variante et au moins une étape. Il n’y a pas de limites, comment définissez-vous donc la forme de votre Canvas ? C’est à ce niveau que vos objectifs, données et hypothèses entrent en jeu. La réflexion « how » (comment) et « where » (où) vous aidera à tracer la forme appropriée et la structure de votre Canvas.

### Travailler à contresens

Certains objectifs ont des sous-objectifs identiques. Par exemple, si votre objectif est de convaincre un utilisateur libre à s’abonner, vous aurez besoin d’un document indiquant vos services d’abonnement. Un visiteur doit voir les options avant d’acheter. Vous devez mettre en avant cette page avant une page de paiement. Travailler à contresens pour comprendre le parcours d’un client va de pair avec la réalisation de votre objectif, élément clé pour la conversion.

### Panacher vos envois de messages

Avez-vous déjà réalisé une campagne identique dans le passé ? Ou est-ce la première que vous menez ? Essayez d’utiliser ce message et d’y ajouter plus de personnalisation. Essayez un nouveau filtre ou ajoutez un message de réponse. Quand vous panachez vos techniques d’envois de message, surveillez vos performances et continuez à optimiser en effectuant des modifications incrémentielles.
