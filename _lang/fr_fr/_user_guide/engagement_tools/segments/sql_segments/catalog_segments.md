---
nav_title: "Segments du catalogue"
article_title: Segments du catalogue
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "Cet article décrit comment créer des segments de catalogue, qui utilisent les données de catalogue dans les extensions de segment SQL pour constituer des audiences d'utilisateurs."
tool: Segments
---

# Segments de catalogue

> Les segments de catalogue sont un type d'extension de segment SQL qui est créé en combinant des données de catalogue avec des données provenant d'événements personnalisés ou d'achats. Ils peuvent être référencés dans un segment, puis ciblés par des campagnes et des canvas. 

{% alert important %}
Les segments de catalogue sont actuellement en accès anticipé. Si vous souhaitez participer à cet accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

Les segments de catalogue utilisent SQL pour joindre les données des catalogues et les données des événements personnalisés ou des achats. Pour ce faire, vous devez avoir un champ d'identifiant commun dans vos catalogues et vos événements personnalisés ou achats. Par exemple, la valeur d'un identifiant d'article dans un catalogue doit correspondre à la valeur d'une propriété dans un événement personnalisé.

## Création d'un segment de catalogue

1. Allez dans **Extensions de segments** > **Créer une nouvelle extension** > **Commencer par un modèle** et sélectionnez un modèle. <br>![Fenêtre modale avec possibilité de créer un segment de catalogue pour des événements ou des achats.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. L'éditeur SQL se remplit automatiquement avec un modèle. <br>![Editeur SQL avec un modèle pré-généré.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Ce modèle combine les données d'événements utilisateur avec les données du catalogue pour segmenter les utilisateurs qui ont interagi avec certains articles du catalogue.

3. Utilisez l'onglet **Variables** pour fournir les champs nécessaires à votre modèle avant de générer votre segment. <br>Pour que Braze identifie les utilisateurs en fonction de leur engagement avec les articles du catalogue, vous devez faire ce qui suit : <br> \- Sélectionnez un catalogue contenant un champ de catalogue <br> \- Sélectionnez un événement personnalisé contenant une propriété d'événement <br> Faites correspondre votre champ de catalogue et les valeurs de propriété de l'événement

Voici des directives pour sélectionner les variables :

| Champ de variable | Description |
| --- | --- |
| `Catalog` | Le nom du catalogue que vous utilisez pour cibler les utilisateurs. |
| `Catalog field`| Le champ de votre catalogue qui contient les mêmes valeurs que votre `Custom event property`. Il s’agit souvent d’un type d'identifiant. Dans le cas du commerce électronique, il s'agit de `shopify_id`. |
| `Custom event` | Le nom de votre événement personnalisé, qui est le même événement contenant une propriété avec des valeurs correspondant à votre `Catalog field`. Dans le cas du commerce électronique, il s'agit de `Made Order`. |
| `Custom event property` | Le nom de votre propriété d'événement personnalisée, qui correspond aux valeurs de votre `Catalog field`. Dans l'exemple d'utilisation du commerce électronique, il s'agirait de `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. Si nécessaire, remplissez les champs optionnels supplémentaires pour votre cas d'utilisation afin de segmenter par une valeur de champ particulière dans votre catalogue :
- `Catalog field` : Un champ particulier (nom de colonne) dans ce catalogue
- `Value` : Une valeur spécifique dans ce champ ou cette colonne <br><br> En utilisant l'application de santé comme exemple, disons que dans le catalogue de chaque médecin que vous pourriez réserver, il y a un champ appelé `specialty` qui contient une valeur telle que `vision` ou `dental`. Pour segmenter les utilisateurs qui ont visité des médecins avec la valeur `dental`, vous pouvez sélectionner `specialty` comme `Catalog field`, et sélectionner `dental` comme `Value`.

5. Après avoir créé un segment SQL, nous vous recommandons de cliquer sur **Exécuter l'aperçu** pour voir si votre requête renvoie des utilisateurs ou s'il y a des erreurs. Pour plus d'informations sur [l'aperçu des résultats de la requête]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), la gestion des [extensions de segment SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions), et plus encore, consultez les [extensions de segment SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Si vous créez un segment SQL qui utilise la table `CATALOGS_ITEMS_SHARED`, vous devez spécifier un ID de catalogue. Par exemple :

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

## Actualiser l’effectif du segment

Pour actualiser la composition d'un segment de catalogue, ouvrez ce segment et sélectionnez **Actions** > **Actualiser** > **Oui, actualiser**.

{% alert tip %}
Si vous avez créé un segment dans lequel vous vous attendez à ce que les utilisateurs entrent et sortent régulièrement, actualisez manuellement le segment de catalogue qu'il utilise avant de cibler ce segment dans une campagne ou un Canvas.
{% endalert %}

### Désigner les paramètres d'actualisation

{% multi_lang_include segments.md section='Actualiser les paramètres' %}

## Cas d’utilisation

### Application de santé

Disons que vous avez une application de santé et que vous souhaitez segmenter les utilisateurs qui ont réservé une visite chez le dentiste. Vous avez également ce qui suit :

- Un catalogue `Doctors` qui contient les différents médecins qu'un patient peut réserver, chacun assigné avec un `doctor ID`
- Un événement personnalisé `Booked Visit` avec une propriété `doctor ID` qui partage les mêmes valeurs que le champ `doctor ID` dans votre catalogue
- Un champ `speciality` dans votre catalogue qui contient la valeur `dental`

Vous établiriez un segment de catalogue en utilisant les variables suivantes :

| Variable | Propriété |
| --- | --- |
| `Catalog`| Médecins |
| `Catalog field` | identifiant du médecin |
| `Custom event`| Visite réservée|
| `Custom event property` | identifiant du médecin |
| `(Under Filter SQL Results) Catalog field` | Spécialité |
| `(Under Filter SQL Results) Value`| Dentaire |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### plateforme SaaS

Disons que vous avez une plateforme SaaS B2B et que vous souhaitez segmenter les utilisateurs qui sont des employés d'un client existant. Vous avez également ce qui suit :

- Un catalogue `Accounts` qui contient les différents comptes qui utilisent actuellement votre plateforme SaaS, chacun étant assigné avec un `account ID`
- Un événement personnalisé `Event Attendance` avec une propriété "ID de compte" qui partage les mêmes valeurs que le champ "ID de compte" dans votre catalogue
- Un champ `Classification` dans votre catalogue qui contient la valeur `enterprise`

Vous établiriez un segment de catalogue en utilisant les variables suivantes :

| Variable | Propriété |
| --- | --- |
| `Catalog` | Comptes |
| `Catalog field `| ID de compte |
| `Custom event` | Participation aux événements |
| `Custom event property` | ID de compte |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Entreprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### L'exécution d'un segment de catalogue consomme-t-elle des crédits d'extension de segment SQL ?

Oui, les segments de catalogue sont alimentés par SQL et consomment des crédits d'extension de segment SQL. Pour en savoir plus, consultez la section [Utilisation des segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### La création d'un segment de catalogue consomme-t-elle des quotas d'extension de segment SQL ?

Oui. De la même manière que les extensions de segment SQL comptent pour votre quota d'extension de segment, les segments de catalogue comptent également pour ce quota.

### J'ai un cas d'utilisation de segment de catalogue que le modèle actuel ne sert pas. Comment devrais-je configurer cela ?

Contactez votre responsable du support client ou [Support Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) pour des conseils supplémentaires.

