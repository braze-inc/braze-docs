---
nav_title: Shopify ユーザアイデンティティマネジメント
article_title: "Shopify ユーザアイデンティティマネジメント"
description: "このリファレンス記事では、Shopify ユーザー アイデンティティマネジメント機能の概要について説明します。"
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Shopify ユーザー識別マネジメント

> Braze は、オンサイトの動作やインテグレーションの一部として設定したShopify webhookを聴くことで、Shopify 顧客 s からシグナルを受信します。ヘッドレスでないShopifyサイトの場合、Brazeはチェックアウトページからユーザーを調整するのを支援します。ヘッドレスShopify拠点については、[チェックアウト]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-checkout)からユーザーを調整する方法に関する当社の統合ガイダンスを参照してください。

## ユーザープロファイルのキャプチャ 

### Shopify ユーザー "トラッキング

ストア訪問者がゲスト(つまり匿名) の場合、Braze はこれらの特定の顧客のセッションs の`device_id` をキャプチャします。[Web SDKの実装中にShopifyフォームのユーザー調整を設定すると、顧客がフォームに入力するたびに、顧客 メールsが匿名ユーザープロファイルに追加されます。 

店舗訪問者がメールをShopifyニュースレターやメールキャプチャーフォームに入力すると、BrazeはShopify Webhookを受け取り、ユーザープロファイルを作成します。Braze は、このユーザープロファイルをWeb SDKによって追跡される匿名ユーザープロファイルとマージし、ユーザープロファイルのユーザー別名としてShopify 顧客 ID を割り当てます。 

顧客がチェックアウトに進み、電話番号などの他の識別可能な情報を提供するにつれて、BrazeはShopify webhookから関連するユーザーデータを取得し、`device_id`で匿名ユーザーとマージする必要があります。
- Shopify ScriptTag、ヘッドレスでないShopify サイト、またはGoogle Tag Manager を使用してWeb SDKを実装した場合、Braze はチェックアウトページからのユーザーデータと匿名ユーザープロファイルからのセッションデータが、割り当てられたShopify 顧客 ID でユーザー別名プロファイルにマージされることを自動的に確認します。
- Web SDKをShopifyヘッドレスサイトに実装した場合は、チェックアウトページ内で送信されたユーザーデータがアプリ適切に、Web SDKまたはAPIのいずれかを介して正しいユーザープロファイルに割り当てられていることを確認する必要があります。詳細については、[Web SDKをヘッドレスShopifyサイト]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-site)に直接実装してください。

顧客がチェックアウト処理を続行すると、Brazeは、入力されたメール住所、電話番号、またはShopify 顧客 IDが存在するユーザープロファイルと一致するかどうかを確認します。一致がある場合、Braze はShopify ユーザーデータをそのプロファイルに同期します。

メールの住所または電話番号が複数の識別されたユーザープロファイルs に関連付けられている場合、Braze はShopifyデータを最新のアクティビティを持つプロファイルに同期します。

Brazeがメールの住所または電話番号と一致するものを見つけられない場合、サポートされているShopify情報を使用して新しいユーザープロファイルが作成されます。

### Shopify 顧客 s がBraze と同期する場合

Shopifyストアでキャプチャされたリード、サインアップ、およびアカウント登録の既存のユーザープロファイルをBraze 更新するか、新しいものを作成します。Shopifyなどで、以下のメソッドからユーザープロファイルを収集できます。
- 顧客がアカウントを作成する
- お客様のメール住所または電話番号がShopifyキャプチャフォームで収集される
- お客様メールの住所は、ニュースレターフォームから収集されます
- お客様のメール先や電話番号は、EcomSendなどのShopifyに接続されたサードパーティ製の機器で収集されます

Brazeは、まず、顧客のメール住所または電話番号を使用して、サポートされているShopifyデータを既存のユーザープロファイルにマッピングしようとします。 

重複するユーザープロファイルs を防ぐために、[ Web SDKをShopify Web サイト]() に実装するために使用したメソッドのShopify Forms 命令のユーザー調整を確認することが重要です。

## ユーザプロファイルのマージ 

{% alert note %}
デフォルト Shopifyインテグレーションは、匿名ユーザープロファイルとShopify別名プロファイルのマージを支援するツールを提供します。ヘッドレスShopifyサイトへの統合を実装する場合は、[ヘッドレスShopifyサイトにWeb SDKを直接的に実装して]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)を確認し、ユーザーが適切に調整されていることを確認します。<br><br> 重複するユーザープロファイルs が発生した場合は、[バルクマージツール]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) を使用して、データの効率化を支援できます。
{% endalert %}

Brazeは、次のいずれかと一致するものが見つかった場合に、匿名ユーザープロファイルのフィールドを識別されたユーザープロファイルにマージします。
- Shopify 顧客番号
- メール
- 電話番号

Braze は、匿名ユーザープロファイルの以下のフィールドを、識別されたユーザープロファイルにマージします。
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
    - カスタムイベントおよび購入イベントデータ(イベントプロパティ、カウント、および最初の日付と最後の日付のタイムスタンプを除く)
    - 「X 回/Y 日」セグメンテーションのカスタムイベントおよび購入イベントプロパティ(X<=50 およびY<=30)
- プッシュトークン
- メッセージ履歴
- 匿名ユーザープロファイルまたは識別されたユーザープロファイルで検出された以下のフィールド(カスタムイベント、購入イベントカウント、最初の日付と最後の日付のタイムスタンプなど)
    - これらのマージされたフィールドs は、「Y 日間のX イベント」フィルターs を更新します。購入イベントの場合、これらのフィルターには、「Y 日の購入数」と「Y 日の最後に消費した金額」が含まれます。

{% alert important %}
セッションデータは、マージプロセスの一部としてまだサポートされていません。
{% endalert %}

## Shopify サブスクライバーの同期

Shopify設定処理中、Braze は柔軟なコントロールを提供して、顧客 メールアドレスとSMS オプトイン状態をBraze ユーザープロファイルs のサブスクリプショングループs およびサブスクリプション 状態に同期します。 

### メールやショートサブスクライバーを収集する

Shopify ストアをBraze に設定する際に、Shopify からBraze にメールとSMS サブスクライバーを同期することができます。 

#### メール サブスクライバーの収集

メール サブスクライバー収集を有効にするには、Shopify設定で機能を有効にします。Shopify メール サブスクライバーs など、少なくとも1 つのBraze[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) を割り当てることをお勧めします。Braze は、指定されたサブスクリプショングループs にメール サブスクライバーs を追加し、メッセージを送信するときにオーディエンスターゲットに含まれるようにします。 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

有効にすると、Braze は更新 s をShopify メール サブスクライバー s と更新 s をリアルタイムでメール サブスクリプションステートに同期します。上書きオプションを有効にしない場合、Shopify 顧客s はShopifyストアに関連付けられたサブスクリプショングループからサブスクライブまたは配信停止d のいずれかになります。

上書きオプションを有効にすると、Braze はユーザープロファイルの大域サブスクリプションステートを更新します。つまり、顧客s が配信停止 d としてShopifyでマークされている場合、Braze は配信停止 d としてサブスクリプション ステートをユーザープロファイル上でマークし、使用可能なすべてのメール サブスクリプショングループs からユーザープロファイルします。そのため、メールからグローバル配信停止dのユーザーにはメッセージは送信されません。

#### SMSサブスクライバーを収集する

Shopify から SMS サブスクライバー s を収集するには、[SMS サブスクリプショングループ s]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) を [SMS セットアップ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup) の一部として作成する必要があります。 

ShopifyのSMS サブスクライバーを収集する準備ができたら、Shopify設定画面でSMS サブスクライバー収集を有効にします。適切にSMSをアプリして送信できるように、少なくとも1つのSMS サブスクリプショングループを選択する必要があります。 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

有効にすると、Braze は更新をShopify SMS サブスクライバーとそのSMS サブスクリプションステートにリアルタイムで同期します。上書きオプションを有効にしない場合、Shopify 顧客s はShopifyストアに関連付けられたサブスクリプショングループからサブスクライブまたは配信停止d のいずれかになります。

SMS サブスクライバーにはグローバルサブスクリプションステートがないため、オーバーライドオプションを使用するときに考慮する必要はありません。ユーザーは、配信停止dまたはSMS サブスクリプショングループへのサブスクライブのみが可能です。

#### レガシーカスタム属性

レガシーShopify 顧客s には、`shopify_accepts_marketing` および`shopify_sms_consent` カスタム属性s を介してメール およびSMS サブスクライバーs を収集する従来のメソッドがある場合があります。上の設定s を上書きを有効にして保存すると、Braze はユーザープロファイルs のカスタム属性s を削除し、それぞれのメール サブスクリプショングループとSMS サブスクリプショングループにこれらの値を同期します。

既存のキャンペーン s またはキャンバスがこれらのレガシーカスタム属性s を使用している場合は、それらの属性s を削除し、キャンペーンs またはキャンバスがアプリの適切なサブスクリプションステート、グループ、またはその両方を使用していることを確認します。
