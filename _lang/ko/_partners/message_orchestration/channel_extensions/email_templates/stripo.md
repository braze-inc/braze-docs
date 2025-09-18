---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "이 참고 문서에서는 대화형 요소가 포함된 정교한 이메일을 쉽게 만들 수 있는 드래그 앤 드롭 이메일 템플릿 빌더인 Braze와 Stripo의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo는](https://stripo.email/) 드래그 앤 드롭 이메일 템플릿 빌더로 대화형 요소가 포함된 반응형 이메일을 만들고 디자인할 수 있도록 도와줍니다. Stripo 사용자는 HTML로 편집하고 Stripo 에디터를 통해 다양한 디바이스에서 표시하거나 숨길 요소를 결정할 수도 있습니다.

_This integration is maintained by Stripo._

## 통합 정보

Braze와 Stripo의 통합을 통해 사용자 지정한 Stripo 이메일을 내보내고 Braze 내에서 템플릿으로 업로드할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ------------| ----------- |
| Stripo 계정 | 이 파트너십을 이용하려면 Stripo 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 클러스터 인스턴스 | 귀하의 Braze [클러스터 인스턴스]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 및 REST 엔드포인트와 일치합니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: Stripo 이메일 만들기

Stripo 플랫폼에서 Stripo 이메일을 생성하고 **내보내기를** 클릭합니다. 

![Stripo 수출]({% image_buster /assets/img_archive/stripo_export.png %})

### 2단계: Braze로 템플릿 내보내기

표시되는 대화 상자에서 내보내기 방법으로 **Braze**를 선택합니다. 

다음으로, **계정 이름**(예: 워크스페이스 이름), **API 키** 및 **클러스터 인스턴스**를 입력합니다.

![Stripo 양식]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
이 설정은 일회성 설정이며 향후 모든 내보내기에서는 이 API 키를 자동으로 활용합니다.
{% endalert %}

## 사용량

Braze 계정의 **템플릿 및 미디어 > 이메일 템플릿** 섹션에서 업로드한 Stripo 템플릿을 찾을 수 있습니다. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 보낼 수 있습니다!


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
