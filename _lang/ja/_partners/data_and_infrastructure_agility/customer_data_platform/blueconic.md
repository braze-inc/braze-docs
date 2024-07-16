---
nav_title: BlueConic
article_title:ブルーコニック
description:この記事は、BrazeとBlueConic（主要な純粋な顧客データプラットフォーム）とのパートナーシップを概説しており、永続的な個別プロファイル全体でデータを統合し、Amazon Web Services S3サーバーを介してインポート目標のために2つのシステム間で同期することができます。
alias: /partners/blueconic/
page_type: partner
search_tag:Partner

---

# ブルーコニック

> [BlueConic][1]、主要な純粋なカスタマーデータプラットフォームは、企業のファーストパーティデータを異なるシステムから解放し、顧客関係を変革し、ビジネスの成長を促進するために必要な場所と時間にアクセスできるようにします。 

BrazeとBlueConicの統合により、ユーザーは永続的な個別プロファイル全体でデータを統合し、Amazon Web Services S3サーバーを介してインポート目標のために2つのシステム間で同期することができます。潜在的な目標には、成長に焦点を当てたイニシアチブ、顧客ライフサイクルのオーケストレーション、モデリングと分析、デジタル製品と体験、オーディエンスベースの収益化などが含まれます。この統合は、スケジュールされたバッチインポートとエクスポートの両方をサポートしています。 

{% alert important %}
統合を使用する場合、BlueConicは各同期でデルタ（変更データ）を送信します。これには、前回の送信以降に変更されたプロファイルおよびそのプロファイルのすべての属性が含まれます。データポイントの使用状況を監視します。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| --- | --- |
| BlueConicアカウント | このパートナーシップを利用するには、[BlueConicアカウント][1]が必要です。プラグインにアクセスするには、BlueConicアカウント内の[接続の表示と編集][4]へのアクセスが必要です。 |
| Braze REST API キー | `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists`, および `segments.details` の権限を持つ Braze REST API キー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | あなたのRESTエンドポイントURL。エンドポイントは、[インスタンスのBraze URL][2]に依存します。 |
| S3認証 | データをエクスポートおよびインポートするには、Amazon Web Services (S3) サーバーへのアクセスが必要です。 |
| アクセスキーID<br>シークレットアクセスキー | アクセスキーIDとシークレットアクセスキーは、インポートおよびエクスポートのためにS3サーバーを認証することを可能にします。 |
| AWSバケット | プラグイン内でS3に接続する必要があります。認証後、利用可能なバケットがドロップダウンメニューに表示されます。これは、インポートまたはエクスポートされるファイルが保存される場所です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 統合

### ステップ1:Braze接続の作成

BlueConic で、ナビゲーションバーから **接続** を選択し、次に **接続を追加** を選択します。表示されるプロンプトで、**Braze**を検索し、**Braze connection**を選択します。 

接続の使用可能なメタデータフィールドを展開または折りたたむには、灰色のシェブロンアイコンをクリックします。これらのフィールド内で、この接続をお気に入りにしたり、接続に名前を付けたり、ラベルを追加したり、説明を含めたり、接続が[実行されるか実行に失敗した場合に][5]メール通知を受け取るように選択したりできます。 

設定を保存します。

### ステップ2:Braze接続の構成

BlueConicとBrazeの接続を構成するには、Brazeアカウントの認証情報とAmazon Web Services (S3)アカウント情報を追加して接続を認証する必要があります。 

1. BlueConic で、左側のパネルの **セットアップ** セクションで **セットアップと実行** を選択します。<br><br>
2. Braze認証ページが開いたら、Braze REST APIエンドポイントとBraze APIキーを入力します。<br>
![\]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. S3のセットアップと認証セクションで、次の資格情報を入力します:Amazon Web Services（S3）アクセスキーID、シークレットアクセスキー、およびS3バケット。それらは、BrazeとAmazon S3の統合を設定する際に構成した[同じ資格情報]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/)である必要があります。設定を保存します。<br>![\]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### ステップ3:インポートまたはエクスポートの目標を作成する（インポートマッピング）

認証が完了したら、少なくとも1つのインポートまたはエクスポート目標を作成し、接続をオンにして、接続をスケジュールまたは実行する必要があります。

{% tabs %}
{% tab Import %}

1. 左側のパネルで**BlueConicにデータをインポート**を選択して、Brazeデータ構成ページを開きます。<br><br>
2. Brazeでデータの場所を選択します。ここで、Brazeオーディエンスを選択して、インポートするデータの場所をBlueConicに指定できます。<br>![The BlueConic Braze audience set as "BlueConic Test Users".]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BrazeとBlueConicの間で識別子をマッピングします。<br>![The Braze field "External ID" set to map to the BlueConic "Braze external ID" field.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> 2つのシステム間で顧客データをリンクするには、1つ以上の顧客識別子を入力します。<br>**Allow creation...** チェックボックスを使用して、既存のBlueConicプロファイルと一致しないデータの新しいプロファイルをBlueConicに作成させることができます。<br><br>
4. 次に、エクスポートするBlueConicデータフィールドをBrazeフィールドに一致させます。ドロップダウンフィールドを使用して、左側のBlueConicプロファイル識別子またはプロファイルプロパティのいずれかを選択し、対応するBrazeプロファイル識別子を選択します。次に、ドロップダウンメニューを使用して、インポートされたコンテンツを既存の値にどのように追加するかを指定します: 追加、合計、プロファイルプロパティが空の場合にのみ設定、またはクリアに設定（Brazeフィールドが空の場合）。<br>![\]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>「**マッピングの追加**」ボタンを使用して、必要に応じて追加のマッピング行を作成します。残りのフィールドを追加するオプション**を使用して、複数のマッピング行を追加できます。**BlueConicは残りのBrazeフィールドを検出し、それらをBlueConicプロファイルプロパティと一致させます。インポートのマージ戦略（セット、追加、合計、空の場合にセット、またはクリア）を設定し、BlueConicプロファイルプロパティの名前にカスタムプレフィックスを提供できます。<br><br>
5. 最後に、接続を開始するには**接続を実行**を選択します。[BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) にアクセスして、接続のスケジュールと実行について詳しく学んでください。
{% endtab %}
{% tab Export %}

1. 左側のパネルで**BlueConicからBrazeへのデータエクスポートを設定するには、データをエクスポート**を選択します。<br><br>
2. エクスポートするBlueConicセグメントを選択してください。Brazeで一致する識別子を持つこのセグメントのプロファイルのみがエクスポートされます。<br>![A BlueConic segment of 20k profiles.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BlueConicプロファイルとBrazeフィールドの間で識別子をリンクします。一致するものが見つからない場合は、BlueConicに新しいレコードを作成させることもできます。<br>![The Braze field "External ID" set to map to the BlueConic "Braze external ID" field.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. 次に、エクスポートするBlueConicデータフィールドをBrazeフィールドに一致させます。BlueConicアイコンからドロップダウンメニューを使用して、エクスポートしたい[情報](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals)の種類を選択します。利用可能な情報には、プロファイルプロパティ、BlueConicプロファイル識別子、関連セグメント、すべての表示されたインタラクション、権限レベル、および静的テキスト値が含まれます。<br>![\]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. 最後に、接続を開始するには**接続を実行**をクリックします。[BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) にアクセスして、接続のスケジュールと実行について詳しく学んでください。
{% endtab %}
{% endtabs %}

## ステップ 4:接続を切り替える

Braze接続タイトルの横にあるトグルを使用して、接続をオンおよびオフに切り替えます。スケジュールされた時間に実行するには、接続がオンになっている必要があります。 

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ