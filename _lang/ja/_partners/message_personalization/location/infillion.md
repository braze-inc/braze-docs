---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "この参考記事では、Braze と Infillion のパートナーシップの概要を説明しています。Infillion では位置情報を利用したマーケティングの妥当性を改善することができます。"
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) を利用すると、位置情報を活用してマーケティングの妥当性を改善することができます。同社の位置情報SDKは、ジオフェンシング・ソフトウェアやビーコンと組み合わせることで、関連性が高く、パーソナライズされた、近接を意識したモバイル体験を提供する。

ビーコンやジオフェンスサポートを Braze のターゲティングやメッセージング機能と組み合わせることで、ユーザーの物理的なアクションについて詳しく知ることができ、それに応じてメッセージを送ることができます。このパートナー連携により、次のようなさまざまなユースケースが可能になります。

- **マーケティング:**状況に対応した関連性のあるメッセージを送信し、体験型の消費者ジャーニーを構築します。
- **競合分析:**消費者の傾向やパターンを理解するために、競合ロケーション周辺にトリガーを設定します。
- **オーディエンスインサイト:**ユーザーの訪問行動を理解し、それらの学習に基づいてさらにセグメント化する。

{% alert note %}
この統合は、Infillion のビーコンと Infillion のジオフェンスソリューションで、同様の機能を果たします。
{% endalert %}

## 前提条件

| 必要条件| 説明|
| ---| ---|
| [Infillion マネージャーアカウント](https://manager.gimbal.com/login/users/sign_in) | このパートナーシップを利用するには、Infillion のマネージャーアカウントが必要です。 |
|[Infillion Location SDK](https://docs.gimbal.com/index.html) | Infillion Location SDK は、近接ビーコンとジオフェンスを使用したマクロおよびミクロの位置情報ベースのモバイル機能を提供し、アプリユーザーとのコミュニケーション効果を上げます。SDK を実装し、ジオフェンス (またはビーコン) を設定しておく必要があります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDKの統合

Braze と Infillion を統合するには、Infillion Location SDK を実装し、Infillion マネージャーアカウントを作成する必要があります。Android、FireOS、iOS 向けの以下の統合では、ユーザーが入る新しい場所ごとに固有のカスタムイベントが作成されます。これらのイベントをキャンペーンやキャンバスでのトリガーやリターゲティングに使用できます。

50以上の場所を作成することが予想される場合は、一般的な`Places Entered` カスタムイベントを作成し、イベントプロパティとして場所名を追加することを推奨する。 

1. [Infillion ドキュメント](https://docs.gimbal.com/)の手順に従って [Infillion SDK](https://manager.gimbal.com/sdk_downloads) for Android and iOS をアプリに統合します。
2. Infillion の [place REST API](https://docs.gimbal.com/rest.html) を使って、ユーザー `places` を取得します。
3. Braze [REST API キー](https://manager.gimbal.com/apps)を入力して、Infillion アカウントを Braze にリンクします。
4. Braze SDKで[カスタムイベントを]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)設定する。Infillion を Braze に統合して [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) および [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons) に使用できます。
5. これらのイベントのログ・プロパティ（場所名、滞留時間）。
6. Brazeでキャンペーンやキャンバスをトリガーするには、これらのプロパティとイベントを使用する。 

