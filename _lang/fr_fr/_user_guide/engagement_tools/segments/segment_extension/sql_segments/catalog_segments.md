---
nav_title: "Segmentation du catalogue"
article_title: Segments du catalogue
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "Cet article explique comment créer des segments de catalogue, qui utilisent les données de catalogue dans SQL Segment Extensions pour créer des audiences d'utilisateurs."
tool: Segments
---

# Segmentation du catalogue

> Les segments de catalogue sont un type d'extension de segment SQL qui est créé en combinant des données de catalogue avec des données provenant d'événements personnalisés ou d'achats. Ils peuvent être référencés dans un segment et ensuite ciblés par des campagnes et des Canevas. 

{% alert important %}
Les segments du catalogue sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Les segments de catalogue utilisent SQL pour joindre les données des catalogues et les données des événements personnalisés ou des achats. Pour ce faire, vous devez disposer d'un champ d'identification commun à l'ensemble de vos catalogues et de vos événements personnalisés ou achats. Par exemple, la valeur d'un ID d'article dans un catalogue doit correspondre à la valeur d'une propriété dans un événement personnalisé.

## Création d'un segment de catalogue

1. Allez dans **Extensions de segments** > **Créer une nouvelle extension** > **Commencer par un modèle** et sélectionnez un modèle. <br>\![Fenêtre modale/boîte de dialogue, etc. avec la possibilité de créer un segment de catalogue pour des événements ou des achats.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. L'éditeur SQL s'enrichit automatiquement d'un modèle. <br>\![Editeur SQL avec un modèle pré-généré.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Ce modèle associe les données des événements utilisateurs aux données du catalogue afin de segmenter les utilisateurs qui ont acheté certains articles du catalogue.

3. Utilisez l'onglet **Variables** pour fournir les champs nécessaires à votre modèle avant de générer votre segmentation. <br>Pour que Braze identifie les utilisateurs en fonction de leur engagement avec les éléments du catalogue, vous devez procéder comme suit : <br> \- Sélectionnez un catalogue qui contient un champ de catalogue <br> \- Sélectionnez un événement personnalisé qui contient une propriété d'événement <br> \- Faites correspondre les valeurs des propriétés des champs et des événements de votre catalogue.

Voici quelques conseils pour sélectionner les variables :

| Champ variable | Description |
| --- | --- |
| `Catalog` | Le nom du catalogue que vous utilisez pour le ciblage des utilisateurs. |
| `Catalog field`| Le champ de votre catalogue qui contient les mêmes valeurs que votre `Custom event property`. Il s'agit souvent d'un type d'ID. Dans le cas du commerce électronique, il s'agit de `shopify_id`. |
| `Custom event` | Le nom de votre événement personnalisé, qui est le même événement qui contient une propriété dont les valeurs correspondent à votre `Catalog field`. Dans le cas du commerce électronique, il s'agit de `Made Order`. |
| `Custom event property` | Le nom de votre propriété d'événement personnalisé, qui fait correspondre les valeurs avec votre `Catalog field`. Dans l'exemple d'utilisation du commerce électronique, il s'agirait de `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. Si nécessaire, remplissez des champs facultatifs supplémentaires pour votre cas d'utilisation afin de segmenter par une valeur de champ particulière dans votre catalogue :
- `Catalog field`: Un champ particulier (nom de colonne) dans ce catalogue
- `Value`: Une valeur spécifique dans ce champ ou cette colonne <br><br> Si l'on prend l'exemple de l'application santé, disons que dans le catalogue de chaque médecin que vous pouvez consulter, il y a un champ appelé `specialty` qui contient une valeur telle que `vision` ou `dental`. Pour segmenter les utilisateurs qui ont consulté un médecin avec la valeur `dental`, vous pouvez sélectionner `specialty` comme `Catalog field`, et sélectionner `dental` comme `Value`.

5. Après avoir créé un segment SQL, nous vous recommandons de cliquer sur **Exécuter l'aperçu** pour voir si votre requête renvoie des utilisateurs ou s'il y a des erreurs. Pour plus d'informations sur la [prévisualisation des résultats des requêtes]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), la gestion des [extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions), etc., consultez le site [Extensions de segments SQL.]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 

{% alert note %}
Si vous créez un segment SQL qui utilise la table `CATALOGS_ITEMS_SHARED`, vous devez spécifier un ID de catalogue. Par exemple :

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Déterminer si vous devez inverser SQL

Bien qu'il ne soit pas possible de requêter directement les utilisateurs dont les événements sont nuls, vous pouvez utiliser **Invert SQL** pour cibler ces utilisateurs.

Par exemple, pour cibler les utilisateurs qui ont effectué moins de trois achats, écrivez d'abord une requête pour sélectionner les utilisateurs qui ont effectué trois achats ou plus. Ensuite, sélectionnez **Inverser le SQL** pour cibler les utilisateurs ayant effectué moins de trois achats (y compris ceux ayant effectué zéro achat).

!Extension de segment nommée "A cliqué sur 1 à 4 e-mails au cours des 30 derniers jours" avec l'option d'inversion de SQL sélectionnée.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
À moins que vous ne visiez spécifiquement à cibler les utilisateurs n'ayant aucun événement, vous n'aurez pas besoin d'inverser SQL. Si l'option **Inverser SQL** est sélectionnée, confirmez que la fonctionnalité est nécessaire et que la segmentation correspond à l'audience souhaitée. Par exemple, si une requête cible les utilisateurs ayant au moins un événement, elle ne ciblera que les utilisateurs ayant zéro événement lorsqu'elle est inversée.
{% endalert %}

## Actualiser la composition des segments

Pour actualiser la composition d'un segment de catalogue, ouvrez ce segment et sélectionnez **Actions** > **Actualiser** > **Oui, actualiser**.

{% alert tip %}
Si vous avez créé un segment dans lequel vous vous attendez à ce que les utilisateurs entrent et sortent régulièrement, actualisez manuellement le segment de catalogue qu'il utilise avant de cibler ce segment dans une campagne ou un Canvas.
{% endalert %}

### Désigner les paramètres d'actualisation

{% multi_lang_include segments.md section='Refresh settings' %}

## Cas d'utilisation

{% tabs local %}
{% tab Health %}

### Application santé

Imaginons que vous ayez une appli de santé et que vous souhaitiez segmenter les utilisateurs qui ont réservé une visite chez le dentiste. Vous disposez également des éléments suivants :

- Un catalogue `Doctors` qui contient les différents médecins qu'un patient peut réserver, chacun d'entre eux étant associé à un `doctor ID`
- Un événement personnalisé `Booked Visit` avec une propriété `doctor ID` qui partage les mêmes valeurs que le champ `doctor ID` de votre catalogue.
- Un champ `speciality` dans votre catalogue qui contient la valeur `dental` 

Vous pouvez configurer un segment de catalogue en utilisant les variables suivantes :

| Variable | Propriété |
| --- | --- |
| `Catalog`| Médecins |
| `Catalog field` | ID du médecin |
| `Custom event`| Visite réservée|
| `Custom event property` | ID du médecin |
| `(Under Filter SQL Results) Catalog field` | Spécialité |
| `(Under Filter SQL Results) Value`| Soins dentaires |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### Plate-forme SaaS

Supposons que vous ayez une plateforme SaaS B2B et que vous souhaitiez segmenter les utilisateurs qui sont des employés d'un client existant. Vous disposez également des éléments suivants :

- Un catalogue `Accounts` qui contient les différents comptes qui utilisent actuellement votre plateforme SaaS, chacun étant affecté d'un `account ID`
- Un événement personnalisé `Event Attendance` avec une propriété "account ID" qui partage les mêmes valeurs que le champ "account ID" de votre catalogue.
- Un champ `Classification` dans votre catalogue qui contient la valeur `enterprise` 

Vous pouvez configurer un segment de catalogue en utilisant les variables suivantes :

| Variable | Propriété |
| --- | --- |
| `Catalog` | Comptes |
| `Catalog field `| ID du compte |
| `Custom event` | Participation à l'événement |
| `Custom event property` | ID du compte |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Entreprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Questions fréquemment posées

### L'exécution d'un segment de catalogue consomme-t-elle des crédits d'extension de segments SQL ?

Oui, les segments de catalogue sont alimentés par SQL et consomment des crédits SQL Segment Extension. Pour en savoir plus, consultez l'[utilisation des segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### La création d'un segment de catalogue consomme-t-elle des allocations d'extensions de segments SQL ?

Oui. De la même manière que les extensions de segments SQL sont prises en compte dans votre quota d'extensions de segments, les segments de catalogues sont également pris en compte dans ce quota.

### J'ai un cas d'utilisation de segmentation de catalogue que le modèle actuel ne permet pas de réaliser. Comment dois-je procéder ?

Contactez votre gestionnaire d'assistance à la clientèle ou le [service d'assistance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) pour obtenir des conseils supplémentaires.

