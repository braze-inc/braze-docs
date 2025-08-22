---
nav_title: Cas d’utilisation
article_title: "Cas d'utilisation de la transformation des données de Braze"
page_order: 2
page_type: reference
description: "Cet article de référence présente quelques cas d'utilisation de la transformation des données Braze."
---

# Cas d'utilisation de la transformation des données

> Considérez les cas d'utilisation possibles suivants avec Braze Data Transformation et une combinaison de webhooks provenant des plateformes externes données en exemple.

## Générer des prospects

Vous hébergez un formulaire Typeform de génération de leads sur votre site web. Lorsque de nouveaux utilisateurs remplissent ce formulaire, vous pouvez.. :
- Créez de nouveaux utilisateurs dans Braze.
- Ajoutez-les à l'une de vos listes d'e-mails de Braze.
- Synchronisez certaines de leurs réponses en tant qu'attributs personnalisés dans Braze, car leurs réponses sont des données first-party précieuses qui peuvent alimenter des expériences d'envoi de messages personnalisés pour une utilisation future.

## Ouverture des tickets de service

Lorsque les clients ouvrent des tickets de service client sur une plateforme comme Zendesk, vous pouvez :
- Écrire un événement personnalisé dans Braze lorsqu'un ticket Zendesk est créé.
- Écrire un événement personnalisé avec des propriétés d'événement dans Braze lorsqu'une note CSAT négative est fournie à Zendesk.

## Intégration avec Braze

Braze dispose d'une intégration avec [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/), une plateforme d'informations et d'enquêtes sur les clients. Grâce à la transformation des données, vous pouvez enregistrer plusieurs réponses d'enquête sous un seul attribut personnalisé imbriqué, au lieu de l'intégration existante qui enregistre plusieurs attributs personnalisés.

## Exemple de code de transformation

Considérez cet exemple de charge utile provenant de Typeform, une plateforme d'enquête, qui est envoyée chaque fois qu'une réponse à l'enquête est reçue.

![]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Transformation de base %}

Cet exemple prend les réponses à l'enquête comme attributs et écrit un événement pour indiquer que l'enquête a été complétée :

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Transformation avancée %}

Créons un nouvel exemple de transformation de base et introduisons une déclaration `if` pour classer l'utilisateur dans l'une des réponses.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}