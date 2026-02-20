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

> Boostez la livrabilité et l'engagement en touchant davantage les bons utilisateurs sur WhatsApp grâce à une réception/distribution dynamique et basée sur l'engagement.

Les messages WhatsApp à réception/distribution optimisée sont envoyés à l'aide de l'[API de messages marketing](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) de Meta pour WhatsApp (MM API pour WhatsApp), qui offre une réception/distribution dynamique et basée sur l'engagement. Cela signifie que vos messages à fort taux d'engagement (par exemple, ceux qui sont plus susceptibles d'être lus et cliqués) peuvent atteindre plus d'utilisateurs qui sont susceptibles de s'engager avec eux. WhatsApp considère que vos messages ont un taux d'engagement élevé s'ils sont attendus, pertinents et opportuns, et donc plus susceptibles d'être lus et cliqués. 

Les marques peuvent s'attendre à une livrabilité égale ou supérieure avec l'API MM pour WhatsApp, par rapport à l'API Cloud. En Inde, les messages marketing à fort engagement ont vu jusqu'à 9 % de messages supplémentaires délivrés par rapport à l'API Cloud, selon Meta. Notez que l'API MM pour WhatsApp ne garantit toujours pas une livrabilité à 100 %.

### Disponibilité régionale

La disponibilité et les possibilités de réception/distribution optimisée dépendent de la région du numéro de téléphone professionnel et de l'utilisateur. Pour en savoir plus, reportez-vous à la [disponibilité géographique des fonctionnalités.](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features) 

## Mise en place d'une réception/distribution optimisée

1. Dans Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** > **WhatsApp**.
2. Dans la section **Optimisez vos envois avec la réception/distribution optimisée**, sélectionnez **Paramètre de mise à niveau** pour déclencher le [flux d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

![La section Intégration des messages WhatsApp avec une option d'optimisation de l'envoi avec réception/distribution optimisée.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Une fois la réception/distribution optimisée activée, les détails de votre compte dans **WhatsApp Business Account Management** afficheront l'état de la réception/distribution optimisée.

![WhatsApp section Gestion des abonnements avec un groupe d'abonnement listé qui a un statut de numéro actif.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

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

![Compositeur de messages avec un onglet de prévisualisation comportant une case à cocher pour sélectionner la réception/distribution optimisée.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Reciblage des utilisateurs sur d'autres canaux de Braze 

L'API MM pour WhatsApp n'offrant pas une livrabilité à 100 %, il est important de comprendre comment recibler les utilisateurs qui n'ont peut-être pas reçu votre message sur d'autres canaux. 

Pour recibler les utilisateurs, nous vous recommandons de créer un segment d'utilisateurs qui n'ont pas reçu un message spécifique. Pour ce faire, filtrez par le code d'erreur `131049`, qui indique qu'un message de modèle marketing n'a pas été envoyé en raison de l'application de la limite de modèles marketing par utilisateur de WhatsApp. Pour ce faire, vous pouvez utiliser les Braze Currents ou les extensions de segments SQL :

- **Braze Currents :** Exportez les événements de défaillance des messages à l'aide de Braze Currents. Vous pouvez ensuite utiliser ces données pour mettre à jour un attribut personnalisé sur le profil utilisateur (tel que `whatsapp_failed_last_msg: true`), que vous pouvez utiliser comme filtre pour votre campagne de reciblage.
- **Extensions de segments SQL :** Si vous avez accès à cette fonctionnalité, vous pouvez utiliser SQL pour interroger les journaux d'échec des messages et créer un segment de ces utilisateurs, puis cibler ce segment sur un canal différent.
