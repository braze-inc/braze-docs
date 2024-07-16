---
nav_title: Amperity
article_title:Amperity
alias: /partners/amperity/
description:「この参考記事では、包括的なエンタープライズ顧客データプラットフォームであるBrazeとAmperityのパートナーシップの概要を説明しています。これにより、Amperityユーザーの同期、データの統合、AWS S3 バケットを使用したBrazeへのデータ送信などが可能になります。「
page_type: partner
search_tag:Partner

---

# Amperity

> [Amperityは包括的なエンタープライズ顧客データプラットフォームであり](https://amperity.com/)、ブランドが顧客について知り、戦略的意思決定を行い、消費者により良いサービスを提供するために常に正しいアクションを取るのに役立ちます。Amperityは、データ管理の統合、分析、洞察、およびアクティベーションにわたるインテリジェントな機能を提供します。

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

Braze と Amperity の統合により、2 つのプラットフォームにわたる顧客情報を統一的に把握できます。この統合により、次のことが可能になります。
- **顧客プロフィールの同期**:ユーザーデータカスタム属性を Amperity から Braze にマッピングします。 
- **オーディエンスの作成と送信**:アクティブな顧客のリストとそれに関連するカスタム属性を Braze に返すセグメントを作成し、Braze に送信します。
- **データ更新の管理**:カスタム属性の更新を Braze に送信する頻度を制御します。
- **データを統合**:Amperity がサポートするさまざまな Amperity プラットフォームと Braze のデータを統合します。
- **Braze データを Amazon S3 に同期**:Braze Currents を使用して Braze キャンペーンのエンゲージメントデータを統合すると、データを Apache Avro 形式で Amazon S3 に同期できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amperity 口座 | このパートナーシップを利用するには、[Amperity アカウントが必要です](https://amperity.com/request-a-demo)。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br> これは、Braze ダッシュボードで \[**開発者コンソール**] > \[**Rest API キー] > \[**新しい API キーを作成****] に移動して作成できます。 |
| Brazeインスタンス | Brazeインスタンスは Braze オンボーディングマネージャーから入手するか、[API]({{site.baseurl}}/api/basics#endpoints) 概要ページにあります。 |
| Braze REST エンドポイント | あなたの Braze エンドポイント URL。エンドポイントは Brazeインスタンスによって異なります。 |
| Currents コネクタ (オプション) | S3 Currents コネクター。 |
{: .reset-td-br-1 .reset-td-br-2}

## データマッピング

標準属性とカスタム属性の両方をAmperityからBrazeに送信できるため、Amperityを通じてさまざまなソースからのデータでBrazeの顧客プロファイルを充実させることができます。送信できる具体的な属性は、Amperityシステムのデータと、Brazeで設定した属性によって異なります。

これらの属性については、以下をお読みください。

### 標準属性 

[プロファイル属性は]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)、顧客が誰であるかを表します。多くの場合、次のような顧客身元に関連付けられます。
- 名前
- 生年月日
- Eメールアドレス
- 電話番号

### カスタム属性 

Braze [のカスタム属性は]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)、ブランドによって決まるフィールドです。Amperity に Braze にすでに存在するカスタム属性を管理させたい場合は、Amperity から送信される出力を Braze ワークスペースにすでに存在する名前に合わせてください。これには以下が含まれます。
- 購入履歴
- ロイヤルティステータス
- バリュー階層
- 最近のエンゲージメントデータ

Amperity から Braze に送信されるカスタムアトリビュートの名前を確認してください。Amperity は、一致する名前がない場合はいつでもカスタム属性追加します。

カスタム属性は、`external_id``braze_id`一致するユーザーまたはBraze内のユーザーに対してのみ更新されます。

### Amperity・オーディエンス

AmperityからBrazeに同期されたオーディエンスは、カスタム属性としてユーザープロファイルに記録されます。その後、これらを使用してBrazeのユーザーをターゲットにすることができます。

![カスタムデータカテゴリに表示されるカスタム属性を含むフィルタのドロップダウンリスト。][1]{: style="max-width:60%;"}

![「l12m_frequency」や「l12m_monetary」などのカスタム属性のドロップダウンリスト。][2]{: style="max-width:40%;"}

### データタイプ

サポートされているデータ型は次のとおりです。
- ブール値
- 日付
- 日時
- 十進法
- フロート
- 整数
- String
- ヴァルチャー

使用されるデータタイプは、属性性質によって異なります。たとえば、メールは文字列で、顧客の年齢は整数かもしれません。

### 属性の複製

デフォルトユーザープロファイルフィールドと重複するカスタム属性を送信しないでください。たとえば、誕生日は Braze の標準属性項目と一致する「dob」という名前のユーザープロファイルフィールドとして Braze に送信する必要があります。「birthday」、「Birthdate」、またはその他の文字列として送信された場合、カスタム属性作成され、「dob」フィールドの値は更新されません。

### データポイント

Amperityは、Brazeへの同期と送信全体のステータスとの間に何が変化したかを追跡します。Amperityは、前回の同期以降に変更されたリストのメンバーシップとその他の選択された属性のみをBrazeに送信します。  

## 統合

### ステップ1:Braze の設定の詳細をキャプチャする

1. `users.track`**ユーザーデータの権限を使用して**、Braze ワークスペース用の Braze REST API キーを作成します。`users.track`エンドポイントは Amperity オーディエンスカスタム属性として Braze に同期します。
2. Brazeインスタンスの [REST API エンドポイントを決定します]({{site.baseurl}}/api/basics#endpoints)。たとえば、Braze URL `https://dashboard-03.braze.com` がで、REST API エンドポイント`https://rest.iad-03.braze.com`がで、インスタンスが「US-03」の場合。
3. Amperity から Braze [[に送信できるユーザープロファイルフィールドとカスタム属性のリストを決定します]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)。

### ステップ2:Braze を送信先として設定—データグリッドオペレーター

#### ステップ 2a: 顧客プロファイル表の作成

Amperity の Customer 360 データベース内に「Braze 顧客属性」という名前の新しいテーブルを作成します。この表には、Brazeが必要とするデフォルトユーザープロファイルフィールドとカスタム属性の両方を含め、ブランドがAmperityで管理したいBrazeのすべての属性が含まれている必要があります。[Amperity](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table) のドキュメントに示されているように、SQL を使用してこのテーブルの構造を定義します。

#### ステップ 2b: テーブルに名前を付けて検証し、保存する

テーブルに「Braze 顧客属性」という名前を付けて保存します。****キャンペーン内のセグメントエディターと属性編集エディターから表にアクセスできることを確認します****。

#### ステップ 2c: Braze 送信先として追加

Amperity プラットフォームで、「**宛先**」タブに移動します。新しい送信先を追加するオプションを探してください。使用可能なオプションから、**Braze** を選択します。

![「Braze API」という名前の新しいデスティネーションセクション、「オーディエンス属性をBrazeに送信」の説明が付いています。「、そして「Braze」のプラグイン。][3]{: style="max-width:60%;"}

#### ステップ 2d: 送信先の詳細を設定

**Amperityのドキュメントに記載されているように**[、Braze設定で、Brazeの認証情報と送信先設定を入力します](https://docs.amperity.com/datagrid/destination_braze.html#add-destination)。最後のステップで収集した設定の詳細を入力し、Braze 識別子を定義します。照合できる識別子は次のとおりです。
- `braze_id`:自動的に割り当てられる Braze 識別子で、変更できず、Braze で作成した時点で特定のユーザーに関連付けられます。
- `external_id`:顧客によって割り当てられた識別子 (通常は UUID)。 

![「US-03」のインスタンス、「external_id」のユーザー識別子、空白のSegment 名、「amperity-training-abc123」のS3バケット、「braze属性」のS3フォルダを含むBraze設定セクション。][4]{: style="max-width:60%;"}

#### ステップ 2e:データテンプレートを追加する

「**送信先**」タブで、Braze 送信先のメニュー開封、「**データテンプレートを追加**」を選択します。テンプレート名前と説明 (「Braze」や「カスタム属性を Braze に送信」など) を入力し、ビジネスユーザーアクセスを確認し、すべての設定を確認します。 

必要な設定が送信先の一部として構成されていない場合は、データテンプレートの一部として構成します。データテンプレートを保存します。

![「Braze オーディエンス属性」という名前と「オーディエンス属性を Braze に送信」という説明が付いたデータテンプレート名セクション。「][5]{: style="max-width:60%;"}

#### ステップ 2f:設定を保存する 

必要な詳細を入力したら、設定を保存します。Braze が送信先として設定されたので、Amp360 と AmpIQ のユーザーはデータを Braze に同期できます。

### ステップ3:データを Braze に同期する

Amperity テナントで Braze が有効になっていることを確認してください。そうでない場合は、DataGrid オペレーターまたは Amperity の担当者にお問い合わせください。

次に、会社に適用される Amp360 または AmpIQ の同期手順に従ってください。

#### 同期オプション 1:クエリ結果をAmp360経由でBraze に送信する

Amp360ユーザーは、SQLを使用して自由形式のクエリを作成し、その結果をBrazeに送信するスケジュールを設定できます。

##### ステップ1:Amperity でクエリを作成する

Amperity のクエリ関数に移動し、必要な顧客データセットを生成する SQL クエリを作成します。結果には、Braze に送信したい特定の属性が含まれている必要があります。購入履歴を含むユーザーのリストを返すには、このAmperityクエリの例を参照してください。

##### ステップ2:Amperity に新しいオーケストレーションを追加する

1. **オーケストレーションセクションに移動し、オプションをクリックして新しいオーケストレーションを追加します**。 
2. オーケストレーションが何をすべきかを指定してください。これには通常、実行する SQL クエリと結果の送信先を指定する必要があります。この場合、作成した SQL クエリを選択してアクティブな顧客のリストを生成し、結果の送信先として Braze を指定します。
3. オーケストレーションをいつ、どのくらいの頻度で実行するかを定義します。たとえば、毎日特定の時間にオーケストレーションを実行できます。
4. 好みに合わせて構成したら、オーケストレーションを保存します。Amperity のオーケストレーションのリストに追加されます。
5. オーケストレーションをテストして、期待どおりに動作することを確認します。そのためには、オーケストレーションを手動でトリガーし、Braze で結果を確認します。

##### ステップ3:オーケストレーションを実行する 

オーケストレーションを実行してクエリを実行し、結果を Braze に送信します。これは手動で行うことも、オーケストレーション設定で設定したスケジュールに従って行うこともできます。

#### 同期オプション 2:AMPiQ 経由でオーディエンスを Braze に送信

AMPiQユーザーは、非SQLインターフェイス介してAmperityでセグメントを作成し、それらをBrazeなどのダウンストリームの宛先に同期できます。ユーザーは宛先を選択し、各送信先に送信する属性のリストを設定できます。

##### ステップ1:Amperity でSegment を作成する 

顧客のリストを返すSegment を Amperity に作成します。このSegment は、Braze で更新したいカスタムアトリビュートに関連付けられている必要があります。

{% alert note %}
Braze に送信したいさまざまなSegment タイプの例については、Amperity のドキュメントをご覧ください。
{% endalert %}

##### ステップ2:Amperity でキャンペーンを作成

1. 「**キャンペーン**」セクションに移動し、オプションをクリックして新しいキャンペーンを作成します。
2. キャンペーンには、特に複数のキャンペーンがある場合に、後で識別しやすいわかりやすく一意の名前を付けてください。
3. このキャンペーンでターゲットにしたい顧客のSegment を選択します。これは前に作成したSegment でなければなりません。<br>![ターゲティングから除外するセグメントのドロップダウンフィールド。][6]{: style="max-width:50%;"}<br><br>
4. キャンペーン一環として送信するデータを選択します。これには、さまざまな顧客属性が含まれる場合があります。![キャンペーン属性の編集モーダルでは、送信先と顧客属性を選択できます。 ][7]{: style="max-width:90%;"}<br><br>
5. キャンペーンデータの送信先として **Braze** を選択します。
6. キャンペーンをいつ、どのくらいの頻度で実施するかを選択します。これは、1 回限りのイベントでも、定期的なスケジュールでもかまいません。
7. キャンペーンを保存し、テストを実行して期待どおりに動作することを確認します。

##### ステップ3:キャンペーンを実行する

キャンペーンを実行してSegment を Braze に送信します。これは手動で行うことも、キャンペーン設定で設定したスケジュールに基づいて行うこともできます。


### Amperity とろうBraze Currents 使い方
AmperityにBraze Currents データを送信するには:
1. Amazon S3 [バケットにデータを送信するようにBraze カレントを設定します]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/)。
2. [その Amazon S3 バケットから Apache Avro ファイルを読み取るように](https://docs.amperity.com/datagrid/source_amazon_s3.html) Amperity を設定します。
3. 標準ワークフローを使用してフィードを設定し、データロードを自動化します。

[1]: {% image_buster /assets/img/amperity/custom_attributes_filters.png %}
[2]: {% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}
[3]: {% image_buster /assets/img/amperity/destination_name.png %}
[4]: {% image_buster /assets/img/amperity/braze_settings.png %}
[5]: {% image_buster /assets/img/amperity/data_template_name.png %}
[6]: {% image_buster /assets/img/amperity/select_segments.png %}
[7]: {% image_buster /assets/img/amperity/edit_campaign_attributes.png %}
