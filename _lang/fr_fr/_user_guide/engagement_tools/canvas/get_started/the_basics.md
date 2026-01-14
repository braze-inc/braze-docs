---
nav_title: Les bases de la toile
article_title: Les bases de la toile
page_order: 1
page_type: reference
description: "Cet article de référence couvre les bases de Canvas, en abordant les différentes questions que vous devriez vous poser lors de la mise en place de votre premier Canvas."
tool: Canvas

---

# Les bases de la toile

> Cet article de référence couvre les bases de Canvas, en abordant les différentes questions que vous devriez vous poser lors de la mise en place de votre premier Canvas. Nous expliquerons également les cinq W (quoi, quand, qui, pourquoi et où) de la visualisation et la manière dont ils peuvent façonner et définir la façon dont vous pouvez créer votre Canvas.

## Comprendre la structure de Canvas

Avant d'aborder les détails de la [configuration d'un]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) canvas, identifions les éléments clés qui le composent.

{% tabs %}
  {% tab Canvas %}
  Canvas est une interface unifiée où les marketeurs conçoivent des campagnes avec plusieurs messages. C'est un peu comme un outil de programmation visuelle, qui vous permet de créer un parcours utilisateur cohérent à partir d'une série d'étapes.

  Un exemple de Canvas avec une étape de l'arbre décisionnel en deux parcours utilisateur différents selon que l'utilisateur est activé ou non pour le push.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Journey %}

  Un parcours, ou communément appelé parcours de l'utilisateur, est l'expérience d'un utilisateur individuel au sein du Canvas.<br><br> Un graphique présentant le parcours client d'un nouvel utilisateur. Un utilisateur anonyme installe une application, Kat crée un compte, Kat n'ouvre pas l'application pendant une semaine, une notification push ramène Kat à l'application, puis Kat utilise l'application régulièrement.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Canvas Builder %}
  Le générateur de canvas mappe les étapes du canvas. Il s'agit notamment de donner un nom à votre Canvas et d'ajouter des équipes. Le générateur de canevas est essentiellement la configuration essentielle requise avant de commencer à créer votre canevas. Ici, vous pouvez contrôler la façon dont vos utilisateurs commencent et accomplissent leur parcours client grâce à des options permettant de modifier la [planification des entrées]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), l'[audience cible]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) et les [paramètres d'envoi.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings)<br><br> \![Le générateur de canevas sur la section Basics pour un canevas nommé "New Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variants %}
  Une variante est le chemin que suit chaque client dans son parcours. Canvas prend en charge jusqu'à huit variantes avec un groupe de contrôle. Vous contrôlez le segment de votre audience qui suivra chaque variante.<br><br> \![Sélection du bouton "Ajouter une variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Steps %}
  Une étape du canvas est un point de décision marketing : "si ceci, alors cela". Tirez parti des [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) pour créer les étapes d'un parcours utilisateur.<br><br> \![Exemple d'ajout d'une étape du canevas (Delay).]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Lorsqu'un utilisateur entre dans un canvas, il commence par la première étape. Chaque étape est assortie de conditions qui déterminent si l'utilisateur peut passer à l'étape suivante. Au sein d'une étape, vous pouvez définir des déclencheurs ou planifier la réception/distribution, affiner le ciblage en ajoutant des filtres ou en marquant des événements d'exception, et spécifier différents canaux comme les notifications push ou les événements webhook. Dans Canvas, les étapes se déroulent dans l'ordre, c'est-à-dire que la première étape se produit avant que la seconde ne puisse avoir lieu. Supposons que nous ayons un canvas avec les étapes suivantes : Retardez l'étape A avec un délai de 24 heures, envoyez un message à l'étape A avec un message push et envoyez un message in-app à l'étape B. L'utilisateur A est retenu dans un délai de 24 heures, puis, au bout de 24 heures, il recevra un message push, puis un message in-app.

  {% endtab %}
{% endtabs %}

## Créer le parcours client

L'utilisation des cinq W (quoi, quand, qui, pourquoi et où) de la visualisation peut aider à identifier vos stratégies d'engagement client pour savoir comment créer un parcours de message personnalisé pour chacun de vos utilisateurs.

### Le "quoi" : Nommez votre canvas

> Qu'essayez-vous d'aider l'utilisateur à faire ou à comprendre ?

Ne sous-estimez jamais le pouvoir du nom. Braze est créé pour la collaboration, c'est donc le bon moment pour vous familiariser avec la façon dont vous communiquerez les objectifs à votre équipe.

Vous pouvez ajouter des tags et nommer les étapes et les variantes d'un Canvas. Pour en savoir plus sur les parcours clients, consultez notre cours d'apprentissage Braze sur le [mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles).

### Le "pourquoi" : Identifier les événements de conversion

> En partant du "quoi", pourquoi construisez-vous ce Canvas ? 

Il est toujours important d'avoir un objectif défini en tête et Canvas vous aide à comprendre vos performances par rapport à des indicateurs clés de performance tels que l'engagement des sessions, les achats et les événements personnalisés.

La sélection d'au moins un [événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) vous permettra de comprendre comment optimiser les performances au sein du Canvas. Et si votre Canvas comporte plusieurs variantes ou un groupe de contrôle, Braze utilisera l'événement de conversion pour déterminer la meilleure variation permettant d'atteindre cet objectif.

* **Début de la session**: Je veux que mes utilisateurs reviennent et s'engagent dans l'application.
* **Effectuez vos achats**: Je veux que mes utilisateurs achètent.
* **Exécuter un événement personnalisé**: Je souhaite que mes utilisateurs effectuent une action spécifique que j'enregistre en tant qu'événement personnalisé.
* **Améliorations App :** Je veux que mes utilisateurs mettent à jour la version de leur application.

### Le "quand" : Créer des conditions de départ

> Quand l'utilisateur commencera-t-il cette expérience ?

Votre réponse déterminera les détails de la livraison de votre Canvas à votre client. Les utilisateurs peuvent entrer dans votre Canvas de deux manières : par des déclencheurs planifiés ou par des déclenchements basés sur des actions.

{% alert tip %}
Consultez la rubrique [Fonctionnalités temporelles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) pour Canvas pour obtenir davantage de stratégies et de réponses aux questions les plus courantes.
{% endalert %}

La réception/distribution planifiée vous permet d'envoyer immédiatement un canvas à votre audience cible. Vous pouvez également l'envoyer régulièrement ou le planifier pour un moment précis dans le futur. Les toiles basées sur l'action répondent à des comportements spécifiques des clients au fur et à mesure qu'ils se produisent. Par exemple, un déclencheur basé sur une action peut inclure l'ouverture d'une appli, un achat, une interaction avec une autre campagne ou le déclenchement de tout événement personnalisé. Au moment où l'action se produit, vous pouvez envoyer le canvas à vos utilisateurs.

### Le "qui" : Sélectionnez une audience

> Qui cherchez-vous à atteindre ? 

Pour définir votre "qui", vous pouvez utiliser des segmentations prédéfinies disponibles dans Canvas. Vous pouvez également ajouter d'autres filtres pour vous concentrer davantage sur la connexion avec votre audience ciblée. Après avoir créé ces segments, seuls les utilisateurs qui correspondent aux critères de l'audience cible peuvent entrer dans le parcours Canvas, ce qui conduit à une expérience plus personnalisée. Consultez ce tableau pour connaître les filtres disponibles et la façon dont ils segmentent vos utilisateurs en fonction de votre cas d'utilisation.

| Filtre              | Description                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Données personnalisées         | Segmentez les utilisateurs en fonction des événements et des attributs que vous définissez. Peut utiliser des fonctionnalités spécifiques à votre produit. |
| Activité de l'utilisateur       | Segmentez les clients en fonction de leurs actions et de leurs achats.                                             |
| Reciblage         | Segmentez les clients qui ont été envoyés, reçus ou qui ont interagi avec des canevas précédents.               |
| Activité de marketeur  | Segmentez les clients en fonction de comportements universels tels que le dernier engagement.                         |
| Attributs de l'utilisateur     | Segmenter les clients en fonction de leurs attributs et caractéristiques constants.                                 |
| Attribution d'installation | Segmentez les clients en fonction de leur première source, du groupe d'annonces, de la campagne ou de l'annonce.                                 |

### Le "où" : Trouver mon audience

> Où puis-je atteindre au mieux mon audience ? 

C'est ici que nous déterminons quels canaux de communication sont les plus judicieux pour votre parcours utilisateur. Idéalement, vous souhaitez atteindre vos utilisateurs là où ils sont le plus accessibles. Dans cette optique, vous pouvez utiliser l'un des canaux suivants avec Canvas :
* [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Pousser]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [Messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS ou MMS]({{site.baseurl}}/about_sms/)
* [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### Le "comment" : Créer une expérience complète

> Comment créer mon parcours Canvas après avoir identifié les cinq W ?

Le "comment" résume collectivement la manière dont vous allez créer votre Canvas et dont vous allez transmettre votre message à vos utilisateurs. Par exemple, pour qu'un message soit efficace, vous devez optimiser le moment de l'envoi de vos messages en fonction des fuseaux horaires de vos différents utilisateurs.

La réponse à la question " comment " détermine également la cadence d'envoi d'un Canvas à votre audience (par exemple une fois par semaine ou toutes les deux semaines), et les canaux d'envoi de messages à exploiter pour chaque Canvas que vous créez, comme décrit avec la question " où ".

## Cas d'utilisation : Flux d'onboarding des clients

Par exemple, disons que vous êtes marketeur pour MovieCanon, une société de services de streaming en ligne, et que vous êtes chargé de créer un flux d'onboarding pour les nouveaux utilisateurs de votre application. En nous référant aux cinq W, nous pourrions créer le Canvas de la manière suivante.

* **Quoi**? Le nom de notre canvas sera "New Onboarding Journey".
* **Pourquoi**? L'objectif de notre Canvas est d'accueillir nos utilisateurs et de faire en sorte qu'ils continuent à s'engager dans l'application.
* **Quand**: Lorsqu'un utilisateur ouvre l'application pour la première fois, nous voulons lui envoyer un e-mail de bienvenue. 
* **Qui**: Nous ciblons les nouveaux utilisateurs qui utilisent notre appli pour la première fois.
* **Où**? Nous sommes convaincus que nous pouvons atteindre les nouveaux utilisateurs par l'intermédiaire de leur e-mail, comme nous l'avons fait pour tous nos envois de messages antérieurs.
* **Comment**? Nous souhaitons fixer un délai d'un jour afin de ne pas submerger nos nouveaux utilisateurs de notifications. Passé ce délai, nous leur enverrons un e-mail contenant une liste des films et émissions de télévision les plus populaires pour les inciter à continuer à utiliser l'appli.

## Conseils généraux

### Déterminer quand et comment utiliser les étapes et les variantes

Chaque canvas doit comporter au moins une variante et au moins une étape. À partir de là, les possibilités sont infinies. Comment décidez-vous de la forme de votre toile ? C'est ici que vos objectifs, vos données et vos hypothèses entrent en jeu. Le brainstorming sur le "comment" et le "où" vous aidera à mapper la forme et la structure de votre Canvas.

### Travailler à l'envers

Certains objectifs sont assortis de sous-objectifs plus modestes. Par exemple, si votre objectif est de convertir un utilisateur gratuit en abonné, vous aurez peut-être besoin d'une page décrivant vos services d'abonnement. Un visiteur peut avoir besoin de voir les options avant d'acheter. Vous pouvez concentrer vos efforts d'envoi de messages sur la présentation de cette page avant une page de paiement. Travailler à rebours pour comprendre le parcours qu'un client doit effectuer pour atteindre votre objectif est essentiel pour le guider jusqu'à la conversion.

### Mélangez vos messages

Avez-vous mené une campagne similaire dans le passé ? Ou y en a-t-il un en cours ? Essayez d'utiliser ce message unique et de le personnaliser davantage. Essayez un nouveau filtre ou ajoutez un message de suivi. Au fur et à mesure que vous modifiez vos techniques d'envoi de messages, surveillez vos performances et continuez à les optimiser en procédant à des changements progressifs.
