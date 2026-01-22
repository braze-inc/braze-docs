---
nav_title: Smartling
article_title: Smartling
description: "このリファレンス記事では、Braze と Smartling のパートナーシップについて説明します。Smartling はクラウドベースのローカライゼーションソフトウェアです。Braze Connectorは、HTMLメールテンプレート、コンテンツブロック、キャンバス、キャンペーンメールメッセージの翻訳をサポート。"
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) は、Web サイト s、アプリライセンス、およびカスタマーエクスペリエンス s の翻訳を自動化することを目的とした顧客向けのエンドツーエンドの クラウド翻訳マネジメントソフトウェアです。

_この統合は Smartling によって管理されます。_

## 統合について

Brazeコネクターは、キャンペーン s およびキャンバス(メール、プッシュ、およびアプリ内メッセージ s)、メール テンプレート s、およびコンテンツブロックのメッセージの翻訳をサポートします。マルチ言語サポートまたはレガシーワークフローで新しいコネクタを使用する場合は、次のテーブルを参照して、サポートされているチャネルと機能を確認してください。

| チャネル/機能 | 従来のエディタ(例)HTML) | ドラッグ＆ドロップ・エディター |
| --------------- | ----------------------------- | -------------------- |
| [メール]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [プッシュ]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | 該当なし |
| メールテンプレート | レガシーワークフロー | レガシーワークフロー|
| コンテンツブロック |  ✅* |  ✅* |

\* 詳細については、[コンテンツブロックの翻訳の管理](#managing-translations-for-content-blocks)を参照してください。

### レガシーワークフロー

ユースケースに応じて、レガシー変換ワークフローまたは更新 d ワークフローを使用してコンテンツブロックの変換を管理します。 

更新 dワークフローでは、Brazeのマルチ言語サポートとメッセージのロケールを使用して、翻訳タグsがコンテンツブロックに追加されます。ただし、Smartling はメッセージレベルで変換を実行します。コンテンツは、コンテンツがキャンペーンまたはキャンバスに含まれ、ターゲットロケールが設定されている場合にのみ翻訳されます。詳細については、[コンテンツブロックの翻訳の管理](#managing-translations-for-content-blocks)を参照してください。

メール テンプレート s では、レガシーワークフローのみがサポートされます。詳細については、[レガシーワークフローを使用した翻訳の管理](#managing-translations-using-the-legacy-workflow)を参照してください。

## 前提条件

| 必要条件                   | 説明                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartling アカウント             | このパートナーシップを活用するには、[Smartling アカウント](https://dashboard.smartling.com/)が必要です。                                                          |
| Smartling 翻訳プロジェクト | Braze アカウントを Smartling に接続するには、まずサインインし、[翻訳プロジェクトを作成する](https://help.smartling.com/hc/en-us/articles/115003074093)必要があります。 |
| Braze REST API キー            | 以下の権限を持つBraze REST APIキー：<br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> これは、Braze ダッシュボードの**「設定」>「API キー」**から作成できます。 |
| Braze RESTエンドポイント           | [あなたのRESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。             |
| Brazeの多言語設定 | [Braze での多言語設定の完了]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1: Braze での多言語設定の設定

Brazeでのロケールの設定については、[Brazeの多言語セットアップ命令]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites)を参照してください。

### ステップ 2:Smartling TMS で Braze プロジェクトを設定する

コネクタ構成については、[スマートリングドキュメント](https://help.smartling.com/hc/en-us/articles/13248549217435)を参照してください。

### Braze を Smartling に接続する

1. [Smartlingアカウント](https://dashboard.smartling.com/)で、[Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093)プロジェクト種別を作成します。

![スマートリングのBrazeコネクション]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2\.このプロジェクトで、[**設定**] > [**Braze 設定**] > [**Braze に接続する**] の順にクリックします。
3\.API URL やAPI キーなど、必要なフィールドs を入力します。テスト接続が成功した場合は、接続を保存します。テストが成功しなかった場合は、正しいAPI URL とAPI キーを入力したことを確認します。

![スマートリングAPI設定におけるBrazeコネクション]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. プロジェクト言語を追加します。

![スマートリングプロジェクトランゲージのBrazeコネクション。]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Braze 設定s で、**Target Language (Braze)** 列の値が、Braze 多言語設定s で設定されたロケールと一致することを確認します。ロケールの命名規則は完全に一致する必要があります。

![スマートリング・ランゲージ・コンファメーションのBrazeコネクション]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### ステップ 3:変換タグs をBrazeに追加する

メッセージに変換タグs を追加する方法については、[ Brazeの指示]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) を参照してください。

- [メール]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [プッシュ]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [アプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

次に、変換タグs を使用したHTML メール キャンペーンを示します。

![変換タグs のBraze メール。]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

ロケールを選択するには、下書きとして保存する必要があります。

### ステップ 4: スマートリングでの翻訳の管理

Braze コネクターを接続して設定したら、スマートリングプロジェクトのBraze タブでBrazeの内容を確認します。詳細については、[スマートリングドキュメント](https://help.smartling.com/hc/en-us/articles/13248577069979)を参照してください。

Smartling は、以下の方法でコンテンツを検索および選択する高度な機能を提供します。
- キーワード検索
- Braze コンテンツタイプ
- Braze タグ付け

1. この例題では、[Step 3](#step-3-add-translation-tags-to-your-braze-message) に新年プロモーションメール キャンペーンを作成しました。

![変換タグs のBraze メール。]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2\.翻訳するキャンペーンを見つけたら、フォルダーを選択し、バリアントs を選択し、**翻訳のリクエスト** を選択します。

![翻訳をリクエストします。]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3\.翻訳の新しいジョブを作成します。

![翻訳の新しいジョブを作成します。]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. ジョブが許可されたら、CAT ツールで各翻訳を編集します。

![翻訳CATツール。]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. 翻訳が完了したら、翻訳を保存してBraze に送信します。

![Brazeに訳文を提出する。]({% image_buster /assets/img/smartling/image10_translations.png %})

### ステップ 5: Braze で多言語ユーザーとしてプレビューする

Braze では、多言語ユーザーとしてキャンペーンをプレビューし、翻訳がアプリ正しく行われていることを確認します。

![多言語ユーザー プレビュー。]({% image_buster /assets/img/smartling/image11_preview.png %})

## コンテンツブロックの翻訳の管理

コンテンツブロックは、Brazeの**Templates & Media** セクションで管理されます。

### メッセージコンポーネントの一部として保存された翻訳

トランスレーションタグは、コンテンツブロックに属します。ただし、スマートリングでは、メッセージレベルで変換が実行されます。コンテンツは、キャンペーンまたはキャンバスに含まれ、ターゲットロケールが設定されている場合にのみ変換されます。

### 考慮事項

- HTMLおよびドラッグアンドドロップの両方のコンテンツブロックエディタで、翻訳タグs を手動でコンテンツブロックに追加する必要があります。
- ロケールはメッセージレベルで選択され、コンテンツブロック自体では選択されません。
- キャンバスでは、リキッドタグを使用して手動で行を追加する代わりに、行を使用してコンテンツブロックをメッセージに挿入することをお勧めします。コンテンツブロックをプレビューからメールにドラッグすると、ローカルコピーが作成されます。"parent"に変更が加えられても、そのブロックを使用してコンテンツブロックは他のキャンペーンには伝達されません。
- コンテンツブロックリキッドタグを使用する場合は、少なくとも1 つの変換タグをメール本体に直接的に含めるようにしてください。変換タグを手動で追加すると、多言語ドロップダウンからロケールを選択できます。スマートリングは、コンテンツブロックの翻訳タグをピックアップします。`comment` タグを追加して、ユーザーに表示されないようにすることができます。

## レガシーワークフローを使用した翻訳の管理

コンテンツブロックまたはメール テンプレート内で翻訳を直接的に管理する場合は、[Smartling のドキュメント](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector) のレガシー命令を参照してください。このメソッドは、言語属性とLiquid if/else ロジックを使用して、さまざまな言語でテキストを表示します。

## よくある質問

### ドラッグアンドドロップエディタで変換タグがサポートされていますか?

ドラッグアンドドロップエディタ(メール、コンテンツブロック、アプリ内メッセージ) では、リキッドタグとして変換タグs を手動で追加する必要があります。

### リキッドタグ内で文字を翻訳するにはどうすればよいですか?

Smartling は、リキッドタグを認識し、コンポーザーで編集不能にします。「リキッド」タグ内の他のテキスト(デフォルトテキストや結合のようなフィルターなど)も、スマートリングでは編集不能になります。ただし、スマートリングでリキッドタグを削除し、リキッドタグを翻訳されたデフォルトで再作成します。変換を保存すると、ワーニングアプリが鳴ります。
