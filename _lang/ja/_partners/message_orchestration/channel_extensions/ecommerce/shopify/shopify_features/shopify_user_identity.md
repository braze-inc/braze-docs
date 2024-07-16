---
nav_title: Shopify ユーザーID管理
article_title:"ShopifyユーザーID管理"
description:"この参考記事では、Shopify のユーザー ID 管理機能について概説する。"
page_type: partner
search_tag:Partner
alias: "/shopify_user_identity/"
page_order:3
---

# ShopifyユーザーID管理

> Brazeは、Shopify顧客からのシグナルを、顧客のサイト内での行動や、統合の一部として設定したShopifyのWebhookをリスニングすることで受信する。Shopifyの非ヘッドレスサイトでは、Brazeがチェックアウトページからユーザーの照合をサポートする。Shopifyのヘッドレスサイトの場合、[チェックアウトからユーザーを照合]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-checkout)する方法については、インテグレーションガイダンスを参照のこと。

## ユーザープロファイルの情報を取得する 

### Shopifyユーザー追跡

来店客がゲスト（つまり匿名）の場合、Brazeはその特定の顧客のセッションの`device_id` 。[Web SDKの実装]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)中にShopifyフォームのユーザー照合を設定すると、顧客がフォームに情報を入力するたびに、匿名のユーザープロファイルに顧客メールが追加される。 

店舗訪問者がShopifyのニュースレターやメールキャプチャフォームにメールを入力すると、BrazeはShopifyのWebhookイベントを受信し、ユーザープロファイルを作成する。Brazeは次に、このユーザープロファイルをWeb SDKによって追跡された匿名ユーザープロファイルと統合し、ユーザープロファイル上のユーザーエイリアスとしてShopify顧客IDを割り当てる。 

顧客がチェックアウトに進み、電話番号などの識別可能な他の情報を提供すると、BrazeはShopifyのWebhookから関連するユーザーデータを取得し、匿名ユーザーとマージする必要がある`device_id` 。
- Shopify ScriptTag、非ヘッドレスShopifyサイト、またはGoogle Tag Manager経由でWeb SDKを実装した場合、Brazeは自動的に、チェックアウトページのユーザーデータと匿名ユーザープロファイルのセッションデータが、割り当てられたShopifyユーザーIDを持つユーザーエイリアスプロファイルにマージされるようにします。
- WebSDKをShopifyヘッドレスサイトに実装している場合、チェックアウトページ内で送信されたユーザーデータが、Web SDKまたはAPIを通じて正しいユーザープロファイルに適切に割り当てられていることを確認する必要がある。詳しくは、[Web SDKをヘッドレスShopifyサイトに直接実装する]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-site)をご覧いただきたい。

顧客がチェックアウトのプロセスを進めると、Brazeは入力されたメールアドレス、電話番号、またはShopifyのユーザーIDが既存のユーザープロファイルと一致するかどうかをチェックする。一致した場合、BrazeはShopifyユーザーデータをそのプロファイルに同期する。

メールアドレスまたは電話番号が複数のユーザープロファイルに関連付けられている場合、Brazeは最新のアクティビティを持つプロファイルにShopifyデータを同期する。

Brazeは、メールアドレスまたは電話番号に一致するものが見つからない場合、サポートされているShopifyデータで新しいユーザープロファイルを作成する。

### Shopifyの顧客がBrazeと同期する場合

Brazeは、Shopifyストアで獲得したリード、サインアップ、アカウント登録に対して、既存のユーザープロファイルを更新したり、新しいユーザープロファイルを作成したりする。Shopifyでは、以下の方法などからユーザープロファイルのデータを収集することができる：
- 顧客がアカウントを作成する
- 顧客のメール アドレスまたは電話番号が Shopify のキャプチャ フォームで収集される
- 顧客のEメールアドレスがニュースレターフォームから収集される
- 顧客のメール アドレスまたは電話番号は、EcomSend のような Shopify に接続されたサードパーティのツールを通じて収集される。

Brazeはまず、顧客のメールアドレスまたは電話番号を使用して、サポートされているShopifyデータと既存のユーザープロファイルのマッピングを試みる。 

ユーザープロファイルの重複を防ぐため、[Shopify Web サイトに Web SDK を実装]()する際に使用した方法の、Shopify Forms 用のユーザー照合手順を確認することが重要である。

## ユーザープロファイルの統合 

{% alert note %}
デフォルトのShopifyインテグレーションは、匿名ユーザープロファイルとShopifyエイリアスプロファイルの統合を支援するツールを提供する。ヘッドレスShopifyサイトへの統合を実装する場合は、[Web SDKをヘッドレスShopifyサイトに直接実装]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)するを確認し、ユーザーを適切に照合していることを確認する。
{% endalert %}

Brazeは、匿名ユーザープロファイルから識別子ユーザープロファイルにフィールドをマージする：
- Shopify顧客ID
- メール
- 電話番号

Brazeは、以下のフィールドを匿名ユーザープロファイルから識別子ユーザープロファイルにマージする：
- 名
- 姓
- メール
- 性別
- 生年月日
- 電話番号
- タイムゾーン
- 市区町村
- 国
- 言語
- カスタム属性
    - カスタムイベントおよび購入イベントデータ（イベントプロパティ、カウント、最初の日付と最後の日付のタイムスタンプを除く。）
    - Y日間でX回」のセグメンテーション（X<=50、Y<=30）のためのカスタムイベントと購入イベントのプロパティ。
- プッシュトークン
- メッセージ履歴
- カスタムイベント、購入イベントカウント、最初の日付と最後の日付のタイムスタンプなど、匿名ユーザープロファイルまたは識別子ユーザープロファイルで見つかった以下のフィールドのいずれか。
    - これらの統合されたフィールドは、「Y日以内にXイベント」フィルターを更新する。購入イベントの場合、これらのフィルターには「Y日間の購入回数」と「過去Y日間の使用金額」が含まれる。

{% alert important %}
セッションデータは、統合プロセスの一部としてまだサポートされていない。
{% endalert %}

## Shopifyのサブスクライバーを同期する

Shopifyのセットアッププロセスにおいて、Brazeは柔軟なコントロールを提供し、顧客のEメールアドレスとSMSオプトインステートをBrazeユーザープロファイルのサブスクリプショングループとサブスクリプションステートに同期させることができる。 

### メールやSMSのサブスクライバーを集める

ShopifyストアをBrazeにセットアップする際に、ShopifyからEメールとSMSサブスクライバーをBrazeに同期するオプションがある。 

#### サブスクライバーを集める

サブスクライバー収集をイネーブルメントにするには、Shopifyのセットアップの中で機能をオンにする。Shopifyメール購読者など、少なくとも1つの[サブスクリプショングループを]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups)割り当てることを推奨する。Brazeは、指定したサブスクリプショングループにメール購読者を追加し、メッセージ送信時にオーディエンスターゲティングに含まれるようにする。 

![\]({% image_buster /assets/img/Shopify/collect_email.png %})

イネーブルメントを有効にすると、Shopifyメール購読者への更新とメール購読状態の更新がリアルタイムで同期される。オーバーライドオプションをイネーブルメントしない場合、Shopifyの顧客は、Shopifyストアに関連付けられたサブスクリプショングループから購読または配信停止される。

オーバーライドオプションをイネーブルメントにすると、Brazeはユーザープロファイルのグローバルサブスクリプションの状態を更新する。つまり、顧客がShopifyで配信停止とマークされている場合、Brazeはユーザープロファイル上でグローバルサブスクリプションの状態を配信停止とマークし、利用可能なすべてのメールサブスクリプショングループから顧客を配信停止にする。その結果、グローバルにメール配信停止されたユーザーにはメッセージが送られなくなる。

#### SMSサブスクライバーを集める

ShopifyからSMSサブスクライバーを集めるには、[SMSセットアップの]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup)一部として[SMSサブスクリプショングループを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/)作成する必要がある。 

ShopifyのSMSサブスクライバーを集める準備ができたら、ShopifyのセットアップページでSMSサブスクライバー集めをイネーブルメントにする。SMSメッセージを適切にターゲットして送信できるように、少なくとも1つのSMSサブスクリプショングループを選択する必要がある。 

![\]({% image_buster /assets/img/Shopify/collect_sms.png %})

イネーブルメントを有効にすると、Brazeは、Shopify SMSサブスクライバーとそのSMSサブスクリプション状態の更新をリアルタイムで同期する。オーバーライドオプションをイネーブルメントしない場合、Shopifyの顧客は、Shopifyストアに関連付けられたサブスクリプショングループから購読または配信停止される。

SMSのサブスクライバーは、オーバーライド・オプションを使用する際、それらを考慮する必要はない（'t have global subscription states, so you don'）。ユーザーは、SMSサブスクリプショングループにのみ配信停止またはサブスクライブすることができる。

#### レガシーカスタム属性

従来のShopify顧客は、`shopify_accepts_marketing` と`shopify_sms_consent` カスタム属性を介してメールとSMSサブスクライバーを収集する古い方法を持っているかもしれない。イーブルネーションを有効にして上記の設定を保存すると、Brazeはユーザープロファイルのカスタム属性を削除し、それらの値をそれぞれのメールサブスクリプショングループとSMSサブスクリプショングループに同期させる。

これらのレガシーカスタム属性を使用している既存のキャンペーンまたはキャンバスがある場合、これらの属性を削除し、キャンペーンまたはキャンバスが適切なサブスクリプションステート、グループ、またはその両方を使用していることを確認する。
