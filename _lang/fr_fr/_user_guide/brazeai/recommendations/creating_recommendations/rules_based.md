---
nav_title: Recommandations basées sur des règles
article_title: "Création de recommandations d'articles basées sur des règles"
description: "Cet article de référence explique comment créer une recommandation d'article d'intelligence artificielle pour les articles d'un catalogue."
page_order: 2
---

# Créer des recommandations d'articles basées sur des règles

> Apprenez à créer un moteur de recommandation basé sur des règles à partir des articles de votre catalogue.

## À propos des recommandations d'articles basées sur des règles

Un moteur de recommandation basé sur des règles utilise les données des utilisateurs et les informations sur les produits pour suggérer des articles pertinents aux utilisateurs dans les messages. Il utilise [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) et les [catalogues de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) Braze ou le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) pour personnaliser dynamiquement le contenu en fonction du comportement et des attributs de l'utilisateur.

{% alert important %}
Les recommandations basées sur des règles sont fondées sur une logique fixe que vous devez définir manuellement. Cela signifie que vos recommandations ne s'ajusteront pas à l'historique d'achat et aux goûts d'un utilisateur, à moins que vous ne mettiez à jour la logique.<br><br>Pour créer des recommandations personnalisées basées sur l’IA qui s'adaptent automatiquement à l'historique de l'utilisateur, consultez les [recommandations de produits basées sur l’IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
{% endalert %}

## Options du moteur de recommandation

Pour choisir un moteur de recommandation adapté à vos ressources disponibles et à vos cas d'utilisation, reportez-vous à ce tableau de considérations :

<table style="text-align: center;">
  <thead>
    <tr>
      <th>Moteur de recommandation</th>
      <th>Aucun point de données consommé</th>
      <th>Solution sans code</th>
      <th>Pas de liquide avancé</th>
      <th>Mise à jour automatique du flux de produits</th>
      <th>Généré avec Braze UI</th>
      <th>Pas d'hébergement de données ni de résolution des problèmes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Catalogues CSV</strong></td>
      <td>✔</td>
      <td>Oui, si vous utilisez un liquide pré-généré.</td>
      <td>✔</td>
      <td>Oui, si les recommandations ne sont <strong>pas</strong> mises à jour fréquemment.</td>
      <td>✔</td>
      <td>✔</td>
    </tr>
    <tr>
      <td><strong>API de catalogues</strong></td>
      <td>✔</td>
      <td></td>
      <td>✔</td>
      <td>Oui, si les recommandations sont mises à jour toutes les heures.</td>
      <td>✔</td>
      <td>✔</td>
    </tr>
    <tr>
      <td><strong>Contenu connecté</strong></td>
      <td>✔</td>
      <td></td>
      <td></td>
      <td>✔<br>(Recommandations mises à jour en temps réel)</td>
      <td>Oui, s'il est généré en dehors de Braze.</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Liquid</strong></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>✔</td>
      <td>✔</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 role="presentation" }

## Créer un moteur de recommandation

Créez votre moteur de recommandation en utilisant soit un catalogue, soit du contenu connecté :

{% tabs local %}
{% tab utiliser un catalogue %}
Pour créer votre moteur de recommandation à l'aide d'un catalogue :

1. [Créez un catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) de produits.
2. Pour chaque produit, ajoutez une liste de produits recommandés sous forme de caractères séparés par un délimiteur (comme une pipe `|`) dans une colonne nommée « recommandations_produits ».
3. Transmettez au catalogue l'ID du produit pour lequel vous souhaitez trouver des recommandations.
4. Obtenez la valeur `product_recommendations` pour ce produit de catalogue et divisez-la par le délimiteur à l'aide d'un filtre de division Liquid.
5. Renvoyez un ou plusieurs de ces ID au catalogue pour collecter les autres détails du produit.

### Exemple

Imaginons que vous ayez une application de produits diététiques et que vous souhaitiez créer une campagne cartes de contenu qui envoie différentes recettes en fonction de la durée d'inscription d'un utilisateur à votre application. Tout d'abord, créez et téléchargez un catalogue à l'aide d'un fichier CSV comprenant les informations suivantes :

|Champ|Description|
|-----|-----------|
| **id** | Un nombre unique en corrélation avec le nombre de jours écoulés depuis l'inscription de l'utilisateur à votre appli. Par exemple, `3` correspond à trois jours. |
| **type** | La catégorie de recette, telle que `comfort`, `fresh`, et autres. |
| **titre** | Le titre de la carte de contenu qui sera envoyée pour chaque ID, par exemple « Préparer le déjeuner de cette semaine » ou « Taco, parlons-en ». |
| **lien** | Le lien vers l'article de la recette. |
| **image_url** | L'image qui correspond à la recette. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Une fois le catalogue chargé dans Braze, vérifiez l'aperçu d'une série de produits du catalogue pour confirmer que les informations importées sont exactes. Les éléments peuvent être aléatoires dans l'aperçu, mais cela n'affectera pas le résultat du moteur de recommandation.

![Exemple de catalogue en Braze.]({% image_buster /assets/img/recs/catalog_items.png %})

Créez une campagne de cartes de contenu. Dans le compositeur, saisissez la logique Liquid pour déterminer quels utilisateurs doivent recevoir la campagne, ainsi que la recette et l'image à afficher. Dans ce cas d'utilisation, Braze extrait le site `start_date` (ou la date d'inscription) de l'utilisateur et le compare à la date du jour. La différence de jours déterminera la carte de contenu à envoyer.

{% subtabs local %}
{% subtab title %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}
{% endsubtab %}

{% subtab message %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}
{% endsubtab %}

{% subtab image %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

Par exemple :

![Un exemple de message composé à partir d'une campagne de cartes de contenu.]({% image_buster /assets/img/recs/content_card_preview.png %})

Dans la section **Comportement au clic**, entrez la logique Liquid pour savoir où les utilisateurs doivent être redirigés lorsqu'ils cliquent sur la carte de contenu sur les appareils iOS, Android et Web. 

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

Par exemple :

![Un exemple de bloc de comportement au clic dans le compositeur.]({% image_buster /assets/img/recs/on_click_behavior.png %}){: style="max-width:60%;"}<br><br>

Allez dans l'onglet **Test** et sélectionnez **Utilisateur personnalisé** sous **Prévisualiser le message en tant qu'utilisateur**. Saisissez une date dans le champ **Attribut personnalisé** pour prévisualiser la carte de contenu qui serait envoyée à un utilisateur s'étant inscrit à cette date. <br><br>

![Exemple d'attribut personnalisé nommé "start_date".]({% image_buster /assets/img/recs/custom_attributes_test.png %})
{% endtab %}

{% tab l'utilisation du contenu connecté %}
Pour créer votre moteur de recommandation à l'aide du contenu connecté, commencez par créer un nouvel endpoint à l'aide de l'une des méthodes suivantes :

|Option|Description|
|------|-----------|
|**Convertir une feuille de calcul**|Convertissez une feuille de calcul en un endpoint API JSON en utilisant un service comme SheetDP, et prenez note de l'URL API ainsi générée.|
|**Créer un endpoint personnalisé**|Créez, hébergez et entretenez un endpoint interne personnalisé.|
|**Utiliser un moteur tiers** |Utiliser un moteur de recommandation tiers, tel que l'un de nos [partenaires Alloy]({{site.baseurl}}/partners/message_personalization/), notamment [Amazon Personalise]({{site.baseurl}}/partners/amazon_personalize/), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/certona/), [Dynamic Yield]({{site.baseurl}}/partners/dynamic_yield/), et d'autres.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ensuite, utilisez Liquid dans votre message qui appelle votre endpoint pour faire correspondre une valeur d'attribut personnalisé avec le profil d'un utilisateur et obtenir la recommandation correspondante.

{% raw %}
```liquid
{% connected_content YOUR_API_URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

Remplacez les éléments suivants :

| Attribut | Remplacement |
| --- | --- |
|`YOUR_API_URL` | Remplacez par l'URL réelle de votre API. |
|`RECOMMENDED_ITEM_IDS` | Remplacer par le nom réel de votre attribut personnalisé qui contient les ID des éléments recommandés. Cet attribut est censé être une chaîne de caractères d'ID séparés par des points-virgules. |
|`ITEM_ID` | Remplacer par le nom réel de l'attribut dans votre réponse API qui correspond à l'ID de l'élément. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Il s'agit d'un exemple de base que vous devrez peut-être modifier en fonction de vos besoins spécifiques et de la structure de vos données. Pour obtenir des conseils plus détaillés, reportez-vous à la [documentation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou contactez un développeur.
{% endalert %}

### Exemple

Supposons que vous souhaitiez extraire des recommandations de restaurants de la base de données Zomato Restaurants et enregistrer le résultat dans une variable locale appelée `restaurants`. Vous pouvez passer les appels de contenu connecté suivants :

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Supposons ensuite que vous souhaitiez obtenir des recommandations de restaurants en fonction de la ville et du type de nourriture de l'utilisateur. Vous pouvez le faire en insérant dynamiquement les attributs personnalisés pour la ville et le type de nourriture de l'utilisateur au début de l'appel, puis en affectant la valeur de `restaurants` à la variable `city_food.restaurants`.

L'appel au contenu connecté se présente comme suit :

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Si vous souhaitez adapter la réponse pour ne récupérer que le nom et la note du restaurant, vous pouvez ajouter des filtres à la fin de l'appel, comme suit :

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

Enfin, supposons que vous souhaitiez regrouper les recommandations de restaurants en fonction de leur note. Procédez comme suit :

1. Utilisez `assign` afin de créer des tableaux vides pour les catégories d'évaluation « excellent », « très bon » et « bon ».
2. Ajoutez une boucle `for` qui examine l'évaluation de chaque restaurant de la liste. 
- Si une note est "Excellent", ajoutez le nom du restaurant à la chaîne de caractères `excellent_restaurants`, puis ajoutez un caractère * à la fin pour séparer chaque nom de restaurant. 
- Si l'évaluation correspond à « Très bon », ajoutez le nom du restaurant à la chaîne de caractères `very_good_restaurants`, puis ajoutez un caractère * à la fin.
- Si l'évaluation est « Bon », ajoutez le nom du restaurant à la chaîne de caractères `good_restaurants`, puis ajoutez un caractère * à la fin.
3. Limitez le nombre de recommandations de restaurants renvoyées à quatre par catégorie.

Voici à quoi ressemblerait l'appel final :

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

Voir la capture d'écran ci-dessous pour un exemple d'affichage de la réponse sur l'appareil d'un utilisateur.

![Représentation d'une liste de restaurants générée par l'exemple de l'appel final.]({% image_buster /assets/img/recs/sample_response.png %}){: style="max-width:30%;"}
{% endtab %}
{% endtabs %}
