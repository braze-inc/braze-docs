---
nav_title: Recommandations basées sur des règles
article_title: Recommandations basées sur des règles
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "Cet article explique comment créer un moteur de recommandations basé sur des règles qui utilise des catalogues ou du contenu connecté."
tool:
  - Campaigns
  - Canvas

---

# Recommandations basées sur des règles

> Un moteur de recommandation basé sur des règles utilise les données des utilisateurs et les informations sur les produits pour suggérer des articles pertinents aux utilisateurs dans les messages. Il utilise [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) et les [catalogues]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) Braze ou le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) pour personnaliser dynamiquement le contenu en fonction du comportement et des attributs de l'utilisateur.

Pour en savoir plus sur Liquid, les catalogues et le contenu connecté, consultez ces cours d'apprentissage Braze :

- [Recommandations personnalisées par e-mail](https://learning.braze.com/personalized-recommendations-with-email)
- [Personnalisation dynamique avec Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [Principes de base du contenu connecté](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
Les recommandations basées sur des règles sont fondées sur une logique fixe que vous devez définir manuellement. Cela signifie que vos recommandations ne s'ajusteront pas à l'historique d'achat et aux goûts d'un utilisateur, à moins que vous ne mettiez à jour la logique.<br><br>Pour créer des recommandations personnalisées basées sur l’IA qui s'adaptent automatiquement à l'historique de l'utilisateur, consultez les [recommandations de produits basées sur l’IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
{% endalert %}

## Création d'un moteur de recommandation de catalogues

1. [Créez un catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) de produits.
2. Pour chaque produit, ajoutez une liste de produits recommandés sous forme de caractères séparés par un délimiteur (comme une pipe `|`) dans une colonne nommée « recommandations_produits ».
3. Transmettez au catalogue l'ID du produit pour lequel vous souhaitez trouver des recommandations.
4. Obtenez la valeur `product_recommendations` pour ce produit de catalogue et divisez-la par le délimiteur à l'aide d'un filtre de division Liquid.
5. Renvoyez un ou plusieurs de ces ID au catalogue pour collecter les autres détails du produit.

### Cas d'utilisation des catalogues

Imaginons que vous ayez une application de produits diététiques et que vous souhaitiez créer une campagne cartes de contenu qui envoie différentes recettes en fonction de la durée d'inscription d'un utilisateur à votre application. 

1. Créez et téléchargez un catalogue au format CSV contenant les informations suivantes :<br>- **ID :** Un nombre unique en corrélation avec le nombre de jours écoulés depuis l'inscription de l'utilisateur à votre appli. Par exemple, `3` correspond à trois jours.<br>- **type :** La catégorie de recette, telle que `comfort`, `fresh`, et autres.<br>- **titre :** Le titre de la carte de contenu qui sera envoyée pour chaque ID, par exemple « Préparer le déjeuner de cette semaine » ou « Taco, parlons-en ».<br>- **lien :** Le lien vers l'article de la recette.<br>- **image_url :** L'image qui correspond à la recette.

{: start="2"}
2\. Une fois le catalogue chargé dans Braze, vérifiez l'aperçu d'une série de produits du catalogue pour confirmer que les informations importées sont exactes. Les éléments peuvent être aléatoires dans l'aperçu, mais cela n'affectera pas le résultat du moteur de recommandation.

![][1]

{: start="3"}
3\. Créez une campagne de cartes de contenu. Dans le compositeur, saisissez la logique Liquid pour déterminer quels utilisateurs doivent recevoir la campagne, ainsi que la recette et l'image à afficher. Dans ce cas d'utilisation, Braze extrait le site `start_date` (ou la date d'inscription) de l'utilisateur et le compare à la date du jour. La différence de jours déterminera la carte de contenu à envoyer. 

![][2]

**Titre :**

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

**Message :**

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

**Image :**

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

{: start="4"}
4\. Dans la section **Comportement au clic**, entrez la logique Liquid pour savoir où les utilisateurs doivent être redirigés lorsqu'ils cliquent sur la carte de contenu sur les appareils iOS, Android et Web. 

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

![][3]{: style="max-width:60%;"}<br><br>

{: start="5"}
5\. Allez dans l'onglet **Test** et sélectionnez **Utilisateur personnalisé** sous **Prévisualiser le message en tant qu'utilisateur**. Saisissez une date dans le champ **Attribut personnalisé** pour prévisualiser la carte de contenu qui serait envoyée à un utilisateur s'étant inscrit à cette date. <br><br>

![][4]

## Création d'un moteur de recommandation pour le contenu connecté

1. Créez un endpoint de contenu connecté de l'une des manières suivantes :
- Convertissez une feuille de calcul en un endpoint API JSON en utilisant un service tel que SheetDP, et prenez note de l'URL API ainsi générée.
- Créez, hébergez et gérez un endpoint personnalisé en interne.
- Acheter un moteur de recommandations via un partenaire tiers, tel que l'un de nos [partenaires Alloy]({{site.baseurl}}/partners/message_personalization/dynamic_content/), notamment [Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/), [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) et autres.

2. Rédigez un contenu connecté dans le corps du message ou dans l'éditeur HTML du bloc contenu qui appellera votre endpoint pour effectuer une recherche dans votre base de données.
3. Aligner le liquide sur une valeur d'attribut personnalisé trouvée dans le profil d'un utilisateur donné.
4. Extrayez la bonne recommandation en conséquence.

{% raw %}
```
{% connected_content YOUR-API-URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

| Attribut | Remplacement |
| --- | --- |
|`YOUR-API-URL` | Remplacez par l'URL réelle de votre API. |
|`RECOMMENDED_ITEM_IDS` | Remplacer par le nom réel de votre attribut personnalisé qui contient les ID des éléments recommandés. Cet attribut est censé être une chaîne de caractères d'ID séparés par des points-virgules. |
|`ITEM_ID` | Remplacer par le nom réel de l'attribut dans votre réponse API qui correspond à l'ID de l'élément. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Il s'agit d'un exemple de base que vous devrez peut-être modifier en fonction de vos besoins spécifiques et de la structure de vos données. Pour obtenir des conseils plus détaillés, reportez-vous à la [documentation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou contactez un développeur.
{% endalert %}

## Cas d'utilisation du contenu connecté

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

![][5]{: style="max-width:30%;"}

## Considérations

Pour choisir un moteur de recommandation adapté à vos ressources disponibles et à vos cas d'utilisation, reportez-vous à ce tableau de considérations :

| Considérations | Liquid | Catalogues CSV | API de catalogues | Contenu connecté |
| --- | --- | --- | --- | --- |
| Ne consomme pas de points de données | Non pris en charge | Pris en charge | Pris en charge | Pris en charge |
| Pas de solution de code | Non pris en charge | Pris en charge si Liquid pré-généré | Non pris en charge | Non pris en charge |
| Liquid avancé souvent requis | Pris en charge | Non pris en charge | Non pris en charge | Pris en charge |
| Mises à jour des données dans le flux de produits | Non pris en charge | Soutenu si les recommandations ne sont pas souvent mises à jour | Pris en charge si les recommandations sont mises à jour toutes les heures. | Pris en charge si les recommandations sont mises à jour en temps réel |
| Générer des recommandations dans l'interface utilisateur de Braze | Pris en charge | Pris en charge | Pris en charge | Non pris en charge s'il est généré en dehors de Braze |
| Aucune donnée de recommandation pour l’hébergement, la gestion et la résolution des problèmes | Pris en charge | Pris en charge | Pris en charge | Non pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}