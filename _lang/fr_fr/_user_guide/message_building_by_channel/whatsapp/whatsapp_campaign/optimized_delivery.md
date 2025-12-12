---
nav_title: Messages WhatsApp avec réception/distribution optimisée
article_title: Messages WhatsApp avec réception/distribution optimisée
page_order: 1
description: "Cet article de référence présente les étapes à suivre pour créer un message WhatsApp dont la réception/distribution est optimisée."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Messages WhatsApp avec réception/distribution optimisée

> Tirez parti des systèmes d'intelligence artificielle avancés de Meta pour diffuser vos messages marketing à un plus grand nombre d'utilisateurs qui sont les plus susceptibles de s'engager avec eux, en stimulant considérablement la livrabilité et l'engagement des messages.

Les messages WhatsApp à réception/distribution optimisée sont envoyés à l'aide de la nouvelle [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, qui offre des performances supérieures à celles de l'API Cloud traditionnelle. Ce nouveau pipeline d'envoi vous permet de mieux atteindre les utilisateurs qui valorisent vos messages et souhaitent les recevoir.

Les avantages de l'utilisation de la réception/distribution optimisée sont les suivants :

- **Limites de l'envoi de messages dynamiques :** La nouvelle API offre des limites d'envoi de messages plus dynamiques par utilisateur, ce qui permet aux messages marketing à fort engagement (ceux qui sont plus susceptibles d'être lus ou cliqués) d'atteindre un plus grand nombre d'utilisateurs.
- **Optimisation de la livrabilité :** Vous pouvez vous attendre à des taux de réception/distribution plus faibles, mais à des taux d'engagement plus élevés pour les messages délivrés, car l'intelligence artificielle avancée de Meta optimisera pour les utilisateurs dont elle s'attend à ce qu'ils accordent de la valeur au message et qu'ils s'y engagent. 
- **Des résultats probants :** En Inde, les messages identifiés comme étant plus susceptibles d'être lus ou cliqués ont eu jusqu'à 9 % de messages supplémentaires livrés par rapport à l'envoi via l'API Cloud.
- **Réception/distribution ciblée :** L'intelligence artificielle avancée de Meta identifie les messages à fort taux d'engagement et les diffuse à un plus grand nombre d'utilisateurs, ce qui vous permet de transmettre le bon message à un plus grand nombre de personnes sur WhatsApp.

### Disponibilité régionale

La disponibilité et les possibilités de réception/distribution optimisée dépendent de la région du numéro de téléphone professionnel et de l'utilisateur. Pour en savoir plus, reportez-vous à la [disponibilité géographique des fonctionnalités.](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features) 

## Mise en place d'une réception/distribution optimisée

1. Dans Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** > **WhatsApp**.
2. Dans la section **Optimisez vos envois avec la réception/distribution optimisée**, sélectionnez **Paramètre de mise à niveau** pour déclencher le [flux d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

!La section Intégration des messages WhatsApp avec une option d'optimisation de l'envoi avec réception/distribution optimisée.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Une fois la réception/distribution optimisée activée, les détails de votre compte dans **WhatsApp Business Account Management** afficheront l'état de la réception/distribution optimisée.

!WhatsApp section Gestion des comptes d'entreprise avec un groupe d'abonnement répertorié qui a un statut de numéro actif.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Sinon, vous pouvez activer la réception/distribution optimisée directement dans votre gestionnaire WhatsApp, puis commencer à envoyer dans Braze.

### Résolution des problèmes de votre configuration

- **Erreur générale :** Si un problème survient pendant la mise à niveau, cette bannière d'erreur s'affichera et vous conseillera de [contacter le service d'assistance.]({{site.baseurl}}/braze_support/)
- **Erreur inéligible :** Si vous êtes limité par Meta, cette bannière d'erreur s'affichera : "Au moins un compte WhatsApp Business est restreint par Meta. Les comptes doivent être en règle pour pouvoir être mis à jour". Cette question ne peut être rejetée tant que le problème n'est pas résolu.

## Utilisation de la réception/distribution optimisée dans les campagnes et les canevas

La réception/distribution optimisée devrait être utilisée pour les **messages marketing**. Braze supprimera automatiquement l'option de réception/distribution optimisée pour les **messages d'utilité, d'authentification, de service et de réponse**, qui doivent continuer à être envoyés via l'API Cloud, qui est le paramètre par défaut. 

### Choix de la méthode de réception/distribution

1. Dans l'étape du compositeur WhatsApp de Braze pour une campagne ou un envoi canvas, accédez à l'onglet **Paramètres**.
2. Dans la section **Méthode de réception/distribution**, la case **Livraison optimisée (recommandée)** sera cochée par défaut si votre compte WhatsApp Business (WABA) est activé. Si vous ne souhaitez pas utiliser la réception/distribution optimisée pour ce message spécifique, décochez la case.
- Si vous sélectionnez la réception/distribution optimisée mais qu'elle n'est pas disponible, le message reviendra automatiquement à la méthode de l'API dans le nuage.

!Compositeur de messages avec un onglet de prévisualisation qui comporte une case à cocher pour sélectionner la réception/distribution optimisée.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})