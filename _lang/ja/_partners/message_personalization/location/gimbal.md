---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "この参考記事では、BrazeとGimbalのパートナーシップについて概説しており、位置情報を利用したマーケティングの関連性を完璧なものにすることができる。"
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/) は、位置情報データを活用して、適切なマーケティングのパーフェクトな実行を支援しています。同社の位置情報SDKは、ジオフェンシング・ソフトウェアやビーコンと組み合わせることで、関連性が高く、パーソナライズされた、近接を意識したモバイル体験を提供する。

ビーコンやジオフェンスサポートをBrazeのターゲティングやメッセージング機能と組み合わせることで、ユーザーの物理的な行動を詳しく知り、それに応じてメッセージを送ることができる。このパートナー連携により、次のようなさまざまなユースケースが可能になります。

- **マーケティング:**状況に対応した関連性のあるメッセージを送信し、体験型の消費者ジャーニーを構築します。
- **競合分析:**消費者の傾向やパターンを理解するために、競合ロケーション周辺にトリガーを設定します。
- **オーディエンスインサイト:**ユーザーの訪問行動を理解し、それらの学習に基づいてさらにセグメント化する。

{% alert note %}
この統合は、Gimbal ビーコンと Gimbal ジオフェンスソリューションでも同じように機能します。
{% endalert %}

## 前提条件

| 必要条件| 説明|
| ---| ---|
| [Gimbal マネージャーアカウント][1] | このパートナーシップを活用するには、Gimbal マネージャーアカウントが必要です。 |
|[Gimbal Location SDK](https://docs.gimbal.com/index.html) | Gimbal Location SDK は、近接ビーコンとジオフェンスを使用してマクロおよびミクロの位置情報ベースのモバイルエクスペリエンスを提供し、アプリのユーザーとのより効果的なコミュニケーションを可能にします。SDK を実装し、ジオフェンス (またはビーコン) を設定しておく必要があります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDKの統合

Braze と Gimbal を統合するには、Gimbal Location SDK を実装し、Gimbal マネージャーアカウントを作成する必要があります。Android、FireOS、iOS 向けの以下の統合では、ユーザーが入る新しい場所ごとに固有のカスタムイベントが作成されます。これらのイベントをキャンペーンやキャンバスでのトリガーやリターゲティングに使用できます。

50以上の場所を作成することが予想される場合は、一般的な`Places Entered` カスタムイベントを作成し、イベントプロパティとして場所名を追加することを推奨する。 

1. [Gimbal ドキュメント][3]の手順に従って [Gimbal SDK][2] for Android and iOS をアプリに統合します。
2. Gimbal's[place REST APIを使って][4]、ユーザー`places` を取得する。
3. Braze [REST API キー][5]を入力して、Gimbal アカウントを Braze にリンクします。
4. Braze SDKで[カスタムイベントを][6]設定する。[Android および FireOS][7] と [iOS][8] 向けに、Braze に Gimbal を統合できます。
5. これらのイベントのログ・プロパティ（場所名、滞留時間）。
6. Brazeでキャンペーンやキャンバスをトリガーするには、これらのプロパティとイベントを使用する。 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons