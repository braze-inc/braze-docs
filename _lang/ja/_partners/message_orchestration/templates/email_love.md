---
nav_title: "Email Love"
article_title: Email Love
description: "Figma から直接レスポンシブでアクセス可能なHTML メールを設計およびエクスポートできるFigma プラグインであるEmail Love とBraze を統合する方法について説明します。"
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) は、Figma から直接レスポンシブでアクセス可能なHTML メールを設計およびエクスポートできるようにするFigma プラグインです。Email Love の Export to Braze 機能は、Braze API を使用して、メールテンプレートを Braze にシームレスにアップロードします。

## 前提条件

| 必要条件            | 説明                                                      |
|------------------------|------------------------------------------------------------------|
| **Email Love のアカウント** | このパートナーシップを活用するには、Email Loveアカウントが必要です。 |
| **Braze REST API キー** | `Templates` 権限がすべて有効化されている Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Braze での Email Love の使用

### ステップ 1: プラグインを実行する

メールテンプレートを設計するには、まずプラグインをロードする必要があります。詳細な手順については、Email Love の[メールの Braze へのアップロード](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm)についてのドキュメントを参照してください。

### ステップ2: 最初のフレームを作成する

プラグインで**[+ No Template Selected]**ボタンを選択し、メールデザイン用の新しいフレームを作成する。

### ステップ 3:Email Loveの事前に構築されたコンポーネントを使用してテンプレートをデザインする

作成したフレームを選択し、プラグインの **Assets** ライブラリーからコンポーネント (ヘッダー、コンテンツブロック、CTA、フッター) の追加を開始して、メールを構築します。

![メールラブの既成コンポーネント。]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### ステップ 4: コンポーネントのカスタマイズ

Figma のツールを使用してコンポーネントを変更し、テキスト、画像、色、レイアウトの要素を調整して、ブランドに合わせてテンプレートをデザインします。フッターコンポーネントを追加すると、エクスポート時に Braze 購読解除リンクが自動的に追加されます。

![Figmaでコンポメントをカスタマイズする。]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### ステップ 5: Braze へのメールテンプレートのエクスポート

1. 書き出しが終わったら、書き出したいフレームを選択します。エクスポートを実行するには、購読解除リンクを含むEmail Love フッターを使用する必要があります。
2. プラグインで**Export** ボタンを選択し、ドロップダウンメニューから**Braze** を選択します。
3. Email Love Figma プラグイン内の**Braze API Key** ボックスにAPI キーをコピーして貼り付けます。
4. [**Set API キー**] ボタンを選択します。
5. [**インスタンス ID の変更**] を選択してから、Braze インスタンス ID を選択します。

![Email LoveプラグインからBrazeにテンプレートをエクスポートする。]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### ステップ 6: Braze でのメールの編集

Braze で、[**テンプレート**] > [**テンプレートを編集**] > [**メッセージを編集**] に移動します。テンプレートエディタ内で、メールHTML を編集するか、**Classic** タブの**リッチテキストエディタ** を使用できます。

## サポートとトラブルシューティング

詳細な手順については、Email Love の[メールデザインのエクスポート](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm)についてのドキュメントを参照してください。その他のサポートについては、Email Love サポートチームにお問い合わせください。
