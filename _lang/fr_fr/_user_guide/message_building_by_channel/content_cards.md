---
nav_title: Cartes de contenu
article_title: Cartes de contenu
page_order: 1
layout: dev_guide
guide_top_header: "Cartes de contenu"
guide_top_text: "Avec les cartes de contenu, vous pouvez envoyer un flux dynamique très ciblé de contenu enrichi à vos clients au sein des applications qu'ils aiment, sans interrompre leur expérience. <br><br>Les cartes de contenu sont intégrées directement dans votre application ou votre site web, ce qui vous permet de créer des boîtes réception de messages et des interfaces personnalisées qui étendent la portée d'autres canaux tels que l'e-mail ou les notifications push. En outre, les cartes de contenu prennent en charge des fonctionnalités plus personnalisées, notamment l'épinglage des cartes, la fermeture des cartes, la réception/distribution basée sur l'API, le contenu connecté, les délais d'expiration personnalisés des cartes, l'analyse des cartes et la coordination aisée avec les notifications push. <br><br>**La disponibilité des cartes de contenu dépend de votre paquetage Braze. Contactez votre gestionnaire de compte ou votre responsable satisfaction client pour commencer.**."
description: "Cette page d'atterrissage accueille les cartes de contenu de Braze. Vous y trouverez des articles sur la création d'une carte de contenu, la personnalisation de vos cartes de contenu, les tests, les rapports, etc."
channel:
  - content cards
search_rank: 5
guide_featured_title: "Articles de section"
guide_featured_list:
- name: Créer une carte de contenu
  link: /docs/user_guide/message_building_by_channel/content_cards/create/
  image: /assets/img/braze_icons/columns-01.svg
- name: Création de cartes
  link: /docs/user_guide/message_building_by_channel/content_cards/create/card_creation
  image: /assets/img/braze_icons/message-check-circle.svg
- name: Détails créatifs
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/
  image: /assets/img/braze_icons/brush-02.svg
- name: Essais
  link: /docs/user_guide/message_building_by_channel/content_cards/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Rapports
  link: /docs/user_guide/message_building_by_channel/content_cards/reporting/
  image: /assets/img/braze_icons/pie-chart-01.svg
- name: Meilleures pratiques
  link: /docs/user_guide/message_building_by_channel/content_cards/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
---

## ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Avantages de l'utilisation des cartes de contenu

Voici quelques avantages de l'utilisation des cartes de contenu par rapport au fait de demander à vos développeurs de créer du contenu dans votre application :

- **Une segmentation et une personnalisation plus faciles :** Les données de vos utilisateurs sont en ligne/en production/instantanée dans Braze, ce qui facilite la définition de votre audience et la personnalisation de vos messages avec les cartes de contenu.
- **Rapports centralisés :** Les analyses/analytiques des cartes de contenu sont suivies dans Braze, ce qui vous permet d'avoir des informations sur toutes vos campagnes en un seul emplacement/localisation.
- **Des parcours clients cohérents :** Vous pouvez combiner les cartes de contenu avec d'autres canaux dans Braze pour créer des expériences client cohérentes. Un cas d'utilisation courant est l'envoi d'une notification push, puis l'enregistrement de cette notification en tant que carte de contenu dans votre application pour tous ceux qui n'ont pas réagi à la notification push. Si le contenu est créé directement dans votre application par vos développeurs, il est alors isolé du reste de votre envoi de messages.
- **Aucun abonnement n'est requis :** À l'instar des messages in-app, les cartes de contenu ne nécessitent pas d'abonnement ou d'autorisation de la part de vos utilisateurs. Mais alors que les messages in-app sont sans permission et éphémères, les cartes de contenu sont sans permission et permanentes. Cela signifie que les stratégies d'envoi de messages qui associent les messages in-app et les cartes de contenu trouvent un excellent équilibre.
- **Plus de contrôle sur l'expérience de l'envoi de messages :** Bien que vous ayez toujours besoin de l'aide de vos développeurs pour la configuration initiale des cartes de contenu, vous pouvez par la suite contrôler le message, les destinataires, le calendrier et bien plus encore, directement depuis votre tableau de bord de Braze.

### Les cartes de contenu en chiffres

Parce que vous, le marketeur, créez vous-même les cartes de contenu dans Braze, vous pouvez faire des mises à jour de messages et bénéficier d'un retour sur investissement sans avoir à refondre complètement votre application ou votre site web. Voici quelques statistiques utiles sur le ROI des cartes de contenu :

- Les cartes de contenu sont **38 fois** plus efficaces que les e-mails pour stimuler les ventes sur une fenêtre de 72 heures[^1].
- L'utilisation de cartes de contenu dans les campagnes de fidélisation augmente les conversions de **5 fois**[^1].
- L'envoi aux utilisateurs d'actions de sensibilisation par le biais de notifications push, de messages in-app et de cartes de contenu se traduit par **6,9X** plus de sessions, par rapport aux utilisateurs engagés par le seul biais du push[^2].
- L'envoi aux utilisateurs d'actions de sensibilisation par e-mail, de messages in-app et de cartes de contenu se traduit par une durée de vie moyenne des utilisateurs **3,6X** plus longue, par rapport aux utilisateurs engagés uniquement par e-mail[^2].

## Comment cela fonctionne-t-il ?

Braze propose différents types de cartes de contenu pour afficher la carte de contenu : Classique, Image légendée ou Image. À la base, les cartes de contenu sont en fait une charge utile de données, et non ce à quoi les données ressemblent. 

Soyons un peu plus techniques. En coulisses, une carte de contenu se compose de trois parties principales :

- **Modèle :** Quelles sont les données en ligne/en production/instantanée dans la carte ?
- **Voir :** A quoi ressemble la carte
- **Contrôleur :** Comment l'utilisateur interagit avec la carte

Dans le cas d'une implémentation par défaut, vous ajoutez le contenu de la carte - le modèle - à partir du tableau de bord ou par le biais d'API, et la vue et le contrôleur sont gérés par ce que l'on appelle un contrôleur de vue. Le contrôleur de vue est la "colle" entre l'application globale et l'écran.

## Cas d'utilisation

Consultez cette section pour connaître quelques cas d'utilisation courants des cartes de contenu.

{% alert tip %}
Pour plus d'inspiration, nous vous recommandons vivement de consulter notre [Guide d'inspiration des cartes de contenu](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), qui comprend plus de 20 campagnes personnalisables, notamment des programmes de recommandation, des lancements de nouveaux produits et des renouvellements d'abonnement.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

Lorsque de nouveaux utilisateurs explorent votre application et votre site web, faites-leur découvrir les valeurs et les avantages de ce que vous proposez à l'aide de cartes de contenu placées à des endroits stratégiques. Encouragez les utilisateurs à s'abonner à d'autres canaux de communication avec une carte de contenu sur votre page d'accueil, et enregistrez les tâches d'onboarding en suspens dans un onglet dédié à l'onboarding alimenté par des cartes de contenu. N'oubliez pas de retirer une carte lorsque l'utilisateur a accompli la tâche souhaitée !

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event attendance %}

Présentez les cartes de contenu en haut de la page d'accueil d'un utilisateur pour encourager la participation à un événement, en utilisant le ciblage par emplacement/localisation pour atteindre les utilisateurs potentiels là où ils se trouvent. En invitant les utilisateurs à des événements physiques pertinents, ils se sentent spéciaux, notamment grâce à des envois de messages personnalisés qui tirent parti de leur activité antérieure avec votre marque.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

Utilisez les données dont vous disposez sur les comportements et les préférences des utilisateurs pour faire apparaître en temps réel un contenu pertinent à partir des cartes de contenu de la page d'accueil ou de la boîte de réception et les inciter à revenir vers votre offre de produits.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

Profitez des cartes de contenu pour mettre en avant les messages promotionnels et les offres non réclamées directement sur votre page d'accueil ou dans une boîte de réception promotionnelle dédiée. Faites appel à du contenu pertinent basé sur les achats précédents de chaque client pour proposer des promotions personnalisées qui attirent l'attention.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Autres cas d'utilisation

En dehors de ces cas d'utilisation principaux, nos clients utilisent les cartes de contenu de multiples façons. La force des cartes de contenu réside dans leur flexibilité. Si le cas d'utilisation que vous souhaitez n'est pas indiqué ici, vous pouvez configurer des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) et envoyer les charges utiles à votre app ou site web.

## Cartes de contenu dans votre application

Cette section couvre les façons les plus courantes de placer les cartes de contenu dans votre application ou votre site web :

- [Boîte de réception des messages](#message-inbox)
- [Carrousel](#carousel)

La logique et la mise en œuvre de ces placements ne sont pas une option par défaut dans Braze, de sorte que votre équipe d'ingénieurs doit fournir et prendre en charge le travail pour réaliser ces cas d'utilisation. Pour un aperçu de la manière de mettre en œuvre ces placements, reportez-vous à la section [Création d'une carte de contenu personnalisée]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

[3 exemples de cartes de contenu, montrant les différentes options de placement : boîte de réception des messages, carrousel et bannière.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Boîte de réception des messages

Un exemple de carte de contenu utilisant l'envoi de la boîte de réception.]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Une boîte de réception des messages (également appelée centre de notification ou flux) est un endroit persistant dans votre application ou votre site web où vous pouvez afficher les cartes de contenu dans le format que vous préférez. Chaque message de la boîte de réception constitue sa propre carte de contenu. 

La boîte de réception des messages est une implémentation par défaut qui ne nécessite qu'un minimum de développement. Braze fournit un [contrôleur de vue](#how-it-works) pour une boîte de réception de messages sur iOS, Android et web afin de faciliter le processus de création.

#### Avantages

- Les utilisateurs peuvent recevoir plusieurs cartes en un seul endroit
- Moyen efficace de faire resurgir des informations manquées ou écartées sur d'autres canaux (notamment les notifications push).
- Pas d'abonnement nécessaire

#### Comportement

Lorsqu'un utilisateur est éligible pour une carte, celle-ci apparaît automatiquement dans sa boîte de réception. Les cartes de contenu sont créées pour être consultées en bloc, de sorte que les utilisateurs peuvent consulter en une seule fois toutes les cartes auxquelles ils peuvent prétendre.

Avec la mise en œuvre par défaut, les cartes de contenu dans la boîte de réception peuvent apparaître comme des cartes classiques (contenant un titre, du texte et une image facultative), des cartes contenant uniquement une image ou des cartes contenant une image légendée. Vous choisissez l'emplacement de la boîte de réception des messages dans votre application.

Les cartes de contenu sont livrées avec un style par défaut, mais vous pouvez choisir une implémentation personnalisée pour afficher les cartes et le flux en fonction de l'aspect et de la convivialité de votre application.

### Carrousel

Un exemple de carte de contenu utilisant le placement "carrousel".]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Les carrousels affichent plusieurs éléments de contenu dans un espace unique que vos clients peuvent faire glisser pour les voir. Il peut s'agir d'un diaporama d'images, de texte, de vidéo ou d'une combinaison de ces éléments. Il s'agit d'une mise en œuvre personnalisée qui nécessite un peu de travail de la part de vos développeurs.

#### Avantages

- Les utilisateurs peuvent recevoir plusieurs cartes en un seul endroit
- Une façon attrayante de faire remonter les recommandations

#### Comportement

Lorsqu'un utilisateur est éligible pour une carte, celle-ci apparaît dans un carrousel sur la page de votre application à laquelle le carrousel est ajouté. Les utilisateurs peuvent balayer horizontalement pour afficher d'autres cartes en fonctionnalité.

Comme il s'agit d'une mise en œuvre personnalisée, vous devrez travailler avec vos développeurs pour créer vos propres vues afin d'afficher les cartes de contenu. Les cartes classiques par défaut, les cartes avec image seulement et les cartes avec image légendée ne sont pas prises en charge par cette implémentation.

## Intégration des cartes de contenu

Vos développeurs intégreront les cartes de contenu lorsqu'ils intégreront le SDK de Braze. Pour plus de détails sur l'intégration avec les cartes de contenu, consultez les articles du guide du développeur de votre plateforme :

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## Sources d'information

<span></span>

[^1] : [8 conseils pour tirer le meilleur parti de vos campagnes de rétention des clients](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2] : [Rapport : La différence du marketing cross-canal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
