---
nav_title: Apteligent
article_title:アプテリジェント
alias: /partners/apteligent/
description:この記事は、クラッシュレポートを詳細に記述するモバイルアプリケーションであるApteligentとBrazeのパートナーシップを概説しており、既存のBrazeソリューションに重要なデータを記録することができます。
page_type: partner
search_tag:Partner

---

# アプテリジェント

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) は、開発者とプロダクトマネージャーにツールと洞察を提供するモバイルアプリケーションパフォーマンスプラットフォームです。 

BrazeとApteligentの統合により、詳細なiOSクラッシュレポートが提供され、既存のBrazeソリューションに重要なデータを記録することができるだけでなく、アプリケーションクラッシュを経験したユーザーをセグメント化、理解、エンゲージすることができます。

## 前提条件 

| 要件 | 説明 |
|---|---|
| テストドライブアカウント | このパートナーシップを利用するには、TestDriveアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
この統合は現在iOSでのみサポートされています。
{% endalert %}

## 統合 {#apteligent-ios-integration}

### ステップ1:オブザーバーを登録する

まず、オブザーバーを登録する必要があります。Apteligentを初期化する前にこれを行うことを確認してください。

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### ステップ2:カスタムクラッシュ分析を記録する

Apteligent SDKは、クラッシュが発生した後にユーザーがアプリケーションをロードすると通知を発行します。通知には、クラッシュ名、理由、および発生日時が含まれます。

通知を受け取ると、カスタムクラッシュイベントを記録し、Apteligentのクラッシュレポート分析でユーザー属性を更新します。

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

完了すると、Apteligentプラットフォームで見つかったクラッシュ情報を使用して、Brazeのセグメンテーションとエンゲージメント分析の力を活用できるようになります。