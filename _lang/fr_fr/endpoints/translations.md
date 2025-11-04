---
nav_title: Traductions
article_title: Endpoints de traduction
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Cette page d’accueil répertorie les endpoints de traduction de Braze."
page_type: landing

guide_top_header: "Endpoints de traduction"
guide_top_text: "Utilisez les endpoints de traduction de Braze pour gérer et mettre à jour les traductions de vos campagnes et canvas."

guide_featured_title: "Les endpoints de la campagne"
guide_featured_list:
  - name: "GET : Voir la traduction pour une campagne"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : Voir toutes les traductions pour une campagne"
    link: /docs/api/endpoints/translations/campaigns/get_bulk_translations_campaigns/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT : Mettre à jour la traduction dans une campagne"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "GET : Afficher la traduction d’un canvas"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : Voir toutes les traductions pour un canvas"
    link: /docs/api/endpoints/translations/canvas/get_bulk_translations_canvases/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT : Mise à jour de la traduction dans un canvas"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  
guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "GET : Voir la traduction de la source"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : Voir la traduction et la langue spécifiques"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Voir toutes les traductions et localisations"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT : Mise à jour des traductions dans un modèle d'e-mail"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

---

{% alert important %}
Les endpoints de traduction de Braze sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Fonctionnement de nos endpoints de traduction

Nos endpoints de traduction fonctionnent avec la [composition multilingue]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/), où un message peut avoir différentes versions qui peuvent être rendues en fonction de l'utilisateur qui reçoit le message.

### Conditions préalables

Avant d'utiliser ces endpoints, vous devez [ajouter vos locales.]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale)

### Comment tester vos traductions

Vous pouvez valider la prise en charge de la traduction de deux manières différentes à l'aide de l'API et du tableau de bord de Braze sur les campagnes, les Canvas (y compris les étapes individuelles) et les modèles d'e-mail :

- Pendant la composition (avant le lancement)
- Après le lancement (à l'aide de versions préliminaires postérieures au lancement)

Avant de tester la mise à jour des traductions, vous devez

1. [Ajoutez vos localités]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Créez un message et utilisez les étiquettes de traduction le cas échéant.
3. Enregistrez le message.
4. Sélectionnez les localités à inclure.
