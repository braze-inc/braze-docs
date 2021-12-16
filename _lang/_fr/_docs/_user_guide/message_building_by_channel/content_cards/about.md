---
nav_title: À propos des cartes de contenu
article_title: À propos des cartes de contenu
page_order: 0
description: "Cet article de référence donne un aperçu du canal de la carte de contenu Braze et des cas d'utilisation courante."
channel:
  - cartes de contenu
---

# À propos des cartes de contenu

> Cet article de référence donne un aperçu du canal de la carte de contenu Braze et des cas d'utilisation courante. Pour en savoir plus sur ce sujet, consultez notre cours LAB [Cartes de Contenu](https://lab.braze.com/messaging-channels-content-cards)!

{% include video.html id="4FUPxkIq2xc" align="right" %}

Avec les Cartes de Contenu, vous pouvez envoyer un très ciblé, flux dynamique de contenu riche pour vos clients directement dans les applications qu'ils aiment sans interrompre leur expérience. De plus, les cartes de contenu prennent en charge des fonctionnalités plus personnalisées, y compris le épinglage de carte, le rejet de la carte, Livraison basée sur API, temps d'expiration des cartes personnalisées, analyse des cartes et coordination facile avec les notifications push.

Les cartes de contenu ne sont pas disponibles hors de la boîte et doivent être achetées. Pour commencer avec les Cartes de Contenu, contactez votre Responsable du Succès Client ou notre équipe d'assistance pour plus d'informations.

{% alert note %}
Si vous utilisez notre outil Flux d'actualités, nous vous recommandons de passer au canal de messagerie de nos Cartes de Contenu — il est plus flexible, personnalisable et fiable. Les cartes de contenu sont également plus faciles à trouver et à utiliser dans le produit Braze. Consultez notre [Guide de Migration](/docs/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) ou contactez votre responsable de compte Braze pour plus d'informations.
{% endalert %}

## Quand utiliser les cartes de contenu

Les cartes de contenu sont généralement stockées dans un fil d'actualité (mais pas nécessairement), et vous aider à tirer parti de l'espace visuel en incorporant des images et des graphiques qui se démarquent. Vous pouvez personnaliser les cartes en fonction des actions de l'utilisateur, à bord de vos clients avec une liste de contrôle, et bien plus encore !

### Avantages de l'utilisation des cartes de contenu

Vous vous interrogez sur les avantages de l'utilisation des Cartes de Contenu par rapport à la création de contenu dans votre application ? Voici quelques avantages à utiliser les Cartes de Contenu :

- **Segmentation et personnalisation plus faciles :** Vos données utilisateur vivent au Brésil, en facilitant la définition de votre public et la personnalisation de vos messages avec les Cartes de Contenu.
- **Rapports centralisés :** Les analyses de carte de contenu sont suivies au Brésil, donc vous avez un aperçu de toutes vos campagnes dans un seul emplacement centralisé.
- **Voyages clients Cohesive :** Vous pouvez combiner des Cartes de Contenu avec d'autres canaux dans Braze pour créer des expériences clients cohérentes. Un cas d'utilisation populaire est d'envoyer une notification push, puis l'enregistrement de cette notification en tant que Carte de Contenu dans votre application pour toute personne qui ne s'est pas engagée avec le push. Si le contenu est directement intégré dans votre application par votre équipe technologique, il est stocké dans le reste de votre messagerie.
- **Plus de contrôle sur l'expérience de messagerie :** Bien que vous ayez encore besoin de votre équipe technique pour aider à la configuration initiale des cartes de contenu, après cela, vous serez en mesure de contrôler le message, les destinataires, le timing, et plus directement depuis votre tableau de bord Braze.

{% alert warning %}
Les Cartes de Contenu n'offrent pas de support de groupe de contrôle. Si vous souhaitez tirer parti des groupes de contrôle, un flux personnalisé doit être construit, y compris des cartes personnalisées et un suivi d'implémentation personnalisé. Pour plus de détails, reportez-vous au [rapport de la carte de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/).
{% endalert %}

### Caisses d'utilisation géniales

- Présenter un nouveau contenu.
- Coordonner avec les messages push pour illustrer un historique persistant des promotions.
- Offrez aux clients sans push un accès aux promotions.
- Déclenchez les confirmations de commande ou toute autre communication personnalisée avec votre client.
- Développer et livrer ainsi qu'un calendrier d'embarquement.

## Cartes de contenu et flux

C'est à quoi il semble que vos utilisateurs ouvrent un flux de carte de contenu standard. Comme vous pouvez le voir, trois types de cartes standard peuvent s'asseoir dans le flux : une carte de bannière, une carte de contenu sous-titrée et une carte de contenu classique.

![Flux de cartes de contenu]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

{% alert note %}
Les cartes de contenu ont une taille maximale de 2 Ko pour le contenu que vous entrez dans le tableau de bord Braze. Ceci inclut le texte du message, les URL de l'image, les liens et les paires clé-valeur. Le dépassement de ce montant empêchera l'envoi de la carte.
{% endalert %}
