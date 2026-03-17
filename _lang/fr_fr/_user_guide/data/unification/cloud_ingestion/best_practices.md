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

## Comprendre la`UPDATED_AT`colonne

{% alert note %}
`UPDATED_AT` Ceci est pertinent uniquement pour les intégrations d'entrepôts de données, et non pour les synchronisations S3.
{% endalert %}

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. À chaque exécution de la synchronisation, Braze reflète toutes les données mises à jour.

{% alert important %}
Braze CDI synchronisera les lignes strictement en fonction de la`UPDATED_AT`valeur, que le contenu de la ligne soit identique ou non à celui actuellement présent dans Braze. Compte tenu de cela, nous recommandons d'utiliser`UPDATED_AT`correctement afin de ne synchroniser que les données nouvelles ou mises à jour, et ainsi éviter toute utilisation inutile de points de donnée.
{% endalert %}

### Exemple : Synchronisation récurrente

Pour illustrer l'utilisation`UPDATED_AT`de  dans une synchronisation CDI, veuillez considérer cet exemple de synchronisation récurrente pour la mise à jour des attributs utilisateur :

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

Vous pouvez mettre à jour les données utilisateur à l'aide de l'ID externe, de l'alias d'utilisateur, de l'identifiant Braze, de l'e-mail ou du numéro de téléphone. Vous pouvez supprimer des utilisateurs par ID externe, alias d'utilisateur ou identifiant Braze. 

## Qu’est-ce qui est synchronisé

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Braze sélectionne et importe toutes les lignes dont`UPDATED_AT`la date est égale ou postérieure à la dernière`UPDATED_AT`date de la dernière synchronisation réussie.

Dans votre entrepôt de données, ajoutez les utilisateurs et les attributs suivants à votre table, en définissant l'heure `UPDATED_AT` sur le moment où vous ajoutez ces données :

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Lors de la prochaine synchronisation de planification, Braze synchronise toutes les lignes dont `UPDATED_AT`l'horodatage est égal ou postérieur à l'horodatage le plus récent avec les profils utilisateurs. Braze met à jour ou ajoute des champs, vous n'avez donc pas besoin de synchroniser l'intégralité du profil utilisateur à chaque fois. Après la synchronisation, les profils utilisateurs reflètent les nouvelles mises à jour :

**Synchronisation récurrente, deuxième exécution le 20 juillet 2022 à 12 h.**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Une ligne a été ajoutée, mais la`UPDATED_AT`valeur est antérieure à`2022-07-19 09:07:23`(enregistrée lors de la première exécution). Par conséquent, aucune de ces lignes ne sera synchronisée lors de cette exécution. La dernière valeur`UPDATED_AT` pour la synchronisation n'est pas modifiée par cette exécution et reste inchangée`2022-07-19 09:07:23`.

**Synchronisation récurrente, troisième exécution le 21 juillet 2022 à 12 h.**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Dans cette troisième série, une nouvelle ligne a été ajoutée. À présent, une ligne présente une`UPDATED_AT`valeur postérieure à `2022-07-19 09:07:23`, ce qui signifie qu'une seule ligne sera synchronisée. Le dernier`UPDATED_AT`est désormais défini comme `2022-07-21 08:30:00`suit.

{% alert note %}
`UPDATED_AT` Les valeurs peuvent être encore plus tardives que l'heure de début d'exécution pour une synchronisation donnée. Cependant, cette pratique n'est pas recommandée car elle repousse le dernier`UPDATED_AT`horodatage « dans le futur » et les synchronisations suivantes ne synchroniseront pas les valeurs antérieures.
{% endalert %}

## Utilisez un horodatage UTC pour la colonne `UPDATED_AT`

La colonne `UPDATED_AT` devrait être en UTC pour éviter les problèmes liés aux heures d’été. Utilisez de préférence des fonctions uniquement en UTC, telles que `SYSDATE()` plutôt que `CURRENT_DATE()` dès que possible.

## Veuillez vous assurer que`UPDATED_AT`l'heure ne correspond pas à celle de votre synchronisation.

Votre synchronisation CDI peut contenir des données en double si certains`UPDATED_AT`champs ont exactement la même date et heure que le dernier`UPDATED_AT`horodatage de la dernière tâche de synchronisation réussie. En effet, CDI choisira une "limite inclusive" lorsqu'il identifiera une ligne qui se situe à la même heure que la synchronisation précédente, et fera en sorte que les lignes puissent se synchroniser. CDI ré-ingère ces lignes et crée des données en double.

Voici quelques suggestions pour éviter les données doublées :

- Si vous configurez une synchronisation avec un `VIEW`, veuillez ne pas utiliser`CURRENT_TIMESTAMP`  comme valeur par défaut. Ceci entraînera la synchronisation de toutes les données chaque fois qu’elle s’effectue, car le champ `UPDATED_AT` sera évalué à chaque fois que nos requêtes sont lancées.
- Si vous avez des flux de données à très longue durée d’exécution ou des requêtes écrivant des données dans votre table source, évitez de les exécuter en même temps que la synchronisation ou évitez d’utiliser le même horodatage pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les rangées qui ont le même horodatage.

### Exemple : Gestion des mises à jour ultérieures

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

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

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

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI ne synchronisera que les nouvelles lignes, de sorte que la prochaine synchronisation ne portera que sur les cinq dernières lignes.

## Conseils supplémentaires

### N’écrivez que les attributs nouveaux ou mis à jour pour limiter l’utilisation

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Braze sélectionne et importe toutes les lignes dont`UPDATED_AT`la date est égale ou postérieure à la dernière`UPDATED_AT`date de la dernière synchronisation réussie, qu'elles soient identiques ou non à celles actuellement présentes dans le profil utilisateur. Voilà pourquoi nous recommandons de ne synchroniser que les attributs que vous voulez ajouter ou mettre à jour.

L'utilisation des points de données est identique avec CDI et avec d'autres méthodes d'ingestion de données telles que les API REST ou les SDK. Il est donc de votre responsabilité de vous assurer que vous n'ajoutez que des attributs nouveaux ou mis à jour dans vos tables sources.

### Séparer la colonne `EXTERNAL_ID` de la colonne `PAYLOAD` 

L'objet `PAYLOAD` ne doit pas comporter d'ID externe ou d'autre type d'ID. 

### Supprimer un attribut

Vous pouvez lui attribuer la valeur `null` si vous souhaitez omettre un attribut dans le profil d'un utilisateur. Si vous désirez qu’un attribut reste inchangé, ne l’envoyez pas à Braze jusqu’à ce qu’il ait été mis à jour. Pour supprimer complètement un attribut, utilisez `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Effectuer des mises à jour incrémentielles

Effectuez des mises à jour incrémentielles de vos données afin d'éviter les écrasements involontaires lors de mises à jour simultanées.

{% alert important %}
* **Mises à jour de différents attributs :** Dans la grande majorité des cas, si deux mises à jour n'affectent pas les mêmes attributs d'un utilisateur, elles ont des résultats totalement indépendants. Par exemple, si vous mettez à jour `Color`l'attribut d'un utilisateur et que vous mettez à jour séparément son`Size`attribut, les deux mises à jour devraient être appliquées correctement, même si elles ont lieu à quelques secondes d'intervalle.
* **Mises à jour du même attribut :** Des conditions de concurrence peuvent survenir lorsque plusieurs mises à jour effectuent le ciblage du même attribut au cours d'une même synchronisation. Dans ces cas exceptionnels, une mise à jour peut remplacer une autre. La meilleure façon d'éviter ce comportement est de vous assurer que les données source pour votre synchronisation CDI reflètent uniquement l'état le plus récent de chaque utilisateur, ou que toutes les mises à jour pour un utilisateur donné ou une paire utilisateur+attribut sont contenues dans une seule ligne.
* **Opérateurs de tableau d'objets :** Les seules exceptions aux mises à jour indépendantes concernent les opérateurs`$add` , `$remove``$update`, et  pour les tableaux d'objets, où les mises à jour d'un même tableau peuvent interagir entre elles.
* **Événements :** Les conditions de concurrence n'affectent pas les événements, car chaque événement est unique et associé à un horodatage.
{% endalert %}

La meilleure façon d'éviter ce comportement est de vous assurer que les données source pour votre synchronisation CDI reflètent uniquement l'état le plus récent de chaque utilisateur, ou que toutes les mises à jour pour un utilisateur donné ou une paire utilisateur+attribut sont contenues dans une seule ligne.

### Créer une chaîne de caractères JSON à partir d'une autre table

Si vous préférez stocker de manière interne chaque attribut dans sa propre colonne, vous devez convertir ces colonnes en chaîne de caractères JSON pour remplir la synchronisation avec Braze. Pour ce faire, vous pouvez utiliser une requête du type :

{% tabs local %}
{% tab Snowflake %}
```sql
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
```sql
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
```sql
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
```sql
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
```sql
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
Pour synchroniser des événements, un nom d'événement est nécessaire. Veuillez formater le`time`champ sous forme de chaîne de caractères ISO 8601 ou au`yyyy-MM-dd'T'HH:mm:ss:SSSZ`format. Si le`time`champ n'est pas présent, Braze utilise la valeur`UPDATED_AT` de la colonne comme heure de l'événement. Les autres champs, y compris `app_id` et `properties`, sont facultatifs. 

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
Pour synchroniser les événements d'achat, `product_id`, `currency`, et `price` sont nécessaires. Veuillez formater le`time`champ, qui est facultatif, sous forme de chaîne de caractères ISO 8601 ou au`yyyy-MM-dd'T'HH:mm:ss:SSSZ`format. Si le`time`champ n'est pas présent, Braze utilise la valeur`UPDATED_AT` de la colonne comme heure de l'événement. Les autres champs, y compris `app_id`, `quantity` et `properties`, sont facultatifs.

Notez que vous ne pouvez synchroniser qu'un seul événement d'achat par ligne.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
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

### Évitez les délais d'attente pour les requêtes d'entrepôt de données.

Nous vous recommandons d'effectuer les requêtes dans un délai d'une heure afin d'optimiser les performances et d'éviter les erreurs potentielles. Si les requêtes dépassent ce délai, envisagez de revoir la configuration de votre entrepôt de données. L'optimisation des ressources allouées à votre entrepôt peut contribuer à améliorer la vitesse d'exécution des requêtes.

## Limites du produit

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d’intégrations | Le nombre d’intégrations que vous pouvez définir n’est pas limité. Cependant, vous ne pourrez définir qu’une seule intégration par table ou par affichage.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Braze interrompt toute synchronisation comportant plus de 500 millions de nouvelles lignes. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire satisfaction client Braze ou l'assistance Braze. |
| Attributs par rangée     | Chaque ligne doit contenir un seul ID d'utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau d'objets compte pour un attribut). |
| Taille de la charge utile           | Chaque ligne peut contenir une charge utile allant jusqu'à 1 Mo. Braze rejette les charges utiles supérieures à 1 Mo et consigne l'erreur « La charge utile était supérieure à 1 Mo » dans le journal de synchronisation, avec l'ID externe associé et la charge utile tronquée. |
| Type de données              | Vous pouvez synchroniser les attributs utilisateurs via l’ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connectera à votre entrepôt de données ou à votre environnement Cloud dans n'importe quelle région ou chez n’importe quel fournisseur Cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
