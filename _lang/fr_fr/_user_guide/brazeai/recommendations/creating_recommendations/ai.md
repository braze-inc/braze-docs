---
nav_title: "Recommandations en matière d'intelligence artificielle"
article_title: "Création de recommandations d'éléments d'intelligence artificielle"
description: "Cet article de référence explique comment créer une recommandation d'article d'intelligence artificielle pour les articles d'un catalogue."
page_order: 1
---

# Création de recommandations d'articles par l'intelligence artificielle

> Découvrez comment créer un moteur de recommandation par intelligence artificielle à partir des articles de votre catalogue.

## À propos des recommandations d'articles de l'intelligence artificielle

Utilisez les recommandations d'articles de l'intelligence artificielle pour calculer les produits les plus populaires ou créer des recommandations personnalisées de l'intelligence artificielle pour un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) spécifique. Après avoir créé votre recommandation, vous pouvez utiliser la personnalisation pour insérer ces produits dans vos messages.

{% alert tip %}
Les [recommandations personnalisées par intelligence artificielle](#recommendation-types) fonctionnent mieux avec des centaines ou des milliers d'articles et généralement au moins 30 000 utilisateurs avec des données d'achat ou d'interaction. Il s'agit d'une indication approximative qui peut varier. Les autres types de recommandations peuvent fonctionner avec moins de données.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Création d'une recommandation d'article par l'intelligence artificielle

### Conditions préalables

Avant de commencer, vous devez effectuer les opérations suivantes :

- Vous devez avoir au moins un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) pour utiliser l'un des types de recommandation décrits ci-dessous.
- Vous devez disposer de données d'achat ou d'événement sur Braze (événements personnalisés ou objet d'achat) qui incluent une référence à des ID de produits uniques stockés dans un catalogue.

### Étape 1 : Créer une nouvelle recommandation

Vous pouvez créer une recommandation d'élément d'intelligence artificielle à partir de n'importe quel endroit du tableau de bord :

{% tabs local %}
{% tab From the navigation menu %}
1. Allez dans **Analyse/analytique** > **Recommandation d'élément d'intelligence artificielle (si utilisé comme adjectif**).
2. Sélectionnez **Créer une prédiction** > **Recommandation d'élément d'intelligence artificielle**.
{% endtab %}

{% tab From a catalog %}
Vous pouvez également choisir de créer une recommandation directement à partir d'un catalogue individuel. Sélectionnez votre catalogue dans la page **Catalogues**, puis sélectionnez **Créer une recommandation**.
{% endtab %}
{% endtabs %}

### Étape 2 : Ajouter les détails de la recommandation

Donnez un nom et une description facultative à votre recommandation.

\!["Détails de la recommandation" avec les champs nom et description.]({% image_buster /assets/img/item_recs_1.png %})

### Étape 3 : Définissez votre recommandation {#recommendation-type}

Sélectionnez un type de recommandation. Chaque type utilise les six derniers mois de données d'interaction avec l'article, telles que les données d'un achat ou d'un événement personnalisé. Pour des informations plus détaillées et des cas d'utilisation pour chacun d'entre eux, voir [Types et cas d'utilisation]({{site.baseurl}}/user_guide/brazeai/recommendations/).

{% alert tip %}
Lors de l'utilisation de **Plus récent** ou **Personnalisé par l'intelligence artificielle**, les utilisateurs dont les données sont insuffisantes pour créer des recommandations individualisées recevront les articles **les plus populaires** en guise de solution de repli. La proportion d'utilisateurs recevant la solution de repli **la plus populaire** est affichée sur la page **Analyse/analytique** (si les utilisateurs reçoivent une solution de repli la **plus populaire)**.
{% endalert %}

#### Étape 3.1 : Exclure les achats ou interactions antérieurs (facultatif)

Pour éviter de suggérer des articles qu'un utilisateur a déjà achetés ou avec lesquels il a déjà interagi, sélectionnez **Ne pas recommander d'articles avec lesquels les utilisateurs ont déjà interagi.** Cette option n'est disponible que lorsque le **type de** recommandation est défini sur **Intelligence artificielle personnalisée**.

\!["Définissez votre recommandation" avec "Intelligence artificielle personnalisée" comme type et l'option "Ne pas recommander des éléments avec lesquels les utilisateurs ont déjà interagi" sélectionnée.]({% image_buster /assets/img/item_recs_2-3.png %})

Ce paramètre empêche les messages de réutiliser les éléments qu'un utilisateur a déjà achetés ou avec lesquels il a interagi, à condition que la recommandation ait été mise à jour récemment. Les articles achetés ou ayant fait l'objet d'une interaction entre les mises à jour des recommandations peuvent encore apparaître. Pour la version gratuite des recommandations d'articles, les mises à jour sont hebdomadaires. Pour la version pro des recommandations d'articles d'intelligence artificielle, les mises à jour ont lieu toutes les 24 heures.

Par exemple, lorsque vous utilisez la version pro des recommandations d'articles par intelligence artificielle, si un utilisateur achète quelque chose puis reçoit un e-mail marketing dans les 30 minutes, l'article qu'il vient d'acheter risque de ne pas être exclu de l'e-mail à temps. Toutefois, les messages envoyés après 24 heures ne comporteront pas cet élément.

#### Étape 3.2 : Sélectionnez un catalogue

S'il n'est pas déjà renseigné, sélectionnez le [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) à partir duquel cette recommandation tirera les articles.

#### Étape 3.3 : Ajouter une sélection (facultatif)

Si vous souhaitez mieux contrôler votre recommandation, choisissez une [sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) pour appliquer des filtres personnalisés. Les sélections filtrent les recommandations en fonction de colonnes spécifiques de votre catalogue, telles que la marque, la taille ou l'emplacement/localisation. Les sélections qui contiennent du liquide ne peuvent pas être utilisées dans votre recommandation.

Un exemple de la sélection "en stock" choisie pour la recommandation.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Si vous ne trouvez pas votre sélection, assurez-vous d'abord qu'elle est configurée dans votre catalogue.
{% endalert %}

### Étape 4 : Sélectionnez l'interaction à l'origine des recommandations

Sélectionnez l'événement pour lequel vous souhaitez que cette recommandation soit optimisée. Cet événement est généralement un achat, mais il peut également s'agir de toute interaction avec un article.

Vous pouvez optimiser pour :

- Événements d'achat avec l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Événements personnalisés représentant un achat
- les événements personnalisés qui conseillent toute autre interaction avec l'élément (comme les vues de produits, les clics ou les lectures de médias).

Si vous choisissez **Événement personnalisé**, sélectionnez votre événement dans la liste.

\![L'événement personnalisé "Achat terminé" sélectionné comme mode de suivi des événements.]({% image_buster /assets/img/item_recs_3.png %})

### Étape 5 : Choisissez le nom de la propriété correspondante {#property-name}

Pour créer une recommandation, vous devez indiquer à Braze le champ de votre événement d'interaction (objet d'achat ou événement personnalisé) dont l'identifiant unique correspond au champ `id` d'un article dans le catalogue. Vous n'êtes pas sûr ? [Voir les exigences](#requirements).

Sélectionnez ce champ pour le **nom de la propriété**.

Le champ **Nom de la propriété** sera pré-rempli avec une liste de champs envoyés par le SDK à Braze. Si suffisamment de données sont fournies, ces biens seront également classés par ordre de probabilité d'être le bon bien. Sélectionnez celui qui correspond au champ `id` du catalogue.

\![Le nom de la propriété "purchase_item" sélectionnée qui correspond aux ID des articles dans le catalogue.]({% image_buster /assets/img/item_recs_4.png %})

#### Exigences {#requirements}

La sélection de votre bien immobilier est soumise à certaines conditions :

- Doit correspondre au champ `id` du catalogue que vous avez sélectionné.
- **Si vous avez sélectionné Objet d'achat :** Il doit s'agir de `product_id` ou d'un champ de votre événement d'interaction `properties`.
- **Si vous avez sélectionné Événement personnalisé :** Doit être un champ de votre événement personnalisé `properties`.
- Les champs imbriqués doivent être saisis dans le menu déroulant **Nom de la propriété** en notation par points, au format `event_property.nested_property`. Par exemple, si vous sélectionnez la propriété imbriquée `district_name` dans la propriété d'événement `location`, vous devez saisir `location.district_name`.
- Le champ peut se trouver à l'intérieur d'un tableau de produits ou se terminer par un tableau d'ID. Dans les deux cas, chaque ID de produit sera traité comme un événement distinct et séquentiel avec le même horodatage.

#### Exemples de mappages

Les exemples de mappages suivants font tous deux référence à ce catalogue d'exemples :

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">titre</th>
    <th class="tg-0pky">prix</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Noir Taille 7</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Rouge Taille 8</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas Blanc Taille 9</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Taille 10</td>
    <td class="tg-0pky">75,00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Custom event %}

Imaginons que vous souhaitiez utiliser l'événement personnalisé `added_to_cart` pour pouvoir recommander des produits similaires avant que le client ne passe à la caisse. L'événement `added_to_cart` a pour propriété d'événement `product_sku`.

La propriété `product_sku` doit alors inclure au moins une des valeurs de la colonne `id` du catalogue d'échantillons : "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" ou "ADI-PP-10". Vous n'avez pas besoin d'événements pour chaque article du catalogue, mais vous avez besoin de certains d'entre eux pour que le moteur de recommandation ait suffisamment de contenu pour travailler.

##### Exemple d'objet d'événement personnalisé

Cet événement a pour adresse `"product_sku": "ADI-BL-7"`, qui correspond au premier élément du catalogue d'échantillons.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Exemple d'objet d'événement personnalisé avec un tableau d'objets

Si les propriétés de votre événement contiennent plusieurs produits dans un tableau, chaque ID de produit sera traité comme un événement distinct et séquentiel. Cet événement peut utiliser la propriété `products.sku` pour faire correspondre les premier et troisième articles du catalogue d'échantillons.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Exemple d'objet d'événement personnalisé avec un objet imbriqué contenant un tableau d'ID de produit

Si vos ID de produits sont des valeurs dans un tableau plutôt que des objets, vous pouvez utiliser la même notation et chaque ID de produit sera traité comme un événement distinct et séquentiel. Ceci peut être combiné de manière flexible avec des objets imbriqués dans l'événement suivant en configurant la propriété comme `purchase.product_skus` pour qu'elle corresponde aux premier et troisième éléments du catalogue d'exemples.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Purchase object %}

Un objet d'achat est transmis par l'API lorsqu'un achat a été effectué.

En termes de mappage, la logique est la même pour les objets d'achat que pour les événements personnalisés, à ceci près que vous pouvez choisir d'utiliser le site `product_id` de l'objet d'achat ou un champ de l'objet `properties`.

Rappelez-vous que vous n'avez pas besoin d'événements pour chaque article du catalogue, mais vous devez en avoir quelques-uns pour que le moteur de recommandation ait suffisamment de contenu pour travailler.

##### Exemple d'objet d'achat mappé à l'ID du produit

Cet événement a pour adresse `"product_id": "ADI-BL-7`, qui mappe le premier élément du catalogue.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Exemple d'objet d'achat mappé à un champ de propriétés

Cet événement a pour propriété `"sku": "ADI-RD-8"`, qui correspond au deuxième article du catalogue.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Étape 6 : Former la recommandation

Lorsque vous êtes prêt, sélectionnez **Créer une recommandation**. Ce processus peut durer de 10 minutes à 36 heures. Vous recevrez un e-mail de mise à jour lorsque la recommandation aura été formée avec succès ou une explication sur les raisons de l'échec de la création.

Vous trouverez la recommandation sur la page des **prédictions**, où vous pourrez ensuite la modifier ou l'archiver si nécessaire. Les recommandations seront automatiquement recyclées une fois par semaine (payant) ou par mois (gratuit).