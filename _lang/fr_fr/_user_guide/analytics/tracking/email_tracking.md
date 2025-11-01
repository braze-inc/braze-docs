---
nav_title: "Pixel d'ouverture des e-mails et suivi des clics"
article_title: "Pixel d'ouverture des e-mails et suivi des clics"
page_order: 1
page_type: reference
description: "Cet article de référence explique comment mettre en place un pixel ouvert et un suivi des clics."

---

# Pixel d'ouverture des e-mails et suivi des clics

> Le [suivi des pixels ouverts]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) et le suivi des clics peuvent être activés ou désactivés pour chaque profil utilisateur. Cette flexibilité vous aide à respecter les lois régionales sur la protection de la vie privée, lorsqu'un profil utilisateur individuel peut indiquer qu'il ne souhaite plus être suivi.

## Activation du pixel ouvert ou du suivi des clics

Lors de l'importation ou de la mise à jour d'un profil utilisateur via [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) ou [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv), vous pouvez modifier deux champs :

- `email_open_tracking_disabled`: Accepte `true` ou `false`. Définir sur `false` pour ajouter le pixel de suivi des ouvertures à tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.
- `email_click_tracking_disabled`: Accepte `true` ou `false`. Définissez ce champ sur `false` pour ajouter le suivi des clics à tous les liens contenus dans un futur e-mail envoyé à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.

Pour référence, cette information est reflétée sur le profil utilisateur dans l'e-mail **Paramètres de contact**, situé dans l'onglet **Engagement**.

Champs du pixel de suivi des ouvertures et des clics par e-mail dans l'onglet Engagement du profil utilisateur]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

