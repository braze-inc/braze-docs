---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "このリファレンス記事では、Braze と Apteligent のパートナーシップについて説明します。Apteligent は、詳細なクラッシュレポートを作成するモバイルアプリケーションであり、重要なデータを既存の Braze ソリューションに記録できるようにします。"
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) は、開発者と製品マネージャーにツールとインサイトを提供するモバイルアプリケーションパフォーマンスプラットフォームです。 

_この統合は Apteligent によって管理されます。_

## 統合について

BrazeとApteligentの統合は、詳細なiOSクラッシュレポートを提供し、重要なデータを既存のBrazeソリューションに記録するだけでなく、アプリケーションのクラッシュを経験したユーザーをセグメント化し、理解し、エンゲージすることを可能にする。

## 前提条件 

| 必要条件 | 説明 |
|---|---|
| TestDrive アカウント | このパートナーシップを活用するには、TestDrive アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
この統合は現在iOSでのみサポートされている。
{% endalert %}

## 統合 {#apteligent-ios-integration}

### ステップ1:オブザーバーを登録する

最初にオブザーバーを登録する必要があります。Apteligent を初期化する前に、この登録が完了していることを確認してください。

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### ステップ2:カスタムクラッシュ分析を記録する

Apteligent SDK は、クラッシュが発生した後、ユーザーがアプリケーションをロードしたときに通知を発行します。通知には、クラッシュの名前、理由、発生日が含まれます。

通知を受け取ったら、カスタムクラッシュイベントをログに記録し、Apteligent のクラッシュレポート分析を使用してユーザー属性を更新します。

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

