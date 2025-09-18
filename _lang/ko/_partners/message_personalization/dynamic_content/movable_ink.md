---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "이 참조 문서에서는 고객을 이전하는 매력적이고 고유한 시각적 경험을 구축하는 방법을 디지털 마케터에게 제공하는 클라우드 소프트웨어 플랫폼인 Movable Ink와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/)는 고객을 이전하는 매력적이고 고유한 시각적 경험을 구축하는 방법을 디지털 마케터에게 제공하는 클라우드 소프트웨어 플랫폼입니다. Movable Ink 플랫폼은 캠페인에 쉽게 삽입할 수 있는 중요한 사용자 지정 옵션을 제공합니다. 

_이 통합은 이동식 잉크에 의해 유지됩니다._

## 통합 정보

투표, 카운트다운 타이머, 스크래치 오프 등 Movable Ink의 인텔리전트 크리에이티브 기능을 활용하여 크리에이티브 역량을 확장하세요. Movable Ink와 Braze 통합은 데이터 중심의 동적 메시지에 대한 보다 균형 잡힌 접근 방식을 제공하여 사용자에게 중요한 것들에 대한 실시간 요소를 제공합니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Movable Ink 계정 | 이 파트너십을 활용하려면 Movable Ink 계정이 필요합니다. |
| 데이터 소스 | 데이터 소스를 Movable Ink에 연결해야 합니다. 이는 CSV, 웹사이트 가져오기 또는 API를 통해 수행할 수 있습니다. Braze와 Movable Ink 간에 통합 식별자(예: `external_id`)를 사용하여 데이터를 전달해야 합니다.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

- 개인화된 월별 또는 연말 요약.
- 마지막으로 알려진 행동에 따라 이메일, 푸시 또는 리치 알림용 이미지를 동적으로 개인화합니다.<br>
	예를 들어, 다음과 같습니다. 
	- 리치 푸시 메시지를 사용하여 API에서 데이터를 가져와 이벤트 스케줄을 동적으로 생성할 수 있습니다. 
	- 카운트다운 타이머를 사용하여 대규모 세일(예: 블랙 프라이데이, 발렌타인데이, 홀리데이 딜)이 다가오는 시점을 사용자에게 알립니다.
	- 스크래치 오프 기능을 사용하여 재미있는 인터랙티브한 방식으로 프로모션 코드를 지급할 수 있습니다.

## 지원되는 Movable Ink 기능

인텔리전트 크리에이티브에는 Braze 사용자가 활용할 수 있는 다양한 오퍼링이 있습니다. 다음 목록은 지원되는 기능을 보여줍니다. 

| Movable Ink 기능 | 기능 | 리치 푸시 알림 | 인앱 메시징/콘텐츠 카드/이메일 | 세부 정보 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| 크리에이티브 옵티마이저 | A/B 콘텐츠 표시 | ✗ | ✔ | |
|| 최적화 | ✗ | ✔* | \* 반드시 Branch의 딥링킹 솔루션을 사용해야 함 |
| 타겟팅 규칙 | 날짜 | ✔* | ✔ | \* 푸시 알림은 수신 시 캐시되고 새로 고치치 않으므로 지원되지만 권장되지는 않습니다. |
|| 요일 | ✔* | ✔ | \* 푸시 알림은 수신 시 캐시되고 새로 고치치 않으므로 지원되지만 권장되지는 않습니다. |
|| 하루 중 시간 | ✔* | ✔ | \* 푸시 알림은 수신 시 캐시되고 새로 고치치 않으므로 지원되지만 권장되지는 않습니다. |
| 스토리/행동 활동 | | ✔* | ✔* | \* Braze에 사용되는 고유 사용자 식별자는 ESP의 식별자에 연결되어야 함 |
| 앱 내 딥링킹 | | ✔* | ✔* | \* 고객에게 간소화된 경험을 제공하려면 Branch를 통해 이미 구축된 딥링킹 솔루션을 사용하거나, Movable Ink의 고객 경험 팀과 함께 검증된 솔루션을 사용합니다. |
| 앱 | 카운트다운 타이머 | ✔* | ✔ | \* 푸시 알림은 수신 시 캐시되고 새로 고치치 않으므로 지원되지만 권장되지는 않습니다. |
|| 투표 | ✗ | ✔* | \* 투표 후 앱이 모바일 랜딩 페이지로 전환됨 |
|| 스크래치 오프 | ✔* | ✔* | \* 클릭 시 스크래치 오프 경험을 위해 앱에서 종료됨 |
|| 비디오 | ✔* | ✔* | \* 애니메이션 GIF만 해당, <br>Android의 경우, Braze는 구현에 [GIF 지원][GIFsupport]을 포함해야 함 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

### 1단계: Movable Ink용 데이터 소스 생성

고객은 CSV, 웹사이트 가져오기 또는 API 통합이 가능한 데이터 소스를 생성해야 합니다.

![표시되는 다양한 데이터 소스 옵션: CSV 업로드, 웹사이트 또는 API 통합.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs 로컬 %}
{% tab CSV 데이터 소스 %}
- **CSV 데이터 소스**: 각 행에는 적어도 하나의 세그먼트 열과 하나의 콘텐츠 열이 있어야 합니다. CSV를 업로드한 후 콘텐츠를 타겟팅하는 데 사용해야 하는 열을 선택합니다. [예제 CSV 파일]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![데이터 소스로 'CSV'를 선택하면 표시되는 필드.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab 웹사이트 데이터 소스 %}
- **웹사이트 데이터 소스**: 각 행에는 적어도 하나의 세그먼트 열과 하나의 콘텐츠 열이 있어야 합니다. CSV를 업로드한 후 콘텐츠를 타겟팅하는 데 사용해야 하는 열을 선택합니다.
  - 이 프로세스 내에서 다음을 매핑해야 합니다.
    - 세그먼트로 사용할 필드
    - 크리에이티브에서 동적으로 개인화할 수 있는 데이터 필드로 원하는 필드(예: 사용자 속성 또는 이름, 성, 도시 등과 같은 커스텀 속성)

![데이터 소스로 '웹사이트'를 선택하면 표시되는 필드.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API 통합 %}
- **API 통합**: 회사의 API를 사용하여 API 응답에서 직접 콘텐츠를 지원합니다.

![데이터 소스로 'API 통합'을 선택하면 표시되는 필드]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### 2단계: Movable Ink 플랫폼에서 캠페인 생성

Movable Ink 홈 화면에서 캠페인을 생성합니다. HTML 이미지의 이메일 또는 푸시, 인앱 메시지, 콘텐츠 카드(제안됨) 등 모든 채널에서 사용할 수 있는 블록 중에서 선택할 수 있습니다.
또한 블록을 통해 제공되는 다양한 콘텐츠 옵션도 살펴보는 것이 좋습니다.

![새 Movable Ink 캠페인을 생성할 때 Movable Ink 플랫폼의 모습을 보여주는 이미지.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink에는 텍스트, 이미지 등의 요소를 끌어서 놓을 수 있는 간편한 편집기가 있습니다. 데이터 소스를 채운 경우 데이터 속성정보를 사용하여 이미지를 동적으로 생성할 수 있습니다. 또한 캠페인이 전송되었는데 사용자가 개인화 기준에 맞지 않는 경우 이 흐름 내에서 사용자를 위한 대체 항목을 생성할 수도 있습니다.

![다양한 사용자 지정 가능한 요소를 보여주는 Movable Ink 블록 편집기.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

캠페인을 완료하기 전에 동적 이미지를 미리 보고 쿼리 매개변수를 테스트하여 이미지가 어떻게 표시되는지 확인합니다. 완료되면 Braze에 삽입할 수 있는 동적 URL이 생성됩니다!

Movable Ink 플랫폼 사용 방법에 대한 자세한 내용은 [Movable Ink 지원 센터][support]를 참조하세요.

### 3단계: Movable Ink 콘텐츠 URL 확보

Movable Ink 콘텐츠를 Braze 메시지에 포함하려면 Movable Ink에서 제공한 소스 URL을 찾아야 합니다. 

소스 URL을 얻으려면 Movable Ink 대시보드에서 콘텐츠를 설정한 다음, 여기에서 콘텐츠를 완성하고 내보내야 합니다. **완료** 페이지에서 크리에이티브 태그의 소스 URL(`img src`)을 복사합니다.

![Movable Ink 캠페인을 완료한 후 표시되는 페이지. 여기에서 콘텐츠 URL을 찾을 수 있습니다.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

그런 다음, Braze 플랫폼에서 해당 필드에 URL을 붙여넣습니다. 메시징 채널에 적합한 필드는 4단계에서 찾을 수 있습니다. 마지막으로, 병합 태그(예: {% raw %}```&mi_u=%%email%%```{% endraw %})를 해당 Liquid 변수(예: {% raw %}```&mi_u={{${email_address}}}```{% endraw %})로 바꿉니다.

### 4단계: Braze 경험

{% tabs 로컬 %}
{% tab 이메일 %}
Braze 플랫폼에서 이메일 본문에 크리에이티브 태그를 붙여넣습니다.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab 푸시 알림 %}

1. Braze 플랫폼에서 다음을 수행합니다.
	- Android 푸시: **푸시 아이콘 이미지** 및 **확장된 알림 이미지** 필드에 URL을 붙여넣습니다.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS 푸시: **미디어** 링크 필드에 URL을 붙여넣고 사용 중인 파일 형식을 표시합니다.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- 웹 푸시: **푸시 아이콘 이미지** 및 **큰 알림 이미지** 필드에 URL을 붙여넣습니다.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 이미지가 캐시되지 않도록 하려면 메시지의 URL 앞에 빈 Liquid 태그를 추가합니다. <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab 인앱 메시지 %}

1. Braze 플랫폼에서 **리치 알림 미디어** 필드에 URL을 붙여넣습니다.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. 캐싱을 방지하도록 고유한 URL을 제공합니다. Movable Ink의 실시간 이미지가 작동하고 캐싱의 영향을 받지 않는지 확인하려면 Liquid를 사용하여 Movable Ink 이미지 URL 끝에 타임스탬프를 추가합니다.

이렇게 하려면 다음 구문을 사용하여 필요에 따라 이미지 URL을 바꿉니다.
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
이 템플릿은 현재 시간(초)을 가져와서 Movable Ink 이미지 탭 끝에 쿼리 매개변수로 추가한 다음, 최종 결과를 출력합니다. **테스트** 탭에서 미리 볼 수 있습니다. 코드를 평가하고 미리 보기를 표시합니다.

**3\.** 마지막으로, 세그먼트 멤버십을 다시 평가합니다. 이렇게 하려면 캠페인의 **타겟 오디언스** 단계에 있는 `Re-evaluate audience membership and liquid at send-time` 옵션을 활성화합니다. 이 옵션을 사용할 수 없는 경우 고객 성공 매니저 또는 Braze 지원에 문의하세요. 이 옵션은 인앱 메시지가 트리거될 때마다 고유 URL을 제공하여 캠페인을 다시 요청하도록 Braze SDK에 지시합니다.

{% endtab %}
{% tab 콘텐츠 카드 %}

1. Braze 플랫폼에서 **리치 알림 미디어** 필드에 URL을 붙여넣습니다.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. 모바일의 경우: iOS 및 Android의 콘텐츠 카드 이미지는 수신 즉시 캐시되며 새로 고치지 않습니다. 
  - 해결 방법으로 캠페인을 일별, 주별 또는 월별 반복 메시지로 예약하고 이때 해당 만료일을 지정하여 콘텐츠 카드가 다시 템플릿로 구성합니다. 예를 들어 하루에 한 번 새로 고쳐야 하는 콘텐츠 카드는 만료일이 1일인 일일 예약 전송으로 설정해야 합니다.
3. Movable Ink의 실시간 이미지가 작동하고 콘텐츠 카드가 다시 템플릿으로 구성될 때 캐싱의 영향을 받지 않는지 확인하려면 Liquid를 사용하여 Movable Ink 이미지 URL 끝에 타임스탬프를 추가합니다.

이렇게 하려면 다음 구문을 사용하여 필요에 따라 이미지 URL을 바꿉니다.
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
이 템플릿은 현재 시간(초)을 가져와서 Movable Ink 이미지 탭 끝에 쿼리 매개변수로 추가한 다음, 최종 결과를 출력합니다. **테스트** 탭에서 미리 볼 수 있습니다. 코드를 평가하고 미리 보기를 표시합니다.

{% endtab %}
{% endtabs %}

## 문제 해결

### 동적 이미지가 제대로 표시되지 않나요? 어떤 채널에서 문제가 발생하나요?
- **푸시**: Movable Ink 이미지 URL 앞에 빈 로직이 있는지 확인합니다. <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **인앱 메시지 및 콘텐츠 카드**: 이미지 URL이 노출마다 고유한지 확인합니다. 각 URL이 서로 다르도록 적절한 Liquid를 추가하여 이 작업을 수행할 수 있습니다. [인앱 및 콘텐츠 카드 메시지 지침][instructions]을 참조하세요. 
- **이미지가 로드되지 않음**: '태그 병합'을 Braze 대시보드의 해당 Liquid 필드로 바꾸어야 합니다. 예: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %}을 {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}로 바꿉니다.

### Android에서 GIF를 표시하는 데 문제가 있나요?
- Android에서는 구현 시 GIF 지원이 필요합니다. 이 설정이 없는 경우 Android [인앱 메시지 사용자 지정][GIFsupport] 문서를 참조하세요.


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]:({% image_buster /assets/img/movable_ink/android.png %})
[2]:({% image_buster /assets/img/movable_ink/ios.png %})
[3]:({% image_buster /assets/img/movable_ink/web.png %})