## 언리얼 엔진 브레이즈 SDK 소개

Braze 언리얼 SDK 플러그인을 사용하면 가능합니다:

* 앱 또는 게임 내 세션 평가 및 추적
* 인앱 구매 및 맞춤 이벤트 추적
* 표준 및 사용자 지정 속성으로 사용자 프로필 업데이트하기
* 푸시 알림 보내기
* 언리얼 앱을 더 큰 캔버스 여정에 통합
* 인앱 행동을 기반으로 이메일 또는 SMS와 같은 크로스채널 메시징 발송

## 언리얼 엔진 SDK 통합

### 1단계: Braze 플러그인 추가

터미널에서 [언리얼 엔진 브레이즈 SDK GitHub 리포지토리를](https://github.com/braze-inc/braze-unreal-sdk) 복제합니다.

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

그런 다음 `BrazeSample/Plugins/Braze` 디렉토리를 복사하여 앱의 플러그인 폴더에 추가합니다.

### 2단계: 플러그인 활성화

C++ 또는 블루프린트 프로젝트에 플러그인을 활성화합니다.

{% tabs %}
{% tab C++ %}
C++ 프로젝트의 경우 Braze 모듈을 참조하도록 모듈을 구성하세요. `\*.Build.cs file` 에서 `"Braze"` 을 `PublicDependencyModuleNames` 에 추가합니다.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab 블루프린트 %}
블루프린트 프로젝트의 경우 **설정** > **플러그인으로** 이동한 다음 **Braze** 옆의 **Enabled에** 체크합니다.

![활성화 플러그인]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### 3단계: API 키와 엔드포인트 설정

프로젝트의 `DefaultEngine.ini` 에서 API 키와 엔드포인트를 설정하세요.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Android SDK 31+ 대상 프로젝트의 경우 언리얼은 Android 12+ 디바이스에서 설치 도중 INSTALL_PARSE_FAILED_MANIFEST_MALFORMED 오류와 함께 실패하는 빌드를 생성합니다. 이 문제를 해결하려면 이 저장소의 루트에서 `UE4_Engine_AndroidSDK_31_Build_Fix.patch` git 패치 파일을 찾아 언리얼 소스 빌드에 적용하세요.
{% endalert %}

## 선택적 구성

### 로깅

{% tabs local %}
{% tab Android %}
런타임에 C++를 사용하거나 블루프린트 노드에서 로그 레벨을 설정할 수 있습니다.

{% subtabs %}
{% subtab C++ %}
런타임에 로그 수준을 설정하려면 `UBrazeSubsystem::AndroidSetLogLevel` 으로 전화하세요.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
블루프린트에서 **안드로이드 세트 로그 레벨** 노드를 사용할 수 있습니다:

![블루프린트의 안드로이드 세트 로그 레벨 노드.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Braze SDK 초기화를 호출할 때 로깅이 설정되도록 하려면 `InitializeBraze` 전에 이 함수를 호출하는 것이 좋습니다.
{% endtab %}

{% tab iOS %}
`info.plist` 에서 로그 수준을 활성화하려면 **설정** > **프로젝트 설정으로** 이동한 다음 **플랫폼에서** **iOS를** 선택합니다. **추가** 목록 데이터에서 **추가 목록 데이터를** 찾은 다음 로그 레벨을 입력합니다:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

기본 로그 수준은 최소 로깅 수준인 8입니다. 로그 수준에 대해 자세히 알아보세요: [기타 SDK 사용자 지정]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
