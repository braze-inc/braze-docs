---
nav_title: SDK によるデータ収集
article_title: SDK によるデータ収集
page_order: 1
page_type: reference
description: "このリファレンス記事では、パーソナライズされた連携、自動的に収集される連携、および最小限の連携を通じて SDK によって収集されるデータについて説明します。"

---

# SDK によるデータ収集

> Braze SDK をお客様のアプリやサイトと連携すると、Braze は特定タイプのデータを自動的に収集します。このデータには、当社のプロセスに必須のものと、お客様が必要に応じてオン / オフを切り替えられるものがあります。セグメンテーションとメッセージングをさらに強化するために、インテグレータは他のタイプのデータを追加で収集するように Braze を設定することもできます。

Braze は、柔軟にデータ収集ができるように設計されています。Braze SDK の連携は、以下の 3 とおりの方法で行うことができます。

- **最小限の連携:** Braze は、Braze サービスとの通信を可能にするために必要なデータを自動的に収集します。 
- **デフォルトで収集されるオプションのデータ:** Braze は、お客様のほとんどのユースケースで広く役立つデータを自動的に取得します。この自動的に収集されたデータが最小限の連携に不要な場合、インテグレータはこの自動収集データを無効にすることができます。 
- **パーソナライズされた連携:** デフォルトのオプションデータに加えて、インテグレータはデータを柔軟に収集できます。

## 最小限の連携

以下に、インテグレータが SDK の初期化を選択したときに、Braze が生成し受信する厳密な必須データの一覧を示します。これらはオン / オフ設定ができない要素で、プラットフォームのコア機能に不可欠です。セッションの開始と終了を除き、自動的に追跡される他のデータはすべて、データポイントの割り当てを消費しません。

| 属性 | プラットフォーム | 説明 | 収集する理由 |
| --------- | -------- | ----------- | ------------------ |
| アプリのバージョン名 /<br> アプリのバージョンコード | Android、iOS、Web | 最新のアプリバージョン | この属性は、アプリのバージョンの互換性に関連するメッセージを正しいデバイスに送信するために使用されます。サービスの中断やバグをユーザーに通知する目的で使用できます。 |
| 国 | Android、iOS | IP アドレスのジオロケーションによって特定される国 | この属性は、地理的位置に基づいてメッセージのターゲットを指定するために使用されます。 |
| デバイス ID | Android、iOS、Web | ランダムに生成された文字列で表されるデバイス識別子 | この属性は、ユーザーのデバイスを区別し、目的の正しいデバイスにメッセージを送信するために使用されます。 |
| IDFV | iOS | デバイス識別子。弊社の [Swift SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) で IDFV の収集がオプションになりました。 | ユーザーのデバイスを区別し、目的の正しいデバイスにメッセージを送信するために使用されます。 |
| OS と OSバージョン | Android、iOS、Web | 現在報告されているデバイス /browser and device/browser version | This attribute is used to ensure messages are only sent to compatible devices. It can also be used within segmentation to target users to upgrade app versions. |
| セッションの開始時点と終了時点 | Android、iOS、Web | ユーザーが、連携されているアプリやサイトの使用を開始した時点 | ユーザーの把握に不可欠なユーザーエンゲージメントやその他の分析情報を求めるために、Braze SDK は Braze ダッシュボードで使用されるセッションデータを報告します。アプリでサイトがセッションの開始時点と終了時点を厳密にどの時点と見なすかは、開発者 ([Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/)、 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/)、 [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/)) が設定できます。|
| SDK メッセージのインタラクションデータ | Android、iOS、Web | プッシュの直接開封、アプリ内メッセージのインタラクション、コンテンツカードのインタラクション | この属性は、メッセージが受信されたことや送信が重複していないことの確認など、品質管理の目的で使用されます。 |
| SDK バージョン | Android、iOS、Web | 現在の SDK バージョン | この属性は、互換性のあるデバイスにのみメッセージを送信し、またサービスの中断を防ぐという目的を確実に達成するために使用されます。 |
| セッション ID とセッションのタイムスタンプ | Android、iOS、Web | ランダムに生成された文字列であるセッション識別子と、セッションのタイムスタンプ | ユーザーが新規セッションと既存のセッションのいずれを開始しているかの判別、またこのユーザー宛てのメッセージの再適格性の判別に使用します。<br><br>アプリ内メッセージやコンテンツカードなどの特定のメッセージングチャネルは、セッションの開始時にデバイスに同期されます。その後、バックエンドは、Braze サーバーへの最終アクセス日時に関連するデータ (デバイスが保存して送信する) を使用して、ユーザーに新規メッセージを受け取る資格があるかどうかを判断します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### 計算された指標

Braze バックエンドは、SDK データ、非 SDK メッセージに関連するメッセージインタラクションデータ、および派生情報を計算して指標を生成します。わかりやすく言うと、この計算されたデータは SDK が追跡するものではなく、Braze サービスによって生成されるデータであり、ユーザープロファイルには追跡されたデータと生成されたデータの両方が表示されます。 

計算された指標には、次の属性が含まれます。

| 属性                                      | 説明                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| アプリの初回使用                                 | 時間                                                                 |
| アプリの最終使用                                  | 時間                                                                 |
| 合計セッション数                            | 数値                                                               |
| クリックされたカード数                                   | 数値                                                               |
| メッセージの最終受信                     | 時間                                                                 |
| メールキャンペーンの最終受信                   | 時間                                                                 |
| プッシュキャンペーンの最終受信                    | 時間                                                                 |
| フィードバック項目の数                       | 数値                                                               |
| |過去 Y 日間のセッション数          | 数値と時間                                                      |
| キャンペーンからのメッセージ受信                  | ブール値。このフィルターを使用すると、以前のキャンペーンを受信した (受信していない) に基づいてユーザーのターゲットを設定できます。                               |
| タグ付きのキャンペーンからのメッセージ受信        | ブール値。このフィルターを使用すると、現在タグが付いているキャンペーンを受信した (受信していない) に基づいてユーザーのターゲットを設定できます。                  |
| リターゲティングキャンペーン                              | ブール値。このフィルターを使用すると、ユーザーが過去に特定のメール、プッシュ、またはアプリ内メッセージの開封またはクリックを行ったかどうかに基づいて、ターゲットのユーザーを設定できます。 |
| アンインストール済み                                     |ブール値と時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert important %}
最小限の連携のみに関心があり、mParticle、Segment、Tealium、または GTM と連携する場合は、次の点に注意してください。
- **モバイルプラットフォーム**: これらを構成するコードを手動で更新する必要があります。mParticle と Segment は、そのプラットフォームを通じてこれを行う方法を提供していません。
- **Web**: 最小限の連携構成を可能にするために、Braze の連携をネイティブに行う必要があります。タグマネージャーは、プラットフォームを通じてこれを行う方法を提供していません。
{% endalert %} 

## デフォルトで収集されるオプションのデータ

インテグレータが SDK を初期化すると、Braze によって、最小限の連携データに加えて次の属性が自動的に取得されます。インテグレータは、これらの属性の収集を[オプトアウト]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection)して、最小限の連携を実現できます。

| 属性        | プラットフォーム           | 説明                                            | 収集する理由                                  |
| ---------------- | ------------------ | ------------------------------------------------------ | --------------------------------------------------- |
| ブラウザー名     | Web                | ブラウザーの名前                                   | この属性は、互換性のあるブラウザーにのみメッセージを送信するために使用されます。また、ブラウザーベースのセグメンテーションにも使用できます。|
| デバイス広告の追跡が有効 | iOS      | iOS の `adTrackingEnabled` 属性                 | この属性は、このアプリで広告の追跡が有効になっているかどうかを追跡します。|
| デバイス IDFA      | iOS                | 広告主用のデバイス識別子                     | オプションで、データの追跡に使用されます。 |
| デバイスのロケール    | Android、iOS       | デバイスのデフォルトのロケール                     | この属性は、メッセージをユーザーの優先言語に翻訳するために使用されます。 |
| デバイスモデル     | Android、iOS       | デバイスの特定のハードウェア                   | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。また、セグメンテーション内でも使用できます。 |
| デバイスブランド     | Android       | デバイスのブランド (Samsung など)                   | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。 |
| デバイスの通信事業者 | Android、iOS | モバイル通信事業者                                     | この属性は、オプションでメッセージのターゲット設定に使用されます。              |
| 言語         | Android、iOS、Web  | デバイス /browser language                               | This attribute is used to translate messages to a user's preferred language. |
| Notification settings | Android, iOS, Web  | Whether this app has push notifications enabled. | This attribute is used to enable push notifications. |
| Resolution       | Android, iOS, Web  | Device/browser resolution                             | Optionally used for device-based message targeting. The format of this value is "`<width>`x`<height>`" です。 |
| タイムゾーン        | Android、iOS、Web  | デバイス / ブラウザーのタイムゾーン                              | この属性は、各ユーザーのローカルタイムゾーンに従って、メッセージを適切な時刻に送信するために使用されます。 |
| ユーザーエージェント       | Web                | [ユーザーエージェント](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。また、セグメンテーション内でも使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

デバイスの通信事業者、タイムゾーン、解像度など、デバイスレベルの属性の追跡の詳細については、対応するプラットフォームのドキュメントを参照してください。[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/storage/ "Android の許可リストのドキュメント")、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/storage/ "iOS の許可リストのドキュメント")、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/cookies_and_storage/#device-properties "Web の許可リストのドキュメント")。

## パーソナライズされた連携

Braze を最大限に活用しようとするインテグレータは、多くの場合 Braze SDK を実装し、自動的に収集されたデータに加えて、ビジネスに関連する[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes)、[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events)、[購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events)を記録します。

パーソナライズされた連携により、ユーザーエクスペリエンスに関連付けてコミュニケーションをカスタマイズできます。

{% alert important %}
Brazeは、セッション数が 500 万を超えるユーザー (「ダミーユーザー」) の禁止またはブロックを行い、SDK イベントの取り込みを停止します。詳細については、「[スパムのブロック]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)」を参照してください。
{% endalert %}


[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html "Android のデバイスレベルのフィールド"
