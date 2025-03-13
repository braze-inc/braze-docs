---
nav_title: Recommandations produit basées sur l’IA
article_title: Recommandations produit basées sur l’IA
page_order: 15
alias: "/ai_item_recommendations/"
description: "Cet article de référence explique comment créer une recommandation d'article d'intelligence artificielle pour les articles d'un catalogue."
---

# Recommandations de produits basées sur l’IA

> Découvrez comment créer une recommandation de produits avec l’IA pour les articles d'un catalogue.

Utilisez les recommandations de produits avec l’IA pour calculer les produits les plus populaires ou générer des recommandations personnalisées basées sur l’IA pour un [catalogue][catalogue] spécifique. Après avoir créé votre recommandation, vous pouvez utiliser la personnalisation pour insérer ces produits dans vos messages.

## Conditions préalables

Avant de commencer, vous devrez effectuer les opérations suivantes :

- Vous devez disposer d’au moins un [catalogue][catalogue] pour utiliser l'un des types de recommandations décrits ci-dessous.
- Vous devez disposer de données d'achat ou d'événement sur Braze (événements personnalisés ou objet d'achat) qui incluent une référence à des ID de produits uniques stockés dans un catalogue.

{% alert tip %}
Les [recommandations personnalisées par intelligence artificielle](#recommendation-types) fonctionnent mieux avec des centaines ou des milliers d'articles et généralement au moins 30 000 utilisateurs avec des données d'achat ou d'interaction. Il s'agit d'une indication approximative qui peut varier. Les autres types de recommandations peuvent fonctionner avec moins de données.
{% endalert %}

## Création d'une recommandation d'article par l'intelligence artificielle

Pour créer une recommandation d'article :

1. Sélectionnez **Analyse** > **Recommandation de produits avec l’IA**.
2. Sélectionnez **Créer une prédiction** > **Recommandation d'élément d'intelligence artificielle**.

Vous pouvez également choisir de créer une recommandation directement à partir d'un catalogue individuel. Sélectionnez votre catalogue dans la page **Catalogues**, puis sélectionnez **Créer une recommandation**.

### Étape 1 : Ajouter les détails de la recommandation

Donnez à votre recommandation un nom et une description facultative.

![L'étape "Détails de la recommandation" avec les champs nom et description.][1]

### Étape 2 : Définissez votre recommandation {#recommendation-type}

Sélectionnez le type de recommandation. Tous les types de recommandations utilisent les six derniers mois de données d'interaction avec l'article (achat ou événement personnalisé). L'interaction mentionnée ci-dessous se réfère soit à un événement d'achat, soit à un événement personnalisé choisi à l'[étape 3.](#step-3-select-the-interaction-to-drive-recommendations)

- **Les plus populaires :** Calcule jusqu'à 30 produits du catalogue avec lesquels tous les utilisateurs de l'espace de travail interagissent le plus souvent, comme les produits les plus achetés.
- **Les plus récents :** Crée une liste de 30 produits maximum avec lesquels l'utilisateur a interagi le plus récemment.
- **Intelligence artificielle personnalisée :** Utilise des transformateurs, un nouveau type d'apprentissage profond, pour prédire le prochain ensemble le plus probable d'éléments avec lesquels chaque utilisateur interagira. Nous calculons jusqu'à 30 des éléments les plus probables suivants, classés du plus au moins probable. Ce type de recommandation n'utilise pas de grands modèles de langage (LLM) pour combiner vos données avec celles de n'importe quel autre client de Braze.
- **À la mode :** Calcule jusqu'à 30 éléments de l'espace de travail qui ont eu la dynamique positive la plus récente en ce qui concerne les interactions avec les utilisateurs.

{% alert tip %}
Lors de l'utilisation de **Plus récent** ou **Personnalisé par l'intelligence artificielle**, les utilisateurs dont les données sont insuffisantes pour créer des recommandations individualisées recevront les articles **les plus populaires** en guise de solution de repli. La proportion d'utilisateurs recevant la solution de secours **Les plus populaires** est affichée sur la page **Analyse**.
{% endalert %}

#### Étape 2a : Exclure les achats ou interactions antérieurs (facultatif)

Pour éviter de suggérer des articles qu'un utilisateur a déjà achetés ou avec lesquels il a déjà interagi, sélectionnez **Ne pas recommander d'articles avec lesquels les utilisateurs ont déjà interagi.** Cette option n'est disponible que lorsque le **type de** recommandation est défini sur **Intelligence artificielle personnalisée**.

![Étape "Définir votre recommandation" avec "Le plus populaire" comme type et l'option "Ne pas recommander des éléments avec lesquels les utilisateurs ont déjà interagi" sélectionnée.][2-3]

Ce paramètre empêche les messages de réutiliser les éléments qu'un utilisateur a déjà achetés ou avec lesquels il a interagi, à condition que la recommandation ait été mise à jour récemment. Les articles achetés ou ayant fait l'objet d'une interaction entre les mises à jour des recommandations peuvent encore apparaître. Pour la version gratuite des recommandations de produits, les mises à jour sont hebdomadaires. Pour la version pro des recommandations de produits avec l’IA, les mises à jour ont lieu toutes les 24 heures.

Par exemple, lorsque vous utilisez la version pro des recommandations d'articles par intelligence artificielle, si un utilisateur achète quelque chose puis reçoit un e-mail marketing dans les 30 minutes, l'article qu'il vient d'acheter risque de ne pas être exclu de l'e-mail à temps. Toutefois, les messages envoyés après 24 heures ne comporteront pas cet élément.

#### Étape 2b : Sélectionner un catalogue

S'il n'est pas déjà indiqué, sélectionnez le [catalogue][catalogue] à partir duquel cette recommandation va extraire les produits.

#### Étape 2c : Ajouter une sélection (facultatif)

Si vous souhaitez mieux contrôler votre recommandation, choisissez une [sélection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) pour appliquer des filtres personnalisés. Les sélections filtrent les recommandations en fonction de colonnes spécifiques de votre catalogue, telles que la marque, la taille ou l'emplacement/localisation. Les sélections qui contiennent du liquide ne peuvent pas être utilisées dans votre recommandation.

![Exemple de la sélection "en stock" choisie pour la recommandation.][2-2]

{% alert tip %}
Si vous ne trouvez pas votre sélection, vérifiez qu’elle est configurée dans votre catalogue.
{% endalert %}

### Étape 3 : Sélectionnez l'interaction à l'origine des recommandations

Sélectionnez l'événement pour lequel vous souhaitez que cette recommandation soit optimisée. Cet événement est généralement un achat, mais il peut également s'agir de toute interaction avec un article.

Vous pouvez optimiser pour :

- Événements d'achat avec l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Événements personnalisés représentant un achat
- Événements personnalisés qui représentent toute autre interaction avec le produit (comme les consultations de produits, les clics ou les lectures de médias)

Si vous choisissez un **événement personnalisé**, sélectionnez votre événement dans la liste.

![L'événement personnalisé "Achat terminé" a été sélectionné en fonction de la manière dont les événements sont actuellement suivis.][3]

### Étape 4 : Choisissez le nom de la propriété correspondante {#property-name}

Pour créer une recommandation, vous devez indiquer à Braze le champ de votre événement d'interaction (objet d'achat ou événement personnalisé) dont l'identifiant unique correspond au champ `id` d'un article dans le catalogue. Vous avez des doutes ? [Consultez les conditions](#requirements).

Sélectionnez ce champ pour le **nom de la propriété**.

Le champ **Nom de la propriété** sera pré-rempli avec une liste de champs envoyés par le SDK à Braze. Si suffisamment de données sont fournies, ces propriétés seront également classées par ordre de probabilité d'être la propriété correcte. Sélectionnez celle qui correspond au champ `id` du catalogue.

![Le nom de la propriété "purchase_item" sélectionnée qui correspond aux ID des articles dans le catalogue.][4]

#### Conditions {#requirements}

La sélection de votre propriété est soumise à certaines conditions :

- Doit correspondre au champ `id` du catalogue que vous avez sélectionné.
- **Si vous avez sélectionné Objet d'achat :** Doit être le `product_id` ou un champ des `properties` de votre événement d’interaction.
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
    <th class="tg-0pky">id</th>
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
    <td class="tg-0pky">Adidas Rouge pointure 44</td>
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
{% tab Événement personnalisé %}

Imaginons que vous souhaitiez utiliser l'événement personnalisé `added_to_cart` pour pouvoir recommander des produits similaires avant que le client ne passe à la caisse. L'événement `added_to_cart` a pour propriété d'événement `product_sku`.

La propriété `product_sku` doit alors inclure au moins une des valeurs de la colonne `id` du catalogue d’échantillons : "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" ou "ADI-PP-10". Vous n'avez pas besoin d'événements pour chaque produit du catalogue, mais vous avez besoin de certains d'entre eux afin que le moteur de recommandation dispose de suffisamment de contenu pour travailler.

##### Exemple d'objet d'événement personnalisé

Cet événement comporte `"product_sku": "ADI-BL-7"`, ce qui correspond au premier produit du catalogue d'échantillons.

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

Si vos ID de produits sont des valeurs dans un tableau plutôt que des objets, vous pouvez utiliser la même notation et chaque ID de produit sera traité comme un événement distinct et séquentiel. Ceci peut être combiné de manière flexible avec des objets imbriqués dans l'événement suivant en configurant la propriété comme `purchase.product_skus` pour qu'elle corresponde aux premier et troisième articles du catalogue d'exemples.

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
{% tab Objet Achat %}

Un objet d'achat est transmis par l'API lorsqu'un achat a été effectué.

En termes de mappage, la logique est la même pour les objets d'achat que pour les événements personnalisés, à ceci près que vous pouvez choisir d'utiliser le site `product_id` de l'objet d'achat ou un champ de l'objet `properties`.

Rappelez-vous, vous n'avez pas besoin d'événements pour chaque produit du catalogue, mais vous avez besoin de certains d'entre eux afin que le moteur de recommandation dispose de suffisamment de contenu pour travailler.

##### Exemple d'objet d'achat mappé à l'ID du produit

Cet événement comporte `"product_id": "ADI-BL-7`, ce qui correspond au premier produit du catalogue.

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

### Étape 5 : Former la recommandation

Lorsque vous êtes prêt, sélectionnez **Créer une recommandation**. Ce processus peut durer de 10 minutes à 36 heures. Vous recevrez un e-mail lorsque la recommandation aura été entraînée avec succès ou une explication sur les raisons de l'échec de la création.

Vous trouverez la recommandation sur la page des **prédictions**, où vous pourrez ensuite la modifier ou l'archiver si nécessaire. Les recommandations seront automatiquement recyclées une fois par mois.

## Analyse

Vous pouvez consulter l'analyse/analytique de votre recommandation pour voir quels éléments ont été recommandés aux utilisateurs et quelle a été la précision du modèle de recommandation.

1. Allez dans **Analyse/analytique** > **Recommandation d'élément (si utilisé comme adjectif)**.
2. Sélectionnez votre recommandation dans la liste.

En haut de la page, vous trouverez des statistiques sur votre recommandation, telles que la précision et la couverture.

![Les indicateurs d'audience de la recommandation montrent la précision (21,1 %), la couverture (83,0 %) et les types de recommandation répartis entre les articles personnalisés et les articles les plus populaires.][5]

Ces indicateurs sont définis dans le tableau suivant. 

| Indicateur              | Description |
| ------------------- | ---------- |
| Précision           | Le pourcentage de fois où le modèle a correctement deviné le prochain article acheté par un utilisateur. La précision dépend fortement de la taille et du mélange de votre catalogue et doit être utilisée comme un guide pour comprendre à quelle fréquence le modèle est correct.<br><br>Lors de tests antérieurs, nous avons constaté que les modèles fonctionnaient bien, avec une précision allant de 6 à 20 %. Cette métrique est mise à jour lors du prochain recyclage du modèle.  |
| Couverture            | Quel est le pourcentage d'articles disponibles dans le catalogue qui sont recommandés à au moins un utilisateur. Vous pouvez vous attendre à une couverture de produits plus élevée, avec des recommandations de produits personnalisées par rapport aux produits les plus populaires. |
| Type de recommandation | Pourcentage d'utilisateurs qui recevront des recommandations personnalisées ou les plus récentes par rapport à la solution de repli des articles les plus populaires. La solution de repli est envoyée aux utilisateurs qui ne disposent pas de suffisamment de données pour générer une recommandation personnalisée ou la plus récente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La section suivante présente une ventilation des produits du catalogue, divisée en deux colonnes possibles :

- **Produits personnalisés** ou **Produits les plus récents :** Cette colonne répertorie chaque produit du catalogue par ordre décroissant de recommandation aux utilisateurs. Cette colonne indique également le nombre d'utilisateurs auxquels le modèle a attribué chaque élément.
- **Produits les plus populaires :** Cette colonne présente chaque article du catalogue par ordre décroissant de popularité. La popularité fait ici référence aux éléments du catalogue avec lesquels les utilisateurs interagissent le plus souvent dans l'ensemble de l'espace de travail. Le plus populaire est utilisé comme solution de repli lorsque la personnalisation ou le plus récent ne peuvent être calculés pour un utilisateur individuel.

![Tableaux côte à côte répertoriant les éléments attribués aux utilisateurs, séparés par les recommandations personnalisées et les recommandations les plus populaires.][6]

L'**aperçu de la recommandation** présente un résumé de la configuration de la recommandation que vous avez choisie, y compris la date de la dernière mise à jour de la recommandation.

![Tableau d'aperçu des recommandations affichant le type, le catalogue, le type d'événement, le nom de l'événement personnalisé, le nom de la propriété et la date de la dernière mise à jour.][7]{: style="max-width:45%" }

## Utilisation des recommandations dans les messages

![Modale "Ajouter une personnalisation" avec la recommandation d'articles comme type de personnalisation.][10]{: style="max-width:30%;float:right;margin-left:15px;"}

Une fois l’entraînement de votre recommandation terminé, vous pouvez personnaliser vos messages avec Liquid pour y insérer les produits les plus populaires de ce catalogue. Le liquide peut être généré pour vous par la fenêtre de personnalisation qui se trouve dans les compositeurs de messages :

1. Dans tous les compositeurs de messages qui prennent en charge la personnalisation, sélectionnez <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Ajouter une personnalisation"></i> pour ouvrir la fenêtre de personnalisation.
2. Pour le **type de personnalisation**, sélectionnez **Recommandation produit**.
3. Pour **Nom de la recommandation de l'élément**, sélectionnez la recommandation que vous venez de créer.
4. Pour **Nombre de produits prédits**, indiquez le nombre de meilleurs produits que vous souhaitez insérer. Par exemple, vous pouvez afficher les trois produits les plus achetés.
5. Pour les **informations à afficher**, sélectionnez les champs du catalogue à inclure pour chaque article. Les valeurs de ces champs pour chaque article seront tirées du catalogue associé à cette recommandation.
6. Sélectionnez l'icône **Copier** et collez le liquide à l'endroit voulu dans votre message.

## Niveaux de recommandation de produits avec l’IA

Le tableau suivant décrit les différences entre la version gratuite et la version pro des types de recommandation Intelligence artificielle personnalisée, Populaire et Tendance :

| Secteur                   | Version gratuite                          | Version Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Fréquence de mise à jour de l’utilisateur<sup>1</sup>   | Hebdomadaire                                | Tous les jours                                    |
| Fréquence de réentraînement du modèle  | Mensuelle                               | Mensuelle                                   |
| Modèles de recommandation maximale | 1 modèle par <sup>type2</sup> | 100 modèles par <sup>type2</sup> |

<sup>1\. Il s'agit de la fréquence à laquelle les recommandations d'articles spécifiques à l'utilisateur sont mises à jour (tous les modèles à l'exception des articles les plus populaires, qui sont mis à jour lorsque le modèle se réapprend). Par exemple, si un utilisateur achète un produit sur la base des recommandations de produits avec l’IA, ses produits recommandés seront mis à jour selon cette fréquence</sup><br>
<sup>2\. Les types de recommandations disponibles sont les suivants : Intelligence artificielle personnalisée, Plus récent, Plus populaire et Tendance.</sup>

## Foire aux questions

### Qu'est-ce qui fait que les articles les plus populaires sont mélangés aux recommandations d'autres modèles ?

Lorsque notre moteur de recommandation établit une liste pour vous, il donne d'abord la priorité aux sélections personnalisées en fonction du modèle spécifique que vous avez choisi, comme "Plus récent" ou "Personnalisé par l'intelligence artificielle". Si, pour une raison quelconque, ce modèle ne peut pas remplir la liste complète des 30 recommandations, certains de vos articles les plus populaires parmi tous les utilisateurs sont alors ajoutés afin de s'assurer que chaque utilisateur dispose toujours d'un ensemble complet de recommandations.

Cela se produit dans quelques conditions spécifiques :

- Le modèle trouve moins de 30 produits correspondant à vos critères.
- Les articles concernés ne sont plus disponibles ou en stock.
- Les produits ne répondent pas aux critères de sélection actuels, peut-être en raison d'un changement au niveau des stocks ou des préférences de l'utilisateur.

### Les recommandations existantes font-elles l'objet d'une formation hebdomadaire après la mise à niveau vers Item Recommendations Pro ?

Non, les recommandations existantes ne seront pas automatiquement mises à jour pour s'entraîner chaque semaine ou prédire chaque jour après la mise à niveau. Vous pouvez vérifier les prochaines heures d'entraînement et de prédictions dans la section **Recommandation** en sélectionnant une recommandation. Pour les planifications mises à jour, nous vous suggérons de recréer vos recommandations.

[1]: {% image_buster /assets/img/item_recs_1.png %}
[2-1]: {% image_buster /assets/img/item_recs_2-1.png %}
[2-2]: {% image_buster /assets/img/item_recs_2-2.png %}
[2-3]: {% image_buster /assets/img/item_recs_2-3.png %}
[3]: {% image_buster /assets/img/item_recs_3.png %}
[4]: {% image_buster /assets/img/item_recs_4.png %}
[5]: {% image_buster /assets/img/item_recs_analytics_1.png %}
[6]: {% image_buster /assets/img/item_recs_analytics_2.png %}
[7]: {% image_buster /assets/img/item_recs_analytics_3.png %}
[10]: {% image_buster /assets/img/add_personalization.png %}
[catalogue] : {{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/
