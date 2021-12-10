---
nav_title: Toucher haut
article_title: Toucher haut
description: "Cet article détaille le partenariat entre Braze et Hightouch, une plateforme pour synchroniser les données de vos clients de votre entrepôt aux outils commerciaux."
alias: /fr/partners/hightouch/
page_type: partenaire
search_tag: Partenaire
---

# Toucher haut

> [Hightouch][1] est une plate-forme moderne d'intégration de données qui vous permet de synchroniser le client, le produit, le client ou des données de propriété de votre entrepôt ou de votre lac de données vers n'importe quelle application de votre choix, le tout sans l'aide de vos équipes informatiques ou d'ingénierie.

L'intégration de Braze et Hightouch vous permet de construire de meilleures campagnes sur Braze avec des données clients actualisées à partir de votre entrepôt de données. Vous souhaitez fournir des interactions pertinentes et opportunes à vos clients, et le faire repose fortement sur les données dans votre compte Braze pour être précis et frais. En synchronisant automatiquement les données clients de votre entrepôt de données dans Braze, vous n'avez plus besoin de vous soucier de la cohérence des données, et vous pouvez vous concentrer sur la construction d'expériences de classe mondiale.

## Exigences

| Exigences                       | Origine      | Accès                                                                                                                                                                                                      | Libellé                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Clé API Braze                   | Brasero      | Vous devrez créer une nouvelle clé API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | Vous utiliserez votre clé API Braze pour vous authentifier en utilisant Hightouch. |
| Point de terminaison REST Braze | Brasero      | [Braze liste de terminaux REST][2].                                                                                                                                                                        | Votre URL de terminaison REST.                                                     |
| Compte Hightouch                | Toucher haut | Votre espace de travail Hightouch                                                                                                                                                                          | Un compte Hightouch actif.                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration de Braze et Hightouch

### Étape 1 : Obtenir les identifiants Braze

#### Créer une clé API Braze

1. Dans Braze, accédez à __Paramètres__ en bas de la barre de navigation de gauche et cliquez sur __Console développeur__.
2. Dans l'onglet __Paramètres de l'API__ , sous __Clefs d'API Rest__, cliquez sur __+ Créer une nouvelle clé API__.
3. Nommez cette clé API et sélectionnez toutes les permissions __users.track__.  Ensuite, sélectionnez __Enregistrer la clé API__.
4. Enfin, copiez la clé API trouvée sous __Identificateur__ pour utiliser lors de la création de votre connexion HighTouch.

#### Trouvez votre point de terminaison de l'API Braze

Vous devrez localiser votre point de terminaison de l'API REST de Braze. Vous en aurez besoin lors de la création de votre destination Hightouch avec Braze. Votre point de terminaison dépendra de l'URL de Braze pour votre instance; vous pouvez trouver une liste complète de tous les points de terminaison de Braze [ici][2].

La touche haute ne nécessite que tout après "https://rest". Pour spécifier votre terminal. Par exemple, si votre point de terminaison Braze est https://rest.iad-01.braze.com, vous aurez seulement besoin de `iad-01.braze.com`.

### Étape 2 : Créez votre destination de Braze en mode Hightouch

1. Dans la section __Destinations__ de Hightouch, cliquez sur __Ajouter une destination__.
2. Sélectionnez __Braze__ dans la liste des destinations listées.
3. Fournir le point de terminaison de Braze (à l'exception de "https://rest.") et votre clé API.<br><br>!\[add_destination\]\[3\]

## Objets pris en charge et modes de synchronisation

Hightouch prend en charge la synchronisation avec les objets utilisateur et les événements.

| Destination | Libellé                                                                                                                        | Modes pris en charge                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| Objet       | Synchronise les enregistrements vers des objets tels que les utilisateurs ou les organisations de votre destination.           | Mise à jour ou mise à jour                  |
| Évènements  | Synchronise les enregistrements en tant qu'événements vers votre destination; c'est souvent sous la forme d'un appel de piste. | Suivre l'achat d'un événement ou d'un suivi |

## Cas d'utilisation

* Synchronisez les données des utilisateurs et des comptes dans Braze pour créer des campagnes hyper-personnalisées.
* Mettre à jour automatiquement vos segments Braze avec de nouvelles données depuis votre entrepôt.
* Offrez de meilleures expériences en apportant des données provenant d'autres points de contact clients au Brésil.

## Informations complémentaires

Pour plus d’informations sur l’intégration de Braze et Hightouch concernant le mapping des champs et la synchronisation des utilisateurs et des événements, visitez la [documentation Hightouch](https://hightouch.io/docs/destinations/braze/).
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
