---
nav_title: BlueConic
article_title: BlueConic
description: "このリファレンス記事では、Braze と BlueConic のパートナーシップについて説明します。BlueConic は、業界をリードするピュアプレイ顧客データプラットフォームであり、永続的な個々のプロファイル間でデータを統合し、Amazon Web Services S3 サーバーを介してインポート目標のために2つのシステム間でデータを同期することができます。"
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/) は業界をリードするピュアプレイ顧客データプラットフォームであり、異種システムから企業のファーストパーティデータを解放し、顧客との関係を変えビジネスの成長を促進するために必要であれば、いつでもどこからでもこのデータにアクセスできるようにします。 

_この統合は Blueconic によって管理されます。_

## 統合について

BrazeとBlueConicの統合により、ユーザーは永続的な個々のプロファイル間でデータを統一し、Amazon Web ServicesのS3サーバーを経由してインポート目標のために2つのシステム間で同期することができる。想定される目標には、成長に焦点を当てた取り組み、顧客ライフサイクルのオーケストレーション、モデリングと分析、デジタル製品と体験、視聴者ベースの収益化などが含まれる。この統合は、スケジュールされたバッチインポートとエクスポートの両方をサポートしている。 

{% alert important %}
インテグレーションを使用する場合、BlueConicは同期ごとにデルタ（変化するデータ）を送信する。これには、前回の送信以降に変更されたプロファイルと、そのプロファイルのすべての属性が含まれる。データポイントの使用状況を適宜監視する。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| BlueConic アカウント | このパートナーシップを活用するには、[BlueConic アカウント](https://www.blueconic.com/)が必要です。プラグインにアクセスするには、BlueConicアカウント内で[接続を表示および編集](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles)するためのアクセス権が必要である。 |
| Braze REST API キー | `users.track`、`users.export.segment`、`campaigns.list`、`campaigns.details`、`segments.lists`、`segments.details` の権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントは、[BrazeインスタンスのURL](https://portal.aws.amazon.com/billing/signup#/start)によって異なります。 |
| S3認証 | データのエクスポートとインポートには、Amazon Web Services（S3）サーバーへのアクセスが必要だ。 |
| アクセスキーID<br>シークレットアクセスキー | アクセスキー ID とシークレットアクセスキーを使用して、インポートとエクスポートのために S3 サーバーを認証できます。 |
| AWSバケット | プラグイン内で S3 に接続する必要があります。認証後に、利用可能なバケットがドロップダウンメニューに表示されます。ここには、インポートまたはエクスポートされるファイルが保存される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:Braze 接続を作成する

BlueConic のナビゲーションバーで [**Connections**] を選択し、次に [**Add Connection**] を選択します。表示されるプロンプトで、**Braze** を検索し、[**Braze connection**] を選択します。 

グレーの山形記号アイコンをクリックして、接続の使用可能なメタデータフィールドを展開または折りたたみます。これらのフィールドでは、お気に入りへのこの接続の追加、接続の名前の指定、ラベルの追加、説明の追加、および接続が[実行されているか、実行できていないか](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ)に関するメール通知を受信するかどうかの選択を行うことができます。 

設定を保存する。

### ステップ2:Braze接続を設定する

BlueConicとBraze間の接続を設定するには、接続を認証するためにBrazeのアカウント認証情報とAmazon Web Services（S3）のアカウント情報を追加する必要がある。 

1. BlueConic の左パネルの [**Set up**] セクションで [**Set up and run**] を選択します。<br><br>
2. 開いたBraze認証ページで、Braze REST APIエンドポイントとBraze APIキーを入力する。<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. S3 の設定と認証のセクションで、次の認証情報を入力します。Amazon Web Services（S3）のアクセスキーID、シークレットアクセスキー、S3バケット。これらは、BrazeとAmazon S3の統合を設定するときに設定した[のと同じ認証情報]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)である必要がある。設定を保存する。<br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### ステップ3:インポートゴールまたはエクスポートゴールを作成する（インポートマッピング）

認証が完了したら、少なくとも1つのインポートまたはエクスポートゴールを作成し、接続をオンにし、接続をスケジュールまたは実行する必要がある。

{% tabs %}
{% tab インポート %}

1. 左パネルで [**Import data into BlueConic**] を選択し、Braze データ設定ページを開きます。<br><br>
2. Brazeのデータの場所を選択する。ここで、Brazeのオーディエンスを選択することで、インポートするデータの場所をBlueConicに伝えることができる。<br>![「Blue Conic Test Users」に設定されている BlueConic Braze オーディエンス。]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BrazeとBlueConicの間で識別子をマッピングする。<br>![Braze のフィールド「external ID」が、BlueConic の「Braze external ID」フィールドにマッピングするように設定されている。]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> 2つのシステム間で顧客データをリンクさせるには、1つ以上の顧客識別子を入力します。<br>既存のBlueConicプロファイルに一致しないデータについて、BlueConicが新しいプロファイルを作成することを許可するには、**「作成を許可...」**チェックボックスを使用する。<br><br>
4. 次に、エクスポートするBlueConicのデータフィールドをBrazeのフィールドに合わせる。ドロップダウンフィールドを使用して、左側のBlueConicプロファイル識別子またはプロファイルプロパティのいずれかを選択し、対応するBrazeプロファイル識別子を選択する。次に、ドロップダウンメニューを使用して、インポートしたコンテンツを既存の値に追加する方法を指定する：追加、合計、プロファイル・プロパティが空の場合のみ設定、またはクリアに設定（Brazeフィールドが空の場合）。<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>**Add Mapping**ボタンを使って、必要に応じてマッピング行を追加作成する。**Add remaining fields**オプションで複数のマッピング行を追加できる。BlueConicは残りのBrazeフィールドを検出し、BlueConicプロファイル・プロパティと照合する。インポートのマージ戦略（set、add、sum、set if empty、clear）を設定し、BlueConicプロファイル・プロパティの名前にカスタム接頭辞を指定できる。<br><br>
5. 最後に、**Run the connectionを**選択して接続を開始する。接続のスケジューリングと実行については、[BlueConicを](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)ご覧いただきたい。
{% endtab %}
{% tab エクスポート %}

1. 左パネルで [**Export data to Braze**] を選択し、BlueConic から Braze へのデータエクスポートを設定します。<br><br>
2. エクスポートするBlueConicセグメントを選択する。このセグメントで、Braze で一致する識別子を持つプロファイルのみがエクスポートされます。<br>![2万件のプロファイルからなる BlueConic セグメント。]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BlueConicプロファイルとBrazeフィールド間の識別子をリンクさせる。オプションで、一致するレコードがない場合、BlueConicに新しいレコードを作成させることもできる。<br>![Braze のフィールド「external ID」が、BlueConic の「Braze external ID」フィールドにマッピングするように設定されている。]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. 次に、エクスポートするBlueConicのデータフィールドをBrazeのフィールドに合わせる。BlueConic アイコンのドロップダウンメニューを使用して、エクスポートする[情報](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals)のタイプを選択します。利用可能な情報には、プロファイルプロパティ、BlueConicプロファイル識別子、関連セグメント、閲覧されたすべてのインタラクション、パーミッションレベル、静的テキスト値が含まれる。<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. 最後に [**Run the connection**] をクリックして接続を開始します。接続のスケジューリングと実行については、[BlueConicを](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)ご覧いただきたい。
{% endtab %}
{% endtabs %}

## ステップ4:接続をオンに切り替える

Braze接続のタイトルの横にあるトグルを使って、接続のオンとオフを切り替える。スケジュールされた時間に実行するには、接続がオンになっている必要があります。 


