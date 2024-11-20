---
nav_title: Aperçu
page_order: 0
noindex: true
---

# Exemple de mise en page : Aperçu

> La mise en page d'aperçu permet de créer une option de navigation spécifique en haut d'une page qui permet aux utilisateurs de cliquer sur un bouton pour se rendre à une partie spécifique d'une page ou à une page complètement différente.

La page des [modifications du SDK](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_changelogs/) ou la [page des détails créatifs des messages in-app](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/) sont des exemples classiques de la mise en page du sélecteur.

## Composants requis

1. Notation d'ouverture et de fermeture YAML. En d'autres termes, --- avant le contenu et --- après.
2. Des guillemets entourent le contenu de certains paramètres. (Paramètres d'en-tête, paramètres de texte, contenu comportant des traits d'union ou d'autres caractères spéciaux).
3. Notation des tags du glossaire (il s'agit de tags de filtrage)

## Paramètres requis

|Paramètre | Type de contenu | Détails |
|---|---|---|
|`page_order`| numérique | Ordonnez la page à l'intérieur de la section. Cet ordre se reflète dans la navigation de gauche. |
| `nav-title`| Alphanumérique | Titre qui apparaîtra dans la navigation de gauche. |
|`layout`| Alphanumérique - Sans espace | Sélectionnez une mise en page dans la [section "Mise en page"](https://github.com/Appboy/braze-docs/tree/develop/_layouts) de la documentation. | 
|`guide_top_header`|Alphanumérique | Donnez un titre à votre page.|
|`guide_top_text`|Alphanumérique | Décrivez votre page, cela ira directement au-dessus des boutons et de leur titre. Des guillemets doivent être insérés autour du contenu. |
|`guide_featured_title`| Alphanumérique | Donnez un titre à vos cartes. Il sera placé directement au-dessus des boutons.
|`guide_featured_list`| Plus de YAML, Alphanumérique | Voir le [format des listes du guide](#guide-listing-format) ci-dessous. |

### Format des listes du guide

|Paramètre | Type de contenu | Détails |
|---|---|---|
|`name`| Alphanumérique | Attribuez un nom à la case. |
| `link`| URL ou chemin d'accès | Lien vers l'emplacement de la case. Doit contenir l'URL complète ou (s'il s'agit d'un lien interne) `/docs...`  |
|`image`| Chemin | Lien vers l'emplacement/localisation de l'image. |

Exemple de format :

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## Exemple

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
