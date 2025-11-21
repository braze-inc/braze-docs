---
nav_title: FAQ
article_title: Questions fréquemment posées
page_order: 12
description: "Cet article fournit des réponses aux questions fréquemment posées sur Liquid."

---

# Questions fréquemment posées

> Sur cette page, vous trouverez des réponses à certaines questions fréquemment posées sur Liquid.<br><br>Braze ne prend actuellement pas en charge 100 % du liquide de Shopify, mais seulement certaines parties que nous avons tenté de présenter dans notre documentation. Nous vous recommandons vivement de tester tous les messages utilisant Liquid avant de les envoyer afin de réduire le risque d'erreurs ou d'utilisation de Liquid non pris en charge.

### Comment utiliser les extraits de code liquides dans Braze ?

Dans de nombreux cas, vous pouvez incorporer des extraits Liquid en naviguant vers vos campagnes ou Canvas, et en insérant Liquid dans la fenêtre modale/boîte de personnalisation dans des zones telles que le corps du message de l'e-mail ou dans vos segments. 

#### Où puis-je en savoir plus ?

Pour en savoir plus sur Liquid, consultez notre parcours d'apprentissage guidé [La personnalisation dynamique avec Liquid Braze](https://learning.braze.com/path/dynamic-personalization-with-liquid)! Vous pouvez également vous référer à la [bibliothèque de cas d'utilisation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) pour trouver l'inspiration et une série d'exemples de personnalisation à l'aide de Liquid.

### Quelle est la différence entre l'utilisation du contenu liquide et du contenu connecté pour la personnalisation ?

Le contenu connecté de Braze est un exemple d'étiquette Liquid. Elles sont également utilisées pour la personnalisation, mais ces données proviennent d'un endpoint externe plutôt que de données stockées au sein de Braze. Consultez notre section dédiée au [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) pour en savoir plus sur l'élargissement de la personnalisation de vos messages.

### Qu'est-ce que le "Liquid Templating" ?

C'est la façon la plus courante d'utiliser le liquide dans la Braze. Le "Liquid Templating" consiste à intégrer dans un message des données provenant du profil d'un utilisateur. Ces données peuvent aller du prénom d'un utilisateur aux événements personnalisés d'un message déclenché par un événement.

Reportez-vous à la section [Étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pour obtenir la liste complète des étiquettes Liquid prises en charge.

### Comment affecter des variables avec Liquid ?

Vous pouvez créer et affecter des variables en utilisant l'étiquette `assign`. Cela crée une variable dans le compositeur du message qui peut également être référencée dans votre message.

### L'utilisation de Liquid permet-elle d'enregistrer des points de données ?

Non.

### Comment puis-je utiliser Liquid pour envoyer un message d'accueil personnalisé ?

Pour un message d'accueil personnalisé utilisant le prénom de l'utilisateur, vous pouvez utiliser les attributs du profil utilisateur standard tels que {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

Vous pouvez également utiliser une instruction Liquid `{% if X %}` {% endraw %}pour effectuer un rendu conditionnel basé sur n'importe quoi, comme le jour de la semaine ou des attributs personnalisés. Pour plus d'informations sur les opérateurs Liquid pris en charge et pouvant être utilisés dans les instructions conditionnelles, consultez la rubrique [Opérateurs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### Comment puis-je personnaliser un message en fonction de l'emplacement/localisation d'un client ?

{% raw %}
Il existe un attribut par défaut pour l'emplacement/localisation de l'utilisateur : `{{${most_recent_location}}}`.

### Quelle est la différence entre {{campaign.${name}}} et {{campaign.${message_name}}} ?

Les étiquettes de personnalisation liquide `{{campaign.${name}}}` et `{{campaign.${message_name}}}` sont toutes deux prises en charge. Les deux tags font référence aux attributs de la campagne. `{{campaign.${name}}}` indique le nom de votre campagne, et `{{campaign.${message_name}}}` le nom de votre variante de message.
{% endraw %}

### Comment utiliser Liquid avec des objets imbriqués ?

Braze dispose d'une fonctionnalité intégrée qui génère le code Liquid pour les segments pouvant être utilisés dans un message. Plus précisément, vous pouvez créer une segmentation qui correspond à plusieurs critères d'un objet.

Pour en savoir plus, consultez la rubrique [Segmentation multicritères]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Comment utiliser les attributs d'événement pour personnaliser un message déclenché par un événement ?

{% raw %}
Vous pouvez accéder aux propriétés des événements déclenchés par l'API à l'aide de l'étiquette `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### Qu'est-ce que la logique d'abandon et comment puis-je l'utiliser ?

La logique conditionnelle vous permet d'interrompre l'envoi d'un message si les conditions sont remplies. Cela permet notamment d'éviter l'envoi de messages incomplets à vos utilisateurs. Pour des exemples de logique d'abandon dans vos campagnes de communication, lisez la rubrique [Abandonner les messages.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)

### Qu'est-ce que la logique de la boucle for et comment puis-je l'utiliser ?

Les boucles "for" sont également connues sous le nom d'[étiquettes d'itération](https://shopify.github.io/liquid/tags/iteration/). L'utilisation de la logique for loop dans vos extraits liquid vous permet de faire défiler des blocs de Liquid jusqu'à ce qu'une condition soit remplie. 

Dans Braze, cela pourrait être utilisé pour vérifier les éléments d'un attribut personnalisé de type tableau, ou une liste de valeurs et d'objets renvoyés par un [catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), une [sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) ou une réponse à un appel de [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Plus précisément, vous pouvez utiliser la logique de la boucle for dans le cadre de votre envoi de messages pour vérifier si un produit est en stock, ou si un produit a une cote minimale. 

Par exemple, disons que vous avez un catalogue appelé "Jeux" dont la sélection s'appelle "cheap_games".. Pour extraire les titres des jeux contenus dans "cheap_games",, vous pourriez utiliser cet extrait de code liquide :

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Une fois que les conditions fixées sont remplies, votre message peut être transmis. L'utilisation de cette logique est un moyen utile d'enregistrer du temps, au lieu de répéter les blocs Liquid pour différentes conditions.
