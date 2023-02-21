---
nav_title: Treasure Data
article_title: Treasure Data
page_order: 3.5
description: "Cet article présente le partenariat entre Braze et Treasure Data, une plateforme de données client d’entreprise qui vous permet d’écrire les résultats de votre travail directement dans Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partenaire

---

# Données précieuses

> [Treasure Data][4] est la seule plateforme de données client (CDP) d’entreprise qui favorise des expériences client pertinentes en harmonisant les données, les insights et l’engagement pour qu’ils fonctionnent en parfait accord. Avec ces indicateurs exploitables, les équipes d’expérience client (CX), y compris les équipes de marketing, de ventes et de service client, peuvent optimiser leurs dépenses et personnaliser les interactions omnicanal sur l’ensemble du parcours client.

L’intégration de Braze et de Treasure Data vous permet d’écrire les résultats issus de Treasure Data directement dans Braze, en vous permettant de :
* **Mapper des ID externes** : Mapper des ID sur le compte utilisateur Braze depuis votre système de gestion de la relation client (CRM). 
* **Gérer les désinscriptions** : Lorsqu’un utilisateur final met à jour son consentement et choisit de se désabonner.
* **Téléchargez votre suivi des événements, des achats ou des attributs de profil personnalisés**. Ces informations peuvent vous aider à créer des segments de clients précis qui améliorent l’expérience utilisateur de vos campagnes.

## Conditions préalables

| Configuration requise | Description |
| --- | --- |
| Compte Treasure Data | Un [compte Treasure Data](https://www.treasuredata.com/custom-demo/) est requis pour profiter de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec des autorisations `users.track`, `users.delete`, `users.alias.new` et `users.identify`.<br><br>Cela peut être créé dans le **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New Api Key (Créer une nouvelle clé API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][1]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Cas d’utilisation

Vous pouvez synchroniser vos profils clients consolidés depuis Treasure Data vers Braze pour créer des segments cibles. Treasure Data prend en charge les données de cookies internes, les ID mobiles, les systèmes tiers comme votre système de gestion de la relation client (CRM), et bien d’autres encore.

## Intégration

### Étape 1 : Créer une nouvelle connexion

Dans Données précieuses, accédez au **Catalog (Catalogue)** sous le **Integrations Hub (Hub des intégrations)**, puis cherchez et sélectionnez **Braze**. 

Dans l’invite **New Authentication (Nouvelle authentification)** qui s’affiche, nommez votre connexion et fournissez votre clé API REST et l’endpoint REST de Braze. Pour finir, cliquez sur **Done (Terminé)**.

![][2]{: style="max-width:80%;"}

### Étape 2 : Définir votre requête

Dans Treasure Data, accédez à **Queries (Requêtes)** sous votre **Data Workbench (Utilitaire de données)** et sélectionnez une requête pour laquelle vous souhaitez exporter des données. Exécutez cette requête pour valider l’ensemble des résultats.

Ensuite, sélectionnez **Export Results (Exporter les résultats)** et sélectionnez une authentification d’intégration existante.

![][11]{: style="max-width:80%;"}

Définissez les paramètres supplémentaires des résultats d’exportation comme indiqué dans la [section de personnalisation](#customization) suivante. Dans votre contenu d’intégration de l’exportation, passez en revue les paramètres d’intégration.

![Page « Export Results (Exporter les résultats) ». Cette page affiche les champs « mode », « type d’enregistrement de suivi » et « champs préformatés ». Dans cet exemple, « User-Track » et « Custom Events » sont définis dans ces champs, respectivement.][3]{: style="max-width:80%;"}

Enfin, cliquez sur **Done (Terminé)**, exécutez votre requête et vérifiez que vos données ont bien été transférées vers Braze.

### Personnalisation

Les paramètres des résultats d’exportation sont inclus dans le tableau suivant :

| Paramètre | Valeurs | Description |
|---|---|---|
| `mode` | Utilisateur - Nouvel Alias<br>Utilisateur - Identification<br>Utilisateur - Suivi<br>Utilisateur - Suppression | Mode connecteur |
| `pre_formated_fields` | Chaîne de caractères | Utilisée pour conserver le format des colonnes de la matrice ou des colonnes JSON. |
| `track_record_type` | Événements personnalisés<br>Achats<br>Attributs du profil utilisateur| Type d’enregistrement pour le mode **Utilisateur - Suivi** |
| `skip_on_invalid_records` | Booléen | Si cette option est activée, continuez en ignorant tous les enregistrements non valides de la colonne JSON. <br> Sinon, le travail s’arrête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Rendez-vous sur le site Web de [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) pour plus d’informations sur les champs préformatés, les requêtes d’exemple, les détails des paramètres et la planification des tâches d’exportation de requêtes.
{% endalert %}

## Webhooks

Les utilisateurs de Treasure Data peuvent intégrer des données via l’API REST publique. Vous pouvez utiliser Treasure Data pour créer des Webhooks personnalisés dans vos données. Pour en savoir plus, rendez-vous sur le site Web de [Treasure Data][6]

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
[10]: {% image_buster /assets/img/treasure_data/query_1.png %}
[11]: {% image_buster /assets/img/treasure_data/query_2.png %}
