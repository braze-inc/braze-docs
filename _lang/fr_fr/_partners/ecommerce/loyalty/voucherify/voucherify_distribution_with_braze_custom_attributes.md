---
nav_title: Distributions avec Attributs personnalisés
article_title: Distributions avec Attributs personnalisés avec Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "Cet article de référence décrit l'intégration de Braze avec Voucherify. L'intégration de Braze vous permet d'envoyer des codes Voucherify dans vos messages Braze."
page_type: partner
search_tag: Partner
---

# Distributions avec des attributs personnalisés

> L'intégration de Braze vous permet d'envoyer des codes Voucherify dans vos messages Braze. Cet article de référence explique comment utiliser les attributs personnalisés de Braze avec les distributions de Voucherify.

_Cette intégration est gérée par Voucherify._

{% alert tip %}
Avant d'utiliser les attributs personnalisés de Braze dans les distributions de Voucherify, vous devez ajouter vos utilisateurs de Braze au tableau de bord de Voucherify. Vous pouvez utiliser le contenu connecté Braze pour synchroniser les utilisateurs ou importer vos clients à l’aide d’un fichier CSV ou l’API. Visitez [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) pour en savoir plus.
{% endalert %}

Les attributs personnalisés de Braze vous permettent d'attribuer des codes Voucherify à des attributs personnalisés dans les profils utilisateurs de Braze. Vous pouvez utiliser des coupons uniques, des cartes-cadeaux, des cartes de fidélité et des codes de recommandation. Tout d'abord, connectez Voucherify à Braze, créez une distribution dans Voucherify, puis créez une campagne dans Braze avec l'extrait de code d'attribut personnalisé dans votre modèle de message.

## Étape 1 : Connexion de votre compte Voucherify à Braze

Tout d'abord, connectez votre compte Voucherify avec Braze.

1. Copiez la clé API REST de votre compte Braze.
2. Accédez au répertoire **Intégrations** dans votre tableau de bord Voucherify, trouvez Braze et choisissez **Connecter.**  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Collez la clé API Braze et choisissez **Connecter**:  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Étape 2 : distribution de code

Une fois connecté, vous pouvez démarrer une nouvelle distribution Voucherify [distribution](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) qui attribue un code à l'attribut personnalisé dans le profil utilisateur dans Braze. Vous pourrez utiliser ultérieurement les attributs reçus avec des codes dans vos campagnes Braze.

Avant de configurer la distribution, vous devez ajouter vos utilisateurs Braze au tableau de bord Voucherify. Visitez [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) pour en savoir plus.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Vous pouvez distribuer des codes à Braze en utilisant deux modes :

- **Mode manuel**
- Définir un **flux de travail automatisé** qui déclenche la distribution de code en réponse à une action entreprise par vos utilisateurs.

Dans les modes manuel et automatique, Voucherify envoie des codes uniques avec leurs attributs et les assigne aux attributs personnalisés de Braze dans les profils des utilisateurs.

![Mapper les champs aux attributs personnalisés]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Distribution manuelle %}

Le mode manuel est une action unique qui attribue des codes à une audience choisie. Allez dans les **Distributions** de votre tableau de bord, exécutez le gestionnaire de distribution avec le plus, et choisissez **Message manuel**.

1.  Nommez votre distribution.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Choisissez une campagne qui sera une source de codes uniques **(1)** et sélectionnez un segment d'utilisateurs ou un seul client comme vos destinataires **(2)**. Visitez [Voucherify](https://support.voucherify.io/article/51-customer-segments) pour en savoir plus sur les segments de clients.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Ensuite, ajoutez les autorisations de marketing. Si vous ne collectez pas les autorisations de votre audience, désactivez la vérification du consentement.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Choisissez Braze comme canal et mappez les champs personnalisés qui seront ajoutés au profil utilisateur dans Braze. Vous devez ajouter le champ représentant le code du bon publié ; le reste des champs est facultatif.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Une fois terminé, vous pouvez voir un résumé de la distribution. Cliquez sur **enregistrer et envoyer** pour livrer les codes aux profils d'utilisateurs dans Braze.  

_Notez que toutes les distributions manuelles sont envoyées avec un délai de 10 minutes._

{% endtab %}
{% tab Flux de travail automatique %}

Voucherify peut envoyer des codes à Braze automatiquement en réponse aux déclencheurs suivants :

- **Le client est entré/sorti d'un segment spécifique de Voucherify**
- **Publication du code réussie** – le message est envoyé lorsque le code d'une campagne est publié (attribué) à un client dans Voucherify.
- **statut de la commande changé** (commande créée, commande mise à jour, commande payée, commande annulée)
- **Crédits cadeaux ajoutés** – le message est envoyé lorsque des crédits de carte-cadeau sont ajoutés à la carte du client.
- **Points de fidélité ajoutés** – le message est envoyé lorsque des points de fidélité sont ajoutés au profil du client.
- **Bon d'achat échangé** – le message est envoyé aux clients qui ont échangé avec succès des bons.
- **Annulation du remboursement du bon** – le message est envoyé au client dont le remboursement a été annulé avec succès.
- **Échange de récompense** – le message est envoyé lorsqu'un client échange une récompense de fidélité ou de recommandation.
- **Un événement personnalisé a été enregistré pour un client** \- le message est déclenché lorsque Voucherify enregistre un événement personnalisé particulier.

Pour configurer un flux de travail automatique avec Braze et Voucherify, [visitez le tutoriel des distributions](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Étape 3 : Utilisez les attributs personnalisés de Voucherify dans votre campagne Braze

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Une fois que l'attribut personnalisé avec le code est ajouté aux attributs personnalisés du client dans Braze, vous pouvez l'utiliser dans vos campagnes.

Modifier le corps du message et ajouter l'attribut personnalisé défini dans la distribution Voucherify. Place {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} pour afficher le code unique.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

Une fois l’opération terminée, vous pouvez voir le code dans l'aperçu de votre message.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})

