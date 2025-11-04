---
title: Ketch
nav_title: Ketch
description: "このリファレンス記事では、Braze とKetch の統合について説明します。Ketchは、簡素化されたプライバシー運用、完全でダイナミックなデータ制御、インテリジェンスを提供します。"
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch ](https://www.ketch.com)は、企業がそのデータの責任者となることを可能にします。Ketchは、簡素化されたプライバシー処理、完全でダイナミックなデータ制御、インテリジェンスを提供します。 

_この統合は Ketch によって管理されます。_

## 統合について

Braze と Ketch の統合により、Ketch ユーザー設定センター内の顧客のコミュニケーション設定を管理し、これらの変更を自動的に Braze に伝播できます。 

{% alert note %}
購読グループの作成に関するガイダンスをお探しですか？<a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS購読グループと</a> <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>Eメール購読</a>グループの記事をチェックする。
{% endalert %}

## 前提条件

| 要件 | 説明 |
|---|---|
| Ketch アカウント | この統合を有効にするには、管理者権限を持つ[Ketch](https://www.ketch.com)アカウントが必要である。 |
| BrazeのAPIキー | `users.track`、`subscription.status.get`、`subscription.status.set`、`users.delete`、`users.alias.new`、`users.export.ids`、`email.unsubscribe`、`email.blacklist` の権限を持つ Braze REST API キー。<br><br> これは Brazeダッシュボード ([**開発者コンソール**] > [**REST API キー**] > [**新しい API キーを作成**]) で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Brazeの接続をセットアップする

1. [Ketch インスタンス](https://app.ketch.com)で [**Data Systems**] に移動し、[**Braze**] を選択します。次に [**New Connection**] をクリックします。
2. Braze接続に識別可能な名前を付け、APIベースの処理でこの接続を参照するために使用する。この接続のためのコードも作成されることに注意してください。このコードは、すべての接続において一意である必要があります。
3. ユーザーのIDマッピングを確認する。デフォルトでは、Ketch はユーザーのメールアドレスまたは Braze の`external_id` によってユーザー ID をマッピングします。
4. Braze APIキーを追加し、APIエンドポイントを指定する。この[APIエンドポイントは]({{site.baseurl}}/api/basics/#endpoints)、あなたの組織が使用しているBrazeインスタンスに基づいていることに注意すること。

### ステップ2:サブスクリプション設定を構成する

1. **[Policy Center] > [Subscriptions]** に移動します。**Policy Center（ポリシーセンター）**」に「Subscriptions（購読）」タブが表示されない場合は、マーケティング・プリファレンス・センターにアクセスできることを確認し、製品のこの部分にアクセスするための正しいアカウント権限を持っていることを確認する。
2. [**Create New Subscription**] をクリックして新しいトピックを作成します。各サブスクリプションには名前とコードがある。
3. 購読トピックを送信するチャンネルを追加する。各チャネルは、ユーザーのマーケティングユーザー設定センターに表示されます。また、Ketch ユーザー設定センターで特定のオプトインシグナルまたはオプトアウトシグナルを調整する方法の詳細を追加することもできます。
4. オプトインおよびオプトアウト信号の編成に使用するBraze接続を選択する。
5. Ketch ユーザー設定を送信するサブスクリプショングループの Braze `subscription_group_id` を入力します。

![Braze 購読グループ ID。]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
ユーザーのオプトインとオプトアウトのシグナルを収集し、組織化するためには、IDが適切に設定されていなければならない。Ketch では、この統合向けににユーザー設定シグナルを調整するために、識別子としてメールを設定することをお勧めしています。
{% endalert %}


### ステップ3:アイデンティティを設定する

ユーザーは、Ketch がそのユーザーのマーケティングユーザー設定 ID を確認できる場合にのみ、マーケティングユーザー設定センターを表示できます。Ketch がユーザーの ID を適切にキャプチャできない場合、Ketch はそのユーザーのユーザー設定を管理できないため、そのユーザーに対してマーケティングユーザー設定ページは表示されません。

1. マーケティングユーザー設定 ID を設定するには、Ketch の [**Settings**] ページに移動し、[**Identity space**] をクリックします。新しいアイデンティティスペースを作成するか、既存のアイデンティティスペースを編集して、そのアイデンティティスペースをマーケティングユーザー設定 ID として割り当てる必要があります。プロパティに導入されている Ketch タグが、そのアイデンティティスペースを適切にキャプチャしていることを確認します。
2. **エクスペリエンス・サーバー**]、[**プロパティ**] の順に選択し、目的のプロパティを編集する。そのプロパティのデータレイヤーで、カスタムアイデンティティスペースを有効にします。次に、このサイトでマーケティングユーザー設定 ID をキャプチャする方法を設定します。
3. アイデンティティスペースを設定したら、Ketch タグが導入されている Web サイトのユーザー設定センターを開いて、ユーザー設定センターが表示されるかどうかをテストします。


