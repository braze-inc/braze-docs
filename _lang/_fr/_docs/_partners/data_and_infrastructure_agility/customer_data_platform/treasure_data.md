---
nav_title: Données du trésor
article_title: Données du trésor
page_order: 3.5
description: "Cet article décrit le partenariat entre Braze et Treasure Data, une plate-forme de données client d'entreprise qui vous permet d'écrire les résultats directement au Brésil."
alias: /fr/partners/treasure_data/
page_type: partenaire
search_tag: Partenaire
---

# Données du trésor

> [Données au trésor][4] est la seule plate-forme de données client (CDP) d'entreprise qui permet de générer des expériences clients pertinentes en harmonisant les données, des idées et de l'engagement à travailler à l'unisson. Armé de ces indicateurs actionnables, les équipes CX, y compris le marketing, les ventes et le service à la clientèle, permet d'optimiser efficacement les dépenses et de personnaliser les interactions de l'omnicanal tout au long du parcours du client.

{% include video.html id="Zqdm33TWr0E" align="right" %}

L'intégration de Braze et de Treasure Data vous permet d'écrire les résultats des tâches de Treasure Data directement au Brésil, vous laissant :
* **Mapper les identifiants externes**: Mapper les identifiants vers le compte utilisateur Braze de votre système CRM.
* **Gérer l'opt-out**: Lorsqu'un utilisateur final met à jour son consentement en choisissant de ne pas participer.
* **Téléchargez votre suivi des événements, achats ou attributs de profil personnalisés**. Ces informations peuvent vous aider à construire des segments de clients précis qui améliorent l'expérience utilisateur de vos campagnes.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte de données Trésor        | Un [compte de données Trésor](https://www.treasuredata.com/custom-demo/) est requis pour profiter de ce partenariat.                                                                                                                                                      |
| Braze clé API REST              | Une clé API Braze REST avec `utilisateurs.track`, `utilisateurs. elete`, `users.alias.new`, `users.identify` permissions.<br><br>Ceci peut être créé dans le **Tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][1].                                                                                                                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Cas d'utilisation

Vous pouvez synchroniser vos profils de clients consolidés à partir de Treasure Data vers Braze pour construire des segments cibles. Treasure Data prend en charge les données de cookies de première partie, les identifiants mobiles, les systèmes tiers comme votre CRM, et bien plus encore.

## Intégration

### Étape 1 : Créer une nouvelle connexion

Dans les Données au Trésor, accédez au **Catalogue** sous le **Hub d'intégration** et recherchez et sélectionnez **Braze**.

Dans l'invite **Nouvelle Authentification** qui apparaît, nommez votre connexion et fournissez votre clé API Braze REST et votre point de terminaison REST. Sélectionnez **Terminé** une fois terminé.

!\[Dialogue d'authentification des données du trésor\]\[2\]{: style="max-width:80%;"}

### Étape 2 : Définir votre requête

En Trésor, accédez à **Requêtes** sous votre établi de données **** et sélectionnez une requête pour laquelle vous souhaitez exporter des données. Exécutez cette requête pour valider le jeu de résultats.

Ensuite, sélectionnez **Résultats d'exportation** et sélectionnez une authentification d'intégration existante.

!\[Treasure Data query\]\[11\]{: style="max-width:80%;"}

Définissez des paramètres de résultats d'exportation supplémentaires tels que décrits ci-dessous dans la section [de personnalisation](#customization). Dans le contenu de votre intégration d'exportation, consultez les paramètres d'intégration.

!\[Treasure Data query\]\[3\]{: style="max-width:80%;"}

Enfin, sélectionnez **Terminé**, exécutez votre requête et validez que vos données ont été déplacées vers Braze.

### Personnalisation

Les paramètres des résultats d'exportation sont inclus dans le tableau suivant :

| Paramètre                                  | Valeurs                                                                                                                        | Libellé                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `mode`                                     | Utilisateur - Nouvel Alias<br>Utilisateur - Identification<br>Utilisateur - Suivi<br>Utilisateur - Supprimer | Mode Connecteur                                                                                                                   |
| `champs pré-formés`                        | Chaîne de caractères                                                                                                           | Utiliser pour le tableau ou les colonnes JSON pour conserver le format.                                                           |
| `type_track_record_`                       | Événements personnalisés<br>Achetés<br>Attributs du profil utilisateur                                             | Type d'enregistrement pour **Utilisateur - Mode Suivi**                                                                           |
| `sauter sur les enregistrements invalides` | Boolean                                                                                                                        | Si activé, continuer et ignorer tous les enregistrements non valides pour la colonne JSON. <br> Sinon, le travail s'arrête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Visitez [Données au trésor][5] pour plus d'informations sur les champs pré-formatés, les exemples de requêtes, les détails des paramètres et la planification des tâches d'exportation de requête.
{% endalert %}

## Webhooks

Les utilisateurs de Treasure Data peuvent ingérer des données via l'API REST publique. Vous pouvez utiliser les données Trésor pour créer des webhooks personnalisés dans vos données. Pour en savoir plus, visitez [Données au trésor][6]
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %} [3]: {% image_buster /assets/img/treasure_data/braze_export_configuration. ng %} [10]: {% image_buster /assets/img/treasure_data/query_1.png %} [11]: {% image_buster /assets/img/treasure_data/query_2.png %}

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
