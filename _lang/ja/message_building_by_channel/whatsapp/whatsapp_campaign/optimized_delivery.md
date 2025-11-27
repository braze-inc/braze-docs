---
nav_title: 配信を最適化した WhatsApp メッセージ
article_title: 配信を最適化した WhatsApp メッセージ
page_order: 1
description: "この参考記事では、WhatsAppメッセージを最適化して作成するためのステップを紹介する。"
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# 配信を最適化した WhatsApp メッセージ

> ダイナミックなエンゲージメントベースの配信でWhatsAppの適切なユーザー群にリーチし、配信力とエンゲージメントを高める。

最適化された配信を行うWhatsAppメッセージは、ダイナミックなエンゲージメントベースの配信を提供するMetaの[Marketing Messages API for WhatsApp（MM](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp)API for WhatsApp）を使用して送信される。つまり、エンゲージメントの高いメッセージ（例えば、読まれやすく、クリックされやすいメッセージ）は、エンゲージメントの高いユーザーにより多く届くことになる。WhatsAppでは、期待され、関連性があり、タイムリーなメッセージはエンゲージメントが高いと判断され、読まれたりクリックされたりする可能性が高くなる。 

ブランドはMM API for WhatsAppを利用することで、Cloud APIと同等以上の配信性を期待できる。Metaによると、インドでは、エンゲージメントの高いマーケティングメッセージは、クラウドAPIと比較して最大9％多く配信された。なお、WhatsAppのMM APIは100％の配信性を保証するものではない。

### 地域の空室状況

最適化された配信の可用性と最適化能力は、ビジネス電話番号の地域とユーザーに依存する。詳しくは、「[地理的な機能の利用可能性](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features)」を参照のこと。 

## 最適化された配信の設定

1. Brazeで、**Partner Integrations**>**Technology Partners**> WhatsAppに進む。
2. **最適化された配信で送信を最適化する**」のセクションで、[埋め込みサインアップワークフローを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)トリガーする**アップグレード**設定を選択する。

![WhatsApp メッセージの統合セクションには、最適化された配信で送信を最適化するオプションがある。]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\.最適化配信を有効にすると、**WhatsAppビジネスアカウント**マネージャーのアカウント詳細に最適化配信ステータスが表示される。

![WhatsAppビジネスアカウント管理セクションに表示されるサブスクリプショングループのステータスが「アクティブ」になっている。]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

または、WhatsAppマネージャーで直接最適化配信をイネーブルメントにしてから、Brazeで送信を開始することもできる。

### セットアップのトラブルシューティング

- **一般的なエラーだ：**アップグレード中に何か問題が発生した場合、このエラーバナーが表示され、[サポートに連絡]({{site.baseurl}}/braze_support/)するようアドバイスされる。
- **不適格エラー：**Metaによって制限されている場合、このエラーバナーが表示される：「WhatsAppビジネスアカウントの少なくとも1つがMetaによって制限されている。アップグレードするには、アカウントが良好な状態でなければならない。この問題が解決しない限り、これを否定することはできない。

## キャンペーンとキャンバスで最適化された配信を使用する

最適化された配信は**マーケティングメッセージに**使われるべきである。Brazeは、**ユーティリティ、認証、サービス、レスポンスメッセージの**最適化された配信オプションを自動的に削除する。 

### 配送方法を選択する

1. キャンペーンまたはキャンバスメッセージのステップのBraze WhatsApp作成画面で、**設定**タブに移動する。
2. **WhatsApp**ビジネスアカウント(WABA)がイネーブルメントになっている場合、「**最適化配信(推奨)」**チェックボックスがデフォルトでチェックされる。特定のメッセージに最適化配信を使用したくない場合は、チェックボックスをオフにする。
- 最適化された配信を選択してもそれが利用できない場合、メッセージは自動的にCloud APIメソッドにフォールバックする。

![メッセージ作成画面にはプレビュータブがあり、最適化された配信を選択するチェックボックスがある。]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### 他のBrazeチャネルでユーザーをリターゲティングする。 

WhatsAppのMM APIは100%の配信率を提供しないため、他のチャネルでメッセージを受け取っていないユーザーをリターゲティングする方法を理解することが重要である。 

ユーザーをリターゲティングするには、特定のメッセージを受け取らなかったユーザーのセグメントを構築することをお勧めする。この場合、エラーコード`131049` でフィルターをかける。このエラーコードは、WhatsAppのユーザーごとのマーケティングテンプレート制限により、マーケティングテンプレートメッセージが送信されなかったことを示す。Braze CurrentsまたはSQLセグメントエクステンションを使用することで、これを行うことができる：

- **Braze CurrentsBraze Currentsを使用してメッセージ障害イベントをエクスポートする。その後、このデータを使ってユーザープロファイルのカスタム属性（`whatsapp_failed_last_msg: true` など）を更新し、リターゲティングキャンペーンのフィルターとして使うことができる。
- SQL セグメントエクステンションこの機能にアクセスできるのであれば、SQLを使ってメッセージ失敗ログを照会し、それらのユーザーのセグメンテーションを作成し、そのセグメンテーションを別のチャネルでターゲットにすることができる。
