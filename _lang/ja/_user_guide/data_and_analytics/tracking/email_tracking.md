---
nav_title: メール開封ピクセルとクリックの追跡
article_title: メール開封ピクセルとクリックの追跡
page_order: 1
page_type: reference
description: "このリファレンス記事では、開封ピクセルとクリックの追跡の実装方法について説明します。"

---

# メール開封ピクセルとクリックの追跡

> [開封ピクセル追跡][open_tracking]とクリック追跡は、ユーザープロファイルごとに無効にできます。このような柔軟性があるため、ユーザーが各自のユーザープロファイルを追跡対象外と指定したときに地域の個人情報保護法を遵守できます。

## 実装

[API][api_doc] または [CSV][csv_doc] を使用してユーザープロファイルのインポートまたは更新を行う場合、次の 2 つのフィールドを変更できます。

- `email_open_tracking_disabled`
- `email_click_tracking_disabled`

簡単に参照できるように、この情報は [**エンゲージメント**] タブにあるメールの [**連絡先の設定**] のユーザープロファイルに反映されます。

![ユーザープロファイルの [エンゲージメント] タブのメールの開封追跡およびクリック追跡ピクセルフィールド] [1]{: style="max-width:60%;"}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}
