---
nav_title: "Eメール愛"
article_title: Eメール愛
description: "Figma から直接レスポンシブでアクセス可能なHTML メールを設計およびエクスポートできるFigma プラグインであるEmail Love とBraze を統合する方法について説明します。"
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Eメール愛

> [Email Love](https://emaillove.com/) は、Figma から直接レスポンシブでアクセス可能なHTML メールを設計およびエクスポートできるようにするFigma プラグインです。Email Love のExport to Braze 機能は、Braze API を使用して、E メールテンプレートをBraze にシームレスにアップロードします。

## 前提条件

| 必要条件            | 説明                                                      |
|------------------------|------------------------------------------------------------------|
| **Eメールラブアカウント** | このパートナーシップを活用するには、Email Loveアカウントが必要です。 |
| **Braze REST API キー** | 完全な`Templates` 権限が有効になっているブレーズREST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## メールラブとブレーズの併用

### ステップ1:プラグインを実行する

メールテンプレートを設計するには、まずプラグインをロードする必要があります。詳細な手順については、[電子メールをBraze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm)にアップロードするための電子メールラブのドキュメントを参照してください。

### ステップ2:最初のフレームを作成する

プラグインで、**[+ No Template Selected]** ボタンを選択して、メールデザインの新しいフレームを作成します。

### ステップ 3:Email Loveの事前に構築されたコンポーネントを使用してテンプレートをデザインする

作成したフレームを選択し、プラグインの**Assets**ライブラリからコンポーネント(ヘッダ、コンテンツブロック、CTA、フッタ)の追加を開始して、メールを構築します。

![Email Love のビルド済みコンポーネント。]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### ステップ4:コンポーネントのカスタマイズ

Figma のツールを使用してコンポーネントを変更し、テキスト、画像、色、レイアウト要素を調整して、テンプレートのデザインをブランドに合わせます。フッタコンポーネントを追加すると、エクスポート時に自動的にブレーズ解除リンクが追加されます。

![Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})でコンポーネントをカスタマイズする

### ステップ 5: メールテンプレートをブレーズにエクスポートする

1. 書き出しが終わったら、書き出したいフレームを選択します。エクスポートを実行するには、サブスクリプション解除リンクを含むEmail Love フッターを使用する必要があります。
2. プラグインで**Export** ボタンを選択し、ドロップダウンメニューから**Braze** を選択します。
3. Email Love Figma プラグイン内の**Braze API Key** ボックスにAPI キーをコピーして貼り付けます。
4. **Set API Key**ボタンを選択します。
5. **Change Instance ID**を選択し、BrazeインスタンスIDを選択します。

![Email Love プラグインからBraze へのテンプレートのエクスポート。]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### ステップ 6: メールをブレーズで編集する

ブレーズで、**Templates**> **Edit Templates**> **Edit Message**に移動します。テンプレートエディタ内で、メールHTML を編集するか、**Classic** タブの**リッチテキストエディタ** を使用できます。

## サポートとトラブルシューティング

詳細な手順については、[電子メールデザインをエクスポートする](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm)の電子メールラブのドキュメントを参照してください。その他のサポートについては、Email Love サポートチームにお問い合わせください。
