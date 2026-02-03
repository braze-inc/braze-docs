---
nav_title: Zeotap Symphony
description: "このリファレンス記事では、Braze と Zeotap のパートナーシップについて説明します。Zeotap は、アイデンティティ解決、インサイト、データ強化を提供する次世代顧客データプラットフォームです。"
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zeotap Symphony

Braze と Zeotap Symphony の統合により、リアルタイムのオーケストレーションを作成し、電子メールやプッシュ通知キャンペーンを実行することができます。

- ユーザーが Braze からパーソナライズされたメールを送信できるかどうかに基づいて、Zeotap から姓と名を送信します。
- Zeotapを通じてカスタムイベントまたは購入イベントをリアルタイムで送信し、ユーザーはそれに基づいてBraze内でキャンペーントリガーを作成し、顧客をターゲットにすることができる。

{% alert note %}
メールマーケティングキャンペーンを作成するには、生のメールを Zeotap Catalogue の `Email Raw` にマッピングして、これらのメールを登録します。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| クライアント名 | これは、Braze アカウントのクライアント名です。これを確認するには、Braze コンソールに移動します。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| インスタンス | Braze インスタンスは Braze オンボーディングマネージャーから入手できます。また、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)でも確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 統合

このセクションでは、Brazeと統合できる2つの方法について説明する：

### 方法1
この方法では、次の作業を行う必要があります。
1. ウェブサイトやアプリにBraze SDKを統合する。
2. Symphony を介して Braze を Zeotap と統合します。

- `User traits` は、[**Data To Send**] タブの各 Braze フィールドにマッピングされている必要があります。`Event` と`Purchase` のアトリビュートを対応させると、Braze内でイベントが重複することになる。
- Braze SDK の設定時に設定した`User ID` に `External ID` をマッピングします。

統合が正常に設定されると、Symphonyを通じてBrazeに送信されるカスタム属性に基づいて、Eメールやプッシュ通知キャンペーンを作成できる。

### 方法2
この方法では、Symphony を介して Braze とZeotap を統合できます。

- この方法では、アプリ内メッセージ、コンテンツカード、プッシュ通知などのBraze UI 機能はサポートされません。
- Zeotap では、Zeotap Catalogue で利用可能な `hashed email` を `External ID` にマッピングすることを推奨しています。

統合が正常に設定されると、Symphonyを通じてBrazeに送信されたカスタム属性に基づいてのみ、メールキャンペーンを作成できるようになる。

## Brazeへのデータフローとサポートされる識別子

データは、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して Zeotap から Braze に流れます。データの流れをまとめると以下のようになります。

1. Zeotapはユーザープロファイル属性、カスタム属性、カスタムイベント、購入フィールドを送信する。
2. 関連するすべての Zeotap Catalogue フィールドを、[**Data To Send**] タブの Braze フィールドにマッピングします。
3. そのデータはBrazeにアップロードされる。

各属性の詳細は、「[送信するデータ](#data-to-send-tab)」セクションで確認できる。

## 目的地の設定

Symphony でユーザーにフィルターを適用した後、またはユーザーの条件を追加した後は、[**Send to Destinations**] で、Braze のユーザーをアクティブ化できます。新しいウィンドウが開き、宛先を設定できます。[**Available Destination**] リストにある既存の宛先を使用するか、新規の宛先を作成できます。

#### 新しい宛先を追加する
新しい宛先を追加するには、次の手順を実行します。
1. [**新しい宛先を追加する**] をクリックします。
2. **Braze** を検索します。
3. [**Client Name**]、[**API Key**]、および [**Instance**] を追加し、宛先を保存します。

デスティネーションが作成され、「**Available Destinations（利用可能なデスティネーション）**」で利用できるようになる。

#### ワークフローレベルの入力を追加する
宛先を作成したら、次に以下に示すようにワークフローレベルの入力を追加する必要があります。
1. 検索機能を使って、利用可能な目的地のリストから目的地を選ぶ。
2. **Client Name（クライアント名）**、**API Key（APIキー）**、**Instance（インスタンス**）フィールドは、宛先作成時に入力した値に基づいて自動的に入力される。
3. このワークフローノードに対して作成する**オーディエンス名**を入力します。これは**カスタム属性**として Braze に送信されます。
4. [**Data To Send**] タグでカタログから宛先へのマッピングを完了します。マッピングの詳細については、下記を参照されたい。

#### [Data to send] タブ
[**Data To Send**] タブでは、Zeotap Catalogue のフィールドを、Braze に送信できる Braze のフィールドにマッピングできます。マッピングは以下のいずれかの方法で行うことができる：
- **静的マッピング** \- Zeotap により関連する Braze フィールドに自動的にマッピングされるフィールドがあります (メール、電話番号、名前、性など)。<br>
- **ドロップダウン選択** \- Zeotap に取り込まれた関連フィールドを、ドロップダウンメニューに示されている Braze フィールドにマッピングします。<br>![言語、都市、誕生日など、Zeotapに設定されたさまざまなユーザー特性。]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **カスタムデータ入力**-関連するZeotapフィールドにマッピングされたカスタムデータを追加し、Brazeに送信する。<br>![Zeotap のユーザー特性として"loyalty_points" を選択します。]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## サポートされている属性
このセクションでは、すべての Braze フィールドの詳細を確認できます。

| Braze フィールド | マッピングタイプ | 説明 |
| --- | --- | --- |
| external ID | ドロップダウン選択 | これは、デバイスやプラットフォームを超えてユーザーを追跡するためにBrazeが定義した永続的な`User ID` 。`User ID` を`External ID` にマップすることを推奨する。そうしないと、Zeotapはユーザーエイリアスとして電子メールを送信する可能性がある。<br><br>Zeotap では、Zeotap Catalogue で利用可能な `hashed email` を `External ID` にマッピングすることを推奨しています。|
| メール | 静的マッピング | これは、Zeotap Catalogueの`Email Raw` にマッピングされます。 |
| 電話 | 静的マッピング | これは、Zeotap Catalogueの`Mobile Raw` にマッピングされます。<br><br>\- Brazeは`E.164` フォーマットの電話番号を受け付ける。Zeotap は変換を実行しません。このため、電話番号を所定の形式で取り込む必要があります。詳細については、「[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)」を参照してください。 |
| 名 | 静的マッピング | これは、Zeotap Catalogueの`First Name` にマッピングされます。 |
| 姓 | 静的マッピング | これは、Zeotap Catalogueの`Last Name` にマッピングされます。 |
| 性別 | 静的マッピング | これは、Zeotap Catalogueの`Gender` にマッピングされます。 |
| カスタムイベント名 | 静的マッピング | これは、Zeotap Catalogueの`Event Name` にマッピングされます。<br><br>Braze でカスタムイベントをキャプチャするため、カスタムイベント名とカスタムイベントタイムスタンプをマッピングする必要があります。どちらかがマッピングされていないと、カスタムイベントは処理できない。詳細については、「[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object)」を参照してください。 |
| カスタムイベントタイムスタンプ | 静的マッピング | これは、Zeotap Catalogueの`Event Timestamp` にマッピングされます。<br><br>Braze でカスタムイベントをキャプチャするため、カスタムイベント名とカスタムイベントタイムスタンプをマッピングする必要があります。どちらかがマッピングされていないと、カスタムイベントは処理できない。詳細については、「[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object)」を参照してください。 |
| メール購読 | ドロップダウン選択 | `Email Marketing Preference` フィールドを登録してそれにマッピングします。<br><br>Zeotap は次の3つの値を送信します。<br>• `opted_in` - ユーザーがメールマーケティング設定を明示的に登録していることを示します。<br>• `unsubscribed` - ユーザーがメールメッセージを明示的にオプトアウトしたことを示します。<br>• `subscribed` - ユーザーがオプトインもオプトアウトもしていないことを示します。 |
| プッシュサブスクライブ | ドロップダウン選択 | `Push Marketing Preference` フィールドを登録してそれにマッピングします。<br><br>Zeotap は次の3つの値を送信します。<br>• `opted_in` - ユーザーがプッシュマーケティング設定を明示的に登録していることを示します。<br>• `unsubscribed` - ユーザーがプッシュメッセージを明示的にオプトアウトしたことを示します。<br>• `subscribed` - ユーザーがオプトインもオプトアウトもしていないことを示します。 |
| メール開封追跡が有効 | ドロップダウン選択 | 該当する`Marketing Preference` フィールドをマッピングする。<br><br>trueに設定すると、今後このユーザーに送信されるすべてのEメールに開封トラッキングピクセルを追加できるようになる。 |
| 電子メールのクリック追跡を有効にする | ドロップダウン選択 | 該当する`Marketing Preference` フィールドをマッピングする。<br><br>trueに設定すると、このユーザーに今後送信されるすべてのメール内のすべてのリンクのクリックトラッキングを有効にする。 |
| プロダクトID | ドロップダウン選択 | • 購入アクションの ID `(Product Name/Product Category)`。詳細については、「[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)」を参照してください。<br>• 関連する属性を Zeotap Catalogue に登録してそれにマッピングします。<br><br>Braze で購入イベントをキャプチャするには、`Product ID`、`Currency`、および`Price` を必ずマッピングする必要があります。この3つのいずれかが欠落している場合、購入イベントは成立しません。詳細については、「[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-object)」を参照してください。 |
| 通貨 | ドロップダウン選択 | \- 購入アクションの通貨属性。<br>\- サポートされているフォーマットは`ISO 4217 Alphabetic Currency Code` です。<br>\- 正しい形式の通貨データを Zeotap Catalogue に登録してそれにマッピングします。<br><br>Braze で購入イベントをキャプチャするには、`Product ID`、`Currency`、および`Price` を必ずマッピングする必要があります。この3つのいずれかが欠落している場合、購入イベントは成立しません。 |
| 価格 | ドロップダウン選択 | \- 購入アクションの価格属性。<br>• 関連する属性を Zeotap Catalogue に登録してそれにマッピングします。<br><br>Braze で購入イベントをキャプチャするには、`Product ID`、`Currency`、および`Price` を必ずマッピングする必要があります。この3つのいずれかが欠落している場合、購入イベントは成立しません。 |
| 数量 | ドロップダウン選択 | \- 購入アクションの数量属性。<br>• 関連する属性を Zeotap Catalogue に登録してそれにマッピングします。 |
| 国 | ドロップダウン選択 | 登録する`Country` Catalogue フィールドにマッピングします。 |
| 市区町村 | ドロップダウン選択 | 登録する`City` Catalogue フィールドにマッピングします。 |
| 言語 | ドロップダウン選択 | \- 使用可能なフォーマットは、`ISO-639-1` 標準（例：en）である。<br>• 正しい形式の言語を登録してそれにマッピングします。 |
| 生年月日 | ドロップダウン選択 | 登録する`Date of Birth` フィールドにマッピングします。 |
| カスタム属性 | カスタムデータ入力 | 任意のユーザー属性をカスタムデータ入力にマップし、それをBrazeに送信する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Brazeコンソールでデータを見る

送信する関連属性をマッピングし、ワークフローでパブリッシュすると、定義された基準に基づいてBrazeにイベントが流れ始める。Brazeコンソール上で、EメールIDまたは外部IDで検索できる。

![]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

各種属性は、Braze 内のユーザーダッシュボードのさまざまなセクションに表示されます。
- **Profile**タブにはユーザー属性が含まれる。
- **カスタム属性**タブには、ユーザーが定義したカスタム属性が含まれる。
- [**カスタムイベント**] タブには、ユーザーが定義したカスタムイベントが表示されます。
- [**購入**] タブには、ユーザーが一定期間内に購入したものが表示されます。

## キャンペーン作成

ユーザーはBraze内でキャンペーンを作成し、リアルタイムまたはスケジュールされた時間に基づいてユーザーをアクティブにすることができる。キャンペーンは、ユーザーによって実行されたアクション（カスタムイベント、購入）またはユーザー属性に基づいてトリガーすることができる。

