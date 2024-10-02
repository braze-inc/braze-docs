---
nav_title: アプテリジェント
article_title: アプテリジェント
alias: /partners/apteligent/
description: "この参考記事では、BrazeとApteligentのパートナーシップについて概説している。Apteligentは、クラッシュ報告の詳細を提供するモバイル・アプリケーションで、重要なデータを既存のBrazeソリューションに記録することができる。"
page_type: partner
search_tag: Partner

---

# アプテリジェント

> [Apteligentは](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html)モバイル・アプリケーション・パフォーマンス・プラットフォームで、開発者やプロダクト・マネージャーにツールと洞察を提供している。 

BrazeとApteligentの統合は、詳細なiOSクラッシュレポートを提供し、重要なデータを既存のBrazeソリューションに記録するだけでなく、アプリケーションのクラッシュを経験したユーザーをセグメント化し、理解し、エンゲージすることを可能にする。

## 前提条件 

| 必要条件 | 説明 |
|---|---|
| テストドライブアカウント | このパートナーシップを利用するには、テストドライブのアカウントが必要だ。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
この統合は現在iOSでのみサポートされている。
{% endalert %}

## 統合 {#apteligent-ios-integration}

### ステップ1:オブザーバーを登録する

まず、オブザーバーを登録しなければならない。これは、Apteligentを初期化する前に行っておくこと。

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### ステップ2:カスタム・クラッシュ解析を記録する

Apteligent SDKは、クラッシュが発生した後、ユーザーがアプリケーションをロードすると通知を発する。通知には、クラッシュの名称、理由、発生日が記載される。

通知を受信したら、カスタムクラッシュイベントを記録し、Apteligentのクラッシュレポート分析でユーザー属性を更新する：

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

完了すれば、Apteligentプラットフォームにあるクラッシュ情報を使って、Brazeのセグメンテーションとエンゲージメント分析のパワーを活用できるようになる。