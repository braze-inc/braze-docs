---
nav_title: Suivi du pixel d’ouverture et des clics dans les e-mails
article_title: Suivi du pixel d’ouverture et des clics dans les e-mails
page_order: 1
page_type: reference
description: "Cet article de référence explique comment implémenter le suivi du pixel d’ouverture et des clics dans les e-mails."

---

# Aperçu du Suivi du pixel d’ouverture et des clics dans les e-mails

Le [Suivi du pixel d’ouverture et des clics][open_tracking] dans les e-mails peut être désactivé par profil utilisateur. Cette flexibilité vous aide à respecter les règlements sur la protection de la vie privée, où un profil d’utilisateur individuel peut indiquer qu’il ne veut plus être suivi.

## Mise en œuvre

Lorsque vous importez ou mettez à jour un profil utilisateur via [API][api_doc] ou [CSV][csv_doc], deux champs sont modifiables :

- `email_open_tracking_disabled`
- `email_click_tracking_disabled`

Pour une référence facile, ces informations sont reflétées sur le profil utilisateur dans l’e-mail **Paramètres de contact**, sur l’onglet **Engagement**.

![Champs d’ouverture d’e-mail et de pixel de suivi des clics sur l’onglet Engagement d’un profil utilisateur][1]{: style="max-width:60%;"}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}
