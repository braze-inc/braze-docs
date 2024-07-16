---
nav_title: Crowdin
article_title:Crowdin
description:"この参考記事では、BrazeとクラウドベースのソフトウェアプラットフォームであるCrowdinのパートナーシップについて概説している。"Brazeでは、メールテンプレートやコンテンツブロックの翻訳を自動化することができる。
alias: /partners/crowdin/
page_type: partner
search_tag:Partner

---

# Crowdin

> Crowdinはローカライゼーションマネジメントのためのクラウドベースのソフトウェアである。Crowdinを使えば、AndroidやiOSアプリ、Webサイト、店舗のスクリーンショット、その他のコンテンツを翻訳できる。翻訳は、社内チーム、翻訳会社、または機械翻訳エンジンを使って行うことができる。

BrazeとCrowdinの統合により、メールテンプレートやコンテンツブロックを翻訳することができる。また、BrazeアカウントからCrowdinプロジェクトにコンテンツを同期し、Brazeに戻って翻訳を追加することもできる。

## 前提条件

| 必要条件| 説明|
| ---| ---|
| Crowdinアカウント | このパートナーシップを利用するには、[Crowdinアカウントが](https://accounts.crowdin.com/register)必要だ。 |
| Crowdin翻訳プロジェクト | BrazeアカウントとCrowdinまたはCrowdin Enterpriseを接続するには、まずサインアップして翻訳プロジェクトを作成する必要がある。 |
| Braze REST API キー | すべてのテンプレートとコンテンツブロックの権限を持つBraze REST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze SDKエンドポイント | SDKエンドポイントURLは、[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:Crowdin/CrowdinエンタープライズでBrazeアプリを設定する

#### Crowdin
CrowdinでBrazeアプリを設定するには、以下のステップに従う：

1. [マーケットプレイスのBrazeアプリに](https://store.crowdin.com/braze-app)アクセスする。
2. **インストールを**クリックしてアカウントに追加する。
3. Brazeコンテンツのローカライゼーション用に作成したプロジェクトを開封する。
4. **設定＞統合**タブに進む。
5. **アプリケーション**セクションで、Brazeアプリをクリックする。
6. ダイアログで、Braze認証情報（Braze REST APIキーとBraze SDKエンドポイント）を入力する。
7. **Braze Connectorでログインを**クリックする。 

#### Crowdinエンタープライズ
Crowdin EnterpriseでBrazeアプリを設定するには、以下のステップに従う：

1. **ワークスペース**・ホームページ＞**マーケットプレイスに**アクセスする。
2. Brazeアプリの**インストールを**クリックし、組織に追加する。
3. Brazeコンテンツのローカライゼーション用に作成したプロジェクトを開封する。
4. **アプリケーション」＞「顧客」と進む。**
5. Brazeアプリをクリックする。
6. ダイアログで、Braze認証情報（Braze REST APIキーとBraze SDKエンドポイント）を入力する。
7. **Braze Connectorでログインを**クリックする。

### ステップ2:コンテンツをCrowdin/Crowdin Enterpriseに追加する

Brazeの認証情報を入力すると、2つのパネルが表示される。Brazeアカウントから翻訳用ファイルを同期するコンテンツを選択し、**Crowdinに同期を**クリックする。

CrowdinのEditorモードでは、Brazeアカウントから同期されたコンテンツを、文字列リストまたはファイルプレビューとして翻訳者に表示することができる。

![Crowdin Editorのメールコンポーザーに基本的な翻訳を追加した画像写真。][2]

### ステップ3:Brazeに翻訳を追加する

翻訳が完了したら、CrowdinでBrazeアプリを開封し、左側のパネルで翻訳したファイル（ファイルごとに、すべての対象言語か特定の言語かを選択できる）を選択し、**Brazeに同期を**クリックする。

![ユーザーが翻訳ファイルを選択し、Brazeに同期している画像、写真。][3]

[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
