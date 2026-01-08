---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "Cet article de référence présente le partenariat entre Braze et Antavo, un programme de fidélité nouvelle génération qui va au-delà de la récompense des achats."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) est un fournisseur de technologie de programme de fidélité SaaS de niveau entreprise qui crée des programmes de fidélité complets pour favoriser l'adoption de la marque et changer le comportement des clients.

_Cette intégration est maintenue par Antavo._

## À propos de l'intégration

L'intégration d'Antavo et de Braze vous permet d'utiliser les données liées aux programmes de fidélisation pour créer des campagnes personnalisées afin d'améliorer l'expérience client. Antavo prend en charge la synchronisation des données de fidélité entre les deux plateformes - il s'agit d'une synchronisation des données à sens unique, d'Antavo vers Braze. L'intégration prend en charge le champ `external_id` Braze, qu'Antavo utilise pour synchroniser l'ID du membre de fidélité.

## Conditions préalables

| Condition          | Description                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Compte Antavo       | Un compte [Antavo](https://antavo.com/) avec l'intégration Braze activée est nécessaire pour profiter de ce partenariat.                                                |
| Clé d'API REST Braze   | Une clé API REST de Braze avec les autorisations suivantes : `users.track`, `events.list`, `events.data_series`, et `events.get`.<br><br>Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.  |
| Endpoint REST de Braze  | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance.                |
| Identifiant de l'application Braze | La clé de l'identifiant de votre application. <br><br>Pour localiser cette clé dans le tableau de bord de Braze, allez dans **Paramètres** > **Clés API** et trouvez la section **Identification**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Connecter Braze à Antavo

Dans Antavo, allez dans **Modules** > **Braze** et cliquez sur **Configurer.** Lors de la première navigation vers la page de configuration de l'intégration de Braze dans Antavo, l'interface vous invitera à connecter les deux systèmes.

Fournissez les informations d'identification suivantes :

- **URL de l'instance :** L'endpoint REST de Braze de l'instance auprès de laquelle vous êtes provisionné.
- **Jeton API (identifiant) :** La clé API REST de Braze que Antavo doit utiliser lors de l'envoi de requêtes à Braze.
- **Identifiant de l'application :** L'identifiant de l'application Braze.

Après avoir saisi les informations d'identification, cliquez sur **Connecter**.

![Connectez l'écran de Braze dans Antavo avec l'URL de l'instance, le jeton API et l'identifiant de l'application.]({% image_buster /assets/img/antavo/connect_braze.png %})

### Étape 2 : Configurer le mappage des champs

Une fois la connexion établie, vous serez automatiquement redirigé vers la page **Synchroniser les champs** dans Antavo pour configurer la synchronisation des champs entre les deux systèmes.   Vous pouvez accéder à cette page à tout moment via **Modules** > **Braze**.

Pour configurer le mappage des champs dans Antavo :

1. Cliquez sur **Ajouter un nouveau champ** <i class="fas fa-plus" alt=""></i>.
2. Utilisez le champ déroulant pour sélectionner le champ Antavo **Fidélité** que vous souhaitez synchroniser avec Braze.
3. Saisissez le **champ distant** représentant l'attribut personnalisé équivalent dans Braze auquel les données seront attribuées.  

{% alert note %}
Vous trouverez votre liste d'attributs personnalisés dans Braze sous **Paramètres des données** > **Attributs personnalisés**. Si le champ que vous saisissez n'est pas défini dans Braze, un nouveau champ sera automatiquement généré lors de la première synchronisation.
{% endalert %}

{:start="4"}
4\. Pour ajouter d'autres combinaisons de champs, répétez les étapes 1 à 3.
5\. Pour supprimer un champ de la liste des données synchronisées, cliquez sur <i class="fa-solid fa-rectangle-xmark" title="Supprimer"></i> à la fin de la ligne.
6\. Cliquez sur **Enregistrer**.

Lorsqu'une valeur des champs configurés change dans Antavo, non seulement la synchronisation de cette seule valeur est déclenchée, mais chaque champ ajouté au mappage des champs est inclus dans la requête.

![Sync Fields page in Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
Pour minimiser la consommation de points de données, nous vous recommandons de ne mapper que les champs qui feront l'objet d'une action dans Braze.
{% endalert %}

#### Types de données pris en charge

L'intégration prend en charge tous les [types de données]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) d’attributs personnalisés de Braze, à savoir : nombre (entier, virgule flottante), chaîne, tableau, booléen, objet, tableau d'objets et date.

![Profil de Braze montrant différents attributs personnalisés.]({% image_buster /assets/img/antavo/braze_profile.png %})

Les champs de données sont remplis en fonction du mappage des champs configuré.

## Déclencheurs

Outre la configuration du mappage des champs, l'intégration offre d'autres possibilités grâce aux fonctionnalités créées dans l'outil [Workflows](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) d'Antavo. Tous les [types de données ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage)d'attributs personnalisés et les [types de données de]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) propriétés d'événements personnalisés de Braze peuvent également être synchronisés par le biais de flux de travail.

### Synchronisation occasionnelle des données de fidélisation

Utilisez cette option si les données ne sont pas stockées dans les champs de fidélité dans Antavo ou si les données ne sont pas ajoutées à la liste des champs mappés. La synchronisation des données demandées est déclenchée lorsque les critères de flux de travail configurés sont remplis.

Consultez le guide pas à pas pour savoir comment configurer la synchronisation des [données de fidélité liées au dernier achat](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

### Synchronisation des événements du programme de fidélisation

Utilisez les événements synchronisés à partir d'Antavo pour inscrire les membres de la fidélité dans des canvas de Braze basées sur l'action. L'intégration peut synchroniser tout événement Antavo (y compris les événements d'achat) qui apparaît dans Braze en tant qu'événements personnalisés.

Consultez le guide pas à pas pour savoir comment configurer la synchronisation de l'[événement d'inscription au programme de fidélisation](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) et la synchronisation de l'[événement d'acquisition des avantages du programme de fidélisation](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).


