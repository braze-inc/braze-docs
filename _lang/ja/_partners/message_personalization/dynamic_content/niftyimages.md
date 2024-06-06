---
nav_title: ニフティイメージズ
article_title: ニフティイメージズ
description: "NiftyImages を Braze と統合する方法を学びます。"
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# ニフティイメージズ

> [NiftyImages は](https://niftyimages.com) 、マーケティング担当者がエンゲージメントと収益を向上させながら、関連性の高い最新の電子メール通信をより効率的に送信できるようにするリアルタイムの電子メール パーソナライゼーション ソフトウェアです。これは、マーケティング担当者が電子メールに動的なコンテンツを簡単かつ迅速に追加できる、ユーザーフレンドリーなセルフサービス ツールです。

## 前提条件

NiftyImages は、統合を必要とせず、すぐに Braze と連携して動作します。始めるには、[NiftyImages アカウント](https://niftyimages.com/Signup)だけが必要です。

## サポートされている機能

Braze で NiftyImages を活用すると、既存の Braze パーソナライゼーション タグを NiftyImages URL にマッピングして、電子メール キャンペーン用の動的でパーソナライズされた画像を作成できます。

- **プライバシー**;すべてのデータは NiftyImages ではなく Braze に保存されます。
- **パーソナライズされた画像:**任意の Braze マージ タグを使用して画像をパーソナライズします。
- **チャートとグラフ:**カスタマイズ可能なチャートとグラフを通じて、階層レベル、顧客ステータス、支出額、ポイントなどを表示します。
- **マップ:**ユーザーがメールを開いた場所に最も近い場所を使用して地図の画像を表示します。
- **カスタムカウントダウンタイマー:**誕生日、試用期限、最終購入日、支払い期限超過、最終サインイン日などの日付データベース変数を使用して、固有のタイマーを表示します。
- **リアルタイムコンテンツ:**商品の推奨、カートの放棄、値下げ、在庫レベル、天気などのリアルタイム画像を表示します。
- **ライブアンケート:**ライブアンケートを表示してエンゲージメントを促進し、関心レベルに関する洞察を得ます。
- **ルールベースのロジック:**ユーザーデータ、人口統計、行動、場所、時間帯、曜日、開いているデバイス、オペレーティングシステムなどに基づいて動的な画像を表示します。

たとえば、以下は NiftyImages が顧客の名を使用して生成したカスタム画像です。

![ALT_TEXT.]({% image_buster /assets/img/niftyimages/1.png %}){: style="max-width:70%;"}

## NiftyImage の作成

### ステップ 1: マージタグを作成する

NiftyImages で、マージ タグを選択し、デフォルト値を入力します。完了したら、**「次へ」**を選択します。

![alt text]({% image_buster /assets/img/niftyimages/2.png %}){: style="max-width:70%;"}

必要に応じて、データ型を入力し、**「次へ」**を選択します。

![alt text]({% image_buster /assets/img/niftyimages/3.png %})
{: style="max-width:70%;"}

オプションで、将来使用するためにタグを保存することもできます。完了したら、**「保存」** を選択してマージ タグを作成します。

![alt text]({% image_buster /assets/img/niftyimages/4.png %}){: style="max-width:70%;"}

### ステップ 2: 画像をカスタマイズする

画像のフォント、フォント サイズ、配置、色、レイヤーなどをカスタマイズします。完了したら、画像の URL をコピーします。

![alt text]({% image_buster /assets/img/niftyimages/5.png %})

### ステップ 3: Brazeに画像のURLを追加する

Braze でキャンペーンまたはキャンバスを開き、NiftyImage の URL を貼り付けます。必要に応じて、変更内容をプレビューして Liquid タグを検証することもできます。

![alt text]({% image_buster /assets/img/niftyimages/6.png %})
