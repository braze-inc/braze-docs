---
nav_title: Zeotap
description: "このリファレンス記事では、Braze と Zeotap のパートナーシップについて説明します。Zeotap は、アイデンティティ解決、インサイト、データ強化を提供する次世代顧客データプラットフォームです。"
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) は、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。

ZeotapとBrazeの統合により、Zeotapの顧客セグメントを同期してユーザーデータをBrazeのユーザーアカウントにマッピングすることで、キャンペーンの規模とリーチを拡大することができる。そして、このデータに基づいて行動し、ユーザーにパーソナライズされたターゲット体験を提供することができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
|Zeotap アカウント | このパートナーシップを活用するには、[Zeotap アカウント](https://zeotap.com/)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは[インスタンスの Braze URL]({% image_buster /assets/img/zeotap/zeotap1.png %}) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:Zeotap の宛先を作成する

1. Zeotap Unityプラットフォームから**DESTINATIONS**アプリケーションに移動する。
2. **すべてのチャンネル**」で「**Braze**」を選択する。
3. 表示されるプロンプトで、宛先に名前を付け、Braze アカウントに関連付けられたクライアント名と Braze REST API キーを指定します。
4. 最後に、ドロップダウンからBraze RESTエンドポイントインスタンスを選択し、保存先を指定する。<br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### ステップ 2:Zeotapセグメントを作成して目的地にリンクする 
 
1. Zeotap Unityプラットフォームから**CONNECT**アプリケーションに移動する。
2. セグメントを作成し、ステップ1で作成したBrazeデスティネーションを選択する。
3. サポートされている出力識別子を選択する：MAID、SHA256 にハッシュされたメールアドレス、または Braze で認識される1P 顧客識別子 (Braze アカウントにカスタム識別子を使用する場合は、アカウントに対して有効にできるように、Zeotap に連絡してください)。Brazeの統合に使用できる出力識別子は1つだけである。これらの識別子は、Braze SDK データを収集するときに設定された external ID と同じである必要があります。
4. セグメントを保存する。

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
表示される識別子はセグメントで使用でき、Braze でサポートされています。
{% endalert %}

### ステップ3:ブレイズセグメントを作成する

Zeotapでセグメントの作成、プッシュ、処理に成功すると、BrazeダッシュボードにZeotapユーザーが表示される。BrazeダッシュボードでユーザーIDからユーザーを検索できる。 

![「カスタム属性」の下でセグメント1から4が「true」としてリストされている Braze ユーザープロファイル。]({% image_buster /assets/img/zeotap/zeotap4.png %})

ユーザーが Zeotap セグメントの一部である場合、セグメント名は、ブール値 `true` が設定されているユーザープロファイルのカスタム属性として表示されます。Brazeセグメントを作成する際に必要になるので、カスタム属性名をメモしておくこと。 

次に、Braze 内でこのセグメントを作成して定義する必要があります。
1. Braze ダッシュボードから [**セグメント**] を選択し、次に [**セグメントを作成**] を選択します。
2. 次に、セグメントに名前を付け、Zeotapで作成したカスタム属性セグメントを選択する。
3. 変更を保存する。 

![Braze セグメントビルダーでインポートされたセグメントがカスタム属性として設定されていることがわかる。]({% image_buster /assets/img/zeotap/zeotap3.png %})

この新しく作成したセグメントを、今後のBrazeのキャンペーンやキャンバスに追加して、これらのエンドユーザーをターゲットにすることができる。 

