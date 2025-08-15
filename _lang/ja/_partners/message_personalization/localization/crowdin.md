---
nav_title: Crowdin
article_title: Crowdin
description: "このリファレンス記事では、Braze と Crowdin のパートナーシップについて説明します。Crowdin は、クラウドベースのソフトウェアプラットフォームであり、Braze でのメールテンプレートとコンテンツブロックの翻訳を自動化できます。"
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin はローカライゼーション管理のためのクラウドベースのソフトウェアです。Crowdin を使用して、Android や iOS のアプリ、Web サイト、ストアスクリーンショットなどのコンテンツを翻訳できます。翻訳は、社内チーム、翻訳会社、または機械翻訳エンジンを使って行うことができる。

_この統合は Crowdin によって管理されます。_

## 統合について

Braze と Crowdin の統合により、メールテンプレートとコンテンツブロックを翻訳できます。また、Braze アカウントから Crowdin プロジェクトにコンテンツを同期し、Braze に戻って翻訳を追加することもできます。

## 前提条件

| 必要条件| 説明|
| ---| ---|
| Crowdin アカウント | このパートナーシップを活用するには、[Crowdin アカウント](https://accounts.crowdin.com/register)が必要です。 |
| Crowdin 翻訳プロジェクト | Braze アカウントと Crowdin または Crowdin Enterprise を接続するには、最初にサインアップして翻訳プロジェクトを作成する必要があります。 |
| Braze REST API キー | すべてのテンプレートとコンテンツブロック権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze SDKエンドポイント | SDK エンドポイントは[インスタンス]({{site.baseurl}}/api/basics/#endpoints)の Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:Crowdin/Crowdin Enterprise で Braze アプリを設定する

#### Crowdin
CrowdinでBrazeアプリをセットアップするには、以下の手順に従う：

1. [マーケットプレイスの Braze アプリ](https://store.crowdin.com/braze-app)に移動します。
2. [**Install**] をクリックしてアプリをアカウントに追加します。
3. Braze コンテンツのローカライズ用に作成したプロジェクトを開きます。
4. **設定＞統合**タブに進む。
5. **アプリケーション・**セクションで、Brazeアプリをクリックする。
6. ダイアログで、Braze の認証情報 (Braze REST API キーと Braze SDK エンドポイント) を入力します。
7. [**Log in with Braze Connector**] をクリックします。 

#### Crowdin Enterprise
Crowdin EnterpriseでBrazeアプリをセットアップするには、以下の手順に従う：

1. [**Workspace**] ホームページ > [**Marketplace**] に移動します。
2. Braze アプリで [**Install**] をクリックし、組織に追加します。
3. Braze コンテンツのローカライズ用に作成したプロジェクトを開きます。
4. **[Applications] > [Custom]** に移動します。
5. Brazeアプリをクリックする。
6. ダイアログで、Braze の認証情報 (Braze REST API キーと Braze SDK エンドポイント) を入力します。
7. [**Log in with Braze Connector**] をクリックします。

### ステップ2:コンテンツを Crowdin/Crowdin Enterprise に追加する

Brazeの認証情報を入力すると、2つのパネルが表示される。Braze アカウントから翻訳用ファイルを同期するコンテンツを選択し、[**Sync to Crowdin**] をクリックします。

Crowdin の Editor モードでは、Braze アカウントから同期されたコンテンツを、文字列リストまたはファイルプレビューとして翻訳者に表示できます。

![Crowdin Editor のメールコンポーザーに基本的な翻訳を追加した画像。]({% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %})

### ステップ3:Braze に翻訳を追加する

翻訳が完了したらすぐに Crowdin で Braze アプリを開き、左側のパネルで翻訳済みファイルを選択し (ファイルごとに、すべての翻訳言語または特定の翻訳言語のみを選択できます)、[**Sync to Braze**] をクリックします。

![翻訳ファイルを選択し、Braze に同期しているユーザーの画像。]({% image_buster /assets/img/crowdin/sync_translations.png %})


