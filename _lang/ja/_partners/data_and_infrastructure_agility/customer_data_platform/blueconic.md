---
nav_title: ブルーコニック
article_title: ブルーコニック
description: "この参考記事では、Brazeとピュアプレイの大手顧客データプラットフォームであるBlueConicのパートナーシップについて概説しており、永続的な個々のプロファイル間でデータを統一し、Amazon Web ServicesのS3サーバー経由でインポート目標のために2つのシステム間で同期することができる。"
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# ブルーコニック

> [BlueConicは][1]、ピュアプレイ顧客データプラットフォームのリーディングカンパニーであり、企業のファーストパーティデータを異種システムから解放し、いつでもどこでも必要なときにアクセスできるようにすることで、顧客との関係を変革し、ビジネスの成長を促進する。 

BrazeとBlueConicの統合により、ユーザーは永続的な個々のプロファイル間でデータを統一し、Amazon Web ServicesのS3サーバーを経由してインポート目標のために2つのシステム間で同期することができる。想定される目標には、成長に焦点を当てた取り組み、顧客ライフサイクルのオーケストレーション、モデリングと分析、デジタル製品と体験、視聴者ベースの収益化などが含まれる。この統合は、スケジュールされたバッチインポートとエクスポートの両方をサポートしている。 

{% alert important %}
インテグレーションを使用する場合、BlueConicは同期ごとにデルタ（変化するデータ）を送信する。これには、前回の送信以降に変更されたプロファイルと、そのプロファイルのすべての属性が含まれる。データポイントの使用状況を適宜監視する。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| ブルーコニックのアカウント | このパートナーシップを利用するには、[ブルーコニックのアカウントが][1]必要である。プラグインにアクセスするには、BlueConicアカウント内で[接続を表示および編集][4]するためのアクセス権が必要である。 |
| Braze REST API キー | `users.track` 、`users.export.segment` 、`campaigns.list` 、`campaigns.details` 、`segments.lists` 、`segments.details` のパーミッションを持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][2]依存する。 |
| S3認証 | データのエクスポートとインポートには、Amazon Web Services（S3）サーバーへのアクセスが必要だ。 |
| アクセスキーID<br>秘密のアクセス・キー | アクセスキーIDとシークレットアクセスキーによって、インポートやエクスポートを行うS3サーバーを認証することができる。 |
| AWSバケット | プラグイン内でS3に接続する必要がある。認証後、利用可能なバケツがドロップダウンメニューに表示される。ここには、インポートまたはエクスポートされるファイルが保存される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 統合

### ステップ1:ブレイズコネクションを作る

BlueConicのナビゲーション・バーで**「Connections」を**選択し、「**Add Connection」を**選択する。表示されたプロンプトで**Brazeを**検索し、**Braze connectionを**選択する。 

グレーのシェブロンアイコンをクリックして、接続で使用可能なメタデータフィールドを展開または折りたたむ。これらのフィールドでは、この接続をお気に入りに登録したり、接続に名前をつけたり、ラベルを追加したり、説明を含めたり、接続が[実行されたり実行されなかったりした][5]場合にEメールで通知を受け取るかどうかを選択したりすることができる。 

設定を保存する。

### ステップ2:Braze接続を設定する

BlueConicとBraze間の接続を設定するには、接続を認証するためにBrazeのアカウント認証情報とAmazon Web Services（S3）のアカウント情報を追加する必要がある。 

1. BlueConicでは、左パネルの**Setup**セクションで**Set up and runを**選択する。<br><br>
2. 開いたBraze認証ページで、Braze REST APIエンドポイントとBraze APIキーを入力する。<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. S3 setup and authenticationセクションで、これらの認証情報を入力する：Amazon Web Services（S3）のアクセスキーID、シークレットアクセスキー、S3バケット。これらは、BrazeとAmazon S3の統合を設定するときに設定した[のと同じ認証情報]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/)である必要がある。設定を保存する。<br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### ステップ 3:インポートゴールまたはエクスポートゴールを作成する（インポートマッピング）

認証が完了したら、少なくとも1つのインポートまたはエクスポートゴールを作成し、接続をオンにし、接続をスケジュールまたは実行する必要がある。

{% tabs %}
{% tab 輸入 %}

1. 左のパネルで**Import data into BlueConicを**選択し、Brazeのデータ設定ページを開く。<br><br>
2. Brazeのデータの場所を選択する。ここで、Brazeのオーディエンスを選択することで、インポートするデータの場所をBlueConicに伝えることができる。<br>![BlueConic Brazeの視聴者を「BlueConicテストユーザー」に設定した。]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BrazeとBlueConicの間で識別子をマッピングする。<br>![Brazeのフィールド「外部ID」は、BlueConicの「Braze外部ID」フィールドにマッピングするように設定されている。]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> 2つのシステム間で顧客データをリンクさせるには、1つ以上の顧客識別子を入力する。<br>既存のBlueConicプロファイルに一致しないデータについて、BlueConicが新しいプロファイルを作成することを許可するには、**「作成を許可...」**チェックボックスを使用する。<br><br>
4. 次に、エクスポートするBlueConicのデータフィールドをBrazeのフィールドに合わせる。ドロップダウンフィールドを使用して、左側のBlueConicプロファイル識別子またはプロファイルプロパティのいずれかを選択し、対応するBrazeプロファイル識別子を選択する。次に、ドロップダウンメニューを使用して、インポートしたコンテンツを既存の値に追加する方法を指定する：追加、合計、プロファイル・プロパティが空の場合のみ設定、またはクリアに設定（Brazeフィールドが空の場合）。<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>**Add Mapping**ボタンを使って、必要に応じてマッピング行を追加作成する。**Add remaining fields**オプションで複数のマッピング行を追加できる。BlueConicは残りのBrazeフィールドを検出し、BlueConicプロファイル・プロパティと照合する。インポートのマージ戦略（set、add、sum、set if empty、clear）を設定し、BlueConicプロファイル・プロパティの名前にカスタム接頭辞を指定できる。<br><br>
5. 最後に、**Run the connectionを**選択して接続を開始する。接続のスケジューリングと実行については、[BlueConicを](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)ご覧いただきたい。
{% endtab %}
{% tab 輸出 %}

1. 左のパネルで**Export data to Brazeを**選択し、BlueConicからBrazeへのデータエクスポートを設定する。<br><br>
2. エクスポートするBlueConicセグメントを選択する。このセグメントで、Brazeの識別子が一致するプロファイルだけがエクスポートされる。<br>![ブルーコニックの2万プロファイルのセグメント。]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BlueConicプロファイルとBrazeフィールド間の識別子をリンクさせる。オプションで、一致するレコードがない場合、BlueConicに新しいレコードを作成させることもできる。<br>![Brazeのフィールド「外部ID」は、BlueConicの「Braze外部ID」フィールドにマッピングするように設定されている。]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. 次に、エクスポートするBlueConicのデータフィールドをBrazeのフィールドに合わせる。BlueConicのアイコンからドロップダウンメニューを使って、エクスポートしたい[情報の](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals)種類を選択する。利用可能な情報には、プロファイルプロパティ、BlueConicプロファイル識別子、関連セグメント、閲覧されたすべてのインタラクション、パーミッションレベル、静的テキスト値が含まれる。<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. 最後に、**Run the connectionを**クリックして接続を開始する。接続のスケジューリングと実行については、[BlueConicを](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)ご覧いただきたい。
{% endtab %}
{% endtabs %}

## ステップ4:接続をオンに切り替える

Braze接続のタイトルの横にあるトグルを使って、接続のオンとオフを切り替える。スケジュールされた時間帯に実行するには、接続がオンになっていなければならない。 

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ