---
nav_title: 매뉴얼
article_title: 수동 통합 옵션 iOS용
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS용 Braze SDK를 수동으로 통합하는 방법을 보여줍니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 수동 통합

{% alert tip %}
SDK를 [스위프트 패키지 매니저](../swift_package_manager/), [CocoaPods](../cocoapods/), 또는 [Carthage](../carthage_integration/)와 같은 패키지 매니저를 통해 구현할 것을 강력히 권장합니다. 그러면 많은 시간을 절감하고 프로세스의 많은 부분을 자동화할 수 있습니다. 그러나 그렇게 할 수 없는 경우 지침을 따라 통합을 수동으로 완료할 수 있습니다.
{% endalert %}

## 1단계: Braze SDK 다운로드 중

### 옵션 1: 동적 XCFramework

1. `Appboy_iOS_SDK.xcframework.zip`을(를) [릴리스 페이지](https://github.com/appboy/appboy-ios-sdk/releases)에서 다운로드하여 파일을 추출하십시오.
2. Xcode에서 이 `.xcframework`을(를) 프로젝트에 드래그 앤 드롭하세요.
3. 프로젝트의 **일반** 탭에서 **임베드 및 서명**을 선택하여 `Appboy_iOS_SDK.xcframework`을(를) 선택합니다.

### 옵션 2: 정적 통합을 위한 정적 XCFramework

1. `Appboy_iOS_SDK.zip`을(를) [릴리스 페이지](https://github.com/appboy/appboy-ios-sdk/releases)에서 다운로드하십시오.<br><br>
2. Xcode의 프로젝트 탐색기에서 Braze에 대한 대상 프로젝트 또는 그룹을 선택합니다<br><br>
3. **파일 > 파일 추가 > 프로젝트_이름**로 이동합니다.<br><br>
4. `AppboyKit` 및 `AppboyUI` 폴더를 그룹으로 프로젝트에 추가하십시오.
	- **대상 그룹의 폴더에 항목 복사** 옵션이 처음 통합하는 경우 선택되어 있는지 확인합니다. 파일 선택기에서 **옵션**을 확장하여 **필요한 경우 항목 복사** 및 **그룹 생성**을 선택합니다.
	- `AppboyKit/include` 및 `AppboyUI/include` 디렉터리를 삭제하십시오.<br><br>
5. (선택 사항) 다음 중 하나가 적용되는 경우:
  - SDK의 핵심 분석 기능만 원하고 UI 기능(예: 인앱 메시지 또는 콘텐츠 카드)은 사용하지 않으려고 합니다.
  - 귀하는 Braze UI 기능에 대한 커스텀 UI를 가지고 있으며 이미지 다운로드를 직접 처리합니다.<br><br>SDK의 핵심 버전은 `ABKSDWebImageProxy.m` 및 `Appboy.bundle` 파일을 제거하여 사용할 수 있습니다. 그러면 `SDWebImage` 프레임워크 종속성과 모든 UI 관련 리소스(예: Nib 파일, 이미지, 현지화 파일)가 SDK에서 제거됩니다.

{% alert warning %}
SDK의 핵심 버전을 Braze UI 기능 없이 사용하려고 하면, 인앱 메시지가 표시되지 않습니다. 핵심 버전에서 Braze 콘텐츠 카드 UI를 표시하려고 하면 예측할 수 없는 동작이 발생합니다.
{% endalert %}

## 2단계: 필요한 iOS 라이브러리 추가

1. 왼쪽 탐색을 사용하여 프로젝트의 대상을 클릭하고 **구축 단계** 탭을 선택합니다.<br><br>
2. 클릭 <i class="fas fa-plus"></i> 버튼 under **Link Binary With Libraries**.<br><br>
3. 메뉴에서 `SystemConfiguration.framework`을 선택하세요.<br><br>
4. `SystemConfiguration.framework` 옆의 풀다운 메뉴를 사용하여 이 라이브러리를 필수로 표시하십시오.<br><br>
5. 다음 필수 프레임워크를 프로젝트에 추가하고 각 프레임워크를 '필수'로 표시합니다.
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. 다음 프레임워크를 추가하고 선택 사항으로 표시하십시오:
	- `CoreTelephony.framework`<br><br>
7. **구축 설정** 탭을 선택하십시오. **링킹** 섹션에서 **기타 링커 플래그** 설정을 찾아 `-ObjC` 플래그를 추가합니다.<br><br>
8. `SDWebImage` 프레임워크는 콘텐츠 카드 및 인앱 메시징이 제대로 작동하는 데 필요합니다. `SDWebImage`는 GIF를 포함하여 이미지를 다운로드 및 표시하는 데 사용됩니다. 콘텐츠 카드 또는 인앱 메시지를 사용하려면 SDWebImage 통합 단계를 수행합니다.

### SDWebImage 통합

`SDWebImage`를 설치하려면 [지침](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework)을 따르고 결과로 생성된 `XCFramework`를 프로젝트에 끌어 놓습니다.

### 선택적 위치 추적

1. `CoreLocation.framework`을(를) 추가하여 위치 추적을 활성화합니다.
2. 사용자의 앱에서 `CLLocationManager`을(를) 사용하여 위치를 승인해야 합니다.

## 3단계: Objective-C 브리징 헤더

{% alert note %}
프로젝트에서 Objective-C만 사용하는 경우 이 단계를 건너뛰십시오.
{% endalert %}

프로젝트에서 Swift를 사용하는 경우 브리징 헤더 파일이 필요합니다.

브리징 헤더 파일이 없는 경우 **File > New > File > (iOS or OS X) > Source > Header File**을 선택하여 `your-product-module-name-Bridging-Header.h`이라는 이름으로 새로 만드십시오. 그런 다음, 다음 코드 줄을 브리징 헤더 파일의 맨 위에 추가합니다.
```
#import "AppboyKit.h"
```

프로젝트의 **구축 설정**에서 헤더 파일의 상대 경로를 `Objective-C Bridging Header` 구축 설정의 `Swift Compiler - Code Generation` 아래에 추가합니다.

## 다음 단계

[통합을 완료하려면]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/) 지침을 따르세요.
