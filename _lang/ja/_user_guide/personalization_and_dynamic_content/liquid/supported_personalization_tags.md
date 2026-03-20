---
nav_title: サポートされているパーソナライズタグ
article_title: サポートされている Liquid パーソナライゼーションタグ
page_order: 1
description: "このリファレンス記事では、サポートされている Liquid パーソナライゼーションタグの完全なリストを紹介します。"
search_rank: 1
---

# サポートされているパーソナライズタグ

> このリファレンス記事では、サポートされている Liquid パーソナライゼーションタグの完全なリストを紹介します。

## サポートされているタグの概要

便宜上、サポートされているパーソナライゼーションタグの概要を以下に示します。各タイプのタグとベストプラクティスの詳細については、引き続きお読みください。

{% raw %}

| パーソナライゼーションタグタイプ | タグ |
| -------------  | ---- |
| 標準（デフォルト）属性 | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| デバイス属性 | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>メールリスト属性</a> | `{{${set_user_to_unsubscribed_url}}}` <br>このタグは、以前の `{{${unsubscribe_url}}}` タグを置き換えるものです。古いタグは以前に作成されたメールでも機能しますが、代わりに新しいタグを使用することをお勧めします。<br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>SMS 属性</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>WhatsApp 属性</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` |
| キャンペーン属性とキャンバスステップ属性 | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| キャンバス属性 | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| カード属性 | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| ジオフェンスイベント | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| イベントプロパティ <br> (ワークスペースによって異なります) | `{{event_properties.${your_custom_event_property}}}` |
| キャンバスコンテキスト変数 | `{{context}}` |
| カスタム属性 <br> (ワークスペースによって異なります) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API トリガープロパティ</a> |`{{api_trigger_properties}}` |
| キャンバスエントリプロパティ | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### サポートされている属性

キャンペーン、カード、キャンバスの各属性は、対応するメッセージングテンプレートでのみサポートされます（例えば、`dispatch_id` はアプリ内メッセージキャンペーンでは利用できません）。

[Braze のソース間におけるこれらの属性の違い]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/)について詳しくは、こちらのヘルプ記事を参照してください。

### キャンバスとキャンペーンのタグの違い 

以下のタグはキャンバスとキャンペーンで動作が異なります。
{% raw %}
- `dispatch_id` の動作は、Braze がキャンバスのステップ（スケジュール可能なエントリステップを除く）を、スケジュール済みの場合でもトリガーイベントとして扱うため、キャンバスとキャンペーンで異なります。詳細については、[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)を参照してください。
- キャンバスで `{{campaign.${name}}}` タグを使用すると、キャンバスコンポーネント名が表示されます。このタグをキャンペーンで使用すると、キャンペーン名が表示されます。
{% endraw %}

## 最近使用されたデバイス情報

すべてのプラットフォームで、ユーザーの最新デバイスの以下の属性をテンプレート化できます。ユーザーがアプリケーションを使用していない場合（REST API 経由でユーザーをインポートした場合など）、これらの値はすべて `null` になります。

{% raw %}

|タグ | 説明 |
|---|---|
|`{{most_recently_used_device.${browser}}}` | ユーザーのデバイスで最近使用されたブラウザです。「Chrome」や「Safari」などが例として挙げられます。 |
|`{{most_recently_used_device.${id}}}` | Braze デバイス識別子です。iOS の場合、これは Apple のベンダー用識別子（IDFV）または UUID になります。Android などのプラットフォームでは、ランダムに生成された UUID です。 |
| `{{most_recently_used_device.${carrier}}}` | 利用可能であれば、直近で使用したデバイスの電話サービスキャリアです。「Verizon」や「Orange」などが例として挙げられます。 |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | デバイスで広告トラッキングが有効かどうかを示します。これはブール値（`true` または `false`）です。 |
| `{{most_recently_used_device.${idfa}}}` | iOS デバイスの場合、アプリケーションが[オプションの IDFA コレクション]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)で設定されていれば、この値は広告識別子（IDFA）になります。iOS 以外のデバイスの場合、この値は null になります。 |
| `{{most_recently_used_device.${google_ad_id}}}` | Android デバイスの場合、オプションの Google Play 広告 ID コレクションでアプリケーションが設定されていれば、この値は Google Play の広告識別子になります。Android 以外のデバイスの場合、この値は null になります。 |
| `{{most_recently_used_device.${roku_ad_id}}}` | Roku デバイスの場合、この値はアプリケーションが Braze で設定される際に収集される Roku 広告識別子になります。Roku 以外のデバイスの場合、この値は null になります。 |
| `{{most_recently_used_device.${model}}}` | 利用可能であれば、デバイスのモデル名です。「iPhone 6S」や「Nexus 6P」、「Firefox」などが例として挙げられます。 |
| `{{most_recently_used_device.${os}}}` | 利用可能であれば、デバイスのオペレーティングシステムです。「iOS 9.2.1」や「Android (Lollipop)」、「Windows」などが例として挙げられます。 |
| `{{most_recently_used_device.${platform}}}` | 利用可能であれば、デバイスのプラットフォームです。設定されている場合、値は `ios`、`android`、`kindle`、`android_china`、`web`、または `tvos` のいずれかになります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デバイスキャリア、モデル名、およびオペレーティングシステムにはさまざまな種類があるため、これらの値のいずれかに条件付きで依存する Liquid を徹底的にテストすることをお勧めします。特定のデバイスでこれらの値が利用できない場合、値は `null` になります。

## 対象アプリの情報

アプリ内メッセージでは、Liquid 内で以下のアプリ属性を使用できます。この値は、アプリがメッセージングをリクエストするために使用する SDK API キーに基づきます。

|タグ | 説明 |
|------------------|---|
| `{{app.${api_id}}}` | メッセージをリクエストするアプリの API キーです。例えば、このキーを Liquid の `abort_message()` と組み合わせて使用して、別の SDK API キーを使用する TV プラットフォームや開発ビルドなどの特定のアプリに対して、アプリ内メッセージの送信を防止できます。|
| `{{app.${name}}}` | メッセージをリクエストするアプリ名（Braze ダッシュボードで定義されている名前）です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

例えば、以下の Liquid コードは、リクエストするアプリがリスト内の 2 つの API キーのいずれでもない場合にメッセージを中止します。

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## ターゲットデバイス情報

プッシュ通知、アプリ内メッセージ、バナーについては、メッセージを受信するデバイス向けに以下の属性をテンプレート化できます。プッシュ通知、アプリ内メッセージ、またはバナーには、ユーザーがメッセージを読むデバイスの属性を含めることができます。これらの属性はコンテンツカードやメールでは機能しません。メールの場合、メッセージは送信前にレンダリングされるため、ユーザーがメールを開封するデバイスはその時点では不明です。

|タグ | 説明 |
|------------------|---|
| `{{targeted_device.${id}}}` | Braze デバイス識別子です。iOS の場合、これは Apple のベンダー用識別子（IDFV）または UUID になります。Android などのプラットフォームでは、ランダムに生成された UUID です。例えば、ユーザーが 5 つのデバイスを持っている場合、5 つのデバイスすべてに対して送信が試行され、それぞれに対応するデバイス識別子が使用されます。ユーザーの最後に使用したデバイスにメッセージを送信するように設定されている場合、Braze で識別された最後に使用されたデバイスに対して送信が 1 回だけ試行されます。 |
| `{{targeted_device.${carrier}}}` | 利用可能であれば、直近で使用したデバイスの電話サービスキャリアです。「Verizon」や「Orange」などが例として挙げられます。 |
| `{{targeted_device.${idfa}}}` | iOS デバイスの場合、アプリケーションが[オプションの IDFA コレクション]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)で設定されていれば、この値は広告識別子（IDFA）になります。iOS 以外のデバイスの場合、この値は null になります。 |
| `{{targeted_device.${google_ad_id}}}` | Android デバイスの場合、アプリケーションが[オプションの Google Play 広告識別子コレクション]で設定されていれば、この値は Google Play 広告識別子になります。Android 以外のデバイスの場合、この値は null になります。 |
| `{{targeted_device.${roku_ad_id}}}` | Roku デバイスの場合、この値はアプリケーションが Braze で設定される際に収集される Roku 広告識別子になります。Roku 以外のデバイスの場合、この値は null になります。 |
| `{{targeted_device.${model}}}` | 利用可能であれば、デバイスのモデル名です。「iPhone 6S」や「Nexus 6P」、「Firefox」などが例として挙げられます。 |
| `{{targeted_device.${os}}}` | 利用可能であれば、デバイスのオペレーティングシステムです。「iOS 9.2.1」や「Android (Lollipop)」、「Windows」などが例として挙げられます。 |
| `{{targeted_device.${platform}}}` | 利用可能であれば、デバイスのプラットフォームです。設定されている場合、値は `ios`、`android`、`kindle`、`android_china`、`web`、または `tvos` のいずれかになります。パーソナライゼーションタグ `most_recently_used_device` も使用できます。 |
| `{{targeted_device.${foreground_push_enabled}}}` | この値は、対象デバイスでフォアグラウンドのプッシュ通知が有効な場合に `true`、無効の場合に `false` になります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

デバイスキャリア、モデル名、およびオペレーティングシステムにはさまざまな種類があるため、これらの値のいずれかに条件付きで依存するロジックを徹底的にテストすることをお勧めします。特定のデバイスでこれらの値が利用できない場合、値は `null` になります。 

さらに、プッシュ通知では、プッシュトークンが API を介してインポートされた場合など、特定の状況下で Braze がプッシュ通知に紐づくデバイスを判別できないことがあります。その結果、これらのメッセージの値は `null` になります。

![プッシュメッセージで名の変数を使用する際にデフォルト値「there」を使用する例。]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### デフォルト値の代わりに条件付きロジックを使用する

状況によっては、デフォルト値を設定する代わりに[条件付きロジック]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/)を使用することもできます。条件付きロジックでは、カスタム属性の値によって異なるメッセージを送信できます。さらに、条件付きロジックを使用して、null または空白の属性値を持つ顧客への[メッセージを中止]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)できます。 

#### ユースケース

例えば、顧客に報酬残高通知を送信するとします。デフォルト値を使用して、残高が少ない顧客や null の顧客に適切に対応する方法はありません。

この場合、デフォルト値を設定するよりも効果的なオプションが 2 つあります。

1. 残高が少ない、null、および空白の顧客に対するメッセージを中止します。

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. このような顧客にはまったく別のメッセージを送信します。

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

このユースケースでは、名が空白または null のユーザーは「Thanks for downloading!」というメッセージを受け取ります。名には[デフォルト値]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/)を含めて、間違いがあった場合に顧客に Liquid が表示されないようにする必要があります。

{% endraw %}

## 変数タグ

メッセージ作成画面で、`assign` タグを使用して変数を作成できます。変数には一意の名前を使用することをお勧めします。サポートされているパーソナライゼーションタグ（`language` など）と同じ名前の変数を作成すると、メッセージングロジックに影響する可能性があります。

変数を作成したら、メッセージングロジックやメッセージの中でその変数を参照できます。このタグは、[コネクテッドコンテンツ]({% image_buster /assets/img_archive/personalized_firstname_.png %})機能から返されたコンテンツを再フォーマットしたいときに便利です。詳しくは、Shopify の[変数タグに関するドキュメント](https://docs.shopify.com/themes/liquid/tags/variable-tags)を参照してください。

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていませんか？`assign` タグを何度も書き出す代わりに、そのタグをコンテンツブロックとして保存し、メッセージの先頭に配置できます。

1. [コンテンツブロックを作成]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)します。
2. コンテンツブロックに名前を付けます（スペースや特殊文字は使用しないでください）。
3. ページ下部の [**編集**] を選択します。
4. `assign` タグを入力します。

コンテンツブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照します。
{% endalert %}

### ユースケース

例えば、顧客が 100 ポイントの報酬ポイントを獲得した後に、報酬ポイントを賞品に交換できるようにするとします。つまり、追加購入をした場合にポイント残高が 100 以上になる顧客だけにメッセージを送りたいとします。

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## 反復タグ

{% raw %}
反復タグは、コードのブロックを繰り返し実行するために使用できます。以下のユースケースでは、`for` タグを使用しています。

### ユースケース

例えば、Nike のスニーカーのセールを開催し、Nike に興味を示した顧客にメッセージを送信するとします。各顧客のプロファイルには、閲覧した製品ブランドの配列があります。この配列には最大 25 の製品ブランドが含まれている可能性がありますが、最新の製品ビュー 5 つのうちの 1 つとして Nike 製品を閲覧した顧客にのみメッセージを送信したいとします。

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

このユースケースでは、閲覧されたスニーカーブランドの配列の最初の 5 項目をチェックします。これらの項目のいずれかが Converse であれば、`converse_viewer` 変数を作成し、true に設定します。

そして、`converse_viewer` が true のときにセールメッセージを送信します。それ以外の場合は、メッセージを中止します。

これは、Braze メッセージ作成画面での反復タグの使い方の簡単な例です。詳細については、Shopify の[反復タグに関するドキュメント](https://docs.shopify.com/themes/liquid/tags/iteration-tags)を参照してください。

## 構文タグ

構文タグを使用して、Liquid のレンダリング方法を制御できます。`echo` タグを使用して式を返すことができます。これは中括弧を使って式をラップするのと同じですが、Liquid タグの中でこのタグを使用できます。また、`liquid` タグを使用して、各タグに区切り文字を使用せずに Liquid のブロックを記述することもできます。`liquid` タグを使用する場合、各タグは個別の行に配置する必要があります。詳細な情報と例については、Shopify の[構文タグに関するドキュメント](https://shopify.dev/api/liquid/tags#syntax-tags)を参照してください。

[ホワイトスペースコントロール](https://shopify.github.io/liquid/basics/whitespace/)を使用すると、タグの周りのホワイトスペースを削除でき、Liquid 出力の外観をさらに制御できます。

## HTTP ステータスコード {#http-personalization}

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)の呼び出しから HTTP ステータスを使用するには、まず HTTP ステータスをローカル変数として保存してから、`__http_status_code__` キーを使用します。以下に例を示します。

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
このキーは、エンドポイントが JSON オブジェクトを返す場合にのみ、コネクテッドコンテンツオブジェクトに自動的に追加されます。エンドポイントが配列やその他の型を返す場合、そのキーはレスポンスで自動的に設定できません。
{% endalert %}

## 言語、最新のロケール、タイムゾーンに基づいてメッセージを送信する

状況によっては、特定のロケールに固有のメッセージを送信したい場合があります。例えば、ブラジルのポルトガル語は一般的にヨーロッパのポルトガル語とは異なります。

### ユースケース: 最新のロケールに基づいてローカライズする

ここでは、最新のロケールを使用して、国際化されたメッセージをさらにローカライズするユースケースを紹介します。

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

このユースケースでは、直近のロケールが `pt_BR` の顧客にはブラジルポルトガル語のメッセージが、直近のロケールが `pt_PT` の顧客にはヨーロッパポルトガル語のメッセージが表示されます。最初の 2 つの条件を満たさないが、言語をポルトガル語に設定している顧客は、デフォルトに設定したポルトガル語のタイプでメッセージを受け取ります。

### ユースケース: タイムゾーン別にユーザーをターゲットする

タイムゾーンでユーザーをターゲットすることもできます。例えば、EST のユーザーにはあるメッセージ、PST のユーザーには別のメッセージを送信します。そのためには、現在時刻を UTC で保存し、if/else 文でユーザーの現在時刻と比較して、適切なタイムゾーンに適切なメッセージを送信します。ユーザーのローカルタイムゾーンでキャンペーンを送信するように設定し、適切な時間にキャンペーンを届ける必要があります。 

午後 2 時から 3 時の間に送信され、各タイムゾーンに固有のメッセージを作成する方法については、以下のユースケースを参照してください。

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

## ランダムな数値でメッセージを送信する

{% raw %}
`{% random %}` タグはランダムな数値を返します。A/B テスト風のロジック、サンプリング、メッセージコンテンツのバリエーションに使用できます。

| タグ | 説明 |
|-------|--------------|
| `{% random %}` | 0 以上 1 未満の浮動小数点数（0 を含み、1 を含まない）です。 |
| `{% random 10 %}` (整数引数) | 0 以上、指定した整数未満の整数です。例えば、`{% random 10 %}` は 0 から 9 の整数を返します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### ユースケース: ユーザーにランダムなバリアントを送信する

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags