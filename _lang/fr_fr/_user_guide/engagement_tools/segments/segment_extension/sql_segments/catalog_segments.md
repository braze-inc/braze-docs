---
nav_title: "Segments de catalogue"
article_title: Segments de catalogue
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "Cet article décrit comment créer des segments de catalogue, qui utilisent les données de catalogue dans les extensions de segments SQL pour constituer des audiences d'utilisateurs."
tool: Segments
---

# Segments de catalogue

> Les segments de catalogue sont un type d'extension de segment SQL créé en combinant des données de catalogue avec des données provenant d'événements personnalisés ou d'achats. Ils peuvent être référencés dans un segment, puis ciblés par des campagnes et des Canvas. 

Les segments de catalogue utilisent SQL pour joindre les données des catalogues aux données des événements personnalisés ou des achats. Pour cela, vous devez disposer d'un champ d'identifiant commun entre vos catalogues et vos événements personnalisés ou achats. Par exemple, la valeur d'un identifiant d'article dans un catalogue doit correspondre à la valeur d'une propriété dans un événement personnalisé.

## Créer un segment de catalogue

1. Accédez à **Extensions de segments** > **Créer une nouvelle extension** > **Commencer par un modèle** et sélectionnez un modèle. <br>![Fenêtre modale offrant la possibilité de créer un segment de catalogue pour les événements, les achats ou les segments RFM.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. L'éditeur SQL se remplit automatiquement avec un modèle. <br>![Éditeur SQL avec un modèle prégénéré.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Ce modèle combine les données d'événements utilisateur avec les données du catalogue pour segmenter les utilisateurs ayant interagi avec certains articles du catalogue.

3. Utilisez l'onglet **Variables** pour renseigner les champs nécessaires à votre modèle avant de générer votre segment. <br>Pour que Braze identifie les utilisateurs en fonction de leur engagement avec les articles du catalogue, vous devez : <br> - Sélectionner un catalogue contenant un champ de catalogue <br> - Sélectionner un événement personnalisé contenant une propriété d'événement <br> - Faire correspondre les valeurs de votre champ de catalogue et de la propriété d'événement

Voici les recommandations pour sélectionner les variables :

| Champ de variable | Description |
| --- | --- |
| `Catalog` | Le nom du catalogue que vous utilisez pour cibler les utilisateurs. |
| `Catalog field`| Le champ de votre catalogue qui contient les mêmes valeurs que votre `Custom event property`. Il s'agit souvent d'un type d'identifiant. Dans le cas d'un site e-commerce, il s'agirait de `shopify_id`. |
| `Custom event` | Le nom de votre événement personnalisé, c'est-à-dire l'événement contenant une propriété dont les valeurs correspondent à votre `Catalog field`. Dans le cas d'un site e-commerce, il s'agirait de `Made Order`. |
| `Custom event property` | Le nom de la propriété de votre événement personnalisé, dont les valeurs correspondent à votre `Catalog field`. Dans l'exemple e-commerce, il s'agirait de `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4. Si nécessaire, remplissez les champs facultatifs supplémentaires pour votre cas d'utilisation afin de segmenter par une valeur de champ particulière dans votre catalogue :
- `Catalog field` : Un champ particulier (nom de colonne) dans ce catalogue
- `Value` : Une valeur spécifique dans ce champ ou cette colonne <br><br> Prenons l'exemple d'une application de santé : imaginons que dans le catalogue de chaque médecin disponible à la réservation, il existe un champ appelé `specialty` contenant une valeur telle que `vision` ou `dental`. Pour segmenter les utilisateurs ayant consulté des médecins avec la valeur `dental`, vous pouvez sélectionner `specialty` comme `Catalog field` et `dental` comme `Value`.

5. Après avoir créé un segment SQL, nous vous recommandons de cliquer sur **Exécuter l'aperçu** pour vérifier si votre requête renvoie des utilisateurs ou s'il y a des erreurs. Pour en savoir plus sur [l'aperçu des résultats de requête]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), la gestion des [extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) et d'autres sujets, consultez la page [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Si vous créez un segment SQL qui utilise la table `CATALOGS_ITEMS_SHARED`, vous devez spécifier un ID de catalogue. Par exemple :

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Déterminer si vous devez inverser le SQL

Bien qu'il ne soit pas possible d'interroger directement les utilisateurs sans aucun événement, vous pouvez utiliser **Inverser le SQL** pour cibler ces utilisateurs.

Par exemple, pour cibler les utilisateurs ayant effectué moins de trois achats, commencez par écrire une requête sélectionnant les utilisateurs ayant effectué trois achats ou plus. Ensuite, sélectionnez **Inverser le SQL** pour cibler les utilisateurs ayant effectué moins de trois achats (y compris ceux n'en ayant effectué aucun).

![Extension de segments nommée « A cliqué sur 1 à 4 e-mails au cours des 30 derniers jours » avec l'option d'inversion de SQL sélectionnée.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
À moins que vous ne cherchiez spécifiquement à cibler les utilisateurs sans aucun événement, vous n'aurez pas besoin d'inverser le SQL. Si l'option **Inverser le SQL** est sélectionnée, vérifiez que cette fonctionnalité est bien nécessaire et que le segment correspond à l'audience souhaitée. Par exemple, si une requête cible les utilisateurs ayant au moins un événement, elle ne ciblera que les utilisateurs sans aucun événement une fois inversée.
{% endalert %}

## Actualiser la composition du segment

Pour actualiser la composition d'un segment de catalogue, ouvrez ce segment et sélectionnez **Actions** > **Actualiser** > **Oui, actualiser**.

{% alert tip %}
Si vous avez créé un segment dans lequel les utilisateurs sont susceptibles d'entrer et de sortir régulièrement, pensez à actualiser manuellement le segment de catalogue utilisé avant de cibler ce segment dans une campagne ou un Canvas.
{% endalert %}

### Configurer les paramètres d'actualisation

{% multi_lang_include segments.md section='Refresh settings' %}

## Cas d'utilisation

{% tabs local %}
{% tab Health %}

### Application de santé

Imaginons que vous disposez d'une application de santé et que vous souhaitez segmenter les utilisateurs ayant réservé une visite chez le dentiste. Vous disposez également des éléments suivants :

- Un catalogue `Doctors` contenant les différents médecins qu'un patient peut réserver, chacun associé à un `doctor ID`
- Un événement personnalisé `Booked Visit` avec une propriété `doctor ID` partageant les mêmes valeurs que le champ `doctor ID` de votre catalogue
- Un champ `speciality` dans votre catalogue contenant la valeur `dental`

Vous configureriez un segment de catalogue avec les variables suivantes :

| Variable | Propriété |
| --- | --- |
| `Catalog`| Doctors |
| `Catalog field` | doctor ID |
| `Custom event`| Booked Visit|
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### Plateforme SaaS

Imaginons que vous disposez d'une plateforme SaaS B2B et que vous souhaitez segmenter les utilisateurs qui sont des employés d'un client existant. Vous disposez également des éléments suivants :

- Un catalogue `Accounts` contenant les différents comptes utilisant actuellement votre plateforme SaaS, chacun associé à un `account ID`
- Un événement personnalisé `Event Attendance` avec une propriété « account ID » partageant les mêmes valeurs que le champ « account ID » de votre catalogue
- Un champ `Classification` dans votre catalogue contenant la valeur `enterprise`

Vous configureriez un segment de catalogue avec les variables suivantes :

| Variable | Propriété |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field `| account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Foire aux questions

### L'exécution d'un segment de catalogue consomme-t-elle des crédits d'extension de segment SQL ?

Oui, les segments de catalogue reposent sur SQL et consomment des crédits d'extension de segment SQL. Pour en savoir plus, consultez la section [Utilisation des segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### La création d'un segment de catalogue consomme-t-elle des quotas d'extension de segment SQL ?

Oui. De la même manière que les extensions de segments SQL sont décomptées de votre quota d'extensions de segments, les segments de catalogue le sont également.

### J'ai un cas d'utilisation de segment de catalogue que le modèle actuel ne couvre pas. Comment dois-je procéder ?

Contactez votre Customer Success Manager ou l'[assistance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) pour obtenir des conseils supplémentaires.