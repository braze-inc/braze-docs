---
nav_title: Gimbal
article_title:Gimbal
alias: /partners/gimbal/
description:この記事では、BrazeとGimbalの提携について説明し、位置情報を使用してマーケティングの関連性を完璧にする方法を紹介します。
page_type: partner
search_tag:Partner

---

# Gimbal

> [ジンバル](https://gimbal.com/)は、位置データを使用してマーケティングの関連性を完璧にすることができます。彼らの位置情報SDKは、ジオフェンシングソフトウェアとビーコンを組み合わせて、関連性があり、パーソナライズされた、近接認識モバイル体験を提供します。

Braze's targeting and messaging features to learn more about your user'の物理的なアクションとメッセージを組み合わせて、ビーコンやジオフェンスのサポートを組み合わせてください。このパートナーシップの統合により、次のようなさまざまなユースケースが開かれます:
- **Marketing:** コンテキストに関連するメッセージを送信し、体験的な消費者の旅を構築します。
- **競合分析:**競争の激しい場所の周りにトリガーを設定して、消費者の動向やパターンを理解します。
- **オーディエンスインサイト:**ユーザーの訪問行動を理解し、それらの学習に基づいてさらにセグメント化します。

## 前提条件

| 要件| 説明|
| ---| ---|
| [ジンバルマネージャーアカウント][1] | このパートナーシップを利用するには、ジンバルマネージャーアカウントが必要です。 |
|[ジンバルロケーションSDK](https://docs.gimbal.com/index.html) | Gimbal Location SDKは、近接ビーコンとジオフェンスを使用して、マクロおよびミクロの位置情報に基づくモバイル体験を提供し、アプリユーザーとより効果的にコミュニケーションを取ることができます。SDKを実装し、ジオフェンス（またはビーコン）を設定する必要があります。 |
| Braze REST API キー | `users.track` の権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## SDK統合

BrazeとGimbalを統合するには、Gimbal Location SDKを実装し、Gimbalマネージャーアカウントを作成する必要があります。Android、FireOS、およびiOSの次の統合は、ユーザーが新しい場所に入るたびに一意のカスタムイベントを作成します。これらのイベントは、キャンペーンやキャンバスでのトリガーおよびリターゲティングに使用できます。

50 以上の場所を作成する予定がある場合は、一般的な `Places Entered` カスタムイベントを作成し、場所の名前をイベントプロパティとして追加することをお勧めします。 

1. Gimbal SDK[をAndroidおよびiOSに統合し、Gimbalドキュメント[の指示に従ってアプリに統合します。][3]
2. Gimbal の [place REST API][4] を使用してユーザー `places` を取得します。
3. Brazeの[REST APIキー][5]を入力して、GimbalアカウントをBrazeにリンクします。
4. Braze SDKで[カスタムイベント][6]を設定します。GimbalをBrazeと統合して、[AndroidおよびFireOS][7]と[iOS][8]で使用できます。
5. これらのイベントのログプロパティ（場所名、滞在時間）。
6. これらのプロパティとイベントを使用して、Brazeでキャンペーンやキャンバスをトリガーします。 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons