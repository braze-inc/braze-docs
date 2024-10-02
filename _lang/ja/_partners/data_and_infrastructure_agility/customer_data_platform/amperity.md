---
nav_title: アンペア
article_title: アンペア
alias: /partners/amperity/
description: "この参考記事では、Brazeと包括的な企業顧客データプラットフォームであるAmperityのパートナーシップについて概説しており、Amperityユーザーの同期、データの統一、AWS S3バケットを使用したBrazeへのデータ送信などを可能にしている。"
page_type: partner
search_tag: Partner

---

# アンペア

> [Amperityは](https://amperity.com/)、包括的な企業向け顧客データプラットフォームであり、ブランドが顧客を知り、戦略的な意思決定を行い、消費者により良いサービスを提供するために常に正しい行動をとることを支援する。Amperityは、データ管理の統合、分析、洞察、活性化にわたるインテリジェントな機能を提供する。

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

BrazeとAmperityの統合は、2つのプラットフォーム間で顧客の統一されたビューを提供する。この統合により、以下のことが可能になる：
- **顧客プロファイルを同期する**：ユーザーデータとカスタム属性をAmperityからBrazeにマッピングする。 
- **オーディエンスを作成し、送信する**：アクティブな顧客のリストと関連するカスタム属性をBrazeに返すセグメントを構築し、Brazeに送信する。
- **データの更新を管理する**：カスタム属性の更新をBrazeに送信する頻度を制御する。
- **データを統一する**：Amperityがサポートする様々なプラットフォームとBrazeでデータを統合する。
- **BrazeのデータをAmazon S3に同期する**：Braze Currentsを使用して、Brazeキャンペーンからのエンゲージメントデータを統合し、Apache AvroフォーマットでAmazon S3にデータを同期できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| アンペリティ口座 | このパートナーシップを利用するには、[Amperityアカウントが](https://amperity.com/request-a-demo)必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br> これは、Brazeダッシュボードの**Developer Console**>**Rest API Key**>**Create New API Keyで**作成できる。 |
| ブレイズインスタンス | あなたのBrazeインスタンスは、あなたのBrazeオンボーディングマネージャーから取得するか、[API概要ページで]({{site.baseurl}}/api/basics#endpoints)見つけることができる。 |
| Braze RESTエンドポイント | あなたのBrazeエンドポイントURL。エンドポイントはBrazeインスタンスに依存する。 |
| 電流コネクタ（オプション） | S3カレントのコネクターだ。 |
{: .reset-td-br-1 .reset-td-br-2}

## データマッピング

標準属性とカスタム属性の両方をAmperityからBrazeに送信できるため、Amperityを通じて様々なソースからのデータでBrazeの顧客プロファイルを充実させることができる。送信できる特定の属性は、AmperityシステムのデータとBrazeで設定した属性によって異なる。

これらの属性については、以下をお読みいただきたい。

### 標準属性 

[プロフィール属性は]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)、あなたの顧客がどのような人であるかを説明する。それらはしばしば、顧客のアイデンティティと関連付けられる：
- 名前
- 生年月日
- メールアドレス
- 電話番号

### カスタム属性 

Brazeの[カスタム属性は]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)、あなたのブランドによって決定されるフィールドである。Brazeにすでに存在するカスタム属性をAmperityで管理したい場合は、Amperityから送信される出力を、Brazeワークスペースにすでにある名前に合わせる。これには以下のようなものが含まれる：
- 購入履歴
- ロイヤリティ・ステータス
- バリュー層
- 最近のエンゲージメント・データ

AmperityからBrazeに送信されるカスタム属性の名前を確認する。Amperityは、一致する名前がないときはいつでもカスタム属性を追加する。

カスタム属性は、Braze内で一致する`external_id` または`braze_id` を持つユーザーに対してのみ更新される。

### 観客数

AmperityからBrazeに同期されたオーディエンスは、カスタム属性としてユーザープロファイルに記録される。これらは、Brazeでそれらのユーザーをターゲットにするために使用できる。

![カスタムデータカテゴリに表示されるカスタム属性を持つフィルタのドロップダウンリスト。][1]{: style="max-width:60%;"}

![l12m_frequency" や "l12m_monetary" などのカスタム属性のドロップダウンリスト。][2]{: style="max-width:40%;"}

### データタイプ

サポートされているデータタイプは以下の通りである：
- ブール値
- 日付
- 日付
- 10進数
- フロート
- 整数
- String
- Varchar

使用されるデータ型は属性の性質によって異なる。例えば、Eメールアドレスは文字列、顧客の年齢は整数かもしれない。

### 属性の重複

デフォルトのユーザープロファイルフィールドと重複するカスタム属性の送信は避ける。例えば、生年月日は、Brazeの標準属性と一致するように、"dob "という名前のユーザープロファイルのフィールドとしてBrazeに送られるべきである。birthday"、"Birthdate"、またはその他の文字列として送信された場合、カスタム属性が作成され、"dob "フィールドの値は更新されない。

### データポイント

Amperityは、Brazeへのシンクの間に何が変更されたのか、全体的なセンドのステータスを追跡している。Amperityは、前回の同期以降に変更されたリストメンバーシップとその他の選択された属性のみをBrazeに送信する。  

## 統合

### ステップ1:Brazeの設定の詳細をキャプチャする

1. Brazeワークスペース用のBraze REST APIキーを作成し、**User Dataの**下に`users.track` 。`users.track` エンドポイントは、Amperityのオーディエンスをカスタム属性としてBrazeに同期する。
2. Brazeインスタンスの[REST APIエンドポイントを]({{site.baseurl}}/api/basics#endpoints)決定する。例えば、BrazeのURLが`https://dashboard-03.braze.com` 、REST APIのエンドポイントが`https://rest.iad-03.braze.com` 、インスタンスが "US-03 "の場合。
3. AmperityからBrazeに送信される[ユーザープロファイルフィールドと]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) [カスタム属性の]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)リストを決定する。

### ステップ2:Brazeをデスティネーション-DataGrid Operatorとして設定する。

#### ステップ 2a: 顧客プロファイル・テーブルを構築する

AmperityのCustomer 360データベース内に "Braze Customer Attributes "という新しいテーブルを作成する。このテーブルには、ブランドがAmperityから管理したいBrazeのすべての属性（Brazeが要求するデフォルトのユーザープロファイルのフィールドとカスタム属性の両方を含む）を含める必要がある。[Amperityのドキュメントに](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table)示されているように、SQLを使ってこのテーブルの構造を定義する。

#### ステップ 2b: テーブルに名前を付け、検証し、保存する

テーブル名を "Braze Customer Attributes "とし、保存する。テーブルが**セグメントエディター**およびキャンペーン内の**属性編集**エディターにアクセス可能であることを確認する。

#### ステップ 2c: ブラゼを目的地に追加する

Amperityプラットフォームで、**Destinations**タブに移動する。新しい目的地を追加するオプションを探す。利用可能なオプションから、**Brazeを**選択する。

![New Destinationセクションの名前は "Braze API"、説明は "Send audience attributes to Braze."、プラグインは "Braze"。][3]{: style="max-width:60%;"}

#### ステップ 2d: デスティネーションの詳細を設定する

**Brazeの**設定で、[Amperityのドキュメントに](https://docs.amperity.com/datagrid/destination_braze.html#add-destination)示されているように、Brazeの認証情報とデスティネーション設定を提供する。最後のステップで収集した構成の詳細を入力し、Braze識別子を定義する。マッチング可能な識別子は以下の通りである：
- `braze_id`:自動的に割り当てられるBrazeの識別子で、Brazeで作成されたときに特定のユーザーに関連付けられ、変更できない。
- `external_id`:顧客が割り当てた識別子で、通常はUUIDである。 

![インスタンスが "US-03"、ユーザー識別子が "external_id"、セグメント名が空白、S3バケットが "amperity-training-abc123"、S3フォルダが "braze-attributes "のBraze Settingsセクション。][4]{: style="max-width:60%;"}

#### ステップ2e：データ・テンプレートを追加する

**Destinations**タブで、Brazeデスティネーションのメニューを開き、**Add data templateを**選択する。テンプレートの名前と説明（例えば、"Braze "と "Send custom attributes to Braze"）を入力し、ビジネスユーザーのアクセスを確認し、すべての構成設定をチェックする。 

必要な設定がデスティネーションの一部として構成されていない場合は、データテンプレートの一部として構成する。データ・テンプレートを保存する。

![Data Template Nameセクションに "Braze Audience Attributes "という名前と "Send audience attributes to Braze "という説明がある。][5]{: style="max-width:60%;"}

#### ステップ2f：設定を保存する 

必要事項を記入したら、設定を保存する。Brazeがデスティネーションとして設定されたので、Amp360とAmpIQのユーザーはBrazeにデータを同期できる。

### ステップ3:データをBrazeに同期させる

AmperityのテナントでBrazeが有効になっていることを確認する。そうでない場合は、DataGridオペレーターまたはAmperityの担当者に問い合わせること。

次に、貴社に該当するAmp360またはAmpIQの同期手順に従う。

#### 同期オプション 1：Amp360経由でBrazeにクエリー結果を送信する

Amp360のユーザーは、SQLを使って自由形式のクエリーを書き、その結果をBrazeに送信するスケジュールを設定することができる。

##### ステップ1:Amperityでクエリーを作成する

Amperityのクエリー機能に移動し、目的の顧客データセットを得るためのSQLクエリーを構築する。その結果には、Brazeに送りたい特定の属性が含まれているはずだ。購入履歴を持つユーザーのリストを返すAmperityクエリーの例を参照のこと。

##### ステップ2:Amperityに新しいオーケストレーションを追加する

1. **Orchestration**セクションに行き、新しいオーケストレーションを追加するオプションをクリックする。 
2. オーケストレーションが何をすべきかを指定する。これには通常、実行されるべきSQLクエリと、その結果の送信先を指定することが含まれる。この場合、アクティブな顧客のリストを生成するために作成したSQLクエリーを選択し、結果の送信先としてBrazeを指定する。
3. オーケストレーションをいつ、どのくらいの頻度で実行するかを定義する。例えば、毎日特定の時間にオーケストレーションを実行する。
4. オーケストレーションを好みに設定したら保存する。Amperityのオーケストレーションリストに追加される。
5. オーケストレーションをテストして、期待通りに動作することを確認する。手動でオーケストレーションをトリガーし、Brazeで結果をチェックすることでこれを行うことができる。

##### ステップ3:オーケストレーションを実行する 

オーケストレーションを実行してクエリを実行し、結果をBrazeに送信する。これは手動で行うことも、オーケストレーション設定で設定したスケジュールで行うこともできる。

#### 同期オプション 2：AmpIQ経由でブレイズにオーディエンスを送る

AmpIQユーザーは、SQL以外のインターフェイスを使ってAmperityでセグメントを作成し、Brazeのような下流のデスティネーションに同期させることができる。ユーザーは送信先を選択し、各送信先に送信する属性のリストを設定することができる。

##### ステップ1:Amperityでセグメントを作成する 

Amperityで顧客のリストを返すセグメントを作成する。このセグメントは、Brazeで更新したいカスタム属性に関連付けられていなければならない。

{% alert note %}
Brazeに送信したいさまざまなセグメントタイプの例については、Amperityのドキュメントをチェックしてほしい。
{% endalert %}

##### ステップ2:Amperityでキャンペーンを構築する

1. **キャンペーン・**セクションに行き、新しいキャンペーンを作成するオプションをクリックする。
2. 特に複数のキャンペーンを行っている場合は、後でキャンペーンを識別するのに役立つ、説明的でユニークな名前を付ける。
3. このキャンペーンでターゲットにしたい顧客セグメントを選択する。これは先ほど作成したセグメントでなければならない。<br>![ターゲティングから除外するセグメントのドロップダウンフィールド。][6]{: style="max-width:50%;"}<br><br>
4. キャンペーンの一部として送信したいデータを選択する。これには、さまざまな顧客属性が含まれる。![キャンペーン属性の編集]モーダルでは、宛先と顧客属性を選択できる。 ][7]{: style="max-width:90%;"}<br><br>
5. キャンペーンデータの送信先として**Brazeを**選択する。
6. いつ、どれくらいの頻度でキャンペーンを実施するかを選択する。これは1回限りのイベントでも、定期的なスケジュールでも構わない。
7. キャンペーンを保存してテストを実行し、期待通りに機能することを確認する。

##### ステップ3:キャンペーンを実施する

Brazeにセグメントを送信するためにキャンペーンを実行する。これは手動で行うことも、キャンペーン設定で設定したスケジュールに基づいて行うこともできる。


### ブレージング電流でアンペリティを使う
Braze CurrentsのデータをAmperityに送信する：
1. Amazon S3バケットにデータを送信するために[Braze Currentをセットアップ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/)する。
2. [そのAmazon S3バケットからApache Avroファイルを読み込む](https://docs.amperity.com/datagrid/source_amazon_s3.html)ようにAmperityを設定する。
3. フィードを設定し、標準的なワークフローを使用してデータロードを自動化する。

[1]: {% image_buster /assets/img/amperity/custom_attributes_filters.png %}
[2]: {% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}
[3]: {% image_buster /assets/img/amperity/destination_name.png %}
[4]: {% image_buster /assets/img/amperity/braze_settings.png %}
[5]: {% image_buster /assets/img/amperity/data_template_name.png %}
[6]: {% image_buster /assets/img/amperity/select_segments.png %}
[7]: {% image_buster /assets/img/amperity/edit_campaign_attributes.png %}
