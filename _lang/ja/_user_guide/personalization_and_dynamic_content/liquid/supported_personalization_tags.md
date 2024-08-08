---
nav_title: 対応パーソナライズタグ
article_title: 対応リキッドパーソナライゼーションタグ
page_order: 1
description: "この参考記事では、サポートされているリキッドパーソナライゼーションタグの完全なリストをカバーしています。"
search_rank: 1
---

# 対応パーソナライズタグ

> この参考記事では、サポートされているリキッドパーソナライゼーションタグの完全なリストをカバーしています。

便宜上、サポートされているパーソナライゼーション・タグの概要を示す。各タグの詳細とベストプラクティスについては、続きをお読みください。

{% raw %}

| パーソナライゼーション タグタイプ
| -------------  | ---- |
| 標準（デフォルト）属性 `{{${city}}}`<br> `{{${country}}}`<br> `{{${date_of_birth}}}`<br> `{{${email_address}}}`<br> `{{${first_name}}}`<br> `{{${gender}}}`<br> `{{${language}}}`<br> `{{${last_name}}}`<br> `{{${last_used_app_date}}}`<br> `{{${most_recent_app_version}}}`<br> `{{${most_recent_locale}}}`<br> `{{${most_recent_location}}}`<br> `{{${phone_number}}}`<br> `{{${time_zone}}}`<br> `{{${user_id}}}`<br> `{{${braze_id}}}`<br> `{{${random_bucket_number}}}`<br> `{{subscribed_state.${email_global}}}`<br> `{{subscribed_state.${subscription_group_id}}}` |
| デバイス属性 `{{most_recently_used_device.${carrier}}}`<br> `{{most_recently_used_device.${id}}}`<br> `{{most_recently_used_device.${idfa}}}`<br> `{{most_recently_used_device.${model}}}`<br> `{{most_recently_used_device.${os}}}`<br> `{{most_recently_used_device.${platform}}}`<br> `{{most_recently_used_device.${google_ad_id}}}`<br> `{{most_recently_used_device.${roku_ad_id}}}`<br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| 電子メールリストの属性][43]｜電子メールリストの属性 `{{${set_user_to_unsubscribed_url}}}`<br>このタグは、以前の`{{${unsubscribe_url}}}` 。古いタグは以前作成されたメールでも使用できますが、代わりに新しいタグを使用することをお勧めします。<br><br> `{{${set_user_to_subscribed_url}}}`<br> `{{${set_user_to_opted_in_url}}}`|
| [SMSの属性][48] | [SMSの属性 `{{sms.${inbound_message_body}}}`<br> `{{sms.${inbound_media_urls}}}` |
| [WhatsAppアトリビュート][46] | [WhatsAppアトリビュート `{{whats_app.${inbound_message_body}}}`<br> `{{whats_app.${inbound_media_urls}}}` |
| キャンペーン属性 `{{campaign.${api_id}}}`<br> `{{campaign.${dispatch_id}}}`<br> `{{campaign.${name}}}`<br> `{{campaign.${message_name}}}`<br> `{{campaign.${message_api_id}}}` |
| Canvas Attributes | `{{canvas.${name}}}`<br> `{{canvas.${api_id}}}`<br> `{{canvas.${variant_name}}}`<br> `{{canvas.${variant_api_id}}}` |
| キャンバスのステップ属性 `{{campaign.${api_id}}}`<br> `{{campaign.${dispatch_id}}}`<br> `{{campaign.${name}}}`<br> `{{campaign.${message_name}}}`<br> `{{campaign.${message_api_id}}}` |
| カード属性 `{{card.${api_id}}}`<br> `{{card.${name}}}` |
| Geofencing Events｜ジオフェンシング・イベント `{{event_properties.${geofence_name}}}`<br> `{{event_properties.${geofence_set_name}}}` |
イベントプロパティ <br> (これらはワークスペースのカスタムです。)|`{{event_properties.${your_custom_event_property}}}` |
| キャンバスエントリーのプロパティ|`{{canvas_entry_properties}}` |
カスタム属性 <br> (これらはワークスペースによって異なります) |`{{custom_attribute.${your_custom_attribute}}}` |.
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

[Brazeのソース間でこれらの属性がどのように異なるかについては]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/)、このヘルプ記事を参照してください。

{% alert important %}
キャンペーン、カード、およびキャンバスの属性は、対応するメッセージングテンプレートでのみサポートされます（たとえば、`dispatch_id` はアプリ内メッセージキャンペーンでは利用できません）。
{% endalert %}

#### キャンバスとキャンペーンタグの違い 

以下のタグはキャンバスとキャンペーンで動作が異なります：
{% raw %}
-`dispatch_id` キャンバスとキャンペーンで異なるのは、Brazeはキャンバスのステップを、たとえ「スケジュール」されていても、トリガーされたイベントとして扱うからです（スケジュール可能なエントリーステップを除く）。詳しくは【派遣IDの動作】[50]を参照。
\- Canvasで`{{campaign.${name}}}` タグを使用すると、Canvasコンポーネント名が表示されます。キャンペーンでこのタグを使用すると、キャンペーン名が表示されます。
{% endraw %}

## 最近使用したデバイス情報

すべてのプラットフォームで、ユーザーの最新のデバイスについて以下の属性をテンプレート化できます。ユーザがアプリケーションを使用していない場合 (たとえば、REST API 経由でユーザをインポートした場合)、これらの値はすべて`null` になります。

{% raw %}

|タグ
|---|---|
|`{{most_recently_used_device.${browser}}}` ｜ユーザーの端末で最近使用されたブラウザ。例えば、"Chrome "や "Safari "など。|
|`{{most_recently_used_device.${id}}}` ｜これはBrazeのデバイス識別子です。iOSの場合、これはApple Identifier for Vendor（IDFV）またはUUIDとなる。Androidやその他のプラットフォームでは、ランダムに生成されるUUIDとなる。|
|`{{most_recently_used_device.${carrier}}}` ｜最近使用したデバイスの電話サービスキャリア（利用可能な場合）。例としては、"Verizon "や "Orange "などがある。|
|`{{most_recently_used_device.${ad_tracking_enabled}}}` ｜デバイスが広告トラッキングを有効にしているかどうか。これはブーリアン値（`true` または`false` ）である。|
｜`{{most_recently_used_device.${idfa}}}` ｜iOSデバイスの場合、アプリケーションが私たちの[オプションのIDFAコレクション][40]で構成されている場合、この値は広告用識別子（IDFA）になります。iOS以外のデバイスの場合、この値はNULLになる。|
｜`{{most_recently_used_device.${google_ad_id}}}` ｜Androidデバイスの場合、アプリケーションがオプションのGoogle Play Advertising IDコレクションで設定されている場合、この値はGoogle Play Advertising Identifierになります。Android以外のデバイスの場合、この値はNULLになります。|
|`{{most_recently_used_device.${roku_ad_id}}}` ｜Rokuデバイスの場合、この値はアプリケーションがBrazeで設定される際に収集されるRoku Advertising Identifierになります。Roku以外のデバイスの場合、この値はNULLになります。|
|`{{most_recently_used_device.${model}}}` ｜もしあれば、デバイスのモデル名。例としては、"iPhone 6S "や "Nexus 6P"、"Firefox "などがある。|
|`{{most_recently_used_device.${os}}}` ｜もしあれば、デバイスのオペレーティング・システム。例としては、"iOS 9.2.1 "や "Android (Lollipop)"、"Windows "などがある。|
|`{{most_recently_used_device.${platform}}}` ｜もしあれば、デバイスのプラットフォーム。設定された場合、値は`ios`,`android`,`kindle`,`android_china`,`web`,`tvos` のいずれかとなる。|
{: .reset-td-br-1 .reset-td-br-2}


デバイスのキャリア、モデル名、オペレーティングシステムは多岐にわたるため、これらの値のいずれかに条件依存するリキッドを徹底的にテストすることをお勧めします。これらの値は、特定のデバイスで利用できない場合、`null` 。

## ターゲティングされたアプリ情報

アプリ内メッセージでは、Liquid内で以下のアプリ属性を使用できます。値は、アプリがメッセージングを要求するために使用するSDK APIキーに基づいています。

|タグ
|------------------|---|
|`{{app.${api_id}}}` | メッセージをリクエストするアプリのAPIキー。例えば、このキーを`abort_message()` Liquid と組み合わせて使用することで、TV プラットフォームや開発ビルドなど、別の SDK API キーを使用する特定のアプリへのアプリ内メッセージの送信を回避できます。
|`{{app.${name}}}` ｜メッセージを要求するアプリの名前（Brazeダッシュボードで定義されている）。
{: .reset-td-br-1 .reset-td-br-2}

例えば、このリキッドコードは、リクエストアプリがリストにある2つのAPIキーのうちの1つでない場合、メッセージを中止します：

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## ターゲット・デバイス情報

プッシュ通知およびアプリ内メッセージ・チャネルでは、メッセージ送信先のデバイスについて、以下の属性をテンプレート化できます。つまり、プッシュ通知やアプリ内メッセージには、メッセージを読む端末の端末属性を含めることができる。これらの属性はコンテンツ・カードでは機能しないことに注意してください。 

|タグ
|------------------|---|
|`{{targeted_device.${id}}}` ｜これはBrazeのデバイス識別子です。iOSの場合、これはApple Identifier for Vendor（IDFV）またはUUIDとなる。Androidやその他のプラットフォームでは、ランダムに生成されるUUIDとなる。|
|`{{targeted_device.${carrier}}}` ｜最近使用したデバイスの電話サービスキャリア（利用可能な場合）。例としては、"Verizon "や "Orange "などがある。|
｜`{{targeted_device.${idfa}}}` ｜iOSデバイスの場合、アプリケーションが私たちの[オプションのIDFAコレクション][40]で構成されている場合、この値は広告用識別子（IDFA）になります。iOS以外のデバイスの場合、この値はNULLになる。|
｜`{{targeted_device.${google_ad_id}}}` ｜Androidデバイスの場合、アプリケーションが[オプションのGoogle Play Advertising IDコレクション]で設定されている場合、この値はGoogle Play Advertising Identifierになります。Android以外のデバイスの場合、この値はNULLになります。|
|`{{targeted_device.${roku_ad_id}}}` ｜Rokuデバイスの場合、この値はアプリケーションがBrazeで設定される際に収集されるRoku Advertising Identifierになります。Roku以外のデバイスの場合、この値はNULLになります。|
|`{{targeted_device.${model}}}` ｜もしあれば、デバイスのモデル名。例としては、"iPhone 6S "や "Nexus 6P"、"Firefox "などがある。|
|`{{targeted_device.${os}}}` ｜もしあれば、デバイスのオペレーティング・システム。例としては、"iOS 9.2.1 "や "Android (Lollipop)"、"Windows "などがある。|
|`{{targeted_device.${platform}}}` ｜もしあれば、デバイスのプラットフォーム。設定されている場合、値は`ios` 、`android` 、`kindle` 、`android_china` 、`web` 、`tvos` のいずれかとなる。また、`most_recently_used_device` パーソナライズタグを使用することもできます。|
|`{{targeted_device.${foreground_push_enabled}}}` ｜この値は、対象デバイスがフォアグラウンド・プッシュを有効にしている場合は`true` 、そうでない場合は`false` 。|
{: .reset-td-br-1 .reset-td-br-2}


{% endraw %}


デバイスのキャリア、モデル名、オペレーティングシステムは多岐にわたるため、これらの値に条件依存するロジックは徹底的にテストすることをお勧めします。これらの値は、特定のデバイスで利用できない場合、`null` 。さらに、プッシュ通知の場合、プッシュトークンがAPI経由でインポートされた場合など、特定の状況下でBrazeがプッシュ通知に接続されたデバイスを識別できない可能性があり、その結果、これらのメッセージの値が`null` 。

プッシュ・メッセージでファースト・ネーム変数を使うとき、デフォルト値として "there "を使う例][4]。

状況によっては、デフォルト値を設定する代わりに[条件付きロジック][17]を使用することもできます。条件付きロジックでは、カスタム属性の値によって異なるメッセージを送信することができます。

さらに、条件付きロジックを使用して、NULLまたは空白の属性値を持つ顧客への[メッセージを中止する][18]ことができます。

例えば、顧客に特典残高通知を送信する場合、デフォルト値を使用して残高の少ない顧客や残高のない顧客を考慮する良い方法はありません。

この場合、デフォルト値を設定するよりも有効なオプションが2つある：

1. 残高が少ない、ゼロ、空白の顧客に対するメッセージを中止する。

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. このような顧客には、まったく別のメッセージを送ろう：

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

この例では、姓が空白またはNULLのユーザーは、"Thanks for downloading "というメッセージを受け取る。名字には[デフォルト値][47]を入れて、万が一間違えても顧客にリキッドが表示されないようにしてください。

{% endraw %}

## 可変タグ

`assign` タグを使って、メッセージ・コンポーザーに変数を作成することができます。変数を作成したら、メッセージング・ロジックやメッセージの中でその変数を参照することができます。

例えば、顧客がリワードポイントを100ポイント獲得したら、賞品と交換できるようにしたとしよう。そのため、追加で購入した場合、ポイント残高が100以上になる顧客だけにメッセージを送りたい：

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
このタグは、[コネクテッド・コンテンツ][4]機能から返されたコンテンツを再フォーマットしたい場合に便利です。詳しくはShopifyの[変数タグに関する][31]ドキュメントをご覧ください。

{% endraw %}

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていませんか？`assign` タグを何度も書き出す代わりに、そのタグをコンテンツ・ブロックとして保存し、メッセージの先頭に置くことができます。

1. [コンテンツブロックを作成]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)する。
2. コンテンツブロックに名前を付けます（スペースや特殊文字は使用しないでください）。
3. ページ下部の**Editを**クリック。
4. `assign` タグを入力する。

コンテンツ・ブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照します！
{% endalert %}

## 反復タグ

{% raw %}
反復タグは、コードのブロックを繰り返し実行するために使うことができる。この例では、`for` 。

例えば、ナイキのスニーカーのセールを開催し、ナイキに興味を示した顧客にメッセージを送るとしよう。各顧客のプロフィールには、さまざまな商品ブランドが表示されています。この配列には最大25の製品ブランドを含めることができますが、直近の5つの製品ビューの1つとしてナイキ製品を見た顧客だけにメッセージを送りたいのです。

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

この例では、閲覧されたスニーカーブランド配列の最初の5項目をチェックします。その中にconverseという項目があれば、converse\_viewerという変数を作り、trueをセットする。

そして、converse\_viewerがtrueの時にセールメッセージを送る。そうでなければ、メッセージを中止する。

これは、Brazeメッセージコンポーザーでの反復タグの使い方の簡単な例です。Shopifyの[イテレーションタグに関する][32]ドキュメントに詳しい情報があります。

## 構文タグ

構文タグは、リキッドがどのようにレンダリングされるかを制御するために使用することができます。`echo` タグを使って式を返すことができる。これは、中括弧を使って式をラップするのと同じですが、リキッドタグの中でこのタグを使うことができます。また、`liquid` タグを使用すると、各タグに区切り文字のないリキッドのブロックを持つことができます。`liquid` タグを使用する場合は、各タグを独立した行にする必要がある。より詳細な情報と例については、Shopifyの[構文タグに関する][33]ドキュメントをチェックしてください。

空白コントロール][49]を使うと、タグの周りの空白を取り除くことができます。

## HTTPステータスコード {#http-personalization}

まずローカル変数として保存し、`__http_status_code__` キーを使用することで、[Connected Content][38]呼び出しからの HTTP ステータスを利用することができます。例えば、こうだ：

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
  このキーは、エンドポイントが JSON オブジェクトを返した場合にのみ、Connected Content オブジェクトに自動的に追加されます。エンドポイントが配列や他の型を返す場合、そのキーをレスポンスに自動的に設定することはできない。
{% endalert %}

## 言語、最新のロケール、タイムゾーンに基づいたメッセージ送信

状況によっては、特定のロケールに特化したメッセージを送りたい場合もあるでしょう。例えば、ブラジルのポルトガル語は、一般的にヨーロッパのポルトガル語とは異なる。

ここでは、国際化されたメッセージをさらにローカライズするために、最新のロケールを使用する方法の例を示します。

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

この例では、最新のロケールが「pt\_BR」の顧客にはブラジルのポルトガル語のメッセージが届き、最新のロケールが「pt\_PT」の顧客にはヨーロッパのポルトガル語のメッセージが届きます。最初の2つの条件を満たさないが、言語がポルトガル語に設定されている顧客には、デフォルトのポルトガル語の言語タイプでメッセージが表示されます。

また、タイムゾーンでユーザーをターゲットにすることもできます。例えば、相手が東部標準時をベースにしている場合は1通のメッセージを送り、東部標準時をベースにしている場合は別のメッセージを送る。これを行うには、現在時刻をUTCで保存し、if/else文でユーザーの現在時刻と比較し、正しいタイムゾーンに正しいメッセージを送信していることを確認します。ユーザーが適切な時間にキャンペーンを受け取れるように、ユーザーのローカルタイムゾーンで送信するようにキャンペーンを設定する必要があります。午後2時から午後3時の間に発信されるメッセージで、各タイムゾーンに特化したメッセージを書く方法については、次の例を参照してください。

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[30]: https://shopify.dev/api/liquid/tags#syntax-tags
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[33]: https://shopify.dev/api/liquid/tags#syntax-tags
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[17]:{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[18]:{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[40]:{{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/
[43]:{{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[46]:{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/
[47]:{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
[48]:{{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword
[49]: https://shopify.github.io/liquid/basics/whitespace/
[50]:{{site.baseurl}}/help/help_articles/data/dispatch_id/
