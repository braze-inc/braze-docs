## 언리얼 엔진 Braze 소프트웨어 개발 키트 소개

Braze 언리얼 소프트웨어 개발 키트 플러그인을 사용하면 가능합니다:

* 앱 또는 게임 내 세션 평가 및 추적
* 인앱 구매 및 맞춤 이벤트 추적
* 표준 및 사용자 지정 속성으로 사용자 프로필 업데이트하기
* 푸시 알림 보내기
* 언리얼 앱을 더 큰 캔버스 여정에 통합
* 인앱 행동을 기반으로 이메일 또는 SMS와 같은 크로스채널 메시징 발송

## 언리얼 엔진 SDK 통합하기

### 1단계: Braze 플러그인 추가하기

터미널에서 [언리얼 엔진 Braze 소프트웨어 개발 키트 GitHub 저장소를](https://github.com/braze-inc/braze-unreal-sdk) 복제합니다.

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

그런 다음 `BrazeSample/Plugins/Braze` 디렉토리를 복사하여 앱의 플러그인 폴더에 추가합니다.

### 2단계: 플러그인 인에이블먼트

C++ 또는 블루프린트 프로젝트에 플러그인을 인에이블먼트합니다.

{% tabs %}
{% tab C++ %}
C++ 프로젝트의 경우, 모듈이 Braze 모듈을 참조하도록 구성하세요. `\*.Build.cs file` 에서 `"Braze"` 을 `PublicDependencyModuleNames` 에 추가합니다.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab 블루프린트 %}
블루프린트 프로젝트의 경우 **설정** > **플러그인으로** 이동한 다음 **Braze** 옆의 **인에이블먼트에** 체크합니다.

![활성화 플러그인]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### 3단계: API 키와 엔드포인트 설정하기

프로젝트의 `DefaultEngine.ini` 에서 API 키와 엔드포인트를 설정하세요.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Android 소프트웨어 개발 키트 31 이상을 타겟팅하는 프로젝트의 경우 언리얼은 Android 12 이상 기기에 설치하는 동안 INSTALL_PARSE_FAILED_MANIFEST_MALFORMED 오류와 함께 실패하는 빌드를 생성합니다. 이 문제를 해결하려면 이 저장소의 루트에서 `UE4_Engine_AndroidSDK_31_Build_Fix.patch` git 패치 파일을 찾아 언리얼 소스 빌드에 적용하세요.
{% endalert %}

### 4단계: 소프트웨어 개발 키트 수동 초기화(선택 사항)

기본적으로 소프트웨어 개발 키트는 실행 시 자동으로 초기화됩니다. 사용자 동의를 기다리거나 로그 레벨을 설정하는 등 초기화에 대한 더 많은 제어를 원하는 경우 `DefaultEngine.ini` 에서 `AutoInitialize` 을 비활성화하고 C++ 또는 블루프린트에서 수동으로 초기화할 수 있습니다.

{% tabs %}
{% tab C++ %}
네이티브 C++에서는 BrazeSubsystem에 액세스하여 `InitializeBraze()` 을 호출하고 선택적으로 Engine.ini 설정을 재정의하는 컨피규어를 전달합니다.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab 블루프린트 %}
블루프린트에서는 블루프린트 노드와 동일한 기능에 액세스할 수 있습니다:  
`GetBrazeSubsystem` 노드를 사용하여 `Initialize` 노드를 호출합니다.  
선택적으로 블루프린트에서 BrazeConfig 오브젝트를 생성하여 다음 주소로 전달할 수 있습니다. `Initialize`

![초기화브레이즈]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}

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
블루프린트에서 **Android 설정 로그 레벨** 노드를 사용할 수 있습니다:

![블루프린트의 Android Set Log Level 노드입니다.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Braze 소프트웨어 개발 키트 초기화를 호출할 때 로깅이 설정되도록 하려면 `InitializeBraze` 전에 이 함수를 호출하는 것이 좋습니다.
{% endtab %}

{% tab iOS %}
`info.plist` 에서 로그 레벨을 인에이블먼트하려면 **설정** > **프로젝트 설정으로** 이동한 다음 **플랫폼에서** **iOS를** 선택합니다. **추가** 목록 데이터에서 **추가 목록 데이터를** 찾은 다음 로그 수준을 입력합니다:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

기본값 로그 수준은 최소 로깅인 8입니다. 로그 수준에 대해 자세히 알아보세요: [기타 소프트웨어 개발 키트 커스터마이징]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
