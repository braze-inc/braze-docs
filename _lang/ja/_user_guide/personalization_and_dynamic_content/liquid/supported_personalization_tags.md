---
nav_title: 対応パーソナライズタグ
article_title: 対応リキッド・パーソナライゼーション・タグ
page_order: 1
description: "このリファレンス記事は、サポートされているリキッドパーソナライゼーションタグの完全なリストをカバーしている。"
search_rank: 1
---

# 対応パーソナライズタグ

> このリファレンス記事は、サポートされているリキッドパーソナライゼーションタグの完全なリストをカバーしている。

便宜上、サポートされているパーソナライゼーション・タグの概要を示す。各タグの詳細とベストプラクティスについては、このまま読み進めてほしい。

{% raw %}

| 名入れタグタイプ | tags |
| -------------  | ---- |
| 標準（デフォルト）属性 | `{{${city}}}`<br> `{{${country}}}`<br> `{{${date_of_birth}}}`<br> `{{${email_address}}}`<br> `{{${first_name}}}`<br> `{{${gender}}}`<br> `{{${language}}}`<br> `{{${last_name}}}`<br> `{{${last_used_app_date}}}`<br> `{{${most_recent_app_version}}}`<br> `{{${most_recent_locale}}}`<br> `{{${most_recent_location}}}`<br> `{{${phone_number}}}`<br> `{{${time_zone}}}`<br> `{{${user_id}}}`<br> `{{${braze_id}}}`<br> `{{${random_bucket_number}}}`<br> `{{subscribed_state.${email_global}}}`<br> `{{subscribed_state.${subscription_group_id}}}` |
| デバイス属性 | `{{most_recently_used_device.${carrier}}}`<br> `{{most_recently_used_device.${id}}}`<br> `{{most_recently_used_device.${idfa}}}`<br> `{{most_recently_used_device.${model}}}`<br> `{{most_recently_used_device.${os}}}`<br> `{{most_recently_used_device.${platform}}}`<br> `{{most_recently_used_device.${google_ad_id}}}`<br> `{{most_recently_used_device.${roku_ad_id}}}`<br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| \[電子メールリストの属性][43] | `{{${set_user_to_unsubscribed_url}}}`<br>このタグは、以前の`{{${unsubscribe_url}}}` 。古いタグは以前に作成されたEメールでも機能するが、代わりに新しいタグを使用することをお勧めする。<br><br> `{{${set_user_to_subscribed_url}}}`<br> `{{${set_user_to_opted_in_url}}}`|
| \[SMSの属性][48] | `{{sms.${inbound_message_body}}}`<br> `{{sms.${inbound_media_urls}}}` |
| \[WhatsAppの属性][46] | `{{whats_app.${inbound_message_body}}}`<br> `{{whats_app.${inbound_media_urls}}}` |
| キャンペーン属性 | `{{campaign.${api_id}}}`<br> `{{campaign.${dispatch_id}}}`<br> `{{campaign.${name}}}`<br> `{{campaign.${message_name}}}`<br> `{{campaign.${message_api_id}}}` |
| キャンバスの属性 | `{{canvas.${name}}}`<br> `{{canvas.${api_id}}}`<br> `{{canvas.${variant_name}}}`<br> `{{canvas.${variant_api_id}}}` |
| キャンバス・ステップの属性 | `{{campaign.${api_id}}}`<br> `{{campaign.${dispatch_id}}}`<br> `{{campaign.${name}}}`<br> `{{campaign.${message_name}}}`<br> `{{campaign.${message_api_id}}}` |
| カード属性 | `{{card.${api_id}}}`<br> `{{card.${name}}}` |
| ジオフェンシング・イベント | `{{event_properties.${geofence_name}}}`<br> `{{event_properties.${geofence_set_name}}}` |
| イベントプロパティ <br> (これらはあなたのワークスペースに合わせてカスタマイズされる）。| `{{event_properties.${your_custom_event_property}}}` |
| キャンバスエントリのプロパティ| `{{canvas_entry_properties}}` |
| カスタム属性 <br> (これらはあなたのワークスペースに合わせてカスタマイズされる）。 | `{{custom_attribute.${your_custom_attribute}}}` |
| \[APIトリガープロパティ][75] |`{{api_trigger_properties}}` |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

[Brazeのソース間でこれらの属性がどのように異なるかについては]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/)、このヘルプ記事を参照のこと。

{% alert important %}
Campaign、Card、Canvas属性は、対応するメッセージングテンプレートでのみサポートされる（例えば、`dispatch_id` はアプリ内メッセージキャンペーンでは利用できない）。
{% endalert %}

#### キャンバスとキャンペーンタグの違い 

以下のタグはキャンバスとキャンペーンで動作が異なる：
{% raw %}
- `dispatch_id` Brazeは、キャンバスのステップを、たとえ「スケジュール」されていても、トリガーされたイベントとして扱うからだ（スケジュール可能なエントリーステップを除く）。詳しくは、\[派遣IDの動作][50] を参照のこと。
- Canvasで`{{campaign.${name}}}` タグを使用すると、Canvasコンポーネント名が表示される。このタグをキャンペーンで使用すると、キャンペーン名が表示される。
{% endraw %}

## 最近使用されたデバイス情報

すべてのプラットフォームで、ユーザーの最新のデバイスについて、以下の属性をテンプレート化することができる。ユーザーがアプリケーションを使用していない場合（たとえば、REST API経由でユーザーをインポートした場合）、これらの値はすべて`null` になる。

{% raw %}

|タグ | 説明 |
|---|---|
|`{{most_recently_used_device.${browser}}}` | ユーザーの端末で最近使用されたブラウザ。Chrome」や「Safari」などがその例だ。 |
|`{{most_recently_used_device.${id}}}` | これはBrazeのデバイス識別子である。iOSの場合、これはApple Identifier for Vendor（IDFV）またはUUIDとなる。Androidやその他のプラットフォームでは、ランダムに生成されるUUIDとなる。 |
| `{{most_recently_used_device.${carrier}}}` | 利用可能であれば、直近で使用したデバイスの電話サービスキャリア。例えば、「ベライゾン」や「オレンジ」などである。 |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | デバイスが広告トラッキングを有効にしているかどうか。これはブーリアン値（`true` または`false` ）である。 |
| `{{most_recently_used_device.${idfa}}}` | iOSデバイスの場合、アプリケーションが\[オプションのIDFAコレクション][40]]で構成されている場合、この値は広告用識別子（IDFA）になる。iOS以外のデバイスの場合、この値はNULLになる。 |
| `{{most_recently_used_device.${google_ad_id}}}` | Androidデバイスの場合、アプリケーションがオプションのGoogle Play Advertising IDコレクションで設定されている場合、この値はGoogle Play Advertising Identifierになる。Android以外のデバイスの場合、この値はNULLになる。 |
| `{{most_recently_used_device.${roku_ad_id}}}` | Rokuデバイスの場合、この値は、アプリケーションがBrazeで設定される際に収集されるRoku Advertising Identifierとなる。Roku以外のデバイスの場合、この値はNULLになる。 |
| `{{most_recently_used_device.${model}}}` | もしあれば、デバイスのモデル名。例えば、「iPhone 6S」や「Nexus 6P」、「Firefox」などだ。 |
| `{{most_recently_used_device.${os}}}` | もしあれば、デバイスのオペレーティングシステム。例えば、「iOS 9.2.1」や「アンドロイド（ロリポップ）」、「ウィンドウズ」などだ。 |
| `{{most_recently_used_device.${platform}}}` | もしあれば、デバイスのプラットフォーム。設定されている場合、値は`ios` 、`android` 、`kindle` 、`android_china` 、`web` 、`tvos` のいずれかとなる。 |
{: .reset-td-br-1 .reset-td-br-2}


デバイスのキャリア、モデル名、オペレーティングシステムは多岐にわたるため、これらの値のいずれかに条件依存するリキッドは、徹底的にテストすることをお勧めする。これらの値が特定のデバイスで利用できない場合は、`null` 。

## ターゲットを絞ったアプリ情報

アプリ内メッセージでは、Liquid内で以下のアプリ属性を使用できる。値は、アプリがどのSDK APIキーを使ってメッセージングをリクエストするかに基づいている。

|タグ | 説明 |
|------------------|---|
| `{{app.${api_id}}}` | メッセージを要求するアプリのAPIキー。例えば、`abort_message()` Liquidと組み合わせてこのキーを使用し、TVプラットフォームや別のSDK APIキーを使用する開発ビルドなど、特定のアプリへのアプリ内メッセージの送信を回避する。|
| `{{app.${name}}}` | メッセージを要求するアプリの名前（Brazeダッシュボードで定義されている）。|
{: .reset-td-br-1 .reset-td-br-2}

例えば、このリキッドコードは、リクエストアプリがリストにある2つのAPIキーのうちの1つでない場合、メッセージを中止する：

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## ターゲット・デバイス情報

プッシュ通知とアプリ内メッセージ・チャンネルでは、メッセージを送信するデバイスの属性を以下のようにテンプレート化できる。つまり、プッシュ通知やアプリ内メッセージには、メッセージを読む端末の端末属性を含めることができる。これらの属性はコンテンツ・カードでは機能しないことに注意しよう。 

|タグ | 説明 |
|------------------|---|
| `{{targeted_device.${id}}}` | これはBrazeのデバイス識別子である。iOSの場合、これはApple Identifier for Vendor（IDFV）またはUUIDとなる。Androidやその他のプラットフォームでは、ランダムに生成されるUUIDとなる。 |
| `{{targeted_device.${carrier}}}` | 利用可能であれば、直近で使用したデバイスの電話サービスキャリア。例えば、「ベライゾン」や「オレンジ」などである。 |
| `{{targeted_device.${idfa}}}` | iOSデバイスの場合、アプリケーションが\[オプションのIDFAコレクション][40]]で構成されている場合、この値は広告用識別子（IDFA）になる。iOS以外のデバイスの場合、この値はNULLになる。 |
| `{{targeted_device.${google_ad_id}}}` | Androidデバイスの場合、アプリケーションが\[オプションのGoogle Play Advertising IDコレクション]]で設定されている場合、この値はGoogle Play Advertising Identifierになる。Android以外のデバイスの場合、この値はNULLになる。 |
| `{{targeted_device.${roku_ad_id}}}` | Rokuデバイスの場合、この値は、アプリケーションがBrazeで設定される際に収集されるRoku Advertising Identifierとなる。Roku以外のデバイスの場合、この値はNULLになる。 |
| `{{targeted_device.${model}}}` | もしあれば、デバイスのモデル名。例えば、「iPhone 6S」や「Nexus 6P」、「Firefox」などだ。 |
| `{{targeted_device.${os}}}` | もしあれば、デバイスのオペレーティングシステム。例えば、「iOS 9.2.1」や「アンドロイド（ロリポップ）」、「ウィンドウズ」などだ。 |
| `{{targeted_device.${platform}}}` | もしあれば、デバイスのプラットフォーム。設定されている場合、値は`ios` 、`android` 、`kindle` 、`android_china` 、`web` 、`tvos` のいずれかとなる。また、`most_recently_used_device` パーソナライゼーション・タグを使うこともできる。 |
| `{{targeted_device.${foreground_push_enabled}}}` | この値は、対象デバイスがフォアグラウンド・プッシュを有効にしている場合は`true` 、そうでない場合は`false` 。 |
{: .reset-td-br-1 .reset-td-br-2}


{% endraw %}


デバイスのキャリア、モデル名、オペレーティングシステムは多岐にわたるため、これらの値に条件依存するロジックは徹底的にテストすることをお勧めする。これらの値が特定のデバイスで利用できない場合は、`null` 。さらに、プッシュ通知の場合、プッシュトークンがAPI経由でインポートされた場合など、特定の状況下でBrazeがプッシュ通知に接続されたデバイスを識別できない可能性があり、その結果、それらのメッセージの値が`null` 。

![プッシュ・メッセージでファーストネーム変数を使うときにデフォルト値「there」を使う例。][4]

状況によっては、デフォルト値を設定する代わりに\[条件付きロジック][17] ]を使用することもできる。条件付きロジックでは、カスタム属性の値によって異なるメッセージを送信することができる。

さらに、条件付きロジックを使用して、NULLまたは空白の属性値を持つ顧客への\[中止メッセージ][18] ]を作成することもできる。

例えば、顧客に特典残高通知を送信する場合、デフォルト値を使用して残高の少ない顧客や残高のない顧客を考慮する良い方法はない。

この場合、デフォルト値を設定するよりも効果的なオプションが2つある：

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

この例では、姓が空白またはNULLのユーザーは、"Thanks for downloading "というメッセージを受け取る。名字には\[デフォルト値][47] ]を入れて、万が一間違えても顧客にリキッドが表示されないようにすべきである。

{% endraw %}

## 可変タグ

`assign` タグを使って、メッセージ・コンポーザーに変数を作ることができる。変数を作成したら、メッセージング・ロジックやメッセージの中でその変数を参照できる。

例えば、顧客が100ポイント貯まったら、そのポイントを賞品と交換できるようにしたとしよう。つまり、追加購入をした場合、ポイント残高が100以上になる顧客だけにメッセージを送りたいわけだ：

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
このタグは、\[Connected Content][4] ]機能から返されたコンテンツを再フォーマットしたいときに便利だ。詳しくは、Shopifyの[変数タグに関する][31]ドキュメントを参照されたい。

{% endraw %}

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていることに気づいているか？`assign` タグを何度も書き出す代わりに、そのタグをコンテンツ・ブロックとして保存し、メッセージの先頭に置くことができる。

1. [コンテンツブロックを作成する]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)。
2. コンテンツブロックに名前をつける（スペースや特殊文字は使わない）。
3. ページ下部の**Editを**クリックする。
4. `assign` タグを入力する。

コンテンツ・ブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照することになる！
{% endalert %}

## 反復タグ

{% raw %}
反復タグは、コードのブロックを繰り返し実行するために使うことができる。この例では、`for` 。

例えば、ナイキのスニーカーのセールを開催し、ナイキに興味を示した顧客にメッセージを送るとしよう。各顧客のプロフィールには、さまざまな商品ブランドが表示されている。この配列には最大25の製品ブランドを含めることができるが、直近の5つの製品ビューの1つとしてナイキ製品を見た顧客だけにメッセージを送りたい。

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

この例では、閲覧されたスニーカーブランドの配列の最初の5項目をチェックする。それらの項目の1つがconverseであれば、converse_viewer変数を作り、それをtrueに設定する。

そして、converse_viewerがtrueのときにセール・メッセージを送る。そうでなければ、メッセージを中止する。

これは、Brazeメッセージコンポーザーでの反復タグの使い方の簡単な例である。Shopifyの[イテレーションタグに関する][32]ドキュメントに詳細がある。

## 構文タグ

シンタックスタグは、リキッドがどのようにレンダリングされるかをコントロールするために使うことができる。`echo` 、式を返すことができる。これは、中括弧を使って式をラップするのと同じだが、リキッドタグの中でこのタグを使うことができる。また、`liquid` タグを使えば、各タグに区切りのないリキッドのブロックを持つことができる。`liquid` 、それぞれのタグは1行にまとめなければならない。より詳細な情報と例については、Shopifyの[構文タグに関する][33]ドキュメントをチェックしよう。

\[空白コントロール][49]] を使用すると、タグの周りの空白を削除でき、リキッド出力の外観をさらにコントロールするのに役立ちます。

## HTTPステータスコード {#http-personalization}

[コネクテッドコンテンツ][38] コールからのHTTPステータスをローカル変数として保存し、次に`__http_status_code__`キーを使用することで利用できます。以下に例を示します。

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
  このキーは、エンドポイントがJSONオブジェクトを返した場合にのみ、Connected Contentオブジェクトに自動的に追加される。エンドポイントが配列や他の型を返す場合、そのキーをレスポンスに自動的に設定することはできない。
{% endalert %}

## 言語、最新のロケール、タイムゾーンに基づいてメッセージを送信する

状況によっては、特定のロケールに特化したメッセージを送りたい場合もあるだろう。例えば、ブラジルのポルトガル語は一般的にヨーロッパのポルトガル語とは異なる。

以下は、国際化されたメッセージをさらにローカライズするために、最新のロケールを使用する方法の例である。

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

この例では、最新のロケールが「pt_BR」である顧客にはブラジルのポルトガル語のメッセージが届き、最新のロケールが「pt_PT」である顧客にはヨーロッパのポルトガル語のメッセージが届く。最初の2つの条件を満たさないが、言語がポルトガル語に設定されている顧客には、デフォルトのポルトガル語の言語タイプでメッセージが表示される。

また、タイムゾーンでユーザーをターゲットにすることもできる。例えば、相手が東部標準時をベースにしている場合は1通のメッセージを送り、東部標準時をベースにしている場合は別のメッセージを送る。これを行うには、現在時刻をUTCで保存し、if/else文でユーザーの現在時刻と比較し、正しいタイムゾーンに正しいメッセージを送信していることを確認する。ユーザーが適切な時間にキャンペーンを受け取れるように、ユーザーのローカルタイムゾーンで送信するようにキャンペーンを設定する必要がある。午後2時から3時の間に発信され、各タイムゾーンに固有のメッセージを持つメッセージの書き方については、以下の例を参照のこと。

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
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/
[43]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/
[47]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword
[49]: https://shopify.github.io/liquid/basics/whitespace/
[50]: {{site.baseurl}}/help/help_articles/data/dispatch_id/
[75]: {{site.baseurl}}/api/objects_filters/trigger_properties_object/
