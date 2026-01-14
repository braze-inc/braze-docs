---
nav_title: Treasure data
article_title: Données sur les trésors
description: "Cet article de référence décrit le partenariat entre Braze et Treasure Data, une plateforme de données clients d'entreprise qui vous permet d'écrire les résultats des tâches directement dans Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [Treasure Data](https://www.treasuredata.com/) est une plateforme de données client (CDP) qui collecte et achemine des informations provenant de sources multiples vers divers autres emplacements de votre pile marketing.

L'intégration de Braze et Treasure Data vous permet de transférer les résultats des tâches depuis Treasure Data directement dans Braze. Vous pouvez ainsi :
* **Mapper les identifiants externes** : Associez les identifiants au compte utilisateur Braze depuis votre système CRM. 
* **Gérer la désinscription** : Lorsqu'un utilisateur final met à jour son consentement en choisissant de ne pas participer.
* **Téléchargez votre suivi des événements, des achats ou des attributs de profil personnalisés**. Ces informations peuvent vous aider à créer des segments de clientèle précis qui améliorent l'expérience utilisateur pour vos campagnes.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Treasure Data | Un [compte Treasure Data](https://www.treasuredata.com/custom-demo/) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST Braze avec les autorisations `users.track`, `users.delete``users.alias.new` et `users.identify`.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Cas d'utilisation

Vous pouvez synchroniser vos profils clients consolidés depuis Treasure Data vers Braze afin de définir des segments cibles. Treasure Data prend en charge les données de cookies internes, les identifiants d’appareils mobiles, les systèmes tiers tels que votre CRM, et bien plus encore.

## Intégration

### Étape 1 : Créer une nouvelle connexion

Dans Treasure Data, accédez au **catalogue** sous le **hub d'intégrations**, recherchez et sélectionnez **Braze.** 

Dans l’invite **Nouvelle authentification** qui s'affiche, nommez votre connexion et indiquez votre clé API REST Braze et votre endpoint REST. Sélectionnez **Terminé** lorsque vous avez terminé.

![]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### Étape 2 : Définissez votre requête

Dans Treasure Data, accédez à **Requêtes** dans votre **Data Workbench** et sélectionnez une requête pour laquelle vous souhaitez exporter des données. Exécutez cette requête pour valider le jeu de résultats.

{% alert note %}
Pour les utilisateurs qui utilisent HIVE pour créer des requêtes, HIVE exige que toutes les colonnes ou tous les tableaux commençant par un trait de soulignement soient placés entre guillemets. Par exemple,`_merge_objects`.
{% endalert %}

Ensuite, sélectionnez **Exporter les résultats** et sélectionnez une authentification d'intégration existante.

![]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

Définissez des paramètres de résultats d'exportation supplémentaires comme indiqué dans la [section de personnalisation](#customization) suivante. Dans votre contenu d'intégration d'exportation, passez en revue les paramètres d'intégration.

![La page « Exporter les résultats ». Cette page contient les champs permettant de spécifier le mode, le suivi des types d’enregistrement et des champs préformatés. Dans cet exemple, les champs "User-Track" et "Custom Events" sont respectivement définis comme suit :]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

Enfin, sélectionnez **Terminé**, exécutez votre requête et confirmez que vos données ont été transférées vers Braze.

### Personnalisation

Les paramètres des résultats d'exportation sont inclus dans le tableau suivant :

| Paramètre                 | Valeurs | Description |
|---------------------------|---|---|
| `mode`                    | Utilisateur - Nouvel alias<br>Identification de l'utilisateur<br>Utilisateur - Suivre<br>Utilisateur - Supprimer | Mode connecteur |
| `pre_formatted_fields`    | Chaîne de caractères | Utilisez-le pour les colonnes de type tableau ou JSON afin de conserver le format. |
| `track_record_type`       | Événements personnalisés<br>Achats<br>Attributs du profil utilisateur| Type d'enregistrement pour **Utilisateur - Mode suivi** |
| `skip_on_invalid_records` | Booléen | Si cette option est activée, continuez et ignorez tout enregistrement non valide pour la colonne JSON. <br> Dans le cas contraire, le travail s'arrête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Visitez [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) pour plus d'informations sur les champs préformatés, les exemples de requêtes, les détails des paramètres et la planification des tâches d'exportation des requêtes.
{% endalert %}

## Webhooks

Les utilisateurs de Treasure Data peuvent ingérer des données via l'API REST publique. Vous pouvez utiliser Treasure Data pour créer des webhooks personnalisés dans vos données. Pour en savoir plus, visitez [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API)

