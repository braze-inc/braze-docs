---
nav_title: 対応パーソナライズタグ
article_title: 対応リキッド・パーソナライゼーション・タグ
page_order: 1
description: "このリファレンス記事は、サポートされているリキッドパーソナライゼーションタグの完全なリストをカバーしている。"
search_rank: 1
---

# 対応パーソナライズタグ

> このリファレンス記事は、サポートされているリキッドパーソナライゼーションタグの完全なリストをカバーしている。

## 対応タグの概要

便宜上、サポートされているパーソナライゼーション・タグの概要を示す。各タイプのタグとベストプラクティスの詳細については、引き続きお読みください。

{% raw %}

| パーソナライゼーション・タグタイプ | tags |
| -------------  | ---- |
| 標準（デフォルト）属性 | `{{${city}}}`<br> `{{${country}}}`<br> `{{${date_of_birth}}}`<br> `{{${email_address}}}`<br> `{{${first_name}}}`<br> `{{${gender}}}`<br> `{{${language}}}`<br> `{{${last_name}}}`<br> `{{${last_used_app_date}}}`<br> `{{${most_recent_app_version}}}`<br> `{{${most_recent_locale}}}`<br> `{{${most_recent_location}}}`<br> `{{${phone_number}}}`<br> `{{${time_zone}}}`<br> `{{${user_id}}}`<br> `{{${braze_id}}}`<br> `{{${random_bucket_number}}}`<br> `{{subscribed_state.${email_global}}}`<br> `{{subscribed_state.${subscription_group_id}}}` |
| デバイス属性 | `{{most_recently_used_device.${carrier}}}`<br> `{{most_recently_used_device.${id}}}`<br> `{{most_recently_used_device.${idfa}}}`<br> `{{most_recently_used_device.${model}}}`<br> `{{most_recently_used_device.${os}}}`<br> `{{most_recently_used_device.${platform}}}`<br> `{{most_recently_used_device.${google_ad_id}}}`<br> `{{most_recently_used_device.${roku_ad_id}}}`<br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>メールリストの属性</a> | `{{${set_user_to_unsubscribed_url}}}`<br>このタグは、以前の `{{${unsubscribe_url}}}` タグを置き換えるものです。古いタグは以前に作成されたEメールでも機能するが、代わりに新しいタグを使用することをお勧めする。<br><br> `{{${set_user_to_subscribed_url}}}`<br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>SMS属性</a> | `{{sms.${inbound_message_body}}}`<br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>WhatsApp 属性</a> | `{{whats_app.${inbound_message_body}}}`<br> `{{whats_app.${inbound_media_urls}}}`<br> `{{whats_app.${inbound_flow_response}}}`<br> `{{whats_app.${inbound_product_id}}}`<br> `{{whats_app.${inbound_catalog_id}}}` |
| キャンペーン属性 | `{{campaign.${api_id}}}`<br> `{{campaign.${dispatch_id}}}`<br> `{{campaign.${name}}}`<br> `{{campaign.${message_name}}}`<br> `{{campaign.${message_api_id}}}` |
| キャンバスの属性 | `{{canvas.${name}}}`<br> `{{canvas.${api_id}}}`<br> `{{canvas.${variant_name}}}`<br> `{{canvas.${variant_api_id}}}` |
| キャンバス・ステップの属性 | `{{campaign.${api_id}}}`<br> `{{campaign.${dispatch_id}}}`<br> `{{campaign.${name}}}`<br> `{{campaign.${message_name}}}`<br> `{{campaign.${message_api_id}}}` |
| カード属性 | `{{card.${api_id}}}`<br> `{{card.${name}}}` |
| ジオフェンス関連イベント | `{{event_properties.${geofence_name}}}`<br> `{{event_properties.${geofence_set_name}}}` |
| イベントプロパティ <br> (ワークスペースによって異なる)| `{{event_properties.${your_custom_event_property}}}` |
| キャンバスのコンテキスト変数 | `{{context}}` |
| カスタム属性 <br> (ワークスペースによって異なる) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API トリガーのプロパティ</a> |`{{api_trigger_properties}}` |
| キャンバスエントリのプロパティ | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### サポートされている属性

キャンペーン、カード、キャンバスの各属性は、対応するメッセージングテンプレートでのみサポートされる（例えば、`dispatch_id` はアプリ内メッセージキャンペーンでは利用できない）。

詳細については、[Braze のソース間におけるこれらの属性の違い]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/)に関するヘルプ記事を参照してください。

### キャンバスとキャンペーンタグの違い 

以下のタグはキャンバスとキャンペーンで動作が異なる：
{% raw %}
- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーイベントとして扱うためです。詳細については、[ディスパッチIDの動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)を参照してください。
- キャンバスで `{{campaign.${name}}}` タグを使用すると、キャンバスコンポーネント名が表示されます。このタグをキャンペーンで使用すると、キャンペーン名が表示される。
{% endraw %}

## 最近使用されたデバイス情報

すべてのプラットフォームで、ユーザーの最新デバイスの次の属性をテンプレート化できます。ユーザーがアプリケーションを使用していない場合 (REST API 経由でユーザーをインポートした場合など)、これらの値はすべて `null` になります。

{% raw %}

|タグ | 説明 |
|---|---|
|`{{most_recently_used_device.${browser}}}` | ユーザーの端末で最近使用されたブラウザ。Chrome」や「Safari」などがその例だ。 |
|`{{most_recently_used_device.${id}}}` | Braze デバイス識別子。iOS の場合、これは Apple のベンダー用識別子 (IDFV) または UUID になります。Android などのプラットフォームでは、ランダムに生成されたUUID です。 |
| `{{most_recently_used_device.${carrier}}}` | 利用可能であれば、直近で使用したデバイスの電話サービスキャリア。例えば、「Verizon」や「Orange」などです。 |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | デバイスが広告トラッキングを有効にしているかどうか。これはブーリアン値（`true` または`false` ）である。 |
| `{{most_recently_used_device.${idfa}}}` | iOS デバイスの場合、アプリケーションが[ オプションのIDFA コレクション]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) で設定されている場合、この値はAdvertising (IDFA) の識別子になります。iOS以外のデバイスの場合、この値はNULLになる。 |
| `{{most_recently_used_device.${google_ad_id}}}` | Android デバイスの場合、当社オプションの Google Play 広告 ID コレクションでお客様のアプリケーションが設定されていれば、この値は Google Play の広告識別子になります。Android以外のデバイスの場合、この値はNULLになる。 |
| `{{most_recently_used_device.${roku_ad_id}}}` | Rokuデバイスの場合、この値は、アプリケーションがBrazeで設定される際に収集されるRoku Advertising Identifierとなる。Roku以外のデバイスの場合、この値はNULLになる。 |
| `{{most_recently_used_device.${model}}}` | もしあれば、デバイスのモデル名。例えば、「iPhone 6S」や「Nexus 6P」、「Firefox」などだ。 |
| `{{most_recently_used_device.${os}}}` | もしあれば、デバイスのオペレーティングシステム。例えば、「iOS 9.2.1」や「アンドロイド（ロリポップ）」、「ウィンドウズ」などだ。 |
| `{{most_recently_used_device.${platform}}}` | もしあれば、デバイスのプラットフォーム。設定されている場合、値は `ios`、`android`、`kindle`、`android_china`、`web`、または `tvos` のいずれかになります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デバイスキャリア、モデル名、およびオペレーティングシステムにはさまざまな種類があるため、これらの値のいずれかに条件付きで依存するLiquid を徹底的にテストすることをお勧めします。特定のデバイスについてこれらの値が該当しない場合、値は `null` になります。

## 対象アプリの情報

アプリ内メッセージでは、Liquid内で以下のアプリ属性を使用できる。この値は、アプリがメッセージングをリクエストするために使用する SDK API キーに基づきます。

|タグ | 説明 |
|------------------|---|
| `{{app.${api_id}}}` | メッセージを要求するアプリのAPIキー。例えば、このキーを Liquid の `abort_message()` と組み合わせて使用して、別の SDK API キーを使用する TV プラットフォームや開発ビルドなどの特定のアプリケーションに対して、アプリ内メッセージの送信を防止します。|
| `{{app.${name}}}` | メッセージを要求するアプリ名（Brazeダッシュボードで定義されている）。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

例えば、このリキッドコードは、リクエストアプリがリストにある2つのAPIキーのうちの1つでない場合、メッセージを中止する：

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## ターゲットデバイス情報

プッシュ通知およびアプリ内メッセージチャネルの場合、メッセージの送信先デバイスの以下の属性でテンプレートを作成できます。つまり、プッシュ通知またはアプリ内メッセージに、メッセージが表示されているデバイスのデバイス属性を含めることができます。これらの属性はコンテンツカードでは機能しないことに注意しよう。 

|タグ | 説明 |
|------------------|---|
| `{{targeted_device.${id}}}` | これはBrazeのデバイス識別子である。iOS の場合、これは Apple のベンダー用識別子 (IDFV) または UUID になります。Android などのプラットフォームでは、ランダムに生成されたUUID です。たとえば、ユーザに5 つのデバイスがある場合、5 つのデバイスすべてに対して送信試行が行われ、それぞれに対応するデバイス識別子が使用されます。ユーザーが最後に使用したデバイスにメッセージを送信するようするように設定されている場合、Braze で識別された最後に使用されたデバイスに対して送信操作が1 回だけ試行されます。 |
| `{{targeted_device.${carrier}}}` | 利用可能であれば、直近で使用したデバイスの電話サービスキャリア。例えば、「Verizon」や「Orange」などです。 |
| `{{targeted_device.${idfa}}}` | iOS デバイスの場合、アプリケーションが[ オプションのIDFA コレクション]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) で設定されている場合、この値はAdvertising (IDFA) の識別子になります。iOS以外のデバイスの場合、この値はNULLになる。 |
| `{{targeted_device.${google_ad_id}}}` | Android デバイスの場合、当社オプションの Google Play 広告 ID コレクションでお客様のアプリケーションが設定されていれば、この値は Google Play の広告識別子になります。Android以外のデバイスの場合、この値はNULLになる。 |
| `{{targeted_device.${roku_ad_id}}}` | Rokuデバイスの場合、この値は、アプリケーションがBrazeで設定される際に収集されるRoku Advertising Identifierとなる。Roku以外のデバイスの場合、この値はNULLになる。 |
| `{{targeted_device.${model}}}` | もしあれば、デバイスのモデル名。例えば、「iPhone 6S」や「Nexus 6P」、「Firefox」などだ。 |
| `{{targeted_device.${os}}}` | もしあれば、デバイスのオペレーティングシステム。例えば、「iOS 9.2.1」や「アンドロイド（ロリポップ）」、「ウィンドウズ」などだ。 |
| `{{targeted_device.${platform}}}` | もしあれば、デバイスのプラットフォーム。設定されている場合、値は `ios`、`android`、`kindle`、`android_china`、`web`、または `tvos` のいずれかになります。パーソナライゼーションタグ `most_recently_used_device` も使用できます。 |
| `{{targeted_device.${foreground_push_enabled}}}` | この値は、対象デバイスでフォアグラウンドのプッシュ通知を有効にしている場合に `true`、無効の場合に `false` になります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

デバイスキャリア、モデル名、およびオペレーティングシステムにはさまざまな種類があるため、これらの値のいずれかに条件付きで依存するロジックを徹底的にテストすることをお勧めします。特定のデバイスについてこれらの値が該当しない場合、値は `null` になります。 

さらに、プッシュ通知では、プッシュトークンが API を介してインポートされた場合など、特定の状況下で Braze がプッシュ通知に添付されたデバイスを判別できないことがあります。その結果、これらのメッセージの値は `null` になります。

![プッシュ・メッセージでファーストネーム変数を使うときにデフォルト値「there」を使う例。]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### デフォルト値の代わりに条件付きロジックを使う

状況によっては、デフォルト値を設定する代わりに[条件付きロジック]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/)を使用することもできます。条件付きロジックでは、カスタム属性の値によって異なるメッセージを送信することができる。さらに、条件付きロジックを使用して、NULL または空白の属性値を持つ顧客への[メッセージを中止]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)できます。 

#### ユースケース

たとえば、顧客に報酬残高通知を送信するとします。低い残高と NULL 残高を持つ顧客を考慮するために、デフォルト値を使用する適切な方法はありません。

この場合、デフォルト値を設定するよりも効果的なオプションが2つある：

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

2. このような顧客には、まったく別のメッセージを送ろう：

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

このユースケースでは、名が空白または NULL のユーザーは「Thanks for downloading」というメッセージを受け取ります。顧客の名には[デフォルト値]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/)を含めて、間違いがあった場合に Liquid が表示されないようにする必要があります。

{% endraw %}

## 可変タグ

メッセージ作成画面で、`assign` タグを使用して変数を作成できます。変数には一意の名前を使用することをお勧めします。サポートされているパーソナライゼーションタグ(`language` など) と同じ名前の変数を作成すると、メッセージングロジックに影響する可能性があります。

変数を作成したら、メッセージング・ロジックやメッセージの中でその変数を参照できる。このタグは、[Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}) ]機能から返されたコンテンツを再フォーマットしたいときに便利だ。詳しくは、Shopifyの[変数タグに関する](https://docs.shopify.com/themes/liquid/tags/variable-tags)ドキュメントを参照されたい。

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていることに気づいているか？`assign` タグを何度も書き出す代わりに、そのタグをコンテンツブロックとして保存し、メッセージの先頭に置くことができます。

1. [コンテンツブロックの作成]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)を行います。
2. コンテンツブロックに名前をつける（スペースや特殊文字は使わない）。
3. ページ下部の [**編集**] を選択します。
4. `assign` タグを入力する。

コンテンツ・ブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照することになる！
{% endalert %}

### ユースケース

例えば、顧客が 100 ポイントの報酬ポイントを獲得した後に、報酬ポイントを換金できるようにするとします。つまり、追加購入をした場合、ポイント残高が100以上になる顧客だけにメッセージを送りたいわけだ：

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
反復タグは、コードのブロックを繰り返し実行するために使うことができる。以下のユースケースでは、`for` タグを使用している。

### ユースケース

例えば、ナイキのスニーカーのセールを開催し、ナイキに興味を示した顧客にメッセージを送信するとします。各顧客のプロファイルには、さまざまな商品ブランドの配列が表示されます。この配列には、最大 25 の製品ブランドが含まれている可能性がありますが、最新の製品ビュー 5 つのうち、その 1 つとしてナイキ製品を表示した顧客にのみメッセージを送信します。

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

このユースケースでは、閲覧されたスニーカーブランドの配列の最初の5項目をチェックする。これらの項目のいずれかがコンバージョンであれば、`converse_viewer` 変数を作成し、それをtrueに設定する。

そして、`converse_viewer` が true のときにセールメッセージを送信します。それ以外の場合は、メッセージを中止します。

これは、Brazeメッセージコンポーザーでの反復タグの使い方の簡単な例である。詳細については、Shopify の[反復タグ](https://docs.shopify.com/themes/liquid/tags/iteration-tags)のドキュメントを参照してください。

## 構文タグ

構文タグを使用して、Liquid のレンダリング方法を制御できます。`echo` タグを使用して式を返すことができます。これは、中括弧を使って式をラップするのと同じだが、リキッドタグの中でこのタグを使うことができる。また、`liquid` タグを使用して、各タグに区切り文字を使用せずにLiquid のブロックを設定することもできます。`liquid` タグを使用する場合、各タグは個別の行に配置する必要があります。より詳細な情報と例については、Shopifyの[構文タグに関する](https://shopify.dev/api/liquid/tags#syntax-tags)ドキュメントをチェックしよう。

[ホワイトスペースコントロール](https://shopify.github.io/liquid/basics/whitespace/)を使用すると、タグの周りのホワイトスペースを削除できます。これにより、液体出力の外観をさらに制御することができます。

## HTTPステータスコード {#http-personalization}

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)の呼び出しから HTTP ステータスを使用するには、まず HTTP ステータスをローカル変数として保存してから、`__http_status_code__` キーを使用します。以下に例を示します。

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
このキーは、エンドポイントが JSON オブジェクト返す場合にのみ、コネクテッドコンテンツオブジェクトに自動的に追加されます。エンドポイントが配列や他の型を返す場合、そのキーはレスポンシブで自動的に設定することはできない。
{% endalert %}

## 言語、最新のロケール、タイムゾーンに基づいてメッセージを送信する

状況によっては、特定のロケールに固有のメッセージを送信したい場合があります。例えば、ブラジルのポルトガル語は一般的にヨーロッパのポルトガル語とは異なる。

### ユースケース:最新のロケールに基づいてローカライズする

ここでは、最新のロケールを使用して、国際化されたメッセージをさらにローカライズする方法について説明します。

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

このユースケースでは、直近のロケールが`pt_BR` の顧客にはブラジル系ポルトガル語のメッセージが、直近のロケールが`pt_PT` の顧客には欧州系ポルトガル語のメッセージが表示される。最初の 2 つの条件を満たさないが、言語をポルトガル語に設定している顧客は、お客様がデフォルトに設定したポルトガル語のタイプでメッセージを受け取ります。

### ユースケース:タイムゾーン別のターゲットユーザー

また、タイムゾーンでターゲットのユーザーを設定することもできます。例えば、EST のユーザーにはあるメッセージ、PST のユーザーには別のメッセージを送信します。そのためには、現在時刻をUTCで保存し、if/else文でユーザーの現在時刻と比較し、適切なタイムゾーンに適切なメッセージを送信する。ユーザーのローカルタイムゾーンでキャンペーンを送信するように設定し、適切な時間にキャンペーンを提供する必要がある。 

午後2時から3時の間に発信され、各タイムゾーンに固有のメッセージを書く方法については、以下のユースケースを参照のこと。

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

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
