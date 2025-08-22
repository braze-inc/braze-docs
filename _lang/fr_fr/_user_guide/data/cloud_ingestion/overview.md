---
nav_title: Aperçu
article_title: "Vue d'ensemble de l'ingestion de données en nuage (Cloud Data Ingestion)" 
page_order: 0
page_type: reference
description: "Cette page fournit un aperçu de l'ingestion de données dans le nuage, des meilleures pratiques et des limites du produit."

---

# Aperçu de l’ingestion de données cloud (CDI) dans Braze

> L'ingestion de données dans le cloud de Braze vous permet d'établir une connexion directe entre votre entrepôt de données ou votre système de stockage de fichiers et Braze, afin de synchroniser les données pertinentes relatives aux utilisateurs ou aux catalogues. Une fois synchronisées avec Braze, ces données peuvent être exploitées pour des cas d'utilisation tels que la personnalisation, le déclenchement ou la segmentation. 

## Fonctionnement

Avec Braze Cloud Data Ingestion (CDI), vous configurez une intégration entre votre instance d'entrepôt de données et l'espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation se fait selon la planification que vous déterminez et chaque intégration peut disposer d’une planification différente. Les synchronisations peuvent avoir lieu d’une fois toutes les 15 minutes à une fois par mois. Si vous avez besoin que les synchronisations se produisent à une fréquence supérieure à 15 minutes, contactez votre gestionnaire de satisfaction client ou envisagez d'utiliser les appels API REST pour l'ingestion de données en temps réel.

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. Chaque fois que la synchronisation s'exécute, toute donnée mise à jour est reflétée dans Braze.

## Sources de données prises en charge

L'ingestion de données dans le nuage peut synchroniser les données des sources suivantes avec Braze :

- Sources de l'entrepôt de données 
   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake

- Sources de stockage de fichiers 
   - Amazon S3

## Types de données prises en charge 

L'ingestion de données dans le nuage prend en charge les types de données suivants : 
- Attributs de l'utilisateur, y compris :
   - Attributs personnalisés imbriqués
   - Tableaux d’objets
   - État des abonnements
- Événements personnalisés
- Événements d’achat
- Articles de catalogue
- Demandes de suppression d'un utilisateur

Les données de l'utilisateur peuvent être mises à jour par ID externe, alias d'utilisateur, ID Braze, e-mail ou numéro de téléphone. Les utilisateurs peuvent être supprimés par ID externe, alias d'utilisateur ou ID Braze. 

## Qu’est-ce qui est synchronisé

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Chaque ligne dans laquelle `UPDATED_AT` est plus ancien que la dernière synchronisation, la ligne sera sélectionnée et transmise à Braze.

Dans votre entrepôt de données, ajoutez les utilisateurs et les attributs suivants à votre table, en définissant l'heure `UPDATED_AT` sur le moment où vous ajoutez ces données :

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "attribut_1" : "abcdefg",<br>    "attribute_2": {<br>        "attribut_a" : "valeur_exemple_2",<br>        "attribut_b" : "valeur_exemple_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "attribut_1" : "abcdefg",<br>    "attribut_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5" : "testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribut_1" : "abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |

Pendant la prochaine synchronisation planifiée, toutes les lignes possédant un horodatage `UPDATED_AT` plus ancien que l’horodatage le plus récent seront synchronisées aux profils utilisateurs de Braze. Les champs seront mis à jour ou ajoutés et vous n’aurez donc pas besoin de synchroniser le profil utilisateur tout entier à chaque fois. Après la synchronisation, les utilisateurs afficheront les nouvelles mises à jour :

```json
{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":{
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_2"
    },
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Cas d’utilisation : Première synchronisation et mises à jour ultérieures

Cet exemple montre le processus général de synchronisation des données pour la première fois, puis la mise à jour des seules données changeantes (deltas) dans les mises à jour ultérieures. Supposons que nous ayons une table `EXAMPLE_DATA` contenant des données utilisateur. Le jour 1, il présente les valeurs suivantes :

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>rouge</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>rouge</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Pour obtenir ces données dans le format attendu par CDI, vous pouvez exécuter la requête suivante :

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Rien de tout cela n'ayant été synchronisé avec Braze auparavant, ajoutez tout cela à la table source pour CDI :

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Une synchronisation s'exécute et Braze enregistre que vous avez synchronisé toutes les données disponibles jusqu'à "2023-03-16 15:00:00". Ensuite, le matin du deuxième jour, vous avez un processus ETL qui s’exécute et certains champs de votre table d'utilisateurs sont mis à jour (en surbrillance) :

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">rouge</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">vert</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>rouge</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Vous devez maintenant ajouter uniquement les valeurs modifiées dans le tableau source CDI. Ces lignes peuvent être ajoutées plutôt que de mettre à jour les anciennes lignes. Ce tableau se présente désormais comme suit :

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 12345       | { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} |
| 2023-03-17 09:30:00 | 23456       | { "ATTRIBUTE_1": "15"} |
| 2023-03-17 09:30:00 | 34567       | { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 45678       | { "ATTRIBUTE_2":"green"} |
| 2023-03-17 09:30:00 | 56789       | { "ATTRIBUTE_3":"693"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

CDI ne synchronisera que les nouvelles lignes, de sorte que la prochaine synchronisation ne portera que sur les cinq dernières lignes.

### Cas d’utilisation : Mettre à jour un champ dans un tableau d'objets existant

Cet exemple montre comment mettre à jour un champ dans un tableau d'objets existant. Supposons que nous ayons un tableau source avec la définition suivante :

```json 
Create table BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list (
    pet_id int IDENTITY(1,1), 
    breed VARCHAR, 
    type VARCHAR, 
    name VARCHAR, 
    owner_id VARCHAR, 
    age int
);
```

Dans cet exemple, nous voulons ajouter un tableau des animaux de compagnie appartenant à chaque utilisateur, ce qui correspond à `owner_id`. Plus précisément, nous voulons inclure l'identification, la race, le type et le nom. Nous pouvons utiliser la requête suivante pour remplir une table ou une vue :

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$add', ARRAY_AGG( OBJECT_CONSTRUCT(
                'id',
                pet_id,
                'breed',
                breed,
                'type',
                type,
                'name',
                name
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID;
```

Le résultat attendu serait le suivant :

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

Ensuite, pour envoyer un champ de nom mis à jour et un nouveau champ d'âge pour chaque propriétaire, nous pouvons utiliser la requête suivante pour remplir une table ou une vue :

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$update', ARRAY_AGG( OBJECT_CONSTRUCT(
                '$identifier_key','id',
                '$identifier_value',pet_id,
                '$new_object',OBJECT_CONSTRUCT(
                    'name',name,
                    'age',age
                )
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID; 
```

Le résultat attendu serait le suivant :

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## Utilisation de points de données

La facturation des points de données pour Cloud Data Ingestion équivaut à la facturation des mises à jour via l’[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Pour plus d'informations, reportez-vous à la section [Points de données]({{site.baseurl}}/user_guide/data/data_points/). 

{% alert important %}
Braze Cloud Data Ingestion compte dans la limite de débit disponible, donc si vous envoyez des données par une autre méthode, la limite de débit est combinée entre l'API Braze et Cloud Data Ingestion.
{% endalert %}

## Recommandations pour la configuration des données

### N’écrivez que les attributs nouveaux ou mis à jour pour limiter l’utilisation

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Toutes les lignes pour lesquelles `UPDATED_AT` est postérieur à la dernière ligne synchronisée seront sélectionnées et transférées dans Braze, qu'elles soient ou non identiques à celles figurant actuellement dans le profil utilisateur. Voilà pourquoi nous recommandons de ne synchroniser que les attributs que vous voulez ajouter ou mettre à jour.

La consommation de points de données est identique en utilisant CDI que pour d'autres méthodes d'ingestion comme les API REST ou les SDK, c'est donc à vous de vous assurer que vous n'ajoutez que des attributs nouveaux ou mis à jour dans vos tables sources.

### Utilisez un horodatage UTC pour la colonne `UPDATED_AT`

La colonne `UPDATED_AT` devrait être en UTC pour éviter les problèmes liés aux heures d’été. Utilisez de préférence des fonctions uniquement en UTC, telles que `SYSDATE()` plutôt que `CURRENT_DATE()` dès que possible.

### Assurez-vous que l'heure de `UPDATED_AT` n'est pas la même que celle de votre synchronisation.

Votre synchronisation CDI peut contenir des données en double si l'un des champs `UPDATED_AT` se trouve exactement à la même heure que votre synchronisation précédente. En effet, CDI choisira une "limite inclusive" lorsqu'il identifiera une ligne qui se situe à la même heure que la synchronisation précédente, et fera en sorte que les lignes puissent se synchroniser. CDI ré-ingère ces lignes et crée des données en double.

### Séparer la colonne `EXTERNAL_ID` de la colonne `PAYLOAD` 

L'objet `PAYLOAD` ne doit pas comporter d'ID externe ou d'autre type d'ID. 

### Supprimer un attribut

Vous pouvez lui attribuer la valeur `null` si vous souhaitez omettre un attribut dans le profil d'un utilisateur. Si vous désirez qu’un attribut reste inchangé, ne l’envoyez pas à Braze jusqu’à ce qu’il ait été mis à jour. Pour supprimer complètement un attribut, utilisez `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Effectuer des mises à jour incrémentielles

Effectuez des mises à jour incrémentielles de vos données afin d'éviter les écrasements involontaires lors de mises à jour simultanées.

Dans l'exemple suivant, un utilisateur possède deux attributs :
- Couleur : "Vert"
- Taille : "Grand"

Braze reçoit alors simultanément les deux mises à jour suivantes pour cet utilisateur :
- Demande 1 : Changer la couleur en "Rouge"
- Demande 2 : Modifier la taille en "Moyen"

Comme la demande 1 survient en premier, les attributs de l'utilisateur sont mis à jour comme suit :
- Couleur : "Rouge"
- Taille : "Grand"

Cependant, lorsque la demande 2 se produit, Braze commence par les valeurs d'attribut originales ("Vert" et "Grand"), puis met à jour les attributs de l'utilisateur de la manière suivante :
- Couleur : "Vert"
- Taille : "Moyen"

Lorsque les demandes sont terminées, la demande 2 écrase la mise à jour de la demande 1\. Il est donc préférable d'échelonner vos mises à jour afin d'éviter que les demandes ne soient écrasées.

### Créer une chaîne de caractères JSON à partir d'une autre table

Si vous préférez stocker de manière interne chaque attribut dans sa propre colonne, vous devez convertir ces colonnes en chaîne de caractères JSON pour remplir la synchronisation avec Braze. Pour ce faire, vous pouvez utiliser une requête du type :

{% tabs local %}
{% tab Snowflake %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Utilisez l'horodatage `UPDATED_AT` 

Nous utilisons l’horodatage `UPDATED_AT` pour suivre quelles données ont été synchronisées avec succès dans Braze. Si de nombreuses rangées sont écrites avec le même horodatage pendant qu’une synchronisation est en cours, ceci peut entraîner la synchronisation de données en double dans Braze. Voici quelques conseils pour éviter des données en double :
- Si vous mettez en place une synchronisation avec `VIEW`, n'utilisez pas `CURRENT_TIMESTAMP` comme valeur par défaut. Ceci entraînera la synchronisation de toutes les données chaque fois qu’elle s’effectue, car le champ `UPDATED_AT` sera évalué à chaque fois que nos requêtes sont lancées. 
- Si vous avez des flux de données à très longue durée d’exécution ou des requêtes écrivant des données dans votre table source, évitez de les exécuter en même temps que la synchronisation ou évitez d’utiliser le même horodatage pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les rangées qui ont le même horodatage.

### Configuration de la table

Nous disposons d'un [référentiel GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) public permettant aux clients de partager des bonnes pratiques ou des extraits de code. Pour contribuer avec vos propres extraits de code, créez une requête d’extraction !

### Formatage des données

Toutes les opérations possibles via l'endpoint de Braze `/users/track` sont prises en charge par l'ingestion de données dans le nuage, notamment la mise à jour des attributs personnalisés imbriqués, l'ajout d'un statut d'abonnement et la synchronisation d'événements personnalisés ou d'achats. 

Les champs de la charge utile doivent respecter le même format que l'endpoint `/users/track` correspondant. Pour plus d'informations sur les exigences en matière de formatage, reportez-vous à ce qui suit :

| Type de données | Spécifications de formatage |
| --------- | ---------| --------- | ----------- |
| `attributes` | Voir [objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Voir l'[objet "événements"]({{site.baseurl}}/api/objects_filters/event_object/). |
| `purchases` | Voir [Objet Achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |

Notez la nécessité de [capturer les dates]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) dans les attributs imbriqués. 

{% tabs local %}
{% tab Attributs personnalisés imbriqués %}
Vous pouvez inclure des attributs personnalisés imbriqués dans la colonne payload pour une synchronisation d'attributs personnalisés. 

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Événement %}
Pour synchroniser des événements, un nom d'événement est nécessaire. Le champ `time` doit être formaté comme une chaîne de caractères ISO 8601 ou dans le format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, la valeur de la colonne `UPDATED_AT` est utilisée comme heure de l'événement. Les autres champs, y compris `app_id` et `properties`, sont facultatifs. 

Notez que vous ne pouvez synchroniser qu'un seul événement par ligne.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab Achat %}
Pour synchroniser les événements d'achat, `product_id`, `currency`, et `price` sont nécessaires. Le champ `time`, qui est facultatif, doit être formaté comme une chaîne de caractères ISO 8601 ou dans le format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, la valeur de la colonne `UPDATED_AT` est utilisée comme heure de l'événement. Les autres champs, y compris `app_id`, `quantity` et `properties`, sont facultatifs.

Notez que vous ne pouvez synchroniser qu'un seul événement d'achat par ligne.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
    }
}
```

{% endtab %}
{% tab Groupes d’abonnement %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### Éviter les délais d'attente pour les requêtes de l'entrepôt de données

Nous vous recommandons d'effectuer les requêtes dans un délai d'une heure afin d'optimiser les performances et d'éviter les erreurs potentielles. Si les requêtes dépassent ce délai, envisagez de revoir la configuration de votre entrepôt de données. L'optimisation des ressources allouées à votre entrepôt peut contribuer à améliorer la vitesse d'exécution des requêtes.

## Limites du produit

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d’intégrations | Le nombre d’intégrations que vous pouvez définir n’est pas limité. Cependant, vous ne pourrez définir qu’une seule intégration par table ou par affichage.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Toute synchronisation comportant plus de 500 millions de nouvelles lignes sera interrompue. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire satisfaction client Braze ou l'assistance Braze. |
| Attributs par rangée     | Chaque ligne doit contenir un seul ID d'utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau d'objets compte pour un attribut). |
| Taille de la charge utile           | Chaque ligne peut contenir une charge utile allant jusqu'à 1 Mo. Les données utiles supérieures à 1 Mo seront rejetées et l'erreur "Payload was greater than 1MB" sera consignée dans le journal de synchronisation avec l'ID externe associé et les données utiles tronquées. |
| Type de données              | Vous pouvez synchroniser les attributs utilisateurs via l’ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connectera à votre entrepôt de données ou à votre environnement Cloud dans n'importe quelle région ou chez n’importe quel fournisseur Cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
