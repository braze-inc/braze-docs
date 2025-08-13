---
nav_title: IAM 스튜디오
article_title: IAM 스튜디오
description: "이 참조 문서에서는 개인화된 풍부한 인앱 경험을 생성하고 Braze를 통해 전달할 수 있도록 지원하는 메시지 개인화 플랫폼인 IAM Studio와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM 스튜디오

> [IAM Studio](https://www.inappmessage.com)는 코드 없는 메시지 개인화 플랫폼으로, 개인화된 풍부한 인앱 경험을 생성하고 이를 Braze를 통해 전달할 수 있습니다.

_This integration is maintained by IAM Studio.\*s._

## 통합 정보

Braze 및 IAM Studio 통합을 통해 Braze 인앱 메시지에 사용자 지정 가능한 인앱 메시지 템플릿을 쉽게 삽입하여 이미지 교체, 텍스트 수정, 딥링크 설정, 커스텀 속성 및 이벤트 설정을 제공할 수 있습니다. IAM Studio를 사용하면 메시지 제작 시간을 줄이고 콘텐츠 계획에 더 많은 시간을 할애할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| IAM Studio 계정 | 이 파트너십을 활용하려면 [IAM Studio 계정](https://www.inappmessage.com/register)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용 사례

- 상품 구매 장려
- 사용자 정보 수집
- 멤버십 등록 증가
- 쿠폰 발급 정보

## 통합

### 1단계: 템플릿을 선택하세요

인앱 메시지 템플릿 갤러리에서 사용하려는 인앱 메시지 템플릿을 선택하세요

![IAM Studio 템플릿 갤러리는 '캐러셀 슬라이드 Modal', '간단한 아이콘 Modal', 'Modal 전체 이미지' 등 다양한 템플릿을 보여줍니다.][1]

### 2단계: 템플릿 사용자 정의

먼저 콘텐츠에 맞게 이미지, 텍스트 및 버튼을 사용자 정의하십시오. 이미지와 버튼에 **딥링크**를 연결하십시오.

{% tabs local %}
{% tab 이미지 %}
![IAM 스튜디오 UI에서 이미지를 사용자 정의할 수 있는 옵션을 보여줍니다. 이 옵션에는 이미지, 이미지 반경 및 이미지 흐림 효과가 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab 텍스트 %}
![메시지의 제목과 부제목을 사용자 지정할 수 있는 옵션을 보여주는 IAM Studio UI. 이 옵션에는 텍스트, 서식 및 글꼴이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab 버튼 %}
![기본, 왼쪽 및 오른쪽 버튼을 사용자 지정하는 옵션을 보여주는 IAM Studio UI. 이 옵션에는 색상, 딥링크, 텍스트 및 서식이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

다음으로, 커스텀 글꼴을 추가하고 Liquid 태그를 사용하여 개인화된 인앱 메시지를 만드세요. 로깅 및 추적을 활성화하려면 **로그 데이터 및 사용자 행동 추적**을 선택하십시오.

{% tabs local %}
{% tab 폰트 %}
![IAM Studio UI가 Liquid을 추가하는 옵션을 보여줍니다. These options include making personalized sentence.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![이벤트/속성 로깅을 사용자 지정하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 사용자 행동 로그가 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab 로깅 및 추적 %}
![글꼴을 사용자 지정하는 옵션을 보여주는 IAM Studio UI. 이 옵션에는 사용자가 글꼴 스타일을 사용자 지정할 수 있는 기능이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### 3단계: 템플릿 내보내기

모든 편집이 완료되면 **내보내기**를 클릭하여 템플릿을 내보내십시오. 내보낸 후 인앱 메시지 HTML 코드가 생성됩니다. 이 코드를 **코드 복사** 버튼을 클릭하여 복사하세요. 

![][2]{: style="max-width:45%;"}

### 4단계: Braze에서 코드를 사용하세요 

Braze로 이동하여 인앱 메시지에서 커스텀 코드를 **HTML 입력** 상자에 붙여넣습니다. 메시지가 올바르게 표시되는지 확인하려면 메시지를 테스트하십시오.

![][3]{: style="max-width:85%;"}


[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}
