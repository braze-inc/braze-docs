---
nav_title: Shopify
article_title: "Shopify"
description: "Cet article décrit le partenariat avec Braze et Shopify, une société de commerce mondiale qui vous permet de connecter facilement leur magasin Shopify à Braze pour passer certains Webhooks Shopify au Brésil. Tirez parti des stratégies transversales de Braze et de Canvas pour inciter les clients à achever leurs achats, ou les utilisateurs de retargets en fonction de leurs achats précédents."
page_type: partenaire
search_tag: Partenaire
---

# Shopify

> [Shopify](https://www.shopify.com/) est une entreprise commerciale leader dans le monde qui fournit des outils de confiance pour démarrer, croître, commercialiser et gérer une entreprise de détail de toute taille. Shopify rend le commerce meilleur pour tout le monde avec une plate-forme et des services conçus pour la fiabilité tout en offrant une meilleure expérience d'achat pour les consommateurs partout.

L'intégration de Shopify et de Braze permet aux marques de connecter leur magasin Shopify de façon transparente pour passer certains Webhooks Shopify au Brésil. Profitez des stratégies transversales de Braze et de Canvas pour recibler vos utilisateurs avec des messages de caisse abandonnés pour inciter les clients à compléter leurs achats ou retargets en fonction de leurs achats précédents.


<!--
For some Canvas and Campaign examples, please check out our guide here. 
-->

## Pré-requis

Tous les clients Braze qui souhaitent utiliser l'intégration Shopify doivent signer le bon de commande Shopify de Braze. Veuillez contacter votre responsable de compte pour plus de détails.

Cette intégration créera des profils d'utilisateurs d'alias si nous ne sommes pas en mesure de faire correspondre les données de Shopify en utilisant l'e-mail ou le numéro de téléphone ([voir ici pour plus de détails sur le rapprochement utilisateur de Shopify](#shopify-user-syncing)). Veuillez consulter vos équipes de développement autour des impacts en aval et vous devez fusionner ces profils d'utilisateurs dans le cadre de votre cycle de vie utilisateur avant d'activer l'intégration.

| Exigences                                                                                              | Libellé                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Boutique Shopify                                                                                       | Vous devez avoir une boutique active [Shopify](https://www.shopify.com) .<br><br>Veuillez noter qu'en ce moment, vous ne pouvez connecter qu'un seul magasin Shopify par groupe d'applications.                                                                                                            |
| Segmentation des propriétés d'événement activée                                                        | Pour vous assurer que vous pouvez segmenter vos propriétés d'événements Shopify, vous devez travailler avec votre gestionnaire de succès client ou [l'assistance de Braze]({{site.baseurl}}/braze_support/) pour confirmer que vous avez activé la segmentation des propriétés d'événement pour votre tableau de bord. |
| Prise en charge des propriétés d'événements personnalisés imbriquées dans les extensions de segment    | Ceci sera activé avec l'intégration Shopify.<br><br>Vous aurez accès à cette fonctionnalité pour filtrer les propriétés d'événements personnalisés imbriqués Shopify pendant 365 jours au sein des extensions de segment.                                                                                  |
| Prise en charge des propriétés d'événement personnalisées imbriquées pour le déclenchement de messages | Ceci sera activé avec l'intégration Shopify.<br><br>Vous aurez accès à cette fonctionnalité pour déclencher des campagnes et des toiles en utilisant les propriétés imbriquées dans les événements clients Shopify.                                                                                        |
| Support des attributs personnalisés imbriqués                                                          | Ceci sera activé avec l'intégration de Spotify.<br><br>Vous aurez accès à cette fonctionnalité pour recevoir les attributs personnalisés opt-in marketing de Shopify.                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Avec l'intégration clés en main de Braze Shopify, vous pouvez:
- Connectez votre magasin Shopify à Braze en toute transparence
- Autoriser Braze à ingérer et traiter les événements de Webhook Shopify suivants :
  - Créer une commande
  - Mise à jour de la commande
- Synchroniser les profils utilisateur Shopify dans Braze

### Étape 1 : Localiser Shopify dans le tableau de bord
Au Brésil, allez dans la section **Partenaires Technologiques** puis recherchez **Shopify**. Sur la page partenaire de Shopify, sélectionnez **Démarrer la configuration** pour démarrer le processus d'intégration.

!\[Shopify\]\[2\]{: style="max-width:80%;"}

### Étape 2 : Configuration de Shopify
Ensuite, l'assistant de configuration de Braze vous demandera. Dans ce flux, vous devez entrer votre **nom de magasin Shopify**, passer en revue les **événements Webhook Shopify** (l'ingestion commence une fois que l'intégration est connectée), et visitez la place de marché Shopify pour télécharger l'application Shopify non listée. Une fois que vous avez sélectionné **Installer l'application non listée**, vous serez redirigé vers le tableau de bord de Braze.

#### Shopify configuration dans Braze
<br>!\[Shopify\]\[3\]{: style="max-width:80%;"}

#### Installer l'application Braze's Shopify
<br>!\[Shopify\]\[7\]{: style="max-width:60%;"}

### Étape 3 : Vérifier la finalisation
Voilà! Le statut de votre intégration apparaît dans la section **Import de données** de la page partenaire Shopify. Une fois que l'application Braze a été installée avec succès et que la création du webhook est terminée, vous serez averti par e-mail. De plus, le statut **Connexion en attente** sera mis à jour à **Connecté** et affichera l'horodatage de la date à laquelle la connexion a été établie.

!\[Shopify\]\[8\]{: style="max-width:80%;"} !\[Arrow\]\[4\]{: style="max-width:80%;border:0;margin-bottom:5px;"} !\[Shopify\]\[9\]{: style="max-width:80%;"} !\[Arrow\]\[4\]{: style="max-width:80%;border:0;margin-bottom:5px;"} !\[Shopify\]\[10\]{: style="max-width:80%;"}

## Shopify traitement de l'événement

Une fois l'installation de l'application terminée, Braze crée automatiquement votre intégration de webhook avec Shopify. Voir le tableau ci-dessous pour plus de détails sur la carte des événements supportés par Shopify webhook pour les événements personnalisés de Braze et les attributs personnalisés.

### Événements Shopify pris en charge

{% tabs local %}
{% tab Shopify Events %}
| Nom de l'événement           | Type d'événement de Braze                                                                                     | Déclenché quand...                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `La commande est abandonnée` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)           | Shopify met à jour le déclenchement du webhook lorsqu'un client ajoute ou supprime des articles de son panier ET procède plus avant au processus de commande, y compris à l'ajout de leurs informations personnelles.<br><br>Braze écoutera les webhooks de mise à jour entrants de Shopify et déclenchera l'événement personnalisé `shopify_abandoned_checkout` lorsque ce checkout est considéré abandonné après **1 heure** d'activité du panier. |
| `Créer une commande`         | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)           | La commande crée un déclencheur d'événements:<br><br>automatiquement après qu'un client ait terminé un achat dans votre boutique Shopify.<br>**OU**<br>manuellement à travers la section [commandes](https://help.shopify.com/en/manual/orders/create-orders) de votre compte Shopify.                                                                                                                                                   |
| Achat                        | [Evénement de Recharge de Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | La commande de Shopify crée également immédiatement un événement d'achat de Braze.<br><br>_Remarque : le champ Braze `product_id` inclura l'id du produit Shopify._                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Checkout Abandoned Event %}
```json
{
  "name": "shopify_abandoned_checkout",
  "time": "2020-09-10T18:53:37-04:00",
  "properties": {
    "applied_discount": {
      "amount": "30.00",
      "title": "XYZPromotion",
      "description": "Promotionalitemforblackfriday."
    },
    "discount_code": "30_DOLLARS_OFF",
    "total_price": "398. 0",
    "line_items": [
      {
        "product_id": 632910392,
        "grandeur": 1,
        "sku": "IPOD2008PINK",
        "titre": "IPodNano-8GB",
        "vendeur": "Apple",
        "propriétés": "niil",
        "prix": "199. 0"
      }
    ],
    "abandoned_checkout_url": "https://checkout. ocal/690933842/checkouts/123123123/recover?key=example-secret-token",
    "checkout_id": "123123123123"
  }
}

```
{% endsubtab %}
{% subtab Order Created Event %}
```json
{
  "name": "shopify_created_order",
  "time": "2020-09-10T18:53:45-04:00",
  "properties": {
    "total_discounts": "5. 0",
    "total_price": "403. 0",
    "discount_codes": [],
    "line_items": [
      {
        "product_id": 632910392,
        "quantité": 1,
        "sku": "IPOD2008PINK",
        "titre": "IPodNano-8GB",
        "vendeur": "nil",
        "nom": "IPodNano-8GB",
        "propriétés": [],
        "prix": "199. 0"
      },
      {
        "product_id": 632910392,
        "grandeur": 1,
        "sku": "IPOD2008PINK",
        "titre": "IPodNano-8GB",
        "vendeur": "niil",
        "nom": "IPodNano-8GB",
        "propriétés": [],
        "prix": "199. 0"
      }
    ],
    "order_id": 820982911946154500,
    "confirmed": false,
    "order_status_url": "https://apple. yshopify. om/690933842/orders/123456abcd/authenticate? ey=abcdefg",
    "order_number": 1234,
    "cancelled_at": "2020-09-10T18:53:45-04:00",
    "livraison": [
      {
        "title": "Standard",
        "prix": "10. 0"
      },
      {
        "title": "Expédié",
        "prix": "25. 0"
      }
    ],
    "tags": "heavy"
  }
}
```
{% endsubtab %}
{% subtab Purchase Event %}
```json
{
  "product_id": 632910392,
  "currency": "USD",
  "price": "199. 0",
  "temps": "2020-09-10T18:53:45-04:00",
  "quantité": 1,
  "source": "shopify",
  "properties": {
    "name": "IPodNano-8GB",
    "sku": "IPOD2008PINK",
    "title": "IPodNano-8GB",
    "variant_title": "nil",
    "vendeur": "nil",
    "propriétés": []
  }

```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Attributs personnalisés Shopify pris en charge
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Nom de l'attribut                  | Libellé                                                                                                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `La boutique accepte le marketing` | Cet attribut personnalisé correspond au statut de l'email marketing opt-in qui est capturé sur la page de commande.                                                          |
| `Consentement`                     | Cet attribut personnalisé correspond au statut opt-in de marketing SMS qui est capturé sur la page de paiement.                                                              |
| `Balises de shopping`              | Cet attribut correspond aux [tags client](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) définis par les administrateurs Shopify. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Shopify SMS Consent %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_sms_consent": {
        "state": "subscribed",
        "opt_in_level": "single_opt_in",
        "collected_from": "other"
      }

  ]
}
```
{% endsubtab %}
{% subtab Shopify Accepts Marketing (Email) %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_accepts_marketing": true
    }
  ]
 } }
```
{% endsubtab %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_tags": "VIP_customer"
    }
  ]
 } }
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Attributs standard Shopify pris en charge

- Courriel
- Prénom
- Nom de famille
- Téléphone
- Ville
- Pays

{% alert note %}
Braze ne mettra à jour les attributs personnalisés de Shopify et les attributs standard de Braze que s'il y a une différence dans les données du profil utilisateur existant. Par exemple, si les données entrantes de Shopify contiennent un prénom de Bob et Bob existe déjà en tant que prénom sur le profil de l'utilisateur Braze, Braze ne déclenchera pas de mise à jour, et le client ne sera pas facturé un point de données.
{% endalert %}

## Shopify synchronisation utilisateur

Braze associera les données prises en charge Shopify aux profils d'utilisateurs en utilisant l'adresse e-mail ou le numéro de téléphone du client.

**Profils utilisateur identifiés**<br>
- Si l'adresse e-mail ou le numéro de téléphone est associé à un [profil utilisateur identifié]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), Braze synchronise les données Shopify à cet utilisateur.
- Si l'adresse e-mail ou le numéro de téléphone est associé à plusieurs profils d'utilisateurs identifiés, Braze synchronise les données Shopify à celle avec l'activité la plus récente.

**Utilisateurs anonymes**<br>
- Si l'adresse e-mail ou le numéro de téléphone est associé à un profil d'utilisateur anonyme existant ou à un profil d'alias seulement, nous synchronisons les données Shopify avec cet utilisateur.
  - Pour les profils existants uniquement pour alias, nous allons ajouter l'objet alias Shopify pour cet utilisateur (voir ci-dessous).
- Si l'adresse e-mail ou le numéro de téléphone est **non** associé à un profil utilisateur au Brésil, Braze génère un utilisateur seul avec un objet alias Shopify.
  - Si ces utilisateurs seuls sont identifiés, Les clients Braze doivent assigner un ID externe au profil d'alias uniquement en appelant le [point de terminaison d'identification des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

## Utiliser les données Shopify dans Braze
Une fois que vous avez terminé votre intégration, jetez un coup d'œil à notre prochain article [Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/use_cases/) pour apprendre comment utiliser les données de Shopify dans Braze pour la personnalisation et la segmentation dans vos campagnes et Canvases.

## Dépannage

{% détails Pourquoi mon application Shopify est-elle toujours en attente ? %}
Votre installation peut toujours être en attente pour l'une des raisons suivantes :
  - Lorsque Braze met en place vos webhooks Shopify
  - Quand Braze communique avec Shopify

Si l'installation de votre application est en attente pendant 1 heure, Braze échouera et vous serez invité à recommencer l'installation.<br><br> ![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% détails Pourquoi mon application Shopify a-t-elle échoué ? %}
Votre installation a peut-être échoué pour l'une des raisons suivantes :
  - Braze n'a pas pu atteindre Shopify
  - Braze n'a pas réussi à traiter la demande
  - Votre jeton d'accès Shopify n'est pas valide
  - L'application Braze Shopify a été supprimée de votre page d'administration Shopify

Si cela se produit, vous serez en mesure de sélectionner **Réessayer la configuration** et de relancer le processus d'installation.<br><br> ![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% détails Comment désinstaller l'application Braze de ma boutique Shopify ? %}
Vous devrez aller sur votre page d'administration Shopify située sous **Apps**. Vous verrez alors une option pour supprimer l'application Braze<br><br> ![Shopify]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

## RGPD

En ce qui concerne les données personnelles transmises aux services de Braze par ou au nom de ses clients, Braze est le processeur de données et nos clients sont les contrôleurs de données. En conséquence, Braze traite ces données personnelles uniquement à la demande de nos clients et, le cas échéant, avertit nos clients des demandes de données. En tant que contrôleurs de données, nos clients répondent directement aux demandes d'objet des données. Dans le cadre de l'intégration Shopify de la plateforme Braze, Braze reçoit automatiquement [les webhooks RGPD de Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Cependant, Les clients Braze sont en fin de compte responsables de répondre aux demandes de données soumises par leurs clients Shopify en utilisant [Braze SDKs]({{site.baseurl}}/developer_guide/home/) ou [API REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) conformément à nos politiques [de conformité GDPR]({{site.baseurl}}/help/dp-technical-assistance/).
[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} [3]: {% image_buster /assets/img/Shopify/shopify_integration3-6. if %} [4]: {% image_buster /assets/img/Shopify/arrow.jpeg %} [7]: {% image_buster /assets/img/Shopify/shopify_integration7. ng %} [8]: {% image_buster /assets/img/Shopify/shopify_integration8.png %} [9]: {% image_buster /assets/img/Shopify/shopify_integration9. ng %} [10]: {% image_buster /assets/img/Shopify/shopify_integration10.png %} 