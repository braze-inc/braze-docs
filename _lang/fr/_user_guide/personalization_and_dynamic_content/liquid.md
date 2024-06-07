---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "Personnalisation à l’aide des Balise Liquids"
guide_top_text: "Braze peut automatiquement remplacer les valeurs d’un utilisateur donné dans vos messages. Placez votre expression à l’intérieur de deux ensembles de parenthèses courbes pour notifier Braze que vous utiliserez une valeur interpolée. À l’intérieur de ces parenthèses, toutes les valeurs d’utilisateur que vous souhaitez remplacer doivent être entourées d’un ensemble supplémentaire de parenthèses précédées d’un signe dollar.<br><br>Pour en savoir plus sur Liquid, consultez notre cours d’apprentissage Braze guidé <b><a href='https://learning.braze.com/dynamic-personalization-with-liquid'>Personnalisation dynamique avec Liquid</a></b> !"
description: "Cette page d’accueil couvre tout ce qui concerne Liquid, comme les balises de personnalisation prises en charge, les filtres, la configuration des valeurs par défaut, etc."

guide_featured_title: "Section Articles"
guide_featured_list:
- name: Utilisation de Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Balises de personnalisation prises en charge
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
- name: Paramétrage des valeurs par défaut
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: Logique de messagerie conditionnelle
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Abandon des messages
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Scénarios d’utilisation de Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
---

## À propos de Liquid

> Liquid est un langage de modélisation open-source développé par Shopify et écrit en Ruby. Chez Braze, Liquid est utilisé pour modéliser les données d’un profil utilisateur dans des messages. 

Par exemple, vous pouvez extraire un attribut utilisateur d’un profil utilisateur qui est un type de données entières et arrondir cette valeur au nombre entier le plus proche. Pour plus d’informations sur la syntaxe et l’utilisation de Liquid, consultez les [**Balises de personnalisation prises en charge**][1].

Le langage de modélisation Liquid prend en charge l’utilisation d’objets, de balises et de filtres.

- [**Objets**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) vous permet d’insérer des attributs personnalisés dans vos messages.
- Les [**balises**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) vous permettent d’intégrer des données dans les envois de messages et d’utiliser la logique conditionnelle pour envoyer des messages si les conditions de contour sont remplies. Par exemple, vous pouvez utiliser des balises pour inclure une logique intelligente, telle que des énoncés « si », dans vos campagnes.
- [**Filtres**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) vous permet de reformater les attributs personnalisés et le contenu dynamique. Par exemple, vous pouvez convertir un horodatage, comme *2016-09-07 08:43:50 UTC* en une date telle que *7 septembre 2016*.

{% alert warning %}
Braze ne prend pas actuellement en charge 100 % de Liquid de Shopify, mais seulement certaines parties que nous avons tenté de présenter dans notre documentation. Nous recommandons vivement de tester tous les messages utilisant Liquid avant de les envoyer pour réduire le risque d’erreurs ou d’utiliser du Liquid non pris en charge.
{% endalert %}

### Quelles sont les nouveautés de Liquid 5 ?

Braze a mis à jour sa prise en charge de Liquid jusqu’au et y compris **Liquid 5 de Shopify**. 

L’implémentation Liquid prend maintenant en charge les types de balises de personnalisation de la syntaxe et du thème, ainsi que le contrôle des espaces. Pour plus d’informations concernant une balise donnée, rapportez-vous aux [balises de syntaxe]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags) et aux [balises de thème]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#theme-tags). 

Les nouveaux tableaux et filtres mathématiques suivants peuvent être utilisés dans votre Liquid quand vous construisez votre envoi de message.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Rapportez-vous à notre article sur les [Filtres]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) pour obtenir des définitions.

## Termes à connaître

Ces termes sont réinterprétés à partir de la [**Documentation de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en fonction de notre niveau de compatibilité.

{% raw %}

| Terme | Définition | Exemple |  
|---|---|---|
| Liquid | Un langage modèle en open source et orienté client créé par Shopify et écrit dans Ruby ; utilisé pour charger/tirer du contenu dynamique. | `{{${first_name}}}` insérera le prénom d’un utilisateur dans un message. |
| Objet | Dénotation d’une variable et d’un emplacement du nom de variable prévu qui indique à Liquid où afficher le contenu dans le message. | `{{${city}}}` insérera la ville d’un utilisateur dans un message. |
| Logique conditionnelle (balise) | Les balises créent une logique et contrôlent le flux du contenu du message. Dans les cas d’utilisation de Braze, les balises de logique conditionnelle sont utilisées pour créer des exceptions et des variations dans des messages reposant sur certains critères prédéfinis. | ```{% if ${language} == 'en' %}``` déclenchera votre message d’une manière désignée dans le cas où un utilisateur a sélectionné « Anglais » comme langue. |
| Filtres | Permet de modifier, affiner ou reformater la sortie de l’Objet Liquid. Il est souvent utilisé pour créer des opérations mathématiques. | ```{{"Big Sale" | upcase}}``` affiche les mots « Soldes importantes » en majuscules (c.-à-d. « SOLDES IMPORTANTES ») dans le message. |
| Opérateurs | Utilisé dans les messages pour créer des dépendances ou des critères qui peuvent affecter le message reçu par votre utilisateur. | Si un utilisateur répond aux critères définis dans un message marqué avec `{% custom_attribute.${Total_Revenue} > 0%}`, il recevra le message. Sinon, il recevra un autre message désigné (ou non), selon ce que vous avez défini. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
