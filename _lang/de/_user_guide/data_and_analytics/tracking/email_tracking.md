---
nav_title: E-Mail Öffnung Pixel und Click Tracking
article_title: E-Mail Öffnung Pixel und Click Tracking
page_order: 1
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Open-Pixel- und Click-Tracking implementieren können."

---

# E-Mail Open-Pixel- und Click-Tracking

> [Das Tracking offener Pixel][open_tracking] und das Tracking von Klicks kann für jedes Nutzerprofil ein- oder ausgeschaltet werden. Diese Flexibilität hilft Ihnen bei der Einhaltung regionaler Datenschutzgesetze, wenn in einem einzelnen Nutzerprofil angegeben wird, dass es nicht mehr getrackt werden soll.

## Open-Pixel- und Click-Tracking einschalten

Wenn Sie ein Nutzerprofil über [API][api_doc] oder [CSV][csv_doc] importieren oder aktualisieren, stehen Ihnen zwei Felder zur Verfügung, die Sie ändern können:

- `email_open_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie diese Option auf `false`, um das Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails hinzuzufügen, die an diese Nutzer:innen gesendet werden.
- `email_click_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie diese Option auf `false`, um das Tracking von Klicks für alle Links in einer zukünftigen E-Mail an diesen Nutzer:innen hinzuzufügen.

Zum Referenzieren finden Sie diese Informationen im Nutzerprofil in den **E-Mail-Kontakteinstellungen**, die sich auf dem Tab **Engagement** befinden.

![Felder für Open-Pixel- und Click-Tracking auf dem Tab "Engagement" eines Nutzerprofils][1]{: style="max-width:60%;"}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}
