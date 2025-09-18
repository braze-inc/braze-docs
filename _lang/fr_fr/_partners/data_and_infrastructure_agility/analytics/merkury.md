---
nav_title: Merkury
article_title: Merkury
description: "Cet article de référence décrit le partenariat entre Braze et Merkury, une plateforme d'identité d'entreprise pour vos applications, qui vous permet de tirer parti du « MerkuryID » pour augmenter les taux de reconnaissance des visiteurs du site pour les clients de Braze."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) est la plateforme d'identité d'entreprise de Merkle qui aide les marques à optimiser l'engagement et l'expérience client ainsi que leurs revenus grâce à des fonctionnalités d'identité sans cookies first party. Il `MerkuryID` unifie les enregistrements des clients et prospects connus et inconnus d'une marque, les visites du site ou de l'application et les données sur les consommateurs en un seul identifiant personnel persistant.

_Cette intégration est maintenue par Merkury._

## À propos de l'intégration

L'intégration de Braze et Merkury vous permet de tirer parti de l'augmentation des taux de reconnaissance des visiteurs `MerkuryID` du site pour les clients de Braze. Après avoir reconnu les visiteurs abonnés aux e-mails de la marque, Merkury mettra à jour le profil Braze pour inclure l'adresse e-mail de l'abonné. Les capacités de reconnaissance accrues `MerkuryID` améliorent les opportunités d'engagement et de personnalisation et augmentent immédiatement le nombre d'envois d'e-mails liés à l'abandon du site et le chiffre d'affaires associé. 

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Merkle | Un compte Merkle est nécessaire pour bénéficier de ce partenariat. |
| ID client Merkle | Obtenez votre ID client auprès de votre conseiller Merkle. |
| Balise Merkury | Placez la balise Merkury de Merkle sur votre site Web. |
| Braze REST et endpoint SDK | Votre URL d’endpoint REST ou SDK. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| Clé API REST de Braze | Une clé API REST de Braze avec des autorisations `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Cette clé peut être créée dans le **tableau de bord de Braze > Console de développement > Clé d’API REST > Créer une nouvelle clé d’API**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Les requêtes du connecteur d'identité Merkury adressées à Braze fonctionnent dans le respect des spécifications de limite de débit de l'API Braze. Contactez Braze ou votre gestionnaire de compte Merkle si vous avez des questions.<br><br>Merkury enverra au moins une requête à la fin d'une session qualifiée.
{% endalert %}

## Intégration simultanée des SDK

Utilise l'étiquette Merkury côté client de Merkle pour capturer les appareils Braze et les redirige vers l’endpoint du connecteur d'identité Merkury pour identification.

### Étape 1 : Configurer l'étiquette du SDK Web Braze

Le [SDK Web Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) doit être déployé sur votre site Web pour utiliser cette intégration.

### Étape 2 : Déployez la balise Merkury de Merkle

Déployez la balise Merkury sur votre site Web. Le connecteur d'identité Merkury sera ainsi disponible sur votre site Web. Un guide détaillé contenant des instructions vous sera fourni par votre gestionnaire de compte Merkle.

### Étape 3 : Création d'attributs personnalisés

[Les champs suivants seront remplis par le connecteur d'identité Merkury et devront être créés dans Braze en tant qu'attributs personnalisés.]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes)

| Nom de l'attribut | Type de données | Description |
| --- | --- | --- |
| `hmid` | Chaîne | Identifiant Merkury de Merkle |
| `confidence_score` | Numéro | Le degré de confiance que Merkury a pu identifier (1 à 8, moins c'est mieux) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 4 : Fournir à Merkle un univers d'e-mails utilisateur

Merkle recommande une exportation par segmentation de votre univers d'e-mails autorisé. Cela peut être suivi par des exportations quotidiennes des utilisateurs autorisés actifs.

Les champs suivants sont obligatoires :

- `braze_id`
- `external_id`
- adresse e-mail

Consultez votre conseiller Braze pour plus d'informations.

