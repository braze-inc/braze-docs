---
nav_title: eduMe
article_title: eduMe
description: "이 참조 문서에서는 Braze 연결된 콘텐츠를 활용하여 사용자가 Braze 캠페인에서 eduMe 학습 과정 및 강의에 액세스할 수 있도록 지원하는 모바일 기반 교육 툴인 eduMe와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [EduMe](https://edume.com)는 모바일 기반 교육 툴로, 직원이 필요할 때 언제 어디서나 성공에 필요한 지식을 얻을 수 있도록 지원합니다. 

_This integration is maintained by eduMe._

## 통합 정보

Braze와 eduMe 통합을 통해 Braze [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)를 활용하여 사용자가 Braze 캠페인에서 eduMe 삭습 과정과 레슨에 액세스할 수 있습니다. 그런 다음, 개인 및 그룹 진행 상황을 eduMe 보고 기능을 통해 추적할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| eduMe 계정 | 이 파트너십을 활용하려면 EduMe 계정이 필요합니다. |
| eduMe API 키 | eduMe 고객 성공 담당자에게 API 키를 요청해야 합니다. 이 키는 Braze 커넥티드 콘텐츠 통화에서 사용됩니다. |
| eduMe 링크 서명 비밀 | 조직의 링크 서명 비밀을 설정하려면 eduMe의 고객 성공 담당자에게 요청해야 합니다. 이 비밀은 연결된 콘텐츠에서 원활한 링크를 활성화하는 데 사용됩니다. 이 비밀을 사용하여 다른 작업은 수행할 필요가 없습니다. |
| eduMe 그룹 및 콘텐츠 ID | 이러한 식별자는 연결된 콘텐츠 호출을 설정하는 데 필요합니다. 이러한 식별자를 얻는 데 도움이 필요하면 eduMe 고객 서비스 담당자에게 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 커넥티드 콘텐츠 통화 만들기

사용자에게 코스, 강의 또는 eNPS 설문조사에 대한 접근 권한을 부여하고, eduMe의 내부 사용자 ID와 비교하여 진행 상황을 추적하려면 이 예에 표시된 API 호출을 따르세요:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. `YOUR-EDUME-API-KEY` 을 eduMe API 키로 바꿉니다.<br><br>
2. `EDUME-CONTENT-LINK-AND-CONTENT-ID`를 해당 콘텐츠 링크 문자열 및 모듈, 레슨 또는 설문조사 식별자로 바꿉니다. 이러한 식별자는 EduMe 계정에서 찾을 수 있습니다.
  - 학습 과정: `getCourseLink?moduleId=12087`
  - 레슨: `getLessonLink?lessonId=25805`
  - eNPS 설문조사: `getSurveyLink?surveyId=654`<br><br>
3. 이 링크를 통해 EduMe에 도달한 사용자는 선택한 EduMe 팀 또는 그룹에 추가됩니다. `groupId` 을 관련 팀 ID 또는 eduMe 그룹 ID로 바꿉니다. 등록이 필요한 학습 과정을 제외하고, 일반적으로 팀 ID를 사용합니다. 등록이 필요한 경우 그룹 ID를 사용해야 합니다.<br><br>
4. `externalUserId` 필드를 매핑할 적절한 필드를 포함하세요. 연결된 콘텐츠 호출 예제에서는 `driver_id`를 사용하지만 필드는 다를 수 있습니다. 이 ID는 eduMe 보고서에서 사용할 수 있으며, 이를 통해 시스템과 상호 연관시킬 수 있습니다.<br><br>
5. 마지막으로 필요에 따라 메시지를 사용자 지정하고 테스트합니다. 하나 이상의 시험 메시지를 보내고, eduMe 콘텐츠에 접근하여 레슨 또는 코스를 완료하고, eduMe 분석이 기록되고 있는지 확인하는 것이 좋습니다. 

