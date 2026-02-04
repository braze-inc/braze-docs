---
nav_title: Bonnes pratiques
article_title: "Meilleures pratiques en matière d'ingestion de données dans le cloud"
toc_headers: h2
page_order: 0
page_type: reference
description: "Cette page fournit un aperçu de l'ingestion de données dans le nuage, des meilleures pratiques et des limites du produit."

---

# Bonnes pratiques

> L'ingestion de données dans le cloud de Braze vous permet d'établir une connexion directe entre votre entrepôt de données ou votre système de stockage de fichiers et Braze, afin de synchroniser les données pertinentes relatives aux utilisateurs ou aux catalogues. Lorsque vous synchronisez ces données avec Braze, vous pouvez les exploiter pour des cas d'utilisation tels que la personnalisation, le déclencheur ou la segmentation. 

## Comprendre la colonne `UPDATED_AT` 

{% alert note %}
`UPDATED_AT` ne concerne que les intégrations d'entrepôts de données, et non les synchronisations S3.
{% endalert %}

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. Chaque fois que la synchronisation est exécutée, Braze reflète les données mises à jour.

{% alert important %}
Braze CDI synchronisera les lignes en se basant strictement sur la valeur `UPDATED_AT`, que le contenu de la ligne soit ou non identique à celui qui se trouve actuellement dans Braze. Dans ces conditions, nous vous recommandons d'utiliser correctement le site `UPDATED_AT` pour synchroniser uniquement les données nouvelles ou mises à jour afin d'éviter l'utilisation inutile de points de données.
{% endalert %}

### Exemple : Synchronisation récurrente

Pour illustrer l'utilisation de `UPDATED_AT` dans une synchronisation CDI, prenez cet exemple de synchronisation récurrente pour la mise à jour des attributs d'un utilisateur :

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

Vous pouvez mettre à jour les données de l'utilisateur par ID externe, alias d'utilisateur, ID Braze, e-mail ou numéro de téléphone. Vous pouvez supprimer des utilisateurs par ID externe, alias d'utilisateur ou ID Braze. 

## Qu’est-ce qui est synchronisé

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Braze sélectionne et importe toutes les lignes pour lesquelles `UPDATED_AT` est égal ou postérieur au dernier horodatage `UPDATED_AT` du dernier travail de synchronisation réussi.

Dans votre entrepôt de données, ajoutez les utilisateurs et les attributs suivants à votre table, en définissant l'heure `UPDATED_AT` sur le moment où vous ajoutez ces données :

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_1",<br>        "attribute_b":"example_value_1"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lors de la prochaine synchronisation planifiée, Braze synchronise toutes les lignes dont l'horodatage `UPDATED_AT` est égal ou postérieur à l'horodatage le plus récent dans les profils utilisateurs. Braze met à jour ou ajoute des champs, de sorte que vous ne devez pas synchroniser le profil utilisateur complet à chaque fois. Après la synchronisation, les profils utilisateurs reflètent les nouvelles mises à jour :

**Synchronisation récurrente, deuxième passage le 20 juillet 2022 à 12h**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":false,<br>    "attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Une ligne a été ajoutée, mais la valeur `UPDATED_AT` est antérieure à `2022-07-19 09:07:23` (stockée depuis la première exécution). Par conséquent, aucune de ces lignes ne sera synchronisée lors de cette exécution. Le dernier `UPDATED_AT` pour la synchronisation n'a pas été modifié par cette exécution et reste `2022-07-19 09:07:23`.

**Synchronisation récurrente, troisième passage le 21 juillet 2022 à 12 heures**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_1",<br>        "attribute_b":"example_value_1"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>    "attribute_1":"xyz",<br>    "attribute_4":false,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-21 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3”:”2019-07-20T19:20:30+1:00"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lors de ce troisième passage, une nouvelle ligne a été ajoutée. Maintenant, une ligne a une valeur `UPDATED_AT` postérieure à `2022-07-19 09:07:23`, ce qui signifie qu'une seule ligne sera synchronisée. Le dernier `UPDATED_AT` est désormais défini comme `2022-07-21 08:30:00`.

{% alert note %}
`UPDATED_AT` peuvent même être postérieures à l'heure de début de l'exécution pour une synchronisation donnée. Toutefois, cette méthode n'est pas recommandée car elle repousse le dernier horodatage de `UPDATED_AT` "dans le futur" et les synchronisations suivantes ne synchroniseront pas les valeurs antérieures.
{% endalert %}

## Utilisez un horodatage UTC pour la colonne `UPDATED_AT`

La colonne `UPDATED_AT` devrait être en UTC pour éviter les problèmes liés aux heures d’été. Utilisez de préférence des fonctions uniquement en UTC, telles que `SYSDATE()` plutôt que `CURRENT_DATE()` dès que possible.

## Assurez-vous que l'heure de `UPDATED_AT` n'est pas la même que celle de votre synchronisation.

Votre synchronisation CDI peut contenir des données en double si l'un des champs `UPDATED_AT` est exactement à la même heure que le dernier horodatage `UPDATED_AT` de la précédente synchronisation réussie. En effet, CDI choisira une "limite inclusive" lorsqu'il identifiera une ligne qui se situe à la même heure que la synchronisation précédente, et fera en sorte que les lignes puissent se synchroniser. CDI ré-ingère ces lignes et crée des données en double.

Voici quelques suggestions pour éviter les données en double :

- Si vous mettez en place une synchronisation avec `VIEW`, n'utilisez pas `CURRENT_TIMESTAMP` comme valeur par défaut. Ceci entraînera la synchronisation de toutes les données chaque fois qu’elle s’effectue, car le champ `UPDATED_AT` sera évalué à chaque fois que nos requêtes sont lancées.
- Si vous avez des flux de données à très longue durée d’exécution ou des requêtes écrivant des données dans votre table source, évitez de les exécuter en même temps que la synchronisation ou évitez d’utiliser le même horodatage pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les rangées qui ont le même horodatage.

### Exemple : Gérer les mises à jour ultérieures

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

## Conseils supplémentaires

### N’écrivez que les attributs nouveaux ou mis à jour pour limiter l’utilisation

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Braze sélectionne et importe toutes les lignes pour lesquelles `UPDATED_AT` est égal ou postérieur au dernier horodatage `UPDATED_AT` du dernier travail de synchronisation réussi, qu'elles soient ou non identiques à ce qui figure actuellement sur le profil utilisateur. Voilà pourquoi nous recommandons de ne synchroniser que les attributs que vous voulez ajouter ou mettre à jour.

L'utilisation des points de données est identique avec CDI qu'avec d'autres méthodes d'ingestion comme les API REST ou les SDK, il vous appartient donc de vous assurer que vous n'ajoutez que des attributs nouveaux ou mis à jour dans vos tables sources.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Notez la nécessité de [capturer les dates]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) dans les attributs imbriqués. 

{% tabs local %}
{% tab Nested Custom Attributes %}
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
{% tab Event %}
Pour synchroniser des événements, un nom d'événement est nécessaire. Formatez le champ `time` en chaîne de caractères ISO 8601 ou en format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, Braze utilise la valeur de la colonne `UPDATED_AT` comme heure de l'événement. Les autres champs, y compris `app_id` et `properties`, sont facultatifs. 

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
{% tab Purchase %}
Pour synchroniser les événements d'achat, `product_id`, `currency`, et `price` sont nécessaires. Formatez le champ `time`, qui est facultatif, en tant que chaîne de caractères ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, Braze utilise la valeur de la colonne `UPDATED_AT` comme heure de l'événement. Les autres champs, y compris `app_id`, `quantity` et `properties`, sont facultatifs.

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
{% tab Subscription Groups %}
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
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Braze arrête toute synchronisation avec plus de 500 millions de nouvelles lignes. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire satisfaction client Braze ou l'assistance Braze. |
| Attributs par rangée     | Chaque ligne doit contenir un seul ID d'utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau d'objets compte pour un attribut). |
| Taille de la charge utile           | Chaque ligne peut contenir une charge utile allant jusqu'à 1 Mo. Braze rejette les charges utiles supérieures à 1 Mo et enregistre l'erreur "Payload was greater than 1MB" dans le journal de synchronisation avec l'ID externe associé et la charge utile tronquée. |
| Type de données              | Vous pouvez synchroniser les attributs utilisateurs via l’ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connectera à votre entrepôt de données ou à votre environnement Cloud dans n'importe quelle région ou chez n’importe quel fournisseur Cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
