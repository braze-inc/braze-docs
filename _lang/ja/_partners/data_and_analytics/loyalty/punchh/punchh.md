---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "このリファレンス記事では、Braze と Punchh のパートナーシップについて説明します。Punchh はロイヤルティとエンゲージメントのプラットフォームであり、2つのプラットフォーム間でデータを同期できるようになります。Braze で公開されたデータはセグメンテーションに使用でき、Braze で設定された Webhook テンプレートを使用してユーザーデータを Punchh に同期できます。"
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/)は、ブランドが店内でもデジタルでもオムニチャネル 顧客 ロイヤルティプログラムを配信できる、業界をリードするロイヤルティとエンゲージメント プラットフォームです。 

_この統合は Punchh によって管理されます。_

## 統合について

Braze と Punchh の統合により、2つのプラットフォーム間でギフティングやロイヤルティの目的でデータを同期できます。Braze で公開されたデータはセグメンテーションに使用でき、Braze Webhook を介してユーザーデータを再び Punchh に同期できます。

## メリットは何でしょうか。

- Punchh から Braze にロイヤルティデータをリアルタイムで取り込む。 
- Braze の強力なオーディエンス情報を利用してレイヤー化し、有意義でダイナミックなクロスチャネルエクスペリエンス (アプリ、モバイル、Web、メール、SMS) を提供する。
  - 顧客がメールを開封しましたか?顧客が店舗の周辺でアプリを開きましたか?
- Braze で送信されるトランザクションメールのルックアンドフィールを標準化する。
- その過程で AB テストと最適化を可能にするジャーニーを作成する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Punchh アカウント | このパートナーシップを活用するには、アクティブなPunchh アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## その他の留意点

#### 統合前

- Braze 統合を使用する場合、Punchh と Braze それぞれに1つずつ、2つのキャンペーンが必要です。たとえば、オファーが添付されているキャンペーンを送信する場合、ギフティングキャンペーンは Punchh 内で設定され、通知は Braze から送信できます。
- ゲストは Punchh と Braze にすでに存在している必要があります。Punchh では、まだロイヤルティゲストではない顧客はすべて除外されます。

#### 注意すべき重要事項

- Punchh では、Braze にデフォルトのユーザー属性を送信する動作を無効にできる機能が追加されています。これにより、顧客に対してデータポイントの超過料金が発生することがありません。これは、アダプターのセットアップ中に構成されます。
- キャンペーンが実行されるたびにID が変更されるため、定期的なキャンペーンでカスタムSegments を使用する場合は、キャンペーン ID の代わりにキャンペーンの名前を使用する必要があります。
- 各 Punchh ギフティングキャンペーンで使用できるコミュニケーションチャネルには、リッチメッセージ、プッシュ通信、SMS、メールがあります。
- Braze から Punchh カスタムセグメントに送信されたユーザーは、削除できません。既存のカスタムセグメントには新規ゲストのみを追加できます。既存のPunchhカスタムSegmentからゲストを削除する必要がある場合は、新しいPunchhカスタムSegmentにユーザーを送信するために、新しいWebhook キャンペーンをBrazeで作成する必要があります。

## 統合

Punchh は、Braze の顧客が利用できる複数のエンドポイントを提供します。これは、次の Punchh API エンドポイントを使用して Punchh プラットフォームに external ID を追加するのに役立ちます。外部ID を追加したら、Punchh でアダプターを作成し、Braze 認証情報を入力して、同期したい行動を選択します。次に、Punchh セグメントID を使用して、キャンバスジャーニーで顧客同期をトリガーする Punchh Webhook を作成できます。

統合で同期が正しく行われるようにするには、Punchh`user_id` と Braze `external_id` がどちらのプラットフォームでも利用可能でなければなりません。 
- Punchh からBraze に送信されるイベントには、識別子としてBraze `external_id` が含まれます。Punchh が`external_source_id` を使用するように設定されている場合、その値が Braze `external_id` として設定されます。そうでない場合、統合はデフォルトで Punchh`user_id` を Braze`external_id` として設定します。
- Braze から Punchh へ Webhook を送信するには、Braze ユーザープロファイルで Punchh `user_id` が利用できなければなりません。Punchh `user_id` を Braze `external_id` として使用しない場合は、カスタム属性「punchh_user_id」として設定する必要があります。 

### ステップ 1: 外部ID 取り込みエンドポイントのセットアップ(オプション)

Braze の external ID は、新規および既存の Punchh ユーザーの次のエンドポイントを使用して追加できます。

{% alert important %}
`external_source` および`external_source_id` フィールドの値は、Punchh に対して一意であり、また既存のプロファイルに関連付けられていてはなりません。
{% endalert %}

1. 新規 Punchh ユーザー<br>
`external_source` および`external_source_id` フィールドs を使用して、Punchh サインアップエンドポイントでPunchh に新しいユーザーs を作成します。Punchh では、外部識別子をユーザープロファイルとともに次のいずれかの登録エンドポイントを介して送信できます。
- [Mobile Signup API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO Signup API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 既存の Punchh ユーザー <br>
既存の Punchh ユーザーの`external_source_id` を更新します。Punchh では、ユーザーAPI 更新エンドポイントを介して外部識別子をプロファイルに追加できます。 
- [Mobile User Update](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO User Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard User Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs ローカル %}
{% tab ユーザー登録 API の例 %}
この例では、登録時にユーザープロファイルを使用して外部識別子を送信できます。このために、`external_source` を「customer_id」として、`external_source_id` を文字列データ型の「111111111111111111」として送信します。

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab ユーザー更新 API の例 %}
この例では、ユーザープロファイルを使用して外部識別子を更新できます。このために、`external_source` を「customer_id」として、`external_source_id` を文字列データ型の「111111111111111111」として送信します。

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**プラットフォーム設定:**Punchh で外部識別子を有効にするには、Punchh ダッシュボードから [**Cockpit**] > [**Dashboard**] > [**External User Identifier**] に移動します。
{% endalert %}

### ステップ2:Punchh で Braze アダプターを設定する

#### 同期できるイベント {#available-events-to-sync}

1. **Guest:**登録、ゲストプロファイルの更新、非アクティブ化、または削除時にトリガーされます。
2. **Loyalty Check-in:**ロイヤルティトランザクションまたはレシートのバーコードスキャンによる獲得に対してトリガーされます。
3. **Gift Check-in:**キャンペーンで与えられたポイントに対してトリガーされます。
4. **Redemption:**パンチクーポンを除く報酬償還の場合にトリガーされます。これは、発行と償還を含むクーポンイベントとして別々に送信されるためです
5. **Rewards:**キャンペーン、アクティビティ、ポイントからリワードへの変換、または管理ギフティングで与えられたリワードからトリガーされます。
6. **Transaction Notifications:**Punchh システム内でのユーザーのトランザクションアクティビティに対してトリガーされます (ポイントの有効期限など)。
7. **マーケティング通知:**関連付けられているユーザーセグメントの Punchh での各種キャンペーン設定に基づいてトリガーされます。

{% alert note %}
これらの利用可能なイベントのサンプルペイロードの内容については、Punchh のドキュメントを参照してください。
{% endalert %}

Punchh 実装マネージャーと協力して、このアダプターを設定します。

Braze と Punchh の統合を設定するには、次の手順を実行します。

1. パンチダッシュボードで、**コックピット**> **ダッシュボード**> **主な機能**> **Webフック管理を有効**にし、**Webフック管理を有効**にします。<br><br>
2. 次に、[**Settings**] > [**Webhooks Manager**] > [**Configurations**] > [**Show Adapters Tab**] に移動してアダプターを有効にし、[**Show Adapters Tab**] をオンに切り替えます。<br><br>
3. **Webフックマネージャ**の**設定**タブに移動し、**アダプタ**タブを選択し、**アダプタの作成**をクリックします。<br><br>![]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. アダプターの名前、説明、および管理メールを入力します。アダプターとして **Braze** を選択し、Braze REST API エンドポイントとBraze API キーを入力します。<br><br>
5. 次に、有効にするイベントを選択します。これらのイベントのリストは「[同期できるイベント ](#available-events-to-sync)」にあります。<br><br>![]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. **Submit**を押してWebhookを有効にします。

## Braze で Punchh Webhook を作成する

Braze は、Punchh カスタムセグメントを使用してWebhook 経由でユーザーを Punchh セグメントに追加できます。

1. Punchh でカスタムセグメントを作成し、以下に示す Punchh セグメントダッシュボード URL に含まれている`custom_segment_id` をメモします。従来のセグメントビルダーまたはベータセグメントビルダーの両方を使用できます。ただし、classic は最終的に非推奨になるため、ベータは推奨されています。<br><br>Punchh プラットフォームで [**Guest**] > [**Segment**] > [**Custom List**] > [**New Custom List**] に移動します。<br><br>![]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Braze でWebhook キャンペーンを作成するには、Punchh エンドポイントを使用して、ユーザーをカスタムSegmentにWebhook URL として追加します。ここでは、URL からプルされた`custom_segment_id` と`user_id` をキーと値のペアとして指定できます。<br><br>![]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. このWebhookは、単数キャンペーンとして、またはキャンバス内のステップとして設定できます。または、この特殊なパンチSegmentにユーザーs を追加するWebhookが複数のキャンペーンs またはキャンバスで使用される場合は、[テンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template) として設定できます。<br><br>
Webhook 内の `user_id` キーは、Punchh ユーザー ID にマッピングされます。ユーザーを Punchh カスタムセグメントに追加するには、Braze で作成されたすべての Webhook にこの ID を追加するする必要があります。`punch_user_id` カスタム属性は、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables) を使用して、`user_id` キーの値としてダイナミックな入力できます。`punchh_user_id` カスタム属性変数を挿入するには、任意のテンプレートテキストフィールドの右上にある青色の「プラス」アイコンを使用します。<br><br>![]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Webhook が保存されたら、以下に示すように、ユーザーの同期にこの Webhook を使用できます。たとえば、このBraze Webhook キャンペーンを起動すると、136 人のゲストが「パンチ」カスタムSegmentに追加されます。<br><br>![Braze とPunchh の統合 に伴い、保存された Webhook を使用してユーザーを同期する例。]{% image_buster /assets/img/punchh/punchh6.png %}

Brazeでのwebhookの使用方法の詳細については、[Webhookの作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。 

## ユースケースキャンペーン

### キャンペーンとキャンバスの設定

#### トリガー

Braze に送信される Punchh イベント (リワードイベントやゲストイベントなど) によりトリガーされる Braze メッセージングのユースケースは、[アクションベースのキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery)、または該当する Punchh イベントによってトリガーされるキャンバスとして作成できます。

トリガーを追加すると、Braze で作成されたイベントのリストが取得されます。キャンペーンまたはキャンバスをトリガーし、イベントを記録したユーザーに送信するイベントを選択します。

![]({% image_buster /assets/img/punchh/update5.png %})

トリガーイベントをさらに絞り込むには、プロパティフィルターを追加できます。たとえば、承認済みイベントプロパティが `true` である「checkins_gift」イベントを顧客がトリガーした場合にのみ、メッセージをトリガーします。これはオプションの機能であり、すべてのユースケースに適用できるわけではありません。 

#### セグメンテーション

多くの場合、Punchh イベントによってトリガーされる Braze キャンペーンとキャンバスには、「すべてのユーザー」オーディエンスを設定できます。これは、これらのイベントをトリガーするユーザーのセグメンテーションがが Punchh 内で決定するためです。ただし、イベントによってトリガーされる Braze メッセージを受信するユーザーからなるオーディエンスをさらに絞り込む場合は、キャンペーン作成画面の [**ターゲットオーディエンス**] セクションまたはキャンバス作成画面の [**エントリオーディエンス**] で、フィルターとセグメントを追加します。 

### ユースケース

{% tabs ローカル %}
{% tab サインアップ %}
#### 登録キャンペーン

オファーが添付されている登録キャンペーンに Braze 設定を使用する場合、Punchh 内で登録ギフティングキャンペーンを設定し、Braze でウェルカムメッセージを設定する必要があります。 

Punchh はサインアップキャンペーンに実行遅延を追加することを推奨します。そのため、Braze はゲストイベントに基づいてウェルカムメッセージを最初にトリガーできます。ギフトが贈られたことをユーザーに通知するフォローアップメッセージを送信する場合は、リワードイベントに基づいてこれをトリガーできます。

登録キャンペーンの場合、セグメントに「All signed up」を使用できるので、カスタム Braze セグメントは必要ありません。

必要な Punchh 設定:
- キャンペーン:サインアップ 
- セグメント:登録済み
- リワード:顧客が選択
必要なイベント:
- リワードイベント
- ゲストイベント
考慮事項:
- 実行遅延は、ゲストが5 ～10 分の遅延を追加することをお勧めします

![ユーザーセグメントが Punchh で設定され、ゲストがロイヤルティプログラムに登録されます。この後、ゲストイベント (トリガーされる場合) とBraze メッセージングキャンペーンがトリガーされます。次に、10分後に Punchh 登録ギフティングキャンペーンがトリガーされ、リワードイベントとオプションのフォローアップメッセージがトリガーされます。]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze ウェルカム %}
#### Braze ウェルカムキャンペーン

新しいユーザーがサインアップすると、Punchh はユーザーを作成するゲストイベントを Braze に送信し、カスタム属性`signup_channel` を送信します。これを使用して、Braze ウェルカムキャンペーンをトリガーできます。

Braze ウェルカムキャンペーンを設定するには、次のステップに従います。

1. Braze で、アクションベースのキャンペーンを作成します。
2. トリガーの場合は、[**カスタム属性値の変更**] を選択し、カスタム属性 `signup_channel` を [**新しい値**] に設定します。
3. キャンペーンを作成し続け、準備ができたら送信します。

{% endtab %}
{% tab マスオファー %}
#### マスオファーキャンペーン

ギフティングにマスオファーキャンペーンを使用する場合、マスオファーキャンペーンは Punchh 内で設定し、メッセージングキャンペーンは Braze で設定する必要があります。

Braze セグメントをキャンペーンに利用する場合や、Punchh プラットフォームでゲストにギフトを送る前に Braze からコミュニケーションを送信する場合には、Punchh ギフティングキャンペーンに[カスタム Punchh セグメント]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze)が必要になります。 

Braze でこのオファーを受け取るユーザーのセグメントを作成することは、Punchh 内で使用できない属性を使用する場合にのみ推奨されます。それ以外の場合は、Punchh セグメンテーションを使用できます。Braze メッセージング キャンペーンは、ユーザーが報酬(Punchh によってトリガーされる報酬事象)を受け取ることによって、アクションベースのキャンペーン トリガーとして作成されます。

必要な Punchh 設定:
- キャンペーン:マスオファー
- セグメント:カスタムリストまたは顧客が選択
- リワード:顧客が選択

**セグメンテーションとギフティングに Punchh を使用し、メッセージングに Braze を使用する:**<br>
たとえば、2ドル割引リワードが、Punchh 内で設定可能なセグメントに送信され、メッセージングは Braze で送信されます。<br>
![ユーザーセグメントは Punchh で設定可能であり、ユーザーは Punchh マスオファーキャンペーンでギフトを受け取ります。次に、リワードイベントがトリガーされ、その後 Braze メッセージングキャンペーンががトリガーされます。]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**ギフティングに Braze セグメンテーションおよびメッセージングと Punchh を使用する:**<br>
たとえば、パンチでは利用できない属性 s を持つSegmentに送信される$2 off 報酬 とメッセージング です。<br>
![ユーザーセグメントは Braze で設定でき、メッセージは Braze間セグメントから送信できます。次に、ユーザーはセグメントとユーザー ID を使用して Braze Webhook から Punchh カスタムセグメントに送信されます。その後、ユーザーはカスタムセグメントが設定された Punchh マスオファーキャンペーンでギフトを受け取ります。この後、リワードイベントがトリガーされます。]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**ギフティングとメッセージングのいずれかまたは両方に、Braze セグメンテーションおよびメッセージングと Punchh を使用する:**<br>
たとえば、Punchh では使用できない属性を持つセグメントに2ドル割引リワードが送信されますが、メッセージングが不要であるか、メッセージングを Punchh から送信できます (すべてのゲストが Punchh に存在している必要があることに注意してください)。<br>
![ユーザーセグメントは Braze で設定でき、ユーザーはセグメントとユーザー ID を使用して Braze Webhook を介してPunchh カスタムセグメントに送信されます。その後、ユーザーはカスタムセグメントが設定された Punchh マスオファーキャンペーンでギフトを受け取ります。この後、リワードイベントがトリガーされます。]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab 定期的なマスオファー %}
#### 定期的なマスオファーキャンペーン

定期的なマスオファーキャンペーンをギフティングに使用する場合は、Punchh 内でマスオファーキャンペーンを設定し、Braze でメッセージング キャンペーンを設定する必要があります。顧客が Braze セグメンテーションを使用する場合は、Punchh カスタムセグメントが必要です (Punchh 内で属性を使用できない場合のみ推奨)。それ以外の場合は、Punchh セグメンテーションを使用できます。Braze メッセージング キャンペーンはリワードイベントに基づいてトリガーされます。

必要な Punchh 設定:
- キャンペーン:定期的なマスオファー
- セグメント:カスタムリストまたは顧客が選択
- リワード:顧客が選択
考慮事項:
- キャンペーンID とキャンペーンの名前は、イベントのイベントプロパティとしてBraze に送信されます。キャンペーンを受け取るオーディエンスをさらに絞り込むために Braze で Punchh キャンペーン識別子を使用する場合、キャンペーン ID は毎日変更されるため、キャンペーン名を使用する必要があります。

{% endtab %}
{% tab 通知を使用するチェックイン後オファー %}
#### 通知との事後チェックインオファーキャンペーン

チェックイン後オファーキャンペーンを利用する場合、Braze はギフティングに関する通知を送信します。ゲストがチェックインすると、Punchh のチェックイン後オファーキャンペーンからギフトが送られます。したがって、チェックイン後オファーキャンペーンは Punchh 内で設定し、メッセージングキャンペーンは Braze 内で設定する必要があります (顧客にキャンペーンについて通知する場合)。

必要な Punchh 設定:
- キャンペーン:チェックイン後のオファー
- セグメント:カスタムリスト
- リワード:顧客が選択

たとえば、この週末に訪問するゲストに対し、Punchh では使用できない属性を持つセグメントに対するポイントが2倍になることを通知するメールなどです。対象となるチェックインの完了後に、このセグメントにポイントが与えられ、Braze からオプションのメッセージが送信されます。 

![ユーザー SegmentはBrazeで設定され、メッセージはチェックイン後のBrazeのキャンペーンから送信されます。次に、対象のユーザーは、セグメントとユーザー ID を使用して Braze Webhook を介して Punchh カスタムセグメントに送信されます。最後に、カスタムセグメント内の対象のユーザーがチェックインし、チェックイン後オファーキャンペーンでギフトを受け取り、オプションのメッセージを受信します。]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab 通知を使用しないチェックイン後オファー %}
#### 通知を使用しないチェックイン後オファーキャンペーン

最初に顧客に通知を送信しないチェックイン後オファーキャンペーンを使用する場合、このキャンペーンはギフトを与え (オプションのメッセージング) Braze 内で通知をトリガーします。したがって、チェックイン後のオファーキャンペーンはPunchh 内で設定する必要がありますが、カスタムリストは必要ありません。代わりに、Punchh 内で使用するセグメントを選択できます。 

必要な Punchh 設定:
- キャンペーン:チェックイン後のオファー
- セグメント:顧客が選択
- リワード:顧客が選択

たとえば、Punchh で使用可能なセグメントに、顧客に対し訪問を感謝し、次回の訪問で2ドル割引を提供する予告なしのサプライズ Braze キャンペーンが送信されます。

![該当するユーザー Segmentはパンチ内で設定でき、該当するユーザーがチェックインし、パンチ後チェックインキャンペーンを通じてギフトを受け取ります。この後、リワードイベントがトリガーされ、Braze から送信されたリワードをゲストに通知する呼び戻しメッセージが送信されます。]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab 記念日 %}
#### 記念日キャンペーン 

記念日キャンペーンを利用すると、最初に Punchh キャンペーンから記念日のギフトがユーザーに贈られます。このギフティング (リワードイベント) により、ユーザーにギフトが与えられたことを通知するメッセージングキャンペーンが Braze 内でトリガーされます。そのため、カスタムリストは必要ありません。代わりに、Punchh 内でセグメントと記念日設定を選択できます。

必要な Punchh 設定:
- キャンペーン:記念日キャンペーン
- セグメント:顧客が選択
- リワード:顧客が選択
考慮事項:
- 登録月のギフティング
- 存続期間 (誕生日リワードが有効である期間の長さは?)
- 定期的なキャンペーン、スケジュールが必要 

![オプションのセグメントは Punchh 内で作成でき、対象のユーザーは Punchh 記念日キャンペーンからリワードを受け取ります。この後、リワードイベントがトリガーされ、Braze から送信されたリワードをゲストに通知する呼び戻しメッセージが送信されます。]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab 呼び戻し %}
#### 回収キャンペーン

休眠状態に基づいてユーザーをターゲット設定するときには、呼び戻しキャンペーンを使用できます。顧客は Punchh 内でセグメントとキャンペーンを作成できますが、メッセージングには Braze を使用できます。

Braze で作成されたセグメンテーションを使用する場合は、非アクティブに基づいた[カスタムPunchh Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) を定期的な一括オファーキャンペーンにアタッチできます。

必要な Punchh 設定:
- キャンペーン:回収キャンペーン
- セグメント:顧客が選択
- リワード:顧客が選択
考慮事項:
- キャンペーンはスケジュールで実行されます

![オプションのSegmentはパンチ内で作成でき、該当するユーザーはパンチリコールキャンペーンを介して報酬を受信します。その後、リワードイベントがトリガーされ、Braze から送られたリワードをゲストに通知する呼び戻しメッセージが送信されます。.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


