---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "この参考記事では、BrazeとGimbalのパートナーシップについて概説しており、位置情報を利用したマーケティングの関連性を完璧なものにすることができる。"
page_type: partner
search_tag: Partner

---

# Gimbal

> [ジンバルは](https://gimbal.com/)、位置情報を使ってマーケティングの関連性を完璧にすることを可能にする。同社の位置情報SDKは、ジオフェンシング・ソフトウェアやビーコンと組み合わせることで、関連性が高く、パーソナライズされた、近接を意識したモバイル体験を提供する。

ビーコンやジオフェンスサポートをBrazeのターゲティングやメッセージング機能と組み合わせることで、ユーザーの物理的な行動を詳しく知り、それに応じてメッセージを送ることができる。このパートナーシップの統合によって、さまざまな使用例が可能になる：
- **マーケティングだ：**文脈に関連したメッセージを送り、体験型の消費者ジャーニーを構築する。
- **競合分析：**消費者の傾向やパターンを理解するために、競合する場所の周辺にトリガーを設定する。
- **オーディエンス・インサイト**ユーザーの訪問行動を理解し、それらの学習に基づいてさらにセグメント化する。

## 前提条件

| 必要条件| 説明|
| ---| ---|
| [ジンバル・マネージャー・アカウント][1] | このパートナーシップを利用するには、ジンバル・マネージャーのアカウントが必要である。 |
|[ジンバル・ロケーションSDK](https://docs.gimbal.com/index.html) | Gimbal Location SDKは、近接ビーコンとジオフェンスを使用したマクロおよびミクロの位置情報ベースのモバイル体験を提供し、アプリのユーザーとより効果的なコミュニケーションを可能にする。SDKを実装し、ジオフェンス（またはビーコン）を設定する必要がある。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## SDKの統合

BrazeとGimbalを統合するには、Gimbal Location SDKを実装し、Gimbal managerアカウントを作成する必要がある。Android、FireOS、iOS用の以下の統合は、ユーザーが新しい場所に入るたびにユニークなカスタムイベントを作成し、これらのイベントは、キャンペーンやキャンバスでトリガーやリターゲティングに使用することができる。

50以上の場所を作成することが予想される場合は、一般的な`Places Entered` カスタムイベントを作成し、イベントプロパティとして場所名を追加することを推奨する。 

1. [ジン][2] [バルのドキュメントの][3]指示に従って、AndroidとiOS用の[ジンバルSDKを][2]アプリに統合する。
2. Gimbal's[place REST APIを使って][4]、ユーザー`places` を取得する。
3. Braze[REST APIキーを][5]入力して、GimbalアカウントをBrazeにリンクする。
4. Braze SDKで[カスタムイベントを][6]設定する。ジンバルは[Android、FireOS][7]、[iOS][8]用のBrazeと統合できる。
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