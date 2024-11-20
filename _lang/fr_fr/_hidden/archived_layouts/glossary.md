---
nav_title: Glossaire
article_title: Mise en page du glossaire
page_order: 0
noindex: true
---

# Exemple de mise en page : Glossaire

> La présentation du glossaire est en YAML. Il nécessite plusieurs composants et paramètres. Les mises en page de glossaire conviennent aux contenus localisés pouvant faire l'objet d'une recherche, tels que les dictionnaires et les catégories de contenu spécifiques.

## Composants requis

1. Notation d'ouverture et de fermeture YAML. En d'autres termes, `---` avant le contenu et `---` après. 
2. Des guillemets entourent le contenu de certains paramètres. (Paramètres d'en-tête, paramètres de texte, contenu comportant des traits d'union ou d'autres caractères spéciaux).
3. Notation des tags du glossaire (il s'agit de tags de filtrage)

## Paramètres requis

|Paramètre | Type de contenu | Détails |
|---|---|---|
|`page_order`| numérique | Ordonnez la page à l'intérieur de la section. Cet ordre se reflète dans la navigation de gauche. |
| `nav-title`| Alphanumérique | Titre qui apparaîtra dans la navigation de gauche. |
|`layout`| Alphanumérique - Sans espace | Sélectionnez une mise en page dans la [section "Mise en page"](https://github.com/Appboy/braze-docs/tree/develop/_layouts) de la documentation. | 
|`glossary_top_header` | Alphanumérique | Nécessite des guillemets doubles. Le titre apparaît en haut de la page. |
|`glossary_top_text`| Chaîne de caractères, Alphanumérique | Décrivez votre page de glossaire. Elle apparaît au-dessus de la barre de recherche et des filtres (si vous choisissez d'en avoir). Ceci est essentiellement écrit en HTML, vous pouvez donc utiliser \`\`\`<br> pour créer des ruptures de ligne. | 
|`glossary_tag_name` | Mot unique, alphanumérique | Donnez un nom à vos filtres. Celles-ci apparaîtront dans les cases à cocher situées sous la barre de recherche ainsi que dans les données ci-dessous. | 
|`glossary_filter_text`| Chaîne de caractères, Alphanumérique | Décrivez vos filtres. Généralement utilisé pour instruire. | 
|`glossary_tags`| Davantage de contenu YAML plus. | Format comme indiqué ci-dessous : <br> glossary_tags : <br>  \- nom : Cartes de contenu <br>  \- nom : E-mail | 
| `glossaries`| Davantage de contenu YAML plus. | Voir les [paramètres des glossaires](#glossaries-parameters) ci-dessous. |

### Paramètres des glossaires

|Paramètre | Type de contenu | Détails |
|---|---|---|
|`name`| Alphanumérique | Donnez un nom à votre article de glossaire.| 
|`description`| Chaîne de caractères, Alphanumérique | Décrivez votre article de glossaire. | 
|`calculation`| Chaîne de caractères | (facultatif) Décrivez le mode de calcul de votre élément de glossaire (généralement utilisé pour décrire des données ou des indicateurs). | 
|`tags`| Alphanumérique | Il doit correspondre à ce qui est indiqué comme `name` sous `glossary_tags`. Énumérez-en autant qu'il y a lieu. En écrivant `All`, vous inclurez l'élément dans tous les filtres.|

## Exemple

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
