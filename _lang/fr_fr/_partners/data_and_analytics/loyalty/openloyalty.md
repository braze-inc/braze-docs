---
nav_title: Loyauté ouverte
article_title: Loyauté ouverte
description: "L'intégration de Braze et d'Open Loyalty vous permet de synchroniser les données de fidélité, telles que le solde de points, les changements de niveaux et les avertissements d'expiration, directement dans Braze en temps réel."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Loyauté ouverte

> [Open Loyalty](https://www.openloyalty.io/) est une plateforme de programmes de fidélisation basée sur le cloud qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration de Braze et d'Open Loyalty synchronise les données de fidélité, telles que le solde de points, les changements de niveau et les avertissements d'expiration, directement dans Braze en temps réel. Cela vous permet de déclencher des messages personnalisés (e-mail, Push, SMS) lorsque le statut de fidélité d'un utilisateur change.

_Cette intégration est maintenue par Open Loyalty._

## À propos de l'intégration

Cette intégration utilise les transformations de données de Braze pour capturer les webhooks d'Open Loyalty et les mapper aux profils utilisateurs de Braze.

* **Mises à jour en temps réel**: Poussez les événements de fidélisation (points gagnés, passage à un niveau supérieur) vers Braze.
* **Personnalisation**: Utilisez les attributs de fidélité (solde actuel, nom du prochain palier) dans vos modèles de Braze.
* **Bidirectionnel**: Mettez à jour les attributs personnalisés des clients d'Open Loyalty en fonction des données d'engagement de Braze.

## Cas d’utilisation

Cette intégration couvre les flux de données suivants :

1. **Synchronisation des événements vers Braze (Inbound**) : Suivez les changements de points, les passages à un niveau supérieur ou les échanges de récompenses en envoyant des données d'Open Loyalty à Braze. La transformation des données convertit ces données en événement utilisateur.
2. **Modifier les membres Open Loyalty (Outbound**) : Mettez automatiquement à jour les données des membres dans Open Loyalty en fonction du comportement des utilisateurs dans Braze, par exemple en ajoutant des étiquettes "VIP" ou en mettant à jour des attributs personnalisés.

## Conditions préalables

Avant de commencer, vous devez disposer des éléments suivants :

| Condition | Description |
| :--- | :--- |
| Ouvrir un compte de fidélité | Vous devez disposer d'un compte administrateur sur un locataire Open Loyalty pour profiter de ce partenariat. |
| Clé de l'API REST d'Open Loyalty | Une clé API REST d'Open Loyalty (pour les intégrations qui envoient des données de Braze à Open Loyalty). <br><br> Créez-la dans **Paramètres > Admins > Clés API.** |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Créez cette clé dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API.** |
| Transformation des données de Braze | Vous devez avoir accès à l'onglet "Paramètres des données" dans Braze pour configurer les auditeurs de webhook. |
| Correspondance des ID | Le site `external_id` de l'utilisateur dans Braze doit correspondre à son site `loyaltyCardNumber` (ou à un autre identifiant par défaut) dans Open Loyalty. |
| ID de locataire | Votre ID de locataire Open Loyalty (requis pour les mises à jour sortantes). |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Intégration

L'intégration primaire synchronise les événements webhook d'Open Loyalty avec Braze à l'aide de la transformation de données.

### Étape 1 : Générer l'URL du webhook à Braze

Tout d'abord, créez une transformation de données dans Braze afin de générer une URL unique pour la réception des données.

1.  Dans Braze, ouvrez **Paramètres des données > Transformation des données.**
2.  Cliquez sur **Créer une transformation**.
3.  Complétez les champs suivants :
     * **Nom de la transformation**: Donnez un nom descriptif (par exemple, "Ouvrir les événements de mise à jour des points de fidélité").
     * **Sélectionnez la destination**: Sélectionnez **POST : Suivez les utilisateurs**.
4.  Cliquez sur **Créer une transformation**.
5.  Emplacement/localisation de l'**URL du webhook** sur le côté droit et cliquez sur **Copier**.

{% alert important %}
Conservez cette URL en lieu sûr ; vous en aurez besoin pour l'étape suivante.
{% endalert %}

### Étape 2 : Créez l'abonnement au webhook dans Open Loyalty

Indiquez à Open Loyalty d'envoyer des événements spécifiques à l'URL que vous venez de générer.

1.  Connectez-vous à votre panneau d'administration Open Loyalty.
2.  Naviguez vers **Général > Webhooks**.
3.  Cliquez sur **Ajouter un nouveau webhook** et configurez l'abonnement :
    * **nom de l'événement**: Sélectionnez l'événement que vous souhaitez suivre (par exemple, `AvailablePointsAmountChanged`, `CustomerLevelChanged`, ou `CampaignEffectWasApplied`).
    * **url**: Collez l'URL du webhook Braze de l'étape 1.
    * Ajoutez les en-têtes suivants :
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Enregistrez l'abonnement au webhook.

### Étape 3 : Configurer la transformation des données

Écrivez la logique JavaScript dans Braze pour mapper le payload Open Loyalty entrant aux propriétés de Braze.

1.  Dans Braze, ouvrez la transformation de données que vous avez créée à l'étape 1.
2.  Déclenchez l'événement dans Open Loyalty (par exemple, modifiez les points d'un membre ou attribuez un niveau) pour générer un exemple de charge utile dans le volet **des détails du webhook**.
3.  Dans l'éditeur de **code de transformation**, écrivez un script pour mapper les données entrantes. Utilisez l'exemple suivant comme guide :

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,
     
      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",
     
      // timestamp
      "time": new Date().toISOString(),
     
      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4\. Cliquez sur **Valider** pour vous assurer que le code fonctionne avec votre échantillon de charge utile, puis cliquez sur **Activer**.


## Utiliser Open Loyalty avec Braze

Une fois l'intégration entrante terminée, configurez les **mises à jour sortantes** pour modifier les membres Open Loyalty en fonction du comportement de Braze.

### Étape 1 : Configurer la campagne webhook Braze

Ce processus utilise les webhooks Braze pour envoyer une demande `PATCH` à l'API Open Loyalty Member (par exemple, pour ajouter un label " VIP ").

1.  Dans Braze, créez une nouvelle **campagne webhook** (ou utilisez un webhook au sein d'un canvas).
2.  Cliquez sur **Composer un webhook**.
3.  **URL du webhook** : Construisez l'URL en utilisant votre instance Open Loyalty, l'ID du locataire et la variable Braze Liquid pour l'ID de l'utilisateur.
    * Format :
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Complétez les champs suivants :   
    * **Méthode de demande**: `PATCH`
    * **En-têtes de requête**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Corps de la requête** : Sélectionnez `Raw text` et collez la charge utile :

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Étape 2 : Configurer le déclencheur

1.  Accédez à l'onglet **Planification de la réception/distribution**.
2.  Complétez les champs suivants :
    * **Méthode de réception/distribution**: Basé sur l'action.
    * **Déclencheur**: Définissez le déclencheur pertinent (par exemple, un utilisateur saisit un segment spécifique dans Braze).
    * **Lancement**: Activez la campagne.

## Résolution des problèmes

### Vérifier les événements entrants
Lorsque la transformation des données est active, les données apparaissent dans Braze sous la forme d'un événement personnalisé. Vérifiez-le en créant une campagne avec un déclencheur **Perform Custom Event** et en vérifiant si l'événement que vous avez défini (par exemple, `Loyalty Event Triggered`) est disponible.

### Vérifier les webhooks sortants
Vérifiez le journal d'activité des messages dans Braze pour vous assurer que le webhook a renvoyé un état `200 OK`.
* **401 Erreur**: Vérifiez votre jeton API Open Loyalty.
* **Erreur 404**: L'ID de l'utilisateur dans Braze n'existe pas dans Open Loyalty.