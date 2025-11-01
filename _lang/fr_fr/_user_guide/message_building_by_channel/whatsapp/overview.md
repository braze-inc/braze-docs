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

# Configuration de WhatsApp

> La messagerie [WhatsApp](https://www.whatsapp.com/) Business est une plateforme de messagerie peer-to-peer populaire utilisée dans le monde entier qui propose une messagerie basée sur la conversation pour les entreprises.	

## Conditions préalables

Prenez connaissance des éléments suivants avant de procéder à l'intégration :

- **Politique d'abonnement :** WhatsApp exige des entreprises que leurs clients acceptent l'abonnement à l'envoi de messages.
- **Règles de contenu de WhatsApp :** WhatsApp a plusieurs [règles à respecter en matière de contenu](https://www.whatsapp.com/legal/commerce-policy?l=en).
- **Conformité :** Se conformer à l'ensemble de la documentation applicable de Braze et de Meta ainsi qu'à toute [politique](https://www.whatsapp.com/legal/?lang=en) applicable [de Meta](https://www.whatsapp.com/legal/?lang=en).
- **Limites de conversation de 24 heures :** Après qu'une entreprise a envoyé un premier message type ou qu'un utilisateur a envoyé un message, une fenêtre de 24 heures s'ouvre pendant laquelle les deux parties peuvent échanger des messages. 
- **Engager la conversion :** Les utilisateurs peuvent engager une conversation à tout moment. Une entreprise ne peut engager une conversation que par l'intermédiaire d'un modèle de message approuvé.
<br><br>

| Exigence| Description|
| ---| --- |
| Compte du gestionnaire Meta Business | Un compte Meta Business est nécessaire pour tirer parti de ce canal de communication. |
| Compte WhatsApp Business | Un compte WhatsApp Business est nécessaire pour tirer parti de ce canal de communication. |
| Numéro de téléphone WhatsApp | Vous devez acquérir un numéro de téléphone qui répond aux exigences de WhatsApp pour l ['API dans le cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou l ['API sur site](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) pour l'utilisation du canal de communication.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Connectez WhatsApp Messenger à Braze

Dans Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et recherchez **WhatsApp**.

Sur la page partenaire de WhatsApp, sélectionnez **Commencer l'intégration**.

!page partenaire WhatsApp avec un bouton pour commencer l'intégration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Dans la fenêtre ouverte, sélectionnez **Suivant** jusqu'à ce que le bouton **Commencer l'intégration** apparaisse. Sélectionnez le bouton pour lancer le processus d'intégration.

Instructions pour connecter Braze à WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Étape 2 : Configuration de WhatsApp

Ensuite, vous serez invité à suivre le processus de configuration de Braze. Pour une marche à suivre étape par étape, reportez-vous à l'[inscription intégrée à WhatsApp.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) 

Dans le cadre de ce flux, vous pourrez
1. Créez ou sélectionnez vos comptes Meta et WhatsApp Business. Veillez à prendre connaissance des [directives relatives au nom d'affichage de WhatsApp.](https://www.facebook.com/business/help/757569725593362) <br><br>Il est probable que vous disposiez déjà d'au moins un compte Meta Business dans votre entreprise. Si c'est le cas, sélectionnez celui dans lequel vous souhaitez que votre compte WhatsApp Business soit en ligne/en production/instantané. Les autorisations des utilisateurs et la vérification des entreprises pour WhatsApp seront contrôlées de manière centralisée dans votre compte Meta Business.<br><br>
2. Créez votre profil WhatsApp Business.
3. Vérifiez votre numéro WhatsApp Business.<br><br>

Une fois la configuration terminée, un groupe d'abonnement WhatsApp dédié sera créé pour vos utilisateurs.

### Étape 3 : Créer des modèles WhatsApp

Seuls les modèles de messages WhatsApp approuvés peuvent être utilisés pour engager des conversations avec les clients. Les modèles WhatsApp peuvent être créés dans le [gestionnaire Meta Business.](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) Pour obtenir une liste des fonctionnalités d'envoi de messages WhatsApp prises en charge par Braze, consultez la page [Fonctionnalités WhatsApp prises en charge.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features)

1. **Accédez au [gestionnaire de modèles](https://business.facebook.com/wa/manage/message-templates)**<br>
Dans le gestionnaire de compte Meta Business Manager, sous **Outils de compte**, sélectionnez **Modèles de message.**
Sélectionnez ensuite **Créer des modèles.**<br><br>!gestionnaire WhatsApp avec une liste de modèles d'envoi de messages.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Paramètres des messages**<br>
Dans le compositeur de nouveaux modèles de messages, sélectionnez la catégorie de votre message, nommez votre modèle et choisissez les langues que vous souhaitez prendre en charge. Vous pouvez supprimer ou ajouter des langues ultérieurement.<br><br> 
	Les catégories de modèles d'envoi de messages disponibles sont les suivantes :
	- Marketeur : Envoyez des offres promotionnelles, des annonces de produits et plus encore pour accroître la sensibilisation et l'engagement.
	- Utilité : Envoyez des mises à jour de compte, des mises à jour de commande, des alertes, etc. pour partager des informations importantes.
	- Authentification : Envoyer des codes permettant à vos clients d'accéder à leurs comptes<br><br> 
	!Compositeur de modèles de messages avec des catégories pour le marketing, l'utilité et l'authentification.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Modifier le modèle**<br>
Ensuite, créez votre modèle de message. <br><br>Vous pouvez fournir un en-tête de texte ou de média, le corps du texte, un pied de message et des boutons. Notez que les en-têtes de vidéo et de document ne sont pas disponibles actuellement, et que les en-têtes doivent être de type texte ou image. Les modèles et médias que vous ajoutez servent d'exemple pour le processus de révision et **ne sont pas** inclus dans le message type. Les médias doivent être ajoutés dans Braze. Un aperçu de votre message s'affiche dans un panneau. <br><br>Bien que Meta ne prenne pas en charge le liquide, vous pouvez introduire dans le modèle des variables qui pourront être remplacées ultérieurement dans Braze par des variables liquides. Pour ce faire, sélectionnez le bouton **\+ Ajouter une variable.** <br><br>\![Modèle de compositeur.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Une fois que vous avez terminé votre modèle, cliquez sur **Soumettre**. 

#### Délai d'approbation du modèle

Vous pouvez vérifier le statut d'approbation de votre modèle de message sur la page **Modèle de message** du Meta Business Manager ou lors de la création d'une campagne ou d'un canvas dans Braze. En outre, vous pouvez être notifié par e-mail par l'équipe WhatsApp en fonction de vos autorisations de notification. 

{% alert note %}
Les modèles approuvés peuvent être utilisés dans autant de campagnes et de canevas que vous le souhaitez. Ils peuvent également être envoyés à autant d'utilisateurs ayant souscrit un abonnement que vous le souhaitez. Ceci est vrai à moins que la qualité du modèle ne diminue.
{% endalert %}

### Étape 4 : Créez une campagne WhatsApp

Une fois les modèles WhatsApp approuvés, vous pouvez passer au tableau de bord pour créer un [WhatsApp Canvas ou une campagne.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) 

{% alert note %}
Après la création de votre compte WhatsApp Business, Meta déterminera votre limite d'envoi de messages de départ. Pour en savoir plus, consultez la rubrique [débit]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Prochaines étapes

Une fois l'intégration terminée, nous vous recommandons d'effectuer les deux processus Meta suivants :
- [Vérification de l'entreprise](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Il se peut que vous disposiez déjà d'une vérification des entreprises si vous avez utilisé un gestionnaire Meta Business existant. 
- [Compte professionnel officiel](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Nous vous recommandons également de prendre connaissance des [numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) et d'ajouter tous les utilisateurs qui auront besoin d'un accès pour créer des [modèles de](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143) messages [dans votre organisation](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### WhatsApp Cloud API Stockage local

Braze prend en charge le [stockage local de l'API Cloud de](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) WhatsApp. Pour l'activer, contactez votre gestionnaire du service clientèle de Braze.

