---
nav_title: Nexla
article_title: Nexla
description: "このリファレンス記事では、Braze と Nexla のパートナーシップについて説明します。Nexla は統合データ運用プラットフォームであり、Braze Currents をご利用のお客様はデータレイクデータを抽出、変換し、カスタムフォーマットで他の場所にデータを読み込むことができます。"
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) は統合データ運用分野のリーダーであり、2021年の Gartner Cool Vender に選出されています。Nexla プラットフォームでは、誰でも簡単にスケーラブルなデータフローを作成でき、ビジネスチームとデータチームにフリクションのない制御されたデータ運用、コラボレーションの向上、アジリティをもたらします。データを扱うチームは、ノーコード / ローコードの統一されたエクスペリエンスで、あらゆるユースケースのデータを統合、変換、プロビジョニング、監視することができます。 

Braze と Nexla の統合により、[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) を利用しているお客様は、Nexla を活用してデータレイクデータを抽出、変換し、カスタムフォーマットで他の場所に読み込むことができ、エコシステム全体でデータに簡単にアクセスできるようになります。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Nexla アカウント | このパートナーシップを活用するには、[Nexla アカウント](https://www.nexla.com/get-demo)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[インスタンスの Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) によって異なります。| |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

Nexla の Data as a Product (製品としてのデータ) である [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) により、メタデータを気にすることなく、あらゆるフォーマットのデータを簡単に扱うことができます。Brazeとの間のデータフローをNexlaで設定する場合、コード不要のツールで簡単に数分で利用できる。データフローが宛先に設定された後で、Nexla はフローを監視し、任意のデータ量にスケーリングします。

## 統合

### ステップ1:Nexla アカウントを作成する

まだ Nexla アカウントをお持ちでない方は、Nexla の [Web サイト](https://www.nexla.com)から無料デモとトライアルを申し込むことができます。次に [www.dataops.nexla.io](https://www.dataops.nexla.io)にログオンし、新しい認証情報でサインオンする。

### ステップ2:ソースを追加する

#### Brazeをデータソースとする場合
1. Nexlaプラットフォームで、左ツールバーの「**フロー」>「新規フローの作成**」を選択する。
2. [**Create New Source**] をクリックし、Braze コネクターを選択し、[**Next**] をクリックします。 
3. [**Add a New Credential**] を選択し、認証情報に名前を付け、Braze API キーと REST エンドポイントを追加して、[**Save**] をクリックします。
4. 最後にデータを選択して [**Save**] をクリックします。 

Nexla はソースでデータを検索し、変換または宛先への送信のために [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) を生成します。

#### Braze が宛先の場合

[Nexla へのソースの接続](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source)については、Nexlaのドキュメントを参照してください。

### ステップ3:トランスフォーム（オプション）

データに対してカスタム[変換を](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations)実行したい場合、またはNexlaのビルド済みコネクタを使用したい場合は、データセットの**変換**ボタンをクリックして変換ビルダーに入る。Transform Builder の使用に関するガイダンスは[Nexla のドキュメント](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)にあります。

### ステップ4:宛先に送信する

宛先にデータを送信するには、データセットの [**宛先**] 矢印をクリックし、Nexla の宛先コネクターまたは Braze (ソースが異なる場合) を選択します。認証情報を入力し、宛先オプションを設定し、[**Save**] をクリックします。データは即座に、あなたが指定したフォーマットで、あなたが選んだ宛先に流れ始める。

## この統合を使用する

一度フローがセットアップされれば、あとは何も必要ない。Nexla はソースデータの変更をすべて処理し、新しいデータへのスケーリングを行い、トリアージのためにスキーマの変更やエラーを通知します。変換、ソース、または宛先を変更する場合は、これらのオプションをクリックして変更を行います。Nexla によりフローが即時に更新されます。

