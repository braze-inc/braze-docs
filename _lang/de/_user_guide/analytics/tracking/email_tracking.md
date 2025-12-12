---
nav_title: E-Mail Öffnung Pixel und Klick Tracking
article_title: E-Mail Öffnung Pixel und Click Tracking
page_order: 1
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie das Tracking von Öffnungen und Klicks implementieren können."

---

# E-Mail Öffnung Pixel und Klick Tracking

> [Das Tracking offener Pixel]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) und das Tracking von Klicks kann für jedes Nutzerprofil ein- oder ausgeschaltet werden. Diese Flexibilität hilft Ihnen bei der Einhaltung regionaler Datenschutzgesetze, bei denen das Profil eines einzelnen Nutzers:in angeben kann, dass er nicht mehr getrackt werden möchte.

## Öffnung des Pixels oder Tracking von Klicks einschalten

Wenn Sie ein Nutzerprofil über [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) oder [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) importieren oder aktualisieren, stehen Ihnen zwei Felder zur Verfügung, die Sie ändern können:

- `email_open_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie diese Option auf `false`, um das Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails hinzuzufügen, die an diese Nutzer:innen gesendet werden. Nur für SparkPost und SendGrid verfügbar.
- `email_click_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie diese Option auf `false`, um das Tracking von Klicks für alle Links in einer zukünftigen E-Mail an diesen Nutzer:innen hinzuzufügen. Nur für SparkPost und SendGrid verfügbar.

Zum Referenzieren finden Sie diese Informationen im Nutzerprofil in den **E-Mail-Kontakteinstellungen**, die sich auf dem Tab **Engagement** befinden.

\![Felder für das Öffnen von E-Mails und das Tracking von Klicks auf dem Tab "Engagement" des Profils eines Nutzers:innen]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

