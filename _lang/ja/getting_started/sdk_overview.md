---
nav_title: SDK の概要
article_title: 開発者向けの SDK 概要
description: "このオンボーディングリファレンス記事には、Braze SDK の開発者向けの技術概要が記載されています。ここでは、SDK でトラッキングされるデフォルトの分析、自動データ収集のブロック、アプリのライブ SDK バージョンについて説明します。"
page_order: 0
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}開発者sのSDK概観

> Braze SDK の統合を開始する前に、正確に何を構築および統合するのかを疑問に思うかもしれません。また、ニーズに応じて SDK をより詳細にカスタマイズする方法に興味があるかもしれません。この記事は、SDK に関するすべての疑問を解決するのに役立ちます。 

SDK の基本的な概要を探しているマーケターは、代わりに[マーケターの概要]({{site.baseurl}}/user_guide/getting_started/web_sdk/)をご覧ください。

Braze SDK を簡単に説明すると、次のとおりです。
* ユーザーデータを収集し、統合ユーザープロファイルに同期します
* セッションデータ、デバイス情報、プッシュトークンを自動的に収集する
* マーケティングエンゲージメントデータとビジネスに固有のカスタムデータを取得します
* プッシュ通知、アプリ内メッセージ、コンテンツカード メッセージング チャネルを強化します

## アプリのパフォーマンス

Braze がアプリのパフォーマンスに悪影響を及ぼすことはありません。

Braze SDK のフットプリントは非常に小さいです。手動のネットワーク制御が許可されるのに加え、ネットワークの品質に応じ、ユーザーデータをフラッシュするレートの自動変更が実行されます。SDK からの API リクエストを自動的にバッチ処理して、ネットワーク効率を常に最大化しながらデータが迅速にロギングされるようにします。最後に、各 API 呼び出し内でクライアントから Braze に送信されるデータは非常に少量です。

## SDK の互換性

Braze SDK は非常に円滑に動作し、アプリ内に存在する他の SDK に干渉しないよう設計されています。他のSDKとの互換性がないことが原因であると思われる問題が発生した場合は、Brazeサポートにお問い合わせください。

## デフォルトの分析とセッション処理

最初に使用したアプリ、最後に使用したアプリ、合計セッション数、デバイス OS など、特定のユーザーデータは SDK で自動的に収集されます。統合ガイドに従って SDK を実装すると、この[デフォルトデータ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)を利用できるようになります。このリストを確認することで、ユーザーに関する同じ情報を複数回保存しなくて済みます。セッションスタートとセッションエンドを除いて、他の自動トラッキングデータはデータポイント使用量には含まれません。

{% alert note %}
すべての機能が構成可能ですが、デフォルトのデータ収集モデルを完全に実装することをお勧めします。

<br>ユースケースで必要な場合は、統合の完了後に[特定のデータの収集を制限](#blocking-data-collection)できます。
{% endalert %}

## データのアップロードとダウンロード

Braze SDK では、データ (セッション、カスタムイベントなど) がキャッシュされ、定期的にアップロードされます。データがアップロードされた後でのみ、ダッシュボード上で値が更新されます。アップロード間隔は、デバイスの状態を考慮し、ネットワーク接続の品質に基づいて決定されます。

|ネットワーク接続品質 |    データフラッシュ間隔|
|---|---|
|素晴らしい    |10秒|
|良好    |30秒|
|不良    |60秒|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ネットワーク接続がない場合、ネットワーク接続が再確立されるまで、データはデバイスのローカルにキャッシュされます。接続が再確立されると、データが Braze にアップロードされます。

セッションの時点でユーザーが属するセグメントに基づいて、セッションの開始時に Braze から SDK にデータが送信されます。新しいアプリ内メッセージはセッション中に更新されません。ただし、セッション中のユーザーデータは、クライアントから送信されると継続的に処理されます。たとえば、離脱ユーザー (アプリを最後に使用してから7日以上経過) には、アプリに戻ってから最初のセッションで、離脱ユーザーをターゲットにしたコンテンツが提供されます。

## データ収集のブロック

SDK 統合からの特定のデータの自動収集をブロックしたり、そのプロセスを許可リストに登録したりすることは (推奨はされませんが) 可能です。 

分析データを削除すると、プラットフォームのパーソナライゼーションとターゲット設定の能力が低下するため、データ収集をブロックすることは推奨されません。以下はその例です。

- いずれかの SDK で位置情報を完全に統合しないことを選択した場合、言語や位置情報に基づいてメッセージングをパーソナライズできません。 
- タイムゾーンを統合しないことを選択した場合、ユーザーのタイムゾーン内でメッセージを送信できない可能性があります。 
- 特定のデバイスビジュアル情報を統合しないことを選択した場合、メッセージのコンテンツがそのデバイス向けに最適化されない可能性があります。

製品の機能を最大限に活用するには、SDK を完全に統合することを強くお勧めします。

{% tabs %}
{% tab Web SDK %}

SDK の特定の部分を統合しないことも、ユーザーに [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) を使用することもできます。このメソッドにより、`disableSDK()` の呼び出し前にロギングされたデータが同期され、このページと将来のページの読み込みに対するその後の Braze Web SDK の呼び出しはすべて無視されます。後の時点でデータ収集を再開するには、後で [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) メソッドを使用できます。この詳細については、[Web トラッキングの無効化]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web)に関する記事をご覧ください。

{% endtab %}
{% tab Android SDK %}

[`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) を使用し、設定された許可リストに従ってデバイスオブジェクトのキーまたは値のサブセットのみを送信するよう SDK を構成できます。これは [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder) を介して有効にする必要があります。

{% alert important %}
許可リストが空の場合、 デバイスデータは Braze に送信**されません**。
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

`Braze.Configuration` で対象となるフィールドのセットを [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) に割り当て、SDK で収集されるデバイスフィールドの許可リストを指定することができます。フィールドの完全なリストは [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) で定義されます。すべてのデバイスフィールドの収集をオフにするには、このプロパティの値を空のセット (`[]`) に設定します。

{% alert important %}
デフォルトでは、Braze Swift SDK ですべてのフィールドが収集されます。一部のデバイスプロパティを削除すると、SDK 機能が無効になる場合があります。
{% endalert %}

使用の詳細については、Swift SDK ドキュメントの「[ストレージ]({{site.baseurl}}/developer_guide/storage/?tab=swift)」を参照してください。

{% endtab %}
{% endtabs %}

## 使用している SDK バージョンの確認

ダッシュボードを使用して、**[設定] > [アプリ設定]** から特定のアプリの SDK バージョンを確認できます。[**ライブ SDK バージョン**] には、ユーザーの5% 以上を対象とする最新のライブアプリケーションで使用されている最上位の Braze SDK バージョンが一覧にされています。

![ワークスペースの Swifty という名前のアプリ。Live SDK バージョンは6.6.0です。]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
iOS アプリをお持ちの場合、**Live SDK バージョン**が5.0.0 (最初にリリースされた Swift SDK のバージョン) 以降であれば、従来の [Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) の代わりに [Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) を使用していることを確認できます。
{% endalert %}

