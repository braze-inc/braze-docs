---
nav_title: Zeotap
description:「この参考記事では、IDの解決、洞察、エンリッチメントを提供する次世代の顧客データプラットフォームであるBrazeとZeotapのパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner
page_order:1
---

# Zeotap

> [Zeotapは](https://zeotap.com/)、ID解決、洞察、データエンリッチメントを提供することで、モバイルオーディエンス発見と理解を支援する次世代の顧客データプラットフォームです。

ZeotapとBrazeの統合により、Zeotapの顧客セグメントを同期してユーザーデータをBrazeユーザーアカウントにマッピングすることで、キャンペーンの規模とリーチを拡大できます。その後、このデータに基づいて行動を起こし、パーソナライズされたターゲットエクスペリエンスをユーザーに提供できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
|ゼロタップアカウント | このパートナーシップを利用するには、[Zeotapアカウントが必要です](https://zeotap.com/)。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント  | あなたの REST エンドポイント URL。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 統合

### ステップ1:ゼオタップ送信先の作成

1. Zeotap Unity プラットフォームから、**デスティネーションアプリケーションに移動します**。
2. \[**すべてのチャンネル**] で \[**Braze**] を選択します。
3. 表示されるプロンプトで、送信先に名前を付け、クライアント名と Braze アカウントに関連付けられた Braze REST API キーを入力します。
4. 最後に、ドロップダウンから Braze REST エンドポイントインスタンスを選択し、送信先を保存します。<br><br>![][1]

### ステップ2:ZeotapSegment を作成して送信先にリンクする 
 
1. Zeotap Unity プラットフォームから、**CONNECT** アプリケーションに移動します。
2. Segment を作成し、ステップ 1 で作成した Braze 送信先を選択します。
3. サポートされている出力識別子を選択してください:MAID、SHA256にハッシュされたメールアドレス、またはBrazeが認識する任意の1P顧客識別子（Brazeアカウントにカスタム識別子を使用したい場合は、Zeotapに連絡して、アカウントで有効にできるようにしてください）。Braze インテグレーションに使用できる出力識別子は 1 つだけです。これらの識別子は、Braze SDK データを収集するときに設定された外部 ID と同じである必要があります。
4. Segment を保存します。

![][2]

{% alert note %}
表示される識別子は、Segment で利用できるものとBrazeがサポートしているものの両方です。
{% endalert %}

### ステップ3:Braze Segment を作成

ZeotapでSegment の作成、プッシュ、処理が正常に完了すると、ZeotapユーザーがBrazeダッシュボードに表示されます。Braze ダッシュボードでユーザー ID でユーザーを検索できます。 

![「カスタム属性」に「true」と表示されているSegment 1～4のBrazeユーザープロファイル。][4]

ユーザーがZeotapSegment の一部である場合、Segment 名はユーザープロファイルのカスタム属性としてブーリアン値とともに表示されます。`true`Braze セグメントを作成するときに必要になるので、カスタム属性名をメモしておいてください。 

次に、Braze 内でこのSegment を作成して定義する必要があります。
1. Braze ダッシュボードから \[**セグメント] を選択し、\[**セグメントを作成****] を選択します。
2. 次に、Segment に名前を付け、Zeotapで作成したカスタム属性Segment を選択します。
3. 変更を保存します。 

![Braze Segment ビルダーでは、インポートされたセグメントがカスタム属性として設定されています。][3]

これで、新しく作成したSegment を今後のBrazeキャンペーンやキャンバスに追加して、これらのエンドユーザーをターゲットにすることができます。 

[1]: {% image_buster /assets/img/zeotap/zeotap1.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap2.png %}
[3]: {% image_buster /assets/img/zeotap/zeotap3.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap4.png %}
