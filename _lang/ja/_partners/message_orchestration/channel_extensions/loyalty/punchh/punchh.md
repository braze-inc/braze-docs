---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "このリファレンス記事では、ロイヤルティとエンゲージメント プラットフォームであるBraze とパンチの提携について概説します。これにより、2 つのプラットフォームs 間でデータを同期できます。Braze で公開されたデーターはセグメンテーションに使用でき、Braze で設定されたWebhook テンプレートを使ってユーザーデータをパンチに戻すことができます。"
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/)は、ブランドが店内でもデジタルでもオムニチャネル 顧客 ロイヤルティプログラムを配信できる、業界をリードするロイヤルティとエンゲージメント プラットフォームです。 

Braze とパンチインテグレーションでは、2 つのプラットフォームs 間でギフトやロイヤルティのためにデータを同期できます。Braze で公開されたデーターはセグメンテーションに使用でき、ユーザーデータをBraze webhook でパンチに戻すことができます。

## メリットは何でしょうか。

- パンチからBrazeへのロイヤルティをリアルタイムで取り込みます。 
- Brazeからの強力なオーディエンス情報を活用し、意味のあるダイナミックな クロスチャネルの体験(アプリ、モバイル、ウェブ、メール、SMS)を提供する
  - 顧客 sはsを開封 メールしましたか?顧客は店の近くでアプリを開封しましたか？
- Brazeで送信されるアクション間のメールのルックアンドフィールを標準化します。
- A/B テストと最適化を可能にするジャーニーを作成します。

## 前提条件

| 要件 | 説明 |
|---|---|
| パンチアカウント | この提携の前進タグeを考慮するには、積極的なパンチの勘定が必要である。 |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | \[Your REST エンドポイント URL][6].エンドポイントは、インスタンスのBraze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 他に何を知るべきですか？

#### 統合前

- Brazeインテグレーションを使用する場合、パンチに1つ、Brazeに2つのキャンペーンsが必要です。たとえば、オファーが添付されたキャンペーンを送信すると、ギフトキャンペーンはパンチ内で設定され、通知はBrazeから送信できます。
- ゲストはパンチとBrazeにすでに存在するはずです。パンチはまだロイヤルティ客でない顧客をフィルターするだろう。

#### 注意すべき重要事項

- パンチはデフォルト ユーザー 属性sのBrazeへの送信を無効にする機能を追加したので、顧客はデータポイント 超過料金sを発生させません。これは、アダプターのセットアップ中に構成されます。
- キャンペーンが実行されるたびにID が変更されるため、定期的なキャンペーンでカスタムSegments を使用する場合は、キャンペーン ID の代わりにキャンペーンの名前を使用する必要があります。
- パンチギフトキャンペーンで使用できる通信チャネルには、リッチメッセージ、プッシュ通知s、SMS、メールがあります。
- ユーザー s がBraze からパンチカスタムSegmentに送信された後は、削除できません。既存のカスタムSegmentに追加できるのは、新しいゲストのみです。既存のPunchhカスタムSegmentからゲストを削除する必要がある場合は、新しいPunchhカスタムSegmentにユーザーを送信するために、新しいWebhook キャンペーンをBrazeで作成する必要があります。

## 統合

Punchh には、以下のPunchh API エンドポイントを使用して外部ID をPunchh プラットフォームに追加するために、Braze 顧客 s で使用できるいくつかのエンドポイントが用意されています。外部ID を追加したら、Punchh でアダプターを作成し、Braze 認証情報を入力して、同期したい行動を選択します。次に、パンチSegment ID を取得し、それを使用してパンチWebhookを作成し、キャンバスの旅行で同期をトリガー 顧客できます。

Punchh `user_id` はカスタム属性"punchh_ユーザー_id" としてBraze ユーザープロファイルに追加する必要があることに注意してください。同様に、Braze で使用されている`external_id` は、Punchh ユーザープロファイルの`external_source_id` フィールドとして含める必要があります。 

### ステップ1:外部ID 取り込みエンドポイントの設定s

Braze の外部ID は、新規および既設のパンチユーザーs の次のエンドポイントs を使用して追加できます。

{% alert important %}
`external_source` および`external_source_id` フィールドは、Punchh に対して一意であり、存在するプロファイルs に関連付けられていない必要があります。
{% endalert %}

1. 新型パンチユーザー<br>
`external_source` および`external_source_id` フィールドs を使用して、Punchh サインアップエンドポイントでPunchh に新しいユーザーs を作成します。パンチ機能を使用すると、次のいずれかのサインアップエンドポイントs を使用して、external ID全体をユーザープロファイルで送信できます。
- [モバイルサインアップAPI](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO サインアップAPI](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 従来のパンチユーザー <br>
既設パンチユーザーs の`external_source_id` をアップデートします。パンチ機能を使用すると、ユーザー API 更新 エンドポイントを介してexternal ID全体をプロファイルに追加できます。 
- [モバイルユーザーの更新](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO ユーザー更新](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [ダッシュボードユーザーの更新](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs ローカル %}
{% tab ユーザーサインアップAPI の例 %}
このサンプルでは、サインアップ時にユーザープロファイルを持つexternal ID全体を送信できます。これは、`external_source` を"顧客_id" および`external_source_id` を"111111111111111111" として文字列データ型として送信することによって行われます。

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
{% tab ユーザ更新の事例 %}
このサンプルでは、ユーザープロファイルを使用して全体を更新 external IDできます。これは、`external_source` を"顧客_id" および`external_source_id` を"111111111111111111" として文字列データ型として送信することによって行われます。

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
**プラットフォーム設定:**Punchh でexternal ID全体を有効にするには、Punchh ダッシュボードから**Cockpit**> **ダッシュボード**> **外部ユーザ識別子** に移動します。
{% endalert %}

### ステップ2:パンチでのBrazeアダプターの設定

#### 同期可能なイベント {#available-events-to-sync}

1. **ゲスト:**サインアップ、ゲストプロファイルへの更新、非アクティブ化または削除時にトリガされます
2. **ロイヤリティチェックイン:**ロイヤルティのトランスアクションでトリガーされるか、レシートからバーコードをスキャンして獲得します
3. **ギフトチェックイン:**キャンペーンから贈られた点をトリガー
4. **償還:**パンチクーポンを除く報酬償還の場合にトリガーされます。これは、発行と償還を含むクーポンイベントとして別々に送信されるためです
5. **報酬:**報酬がキャンペーンs、活動、点から報酬sへのコンバージョン、または管理者ギフトから贈られたことをきっかけにした
6. **トランスアクション通知:**パンチシステム内のユーザーのtrans アクション al アクティビティでトリガーされます(たとえば、ポイントの有効期限)。
7. **マーケティング通知:**ユーザー s の関連付けられたSegmentに対して、パンチでのさまざまなキャンペーン設定に基づいてトリガーされます

{% alert note %}
参考パンチドキュメントでは、これらの利用可能なイベントのサンプル有料読み込むがどのように見えるかを確認できます。
{% endalert %}

このアダプターをセットアップするには、パンチインプリメンテーション・マネージャーを使用します。

Brazeとパンチインテグレーションを設定するには、以下の手順に従います。

1. パンチダッシュボードで、**コックピット**> **ダッシュボード**> **主な機能**> **Webフック管理を有効にし、**Webフック管理を有効にします**。<br><br>
2. 次に、**Settings**> **Webフックマネージャ**> **Configurations**> **Show Adapters Tab**に移動してアダプタを有効にし、**Show Adapters Tab**で切り替えます。<br><br>
3. **Webフックマネージャ**の**設定**タブに移動し、**アダプタ**タブを選択し、**アダプタの作成**をクリックします。<br><br>![][1]<br><br>
4. アダプターの名前、説明、および管理メールを入力します。アダプターとして **Braze** を選択し、Braze REST API エンドポイントとBraze API キーを入力します。<br><br>
5. 次に、有効にするイベントを選択します。これらのイベントのリストは、[Available events to sync](#available-events-to-sync)にあります。<br><br>![][3]<br><br>
6. **Submit**を押してWebhookを有効にします。

## Braze でのパンチWebhookの作成

Braze は、ユーザー s をパンチSegmentに、パンチカスタムSegments を使用するwebhookを介して追加できます。

1. Punchh でカスタムSegmentを作成し、Punchh Segment ダッシュボード URL に存在する`custom_segment_id` を以下のように書き留めます。古典的またはβSegmentビルダーの両方を使用できます。ただし、classic は最終的に非推奨になるため、ベータは推奨されています。<br><br>パンチプラットフォームで、**ゲスト**> **セグメント**> **カスタムリスト**> **新規カスタムリスト** に移動します。<br><br>![][8]<br><br>

2. Braze でWebhook キャンペーンを作成するには、Punchh エンドポイントを使用して、ユーザーをカスタムSegmentにWebhook URL として追加します。ここでは、URL からプルされた`custom_segment_id` と`user_id` をキーと値のペアとして指定できます。<br><br>![][4]<br><br>

3. このWebhookは、単数キャンペーンとして、またはキャンバス内のステップとして設定できます。または、この特殊なパンチSegmentにユーザーs を追加するWebhookが複数のキャンペーンs またはキャンバスで使用される場合は、[テンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template) として設定できます。<br><br>
Webhook内の`user_id` キーは、パンチユーザー IDにマップされます。この識別子は、Braze で作成されたすべてのwebhookに追加して、ユーザーs をパンチカスタムSegmentに追加する必要があります。`punch_user_id` カスタム属性は、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables) を使用して、`user_id` キーの値としてダイナミックな入力できます。`punchh_user_id` カスタム属性は、青色の"plus" アイコンを使用して挿入できます。アイコンは、任意のテンプレートd テキストフィールドの右上にあります。<br><br>![][10]{: style="max-width:65%;"}<br><br>![][11]{: style="max-width:65%;"}<br><br>

4. Webhookが保存されたら、以下に示すようにユーザーs を同期するために使用できます。たとえば、このBraze Webhook キャンペーンを起動すると、136 人のゲストが「パンチ」カスタムSegmentに追加されます。<br><br>![Brazeとパンチインテグレーションによって保存されたWebhookを使用してユーザーsを同期するサンプル。][7]

Brazeでのwebhookの使用方法の詳細については、[Webhookの作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。 

## ユースケースキャンペーン

### キャンペーンとキャンバスの設定

#### トリガー

報酬イベントやゲストイベントなど、パンチイベントがBrazeに送信するBraze メッセージング トリガーのユースケースは、[アクション ベースのキャンペーンs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) または該当するパンチイベントによってトリガーされるキャンバスとして作成できます。

トリガーを追加すると、Braze で作成された行動の一覧がプルアップされます。キャンペーンまたはキャンバスをトリガーし、イベントを記録したユーザーに送信するイベントを選択します。

![][12]

プロパティー・フィルターs を追加して、トリガーの実行イベントをさらにフィルターできます。たとえば、メッセージは、顧客 トリガーが"checkins_gift"event の場合にのみトリガーされます。この場合、アプリのroved イベントプロパティは`true` です。これは、すべてのユースケースにアプリ使用できるわけではないオプション機能です。 

#### セグメンテーション

多くの場合、パンチイベントによってトリガーされているBraze キャンペーン s とキャンバスは"すべてのユーザー s" オーディエンスに設定できます。これは、これらのイベントをトリガーするユーザー s のセグメンテーションがパンチ内で決定されるためです。ただし、顧客 は、イベントによってBraze メッセージング トリガーを受け取るユーザーs のオーディエンスをさらに絞り込むために、キャンバスコンポーザーの**Target オーディエンス s** セクションまたは**Entry オーディエンス** にフィルターs とSegments を追加します。 

### ユースケース

{% tabs ローカル %}
{% tab サインアップ %}
#### 登録キャンペーン

オファーが添付されているサインアップキャンペーンのBraze設定を使用する場合、Punchh内でサインアップギフトキャンペーンを設定し、Brazeでウェルカムメッセージを設定する必要があります。 

Punchh はサインアップキャンペーンに実行遅延を追加することを推奨します。そのため、Braze はゲストイベントに基づいてウェルカムメッセージを最初にトリガーできます。ユーザーに贈られたことを知らせるフォローアップメッセージを送りたい場合は、報酬の出来事に基づいてトリガーすることができます。

サインアップキャンペーンでは、すべてのサインアップをSegmentに使用できるため、カスタムBraze Segmentは必要ありません。

必要なパンチ構成:
- キャンペーン:サインアップ 
- セグメント情報:登録済み
- 報酬:顧客選択
必要なイベント:
- 報奨イベント
- ゲストイベント
考慮事項:
- 実行遅延は、ゲストが5 ～10 分の遅延を追加することをお勧めします

![ユーザー Segmentがパンチで設定され、ゲストがロイヤルティプログラムにサインアップします。この後、ゲストイベント(トリガー の場合) がed になり、Braze メッセージング キャンペーンがトリガーed になります。次に、パンチ・サインアップ・ギフト・キャンペーンは、10分後にトリガーされ、報酬・イベントとオプションのフォローアップ・メッセージがトリガーされます。]({% image_buster /assets/img/punchh/usecase3.png %})

{% endtab %}
{% tab マスオファー %}
#### マスオファーキャンペーン

プレゼントに大量のオファーキャンペーンを使用する場合、パンチとBrazeのメッセージング キャンペーン内で大量のオファーキャンペーンを設定する必要があります。

Braze Segmentをキャンペーンに利用したり、Brazeから通信を送信したりする場合は、パンチキャンペーンに[カスタムパンチSegment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze)が必要になります。 

Brazeでこのオファーを受信するユーザーsのSegmentを作成することは、パンチ内で使用できない属性を使用する場合にのみ推奨されます。それ以外の場合は、Punchh セグメンテーションを使用できます。Braze メッセージング キャンペーンは、ユーザーが報酬(Punchh によってトリガーされる報酬事象)を受け取ることによって、アクションベースのキャンペーン トリガーとして作成されます。

必要なパンチ構成:
- キャンペーン:マスオファー
- セグメント情報:カスタムリストまたは顧客の選択肢
- 報酬:顧客選択

**セグメンテーションとギフトにパンチ、メッセージングにBrazeを使用:**<br>
たとえば、$2 off 報酬は、パンチ内で設定可能なSegmentに送信され、メッセージングはBraze 経由で送信されます。<br>
![ユーザー Segmentはパンチで設定でき、ユーザー sはパンチマスオファーキャンペーンを通じてプレゼントを受け取ります。次に、報酬事象がトリガーされ、次にBraze メッセージング キャンペーンがトリガーされます。]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**ギフトにBraze セグメンテーションとメッセージング、パンチを使用する:**<br>
たとえば、パンチでは利用できない属性 s を持つSegmentに送信される$2 off 報酬 とメッセージング です。<br>
![ユーザー SegmentはBrazeで設定でき、その後、BrazeからBraze Segmentにメッセージを送信できます。次に、ユーザーsは、パンチカスタムSegmentに、Segmentとユーザー IDを備えたBraze Webhookを通して送られる。その後、ユーザーはパンチマスオファーキャンペーンで特注のSegmentでプレゼントを受け取ります。この後の報酬事象はトリガー ed.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**ギフトまたはメッセージング、またはその両方にBraze セグメンテーションとパンチを使用する:**<br>
たとえば、$2 off 報酬は、Punchh で使用できない属性 s を持つSegmentに送信されますが、メッセージングは必要ありません。または、メッセージングはPunchh 経由で送信できます(すべてのゲストがPunchh に存在する必要があることに注意してください)。<br>
![ユーザー SegmentはBraze で設定でき、ユーザーs はSegment とユーザー ID のBraze Webhookを介してパンチカスタムSegmentに送信されます。その後、ユーザーはパンチマスオファーキャンペーンで特注のSegmentでプレゼントを受け取ります。この後の報酬事象はトリガー ed.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab 定期的なマスオファー %}
#### 定期的なマスオファーキャンペーン

定期的なマスオファーキャンペーンをギフトに使用する場合は、パンチ内にマスオファーキャンペーンを設定し、Brazeにメッセージング キャンペーンを設定する必要があります。顧客がBraze セグメンテーションを使用する場合は、パンチカスタムSegmentが必要になります(パンチ内で属性を使用できない場合のみ推奨)。それ以外の場合は、パンチセグメンテーションを使用でき、Braze メッセージング キャンペーンは報酬の事象に基づいてトリガーされます。

必要なパンチ構成:
- キャンペーン:定期的なマスオファー
- セグメント情報:カスタムリストまたは顧客の選択肢
- 報酬:顧客選択
考慮事項:
- キャンペーンID とキャンペーンの名前は、イベントのイベントプロパティとしてBraze に送信されます。キャンペーンを受信するオーディエンスをさらにフィルターするためにBrazeでパンチキャンペーン 識別子を使用する場合は、キャンペーンID が毎日変更されるため、キャンペーンの名前を使用する必要があります。

{% endtab %}
{% tab 通知によるチェックイン後のオファー %}
#### 通知との事後チェックインオファーキャンペーン

チェックイン後のオファーキャンペーンを利用する場合、Brazeはプレゼントに関する通知を送付し、ゲストがチェックインを行うと、パンチ後のチェックインキャンペーンからプレゼントされます。したがって、チェックイン後のオファーキャンペーンは、パンチとBrazeのメッセージング キャンペーン内で設定する必要があります(キャンペーンを顧客に通知する場合)。

必要なパンチ構成:
- キャンペーン:チェックイン後のオファー
- セグメント情報:カスタムリスト
- 報酬:顧客選択

例えば、今週末に来訪することを客に知らせるメールは、パンチでは利用できない属性sのあるSegmentをダブルポイントする。Brazeからの適格なチェックインとオプションのメッセージングの後に、パンチがこのSegment点をプレゼントします。 

![ユーザー SegmentはBrazeで設定され、メッセージはチェックイン後のBrazeのキャンペーンから送信されます。次に、該当するユーザーsが、パンチカスタムSegmentに、Segmentとユーザー IDのBraze Webhookを介して送信されます。最後に、カスタムSegmentの修飾ユーザーは、チェックイン後のキャンペーン]({% image_buster /assets/img/punchh/update7.png %}) を通じてギフトとオプションメッセージをチェックインして受け取ります。

{% endtab %}
{% tab 通知のない事後チェックインオファー %}
#### チェックイン後のオファーキャンペーン(通知なし)

キャンペーンは、最初に顧客に通知しないチェックイン後のオファーキャンペーンを使用する場合、ギフト(オプションメッセージング)を付与し、Braze内の通知をトリガーします。したがって、チェックイン後のオファーキャンペーンはPunchh 内で設定する必要がありますが、カスタムリストは必要ありません。代わりに、パンチ内で希望するSegmentを選択することができます。 

必要なパンチ構成:
- キャンペーン:チェックイン後のオファー
- セグメント情報:顧客選択
- 報酬:顧客選択

例えば、パンチで利用可能なSegmentに、驚きと喜びのBraze キャンペーンが送られ、来客の来訪に感謝し、次回の訪問から2ドルで報酬する。

![該当するユーザー Segmentはパンチ内で設定でき、該当するユーザーがチェックインし、パンチ後チェックインキャンペーンを通じてギフトを受け取ります。この後、報酬事象がトリガーされ、ゲストにBraze.]({% image_buster /assets/img/punchh/usecase2.png %})から送信された報酬を通知するリコールメッセージが送信されます。

{% endtab %}
{% tab 記念日 %}
#### 記念日キャンペーン 

記念日キャンペーンをご利用の際は、まずパンチキャンペーンから記念日のユーザーをプレゼントします。このギフト(報酬行事)は、ギフトのユーザーを通知するBraze内のメッセージング キャンペーンをトリガーします。そのため、カスタムリストは必要ありません。代わりに、パンチ内のSegmentと記念日の設定を選択することができます。

必要なパンチ構成:
- キャンペーン:記念日キャンペーン
- セグメント情報:顧客選択
- 報酬:顧客選択
考慮事項:
- 登録プレゼント月
- 存続期間(誕生日報酬はどのくらい有効ですか?)
- 経常キャンペーン、必要スケジュール 

![オプションのSegmentはパンチ内で作成でき、該当するユーザーはパンチ・アニバーサリー・キャンペーンを通じて報酬を受信します。この後、報酬事象がトリガーされ、ゲストにBraze.]({% image_buster /assets/img/punchh/usecase1.png %})から送信された報酬を通知するリコールメッセージが送信されます。

{% endtab %}
{% tab リコール %}
#### 回収キャンペーン

非アクティブに基づいてユーザーs をターゲットにする場合は、リコールキャンペーンを使用できます。顧客はパンチ内にSegmentとキャンペーンを作成できますが、メッセージングにはBrazeを使用します。

Braze で作成されたセグメンテーションを使用する場合は、非アクティブに基づいた[カスタムPunchh Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) を定期的な一括オファーキャンペーンにアタッチできます。

必要なパンチ構成:
- キャンペーン:回収キャンペーン
- セグメント情報:顧客選択
- 報酬:顧客選択
考慮事項:
- キャンペーンはスケジュールで実行されます

![オプションのSegmentはパンチ内で作成でき、該当するユーザーはパンチリコールキャンペーンを介して報酬を受信します。この後、報酬事象がトリガーされ、ゲストにBraze.]({% image_buster /assets/img/punchh/usecase.png %})から送信された報酬を通知するリコールメッセージが送信されます。

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#エンドポイントs
[8]: {% image_buster /assets/img/punchh/update1.png %}
[9]: {% image_buster /assets/img/punchh/update2.png %}
[10]: {% image_buster /assets/img/punchh/update3.png %}
[11]: {% image_buster /assets/img/punchh/update4.png %}
[12]: {% image_buster /assets/img/punchh/update5.png %}
[13]: {% image_buster /assets/img/punchh/update6.png %}
[14]: {% image_buster /assets/img/punchh/update7.png %}
