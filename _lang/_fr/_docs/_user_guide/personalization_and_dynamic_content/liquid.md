---
nav_title: Liquide
article_title: Liquide
page_order: 0
layout: en vedette
guide_top_header: "Personnalisation en utilisant des balises Liquid"
guide_top_text: "Braze peut automatiquement remplacer les valeurs d'un utilisateur donné dans vos messages. Placez votre expression entre deux ensembles de parenthèses pour avertir Braze que vous utiliserez une valeur interpolée. À l'intérieur de ces accolades, toute valeur utilisateur que vous voulez remplacer doit être entourée d'un ensemble de parenthèses supplémentaires avec un signe dollar devant eux.<br><br>Pour en savoir plus sur Liquid, consultez notre guide <b><a href='https://lab.braze.com/dynamic-personalization-with-liquid'>Personnalisation dynamique avec cours Liquid</a></b> LAB !"
description: "Braze peut automatiquement remplacer les valeurs d'un utilisateur donné dans vos messages. Placez votre expression entre deux ensembles de parenthèses pour avertir Braze que vous utiliserez une valeur interpolée."
guide_featured_title: "Articles de la section"
guide_featured_list:
  - 
    name: Utilisation de Liquid
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
    fa_icon: fas fa-flask
  - 
    name: Tags de personnalisation pris en charge
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
    fa_icon: fas fa-tag
  - 
    name: Opérateurs
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquidation/operators/
    fa_icon: fas fa-code
  - 
    name: Filtres
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquid/filters/
    fa_icon: filtre Fas Fas
  - 
    name: Filtres avancés
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
    fa_icon: fas fa-cog
  - 
    name: Réglage des valeurs par défaut
    link: /fr/docs/user_guide/personnalisation_and_dynamic_content/liquid/setting_default_values/
    fa_icon: fas fa-table
  - 
    name: Logique de la messagerie conditionnelle
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquidation/conditional_logic/
    fa_icon: fas fa-columns
  - 
    name: Abandon des messages
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
    fa_icon: fas fa-undo
  - 
    name: Cas d'utilisation des liquides
    link: /fr/docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
    fa_icon: fas fa-list-ul
---

## À propos de Liquid

Les messages de campagne prennent en charge les messages tempérés en utilisant le langage de template Liquid. Pour plus d'informations sur la syntaxe et l'utilisation de Liquid, reportez-vous aux balises de personnalisation [**prises en charge**][1].

Le langage de template Liquid supporte l'utilisation d'objets, de balises et de filtres.

- [**Objets**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) vous permettent d'insérer des attributs personnalisés dans vos messages.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) vous permettent d'exécuter la logique de programmation dans vos messages. Par exemple, vous pouvez utiliser des balises pour inclure une logique intelligente, comme des instructions "si", dans vos campagnes.
- [**Filtres**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) vous permettent de reformater les attributs personnalisés et le contenu dynamique. Par exemple, vous pouvez convertir un horodatage, comme *2016-09-07 08:43:50 UTC* en une date telle que *7 septembre 2016*.

## Termes à connaître

Ces termes sont réinterprétés à partir de la documentation de [**Shopify**](https://shopify.github.io/liquid/basics/introduction/) en fonction de notre niveau de support.

{% alert warning %}

Braze ne prend actuellement pas en charge 100% de Shopify's Liquid, seulement certaines parties que nous avons tenté de décrire dans notre documentation. Nous vous recommandons fortement de tester tous les messages utilisant Liquid avant d'envoyer pour réduire les risques d'erreurs ou d'utiliser Liquid non pris en charge.

{% endalert %}

{% raw %}

| Condition                           | Définition                                                                                                                                                                                                                                                                                                        | Exemple                                                                                                                                                                                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Liquide                             | Un langage de modèle open-source, orienté client créé par Shopify et écrit en Ruby; utilisé pour charger/extraire du contenu dynamique.                                                                                                                                                                           | `{{${first_name}}}` va insérer le prénom d'un utilisateur dans un message.                                                                                                                                                                                  |
| Objet                               | Désignation d'une variable et de l'emplacement du nom de variable voulue qui indique à Liquid où afficher le contenu du message.                                                                                                                                                                                  | `{{${first_name}}}` va insérer le prénom d'un utilisateur dans un message.                                                                                                                                                                                  |
| Étiquette de logique conditionnelle | Les balises créent une logique et contrôlent le flux des modèles. Dans le cas de Brase, les Tags logiques conditionnels sont liquides utilisés pour considérer la logique intelligente ou de programmation pour créer des exceptions et des variations dans les messages basés sur certains, critères prédéfinis. | `{% if ${language} == 'en' %}` déclenchera votre message de manière désignée dans le cas où un utilisateur aurait désigné "Français" comme sa langue.                                                                                                       |
| Filtres                             | Utilisé pour modifier, rétrécir ou reformater la sortie de l'objet Liquid. Il est souvent utilisé pour créer des opérations mathématiques.                                                                                                                                                                        | `{{"Big Sale" | upcase}}` fera apparaître les mots "Big Sale" dans le message.                                                                                                                                                                              |
| Opérateurs                          | Utilisé dans les messages pour créer des dépendances ou des critères qui peuvent affecter quel message reçoit votre utilisateur.                                                                                                                                                                                  | Est qu'un utilisateur répond aux critères définis dans un message taggé avec `{% custom_attribute.${Total_Revenue} > 0%}`, il recevra le message. Dans le cas contraire, ils recevront un autre message désigné (ou pas), selon ce que vous avez défini. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
