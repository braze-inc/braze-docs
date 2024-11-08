---
nav_title: 수동 통합
article_title: iOS용 수동 통합
platform: Swift
page_order: 3
description: "이 참조 문서에서는 수동 설치를 사용하여 Braze Swift SDK를 통합하는 방법을 설명합니다."
toc_headers: "h2"
---

# 수동 통합

> [스위프트 패키지 매니저]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) 또는 [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/)와 같은 패키지 매니저에 액세스할 수 없는 경우, 대신 Swift SDK를 수동으로 통합할 수 있습니다.

## 1단계: Braze SDK 다운로드

[GitHub의 Braze SDK 릴리스 페이지](https://github.com/braze-inc/braze-swift-sdk/releases)로 이동한 다음, `braze-swift-sdk-prebuilt.zip`을 다운로드합니다.

!['GitHub의 Braze SDK 릴리스 페이지.']({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## 2단계: 프레임워크 선택

Braze Swift SDK에는 다양한 독립형 XCFrameworks가 포함되어 있어 모든 기능을 통합할 필요 없이 원하는 기능을 자유롭게 통합할 수 있습니다. 다음 표를 참조하여 XCFrameworks를 선택합니다.

| 패키지                    | 필수 항목인가요? | 설명                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | 예       | 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리입니다.                                                                                                                                                                                                                                             |
| `BrazeLocation`            | 아니요        | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리입니다.                                                                                                                                                                                                                                   |
| `BrazeUI`                  | 아니요        | 앱 내 메시지 및 콘텐츠 카드를 위한 Braze에서 제공하는 사용자 인터페이스 라이브러리입니다.                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | 아니요        | 리치 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. 이 라이브러리를 기본 애플리케이션 대상에 직접 추가하지 말고 [`BrazeNotificationService` 라이브러리를 별도로 추가](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)합니다.     |
| `BrazePushStory`           | 아니요        | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리입니다. 이 라이브러리를 기본 애플리케이션 대상에 직접 추가하지 말고 [`BrazePushStory` 라이브러리를 별도로 추가](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)합니다.                                     |
| `BrazeKitCompat`           | 아니요        | `Appboy-iOS-SDK` 버전 4.X.X에서 사용 가능했던 모든 `Appboy` 및 `ABK*` 클래스 및 메서드가 포함된 호환성 라이브러리. 사용법에 대한 자세한 내용은 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)의 최소 마이그레이션 시나리오를 참조하세요. |
| `BrazeUICompat`            | 아니요        | `Appboy-iOS-SDK` 버전 4.X.X부터 `AppboyUI` 라이브러리에서 사용 가능했던 모든 `ABK*` 클래스 및 메서드가 포함된 호환성 라이브러리. 사용법에 대한 자세한 내용은 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)의 최소 마이그레이션 시나리오를 참조하세요. |
| `SDWebImage`               | 아니요        | 최소 마이그레이션 시나리오에서 `BrazeUICompat` 에서만 사용하는 종속성입니다. |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 3단계: 파일 준비

**정적** XCFrameworks를 사용할지 **동적** XCFrameworks를 사용할지 결정한 다음, 파일을 준비합니다.

{% tabs %}
{% tab 동적 %}
1. XCFrameworks의 임시 디렉토리를 생성합니다.
2. `braze-swift-sdk-prebuilt`에서 `dynamic` 디렉토리를 열고 `BrazeKit.xcframework`를 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. 각 [선택한 XCFrameworks](#step-2-choose-your-frameworks)를 임시 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab 정적 %}
### 3.1단계: 프레임워크 준비

1. XCFrameworks의 임시 디렉토리를 생성합니다.
2. `braze-swift-sdk-prebuilt`에서 `static` 디렉토리를 열고 `BrazeKit.xcframework`를 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. 각 [선택한 XCFrameworks](#step-2-choose-your-frameworks)를 임시 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### 3.2단계: 번들 준비하기

1. 번들을 위한 임시 디렉토리를 생성합니다.
2. `bundles` 디렉토리를 열고 `BrazeKit.bundle`을 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. `BrazeLocation`, `BrazeUI`, `BrazeUICompat` 또는 `SDWebImage` XCFrameworks를 사용하는 경우 해당 번들을 임시 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
[준비한 프레임워크](#step-31-prepare-your-frameworks)에 대한 번들만 이동합니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 4단계: 프레임워크 통합

다음으로, [이전에 준비](#step-3-prepare-your-files)한 **동적** 또는 **정적** XCFrameworks를 통합합니다.

{% tabs %}
{% tab 동적 %}
Xcode 프로젝트에서 빌드 대상을 선택한 다음, **일반**을 선택합니다. **프레임워크, 라이브러리 및 임베디드 콘텐츠**에서 [이전에 준비한 파일](#step-3-prepare-your-files)을 끌어다 놓습니다.

!['각 Braze 라이브러리가 '임베드 및 서명'으로 설정된 예제 Xcode 프로젝트.']({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
GIF 지원을 활성화하려면 `braze-swift-sdk-prebuilt/dynamic`에 `SDWebImage.xcframework`를 추가합니다.
{% endalert %}
{% endtab %}

{% tab 정적 %}
Xcode 프로젝트에서 빌드 대상을 선택한 다음, **일반**을 선택합니다. **프레임워크, 라이브러리 및 임베디드 콘텐츠**에서 [이전에 준비한 프레임워크](#step-31-prepare-your-frameworks)를 끌어다 놓습니다. 각 프레임워크 옆에서 **임베드하지 않음**을 선택합니다. 

!['각 Braze 라이브러리가 '임베드하지 않음'으로 설정된 예제 Xcode 프로젝트.']({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
GIF 지원을 활성화하려면 `braze-swift-sdk-prebuilt/static`에 `SDWebImage.xcframework`를 추가합니다.
{% endalert %}

빌드 대상에서 **빌드 단계**를 선택합니다. **번들 리소스 복사**에서 [이전에 준비한 번들](#step-32-prepare-your-bundles)을 끌어다 놓습니다.

![''번들 리소스 복사' 아래에 번들이 추가된 예제 Xcode 프로젝트.']({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Objective-C 프로젝트의 일반적인 오류

Xcode 프로젝트에 Objective-C 파일만 포함된 경우 프로젝트를 빌드하려고 할 때 '누락된 기호' 오류가 발생할 수 있습니다. 이러한 오류를 해결하려면 프로젝트를 열고 파일 트리에 빈 Swift 파일을 추가합니다. 그러면 빌드 툴체인에 [Swift 런타임](https://support.apple.com/kb/dl1998)이 강제로 임베드되고 빌드 시간 동안 적절한 프레임워크에 링크됩니다.

```bash
FILE_NAME.swift
```

`FILE_NAME` 을 띄어쓰기가 없는 문자열로 바꿉니다. 파일은 다음과 비슷하게 보일 것입니다:

```bash
empty_swift_file.swift
```
