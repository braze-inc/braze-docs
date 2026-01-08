---
nav_title: Modèles de données
article_title: "Création d'un modèle de données B2B"
page_order: 0
page_type: reference
description: "Apprenez à utiliser les outils de données de Braze pour créer des modèles B2B."
---

# Création d'un modèle de données B2B

> Ce cas d'utilisation montre comment vous pouvez utiliser les outils de données Braze pour créer un modèle de données B2B efficace et efficient qui vous aide à cibler, déclencher, personnaliser et envoyer des messages à vos utilisateurs professionnels. 

{% alert note %}
Ces recommandations sont susceptibles d'évoluer au fil du temps, à mesure que Braze crée ses capacités B2B.
{% endalert %}

Avant d'aborder la manière dont vous pouvez mettre en place votre modèle de données B2B, passons en revue plusieurs concepts et termes que vous devez connaître.

Il y a quatre objets principaux B2B dont vous avez besoin pour exécuter des campagnes B2B.

| Objet | Description |
| --- | --- |
| Pistes | Registre des clients potentiels qui ont manifesté de l'intérêt pour un produit ou un service mais qui n'ont pas encore été qualifiés d'opportunité. |
| Contacts | Il s'agit généralement de personnes qui ont été qualifiées et converties d'une piste à un contact pour poursuivre une opportunité de vente. |
| Opportunités | Un enregistrement qui suit les détails d'une vente potentielle ou d'une transaction en cours.
| Comptes | Une organisation qui est un client potentiel qualifié, un client existant, un partenaire ou un concurrent qui entretient une relation d'importance similaire. |
{: .reset-td-br-1 .reset-td-br-2 }

Dans Braze, ces quatre objets sont combinés et réduits en deux objets : les profils utilisateurs et les objets métiers.

| Braze objet B2B | Description | Objets B2B originaux  |
| --- | --- | --- |
| Profils utilisateurs | Ceux-ci mappent directement les pistes et les contacts dans votre système CRM de vente. Parce que les leads sont capturés par Braze, ils sont automatiquement créés en tant que leads dans votre système CRM de vente. Au fur et à mesure qu'ils sont convertis en contacts, les ID et les détails des contacts sont synchronisés avec Braze. |Pistes<br> Contacts |
| Objets de gestion | Ceux-ci mappent tous les objets non-utilisateurs de votre système CRM de vente. Cela inclut vos objets spécifiques aux ventes, tels que les objets de compte et les objets d'opportunité. | Comptes<br> Opportunités |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Étape 1 : Créez vos objets de gestion dans Braze

Les objets de gestion sont tous les ensembles de données non centrés sur l'utilisateur. Dans un contexte B2B, il s'agit notamment des données relatives aux comptes et aux opportunités, ainsi que de tout autre ensemble de données pertinent non centré sur l'utilisateur que votre entreprise suit.

Il existe deux méthodes pour créer et gérer vos objets de gestion dans Braze, les catalogues et les sources connectées. 

| Méthode | Description |
| --- | --- |
| [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs) | Il s'agit d'objets de données indépendants (objets de données supplémentaires) sur le profil utilisateur principal dans Braze. Dans un contexte B2B, vous aurez probablement des catalogues pour vos comptes et vos opportunités. |
| [Sources connectées]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) | Ceux-ci permettent à Braze d'interroger directement votre entrepôt de données. Il est probable que vous synchronisiez déjà régulièrement vos prospects, contacts, opportunités et comptes avec votre entrepôt de données. Vous pouvez donc pointer la segmentation de Braze directement vers cet entrepôt et l'activer dans un environnement sans copie. |
{: .reset-td-br-1 .reset-td-br-2 }

{% tabs %}
{% tab Catalogs %}

### Option 1 : Utiliser des catalogues pour les comptes et les opportunités

Les catalogues sont des tables de données hébergées et gérées dans Braze. Alors que les données relatives aux comptes et aux opportunités proviennent du système CRM de vente de votre choix, vous les dupliqueriez dans Braze pour les utiliser à des fins marketing : segmentation basée sur les comptes, marketing basé sur les comptes, gestion des leads, etc.

Pour cette option, nous vous recommandons de créer un catalogue pour vos comptes et un autre pour vos opportunités, et de les mettre à jour fréquemment en envoyant des mises à jour à Braze par le biais de notre [API catalogues]({{site.baseurl}}/api/endpoints/catalogs/) ou de l'[ingestion de données dans le cloud (CDI) catalogues]({{site.baseurl}}/user_guide/data/cloud_ingestion/sync_catalogs_data/). Lorsque vous créez ces catalogues, assurez-vous que le `id` (première colonne) de votre catalogue correspond au `id` de votre système CRM de vente.

#### Mappage des champs de votre CRM

Les tableaux ci-dessous présentent quelques exemples de champs que vous pouvez mapper à partir des objets "compte" et "opportunité" de votre CRM.

{% subtabs %}
{% subtab Account catalog %}

Dans ce cas d'utilisation, Salesforce est l'exemple de système CRM. Vous pouvez mapper n'importe quel champ inclus dans les objets de votre CRM.

<table border="1">
  <tr>
    <th><b>Objet de Braze</b></th>
    <th><b>Champ de Braze</b></th>
    <th><b>Objet CRM (Salesforce)</b></th>
    <th><b>Champ CRM (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catalogue > Catalogue de comptes</td>
    <td><code>ID</code></td>
    <td><code>compte</code></td>
    <td><code>ID</code></td>
  </tr>
  <tr>
    <td><code>Nom du compte</code></td>
    <td><code>compte</code></td>
    <td><code>Nom du compte</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>compte</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>compte</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### Exemple de tableau des champs de compte mappés

Tableau des comptes Salesforce avec les informations correspondantes, telles que l'adresse de facturation et le propriétaire du compte.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

Dans ce cas d'utilisation, Salesforce est l'exemple de système CRM. Vous pouvez mapper n'importe quel champ inclus dans les objets de votre CRM.

<table border="1">
  <tr>
    <th><b>Objet de Braze</b></th>
    <th><b>Champ de Braze</b></th>
    <th><b>Objet CRM (Salesforce)</b></th>
    <th><b>Champ CRM (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catalogue > Catalogue d'opportunités</td>
    <td><code>ID</code></td>
    <td><code>opportunité</code></td>
    <td><code>ID</code></td>
  </tr>
  <tr>
    <td><code>Nom de l'opportunité</code></td>
    <td><code>opportunité</code></td>
    <td><code>Nom de l'opportunité</code></td>
  </tr>
  <tr>
    <td><code>Territoire</code></td>
    <td><code>opportunité</code></td>
    <td><code>Territoire</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunité</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### Exemple de tableau des champs d'opportunité mappés

Tableau des opportunités Salesforce avec les informations correspondantes, telles que l'adresse de facturation et le propriétaire du compte.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Option 2 : Utiliser des sources connectées pour les comptes et les opportunités

Les sources connectées sont des tables de données que vous hébergez dans votre propre entrepôt de données et qui sont interrogées par les [CDI Segment Extensions de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Contrairement aux catalogues, au lieu de dupliquer vos objets commerciaux (comptes et opportunités) dans Braze, vous les conserverez dans votre entrepôt de données et utiliserez ce dernier comme source de vérité.

Pour configurer les sources connectées, reportez-vous à la section [Intégration des sources connectées]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Étape 2 : Relier vos objets d'entreprise aux profils utilisateurs

Les profils utilisateurs sont l'objet principal de Braze, qui alimente la majorité de votre segmentation démographique, de vos déclencheurs et de votre personnalisation. Les profils utilisateurs comprennent les [données utilisateur par défaut]({{site.baseurl}}/user_guide/data/user_data_collection/) collectées par notre SDK et d'autres sources, y compris les [données personnalisées]({{site.baseurl}}/user_guide/data/custom_data/), qui prennent la forme soit d'attributs (données démographiques), soit d'événements (données comportementales), soit d'achats (données transactionnelles).

### Étape 2.1 : Mappez les ID des CRM de vente à Braze

Tout d'abord, assurez-vous que Braze et le CRM de votre choix disposent d'un identifiant commun pour partager les données. Nous vous suggérons d'utiliser le tableau suivant pour mapper vos champs d'ID du CRM des ventes à l'objet utilisateur de Braze. Dans le tableau ci-dessous, Salesforce est le système CRM, mais cette opération peut être réalisée avec n'importe quel CRM.

#### Objet de Braze : Utilisateur

| Champ de Braze | Objet CRM (Salesforce) | Champ CRM (Salesforce) | Informations complémentaires |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Plomb | `id` |  \- Libellé alias d'utilisateur : `salesforce_lead_id` <br>\- Nom de l'alias d'utilisateur : `lead_id`|
| `Aliases.salesforce_contact_id` | Contact | `id` | \- Libellé alias d'utilisateur : `salesforce_contact_id` <br>\- Nom de l'alias d'utilisateur : `contact_id` |
| `AccountId` | Contact | `AccountId` | 
| `OpportunityId` (optionnel, scalaire) <br>ou<br> `Opportunities` (optionnel, tableau) | Opportunité | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
Nous vous recommandons d'utiliser des [alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) au lieu de `external_id` pour mapper les identifiants de leads et de contacts Salesforce vers Braze. En effet, il réduit le nombre de consultations nécessaires lors de l'identification et de la mise en œuvre de vos initiatives de style croissance axée sur le produit.
{% endalert %}

Après avoir synchronisé vos ID, vous devez relier vos profils utilisateurs Braze à vos objets métier. 

### Étape 2.2 : Créer une relation entre les profils utilisateurs et vos objets d'entreprise

{% tabs %}
{% tab Catalogs %}

#### Option 1 : Lors de l'utilisation de catalogues

Maintenant que les détails de votre opportunité et de votre compte sont pris en compte en tant que catalogues Braze, vous devez créer une relation entre ces catalogues et les profils utilisateurs auxquels vous souhaitez envoyer des messages. Pour l'instant, il faut procéder en deux étapes :

1. Incluez le compte (tel que `account_id (string)`), l'ID de l'opportunité (tel que `opportunity_ids (array)`) ou les deux dans le profil utilisateur en tant qu'attributs.
2. Enregistrez un événement (tel que `account_linked`) qui inclut l'ID du compte en tant que propriété d'événement.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Option 2 : Lors de l'utilisation de sources connectées

L'une des tables de votre source connectée doit inclure un `user_id` qui correspond au `external_user_id` défini dans Braze pour vos utilisateurs. La configuration du profil utilisateur ci-dessus utilise votre lead et `contact_ids` comme `external_id`, vous devez donc vous assurer que vos tables de leads/contacts incluent ces ID.

En plus de vous assurer que les ID correspondent, nous vous recommandons d'écrire des données de base au niveau du compte, telles que `account_id`, `opportunity_id`, et même des attributs firmographiques communs, tels que `industry`, dans les profils utilisateurs pour une segmentation et une personnalisation efficaces.

{% endtab %}
{% endtabs %}