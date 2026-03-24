---
page_order: 10
nav_title: 버전 관리
article_title: Braze SDK 버전 관리 정보
description: "Braze SDK의 버전 관리에 대해 알아보세요."
---

# 버전 관리 정보

> 앱이 최신 기능과 품질 개선 사항을 반영하여 최신 상태를 유지할 수 있도록 Braze SDK의 버전 관리에 대해 알아보세요. 이전 버전의 SDK는 최신 패치, 버그 수정 또는 고객지원을 받지 못할 수 있으므로, 지속적인 개발 라이프사이클의 일부로 항상 최신 상태를 유지하는 것이 좋습니다.

## 버전 관리 권장 사항

모든 Braze SDK는 [시맨틱 버전 관리 사양(SemVer)](https://semver.org/)을 준수하므로, 버전 번호 `MAJOR.MINOR.PATCH`가 주어지면 다음을 권장합니다:

|버전|이 버전 정보|권장 사항|
|-------|------------------|--------------|
| `PATCH` | 업데이트는 항상 하위 호환성을 유지하며, 중요한 버그 수정이 포함됩니다. 항상 안전합니다. | 현재 사용 중인 메이저 및 마이너 버전의 최신 패치 버전으로 항상 즉시 업데이트해야 합니다. |
| `MINOR` | 업데이트는 항상 하위 호환성을 유지하며, 새로운 기능을 포함합니다. 애플리케이션 코드를 변경할 필요가 없습니다. | 즉시 수행할 필요는 없지만, 현재 사용 중인 메이저 버전의 최신 마이너 버전으로 가능한 한 빨리 업데이트해야 합니다. 
| `MAJOR` | 업데이트는 호환성을 깨뜨리는 변경 사항이며, 애플리케이션 코드를 변경해야 할 수 있습니다. | 코드 변경이 필요할 수 있으므로, 팀에 가장 적합한 일정에 맞춰 최신 메이저 버전으로 업데이트하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
때때로 새로운 Android 또는 Apple OS 업데이트로 인해 Braze SDK를 변경해야 하는 경우가 있습니다. 앱이 최신 기기와 호환되도록 하려면 SDK를 최신 상태로 유지하는 것이 중요합니다.
{% endalert %}

## 새 릴리스 알림 받기

새 SDK 버전이 릴리스될 때 자동으로 알림을 받으려면 Braze SDK의 GitHub 리포지토리를 구독하면 됩니다:

1. SDK의 GitHub 리포지토리로 이동합니다(예: [braze-android-sdk](https://github.com/braze-inc/braze-android-sdk), [braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk) 또는 [braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)).
2. 오른쪽 상단의 **Watch**를 클릭합니다.
3. **Custom**을 클릭한 다음 **Releases**를 선택하고 **Apply**를 클릭합니다.

새 릴리스가 게시될 때마다 GitHub 알림(및 [알림 설정](https://github.com/settings/notifications)에 따라 이메일)을 받게 됩니다. SDK 리포지토리의 전체 목록은 [참조, 리포지토리 및 샘플 앱]({{site.baseurl}}/developer_guide/references/)을 확인하세요.

## 알려진 문제 정보

변경 사항으로 인해 빌드 파이프라인이 손상되지 않도록 하기 위해, 특정 릴리스에 알려진 문제가 있더라도 **배포 시스템에 게시된 후에는 릴리스를 변경하거나 제거하지 않습니다**.

이러한 경우 [Braze SDK 체인지로그]({{site.baseurl}}/developer_guide/changelogs/)에 해당 문제를 문서화한 다음, 영향을 받는 메이저 또는 마이너 버전에 대한 새 패치를 최대한 빨리 릴리스합니다.