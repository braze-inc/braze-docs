---
nav_title: インフィリオン
article_title: インフィリオン
alias: /partners/infillion/
description: "この参考記事では、位置情報を活用したマーケティングの関連性を完璧にすることを可能にする、イネーブルメントとインフィリオンのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# インフィリオン

> [インフィリオンは](https://infillion.com/)、位置情報を利用したマーケティングの関連性を完璧なものにすることを可能にする。同社の位置情報SDKは、ジオフェンシング・ソフトウェアやビーコンと組み合わせることで、関連性が高く、パーソナライズされた、近接を意識したモバイル体験を提供する。

ビーコンやジオフェンスサポートをBrazeのターゲティングやメッセージング機能と組み合わせることで、ユーザーの物理的なアクションについて詳しく知ることができ、それに応じてメッセージを送ることができる。このパートナー連携により、次のようなさまざまなユースケースが可能になります。

- **マーケティング:**状況に対応した関連性のあるメッセージを送信し、体験型の消費者ジャーニーを構築します。
- **競合分析:**消費者の傾向やパターンを理解するために、競合ロケーション周辺にトリガーを設定します。
- **オーディエンスインサイト:**ユーザーの訪問行動を理解し、それらの学習に基づいてさらにセグメント化する。

{% alert note %}
この統合は、インフィリオンのビーコンとインフィリオンのジオフェンス・ソリューションでも同じように機能する。
{% endalert %}

## 前提条件

| 必要条件| 説明|
| ---| ---|
| [インフィリオンマネージャーアカウント][1] | このパートナーシップを利用するには、インフィリオンのマネージャーアカウントが必要である。 |
|[インフィリオン・ロケーションSDK](https://docs.gimbal.com/index.html) | Infillion Location SDKは、近接ビーコンとジオフェンスを使用したマクロおよびミクロの位置情報ベースのモバイル体験を提供し、アプリユーザーとのより効果的なコミュニケーションを可能にする。SDK を実装し、ジオフェンス (またはビーコン) を設定しておく必要があります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDKの統合

BrazeとInfillionを統合するには、Infillion Location SDKを実装し、Infillionマネージャーアカウントを作成する必要がある。Android、FireOS、iOS 向けの以下の統合では、ユーザーが入る新しい場所ごとに固有のカスタムイベントが作成されます。これらのイベントをキャンペーンやキャンバスでのトリガーやリターゲティングに使用できます。

50以上の場所を作成することが予想される場合は、一般的な`Places Entered` カスタムイベントを作成し、イベントプロパティとして場所名を追加することを推奨する。 

1. [Infillion][3] [SDK][2]for Android and iOS をアプリに組み込む。
2. ユーザー`places` を取得するには、Infillion の[REST API を][4]使用する。
3. Braze[REST APIキーを][5]入力し、InfillionアカウントとBrazeをリンクする。
4. Braze SDKで[カスタムイベントを][6]設定する。インフィリオンは、Braze for[Android、FireOS][7]、[iOSと][8]統合できる。
5. これらのイベントのログ・プロパティ（場所名、滞留時間）。
6. Brazeでキャンペーンやキャンバスをトリガーするには、これらのプロパティとイベントを使用する。 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data/custom_data/custom_attributes/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons