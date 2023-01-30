---
nav_title: Métadonnées des documents
page_order: 0
noindex: true
---
# Métadonnées des documents

> Cet article présente les différentes options permettant d’ajouter des métadonnées dans des pages de documents. Notre recherche est optimisée en fonction du type de page et d’autres métadonnées, y compris : les [balises YAML](#yaml-tags) et les [types de pages](#page-types) (basés sur des [modèles]({{site.baseurl}}/home/templates/)).

{% alert important %}

Les [balises de contenu](#content-tags) listées sur cette page sont en cours de développement et entraîneront des erreurs si elles sont ajoutées sur des pages. Revenez plus tard pour découvrir la version finale dès que les balises pourront être utilisées en toute sécurité ! Notez que vous **pouvez** utiliser la balise de contenu `platform`.

{% endalert %}

## Balises YAML

Ces balises sont indépendantes. Si vous avez besoin de consulter du contenu YAML supplémentaire (optionnel) en fonction de la « mise en page », consultez les [modèles]({{site.baseurl}}/home/templates/) et mises en page (à déterminer).

{% alert important %}
Concernant les majuscules… 
<br> 
<br> 
Laissez toutes les valeurs des balises en minuscules (à l’exception du contenu de la balise `description`). Cela permet de maintenir la cohérence des balises. Nous changerons peut-être cela à l’avenir, mais, pour l’instant, les minuscules sont plus efficaces pour effectuer des recherches et remplacements en masse en cas de modification de la mise en page.
{% endalert %}

### Balises de configuration

Ces balises modifieront automatiquement la mise en page ou la fonction d’une page.

| Balise de contenu YAML | Description | Requis ? | Type de données | Valeurs disponibles |
| ----------------- | ----------- | --------- | -------------------- |
| `nav_title` | Il s’agit du titre de l’article qui apparaîtra dans le menu de gauche du site des documents. Encapsulé dans des guillemets. | Oui, à moins que la page ne soit `hidden`. | Chaîne de caractères. | N’importe lequel. C’est à vous de choisir le titre de la page. La longueur recommandée est de moins de 30 caractères, espaces compris. |
| `page_order` | Il s’agit de l’ordre dans lequel l’article apparaîtra dans la barre de navigation de gauche du site de la documentation. | Oui, à moins que la page ne soit masquée. | Entier. | N’importe quel chiffre (avec plusieurs décimales) compris entre `1` et `100`. Vous pouvez aussi utiliser `1.1`, `1.2`, `1.3`, etc. pour organiser les pages.|
| `hidden` | Indique si la page sera visible ou non dans la barre de navigation de gauche. Si cette valeur est définie sur `false`, la page n’apparaîtra pas dans les résultats de la recherche (à la fois sur le site et sur les moteurs de recherche en ligne). | Non. | Booléen. | Vous pouvez choisir entre `true` et `false`. |
| `config_only` | Indique si une page agira en tant que page ou en tant que catégorie dans le panneau de navigation de gauche. Par défaut, `false`. .| Non. |  Booléen. | Vous pouvez choisir entre `true` et `false`. |
| `permalink` | Définit l’URL de la page. Par exemple : `permalink: /this_page_name/` définira `https://www.braze.com/docs/this_page_name/`.  en tant qu’URL de la page| Non, à moins que la page ne soit `hidden`. | Chaîne de caractères. | N’importe laquelle. Vous pouvez choisir cette URL. Encapsulée dans des barres obliques (`/`). |
| `layout` | Définit des fonctionnalités spécifiques sur la page, en accord avec les mises en page que vous avez créées. La page par défaut est une page standard. | Non. | Chaîne de caractères. | Si vous ne configurez pas la page, elle sera définie par défaut en tant que page de contenu standard. Vous pouvez choisir entre `api_page`, `dev_guide`, `featured_video`, `featured`, `glossary_page`, `blank_config` et `redirect`. Il existe d’autres types de pages, mais ceux-ci sont principalement utilisés à des fins internes ou pour effectuer des configurations. |
| `hide_toc` | Détermine si la table des matières située sur le côté droit de la page est incluse ou non. | Non. | Booléen. | Vous pouvez choisir entre `true` et `false`. |
| `noindex` | Détermine si l’article apparaîtra dans Algolia et les recherches Google. Définie comme `false` par défaut, à moins que vous ayez défini l’ensemble de balises YAML `hidden` comme étant `true`. | Non. | Booléen. | `true` ou `false`. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Balises de contenu
Ces balises sont utiles pour le SEO interne et externe. Elles fournissent des informations sur le contenu et le formatage des pages ainsi que d’autres structures de contenu.

| Balise de contenu YAML | Description  | Requis ? | Peut-on utiliser plusieurs balises ou une seule uniquement ? | Type de données | Valeurs disponibles |
| ----------------- | ----------- | --------- | ---------------------------------- | --------- | ---------------- |
| `description` | La description de cette page qui apparaîtra dans les résultats de recherche en ligne. Encapsulé dans des guillemets. | Oui. | Si une seule balise est utilisée, la longueur maximale est de 160 caractères. | Chaîne de caractères. | N’importe laquelle. Vous pouvez choisir la description des pages. Nous recommandons d’écrire moins de trois phrases. <br> <br> Modèle : `Ce {type_de_page} {répertorie, décrit, vous guidera dans} {le sujet ou la tâche} dans l'utilisation de {l'outil} pour {plateforme et/ou canal}` Bien que la formulation puisse varier, elle doit indiquer au minimum le type de la page, la finalité de la page (par ex., « cet article vous explique comment effectuer une tâche X / comment lire un certain rapport / quelles sont les exigences relatives à l’intégration du partenaire X. »). <br> <br> Exemple : `This glossary lists all of the terms you need to know while onboarding with Braze and preparing for the Integration Phase.` Ou `Cet article de référence décrit les différents types de Canvas Step et leur influence sur les campagnes de notifications push iOS ou Android`, voire `Cet article de solutions vous guidera dans l'intégration personnalisée.`[`Retrait en magasin`]|
| `page_type` | Le type de page, qui est déterminé par les modèles de pages. Il fournit des informations sur le formatage et le contenu. | Oui. | Une seule balise : une seule peut être utilisée par page. | Chaîne de caractères. | Voir [Types de page](#page-types). |
| `platform` | Indique la plateforme (iOS, Android, etc.) à laquelle cet article est associé. | Non, à moins qu’il s’agisse d’une page de guide de développement.  | Plusieurs valeurs peuvent être utilisées. | Chaîne de caractères. | N’importe quelle plateforme que Braze peut intégrer : `iOS`, `Android`, `Web` et `API`, ainsi que n’importe quel SDK wrapper. |
| `channel` | Indique les canaux de communication (notifications push, messages in-app, etc.) avec lesquels cet article est associé. | Non, à moins que le contenu ne mentionne un ou plusieurs canaux spécifiques. | Plusieurs valeurs peuvent être utilisées. | Chaîne de caractères. | N’importe quel canal de communication à travers lequel Braze envoie des messages : `content cards`, `email`, `news feed`, `in-app messages`, `push`, `sms` et `webhooks`.|
| `tool` | Indique les outils d’engagement (Canvas, campagnes, etc.) auxquels l’article est associé. | Oui. | Plusieurs valeurs peuvent être utilisées. | Chaîne de caractères. | N’importe quel outil de Braze : `dashboard`, `docs`, `canvas`, `campaigns`, `segments`, `templates`, `media`, `location`, `currents`, `reports`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Balises à valeurs multiples
Vous remarquerez parfois que la balise de contenu d’une page peut être catégorisée selon plusieurs valeurs (par ex., dans le cas d’un article qui parle à la fois des Canvas et des campagnes, ou qui décrit une intégration personnalisée pour Android et iOS).

Vous pouvez la formater comme suit : 
```
clé :
  - string1
  - string2      
  - string3
  - string4
  - string5
  - string6
```
{% alert important %}
Remarque : il ne peut y avoir qu’une seule valeur `page_type` par page. Une page ne peut pas être à la fois une page de `reference` et une page de `glossary`. Les différents types de pages disponibles sont conçus pour créer des articles précis sur des sujets prédéterminés. 
{% endalert %}

### Échantillon YAML

Le haut de chaque page Markdown doit commencer par une section de YAML pour définir la page.

```html
---
nav_title: "Docs Metadata"
page_order: 0

description: "This page walks through the options for adding metadata to Docs pages. We optimize our search based on page type and other bits of metadata. This is a great resource for contributors via our GitHub page."
page_type: reference
tool: 
  - docs
  - dashboard
---
```


## Types de page

Pour les appliquer, assurez-vous que le paramètre YAML des types de pages est : `page_type:`

Par exemple : `page_type: glossary`

| Type de page <br> <br> Balise de type de page | Description | Modèles disponibles |
| ------------- | ------------- | ------------- |
| Page de glossaire <br> <br> `glossary`| La page de glossaire décrit certains termes ou éléments (indicateurs, termes importants, endpoints API, etc.) pouvant faire l’objet d’une recherche | [Glossaire des codes ou API]({{site.baseurl}}/home/templates/api_glossary/) <br> <br> [Glossaire général]({{site.baseurl}}/home/templates/glossary_test_page/)
| Page de solution <br> <br> `solution` | Il s’agit d’un article de résolution des problèmes ou d’un article présentant des « options » pour aider les utilisateurs à trouver une solution à leur problème ou qui fournit des explications étape par étape pour résoudre ou identifier un problème précis. | [Article d’aide]({{site.baseurl}}/home/templates/help_article_template/) <br> <br> [Article de solution]({{site.baseurl}}/home/templates/solution/) |
| Page de référence <br> <br> `reference` | Ce type d’article permet d’expliquer un concept et regroupe des informations spécifiques sur des processus techniques et le contenu de certains produits. (Canvas Steps, Segmentation, Fonctionnalités de produit spécifiques, etc.). | [Article de référence avec vidéo]({{site.baseurl}}/home/templates/reference_vide/) <br> <br> [Article de référence]({{site.baseurl}}/home/templates/reference/) |
| Page Tutoriel <br> <br> `tutorial` | Une procédure pas-à-pas expliquant un concept instructif. Cette page doit contenir des informations pratiques. Les pages Tutoriel abordent un thème spécifique (par ex., comment créer une campagne, comment créer un Canvas, etc.) Un article abordant des objectifs ou des tâches spécifiques étape par étape pour résoudre un problème en particulier (par ex. : comment cibler un groupe d’utilisateurs, comment segmenter une audience en fonction du lieu, etc.). | [Article de tutoriel avec vidéo]({{site.baseurl}}/home/templates/tutorial_video/) <br> <br> [Article de tutoriel]({{site.baseurl}}/home/templates/tutorial/) <br> <br> [Article de cas d’utilisation avec vidéo]({{site.baseurl}}/home/templates/use_case_video/) <br> <br> [Article de cas d’utilisation]({{site.baseurl}}/home/templates/use_case/) |
| Page d’accueil <br> <br> `landing` | Cette page fournit plusieurs options dans une section donnée, accompagnée d’une description ou d’une présentation de cette section. | [Page d’accueil pour une seule section avec icônes d’immobilisations]({{site.baseurl}}/home/templates/landing_single/) <br> <br> [Page d’accueil pour une seule section avec images]({{site.baseurl}}/home/templates/landing_images/) <br> <br> [Page d’accueil multisection avec icônes d’immobilisations]({{site.baseurl}}/home/templates/landing_multiple/) <br> <br> [Page d’accueil multisection avec images]({{site.baseurl}}/home/templates/landing_multiple_images/)
| Page Partenaire <br> <br> `partner` | Un page qui regroupe plusieurs types de pages mentionnés précédemment en une seule page. Ces pages décrivent un partenaire, les avantages associés à ce partenaire, comment intégrer ce partenaire et utiliser cette intégration, ainsi que les bonnes pratiques d’utilisation de l’intégration. | [Page Partenaire avec vidéo]({{site.baseurl}}/home/templates/partner_page_template_video/) <br> <br> [Page Partenaire]({{site.baseurl}}/home/templates/partner_page_template/) |
| Mises à jour et notes de publication <br> <br> `update` | Une page qui répertorie les mises à jour successives d’un produit ou SDK. Si une seule mise à jour est effectuée sur une grande page ou sur une page décrivant une nouvelle fonctionnalité, celle-ci **ne sera pas** considérée comme une page de `update`. | Voir les pages sur les notes de version et les pages du journal de modifications des SDK. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Type de page possible : Meilleures pratiques 
