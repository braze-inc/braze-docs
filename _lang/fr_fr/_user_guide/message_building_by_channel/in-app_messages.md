---
nav_title: "Messages in-app"
article_title: Messages in-app
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "Messages in-app"
guide_top_text: "Les messages in-app vous permettent d'envoyer du contenu à votre utilisateur sans interrompre sa journée avec une notification push, car ces messages ne sont pas envoyés en dehors de l'application de l'utilisateur et n'empiètent pas sur son écran d'accueil. <br><br>Des messages in-app personnalisés et adaptés améliorent l'expérience sur l'application et aident votre audience à tirer le meilleur parti de votre application. Avec une variété de mises en page et d'outils de personnalisation au choix, les messages in-app engagent vos utilisateurs plus que jamais. Ils s'inscrivent dans un contexte, sont moins urgents et sont délivrés lorsque l'utilisateur est actif dans votre application. Pour des exemples de messages in-app, consultez nos <a href='https://www.braze.com/customers'>témoignages de clients</a>."
description: "Cette page d'atterrissage abrite tout ce qui concerne les messages in-app. Vous y trouverez des articles sur la création de messages in-app, l'éditeur par glisser-déposer, la personnalisation de vos messages, la création de rapports, etc."
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "Articles populaires"
guide_featured_list:
- name: "Éditeur par glisser-déposer"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Rédacteur traditionnel"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Détails créatifs"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "Essais"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "Rapports"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Mode sombre"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Invitation à l'évaluation de l'App Store"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "Enquête simple"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "Locales dans les messages"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "Meilleures pratiques"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "FAQ"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Cas d'utilisation potentiels

Grâce à la richesse du contenu offert par les messages in-app, vous pouvez tirer parti de ce canal pour toute une série de cas d'utilisation :

| Cas d'utilisation | Explication |
| --- | --- |
| Amorçage de push | Lancez une campagne d'[amorçage push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) à l'aide d'un message in-app riche pour montrer à vos clients l'intérêt d'opter pour le push pour votre application ou votre site, et présentez-leur une demande d'abonnement au push.
| Ventes et promotions | Utilisez des messages in-app modaux pour accueillir les clients avec des supports visuellement attrayants contenant des codes de promotion ou des offres statiques. Incitez-les à effectuer des achats ou des conversions alors qu'ils ne l'auraient pas fait autrement. |
| Encourager l'adoption des fonctionnalités | Encouragez les clients à utiliser d'autres parties de votre appli ou à profiter d'un service. |
| Des campagnes hautement personnalisées | Placez les messages in-app comme la première chose que vos clients voient lorsqu'ils entrent dans votre application ou votre site. Ajoutez quelques fonctionnalités de personnalisation de Braze, telles que le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), pour obliger les utilisateurs à passer à l'action et ainsi rendre votre sensibilisation plus efficace.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

D'autres cas d'utilisation sont à envisager, notamment les suivants :

- Nouvelles fonctionnalités de l'application
- Gestion des applications
- Commentaires
- Mises à niveau ou mises à jour de l'application
- Concours et loteries

## Types de messages standard

Les onglets suivants montrent comment vos utilisateurs ouvrent l'un de nos types de messages in-app standard : messages in-app en fenêtre modale/boîte de dialogue modale, etc.

{% tabs %}
{% tab Slideup %}

Les messages in-app s'affichent généralement en haut et en bas de l'écran de l'appli (vous pouvez régler ce paramètre lorsque vous créez votre message). Elles sont idéales pour alerter vos utilisateurs sur les nouvelles conditions de service, les cookies et d'autres extraits de code.

!Message in-app contextuel apparaissant en bas de l'écran de l'application. Le diaporama comprend une image d'icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Les fenêtres modales apparaissent au centre de l'écran de l'appareil avec une superposition d'écran qui lui permet de se démarquer de votre application en arrière-plan. Ils sont parfaits pour suggérer subtilement à votre utilisateur de profiter d'une vente ou d'un cadeau.

!message modal in-app apparaissant au centre d'une application et d'un site web sous forme de dialogue. La fenêtre modale comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

Les messages en plein écran sont exactement ce à quoi vous vous attendez : ils occupent tout l'écran de l'appareil ! Ce type de message est idéal lorsque vous avez vraiment besoin de l'attention de votre utilisateur, comme pour les mises à jour obligatoires d'une application.

Un message in-app en plein écran envahit l'écran de l'application. Le message en plein écran comprend une grande image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

Outre ces modèles de messages prêts à l'emploi, vous pouvez également personnaliser davantage votre envoi à l'aide de messages in-app personnalisés en HTML, de fenêtres modales/boîte de dialogue en CSS ou de formulaires de capture d'e-mails en ligne. Pour plus d'informations, reportez-vous à la rubrique [Personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Plus de ressources

Avant de vous lancer dans la création de vos propres campagnes de messages in-app - ou dans l'utilisation de messages in-app dans le cadre d'une campagne multicanal - nous vous recommandons vivement de consulter notre [guide de préparation des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Ce guide aborde les questions de ciblage, de contenu et de conversion que vous devez prendre en compte lorsque vous créez des messages in-app.
