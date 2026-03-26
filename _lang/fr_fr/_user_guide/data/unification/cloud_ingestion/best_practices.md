---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques pour l'ingestion de données cloud
toc_headers: h2
page_order: 0
page_type: reference
description: "Cette page fournit un aperçu de l'ingestion de données cloud, des bonnes pratiques et des limites du produit."

---

# Bonnes pratiques

> L'ingestion de données cloud de Braze vous permet d'établir une connexion directe entre votre entrepôt de données ou votre système de stockage de fichiers et Braze, afin de synchroniser les données pertinentes relatives aux utilisateurs ou aux catalogues. Lorsque vous synchronisez ces données avec Braze, vous pouvez les exploiter pour des cas d'utilisation tels que la personnalisation, le déclenchement ou la segmentation. 

## Comprendre la colonne `UPDATED_AT`

{% alert note %}
`UPDATED_AT` est pertinent uniquement pour les intégrations d'entrepôts de données, et non pour les synchronisations S3.
{% endalert %}

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. À chaque exécution de la synchronisation, Braze reflète toutes les données mises à jour.

{% alert important %}
Braze CDI synchronise les lignes strictement en fonction de la valeur `UPDATED_AT`, que le contenu de la ligne soit identique ou non à celui actuellement présent dans Braze. Compte tenu de cela, nous recommandons d'utiliser `UPDATED_AT` correctement afin de ne synchroniser que les données nouvelles ou mises à jour, et ainsi éviter toute consommation inutile de points de donnée.
{% endalert %}

### Exemple : synchronisation récurrente

Pour illustrer l'utilisation de `UPDATED_AT` dans une synchronisation CDI, considérez cet exemple de synchronisation récurrente pour la mise à jour des attributs utilisateur :

- Sources de stockage de fichiers 
   - Amazon S3

## Types de données pris en charge 

L'ingestion de données cloud prend en charge les types de données suivants : 
- Attributs utilisateur, notamment :
   - Attributs personnalisés imbriqués
   - Tableaux d'objets
   - États d'abonnement
- Événements personnalisés
- Événements d'achat
- Éléments de catalogue
- Demandes de suppression d'utilisateur

Vous pouvez mettre à jour les données utilisateur à l'aide de l'ID externe, de l'alias d'utilisateur, de l'identifiant Braze, de l'e-mail ou du numéro de téléphone. Vous pouvez supprimer des utilisateurs par ID externe, alias d'utilisateur ou identifiant Braze. 

## Ce qui est synchronisé

À chaque exécution d'une synchronisation, Braze recherche les lignes qui n'ont pas encore été synchronisées. Cette vérification s'appuie sur la colonne `UPDATED_AT` de votre table ou vue. Braze sélectionne et importe toutes les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur `UPDATED_AT` synchronisée. Les lignes situées exactement à l'horodatage limite peuvent également être re-synchronisées si de nouvelles lignes sont ajoutées avec ce même horodatage entre deux exécutions.

{% alert important %}
CDI suit le nombre de lignes à la dernière valeur `UPDATED_AT` synchronisée. Si de nouvelles lignes sont ajoutées avec ce même horodatage entre deux exécutions, CDI passe à une limite inclusive (`>=`) et re-synchronise toutes les lignes à cet horodatage, y compris celles déjà traitées. Pour éviter les synchronisations en double et la consommation inutile de points de donnée, utilisez des valeurs `UPDATED_AT` uniques entre les exécutions de synchronisation. Pour plus d'informations, consultez [Éviter la re-synchronisation de lignes avec des horodatages en double](#avoid-resyncing-rows-with-duplicate-timestamps).
{% endalert %}

Dans votre entrepôt de données, ajoutez les utilisateurs et attributs suivants à votre table, en définissant l'heure `UPDATED_AT` sur le moment où vous ajoutez ces données :

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

Lors de la prochaine synchronisation planifiée, Braze synchronise toutes les lignes dont l'horodatage `UPDATED_AT` est postérieur au dernier horodatage synchronisé. Braze met à jour ou ajoute des champs, vous n'avez donc pas besoin de synchroniser l'intégralité du profil utilisateur à chaque fois. Après la synchronisation, les profils utilisateur reflètent les nouvelles mises à jour :

**Synchronisation récurrente, deuxième exécution le 20 juillet 2022 à 12 h**

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

Une nouvelle ligne a été ajoutée pour `customer_9012`, mais sa valeur `UPDATED_AT` (`2022-07-16 00:25:30`) est antérieure à l'horodatage enregistré (`2022-07-19 09:07:23`), elle ne sera donc pas synchronisée. En revanche, la ligne existante pour `customer_5678` a une valeur `UPDATED_AT` égale à l'horodatage enregistré, elle est donc re-synchronisée en raison de la limite inclusive. Pour plus de détails sur ce comportement, consultez [Assurez-vous que l'heure UPDATED_AT ne correspond pas à celle de votre synchronisation](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync). La valeur `UPDATED_AT` enregistrée reste `2022-07-19 09:07:23`.

**Synchronisation récurrente, troisième exécution le 21 juillet 2022 à 12 h**

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

Lors de cette troisième exécution, une nouvelle ligne a été ajoutée pour `customer_1234` avec une valeur `UPDATED_AT` (`2022-07-21 08:30:00`) postérieure à l'horodatage enregistré. Cette nouvelle ligne et la ligne existante pour `customer_5678` (dont la valeur `UPDATED_AT` est égale à l'horodatage enregistré) sont toutes deux synchronisées. La valeur `UPDATED_AT` enregistrée est désormais `2022-07-21 08:30:00`.

{% alert note %}
Les valeurs `UPDATED_AT` peuvent être postérieures à l'heure de début d'exécution d'une synchronisation donnée. Cependant, cette pratique n'est pas recommandée car elle repousse le dernier horodatage `UPDATED_AT` « dans le futur » et les synchronisations suivantes ne synchroniseront pas les valeurs antérieures.
{% endalert %}

## Utilisez un horodatage UTC pour la colonne `UPDATED_AT`

La colonne `UPDATED_AT` doit être en UTC pour éviter les problèmes liés aux changements d'heure. Utilisez de préférence des fonctions UTC uniquement, telles que `SYSDATE()` plutôt que `CURRENT_DATE()`, dès que possible.

## Éviter la re-synchronisation de lignes avec des horodatages en double {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI suit le nombre de lignes à la dernière valeur `UPDATED_AT` synchronisée. Si CDI détecte que de nouvelles lignes ont été ajoutées avec ce même horodatage depuis la dernière exécution, il utilise une limite inclusive (`>=`) pour re-sélectionner toutes les lignes à cet horodatage, y compris celles déjà traitées. Sinon, CDI utilise une limite exclusive (`>`) et ne sélectionne que les lignes strictement postérieures à la dernière valeur synchronisée.

Par exemple, si une synchronisation traite cinq lignes avec `UPDATED_AT = 2025-04-01 00:00:00`, et qu'une sixième ligne est ajoutée ultérieurement avec le même horodatage, la synchronisation suivante détecte le changement de nombre et re-synchronise les six lignes. Cela peut entraîner des données en double et une consommation inutile de points de donnée.

Pour éviter cela :

- Si vous configurez une synchronisation avec une `VIEW`, n'utilisez pas `CURRENT_TIMESTAMP` comme valeur par défaut. Cela entraînerait la synchronisation de toutes les données à chaque exécution, car le champ `UPDATED_AT` serait évalué au moment de l'exécution de la requête.
- Si vous avez des pipelines ou des requêtes de longue durée qui écrivent des données dans votre table source, évitez de les exécuter en même temps qu'une synchronisation, ou évitez d'utiliser le même horodatage pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les lignes qui partagent le même horodatage.
- Utilisez des valeurs `UPDATED_AT` uniques et croissantes de manière monotone pour éviter que des lignes ne soient re-sélectionnées après avoir été traitées.

### Exemple : gestion des mises à jour ultérieures

Cet exemple illustre le processus général de synchronisation des données pour la première fois, puis de mise à jour des seules données modifiées (deltas) lors des mises à jour suivantes. Supposons que nous ayons une table `EXAMPLE_DATA` contenant des données utilisateur. Le jour 1, elle contient les valeurs suivantes :

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
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Pour obtenir ces données dans le format attendu par CDI, vous pouvez exécuter la requête suivante :

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

Rien de tout cela n'ayant été synchronisé avec Braze auparavant, ajoutez l'ensemble à la table source pour CDI :

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

Une synchronisation s'exécute et Braze enregistre que vous avez synchronisé toutes les données disponibles jusqu'à « 2023-03-16 15:00:00 ». Ensuite, le matin du jour 2, un processus ETL s'exécute et certains champs de votre table d'utilisateurs sont mis à jour (en surbrillance) :

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
            <td style="background-color: #FFFF00;">red</td>
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
            <td style="background-color: #FFFF00;">green</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Vous devez maintenant ajouter uniquement les valeurs modifiées dans la table source CDI. Ces lignes peuvent être ajoutées en complément plutôt que de remplacer les anciennes. La table se présente désormais comme suit :

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

### N'écrivez que les attributs nouveaux ou mis à jour pour limiter la consommation

À chaque exécution d'une synchronisation, Braze recherche les lignes qui n'ont pas encore été synchronisées. Cette vérification s'appuie sur la colonne `UPDATED_AT` de votre table ou vue. Braze sélectionne et importe toutes les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur `UPDATED_AT` synchronisée, qu'elles soient identiques ou non à celles actuellement présentes dans le profil utilisateur. Les lignes situées à l'horodatage limite peuvent également être re-synchronisées si de nouvelles lignes partagent cet horodatage. C'est pourquoi nous recommandons de ne synchroniser que les attributs que vous souhaitez ajouter ou mettre à jour.

La consommation de points de donnée est identique avec CDI et avec d'autres méthodes d'ingestion telles que les API REST ou les SDK. Il est donc de votre responsabilité de vous assurer que vous n'ajoutez que des attributs nouveaux ou mis à jour dans vos tables sources.

### Séparer la colonne `EXTERNAL_ID` de la colonne `PAYLOAD`

L'objet `PAYLOAD` ne doit pas contenir d'ID externe ni d'autre type d'identifiant. 

### Supprimer un attribut

Vous pouvez lui attribuer la valeur `null` si vous souhaitez omettre un attribut du profil d'un utilisateur. Si vous souhaitez qu'un attribut reste inchangé, ne l'envoyez pas à Braze tant qu'il n'a pas été mis à jour. Pour supprimer complètement un attribut, utilisez `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Effectuer des mises à jour incrémentielles

Effectuez des mises à jour incrémentielles de vos données afin d'éviter les écrasements involontaires lors de mises à jour simultanées.

{% alert important %}
* **Mises à jour de différents attributs :** Dans la grande majorité des cas, si deux mises à jour n'affectent pas les mêmes attributs d'un utilisateur, elles produisent des résultats totalement indépendants. Par exemple, si vous mettez à jour l'attribut `Color` d'un utilisateur et que vous mettez à jour séparément son attribut `Size`, les deux mises à jour devraient être appliquées correctement, même si elles ont lieu à quelques secondes d'intervalle.
* **Mises à jour du même attribut :** Des conditions de concurrence peuvent survenir lorsque plusieurs mises à jour ciblent le même attribut au cours d'une même exécution de synchronisation. Dans ces cas exceptionnels, une mise à jour peut écraser l'autre. La meilleure façon d'éviter ce comportement est de vous assurer que les données source de votre synchronisation CDI reflètent uniquement l'état le plus récent de chaque utilisateur, ou que toutes les mises à jour pour un utilisateur donné ou une paire utilisateur+attribut sont contenues dans une seule ligne.
* **Opérateurs de tableau d'objets :** Les seules exceptions aux mises à jour indépendantes concernent les opérateurs `$add`, `$remove` et `$update` pour les tableaux d'objets, où les mises à jour d'un même tableau peuvent interagir entre elles.
* **Événements :** Les conditions de concurrence n'affectent pas les événements, car chaque événement est unique et associé à un horodatage.
{% endalert %}

La meilleure façon d'éviter ce comportement est de vous assurer que les données source de votre synchronisation CDI reflètent uniquement l'état le plus récent de chaque utilisateur, ou que toutes les mises à jour pour un utilisateur donné ou une paire utilisateur+attribut sont contenues dans une seule ligne.

### Créer une chaîne de caractères JSON à partir d'une autre table

Si vous préférez stocker chaque attribut dans sa propre colonne en interne, vous devez convertir ces colonnes en chaîne de caractères JSON pour alimenter la synchronisation avec Braze. Pour ce faire, vous pouvez utiliser une requête du type :

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

Braze utilise l'horodatage `UPDATED_AT` pour suivre les données qui ont été synchronisées avec succès. CDI suit également le nombre de lignes au dernier horodatage synchronisé. Si de nouvelles lignes sont ajoutées avec ce même horodatage entre deux exécutions, CDI re-synchronise toutes les lignes à cet horodatage, ce qui peut entraîner des données en double. Pour plus de détails et de conseils, consultez [Éviter la re-synchronisation de lignes avec des horodatages en double](#avoid-resyncing-rows-with-duplicate-timestamps).

### Configuration de la table

Nous disposons d'un [dépôt GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) public permettant aux clients de partager des bonnes pratiques ou des extraits de code. Pour contribuer avec vos propres extraits de code, créez une pull request !

### Formatage des données

Toutes les opérations possibles via l'endpoint `/users/track` de Braze sont prises en charge par l'ingestion de données cloud, notamment la mise à jour des attributs personnalisés imbriqués, l'ajout d'un statut d'abonnement et la synchronisation d'événements personnalisés ou d'achats. 

Les champs de la charge utile doivent respecter le même format que l'endpoint `/users/track` correspondant. Pour plus d'informations sur les exigences de formatage, consultez les ressources suivantes :

| Type de données | Spécifications de formatage |
| --------- | ---------| --------- | ----------- |
| `attributes` | Voir [objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Voir [objet événements]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Voir [objet achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Notez l'exigence particulière pour la [capture des dates]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) dans les attributs imbriqués. 

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
Pour synchroniser des événements, un nom d'événement est requis. Formatez le champ `time` sous forme de chaîne de caractères ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, Braze utilise la valeur de la colonne `UPDATED_AT` comme heure de l'événement. Les autres champs, y compris `app_id` et `properties`, sont facultatifs. 

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
Pour synchroniser les événements d'achat, `product_id`, `currency` et `price` sont requis. Formatez le champ `time`, qui est facultatif, sous forme de chaîne de caractères ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, Braze utilise la valeur de la colonne `UPDATED_AT` comme heure de l'événement. Les autres champs, y compris `app_id`, `quantity` et `properties`, sont facultatifs.

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

### Éviter les délais d'expiration pour les requêtes d'entrepôt de données

Nous recommandons que les requêtes soient exécutées en moins d'une heure pour des performances optimales et pour éviter les erreurs potentielles. Si les requêtes dépassent ce délai, envisagez de revoir la configuration de votre entrepôt de données. L'optimisation des ressources allouées à votre entrepôt peut contribuer à améliorer la vitesse d'exécution des requêtes.

## Limites du produit

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d'intégrations | Le nombre d'intégrations que vous pouvez configurer n'est pas limité. Cependant, vous ne pourrez configurer qu'une seule intégration par table ou vue.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Braze interrompt toute synchronisation comportant plus de 500 millions de nouvelles lignes. Si vous avez besoin d'une limite plus élevée, contactez votre Customer Success Manager Braze ou l'assistance Braze. |
| Attributs par ligne     | Chaque ligne doit contenir un seul ID utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau compte pour un attribut). |
| Taille de la charge utile           | Chaque ligne peut contenir une charge utile allant jusqu'à 1 Mo. Braze rejette les charges utiles supérieures à 1&nbsp;Mo et consigne l'erreur « La charge utile était supérieure à 1 Mo » dans le journal de synchronisation, avec l'ID externe associé et la charge utile tronquée. |
| Type de données              | Vous pouvez synchroniser les attributs utilisateur, les événements et les achats via l'ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connectera à votre entrepôt de données ou à votre environnement cloud dans n'importe quelle région ou chez n'importe quel fournisseur cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>