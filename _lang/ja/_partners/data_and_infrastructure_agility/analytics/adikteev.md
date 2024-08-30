---
nav_title: アディクテフ
article_title: アディクテフ解約予測
description: "この参考記事では、Brazeと、解約予測とフルサービスのアプリリターゲティングを組み合わせたユーザーリテンションエンジンであるAdikteevの提携について概説している。"
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# アディクテフ解約予測

> [Adikteevは](https://www.adikteev.com/churn-prediction)、解約予測とフルサービスのアプリリターゲティングを組み合わせたユーザーリテンションエンジンである。

BrazeとAdikteevの統合により、Braze CRMキャンペーン内でAdikteevの解約予測技術を活用し、リスクの高いユーザーセグメントを優先的にターゲットにすることで、ユーザーリテンションを高めることができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| アディクテフのアカウント | このパートナーシップを利用するには、アディクティーフのアカウントが必要だ。 |
| Braze REST API キー | パーミッションを持つBraze REST APIキー`users.track` 。<br><br> これは、Brazeダッシュボードの**「設定**」>「**APIと識別子**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

{% tabs %}
{% tab 観客のフィルタリング %}
解約リスクに基づいて視聴者セグメントを絞り込む。<br> アディクテフから送信されるカスタム属性の名前と値は設定可能である。

![] （{% image_buster /assets/img/adikteev/audience.png %} ）。
{% endtab %}
{% tab メッセージ・ターゲティング %}
受信者の解約リスクに基づいてBrazeメッセージングキャンペーンをカスタマイズ。

![] （{% image_buster /assets/img/adikteev/campaign.png %} ）。
{% endtab %}
{% endtabs %}

## 統合

### ステップ1:アプリのイベントストリームを共有する

アプリ利用者の解約予測を開始するには、Adikteevがモバイル測定プラットフォームからイベントのポストバックをオンにする必要がある。[アディクティーフのサポートサイトの](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation)ガイドラインに従って設定する。

### ステップ2:Braze REST APIキーを作成する

Brazeで、**Settings**>**APIs and Identifiersに**移動する。**Create New API Keyを**選択し、任意のAPI Key Nameを入力し、以下のパーミッションが追加されていることを確認する：

- `users.track`

### ステップ3:アディクテフ・チームに情報を提供する

統合を完了するには、REST APIキーとRESTエンドポイントURLをAdikteevアカウントマネージャーに提供する必要がある。Adikteevは接続を確立し、セットアップ完了後、統合を確認するためにあなたに連絡する。

## バッチ処理とレート制限

`user.track` エンドポイントは、ユーザーの詳細を更新するために使用される。エンドポイントのレート制限、リクエストのバッチ処理、リクエストの詳細については、[APIのドキュメントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)参照のこと。

{% alert tip %}
APIコールは、全体的なAPIコールの回数を減らすために、変更されたデータを更新するためだけに行うべきであることを覚えておいてほしい。言い換えれば、解約セグメントが変更されたユーザーだけを更新する。
{% endalert %}

## ユーザーとデバイスの識別子

Brazeのユーザープロファイルは、あらゆるタイプのユーザーまたはデバイス識別子に関連付けることができる。Adikteevの場合、解約セグメント情報を正しく送信するために、MMPとBrazeのユーザープロファイルの間で共通の識別子を見つける必要がある。

## データの保持と削除

更新が行われない場合、属性とその値はBrazeユーザープロファイルに無期限に保持される。

プロファイル属性を削除するには、`null` に設定する。

## リクエスト・ペイロード

アディクテフからブレイズに送られるペイロードはカスタマイズ可能で、顧客のニーズに合わせて設定できる。これには、使用される識別子、カスタム属性の名前、AdikteevがBrazeで新しいユーザーを作成できるか、既存のユーザーを更新するだけかを設定することが含まれる。


## サポートとトラブルシューティング

統合に関するご質問や、ユースケースに関するサポートについては、Adikteevのアカウントマネージャーにお問い合わせいただきたい。
