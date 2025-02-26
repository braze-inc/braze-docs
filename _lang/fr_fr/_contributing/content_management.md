---
nav_title: Gestion du contenu
article: Content Management
description: "Voici un aperçu de la façon dont le contenu est géré sur Braze Docs."
page_order: 2 
noindex: true
---

# A propos de la gestion de contenu

> Voici un aperçu de la façon dont le contenu est géré sur Braze Docs. Pour en savoir plus sur un sujet spécifique, choisis la page thématique dédiée dans la navigation.

## Méthodologie

Braze Docs est géré à l'aide de docs-as-code, une méthode de gestion de la documentation qui reflète le cycle de vie du développement logiciel en utilisant un système de contrôle des versions. Braze Docs utilise le système de contrôle de version Git, qui permet aux contributeurs de travailler sur la même documentation sans écraser le travail des autres. Pour plus d'informations, voir [À propos du contrôle de version et de Git](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git).

![The Braze Docs repository's home page on GitHub.]({% image_buster /assets/img/contributing/github/home_page.png %})

## Générateur de site 

Braze Docs est construit à l'aide de Jekyll, un générateur de site statique populaire qui permet de stocker les fichiers de contenu et les fichiers de conception dans des répertoires distincts, tels que `_docs` pour les fichiers de contenu et `assets` pour les fichiers de conception. Lorsque le site est construit, Jekyll fusionne intelligemment chaque fichier et les stocke sous forme de données XML et HTML dans le répertoire `_site`. Pour plus d'informations, voir [Structure des répertoires de Jekyll](https://jekyllrb.com/docs/structure/).

![The home page for Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

En tant que collaborateur, tu travailleras principalement dans les répertoires suivants.

| Répertoire | Description |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)         | Contient tout le contenu écrit pour Braze Docs sous forme de fichiers texte rédigés en Markdown. Les fichiers texte sont organisés en répertoires et sous-répertoires reflétant le site docs, par exemple `_api` pour la [section API]({{site.baseurl}}/api/home) et `user_guide` pour la [section User Guide]({{site.baseurl}}/user_guide/introduction). |
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes) | Contient des fichiers texte (appelés "includes") qui peuvent être réutilisés dans n'importe quel fichier du répertoire `_docs`. Généralement, les inclusions sont des éléments de contenu courts et modulaires qui n'utilisent pas de formatage standard. Les fichiers stockés à cet emplacement sont importants pour la [réutilisation des contenus](#content-reuse).                                            |
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)       | Contient toutes les images de Braze Docs. Tout fichier texte se trouvant dans le répertoire `_docs` ou `_includes` peut être lié à ce répertoire pour afficher une image sur sa page.                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Pour une démonstration complète, voir [Générer un aperçu]({{site.baseurl}}/contributing/generating_a_preview/).
{% endalert %}

## Pages

Chaque page de Braze Docs est rédigée en syntaxe Markdown et stockée sous forme de fichier Markdown à l'aide de l'extension de fichier `.md`. En haut de chaque fichier Markdown, YAML front matter est utilisé pour ajouter des métadonnées cachées pour chaque page.

\`\`\`markdown
---
METADATA\_KEY : METADATA\_VALUE
---

# CONTENU
\`\`\`

Remplacez les éléments suivants :

| Placeholder | Description |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY` | La clé représentant un type de métadonnées pris en charge. Pour plus d'informations, voir [Métadonnées]({{site.baseurl}}/contributing/yaml_front_matter/metadata/). |
| `METADATA_VALUE` | La valeur attribuée à la clé du type de métadonnées. Pour plus d'informations, voir [Métadonnées]({{site.baseurl}}/contributing/yaml_front_matter/metadata/).  |
| `CONTENT` | Le contenu de la page écrit en syntaxe Markdown.                                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: Contribuer aux documents de Braze
article: Contribution aux documents de Braze
description: "Voici ce dont tu as besoin pour commencer à contribuer à Braze Docs !"
page_order: 0
search_tag: Contribuer
---

# Contribution aux documents de Braze

> Merci de contribuer aux documents de Braze ! Tous les mardis et jeudis, nous fusionnons les contributions de la communauté et les déployons sur Braze Docs. Utilise ce guide pour que tes modifications soient fusionnées lors de notre prochain déploiement.
\`\`\`
{% endtab %}

{% tab example output %}
![Example page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour une présentation complète, voir [Créer une page]({{site.baseurl}}/contributing/content_management/pages/#creating-a-page).
{% endalert %}

## Images

Les images sont stockées sous forme de fichiers PNG à l'intérieur de `assets/img`. La structure du répertoire `img` n'a pas besoin de correspondre à la structure de Braze Docs ; cependant, il est préférable de regrouper les images apparentées dans des sous-répertoires.

Chaque image peut être liée à une ou plusieurs pages à l'aide de la syntaxe suivante.

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

Remplacez les éléments suivants :

| Placeholder | Description |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT` | Le texte alt de l'image. Cela est nécessaire pour s'assurer que Braze Docs est également accessible aux personnes qui utilisent des lecteurs d'écran. |
| `IMAGE` | Le chemin relatif de ton image à partir du répertoire `img`.                                                      |
{: .reset-td-br-1 .reset-td-br-2}

Ton image en ligne devrait ressembler à ce qui suit :

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

{% alert tip %}
Pour une démonstration complète, voir [Ajouter une nouvelle image]({{site.baseurl}}/contributing/content_management/images/#adding-a-new-image).
{% endalert %}

## Sections

Braze Docs est organisé en sections et [sous-sections](#subsections) [principales](#primary-sections).

### Sections primaires

Les principales sections de Braze Docs sont les suivantes :

- [Accueil Braze Docs]({{site.baseurl}})
- [Guide d’utilisation]({{site.baseurl}}/user_guide/introduction)
- [Guide du développeur]({{site.baseurl}}/developer_guide/home)
- [Guide de l’API Braze]({{site.baseurl}}/api/home)
- [Partenaires technologiques]({{site.baseurl}}/partners/home)
- [Aide Braze]({{site.baseurl}}/help/home)
- [Contribution aux documents de Braze]({{site.baseurl}}/contributing/home/)

Outre **Contribuer à Braze Docs**, ces sections principales sont accessibles sur l'en-tête du site à partir de n'importe quelle page de Braze Docs.

![The primary sections as shown on the site header on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/header.png %})

Chaque section primaire est construite à l'aide des [collections Jekyll](https://jekyllrb.com/docs/collections/), qui permettent de regrouper des contenus connexes pour faciliter la gestion. Garde à l'esprit que si toutes les sections primaires sont des collections, toutes les collections ne sont pas des sections primaires. Tu trouveras la liste complète des collections Braze Docs dans le fichier de configuration Jekyll, `_config.yml`.

```yaml
collections:
  home:
    title: Documentation
    output: true
    default_nav_url: ''
    page_order: 1
  user_guide:
    title: User Guide
    output: true
    default_nav_url: introduction/
    page_order: 2
  developer_guide:
    title: Developer Guide
    output: true
    default_nav_url: home/
    page_order: 3
  api:
    title: API
    output: true
    default_nav_url: home/
    page_order: 4
  partners:
    title: Technology Partners
    output: true
    default_nav_url: home/
    page_order: 5
  help:
    title: Help
    output: true
    default_nav_url: home/
    page_order: 6
  contributing:
    output: true
    default_nav_url: contributing/
  hidden: # Hidden pages not directly linked via navigation
    title: Braze
    output: true
    hidden: true
  docs_pages: # Site specific pages. ie main redirects and search
    title: Braze
    output: true
    hidden: true
```

Chaque collection répertoriée représente un répertoire au sein du répertoire `_docs`.

```plaintext
braze-docs
└── _docs
    ├── _api
    ├── _contributing
    ├── _developer_guide
    ├── _docs_pages
    ├── _help
    ├── _hidden
    ├── _home
    ├── _partners
    └── _user_guide
```

La page d'accueil de chaque section primaire est un fichier Markdown standard dont la clé `page_order:` est définie sur `0`.

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
page_order: 0
nav_title: Home
article_title:Guide de l’utilisateur Braze
layout: user\_guide
user\_top\_header: Guide de l’utilisateur Braze
---
\`\`\`
{% endtab %}

{% tab example output %}
![An example landing page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/primary_section.png %})
{% endtab %}
{% endtabs %}

### Sous-sections

Toutes les sections principales de Braze Docs contiennent une ou plusieurs sous-sections, chacune représentant un élément extensible dans la navigation de gauche.

Contrairement aux sections primaires, les sous-sections peuvent être configurées avec ou sans page de renvoi. Les sous-sections sans pages d'atterrissage sont utiles pour organiser ensemble le contenu connexe tout en minimisant le nombre de pages non utiles dans Braze Docs. Qu'une sous-section soit configurée avec ou sans page de destination, toutes les sous-sections représentent à la fois un répertoire et un fichier Markdown dans le référentiel. Pour un exemple, voir ce qui suit.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% alert tip %}
Pour une présentation complète, voir [Créer une section]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section).
{% endalert %}

Dans le répertoire `_primary_section`, `subsection_a` n'est pas configuré avec une page d'atterrissage, tandis que `subsection_b` est configuré avec une page d'atterrissage. Dans l'exemple suivant, `subsection_a.md` a pour valeur `config_only:` `true` , ce qui empêche le rendu de cette page en tant que page d'atterrissage.

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: Sous-section A
page_order: 0
config_only: true
---
\`\`\`
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section without a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_config_only.png %})
{% endtab %}
{% endtabs %}

Cependant, `subsection_b.md` n'utilise pas la clé `config_only:`, et cette page _est_ donc rendue comme une page d'atterrissage.

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: Sous-section B
page_order: 0
---
\`\`\`
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section with a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
{% endtab %}
{% endtabs %}

{% alert note %}
Bien qu'une sous-section dont l'adresse `config_only:` est définie sur `true` ne soit pas rendue comme une page, le nom du répertoire de la sous-section est toujours utilisé dans les URL des pages de cette sous-section. Pour plus d'informations, voir [URL](#urls).
{% endalert %}

## Réutilisation du contenu

Jekyll offre la possibilité de réutiliser le contenu écrit dans les documents à l'aide de la balise `include`. Les inclusions se trouvent dans le répertoire `_includes` et peuvent être écrites en syntaxe Markdown ou HTML.

```markdown
{% raw %}{% multi_lang_include RELATIVE_PATH/FILE %}{% endraw %}
```

Remplacez les éléments suivants :

| Placeholder | Description |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RELATIVE_PATH` | (Facultatif) Le chemin d'accès relatif au fichier du répertoire `_includes`. Ceci n'est nécessaire que si tu inclus un fichier provenant d'un répertoire situé à l'intérieur du répertoire `_includes`, tel que `_includes/braze/upgrade_notice.md`. |
| `FILE` | Le nom du fichier, y compris son extension.                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs local %}
{% tab example input %}
{% raw %}
\`\`\`markdown
# Pages

> Apprends à créer, modifier et supprimer des pages sur Braze Docs.

{% multi_lang_include contributing/prerequisites.md %}
\`\`\`
{% endraw %}
{% endtab %}

{% tab example output %}
![Content reuse example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/includes.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour une présentation complète, voir [Réutiliser le contenu]({{site.baseurl}}/contributing/content_management/reusing_content).
{% endalert %}

## Mises en page

Par défaut, Jekyll utilise la mise en page `default.html` dans le répertoire `_layouts` pour construire chaque page sur Braze Docs. Cependant, il est possible d'utiliser différentes mises en page en attribuant la mise en page à la touche `layout:` dans la page d'accueil YAML.

\`\`\`markdown
---
layout: LAYOUT\_VALUE
---
\`\`\`

Remplace `LAYOUT_VALUE` par le nom du fichier de mise en page et l'extension du fichier est supprimée.

{% tabs local %}
{% tab example input %}
**Arbre de fichiers**

```plaintext
braze-docs
└── _layouts
    └── api_page.html
```

**Métadonnées dans la page**

\`\`\`markdown
---
layout: page api
---
\`\`\`
{% endtab %}

{% tab example output %}
![API glossary layout example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour plus d'informations, voir [Mise en page]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts).
{% endalert %}

## URL

Les URL sur Braze Docs correspondent toujours à la structure des répertoires dans le référentiel docs. Dans l'exemple suivant d'arborescence de fichiers, l'URL pour `page_a.md` serait `https://www.braze.com/docs/primary_section/subsection_a/page_a`.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        └── subsection_a
            └── page_a.md
```

Cela inclut les URL des pages situées dans une [sous-section](#subsections) où `config_only:` est défini sur `true`. Même si les sous-sections de `config_only` ne sont pas présentées comme des pages, le nom du répertoire de la sous-section est toujours utilisé pour générer les URL des pages de ce répertoire. Pour un exemple, voir ce qui suit.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% tabs local %}
{% tab subsection a %}

**Exemple de page d'atterrissage**

\`\`\`markdown
---
nav_title: Sous-section A
1\.
config_only: true
---
\`\`\`

Puisque `subsection_a.md` est configuré comme une page d'atterrissage, seuls `page_a.md` et `page_b.md` recevront une URL unique. `subsection_b.md` **ne** recevra aucune URL.

**Exemples d'URL**

```plaintext
Subsection A URL: N/A
Page A URL: https://www.braze.com/docs/primary_section/subsection_a/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_a/page_b
```
{% endtab %}
{% tab subsection b %}
**Exemple de page d'atterrissage**

\`\`\`markdown
---
nav_title: Sous-section B
2\. 
---
\`\`\`

Puisque `subsection_b.md` est configuré comme une page d'atterrissage, `page_a.md`, `page_b.md`, et `subsection_b.md` recevront une URL unique.

**Exemples d'URL**

```plaintext
Subesction B URL: https://www.braze.com/docs/primary_section/subsection_b
Page A URL: https://www.braze.com/docs/primary_section/subsection_b/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_b/page_b
```
{% endtab %}
{% endtabs %}
