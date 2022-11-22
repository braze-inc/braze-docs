---
nav_title: À propos des cartes de contenu
article_title: À propos des cartes de contenu
page_order: 0
description: "Le présent article de référence présente le canal Carte de contenu de Braze avec des cas d’utilisation courants."
channel:
  - cartes de contenu

---

# [![Cours d’apprentissage Braze]{% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} À propos des cartes de contenu

> Le présent article de référence présente le canal Carte de contenu de Braze avec des cas d’utilisation courants.

{% multi_lang_include video.html id="4FUPxkIq2xc" align="right" %}

Avec les cartes de contenu, vous pouvez envoyer à vos clients un flux dynamique et hautement ciblé de contenu riche, dans les applications qu’ils aiment et sans interrompre leur expérience. De plus, les cartes de contenu prennent en charge des fonctionnalités plus personnalisées, notamment l’épinglage et la fermeture de carte de contenu, la livraison basée sur API, les délais personnalisés pour l’expiration des cartes, les métriques des performances et la coordination facile avec les notifications push.

Les cartes de contenu ne sont pas disponibles en standard, elles doivent être achetées. Pour démarrer avec les cartes de contenu, contactez votre gestionnaire du succès des clients ou l’équipe support de Braze pour obtenir plus d’informations.

{% alert note %}
Braze recommande aux clients qui utilisent notre fil d'actualité de passer à notre canal Cartes de contenu. Il est plus flexible, plus personnalisable et plus fiable. Les cartes de contenu sont également plus facile à trouver et à utiliser dans la plateforme Braze. Voir notre [Guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) ou contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

## Quand utiliser les cartes de contenu

Les cartes de contenu sont généralement (mais pas nécessairement) dans une sorte de flux et permettent de tirer parti de l’espace disponible en intégrant des images et des graphiques qui se démarquent des autres. Vous pouvez personnaliser les cartes en fonction des actions de l’utilisateur, onboarder vos clients avec une checklist et bien plus encore !

### Avantages des cartes de contenu

Quels sont les avantages d’utiliser des cartes de contenu plutôt que de demander à votre équipe technique d’intégrer le contenu dans votre appli ? En voici quelques-uns :

- **Segmentation et personnalisation simplifiées :** Vos données utilisateur résident dans Braze, ce qui facilite la définition de votre public et la personnalisation de vos messages avec les cartes de contenu.
- **Reporting centralisé :** Les métriques des performances des cartes de contenu sont suivies dans Braze, vous avez donc des informations sur toutes vos campagnes dans un emplacement centralisé.
- **Parcours clients cohésifs :** Vous pouvez combiner des cartes de contenu avec d’autres canaux dans Braze pour créer des expériences client cohérentes. Un cas d’utilisation populaire consiste à envoyer une notification push, puis à enregistrer cette notification en tant que carte de contenu dans votre application pour tous ceux qui n’ont pas interagi avec la notification push. Si le contenu est intégré directement à votre application par votre équipe technique, alors il est « isolée du reste de vos communications.
- **Plus de contrôle sur l’expérience de messagerie :** Vous aurez toujours besoin de votre équipe technique pour vous aider dans la configuration initiale des cartes de contenu, après cela, vous pourrez contrôler le message, les destinataires, le calendrier et plus encore depuis votre tableau de bord de Braze.

### Excellents exemples d’utilisation

Avec les cartes de contenu, vous pouvez :
- Présenter des nouveaux contenus.
- Les coordonner avec des messages de notification push pour montrer que vous proposez constamment des promotions.
- Offrir aux clients qui n’ont pas activé la notification push un accès à vos promotions.
- Déclencher des confirmations de commande ou toute autre communication personnalisée avec votre client.
- Développer et fournir un calendrier d’onboarding.

## Cartes de contenu et flux

Voici ce que voient vos utilisateurs quand ils ouvrent un flux de carte de contenu standard. Comme vous le voyez, trois types standard de cartes peuvent être placés dans le flux : une carte Bannière, une Captioned Content Card et une Classic Content Card.

![Flux de carte de contenu montrant les trois types de cartes standard.]({% image_buster /assets/img/cc_feed_new.png %}){: style="max-width:60%"}

{% alert note %}
Les cartes de contenu ont une limite de taille maximale de 2 kb pour le contenu que vous saisissez dans le tableau de bord de Braze. Cela inclut le texte des messages, les URL d’images, les liens et les paires clé-valeur. Dépasser ce montant empêchera la carte d’être envoyée.
{% endalert %}
