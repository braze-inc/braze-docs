---
nav_title: NiftyImages
article_title: NiftyImages
description: "NiftyImagesをBrazeと統合する方法を学びます。"
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com) は、マーケターが関連性のある最新情報を含むメールをより効率的に送信し、かつエンゲージメントを強化し収益を増やすことができるリアルタイムのメールパーソナライゼーションソフトウェアです。それはマーケティング担当者が簡単かつ迅速にメールにダイナミックなコンテンツを追加できるユーザーに優しいセルフサービングツールです。

_この統合は NiftyImages によって管理されます。_

## 前提条件

NiftyImages はデフォルトの Braze プラットフォームで動作し、統合は不要です。使用を開始するために必要なものは、[NiftyImages アカウント](https://niftyimages.com/Signup)だけです。

## サポートされている機能

BrazeでNiftyImagesを活用することで、既存のBrazeパーソナライゼーションタグをNiftyImagesのURLにマッピングすることにより、メールキャンペーン用のダイナミックでパーソナライズされた画像を作成できます。

- **プライバシー;**すべてのデータはNiftyImagesではなく、Brazeに保存されます。
- **パーソナライズされた画像:**Braze のマージタグを使用して画像をパーソナライズします。
- **チャートとグラフ:**カスタマイズ可能なチャートやグラフを通じて、ティアレベル、顧客ステータス、支出金額、ポイントなどを表示します。
- **地図:**ユーザーがメールを開く場所に最も近い場所を使用して地図の画像を表示します。
- **カスタムカウントダウンタイマー:**誕生日、トライアルの有効期限、最終購入日、支払期日を過ぎた請求書、最終サインイン日などの日付データベース変数を使用して独自のタイマーを表示します。
- **リアルタイムコンテンツ:**おすすめ製品、カートの放棄、値下げ、在庫レベル、天気などのリアルタイム画像を表示します。
- **ライブ投票:**ライブ投票を表示してエンゲージメントを促進し、関心レベルに関するインサイトを得る。
- **ルールベースのロジック:**ユーザーデータ、人口統計、行動、場所、時刻、曜日、開いているデバイス、オペレーティングシステムなどに基づいてダイナミックな画像を表示します。

たとえば次の画像は、顧客の名を使用して NiftyImages によって生成されたカスタム画像です。

![ALT_TEXT.]({% image_buster /assets/img/niftyimages/1.png %}){: style="max-width:70%;"}

## NiftyImageを作成する

### ステップ1:マージタグを作成

NiftyImagesでマージタグを選択し、デフォルト値を入力します。完了したら、**次へ**を選択します。

![代替テキスト]({% image_buster /assets/img/niftyimages/2.png %}){: style="max-width:70%;"}

オプションで、データ型を入力してから**次へ**を選択します。

![代替テキスト]({% image_buster /assets/img/niftyimages/3.png %})
{: style="max-width:70%;"}

必要に応じて、タグを将来使用するために保存することもできます。完了したら、**保存**を選択してマージタグを作成します。

![代替テキスト]({% image_buster /assets/img/niftyimages/4.png %}){: style="max-width:70%;"}

### ステップ2:画像をカスタマイズする

画像のフォント、フォントサイズ、位置、色、レイヤリングなどをカスタマイズします。終了したら、画像のURLをコピーしてください。

![代替テキスト]({% image_buster /assets/img/niftyimages/5.png %})

### ステップ 3:Brazeに画像URLを追加

Braze でキャンペーンまたはキャンバスを開き、NiftyImage URL を貼り付けます。必要に応じて、変更をプレビューして Liquid タグを確認できます。


![代替テキスト]({% image_buster /assets/img/niftyimages/6.png %})
