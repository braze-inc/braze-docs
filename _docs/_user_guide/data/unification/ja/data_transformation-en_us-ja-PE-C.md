---
nav_title: データ変換
article_title: データ変換
page_order: 0.3
layout: dev_guide
guide_top_header: "データ変換"
guide_top_text: "Braze Data Transformation を使用すると、Webhook 連携の構築および管理を行って、外部プラットフォームから Braze へのデータフローを自動化できます。この新しく統合されたユーザーデータにより、さらに洗練されたマーケティングユースケースを強化できます。Braze Data Transformation では、コーディングの経験がほとんどなくても迅速にデータ統合ができ、また手動 API 呼び出し、サードパーティの統合ツール、さらに顧客データプラットフォームへの依存からチームが脱却するうえで役立ちます。"
page_type: landing
description: "このランディングページには、データ変換やユースケースの使用方法など、Braze Data Transformation に関する記事がまとめられています。"
alias: /data_transformation/

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: 変換の作成
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation/
    image: /assets/img/braze_icons/flip-forward.svg
  - name: ユースケース
    link: /docs/user_guide/data/unification/data_transformation/use_cases/
    image: /assets/img/braze_icons/users-01.svg
---

## 仕組み

最近のプラットフォームの多くは、「Webhook」、つまり新しいイベントや新しいデータに関する情報をあるプラットフォームから別のプラットフォームに送信するためのリアルタイム API 通知を装備しています。Data Transformation は以下のものを提供します。

* このような Webhook を受信するための Braze URL アドレス。
* Webhook ペイロードを JavaScript コードで変換して、Braze の `/users/track` や `/catalogs` など、さまざまな Braze API エンドポイントへの有効なリクエストを作成する機能。例えば、送信先が `/users/track` の場合は、Webhook からどの情報を使用するか、また Braze ユーザープロファイルのユーザー属性、イベント、または購入としてデータをどのように表現するかを選択できます。
* 品質保証、トラブルシューティング、および変換のパフォーマンスの監視を実行するためログ記録。

最終的には、選択したソースプラットフォームの Webhook を Braze 更新に送ることで、そのソースプラットフォームを接続する Webhook 連携が実現します。

{% details More on webhooks %}
Webhook は、HTTP POST リクエストを介して特定の宛先に送信されるリアルタイム通知です。Webhook は、あるポイントから別のポイントへのデータ送信によく使用されます。Webhook は、発生したアクションとそのアクションに誰が関与したかに関するデータを渡すことができます。

例えば、調査プラットフォームは、オンラインフォームにアンケート回答を受信するたびに、選択した宛先に Webhook を送信できます。また、カスタマーサービスプラットフォームは、カスタマーサービスチケットが作成されるたびに、選択した宛先に Webhook を送信できます。
{% enddetails %}

## Data Transformation のバージョン

次の表で、Data Transformation の無料バージョンとプロバージョンの違いを説明します。

| エリア | 無料版 | Data Transformation Pro |
|----|----|----|
| アクティブ変換 | 1 社につき最大 5 個 | 1 社につき最大 55 個 |
| 月あたり | リクエスト 30 万件 / 月 | 月に10,300,000件のリクエストが届きます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Data Transformation Pro へのアップグレードを依頼するには、Braze アカウントマネージャーに問い合わせるか、Braze ダッシュボードの **[アップグレードをリクエスト]** ボタンを選択してください。
{% endalert %}

### レート制限

Braze Data Transformation のレート制限は、ワークスペースあたりリクエスト1,000 件 / 分です。Data Transformation Pro を使用していて、レート制限を上げる必要がある場合は、Braze アカウントマネージャーにお問い合わせください。

## よくある質問

### Braze Data Transformation では何が同期されますか?

外部プラットフォームが Webhook に入れて利用可能にしたデータはすべて、 Braze に同期できます。外部プラットフォームが Webhook 経由で送信するデータの種類が増えるほど、同期するデータを選択するためのオプションが増えます。

### 私はマーケターです。Braze Data Transformation を使用するには開発者のリソースが必要ですか?

開発者にもこの機能を使用していただきたいと考えていますが、Braze Data Transformation を使用する人が開発者である必要はありません。マーケターは、開発者のリソースがなくても変換を正常に設定できます。

### 外部プラットフォームが識別子としてメール アドレスまたは電話番号のみを提供する場合でも、Braze Data Transformation を使用できますか?

はい。[メールアドレスまたは電話番号を識別子として]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address)使用して、変換により `/users/track` エンドポイントを更新できます。

変換コード内の識別子プロパティとして、`external_id` または `braze_id` の代わりに `email` または `phone` を使用することで機能します。[変換コード]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code)の例では この機能が使用されています。

{% alert note %}
2023 年 4 月より前に Braze Data Transformation の使用を開始した早期アクセスユーザーは、このユースケースに役立つ `get_user_by_email` 関数を知っているかもしれませんが、その関数は廃止されました。
{% endalert %}

### Braze Data Transformationはデータポイントを記録するか？

ほとんどの場合はそうだ。Braze Data Transformation は最終的に、必要な属性、イベント、および購入を書き込む `/users/track` 呼び出しを作成します。これらは、`/users/track` の通話が独立系で行われた場合と同じように、データポイントを記録する。変換の書き方によって、ログに記録されるデータポイントの数をコントロールすることができる。

### ユースケースの設定や変換コードのサポートを受けるにはどうすればよいですか?

追加のサポートが必要な場合は、Braze アカウントマネージャーにお問い合わせください。
