---
nav_title: Merkury
article_title: Merkury
description: "Cet article de référence décrit le partenariat entre Braze et Merkury, une plateforme d’identité d’entreprise pour vos applications, qui vous permet de tirer parti du `MerkuryID` pour augmenter les taux de reconnaissance des visiteurs du site pour les clients Braze."
page_type: partner
search_tag: Partenaire

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) est la plateforme d'identité d'entreprise de Merkle qui aide les marques à maximiser l'engagement, l'expérience et les revenus des consommateurs grâce à des capacités d'identité sans cookie first-party. Le `MerkuryID` regroupe les dossiers clients et prospects connus et inconnus d’une marque, les visites du site/de l’application et les données des consommateurs en un seul ID de personne persistant.

L'intégration de Braze et Merkury vous permet de tirer parti du `MerkuryID` pour augmenter les taux de reconnaissance des visiteurs du site pour les clients Braze. Après avoir reconnu les visiteurs qui sont des utilisateurs abonnés aux e-mails de la marque, Merkury mettra à jour le profil Braze pour inclure l’adresse e-mail de ces abonnés. L’augmentation des capacités de reconnaissance du `MerkuryID` améliore l’engagement et les opportunités de personnalisation et augmente immédiatement les quantités d’envoi d’e-mails d’abandon de site et les revenus associés. 

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Merkle | Un compte Merkle est requis pour profiter de ce partenariat. |
| ID client Merkle | Obtenez votre ID client auprès de votre conseiller Merkle. |
| Balise Merkury | Placez la balise Merkury de Merkle sur votre site Web. |
| Endpoint et SDK et d’API REST Braze | L’URL de votre endpoint REST ou SDK. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Pour créer une clé API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Les requêtes de connecteur d’identité Merkury à Braze fonctionnent conformément aux spécifications de limite de débit de l’API de Braze. Contactez Braze ou votre gestionnaire de compte Merkle si vous avez des questions.<br><br>Merkury enverra au moins une requête à la fin d’une session qualifiée.
{% endalert %}

## Intégration SDK côte à côte

Utilise la balise Merkury côté client de Merkle pour capturer les appareils Braze et les transmet à l’endpoint du connecteur d’identité Merkury pour identification.

### Étape 1 : Configurer la balise du SDK Web de Braze

Le [SDK Web Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) doit être déployé sur votre site Web pour utiliser cette intégration.

### Étape 2 : Déployer la balise Merkury de Merkle

Déployez la balise Merkury sur votre site Web. Cela rendra le connecteur d'identité Merkury disponible sur votre site Web. Un guide détaillé contenant des instructions vous sera fourni par votre gestionnaire de compte Merkle.

### Étape 3 : Créer des attributs personnalisés

Les champs suivants seront renseignés par le connecteur d'identité Merkury et doivent être créés dans Braze en tant qu'[attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes).

| Nom de l’attribut | Type de données | Description |
| --- | --- | --- |
| `hmid` | String | ID Merkury de Merkle |
| `confidence_score` | Nombre | Avec quel niveau de confiance Merkury a pu identifier (1 à 8, plus la valeur est basse, mieux c’est) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Étape 4 : Fournir à Merkle un ensemble d’e-mails utilisateur

Merkle recommande une exportation de segmentation de votre ensemble d’e-mails autorisés. Elle peut être suivie d’exportations quotidiennes des utilisateurs actifs autorisés.

Les champs suivants sont obligatoires :

- `braze_id`
- `external_id`
- Adresse e-mail

Contactez votre conseiller Braze pour plus d’informations.