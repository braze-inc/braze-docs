---
nav_title: Configuration de WhatsApp
article_title: Configuration de WhatsApp
alias: /partners/whatsapp/
description: "Cet article explique comment configurer le canal WhatsApp de Braze, y compris les conditions préalables et les étapes suivantes suggérées."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# Configuration WhatsApp

> La messagerie [WhatsApp](https://www.whatsapp.com/) Business est une plateforme de messagerie peer-to-peer populaire utilisée dans le monde entier qui propose une messagerie basée sur la conversation pour les entreprises.	

## Conditions préalables

Acceptez les conditions suivantes avant de poursuivre avec l’intégration :

- **Politique d'abonnement :** WhatsApp exige que les entreprises demandent un abonnement des clients pour l’envoi de messages.
- **Règles de contenu de WhatsApp :** WhatsApp a plusieurs [règles à respecter en matière de contenu](https://www.whatsapp.com/legal/commerce-policy?l=en).
- **Conformité :** Respectez toutes les documentations de Braze et de Meta, ainsi que toutes les [politiques de Méta](https://www.whatsapp.com/legal/?lang=en) applicables.
- **Limites de conversation de 24 heures :** Lorsqu’une entreprise envoie le message modélisé d’origine ou qu’un utilisateur envoie un message, une période de 24 heures s’ouvre au cours de laquelle les deux participants peuvent converser. 
- **Débuter une conversion :** Les utilisateurs peuvent débuter une conversation à tout moment. Une entreprise peut débuter une conversation uniquement à l’aide d’un modèle de message approuvé.
<br><br>

| Condition| Description|
| ---| --- |
| Compte gestionnaire Meta Business | Un compte Meta Business est nécessaire pour exploiter ce canal de communication. |
| Compte WhatsApp Business | Un compte WhatsApp Business est nécessaire pour exploiter ce canal de communication. |
| Numéro de téléphone WhatsApp | Vous devez acquérir un numéro de téléphone qui répond aux exigences de WhatsApp pour l’[API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou l’[API sur site](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) pour l'utilisation du canal de communication.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Connecter WhatsApp Messenger à Braze

Dans Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et recherchez **WhatsApp**.

Sur la page partenaire de WhatsApp, sélectionnez **Commencer l'intégration**.

![Page partenaire de WhatsApp avec un bouton pour commencer l'intégration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Dans la fenêtre ouverte, sélectionnez **Suivant** jusqu'à ce que le bouton **Commencer l'intégration** apparaisse. Sélectionnez le bouton pour lancer le processus d'intégration.

![Instructions pour connecter Braze à WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Étape 2 : Configuration WhatsApp

Ensuite, vous serez invité à suivre le flux de configuration de Braze. Pour une marche à suivre étape par étape, reportez-vous à l'[inscription intégrée à WhatsApp.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) 

Lors de ce flux vous allez :
1. Créer ou sélectionner vos comptes Meta et WhatsApp Business. Veillez à consulter les [directives relatives aux noms d'affichage de WhatsApp.](https://www.facebook.com/business/help/757569725593362) <br><br>Il est probable que vous ayez déjà au moins un compte Meta Business existant dans votre entreprise. Si c’est le cas, sélectionnez celui que vous souhaitez utiliser pour votre compte WhatsApp Business. Les autorisations utilisateur et les vérifications commerciales pour WhatsApp seront contrôlées de manière centralisée dans votre compte Meta Business.<br><br>
2. Créer votre profil WhatsApp Business.
3. Vérifier votre numéro WhatsApp Business.<br><br>

Une fois la configuration terminée, un groupe d'abonnement WhatsApp dédié sera créé pour vos utilisateurs.

### Étape 3 : Créer des modèles WhatsApp

Les modèles de message WhatsApp approuvés sont les seuls à pouvoir être utilisés pour démarrer une conversation avec des clients. Les modèles WhatsApp peuvent être créés dans le [gestionnaire Meta Business.](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) Pour obtenir une liste des fonctionnalités d'envoi de messages WhatsApp prises en charge par Braze, consultez la page [Fonctionnalités WhatsApp prises en charge.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features)

1. **Accédez au [gestionnaire de modèles](https://business.facebook.com/wa/manage/message-templates)**<br>
Dans le gestionnaire Meta Business, sous **Outils de compte**, sélectionnez **Modèles de message**.
Sélectionnez ensuite **Créer des modèles.**<br><br>![]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Paramètres des messages**<br>
Dans le compositeur de nouveaux modèles de messages, sélectionnez la catégorie de votre message, nommez votre modèle et choisissez les langues que vous souhaitez prendre en charge. Vous pouvez en supprimer ou ajouter d’autres langues par la suite.<br><br> 
	Les catégories de modèle de message disponibles comprennent les suivantes :
	- Marketing : Envoyer des offres promotionnelles, annoncer des produits et plus encore pour accroître la connaissance et l’engagement
	- Utilitaire : Envoyer des mises à jour de compte, de commande, des alertes et plus encore pour partager des informations importantes
	- Authentification : Envoyer des codes permettant à vos clients d’accéder à leur compte<br><br> 
	![]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Modifier le modèle**<br>
Il vous sera ensuite demandé de créer votre modèle de message. <br><br>Vous pouvez fournir ici un en-tête sous forme de texte ou de média, le texte du corps, un pied de page de message et des boutons. Notez que les en-têtes de vidéo et de document ne sont pas disponibles actuellement, et que les en-têtes doivent être de type texte ou image. La prévisualisation de votre message s’affichera à droite. <br><br>Même si Meta ne prend pas Liquid en charge, vous pouvez modéliser des variables qui seront ensuite remplacées par des variables Liquid dans Braze. Pour ce faire, sélectionnez le bouton **\+ Ajouter une variable.** <br><br>![]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}<br><br>Une fois que vous avez terminé votre modèle, cliquez sur **Envoyer**. 

#### Délai d’approbation du modèle

Vous pouvez vérifier le statut d'approbation de votre modèle de message sur la page **Modèle de message** du Meta Business Manager ou lors de la création d'une campagne ou d'un canvas dans Braze. En outre, vous pouvez être notifié par e-mail par l’équipe WhatsApp en fonction de vos autorisations de notification. 

{% alert note %}
Les modèles approuvés peuvent être utilisés dans autant de campagnes et de canevas que vous le souhaitez. Ils peuvent également être envoyés à autant d'utilisateurs ayant souscrit un abonnement que vous le souhaitez. Ceci est vrai à moins que la qualité du modèle ne diminue.
{% endalert %}

### Étape 4 : Créer une campagne WhatsApp

Une fois les modèles WhatsApp approuvés, vous pouvez passer au tableau de bord pour créer un [WhatsApp Canvas ou une campagne.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) 

{% alert note %}
Après la création de votre compte WhatsApp Business, Meta déterminera votre limite d'envoi de messages de départ. Pour en savoir plus, consultez la rubrique sur le [débit]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Étapes suivantes

Après avoir terminé l’intégration, nous vous recommandons d’effectuer les deux processus Meta suivants :
- [Vérification commerciale](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Vous avez peut-être déjà une vérification commerciale si vous avez utilisé un gestionnaire Meta Business existant. 
- [Compte professionnel officiel](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Nous vous recommandons également de prendre connaissance des [numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) et d'ajouter tous les utilisateurs qui auront besoin d'un accès pour créer des [modèles de messages dans votre organisation](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### Stockage local de l’API Cloud pour WhatsApp

Braze prend en charge le [stockage local de l'API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) de WhatsApp. Pour l'activer, contactez votre gestionnaire du service clientèle de Braze.

