---
nav_title: Fondamentaux de Canvas
article_title: Fondamentaux de Canvas
page_order: 1
page_type: reference
description: "Cet article de référence aborde les fondamentaux de Canvas, notamment diverses questions que vous devez vous poser lorsque vous configurez votre premier Canvas."
tool: Canvas

---

# Fondamentaux de Canvas

> Cet article de référence aborde les fondamentaux de Canvas, notamment diverses questions que vous devez vous poser lorsque vous configurez votre premier Canvas.

## Comprendre la structure d’un Canvas

Avant d’aborder les détails plus précis du [paramétrage Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), commençons par identifier les éléments clés constituant un Canvas.

{% tabs %}
  {% tab Canvas %}
  Une interface Canvas est une interface unifiée où les marketeurs peuvent implémenter des campagnes comportant plusieurs messages et des étapes pour former un parcours cohérent.

  {% endtab %}

  {% tab Journey %}

  Un parcours, généralement appelé « parcours client », désigne une expérience utilisateur spécifique dans le Canvas.<br><br> ![]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Entry Wizard %}
  L’assistant d’entrée comprend les premières étapes à effectuer lors de la création de votre Canvas. Il contient des bases comme le fait de donner un nom à votre Canvas et d’ajouter des équipes. L’assistant d’entrée constitue donc le paramétrage fondamental nécessaire avant de commencer à créer votre Canvas. Vous pouvez contrôler à cet endroit la manière dont vos utilisateurs commencent et terminent leur parcours utilisateur avec des options permettant de modifier la [planification d’entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), l’[audience ciblée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) et les [paramètres d’envoi]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings).<br><br> ![]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variants %}
  Une variante désigne le chemin que chaque utilisateur suit au cours de son parcours. Canvas prend en charge jusqu’à huit variantes avec un groupe de contrôle. Vous pouvez nommer chaque variante et contrôler la répartition de l’audience cible, suivant chaque variante.<br><br> ![]({% image_buster /assets/img_archive/canvas_flow_variants.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Steps %}
  Une étape dans un Canvas est un point de décision marketing déterminant votre parcours utilisateur. Vous pouvez tirer parti des [composant Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) pour construire les étapes de votre parcours utilisateur.<br>Dans une étape, vous pouvez définir des déclencheurs ou planifier une livraison, affiner le ciblage en ajoutant des filtres ou en marquant des [événements d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) et ajouter des canaux à partir d’e-mails, notifications push et webhooks.<br><br> ![]({% image_buster /assets/img_archive/canvas_flow_step.png %}){: style="max-width:90%;"}

  {% endtab %}
{% endtabs %}

## Création du parcours client

En utilisant les « cinq W » de la visualisation, vous pouvez identifier les stratégies d’engagement de votre client concernant la manière de créer un parcours de messages personnalisés pour chaque utilisateur. Ces « cinq W » sont : What (quoi), When (quand), Who (qui), Why (quand) et Where (où). 

### Le « quoi » : Nommez votre Canvas

> Qu’essayez-vous de faire faire ou comprendre à votre utilisateur ?

Ne sous-estimez jamais le pouvoir du nom. Braze est conçu pour la collaboration, c’est donc le moment idéal pour évaluer la façon dont vous communiquez les objectifs à votre équipe. 

Vous pouvez ajouter des balises et nommer les étapes et les variantes dans le Canvas. Pour en savoir plus sur les parcours client, consultez notre Cours d’apprentissage Braze sur le [mappage des cycles de vie utilisateur](https://learning.braze.com/mapping-customer-lifecycles) !

### Le « pourquoi » : Identifier des événements de conversion

> En partant du « quoi », pourquoi construisez-vous ce Canvas ? 

Il est toujours important d’avoir un objectif défini en tête et Canvas vous permet de comprendre comment vous vous situez par rapport aux KPI tels que l’engagement de session, les achats et les événements personnalisés.

Sélectionner au moins un [événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) vous donnera la possibilité de comprendre comment optimiser les performances de votre Canvas. Et si votre Canvas a plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif.

* **Lancer la session** : Je souhaite que mes utilisateurs reviennent et interagissent avec l’application.
* **Effectuer un achat** : Je souhaite que mes utilisateurs achètent.
* **Effectuer un événement personnalisé** : Je souhaite que mes utilisateurs effectuent une action spécifique pour laquelle je réalise un suivi comme événement personnalisé.
* **Mises à niveau d’application** : Je souhaite que mes utilisateurs mettent à niveau leur version d’application.

### Le « quand » : Créer des conditions de démarrage

> Quand (When) un utilisateur commencera-t-il cette expérience ?

Votre réponse va déterminer les détails : (quand et comment) votre Canvas va être livré à votre client. Les utilisateurs peuvent accéder à votre Canvas de deux façons : par une planification ou des déclencheurs basés sur un événement.

{% alert tip %}
Pour plus de stratégies et trouver des réponses aux questions fréquentes, consultez les [fonctionnalités basées sur le temps]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/) pour Canvas.
{% endalert %}

La livraison planifiée vous permet d’envoyer un Canvas immédiatement à votre audience cible. Vous pouvez aussi le faire envoyer régulièrement ou le planifier à une date précise dans l’avenir. Les Canvas par événement répondent à des comportements des clients spécifiques, lorsqu’ils se produisent. Par exemple, un déclencheur par événement peut inclure l’ouverture d’une application, un achat effectué, l’interaction avec une autre campagne ou le déclenchement d’un événement personnalisé. Au moment où l’événement se produit, le Canvas est envoyé à vos utilisateurs.

### Le « qui » : Sélectionnez une audience

> Qui (Who) essayez-vous de joindre ? 

Pour définir votre « qui », vous pouvez utiliser les segments prédéfinis disponibles dans Canvas. Vous pouvez également ajouter plus de filtres pour pouvoir mieux vous concentrer sur l’interaction avec votre audience cible. Après avoir construit ces segments, seuls les utilisateurs qui correspondent au critère d’audience cible peuvent entrer dans le parcours Canvas, ce qui entraîne une expérience plus personnalisée. Consultez ce tableau pour y trouver les filtres disponibles ainsi que la manière dont ils segmentent vos utilisateurs pour correspondre à votre cas d’utilisation.

| Filtre | Description |
|---|---|
| Données personnalisées | Segmentez les utilisateurs en fonction d’événements et d’attributs que vous définissez. Vous pouvez utiliser des fonctionnalités spécifiques pour votre produit. |
| Activité de l’utilisateur | Segmentez les clients sur la base de leurs actions et de leurs achats. |
| Reciblage | Segmentez des clients qui ont envoyé, reçu ou interagi avec des Canvas précédents. |
| Activité de marketing | Segmentez des clients selon des comportements universels, tels que le dernier engagement. |
| Attributs utilisateur | Segmentez les clients en fonction de leurs caractéristiques et attributs constants. |
| Attribution d’installation | Segmentez les clients en fonction de leur première source, groupe d’annonces, campagne ou annonce. |
{: .reset-td-br-1 .reset-td-br-2}

### Le « où » : Trouver mon audience

> Où puis-je atteindre au mieux mon audience ? 

C’est l’endroit où nous déterminons quels canaux de communication sont les plus pertinents pour votre parcours utilisateur. Nous voudrions, dans l’absolu, atteindre vos utilisateurs là où ils sont les plus actifs. En gardant cela à l’esprit, vous pouvez utiliser un des canaux suivants avec Canvas :
* [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [Messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS ou MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### Le « comment » : Construire l’expérience complète

> Comment puis-je construire mon parcours Canvas après avoir identifié les cinq W ?

Le « comment » résume la manière dont vous allez créer votre Canvas et comment vous allez atteindre vos utilisateurs avec votre message. Par exemple, pour qu’un message soit efficace, vous devriez optimiser le timing de votre envoi de messages en fonction des fuseaux horaires de vos différents utilisateurs.

Répondre au « comment » détermine également la cadence d’envoi d’un Canvas à votre audience (c.-à-d., une fois par semaine, deux fois par semaine, etc.) et ainsi que les canaux de communication à exploiter pour chacun des Canvas que vous construisez, tel que décrit dans le « où ». 

## Conseils généraux

### Déterminer quand et comment utiliser des étapes et des variantes

Chaque Canvas doit avoir au moins une variante et au moins une étape. Il n’y a pas de limites, comment définissez-vous donc la forme de votre Canvas ? C’est à ce niveau que vos objectifs, données et hypothèses entrent en jeu. La réflexion « how » (comment) et « where » (où) vous aidera à tracer la forme appropriée et la structure de votre Canvas.

### Travailler à contresens

Certains objectifs ont des sous-objectifs identiques. Par exemple, si votre objectif est de convaincre un utilisateur libre à s’abonner, vous aurez besoin d’un document indiquant vos services d’abonnement. Un visiteur doit voir les options avant d’acheter. Vous devez mettre en avant cette page avant une page de paiement. Travailler à contresens pour comprendre le parcours d’un client va de pair avec la réalisation de votre objectif, élément clé pour la conversion.

### Panacher vos envois de messages

Avez-vous déjà réalisé une campagne identique dans le passé ? Ou est-ce la première que vous menez ? Essayez d’utiliser ce message et d’y ajouter plus de personnalisation. Essayez un nouveau filtre ou ajoutez un message de réponse. Quand vous panachez vos techniques d’envois de message, surveillez vos performances et continuez à optimiser en effectuant des modifications incrémentielles.
