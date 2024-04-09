---
nav_title: À propos des cartes de contenu
article_title: À propos des cartes de contenu
page_order: 0
description: "Le présent article de référence présente le canal Carte de contenu de Braze avec des cas d’utilisation courants."
channel:
  - cartes de contenu
search_rank: 4
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} À propos des cartes de contenu

> Les cartes de contenu sont un canal qui est intégré directement à l’interface de votre application ou de votre site Web afin que vous puissiez engager les utilisateurs d’une manière ressemblant à une expérience native et harmonieuse. Vous pouvez réaliser beaucoup de choses avec les cartes de contenu, mais les implémentations les plus courantes sont une boîte de réception de message, un carrousel ou une bannière.

Les cartes de contenu sont idéales pour étendre la portée d’autres canaux, comme les notifications par e-mail ou push, et elles vous donnent plus de contrôle sur l’expérience offerte par l’application ou le site Web.

{% alert note %}
Nous recommandons aux clients qui utilisent notre fil d'actualité de passer à notre canal de communication de Cartes de contenu. Il est plus flexible, plus personnalisable et plus fiable. Le Fil d’actualité est obsolète. Voir notre [Guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) ou contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

Les cartes de contenu sont une fonctionnalité supplémentaire et doivent être achetées. Pour démarrer avec les cartes de contenu, contactez votre gestionnaire du succès des clients ou l’équipe support de Braze.

## Avantages des cartes de contenu

Quels sont les avantages d’utiliser des cartes de contenu plutôt que de demander à vos développeurs d’intégrer le contenu dans votre appli ? En voici quelques-uns :

- **Segmentation et personnalisation simplifiées :** Vos données utilisateur résident dans Braze, ce qui facilite la définition de votre audience et la personnalisation de vos messages avec les cartes de contenu.
- **Reporting centralisé :** Les métriques des performances des cartes de contenu sont suivies dans Braze, vous avez donc des informations sur toutes vos campagnes dans un emplacement centralisé.
- **Parcours clients cohésifs :** Vous pouvez combiner des cartes de contenu avec d’autres canaux dans Braze pour créer des expériences client cohérentes. Un cas d’utilisation populaire consiste à envoyer une notification push, puis à enregistrer cette notification en tant que carte de contenu dans votre application pour tous ceux qui n’ont pas interagi avec la notification push. Si le contenu est intégré directement à votre application par vos développeurs, alors il est « isolé » du reste de vos communications.
- **Les cartes de contenu ne nécessitent pas d’abonnement :** Comme pour les messages in-app, les cartes de contenu ne nécessitent pas d’abonnement ou d’autorisations de la part de vos utilisateurs. Bien que les messages in-app soient sans autorisation mais de courte durée, les cartes de contenu sont sans autorisation et permanentes. Cela signifie que les stratégies de communication qui associent les messages in-app et les cartes de contenu atteignent un excellent équilibre.
- **Plus de contrôle sur l’expérience de communication :** Vous aurez toujours besoin de vos développeurs pour vous aider dans la configuration initiale des cartes de contenu, après cela, vous pourrez contrôler le message, les destinataires, le calendrier et plus encore depuis votre tableau de bord de Braze.

### Les cartes de contenu en chiffres

Étant donné que vous, le marketeur, créez vous-même des cartes de contenu dans Braze, vous pouvez effectuer des mises à jour de communication et recevoir un retour sur investissement sans avoir à remanier complètement votre application ou votre site. Voici quelques statistiques utiles sur le RSI des cartes de contenu :

- Les cartes de contenu sont **38 fois** plus efficaces que les e-mails pour stimuler les ventes sur une période de 72 heures.[^1]
- L’utilisation de cartes de contenu lors des campagnes d’inscription à un programme de fidélité **multiplie par 5** les conversions.[^1]
- L’envoi d’informations aux utilisateurs via notifications push, de messages in-app et de cartes de contenu entraîne **6,9 fois** plus de sessions que pour les utilisateurs engagés uniquement via des notifications push.[^2]
- L’envoi d’informations aux utilisateurs par e-mail, messages in-app et cartes de contenu entraîne une durée de vie moyenne de l’utilisateur **3,6 fois** plus longue, par rapport aux utilisateurs engagés uniquement par e-mail.[^2]

## Cas d’utilisation

Cette section décrit certains cas d’utilisation courants pour les cartes de contenu.

{% alert tip %}
Pour plus d’inspiration, nous vous recommandons vivement de consulter notre [Guide d’inspiration des cartes de contenu](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), qui comprend plus de 20 campagnes personnalisables, y compris des programmes de recommandation, des lancements de nouveaux produits et le renouvellement d’abonnement.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

À mesure que de nouveaux clients explorent votre application et votre site Web, présentez-leur la valeur et les avantages de ce que vous offrez à l’aide de cartes de contenu placées stratégiquement. Encouragez les clients à d’abonner à d’autres canaux de communication avec une carte de contenu sur votre page d’accueil et enregistrez les tâches d’onboarding en cours dans un onglet d’onboarding dédié alimenté par des cartes de contenu. N’oubliez pas de retirer une carte une fois qu’un client a effectué la tâche souhaitée !

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

Présentez les cartes de contenu en haut de la page d’accueil d’un utilisateur pour encourager la participation à un événement, en utilisant le ciblage de localisation pour atteindre les clients potentiels où qu’ils se trouvent. Inviter les utilisateurs à des événements physiques pertinents les fait se sentir spéciaux, en particulier en utilisant des communications personnalisées qui tirent partie de leur activité précédente avec votre marque.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

Utilisez les données dont vous disposez sur les comportements et les préférences des utilisateurs pour faire apparaître le contenu pertinent en temps réel depuis les cartes de contenu de la page d’accueil ou de la boîte de réception et les attirer à nouveau vers vos offres de produits.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

Tirez parti des cartes de contenu pour mettre en avant les messages promotionnels et les offres non réclamées directement sur votre page d’accueil ou dans une boîte de réception promotionnelle dédiée. Faites apparaître le contenu pertinent en fonction des achats précédents de chaque client pour proposer des promotions personnalisées qui attirent l’attention.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Autres cas d’utilisation

En dehors de ces principaux cas d’utilisation, nos clients utilisent les cartes de contenu de nombreuses façons différentes. La puissance des cartes de contenu réside dans leur flexibilité. Si le cas d’utilisation que vous souhaitez ne s’affiche pas ici, vous pouvez configurer des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) et faire envoyer les charges utiles à votre application ou à votre site.

## Placements des cartes de contenu

Cette section présente les trois manières les plus courantes de placer des cartes de contenu dans votre application ou votre site :

- [Boîte de réception de messages](#message-inbox)
- [Carrousel](#carousel)
- [Bannière](#banner)

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Boîte de réception de messages

![]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Une boîte de réception de messages (également appelée centre de notification ou flux) est un emplacement persistant dans votre application ou votre site Web où vous pouvez afficher les cartes de contenu dans le format que vous préférez. Chaque message dans la boîte de réception constitue sa propre carte de contenu. 

La boîte de réception de messages est une implémentation par défaut avec un développement minimal nécessaire. Nous fournissons un [contrôleur d’affichage](#how-content-cards-work) pour une boîte de réception sur iOS, Android ou sur le Web qui facilite la mise en place de cette fonctionnalité, alimentée par des cartes de contenu.

#### Avantages

- Les utilisateurs peuvent recevoir de nombreuses cartes en un seul endroit
- Il s’agit d’un moyen facile de resurfacer les informations manquées ou rejetées sur d’autres canaux (en particulier les notifications push)
- Aucun abonnement n’est requis

#### Comportement

Lorsqu’un utilisateur est éligible à une carte, elle apparaîtra automatiquement dans sa boîte de réception. Les cartes de contenu sont intrinsèquement conçues pour être visualisées en grande quantité, de sorte que les utilisateurs pourront voir toutes les cartes auxquelles ils sont éligibles en une fois.

Avec l’implémentation par défaut, les cartes de contenu dans la boîte de réception peuvent apparaître sous forme de cartes classiques, de type bannière ou d’images avec légende. Vous choisissez l’emplacement de la boîte de réception des messages dans votre application.

Les cartes de contenu sont fournies avec un style par défaut, mais vous pouvez choisir une implémentation personnalisée pour afficher les cartes et le flux en fonction de l’apparence de votre application.

### Carrousel

![]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Les carrousels affichent plusieurs éléments de contenu dans un seul emplacement que vos clients peuvent balayer pour l’afficher. Il peut s’agir d’un diaporama d’images, de textes, de vidéos ou d’un ensemble de toutes ces options. Il s’agit d’une implémentation personnalisée qui nécessite un peu de travail de la part de vos développeurs.

#### Avantages

- Les utilisateurs peuvent recevoir de nombreuses cartes en un seul endroit
- Faire des recommandations intéressantes

#### Comportement

Lorsqu’un utilisateur est éligible à une carte, elle apparaîtra dans un carrousel sur la page de votre application à laquelle le carrousel est ajouté. Les utilisateurs peuvent faire le faire glisser horizontalement pour afficher des cartes mises en vedette supplémentaires.

Étant donné qu’il s’agit d’une implémentation personnalisée, vous devrez travailler avec vos développeurs pour créer vos propres vues afin d’afficher les cartes de contenu. Les cartes classiques, bannières et d’images avec légende par défaut ne sont pas prises en charge avec cette implémentation.

Pour connaître la procédure d’implémentation, reportez-vous à la [vue carrousel]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/use_cases/carousel_view/).

### Bannière

![]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Les cartes de contenu peuvent apparaître sous la forme d’une bannière dynamique qui s’affiche constamment sur votre page d’accueil ou en haut d’autres pages désignées.

#### Avantages

- Persiste sur la page contrairement à un message in-app, vous offrant donc plus de temps pour atteindre votre audience
- Excellent moyen de présenter de nouveaux contenus dans un endroit clairement visible sur votre page d’accueil

#### Comportement

Les utilisateurs peuvent afficher le contenu le plus pertinent auquel ils sont éligibles et s’engager vis à vis de lui. Étant donné qu’il s’agit d’une implémentation personnalisée, vous devrez travailler avec vos développeurs pour personnaliser vos vues afin d’afficher les cartes de contenu.

## Fonctionnement des cartes de contenu

Les cartes de contenu sont en fait une charge utile de données, et non pas ce à quoi ressemblent les données. Braze fournit des vues de modèle (bannière, modale, image avec légende) pour afficher les données de la carte de contenu, ce qui est finalement ce à quoi ressemble votre message.

Maintenant, passons à la technique. En coulisses, une carte de contenu comporte trois parties principales :

- **Modèle :** Le type de données contenu dans la carte
- **Affichage :** À quoi ressemble la carte
- **Contrôleur :** Comment l’utilisateur interagit avec la carte

Pour une implémentation d’origine, vous ajoutez le contenu de la carte, le modèle, soit à partir du tableau de bord, soit via des API. La vue et le contrôleur sont gérés par ce que l’on appelle un contrôleur de vue.

### Contrôleur de vue

Un contrôleur de vue est la « colle » entre l’application dans son ensemble et l’écran. Il contrôle les affichages qu’il possède en fonction de la logique de votre application. Chaque application en a un, certaines en ont plusieurs.

Les cartes de contenu Braze disposent de leur propre contrôleur de vue, ce qui signifie que vous pouvez intégrer des cartes de contenu en ajoutant quelques lignes de code à votre application ou à votre site. Vos développeurs peuvent également créer un contrôleur d’affichage de carte de contenu personnalisé au lieu d’utiliser le contrôleur Braze standard pour encore plus d’options de personnalisation.

## Intégrer des cartes de contenu

Vos développeurs intégreront les cartes de contenu lorsqu’ils intégreront le SDK Braze. Pour plus de détails sur l’intégration avec les cartes de contenu, consultez les articles du guide du développeur pour votre plateforme :

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/integration/ "iOS Content Card Integration Guide")
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/ "Android Content Card Integration Guide")
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/ "Web Content Card Integration Guide")

## Sources

<span></span>

[^1]: [8 Tips for Making the Most of Your Customer Retention Campaigns](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Report: The Cross-Channel Marketing Difference](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
