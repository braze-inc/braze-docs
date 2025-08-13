---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "이 참조 문서에서는 기존 Braze 솔루션에 중요한 데이터를 기록할 수 있도록 충돌 보고를 자세히 설명하는 모바일 애플리케이션인 Apteligent와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html)는 개발자와 제품 매니저를 위한 툴 및 인사이트를 제공하는 모바일 애플리케이션 성능 플랫폼입니다. 

_이 통합은 앱텔리전트에서 유지 관리합니다._

## 통합 정보

Braze와 Apteligent의 통합을 통해 상세한 iOS 충돌 보고 기능을 제공하므로 중요한 데이터를 기존 Braze 솔루션에 기록할 뿐만 아니라 애플리케이션 충돌을 경험한 사용자를 세분화하고, 파악하며, 참여시킬 수 있습니다.

## 전제 조건 

| 요구 사항 | 설명 |
|---|---|
| TestDrive 계정 | 이 파트너십을 이용하려면 TestDrive 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
이 통합 기능은 현재 iOS에서만 지원됩니다.
{% endalert %}

## 통합 {#apteligent-ios-integration}

### 1단계: 참관인 등록하기

먼저 참관인을 등록해야 합니다. 이 작업은 Apteligent를 초기화하기 전에 수행해야 합니다.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### 2단계: 사용자 지정 충돌 분석 로그

충돌이 발생한 후 사용자가 애플리케이션을 로드하면 Apteligent SDK에서 알림을 표시합니다. 알림에는 충돌 이름, 이유, 발생 날짜 등이 포함되어 있습니다.

알림을 받으면 Apteligent의 충돌 보고 분석으로 커스텀 충돌 이벤트를 기록하고 사용자 속성을 업데이트합니다.

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

완료되면 Apteligent 플랫폼에서 찾은 충돌 정보를 사용하여 Braze의 강력한 세분화 및 인게이지먼트 분석을 활용할 수 있습니다.

