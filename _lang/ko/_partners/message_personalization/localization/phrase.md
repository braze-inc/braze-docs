---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "이 참조 문서에서는 로컬라이제이션용 클라우드 기반 소프트웨어인 Braze와 Phrase의 파트너십에 대해 간략하게 설명합니다. 이 통합을 통해 Braze 인터페이스에서 나가지 않고도 이메일 템플릿과 콘텐츠 블록을 번역할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Phrase 

> [Phrase는](https://phrase.com/) 로컬라이제이션 관리를 위한 클라우드 기반 소프트웨어입니다. Phrase는 자동화된 번역 워크플로우를 구현하고 민첩한 팀을 위한 지속적인 로컬라이제이션을 지원합니다.

_This integration is maintained by Phrase._

## 통합 정보

Phrase와 Braze 통합을 사용하면 Braze 인터페이스에서 나가지 않고도 이메일 템플릿과 콘텐츠 블록을 번역할 수 있습니다. Braze용 Phrase TMS 통합을 사용하면 원활한 현지화를 통해 고객 참여를 높이고 새로운 시장으로의 성장을 촉진할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| --- | --- |
| Phrase TMS 계정 | 이 파트너십을 이용하려면 Phrase TMS Ultimate 또는 Enterprise 계정이 필요합니다. |
| Braze REST API 키 | 모든 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

## 1단계: Phrase TMS 설정

Phrase에서 **설정 > 통합 > 커넥터 > 새로 만들기**로 이동합니다.

1. 연결 이름을 입력하고 유형을 **Braze로** 변경합니다.<br><br>
2. REST API 키와 Braze REST 엔드포인트를 입력합니다. <br><br>
3. 커넥터가 콘텐츠 블록이 연결된 이메일 템플릿을 가져오는 방법을 선택합니다. 
- 선택한 이메일 템플릿만 해당
- 콘텐츠 블록 포함<br><br>
4. 커넥터가 이메일 템플릿 번역을 내보내는 방법을 선택합니다. 
- 새 항목 생성
- 원본 항목
  - 원본 항목은 번역을 동일한 템플릿/블록으로 내보냅니다. 언어 세그먼트는 제공된 속성으로 정의됩니다.<br><br>
    {% raw %}
    원본 항목을 선택한 경우 언어 속성을 입력합니다. 언어 속성은 if/elsif 인수의 언어를 정의합니다. 원본 항목 옵션을 사용하는 경우 아래 그림과 같이 구조화해야 합니다:

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    또는 할당 키/값 매핑을 사용합니다.
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    위의 Liquid는 엄격하게 준수해야 하지만 언어 속성과 언어, 키 및 값은 조정할 수 있습니다.<br><br>
    각 언어 코드는 한 번만 사용할 수 있지만, 예를 들어 한 세그먼트에 여러 언어를 사용할 수 있습니다:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. **연결 테스트**를 클릭합니다. 연결에 성공하면 확인 표시가 나타납니다. 아이콘 위로 마우스를 가져가면 자세한 내용을 확인할 수 있습니다.<br><br>
7. 마지막으로 **저장**을 클릭합니다. 이 커넥터는 **커넥터** 페이지에서 사용할 수 있습니다.

## 3단계: Phrase에 콘텐츠를 전송하고 다시 Braze로 내보내기

1. 먼저, 제출자가 온라인 리포지토리에서 직접 요청에 파일을 추가할 수 있도록 [제출자 포털](https://support.phrase.com/hc/en-us/articles/5709602111132)을 설정합니다.<br><br>
2. [자동화된 프로젝트 생성(APC)을](https://support.phrase.com/hc/en-us/articles/5709647363356) 사용하면 지정된 워크플로 상태의 변경이 감지되면 Phrase TMS가 자동으로 새 프로젝트를 생성하도록 할 수 있습니다.<br><br>
3. 선택한 콘텐츠 항목은 APC를 처음 실행할 때 가져옵니다.

[커넥터 API](https://cloud.memsource.com/web/docs/api#)는 단계를 자동화할 수 있습니다. 그렇지 않으면 해당 단계는 UI를 통해 수동으로 수행됩니다. [웹훅](https://support.phrase.com/hc/en-us/articles/5709693398812)을 사용하여 Phrase TMS에서 서드파티 시스템에 특정 이벤트(예: 작업 상태 변경)에 대한 알림을 보낼 수 있습니다.


