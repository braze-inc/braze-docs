---
nav\_title : Recibler les utilisateurs article\_title : Recibler les utilisateurs grâce à la description d'une page d'atterrissage : "Apprenez à recibler les utilisateurs qui ont soumis un formulaire via une page d'atterrissage" page\_order : 3
---

# Recibler les utilisateurs par le biais d'une page d'atterrissage

> Découvrez comment recibler les utilisateurs qui ont envoyé un formulaire via une page d'atterrissage en créant un segment dédié ou en déclenchant un message lors de l'envoi du formulaire.

## Conditions préalables

Avant de commencer, vous devez créer une [page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Reciblage des utilisateurs

Braze effectue un suivi automatique lorsqu'un utilisateur soumet le formulaire d'une page d'atterrissage. Vous pouvez consulter le nombre total de soumissions pour un formulaire sous [analyse/analytique de la page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics)(si utilisé comme adjectif). Cependant, pour un reciblage spécifique à l'utilisateur, vous devrez recibler les utilisateurs via le formulaire de votre page d'atterrissage en utilisant l'une des méthodes suivantes :

- **Utilisation d'un segment :** Vous pouvez créer une nouvelle segmentation pour identifier automatiquement les utilisateurs qui ont ou n'ont pas soumis un formulaire de page de destination.
- **Utilisation d'un message déclenché :** Vous pouvez configurer un déclencheur de message pour envoyer automatiquement un message aux utilisateurs ou les inscrire dans un canvas après qu'ils ont soumis le formulaire.

{% onglets local %} {% onglet Utilisation d'une segmentation %} Lorsque vous [créez un segment]({{site.baseurl}}/docs/user_guide/engagement_tools/segments/creating_a_segment/), dans le groupe "Reciblage", choisissez **Formulaire soumis sur la page d'atterrissage**.

\![Création d'un segment avec le groupe de filtres sélectionné comme "Formulaire soumis sur la page d'atterrissage"\]({% image\_buster /assets/img/landing\_pages/segmentation\_selected.png %})

À partir de là, vous pouvez segmenter les utilisateurs selon qu'ils ont ou non soumis un formulaire pour votre page d'atterrissage. {% endtab %}

{% onglet Utiliser un message déclenché %} Lorsque vous choisissez votre option de réception/distribution pour votre [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou votre [canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/), sélectionnez **Livraison par événement**, puis **Formulaire de page d'atterrissage soumis**.

Tous les utilisateurs qui soumettent un formulaire par l'intermédiaire de cette page de renvoi recevront un message par l'intermédiaire du canal de communication choisi ou seront inscrits dans le Canvas choisi.

\![Action déclenchante de la page d'atterrissage dans l'envoi de messages\]({% image\_buster /assets/img/landing\_pages/trigger.png %}) {% endtab %} {% endtabs %}
