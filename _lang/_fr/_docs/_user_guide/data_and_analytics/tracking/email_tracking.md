---
nav_title: Envoyer un e-mail à Open Pixel et cliquez sur Suivi
article_title: Envoyer un e-mail à Open Pixel et cliquez sur Suivi
page_order: 1
page_type: Référence
description: "Cet article de référence traite de la désactivation des pixels ouverts et du suivi des clics."
---

# Ouvrez le pixel et cliquez sur la vue d'ensemble du suivi

[Le suivi des pixels ouverts][open_tracking] et le suivi des clics peuvent maintenant être désactivés par profil d'utilisateur. Cette flexibilité vous aide à respecter les lois régionales en matière de protection de la vie privée, où un profil utilisateur individuel pourrait indiquer qu'il ne souhaite plus être suivi.

## Implémentation

Lors de l'importation ou de la mise à jour d'un profil utilisateur via [API][api_doc] ou [CSV][csv_doc], deux nouveaux champs sont maintenant disponibles pour vous :

- Email_open_tracking_désactivé
- Email_click_tracking_désactivé

Pour une référence facile, cette information est reflétée sur le profil de l'utilisateur dans l'e-mail **Paramètres de contact**, situé dans l'onglet **Engagement**.

!\[open_click_user_profile\]\[1\]{: style="max-width:60%;"}
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#standard-user-data-column-headers
