---
nav_title: Distributions avec Attributs personnalisés
article_title: Distributions avec Attributs personnalisés avec Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "Cet article de référence décrit l'intégration de Braze avec Voucherify. L'intégration Braze vous permet d'envoyer des codes Voucherify dans vos messages Braze."
page_type: partner
search_tag: Partenaire
---

# Distributions avec attributs personnalisés

> L'intégration Braze vous permet d'envoyer des codes Voucherify dans vos messages Braze. Cet article de référence explique comment utiliser les attributs personnalisés de Braze avec les distributions Voucherify.

{% alert tip %}
Avant d'utiliser les attributs personnalisés de Braze dans les distributions de Voucherify, vous devez ajouter vos utilisateurs Braze au tableau de bord de Voucherify. Vous pouvez utiliser le contenu connecté Braze pour synchroniser les utilisateurs ou importer vos clients via CSV ou API. Visitez [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) pour en savoir plus.
{% endalert %}

Les attributs personnalisés de Braze vous permettent d'attribuer des codes Voucherify à des attributs personnalisés dans les profils d'utilisateurs de Braze. Vous pouvez utiliser des coupons uniques, des cartes-cadeaux, des cartes de fidélité et des codes de recommandation. Tout d'abord, connectez Voucherify à Braze, créez une distribution dans Voucherify, et enfin créez une campagne dans Braze avec l'extrait de code d'attribut personnalisé dans votre modèle de message.

## Étape 1 : Connexion de votre compte Voucherify à Braze

Tout d'abord, connectez votre compte Voucherify à Braze.

1. Copiez la clé API REST de votre compte Braze.
2. Allez dans le répertoire **Integrations (Intégrations)** dans votre tableau de bord Voucherify, trouvez Braze et choisissez **Connect (Connecter)**.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Collez la clé API de Braze et choisissez **Connect (Connecter)** :  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Étape 2 : Distribution du code

Une fois connecté, vous pouvez lancer une nouvelle [distribution](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) Voucherify qui attribue un code à l'attribut personnalisé dans le profil d'utilisateur Braze. Plus tard, vous pourrez utiliser les attributs reçus avec des codes dans vos campagnes Braze.

Avant de configurer la distribution, vous devez ajouter vos utilisateurs Braze au Tableau de bord de Voucherify. Visitez [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) pour en savoir plus.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Vous pouvez distribuer des codes à Braze en utilisant deux modes :

- **Mode manuel**
- Définissez un **flux de travail automatisé** qui déclenche la livraison du code en réponse à une action effectuée par vos utilisateurs.

En mode manuel et automatique, Voucherify envoie des codes uniques avec leurs attributs et les affecte aux attributs personnalisés Braze dans les profils utilisateurs.

![Mapper des champs à des attributs personnalisés]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Manual distribution %}

Le mode manuel est une action ponctuelle qui attribue des codes à une audience choisie. Allez dans les **Distributions** de votre tableau de bord, exécutez le gestionnaire de distribution avec le plus, et choisissez **Manual Message (Message manuel)**.

1.  Nommer votre distribution.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Choisissez une campagne qui sera une source de codes uniques **(1)** et sélectionnez un segment d'utilisateurs ou un client unique comme récepteur **(2)**. Visitez [Voucherify](https://support.voucherify.io/article/51-customer-segments) pour en savoir plus sur les segments de clients.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Puis ajoutez des permissions marketing. Si vous ne recueillez pas les autorisations de votre audience, désactivez la vérification du consentement.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Choisissez Braze comme canal et mappez les champs personnalisés qui seront ajoutés au profil utilisateur dans Braze. Vous devez ajouter le champ représentant le code du bon publié ; les autres champs sont facultatifs.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Une fois terminé, vous pouvez voir un résumé de la distribution. Cliquez sur **Save and send (Enregistrer et envoyer)** pour délivrer les codes aux profils d'utilisateurs dans Braze.  

_Notez que toutes les distributions manuelles sont envoyées avec un délai de 10 minutes._

{% endtab %}
{% tab Automatic Workflow %}

Voucherify peut envoyer automatiquement des codes vers Braze en réponse aux déclencheurs suivants :

- **Segment de Voucherify spécifique à l’entrée/left du client**
- **Successful code publication (Publication de code réussie)** – le message est envoyé lorsque le code d’une campagne est publié (attribué) à un client dans Voucherify.
- **Order status changed (Statut de la commande modifié)** (commande créée, mise à jour de la commande, commande payée, commande annulée).
- **Gift credits added (Crédits-cadeaux ajoutés)** – le message est envoyé lorsque des crédits de carte-cadeau sont ajoutés à la carte du client.
- **Loyalty points added (Points de fidélisation ajoutés)** – le message est envoyé une fois que les points de fidélisation sont ajoutés au profil du client.
- **Voucher redeemed (Bon échangé)** – le message est envoyé aux clients qui ont réussi à échanger des coupons.
- **Voucher redeemed rollback (Annulation de l’échange du bon)** – le message est envoyé aux clients qui ont réussi à annuler l’échange des bons.
- **Reward redemption (Échange de récompense)** – le message est envoyé lorsqu’un client échange une récompense de fidélisation ou de recommandation.
- **Custom event was logged for a customer (Un événement personnalisé a été enregistré pour un client)** - le message est déclenché lorsque Voucherify enregistre un événement personnalisé particulier.

Pour configurer un flux de travail automatique avec Braze et Voucherify, [reportez-vous au tutoriel de distribution](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Étape 3 : Utiliser les attributs personnalisés de Voucherify dans votre campagne Braze

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Une fois que l'attribut personnalisé contenant le code est ajouté aux attributs personnalisés du client dans Braze, vous pouvez l'utiliser dans vos campagnes.

Modifiez le corps du message et ajoutez l'attribut personnalisé défini dans la distribution Voucherify. Placez {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} pour afficher le code unique.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

Lorsque cela est prêt, vous pouvez voir le code dans l'aperçu de votre message.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})
