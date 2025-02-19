---
nav_title: "Migration von Benutzerdaten"
article_title: Migration von Benutzerdaten
page_order: 4
description: "In diesem Referenzartikel finden Sie alle Überlegungen, die Sie bei der Migration Ihrer Nutzerdaten nach Braze beachten müssen."
page_type: reference
channel:
  - SMS
noindex: true

---

# Migration von Benutzerdaten

> Dieser Artikel behandelt alle Überlegungen, die Sie bei der Migration Ihrer Nutzerdaten nach Braze beachten müssen.

## Formatieren Sie Nutzertelefonnummern nach den Standards der Netzbetreiber

Die Telefongesellschaften haben ein bestimmtes Format, das sie erwarten: E.164. Dabei handelt es sich um einen internationalen Telefonnummernplan, der sicherstellt, dass jedes Gerät eine weltweit eindeutige Nummer hat. So können Anrufe und Textnachrichten korrekt an einzelne Telefone in verschiedenen Ländern weitergeleitet werden. E.164 Nummern sind wie in der folgenden Abbildung dargestellt formatiert und können maximal 15 Ziffern haben.

![E.164 Format besteht aus einem Pluszeichen, der Landesvorwahl, der Ortsvorwahl und der Telefonnummer][Bild]{: style="max-width:50%;border: 0;"}

Weitere Informationen finden Sie unter [Benutzertelefonnummern][userphone].

## Aktualisieren Sie historische Informationen zum Abonnementstatus der Benutzer

Wenn Sie über historische Informationen zu den [Abo-Status][subscriptionstate] Ihrer Nutzer:innen für Ihre verschiedenen Messaging-Kanäle verfügen, sollten Sie diese Informationen in Braze aktualisieren.

## Beispielhafte Migrationsschritte

Bevor Sie mit der Erstellung von SMS Kampagnen über Braze beginnen, müssen Sie Ihre Nutzerdaten aktualisieren, um sicherzustellen, dass dies alles funktioniert.

**Hier finden Sie eine kurze Zusammenfassung der Nutzerdaten, die Sie in Braze aktualisieren müssen:**

1. **Importieren Sie die Telefonnummern der Benutzer im richtigen Format** ([E.164][0]) Formatierung erfordert ein Pluszeichen (+) und einen Ländercode. Ein Beispiel ist +12408884782. Weitere Informationen über den Import von Benutzertelefonnummern finden Sie unter [Benutzertelefonnummern][userphone].
    * Verwenden Sie den [Endpunkt`/users/track` ][1], um den Wert `phone` zuzuweisen.<br><br>

2. **Weisen Sie den SMS-Status Ihrer Nutzerin oder Ihres Nutzers zu [Abonnentenstatus][subscriptionstate]** (z. B. abonniert oder abgemeldet) , wenn Sie über diese Information verfügen.
    * Verwenden Sie den [`/subscription/status/set`Endpunkt ][6], um Nutzer:innen als Abonnent:innen Ihrer SMS-Abo-Gruppen an- oder abzumelden.

{% alert note %}
Nachdem Sie die SMS-Abo-Gruppen in Ihrem Dashboard konfiguriert haben, können Sie die zugehörigen `subscription_group_id` abrufen, die Sie für Ihre API-Anfrage benötigen.
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[Bild]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/nachrichten_erstellung_durch_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
