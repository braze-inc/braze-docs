---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: featured

guide_top_header: "Personnalisation à l’aide des Balise Liquids"
guide_top_text: "Braze peut automatiquement remplacer les valeurs d’un utilisateur donné dans vos messages. Placez votre expression à l’intérieur de deux ensembles de parenthèses courbes pour notifier Braze que vous utiliserez une valeur interpolée. À l’intérieur de ces parenthèses, toutes les valeurs d’utilisateur que vous souhaitez remplacer doivent être entourées d’un ensemble supplémentaire de parenthèses précédées d’un signe dollar.<br><br>Pour en savoir plus sur Liquid, consultez notre guide <b><a href='https://learning.braze.com/dynamic-personalization-with-liquid'>Personnalisation dynamique avec liquide</a></b> Le cours d’apprentissage Braze !"
description: "Braze peut automatiquement remplacer les valeurs d’un utilisateur donné dans vos messages. Placez votre expression à l’intérieur de deux ensembles de parenthèses courbes pour notifier Braze que vous utiliserez une valeur interpolée."

guide_featured_title: "Section Articles"
guide_featured_list:
- name: Utilisation de Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  fa_icon: fas fa-flask
- name: Balises de personnalisation prises en charge
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  fa_icon: fas fa-tag
- name: Opérateurs
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  fa_icon: fas fa-code
- name: Filtres
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  fa_icon: fas fa-filter
- name: Filtres avancés
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  fa_icon: fas fa-cog
- name: Paramétrage des valeurs par défaut
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  fa_icon: fas fa-table
- name: Logique de messagerie conditionnelle
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  fa_icon: fas fa-columns
- name: Abandon des messages
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  fa_icon: fas fa-undo
- name: Scénarios d’utilisation de Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  fa_icon: fas fa-list-ul
---

## À propos de Liquid

Les messages de campagne prennent en charge des modèles de message en utilisant le langage des modèles de Liquid. Pour plus d’informations sur la syntaxe et l’utilisation de Liquid, consultez les [**Balises de personnalisation prises en charge**][1].

Le langage de modèle de Liquid prend en charge l’utilisation d’objets, de balises et de filtres.

- [**Objets**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) vous permet d’insérer des attributs personnalisés dans vos messages.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) vous permet d’exécuter la logique de programmation dans vos messages. Par exemple, vous pouvez utiliser des balises pour inclure une logique intelligente, telle que des énoncés « si », dans vos campagnes.
- [**Filtres**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) vous permet de reformater les attributs personnalisés et le contenu dynamique. Par exemple, vous pouvez convertir un horodatage, comme *2016-09-07 08 :43 :50 UTC* en une date telle que *7 septembre 2016*.

## Termes à connaître

Ces termes sont réinterprétés à partir de la [**Documentation de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en fonction de notre niveau de compatibilité.

{% alert warning %}

Braze ne prend pas actuellement en charge 100 % de Liquid de Shopify, mais seulement certaines parties que nous avons tenté de présenter dans notre documentation. Nous recommandons vivement de tester tous les messages avec Liquid avant d’envoyer pour réduire le risque d’erreurs ou d’utiliser des parties de Liquid non prises en charge.

{% endalert %}

{% raw %}

| Terme | Définition | Par exemple : |  
|---|---|---|
| Liquid | Un langage modèle en open source et orienté client créé par Shopify et écrit dans Ruby ; utilisé pour charger/tirer du contenu dynamique. | `{{${first_name}}}` insérera le prénom d’un utilisateur dans un message. |
| Objet | Dénotation d’une variable et d’un emplacement du nom de variable prévu qui indique à Liquid où afficher le contenu dans le message. | `{{${first_name}}}` insérera le prénom d’un utilisateur dans un message. |
| Logique conditionnelle (Balise) | Les balises créent une logique et contrôlent le flux pour les modèles. Dans le cas de Braze, les balises logiques conditionnelles sont des Liquid utilisés pour envisager une logique de programmation ou intelligente afin de créer des exceptions et des variations dans des messages reposant sur certains critères prédéfinis. | ```{% if ${language} == 'en' %}``` déclenchera votre message de manière désignée dans le cas où un utilisateur a désigné « Anglais » comme langue. |
| Filtres | Servient à modifier, affiner ou reformater la sortie de l’Objet Liquid. Il est souvent utilisé pour créer des opérations mathématiques. |  ```{{"Big Sale" | upcase}}``` affiche les mots « Soldes importantes » sous la forme de « SOLDES IMPORTANTES » dans le message. |
| Opérateurs | Utilisé dans les messages pour créer des dépendances ou des critères qui peuvent affecter le message reçu par votre utilisateur. | Si un utilisateur répond aux critères définis dans un marqueur marqué avec `{% custom_attribute.${Total_Revenue} > 0%}`, il recevra le message. Sinon, il recevra un autre message désigné (ou non), selon ce que vous avez défini. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
