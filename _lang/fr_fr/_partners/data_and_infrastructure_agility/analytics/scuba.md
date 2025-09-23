---
nav_title: Scuba
article_title: Analyses Scuba
description: "Cette référence technique Scuba et Braze décrit comment activer les informations sur les données en temps réel de Scuba à l'aide des segments Braze."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Analyses Scuba

>[Scuba Analytics][1] est une plateforme de collaboration de données complète, alimentée par l'apprentissage automatique, conçue pour les données de séries temporelles à grande vitesse. Scuba vous permet d'exporter sélectivement des utilisateurs (également appelés acteurs) et de les charger dans votre plateforme Braze. Dans Scuba, les propriétés d'acteurs personnalisées sont utilisées pour analyser les tendances comportementales, activer vos données sur diverses plateformes et effectuer une modélisation prédictive à l'aide de l'apprentissage automatique.

_Cette intégration est maintenue par Scuba Analytics (si utilisé comme adjectif)._

## Conditions préalables

Pour utiliser Scuba Analytics avec Braze, vous aurez besoin des éléments suivants :

| Condition | Description |
|---|---|
|Jeton API Scuba | Un jeton API Scuba que vous pouvez récupérer à partir de l'endpoint `https://{scuba_hostname}/api/create_token`. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance][1]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Téléchargement de vos données de plongée vers Braze

{% alert important %}
La requête suivante utilise curl. Pour une meilleure gestion des requêtes d'API, nous vous recommandons d'utiliser un client API, tel que Postman.
{% endalert %}

Pour charger vos données Scuba vers Braze, envoyez une requête POST à `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` en utilisant le type de contenu `application/json` :

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Remplacez les éléments suivants :

| Marque substitutive             | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | L'URL de l'endpoint REST de Braze de votre instance Braze actuelle. Pour plus d'informations, voir la section consacrée aux [clés de l'API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Votre clé API REST de Braze avec l'autorisation `users.track`.                                                                                                                                      |
| `HOSTNAME`              | Le nom d'hôte de votre instance Scuba actuelle.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Votre jeton d’API Scuba.                                                                                                                                                                           |
| `TABLE_NAME`            | La table à laquelle appartient votre jeu de données. Pour plus d'informations, reportez-vous au [Glossaire : Table de jeux de données][3].                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | La propriété de l'acteur à laquelle appartient votre jeu de données. Seules les données correspondant à ce nom seront renvoyées. Pour plus d'informations, reportez-vous au [Glossaire : Propriété de l'acteur][4].                                             |
| `ACTOR_PROPERTY_FILTER` | Le filtre d'audience pour votre propriété d'acteur.                                                                                                                                             |
| `ACTOR_ID`              | L'ID de la propriété de l'acteur à laquelle appartient votre jeu de données. Cet ID correspond à votre `external_id` dans Braze. Pour plus d'informations, reportez-vous au [Glossaire : Acteur][5].                                              |
| `PERIOD_START`          | La période de démarrage en tant que date compatible avec BQL. Pour plus d'informations, consultez la section [Syntaxe et utilisation de BQL][6].                                                                                                 |
| `PERIOD_END`            | La période de fin en tant que date compatible avec BQL. Pour plus d'informations, consultez la section [Syntaxe et utilisation de BQL][6].                                                                                                   |
| `RECORD_LIMIT`          | **Facultatif** : Le nombre maximum d'enregistrements à renvoyer. Si `scuba_record_limit` n’est pas défini, Scuba renverra un maximum de 100 enregistrements. Pour modifier ce paramétrage, attribuez à `scuba_record_limit` un nombre positif quelconque.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportement par défaut

Par défaut, `update_existing_only` est défini sur `false`, ce qui mettra à jour vos enregistrements existants dans Braze et créera de nouveaux enregistrements pour ceux qui n'existent pas. Pour empêcher Scuba de créer de nouveaux enregistrements, définissez `update_existing_only` sur `true`.

### Limite de débit

Scuba applique une limite de débit de 50 000 requêtes par minute à cet endpoint.

## Création de segments à l'aide des données comportementales de Scuba

Après avoir [téléchargé vos données](#uploading-your-scuba-data-to-braze), vous pouvez créer des segments d'utilisateurs dans Braze en utilisant les données comportementales de Scuba.

### Étape 1 : Créer une nouvelle segmentation

Dans Braze, allez dans **Audience** > **Segments**, puis sélectionnez **Créer un segment** et saisissez un nom pour votre segment.

![Création d'un nouveau segment dans Braze.][501]

### Étape 2 : Recherchez et sélectionnez l'attribut Scuba

Sous **Détails du segment** > **Filtres**, sélectionnez **Attributs personnalisés**.

![Sélectionnez le filtre "Attribut personnalisé" sous "Détails du segment".][502]

Sélectionnez **Rechercher des attributs personnalisés**, puis choisissez le nom de la propriété de l'acteur que vous avez utilisé dans votre requête POST précédente.

![Sélection de la propriété de l'acteur en tant qu'attribut personnalisé.][503]

### Étape 3 : Configurez l'attribut

En regard du nom de votre propriété d'acteur, choisissez un opérateur et une valeur (le cas échéant). Ces valeurs sont déterminées par les propriétés des acteurs que vous avez définies dans Scuba. Lorsque vous avez terminé, sélectionnez **Enregistrer.**

![Choisir une opération et une valeur pour le ][504] sélectionné


[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/analytics/segment_name.png %}
[502]: {% image_buster /assets/img/scuba/analytics/filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/analytics/select_property.png %}
[504]: {% image_buster /assets/img/scuba/analytics/operator_end.png %}
