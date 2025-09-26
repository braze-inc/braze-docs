---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "Personnalisation à l’aide des Balise Liquids"
guide_top_text: "Braze peut automatiquement remplacer les valeurs d’un utilisateur donné dans vos messages. Placez votre expression à l’intérieur de deux ensembles de parenthèses courbes pour notifier Braze que vous utiliserez une valeur interpolée. À l’intérieur de ces parenthèses, toutes les valeurs d’utilisateur que vous souhaitez remplacer doivent être entourées d’un ensemble supplémentaire de parenthèses précédées d’un signe dollar.<br><br>Pour en savoir plus sur Liquid, consultez notre parcours d’apprentissage guidé Braze <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Personnalisation dynamique avec Liquid</a></b> !"
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
- name: Configuration des valeurs par défaut
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
- name: Tutoriels
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Foire aux questions
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## À propos de Liquid

> Liquid est un langage de modélisation open-source développé par Shopify et écrit en Ruby. Chez Braze, Liquid est utilisé pour modéliser les données d’un profil utilisateur dans des messages. 

Par exemple, vous pouvez extraire un attribut utilisateur d’un profil utilisateur qui est un type de données entières et arrondir cette valeur au nombre entier le plus proche. Pour plus d'informations sur la syntaxe et l'utilisation de Liquid, reportez-vous à la section [**Tags de personnalisation pris en charge**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Le langage de modélisation Liquid prend en charge l’utilisation d’objets, de balises et de filtres.

- [**Les objets**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) vous permettent d'insérer des attributs personnalisés dans vos messages.
- [**Les étiquettes**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) vous permettent d'insérer des données dans les messages et d'utiliser une logique conditionnelle pour envoyer des messages si certaines conditions sont remplies. Par exemple, vous pouvez utiliser des balises pour inclure une logique intelligente, telle que des énoncés « si », dans vos campagnes.
- [**Les filtres**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) vous permettent de reformater les attributs personnalisés et le contenu dynamique. Par exemple, vous pouvez utiliser le [filtre`date` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) pour convertir un horodatage, tel que *2016-09-07 08:43:50 UTC*, en une date, telle que le *7 septembre 2016.*

{% alert warning %}
Braze ne prend actuellement pas en charge 100 % du code Liquid de Shopify, mais seulement certaines parties que nous avons tenté de présenter dans notre documentation. Nous recommandons vivement de tester tous les messages utilisant Liquid avant de les envoyer pour réduire le risque d’erreurs ou d’utiliser du Liquid non pris en charge.
{% endalert %}

### Soutien au Liquid 5

Braze prend en charge Liquid jusqu'à et y compris **Liquid 5 de Shopify**. L'implémentation Liquid prend en charge les types d'étiquettes de personnalisation de la syntaxe, ainsi que le contrôle des espaces. Pour plus d'informations sur des balises spécifiques, reportez-vous aux [balises de syntaxe]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

Les nouveaux tableaux et filtres mathématiques suivants peuvent être utilisés dans votre Liquid quand vous construisez votre envoi de message.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Reportez-vous à la section [Filtres]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) pour les définitions.

### Mises à jour de Liquid

#### Étiquettes de couleur

Chaque élément Liquid correspond à une couleur, ce qui vous permet de différencier votre Liquid d'un coup d'œil dans votre éditeur Liquid.

![]({% image_buster /assets/img/liquid_color_code.png %})

#### Cod Liquid prédictif

Vous pouvez également exploiter le code Liquid prédictif pour les attributs personnalisés, les noms d'attributs et bien d'autres choses encore lorsque vous créez vos messages personnalisés.

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Termes à connaître

Ces termes sont réinterprétés à partir de la documentation de [**documentation de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en fonction de notre niveau d'assistance.

{% raw %}

| Terme | Définition | Exemple |  
|---|---|---|
| Liquid | Un langage de modèle couramment utilisé, orienté vers le client, créé par Shopify et écrit en Ruby, qui est utilisé pour charger et tirer du contenu dynamique. | `{{${first_name}}}` insérera le prénom d’un utilisateur dans un message. |
| Objet | Dénotation d’une variable et d’un emplacement du nom de variable prévu qui indique à Liquid où afficher le contenu dans le message. | `{{${city}}}` insérera la ville d’un utilisateur dans un message. |
| Logique conditionnelle (balise) | Utilisé pour créer une logique et contrôler le flux du contenu du message. Dans Braze, les étiquettes de logique conditionnelle sont utilisées pour créer des exceptions et des variations dans les messages sur la base de certains critères prédéfinis. | ```{% if ${language} == 'en' %}``` déclenchera votre message d’une manière désignée dans le cas où un utilisateur a sélectionné « Anglais » comme langue. |
| Filtres | Permet de modifier, affiner ou reformater la sortie de l’Objet Liquid. Il est souvent utilisé pour créer des opérations mathématiques. | ```{{"Big Sale" | upcase}}``` affiche les mots « Soldes importantes » en majuscules (c.-à-d. « SOLDES IMPORTANTES ») dans le message. |
| Opérateurs | Utilisé dans les messages pour créer des dépendances ou des critères qui peuvent affecter le message reçu par votre utilisateur. | Si un utilisateur répond aux critères définis dans un message marqué avec `{% custom_attribute.${Total_Revenue} > 0%}`, il recevra le message. Sinon, il recevra un autre message désigné (ou non), selon ce que vous avez défini. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

