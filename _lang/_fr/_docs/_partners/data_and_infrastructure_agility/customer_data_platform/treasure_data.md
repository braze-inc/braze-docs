---
nav_title: Données du trésor
article_title: Données du trésor
page_order: 3.5
description: "Cet article décrit le partenariat entre Braze et Trésor, une plateforme de données client d'entreprise qui vous permet d'écrire directement des résultats des travaux de Treasure Data vers Braze."
alias: /fr/partners/treasure_data/
page_type: partenaire
search_tag: Partenaire
---

# Données du trésor

> [Données au trésor][4] est la seule plate-forme de données client (CDP) d'entreprise qui permet de tirer des expériences clients pertinentes en harmonisant les données, Perspectives et Engagement à travailler à l'unisson. Treasure Data permet aux marques de donner à des millions de leurs clients et clients potentiels le sentiment que chacun est le seul et unique client. Armé de ces indicateurs actionnables, les équipes CX, y compris le marketing, la vente et le service à la clientèle, peuvent optimiser efficacement les dépenses, et personnaliser les interactions omnicanales à travers tout le parcours du client.

{% include video.html id="Zqdm33TWr0E" align="right" %}

Treasure Data prend en charge la plateforme Braze en vous permettant d'écrire les résultats des tâches directement vers Braze. Cette intégration vous permet de :
* __Mapper les identifiants externes__: IDs de carte de votre système CRM vers le compte utilisateur Braze.
* __Gérer l'opt-out__: Lorsqu'un utilisateur final met à jour son consentement en choisissant de ne pas participer.
* __Téléchargez votre suivi des événements, achats ou attributs de profil personnalisés__. Ces informations peuvent vous aider à construire des segments de clients précis qui améliorent l'expérience utilisateur de vos campagnes.

## Exigences

| Exigences                                              | Origine           | Accès                                                                                                                                                                                                                                                                | Libellé                                                                                                                                                                                |
| ------------------------------------------------------ | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API Braze                                          | Brasero           | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. rack__, __users.delete__, __users.alias.new__, __users.identify__ permissions. | Ces clés API prennent en charge la fonctionnalité actuelle pour synchroniser les profils de données Trésor au Brésil, y compris : mapping des ID externes, Upload Tracking, et opt-out |
| Point de terminaison REST Braze                        | Brasero           | [Liste des points d'extrémité REST Braze][1]                                                                                                                                                                                                                         | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                              |
| Données de trésor et informations sur le compte client | Données du trésor | [https://www.treasuredata.com/fr/custom-demo/](https://www.treasuredata.com/custom-demo/)                                                                                                                                                                            | Vous devez avoir un compte de données Trésor actif pour utiliser leurs services avec Braze                                                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exporter l'intégration

Pour plus d'informations, consultez la [Documentation des produits des données du trésor][5]

### Étape 1 : Obtenir la clé API REST à Braze

Obtenez les points de terminaison et clés de Braze requis détaillés dans la section des exigences précédentes.

### Étape 2 : Créer une nouvelle connexion
Dans Treasure Data, vous devez créer et configurer la connexion de données avant d'exécuter votre requête. Dans le cadre de la connexion de données, vous devez fournir une authentification pour accéder à l'intégration.

1. Tout d'abord, ouvrez la console de données Trésor et accédez au __Catalogue__ sous le __Hub d'intégrations__.
2. Ensuite, recherchez et sélectionnez __Braze__. À partir d'ici, une invite d'authentification __nouvelle__ s'ouvrira.
3. Ajoutez les identifiants __Braze API Key__ et __Endpoint__ pour vous authentifier.
4. Enfin, nommez votre connexion et sélectionnez __Terminé__.

!\[Dialogue d'authentification des données du trésor\]\[2\]{: style="max-width:80%;"}

### Étape 3: Définissez votre requête
1. Naviguez vers __Requêtes__ sous votre Atelier de données ____.
2. Sélectionnez une requête pour laquelle vous souhaitez exporter des données.
3. Exécutez la requête pour valider le jeu de résultats.
4. Ensuite, sélectionnez __Résultats d'exportation__ puis sélectionnez une authentification d'intégration existante.
5. Définissez des paramètres supplémentaires de résultats d'exportation tels que décrits dans la section de personnalisation ci-dessous et sélectionnez __Terminé__.
6. Exécutez votre requête.
7. Validez que vos données ont été déplacées vers la destination que vous avez spécifiée.

## Personnalisation

Les paramètres des résultats d'exportation sont décrits dans le tableau suivant.

!\[Dialogue de configuration d'exportation\]\[3\]{: style="max-width:80%;"}

| Paramètre                                  | Valeurs                                                                                                                        | Libellé                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `mode`                                     | Utilisateur - Nouvel Alias<br>Utilisateur - Identification<br>Utilisateur - Suivi<br>Utilisateur - Supprimer | Mode Connecteur                                                                                                                   |
| `champs pré-formés`                        | chaîne de caractères                                                                                                           | Utiliser pour le tableau ou les colonnes JSON pour conserver le format.                                                           |
| `type_track_record_`                       | Événements personnalisés<br>Achetés<br>Attributs du profil utilisateur                                             | Type d'enregistrement pour __Utilisateur - Mode Suivi__                                                                           |
| `sauter sur les enregistrements invalides` | Boolean                                                                                                                        | Si activé, continuer et ignorer tous les enregistrements non valides pour la colonne JSON. <br> Sinon, le travail s'arrête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Cas d'utilisation

Vous pouvez synchroniser vos profils de clients consolidés à partir de Treasure Data vers Braze pour construire des segments cibles. Treasure Data prend en charge les données de cookies de première partie, les identifiants mobiles, les systèmes tiers comme votre CRM, et bien plus encore.

## Webhooks

Les utilisateurs de Treasure Data peuvent ingérer des données via l'API REST publique. Vous pouvez utiliser les données Trésor pour créer des webhooks personnalisés dans vos données. Pour en savoir plus, visitez la [Documentation des données du Trésor][6]
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %} [3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
