---
nav_title: Reciblage des utilisateurs
article_title: "Recibler les utilisateurs par le biais d'une page d'atterrissage"
description: "Découvrez comment recibler les utilisateurs qui ont soumis un formulaire via une page d'atterrissage."
page_order: 3
---

# Recibler les utilisateurs par le biais d'une page d'atterrissage

> Découvrez comment recibler les utilisateurs qui ont envoyé un formulaire via une page d'atterrissage en créant un segment dédié ou en déclenchant un message lors de l'envoi du formulaire.

## Conditions préalables

Avant de commencer, vous devez créer une [page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Reciblage des utilisateurs

Braze effectue un suivi automatique lorsqu'un utilisateur soumet le formulaire d'une page d'atterrissage. Vous pouvez consulter le nombre total de soumissions pour un formulaire sous [analyse/analytique de la page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics)(si utilisé comme adjectif). Cependant, pour un reciblage spécifique à l'utilisateur, vous devrez recibler les utilisateurs via le formulaire de votre page d'atterrissage en utilisant l'une des méthodes suivantes :

- **Utilisation d'un segment :** Vous pouvez créer une nouvelle segmentation pour identifier automatiquement les utilisateurs qui ont ou n'ont pas soumis un formulaire de page de destination.
- **Utilisation d'un message déclenché :** Vous pouvez configurer un déclencheur de message pour envoyer automatiquement un message aux utilisateurs ou les inscrire dans un canvas après qu'ils ont soumis le formulaire.

{% tabs local %}
{% tab Using a segment %}
Lorsque vous [créez un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), dans le groupe "Reciblage", choisissez **Formulaire soumis sur la page d'atterrissage**.

Création d'un segment avec le groupe de filtres sélectionné comme "Formulaire soumis sur la page d'atterrissage".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

À partir de là, vous pouvez segmenter les utilisateurs selon qu'ils ont ou non soumis un formulaire pour votre page d'atterrissage.
{% endtab %}

{% tab Using a message trigger %}
Lorsque vous choisissez votre option de réception/distribution pour votre [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/), sélectionnez **Livraison par événement**, puis **Formulaire de page d'atterrissage soumis**.

Tous les utilisateurs qui soumettent un formulaire par l'intermédiaire de cette page de renvoi recevront un message par l'intermédiaire du canal de communication choisi ou seront inscrits dans le Canvas choisi.

!Action déclenchée par la page d'atterrissage dans l'envoi de messages.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
L'option de livraison par événement pour les pages de renvoi n'est pas disponible pour les messages in-app. Pour cibler les utilisateurs qui ont soumis un formulaire sur une page de renvoi avec un message in-app, sélectionnez le filtre **Formulaire soumis sur la page de renvoi** dans les **options de ciblage** de votre campagne.
{% endalert %}

{% endtab %}
{% endtabs %}
