---
nav_title: 초기 SDK 설정
article_title: Windows 유니버설용 초기 SDK 설정
platform: Windows Universal
page_order: 0
description: "이 참조 설명서에서는 Windows 유니버설 플랫폼에서 Braze SDK를 통합하기 위한 초기 SDK 통합 단계를 다룹니다."
search_rank: 1
hidden: true
---

# 초기 SDK 통합
{% multi_lang_include archive/windows_deprecation.md %}

Braze SDK는 분석, 세분화 및 인게이지먼트에 사용할 정보를 보고하는 API와 푸시 및 알림 수신에 사용자를 등록할 수 있는 기능을 제공합니다.

>  Windows 유니버설 SDK는 Xamarin Windows 앱과도 호환됩니다.

## 1단계: NuGet 패키지 관리자를 통해 SDK를 설치합니다.

Windows 유니버설 SDK는 [NuGet 패키지 관리자][14]를 통해 설치됩니다. NuGet을 통해 Braze Windows SDK를 설치하려면:

1. 프로젝트 파일을 마우스 오른쪽 버튼으로 클릭합니다.
2. "NuGet 패키지 관리"를 클릭합니다.
3. 왼쪽 드롭다운 메뉴에서 '온라인'을 클릭합니다.
4. "NuGet.org"에서 "Appboy"를 검색합니다
5. "AppboyPlatform.Universal.Release" NuGet 패키지를 클릭하고 설치를 클릭합니다

>  Windows 유니버설 라이브러리는 모든 Windows 8.1, Windows Phone 8.1 및 UWP 애플리케이션에 사용해야 합니다.

## 2단계: AppboyConfiguration.xml의 생성 및 구성

프로젝트의 루트 디렉터리에 `AppboyConfiguration.xml` 이라는 파일을 만들고 해당 파일에 다음 코드 스니펫을 추가합니다:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 찾을 수 있는 API 키로 `YOUR_API_KEY_HERE`를 업데이트하세요.

스니펫을 추가한 후에는 `AppboyConfiguration.xml`의 파일 속성을 수정해야 합니다

1. `Build Action`을 `Content`로 설정
2. `Copy to Output Directory`를 `Copy Always`로 설정

## 3단계: package.appxmanifest 구성

'기능 탭에서 `Internet (Client)` 이 선택되어 있는지 확인합니다.
![][18]

## 4단계: 앱 클래스 편집

- `App.xaml.cs` 파일의 `usings` 에 다음을 추가합니다:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- `OnLaunched` 수명 주기 메서드 내에서 다음을 호출합니다:

```csharp
Appboy.SharedInstance.OpenSession();
```

- `OnSuspending` 수명 주기 메서드 내에서 다음을 호출합니다:

```csharp
Appboy.SharedInstance.CloseSession();
```

## 기본 SDK 통합 완료

이제 Braze가 애플리케이션에서 데이터를 수집하고 있을 것입니다. [속성]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/), [이벤트]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events) 및 [구매]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases)를 SDK에 기록하는 방법과 푸시 메시징을 계측하는 방법은 다음 문서를 참조하세요.

>  동일한 앱에서 Braze Unity 프로젝트를 사용하는 경우, 브레이즈 호출을 "AppboyPlatform.Universal.Appboy"로 완전히 인증해야 할 수 있습니다

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
