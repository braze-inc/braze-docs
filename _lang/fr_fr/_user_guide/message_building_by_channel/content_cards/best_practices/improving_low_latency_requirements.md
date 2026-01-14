---
nav_title: Améliorer la faible latence
article_title: Amélioration de la faible latence pour les cartes de contenu de type bannière
page_order: 10
description: "Cet article traite des stratégies permettant de répondre aux exigences de faible latence avec les cartes de contenu."
channel:
  - content cards
---

# Amélioration de la latence pour les cartes de contenu de type bannière

> Si vous rencontrez des problèmes de latence dans la mise en œuvre de vos cartes de contenu pour des cas d'utilisation critiques, tels que les bannières de page d'accueil, consultez cette page pour obtenir des stratégies et des conseils qui vous aideront à résoudre le problème et à accélérer le rendu.

{% alert tip %}
Vous cherchez à afficher des bannières personnalisées bien visibles sur votre application ou votre site web ? Essayez [les bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/), qui sont créées pour prendre en charge les cas d'utilisation des bannières à faible latence.
{% endalert %}

## Utilisez l'entrée planifiée au lieu de l'entrée basée sur l'action

Les cartes basées sur l'action, tant dans les campagnes que dans les toiles, nécessitent un traitement en arrière-plan. Avant de créer une carte pour un utilisateur, Braze doit d'abord être informé de l'action déclencheuse (par exemple, un achat ou le début d'une session). Par conséquent, il y aura un délai avant que ces cartes ne soient disponibles.

Les cartes basées sur l'action introduiront une complexité supplémentaire dans votre application, car vous risquez de devoir continuellement interroger et actualiser votre application en attendant que la carte soit disponible. Configurez plutôt votre carte de manière à ce qu'elle soit accessible à l'adresse `Scheduled Entry`, ce qui permettra à l'audience ciblée de disposer en permanence d'une fenêtre de disponibilité.

Si vous planifiez vos cartes à l'avance, elles seront prêtes, attendant que l'utilisateur ouvre votre application et demande des cartes.

## Utilisez la logique d'envoi "à la première impression".

Associée à des envois planifiés, l'option `At First Impression` permet d'éviter les temps de latence grâce à la vitesse à laquelle une carte est créée et stockée dans Braze. Le site `At Campaign Launch` crée à l'avance toutes les cartes pour tous les utilisateurs segmentés, ce qui peut prendre du temps. L'option `At First Impression` génère une carte pour un utilisateur la première fois qu'elle est demandée, par exemple lorsqu'un utilisateur ouvre votre application pour la première fois.

Cela signifie qu'avec la saisie planifiée, les cartes seront disponibles immédiatement, dès que vous en aurez besoin, soit au début de la session, soit pour une fenêtre d'éligibilité basée sur le temps.

## N'oubliez pas que la saisie des canvas est une condition préalable à la réception des cartes

Lorsque vous utilisez Canvas, n'oubliez pas qu'un utilisateur doit d'abord entrer dans Canvas en fonction des critères d'entrée que vous avez configurés, *puis* qu'il doit passer par l'étape du message de votre carte de contenu. Ce n'est qu'ensuite que la carte sera disponible pour votre application ou votre site web. N'oubliez pas qu'il existe un temps de latence intégré pour la création de la carte une fois que l'utilisateur a franchi l'étape, ce qui peut retarder la mise à disposition de la carte.

## N'actualisez pas les cartes de manière excessive

Les cartes de contenu sont automatiquement actualisées par le SDK à chaque démarrage de session. Vous pouvez également demander manuellement d'actualiser la carte de contenu à tout moment au cours d'une session active.

Appeler la méthode `requestContentCardsRefresh` et actualiser trop fréquemment peut entraîner une limite de débit. Si votre application devient temporairement limitée de débit, vous risquez de ne pas pouvoir actualiser les cartes lorsque vous en avez besoin ou à un moment critique de l'engagement de l'utilisateur avec votre application.

Pour éviter cela, n'appelez cette méthode d'actualisation qu'à des moments importants du cycle de vie de l'utilisateur, par exemple après qu'il a effectué un achat ou qu'il est passé à un niveau d'abonnement supérieur.

## Évitez d'inclure du contenu connecté

Le contenu connecté enrichit les cartes de contenu avec des données first-party ou third-party API. Cependant, lorsqu'il est inclus dans un message de carte de contenu, il bloque la disponibilité de la carte jusqu'à ce que la demande du réseau de contenu connecté puisse être complétée. Dans certains cas, les SDK réessayeront quelques secondes plus tard afin de ne pas retarder la logique de rendu de votre application, qui peut attendre que le SDK ait terminé sa tâche d'actualisation.

Si vous devez utiliser le contenu connecté, planifiez ces cartes à l'avancement et utilisez l'option `At Campaign Launch` afin que les cartes soient précréées avant la prochaine session d'un utilisateur. Notez que ces cartes ne seront pas disponibles immédiatement car Braze rédige toutes les cartes pour tous les utilisateurs éligibles.
