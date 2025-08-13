---
nav_title: À propos des cartes de contenu
article_title: À propos des cartes de contenu
page_order: 0
description: "Le présent article de référence présente le canal Carte de contenu de Braze avec des cas d’utilisation courants."
channel:
  - content cards
search_rank: 4
---

# [![Cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} À propos des cartes de contenu

> Les cartes de contenu sont intégrées directement dans votre application ou votre site web afin que vous puissiez engager les utilisateurs dans une expérience sur laquelle ils se sentent naturels et homogènes. Ils vous donnent plus de contrôle sur l'expérience sur votre app ou votre site web, et vous permettent de créer des boîtes de réception de messages, des carrousels et des bannières, et d'étendre la portée d'autres canaux (tels que l'e-mail ou les notifications push).

Les cartes de contenu sont une fonctionnalité supplémentaire et doivent être achetées. Pour démarrer avec les cartes de contenu, contactez votre gestionnaire du succès des clients ou l’équipe support de Braze.

## Avantages de l'utilisation des cartes de contenu

Voici quelques avantages de l'utilisation des cartes de contenu par rapport au fait de demander à vos développeurs de créer du contenu dans votre application :

- **Une segmentation et une personnalisation plus faciles :** Vos données utilisateur résident dans Braze, ce qui facilite la définition de votre audience et la personnalisation de vos messages avec les cartes de contenu.
- **Rapports centralisés :** Les analyses/analytiques des cartes de contenu sont suivies dans Braze, ce qui vous permet d'avoir des informations sur toutes vos campagnes en un seul emplacement/localisation.
- **Des parcours clients cohérents :** Vous pouvez combiner des cartes de contenu avec d’autres canaux dans Braze pour créer des expériences client cohérentes. Un cas d’utilisation populaire consiste à envoyer une notification push, puis à enregistrer cette notification en tant que carte de contenu dans votre application pour tous ceux qui n’ont pas interagi avec la notification push. Si le contenu est créé directement dans votre application par vos développeurs, il est alors isolé du reste de votre envoi de messages.
- **Aucun abonnement n'est requis :** Comme pour les messages in-app, les cartes de contenu ne nécessitent pas d’abonnement ou d’autorisations de la part de vos utilisateurs. Mais alors que les messages in-app sont sans permission et éphémères, les cartes de contenu sont sans permission et permanentes. Cela signifie que les stratégies d'envoi de messages qui associent les messages in-app et les cartes de contenu trouvent un excellent équilibre.
- **Plus de contrôle sur l'expérience de l'envoi de messages :** Bien que vous ayez toujours besoin de l'aide de vos développeurs pour la configuration initiale des cartes de contenu, vous pouvez ensuite contrôler le message, les destinataires, le calendrier et bien plus encore, directement depuis votre tableau de bord de Braze.

### Les cartes de contenu en chiffres

Parce que vous, le marketeur, créez vous-même les cartes de contenu dans Braze, vous pouvez faire des mises à jour de messages et bénéficier d'un retour sur investissement sans avoir à refondre complètement votre application ou votre site web. Voici quelques statistiques utiles sur le RSI des cartes de contenu :

- Les cartes de contenu sont **38 fois** plus efficaces que les e-mails pour stimuler les ventes sur une période de 72 heures.[^1]
- L'utilisation de cartes de contenu lors des campagnes d’inscription à un programme de fidélité multiplie les conversions **par 5**.[^1]
- L'envoi aux utilisateurs de messages de sensibilisation par le biais de notifications push, de messages in-app et de cartes de contenu se traduit par **6,9X** plus de sessions, par rapport aux utilisateurs engagés uniquement par le biais du push[^2].]
- L'envoi aux utilisateurs d'actions de sensibilisation par e-mail, de messages in-app et de cartes de contenu se traduit par une durée de vie moyenne des utilisateurs **3,6 fois plus** longue que celle des utilisateurs engagés par le seul biais de l'e-mail[^2.]

## Fonctionnement

Les cartes de contenu sont en fait une charge utile de données, et non pas ce à quoi ressemblent les données. Braze fournit des vues de modèle (bannière, modale, image avec légende) pour afficher les données de la carte de contenu, ce qui est finalement ce à quoi ressemble votre message.

Maintenant, passons à la technique. En coulisses, une carte de contenu comporte trois parties principales :

- **Modèle :** Le type de données contenu dans la carte
- **Voir :** À quoi ressemble la carte
- **Contrôleur :** Comment l’utilisateur interagit avec la carte

Dans le cas d'une implémentation par défaut, vous ajoutez le contenu de la carte - le modèle - à partir du tableau de bord ou par l'intermédiaire d'API, et la vue et le contrôleur sont gérés par ce que l'on appelle un contrôleur de vue. Un contrôleur de vue est la « colle » entre l’application dans son ensemble et l’écran.

## Cas d’utilisation

Consultez cette section pour connaître quelques cas d'utilisation courants des cartes de contenu.

{% alert tip %}
Pour plus d'inspiration, nous vous recommandons vivement de consulter notre [Guide d'inspiration des cartes de contenu](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), qui comprend plus de 20 campagnes personnalisables, notamment des programmes de recommandation, des lancements de nouveaux produits et des renouvellements d'abonnement.
{% endalert %}

{% tabs %}
{% tab Onboarding et étapes suivantes %}

Lorsque de nouveaux utilisateurs explorent votre application et votre site web, faites-leur découvrir les valeurs et les avantages de ce que vous proposez grâce à des cartes de contenu placées à des endroits stratégiques. Encouragez les utilisateurs à s'abonner à d'autres canaux de communication avec une carte de contenu sur votre page d'accueil, et enregistrez les tâches d'onboarding en suspens dans un onglet dédié à l'onboarding alimenté par des cartes de contenu. N'oubliez pas de retirer une carte lorsque l'utilisateur a accompli la tâche souhaitée !

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Participation à l'événement %}

Présentez les cartes de contenu en haut de la page d'accueil d'un utilisateur pour encourager la participation à un événement, en utilisant le ciblage par emplacement/localisation pour atteindre les utilisateurs potentiels là où ils se trouvent. Inviter les utilisateurs à des événements physiques pertinents est valorisant pour eux, surtout si vous leur envoyez des communications personnalisées qui tirent parti de leur activité précédente avec votre marque.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommandations %}

Utilisez les données dont vous disposez sur les comportements et les préférences des utilisateurs pour faire apparaître le contenu pertinent en temps réel depuis les cartes de contenu de la page d’accueil ou de la boîte de réception et les attirer à nouveau vers vos offres de produits.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Ventes et promotions %}

Tirez parti des cartes de contenu pour mettre en avant les messages promotionnels et les offres non réclamées directement sur votre page d’accueil ou dans une boîte de réception promotionnelle dédiée. Faites apparaître le contenu pertinent en fonction des achats précédents de chaque client pour proposer des promotions personnalisées qui attirent l’attention.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Autres cas d’utilisation

En dehors de ces principaux cas d’utilisation, nos clients utilisent les cartes de contenu de nombreuses façons différentes. La puissance des cartes de contenu réside dans leur flexibilité. Si le cas d'utilisation que vous souhaitez n'est pas indiqué ici, vous pouvez configurer des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) et envoyer les charges utiles à votre app ou site web.

## Placements des cartes de contenu

Cette section couvre les trois façons les plus courantes de placer les cartes de contenu dans votre application ou votre site web :

- [Boîte de réception de messages](#message-inbox)
- [Carrousel](#carousel)
- [Bannière](#banner)

La logique et la mise en œuvre de ces placements ne sont pas une option par défaut dans Braze, de sorte que votre équipe d'ingénieurs doit fournir et prendre en charge le travail nécessaire pour réaliser ces cas d'utilisation. Pour un aperçu de la manière de mettre en œuvre ces placements, reportez-vous à la section [Création d'une carte de contenu personnalisée]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

![3 exemples de cartes de contenu, montrant les différentes options de placement : boîte de réception des messages, carrousel et bannière.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Boîte de réception de messages

![Exemple de carte de contenu utilisant l'emplacement "boîte de réception".]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Une boîte de réception de messages (également appelée centre de notification ou flux) est un emplacement persistant dans votre application ou votre site Web où vous pouvez afficher les cartes de contenu dans le format que vous préférez. Chaque message dans la boîte de réception constitue sa propre carte de contenu. 

La boîte de réception des messages est une implémentation par défaut qui ne nécessite qu'un minimum de développement. Braze fournit un [contrôleur de vue](#how-it-works) pour une boîte de réception de messages sur iOS, Android et web afin de faciliter le processus de création.

#### Avantages

- Les utilisateurs peuvent recevoir de nombreuses cartes en un seul endroit
- Moyen efficace de faire resurgir des informations manquées ou écartées sur d'autres canaux (notamment les notifications push).
- Aucun abonnement n’est requis

#### Comportement

Lorsqu’un utilisateur est éligible à une carte, elle apparaîtra automatiquement dans sa boîte de réception. Les cartes de contenu sont créées pour être consultées en bloc, de sorte que les utilisateurs peuvent consulter en une seule fois toutes les cartes auxquelles ils peuvent prétendre.

Avec la mise en œuvre par défaut, les cartes de contenu dans la boîte de réception peuvent apparaître comme des cartes classiques (contenant un titre, du texte et une image facultative), des cartes contenant uniquement une image ou des cartes contenant une image légendée. Vous choisissez l’emplacement de la boîte de réception des messages dans votre application.

Les cartes de contenu sont fournies avec un style par défaut, mais vous pouvez choisir une implémentation personnalisée pour afficher les cartes et le flux en fonction de l’apparence de votre application.

### Carrousel

![Exemple de carte de contenu utilisant le placement "carrousel".]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Les carrousels affichent plusieurs éléments de contenu dans un seul emplacement que vos clients peuvent balayer pour l’afficher. Il peut s'agir d'un diaporama d'images, de texte, de vidéo ou d'une combinaison de ces éléments. Il s’agit d’une implémentation personnalisée qui nécessite un peu de travail de la part de vos développeurs.

#### Avantages

- Les utilisateurs peuvent recevoir de nombreuses cartes en un seul endroit
- Faire des recommandations intéressantes

#### Comportement

Lorsqu’un utilisateur est éligible à une carte, elle apparaîtra dans un carrousel sur la page de votre application à laquelle le carrousel est ajouté. Les utilisateurs peuvent faire le faire glisser horizontalement pour afficher des cartes mises en vedette supplémentaires.

Étant donné qu’il s’agit d’une implémentation personnalisée, vous devrez travailler avec vos développeurs pour créer vos propres vues afin d’afficher les cartes de contenu. Les cartes classiques par défaut, les cartes avec image seulement et les cartes avec image légendée ne sont pas prises en charge par cette implémentation.

### Bannière

![Exemple de carte de contenu utilisant le placement "bannièree".]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Les cartes de contenu peuvent apparaître sous la forme d’une bannière dynamique qui s’affiche constamment sur votre page d’accueil ou en haut d’autres pages désignées.

#### Avantages

- Persiste sur la page contrairement à un message in-app, vous offrant donc plus de temps pour atteindre votre audience
- Excellent moyen de présenter de nouveaux contenus dans un endroit clairement visible sur votre page d’accueil

#### Comportement

Les utilisateurs peuvent afficher le contenu le plus pertinent auquel ils sont éligibles et s’engager vis à vis de lui. Étant donné qu’il s’agit d’une implémentation personnalisée, vous devrez travailler avec vos développeurs pour personnaliser vos vues afin d’afficher les cartes de contenu.

## Intégrer des cartes de contenu

Vos développeurs intégreront les cartes de contenu lorsqu’ils intégreront le SDK Braze. Pour plus de détails sur l’intégration avec les cartes de contenu, consultez les articles du guide du développeur pour votre plateforme :

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## Sources

<span></span>

[^1]: [8 conseils pour tirer le meilleur parti de vos campagnes de rétention des clients](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Rapport : La différence du marketing cross-canal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)