---
nav_title: メール開封ピクセルとクリックの追跡
article_title: メール開封ピクセルとクリックの追跡
page_order: 1
page_type: reference
description: "このリファレンス記事では、開封ピクセルとクリックの追跡の実装方法について説明します。"

---

# メール開封ピクセルとクリックの追跡

> [開封ピクセルトラッキング]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel)とクリックトラッキングは各ユーザープロファイルごとにオンまたはオフにすることができます。このような柔軟性があるため、ユーザーが各自のユーザープロファイルを追跡対象外と指定したときに地域の個人情報保護法を遵守できます。

## 開封ピクセルとクリックの追跡の有効化

[API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) または [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) を使用してユーザープロファイルのインポートまたは更新を行う場合、次の 2 つのフィールドを変更できます。

- `email_open_tracking_disabled`: `true` または `false` を受け入れます。`false`に設定して、このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルを追加します。SparkPostとSendGridでのみ利用可能。
- `email_click_tracking_disabled`: `true` または `false` を受け入れます。`false`に設定して、このユーザーに送信される将来のメール内のすべてのリンクにクリックトラッキングを追加します。SparkPostとSendGridでのみ利用可能。

参考までに、この情報はユーザープロファイルのメール**連絡設定**に反映され、**エンゲージメント**タブにあります。

![ユーザープロファイルのエンゲージメントタブのメール開封およびクリック追跡ピクセルフィールド]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

