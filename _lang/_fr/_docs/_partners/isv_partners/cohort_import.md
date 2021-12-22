---
nav_title: Intégration de l'importation de cohortes
alias: /fr/cohort_import/
hidden: vrai
---

# Intégration de l'importation de cohortes de partenaires

> La fonctionnalité d’intégration Cohort Import permet à nos partenaires de s’intégrer à Braze pour envoyer des cohortes d’utilisateurs générées au sein de l’application partenaire.

## URL de la grappe

Braze héberge notre application sur plusieurs grappes à travers les États-Unis et l'UE. L'URL des terminaux d'importation sera différente en fonction du cluster où l'instance de l'entreprise du client est hébergée sur :

| INSTANCE | Point d'arrivée REST            |
| -------- | ------------------------------- |
| US-01    | `https://rest.iad-01.braze.com` |
| US-02    | `https://rest.iad-02.braze.com` |
| US-03    | `https://rest.iad-03.braze.com` |
| US-04    | `https://rest.iad-04.braze.com` |
| US-05    | `https://rest.iad-05.braze.com` |
| US-06    | `https://rest.iad-06.braze.com` |
| US-08    | `https://rest.iad-08.braze.com` |
| EU-01    | `https://rest.fra-01.braze.eu`  |
| EU-02    | `https://rest.fra-02.braze.eu`  |
{: .reset-td-br-1 .reset-td-br-2}

## URL du point de terminaison

En plus des URL de haut niveau étant spécifiques au cluster, chaque point de terminaison est également un partenaire. Par exemple, lors de l'importation dans notre grappe de serveurs US01, l'URL aurait le format `https://rest.iad-01.braze. om/partners/[partner_name]/…`, où `[partner_name]` est généralement le nom de l'entreprise du partenaire. Les spécifications pour chaque point de terminaison sont indiquées ci-dessous.

## Authentification

pour importer des données de cohorte dans le braze, il y a deux clés d'authentification nécessaires.

### Clé API partenaire

La clé API partenaire identifie le partenaire d'intégration et authentifie la requête comme étant valide pour l'importation. La clé doit être incluse dans le corps de la requête dans le champ `partner_api_key`.

Lors de la configuration de l’intégration dans l’application du partenaire, le client doit être invité à spécifier son cluster Braze afin que l'intégration sache quelle URL de cluster et quelle clé d'API de partenaire utiliser lors de l'importation de données.

Braze fournira la (les) clé(s) API partenaire au(x) partenaire(s) avant que le partenaire commence le développement de l'intégration. En général, nous fournirons une clé unique valable pour tous les clusters américains, et une autre clé valable pour notre grappe européenne.

### Clé d'importation des données du client

La clé d'importation de données du client identifie le groupe d'application client dans lequel la cohorte doit être importée. La clé doit être incluse dans le corps de la requête dans le champ `client_secret`.

Cette clé est générée dans le tableau de bord du client dans les paramètres d’intégration du partenaire. Lors de la configuration de l’intégration dans l’application du partenaire, le client doit être invité à spécifier sa clé d'importation de données afin que l'intégration sache à quel client et groupe d'applications envoyer des données.

## Spécifications de terminaison de l'API

### Point de terminaison du nom de la cohorte
Le point de terminaison du nom de la cohorte peut être utilisé pour spécifier le nom d'une cohorte en fonction de son ID. Ce point de terminaison doit être appelé chaque fois qu'une cohorte est initialement exportée vers le Brésil, ou lorsque le nom d'une cohorte déjà connue de Braze est changé.

| Champ                       | Type de texte        | Requis | Notes                                                                                                                                                                                                                                      |
| --------------------------- | -------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `format@@0 partner_api_key` | chaîne de caractères | Oui    | Clé d'API spécifique à un partenariat, utilisée dans toutes les requêtes du partenaire au Brésil. Cette clé sera spécifique au cluster (voir ci-dessus), donc le partenaire devra connaître le cluster auquel les cohortes seront écrites. |
| `secret du client`          | chaîne de caractères | Oui    | Clé d'importation de données pour le client auquel appartient la cohorte.                                                                                                                                                                  |
| `cohort_id`                 | chaîne de caractères | Oui    | Identifiant de la cohorte. Cet identifiant doit être unique pour le client spécifié.                                                                                                                                                       |
| `Nom`                       | chaîne de caractères | Oui    | Nom spécifié par le client pour la cohorte                                                                                                                                                                                                 |
| `créé à`                    | chaîne de caractères | Oui    | Horodatage au format ISO-8601                                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Exemple de demande :

`POST: https://rest.iad-01.braze.com/partners/[partner_name]/cohorts`
```
{
    “partner_api_key” : “123456-1234-1234-12345678”,
    “client_secret” : “234567-2345-2345-23456789”,
    “cohort_id” : “[un identifiant unique généré par le partenaire]”,
    “name” : “Nom de la cohorte qui apparaîtra dans le tableau de bord de Braze”,
    « created_at » : « 2021-01-21T19:20:30+05:00»
}
```

### Point de terminaison de cohorte de l'utilisateur

Le point de terminaison de la cohorte utilisateur permet de spécifier quels utilisateurs ont été ajoutés ou retirés d'une cohorte particulière. Ce point de terminaison doit être appelé quand une cohorte est rafraîchie. Seuls les utilisateurs qui viennent d'entrer dans la cohorte ou qui ont quitté la cohorte depuis le dernier rafraîchissement doivent être envoyés au Brésil.

| Champ                       | Type de texte        | Requis | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------- | -------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `format@@0 partner_api_key` | chaîne de caractères | Oui    | Clé d'API spécifique à un partenariat, utilisée dans toutes les requêtes du partenaire au Brésil. Cette clé sera spécifique au cluster (voir ci-dessus), donc l'intégration devra connaître le cluster auquel les cohortes seront écrites.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `secret du client`          | chaîne de caractères | Oui    | Clé d'importation de données pour le client auquel appartient la cohorte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `cohort_id`                 | chaîne de caractères | Oui    | Identifiant de la cohorte. L'identifiant doit être unique pour le client spécifié.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `cohort_changes`            | tableau d'objets     | Oui    | Les objets peuvent avoir deux champs. L’un, « user_ids », est requis et est un tableau de chaînes. Chaque élément est un ID pour un utilisateur dont le statut dans la cohorte a changé. Le second champ, « should_remove », est un booléen facultatif indiquant si les utilisateurs de cet objet doivent être retirés de la cohorte au lieu d'être ajoutés. La valeur par défaut est faux. Dans un premier temps, nous ignorerons tous les identifiants qui ne correspondent pas à l'ID d'utilisateur externe, ce qui signifie que les utilisateurs anonymes ne peuvent pas être ajoutés ou supprimés d'une cohorte. La longueur maximale combinée des identifiants de l'utilisateur dans une seule requête est de 1000. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Exemple de demande :

`POST: https://rest.iad-01.braze.com/partners/[partner_name]/cohorts/users`
```
{
    “partner_api_key” : “123456-1234-1234-12345678”,
    “client_secret” : “234567-2345-2345-23456789”,
    “cohort_id” : “[un identifiant unique généré par le partenaire]”,
    "cohort_changes" : "[
       {"user_ids": ["test_user_1", "test_user_2"]}
    ]"
}
```

## Limitation de taux

À part le maximum de 1000 identifiants utilisateur par requête dans le point d'extrémité de la cohorte d'utilisateur, ces terminaux ne sont pas spécifiquement limités au débit.

## Filtre de cohorte

Braze ajoutera un filtre qui permet à un utilisateur du tableau de bord d'inclure ou d'exclure des utilisateurs d'un public ciblé s'ils font partie d'une cohorte partenaire. Le filtre fournira une liste déroulante des noms de toutes les cohortes connues de Braze pour ce client. Ce filtre ne sera visible qu'aux clients avec lesquels le partenaire et Braze ont accepté de s'associer à cette intégration.

## Dépannage

Reportez-vous au tableau suivant pour les codes d'erreurs spécifiques aux terminaux d'importation de Cohort, et comment les résoudre.

| Code d'erreur | Libellé                                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `401`         | Clé API partenaire invalide                                                                                                                 |
|               | Secret client invalide                                                                                                                      |
|               | Partenaire non activé pour le client avec le client secret : **<client secret>**                                                            |
| `400`         | `cohort_id` doit être une chaîne de caractères valide                                                                                       |
|               | `cohort_changes` doit ętre une table d'objets avec la clé `user_ids` et/ou `device_ids` mappage ŕ une table de chaînes, ou un objet `alias` |
|               | Seuls 1 000 `user_ids`, `device_ids`et `alias` sont autorisés par requête                                                                   |
|               | `name` doit être une chaîne de caractères non vide                                                                                          |
|               | `created_at` doit ętre un instant valide comme une chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)                                |
{: .reset-td-br-1 .reset-td-br-2}

Pour un dépannage supplémentaire, reportez-vous à [Erreurs & Réponses]({{site.baseurl}}/api/errors/), qui couvre les différentes erreurs et les réponses du serveur qui peuvent apparaître en utilisant l'API Braze.
