---
nav_title: Liquide
article_title: Liquide
page_order: 0
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Personnalisation à l'aide d'étiquettes Liquid"
guide_top_text: "Braze peut substituer automatiquement les valeurs d'un utilisateur donné dans vos messages. Placez votre expression à l'intérieur de deux séries de crochets pour indiquer à Braze que vous utiliserez une valeur interpolée. À l'intérieur de ces parenthèses, toute valeur utilisateur que vous souhaitez substituer doit être entourée d'une série supplémentaire de parenthèses précédées d'un signe de dollar.<br><br>Pour en savoir plus sur Liquid, consultez notre guide <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Personnalisation dynamique avec Liquid</a></b> de Braze !"
description: "Cette page d'atterrissage couvre tous les aspects de Liquid, tels que les étiquettes de personnalisation prises en charge, les filtres, la définition des valeurs par défaut, et plus encore."

guide_featured_title: "Articles de section"
guide_featured_list:
- name: Utilisation du liquide
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Tags de personnalisation pris en charge
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: Opérateurs
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: Filtres
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtres avancés
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: Réglage des valeurs par défaut
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: "Logique conditionnelle d'envoi des messages"
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Abandon des messages
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: "Cas d'utilisation des liquides"
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: Tutoriels
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Questions fréquemment posées
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## À propos de Liquid

> Liquid est un langage de template open-source développé par Shopify et écrit en Ruby. Chez Braze, Liquid est utilisé pour modéliser les données du profil d'un utilisateur dans des messages. 

Par exemple, vous pouvez récupérer un attribut personnalisé d'un profil utilisateur qui est une donnée de type entier et arrondir cette valeur au nombre entier le plus proche. Pour plus d'informations sur la syntaxe et l'utilisation de Liquid, reportez-vous à la section [**Tags de personnalisation pris en charge**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Le langage de création de modèles Liquid permet d'utiliser des objets, des étiquettes et des filtres.

- [**Les objets**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) vous permettent d'insérer des attributs personnalisés dans vos messages.
- [**Les étiquettes**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) vous permettent d'insérer des données dans les messages et d'utiliser une logique conditionnelle pour envoyer des messages si certaines conditions sont remplies. Par exemple, vous pouvez utiliser des tags pour inclure une logique intelligente, telle que des instructions "si", dans vos campagnes.
- [**Les filtres**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) vous permettent de reformater les attributs personnalisés et le contenu dynamique. Par exemple, vous pouvez utiliser le [filtre`date` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) pour convertir un horodatage, tel que *2016-09-07 08:43:50 UTC*, en une date, telle que le *7 septembre 2016.*

{% alert warning %}
Braze ne prend actuellement pas en charge 100 % du liquide de Shopify, mais seulement certaines parties que nous avons tenté de présenter dans notre documentation. Nous vous recommandons vivement de tester tous les messages utilisant Liquid avant de les envoyer afin de réduire le risque d'erreurs ou d'utilisation de Liquid non pris en charge.
{% endalert %}

### Soutien au Liquid 5

Braze prend en charge Liquid jusqu'à et y compris **Liquid 5 de Shopify**. L'implémentation Liquid prend en charge les types d'étiquettes de personnalisation de la syntaxe et le contrôle des espaces blancs. Pour plus d'informations sur des tags spécifiques, reportez-vous aux [tags de syntaxe]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

Les nouveaux tableaux et filtres mathématiques suivants sont disponibles pour être utilisés dans votre Liquid lorsque vous créez votre envoi de messages.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Reportez-vous à la section [Filtres]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) pour les définitions.

### Mises à jour des liquides

#### Étiquettes de couleur

Chaque élément Liquid correspond à une couleur, ce qui vous permet de différencier votre Liquid d'un coup d'œil dans votre éditeur Liquid.

\![]({% image_buster /assets/img/liquid_color_code.png %})

#### Liquide prédictif

Vous pouvez également exploiter le liquide prédictif pour les attributs personnalisés, les noms d'attributs et bien d'autres choses encore lorsque vous créez vos messages personnalisés.

\![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Termes à connaître

Ces termes sont réinterprétés à partir de la documentation de [**documentation de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en fonction de notre niveau d'assistance.

{% raw %}

| Durée | Définition | Exemple |  
|---|---|---|
| Liquide | Un langage de modèle couramment utilisé, orienté vers le client, créé par Shopify et écrit en Ruby, qui est utilisé pour charger et tirer du contenu dynamique. | `{{${first_name}}}` insérera le prénom de l'utilisateur dans un message. |
| Objet | Dénomination d'une variable et emplacement/localisation du nom de la variable prévue qui indique à Liquid où afficher le contenu dans le message. | `{{${city}}}` insère la ville d'un utilisateur dans un message. |
| Étiquette de logique conditionnelle | Utilisé pour créer une logique et contrôler le flux du contenu du message. Dans Braze, les étiquettes de logique conditionnelle sont utilisées pour créer des exceptions et des variations dans les messages sur la base de certains critères prédéfinis. | ```{% if ${language} == 'en' %}``` déclenchera votre message d'une manière déterminée dans l'événement où un utilisateur a désigné l'"anglais" comme sa langue. |
| Filtres | Utilisé pour modifier, restreindre ou reformater la sortie de l'objet Liquid. Il est souvent utilisé pour créer des opérations mathématiques. | ```{{"Big Sale" | upcase}}``` fera apparaître les mots "Grande vente" sous la forme "GRANDE VENTE" dans le message. |
| Opérateurs | Utilisé dans les messages pour créer des dépendances ou des critères qui peuvent affecter le message reçu par votre utilisateur. | Si un utilisateur répond aux critères définis dans un message étiqueté avec `{% custom_attribute.${Total_Revenue} > 0%}`, il recevra le message. Si ce n'est pas le cas, ils recevront un autre message désigné (ou non), en fonction de ce que vous avez défini. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

