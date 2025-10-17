---
nav_title: Notifier
article_title: Notifier
description: "Cet article de référence présente le partenariat entre Braze et Notify, une solution de personnalisation omnicanale en temps réel qui offre une personnalisation tout au long du cycle de vie du client."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notifier

> [Notify](https://fr.notify-group.com/) est une solution logicielle basée sur l'intelligence artificielle qui s'intègre de façon fluide aux outils de gestion de la relation client afin d'améliorer les stratégies marketing et de faciliter l'engagement sur plusieurs canaux.

L'intégration de Braze et Notify permet aux marketeurs de stimuler efficacement l'engagement sur différentes plateformes. Au lieu de s'appuyer sur les méthodes de marketing traditionnelles, une campagne déclenchée par l'API de Braze peut exploiter les capacités de Notify pour diffuser des messages personnalisés par le biais de plusieurs canaux, notamment les e-mails, les SMS, les notifications push et bien plus encore.

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

| Exigence          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Clé d'API REST Braze  | Une clé d’API REST de Braze avec les autorisations `users.export.segment` et `campaigns.trigger.send`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Configuration du CNAME | Un sous-domaine doit être créé pour le pixel de suivi utilisé dans l'e-mail pour que Notify puisse suivre l'engagement de l'utilisateur avec le message afin d'informer davantage le modèle. Partagez l'URL du sous-domaine avec Notify après sa création. |
| Exportation de la base de données de l'abonnement (opt-in) | Envoyez à Notify les données relatives aux campagnes et aux achats de l'année écoulée (12 mois). ​Cette exportation sera utilisée pour entraîner le modèle prédictif Notify. <br><br> **Domaines :** <br><br> **E-mail :** Un hachage SHA256 de l'e-mail, converti en minuscules et dont les espaces de début et de fin ont été supprimés.<br><br>**Segment :** Les informations de segmentation définissant le niveau d'activité (actif ou inactif).<br><br>**Segmentation :** Toute autre information pertinente sur l'activité, telle que le niveau d'activité d'achat.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créer votre campagne

Créez une [campagne déclenchée par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery) dans Braze. Partagez ensuite la campagne `api_identifier` avec Notify.

### Étape 2 : Créez votre segmentation à Braze

Ensuite, créez le segment d'utilisateurs qu'ils souhaitent cibler avec la campagne créée à l'[étape 1.](#step-1-create-your-campaign) Partagez ensuite l'ID du segment avec Notify.

### Étape 3 : Récupérez votre segmentation

Ensuite, Notify exportera les utilisateurs du segment rattaché à la campagne.

### Étape 4 : Notifier déclenche la campagne

À l'aide de l'endpoint `/campaigns/trigger/send`, l'intelligence artificielle de Notify déclenche la campagne Braze créée à l'[étape 1](#step-1-create-your-campaign) pour l'envoyer aux utilisateurs au moment qu'ils jugent le plus propice à l'engagement.
