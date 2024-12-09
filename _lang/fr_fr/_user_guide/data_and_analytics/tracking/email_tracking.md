---
nav_title: Suivi du pixel d’ouverture et des clics dans les e-mails
article_title: Suivi du pixel d’ouverture et des clics dans les e-mails
page_order: 1
page_type: reference
description: "Cet article de référence explique comment implémenter le suivi du pixel d’ouverture et des clics dans les e-mails."

---

# Suivi du pixel d’ouverture et des clics dans les e-mails

> Le [suivi des pixels ouverts][open_tracking] et le suivi des clics peuvent être activés ou désactivés pour chaque profil utilisateur. Cette flexibilité vous aide à respecter les règlements sur la protection de la vie privée, où un profil d’utilisateur individuel peut indiquer qu’il ne veut plus être suivi.

## Activation du pixel ouvert ou du suivi des clics

Lors de l'importation ou de la mise à jour d'un profil utilisateur via [API][api_doc] ou [CSV][csv_doc], vous pouvez modifier deux champs :

- `email_open_tracking_disabled` : Accepte `true` ou `false`. Définir sur `false` pour ajouter le pixel de suivi des ouvertures à tous les futurs e-mails envoyés à cet utilisateur.
- `email_click_tracking_disabled` : Accepte `true` ou `false`. Définissez ce champ sur `false` pour ajouter le suivi des clics à tous les liens contenus dans un prochain e-mail envoyé à cet utilisateur.

Pour référence, cette information est reflétée sur le profil utilisateur dans l'e-mail **Paramètres de contact**, situé dans l'onglet **Engagement.** 

![Champs d’ouverture d’e-mail et de pixel de suivi des clics dans l’onglet Engagement d’un profil utilisateur][1]{: style="max-width:60%;"}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}
