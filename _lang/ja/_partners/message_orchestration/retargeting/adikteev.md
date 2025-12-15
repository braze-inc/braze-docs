---
nav_title: Adikteev
article_title: Adikteev 解約予測
description: "この参考記事では、Brazeと、解約予測とフルサービスのアプリリターゲティングを組み合わせたユーザーリテンションエンジンであるAdikteevの提携について概説している。"
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev 解約予測

> [Adikteev](https://www.adikteev.com/churn-prediction) は、解約予測とサービス全般を取り扱うアプリリターゲティングを組み合わせたユーザーリテンションエンジンです。

_この統合は Adikteev によって管理されます。_

## 統合について

Braze と Adikteev の統合により、Braze CRM キャンペーン内で Adikteev の解約予測技術を活用し、リスクの高いユーザーセグメントを優先的にターゲットにすることで、ユーザーリテンションを高めることができます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| Adikteev アカウント | このパートナーシップを活用するには、Adikteev アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定**」>「**APIと識別子**」から作成できる。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

{% tabs %}
{% tab Audience filtering %}
解約リスクに基づいてオーディエンスセグメントを絞り込みます。<br> Adikteev により送信されるカスタム属性の名前と値は設定可能です。

![Adikteevから送信されたカスタム属性をオーディエンスセグメントのフィルターとして使用する方法の例を示すスクリーンショット。]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Message targeting %}
受信者の解約リスクに基づいてBrazeメッセージングキャンペーンをカスタマイズ。

![Adikteevから送信されたカスタム属性をキャンペーンターゲティングフィルターとして使用する例を示すスクリーンショット。]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## 統合

### ステップ1:アプリのイベントストリームを共有する

アプリオーディエンスの解約予測を開始するには、Adikteev でモバイル計測プラットフォームからのイベントのポストバックをオンにする必要があります。これは、[Adikteev サポート Web サイト](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation)のガイドラインに従って設定してください。

### ステップ2:Braze REST APIキーを作成する

Braze で [**設定**] > [**API と識別子**] に移動します。[**新しい API キーを作成**] を選択して使用する API キー名を入力し、次の権限が追加されていることを確認します。

- `users.track`

### ステップ3:Adikteev チームに情報を提供する

統合を完了するには、REST API キーと REST エンドポイント URL を Adikteev アカウントマネージャーに提供する必要があります。Adikteevは接続を確立し、セットアップ完了後、統合を確認するためにあなたに連絡する。

## バッチ処理とレート制限

`user.track` エンドポイントは、ユーザーの詳細を更新するために使用されます。エンドポイントのレート制限、リクエストのバッチ処理、リクエストの詳細については、[API のドキュメント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を参照してください。

{% alert tip %}
API 呼び出しの総数を削減するため、変更されたデータを更新する目的でのみ API 呼び出しを実行すべきであることを覚えておいてください。つまり、解約セグメントが変更されたユーザーだけを更新してください。
{% endalert %}

## ユーザーとデバイスの識別子

Braze のユーザープロファイルは、任意のタイプのユーザーまたはデバイス識別子に関連付けることができます。使用できるオプションのリストは、データ収集を Braze とどのように統合したかに応じて異なります。Adikteev では、解約セグメント情報を正しく送信するために、MMP と Braze のユーザープロファイルの間で共通の識別子を見つける必要があります。

## データの保持と削除

更新が行われない場合、属性とその値はBrazeユーザープロファイルに無期限に保持される。

プロファイル属性を削除するには、`null` に設定する。

## リクエストペイロード

Adikteev から Braze に送信されるペイロードはカスタマイズ可能であり、顧客のニーズに合わせて設定できます。これには、使用する識別子、カスタム属性の名前、Adikteev が Braze で新しいユーザーを作成できるかまたは既存のユーザーを更新するだけかを設定することが含まれます。


## サポートとトラブルシューティング

統合に関するご質問や、ユースケースに関するサポートについては、Adikteev アカウントマネージャーにお問い合わせください。

