---
nav_title: API를 통해 사용자 제거하기
article_title: API를 통해 사용자 제거하기
page_order: 0

page_type: reference
description: "이 도움말 문서에서는 Braze REST API를 통해 고객 프로필을 제거할 때의 의미를 설명합니다."
tool: Dashboard
platform: API
---

# API를 통해 사용자 제거하기

[Braze REST API를 통해 사용자를 제거하면]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/) 다음 데이터가 삭제(무효화)됩니다.
- 사용자가 보유한 모든 속성
- 이메일 주소
- 전화번호
- 외부 사용자 ID 
- 성별
- 국가
- 언어

[Braze REST API를 통해 사용자를 제거하면]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/) 다음 이벤트가 발생합니다:
- 사용자 프로필이 삭제(무효화)됩니다.
- [평생 사용자]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) 수는 새로 제거된 사용자를 고려하여 업데이트됩니다.	
- 제거된 사용자도 여전히 집계된 전환율에 포함됩니다. 삭제된 사용자에 대해서는 사용자 지정 이벤트 횟수 및 구매 횟수가 업데이트되지 않습니다.

## 공유 이메일 주소가 있는 여러 프로필

동일한 이메일 주소를 공유하는 여러 사용자 프로필을 병합하고 싶다고 가정해 보겠습니다. 

이러한 사용자 프로필을 병합하려면 다음과 같이 하세요:

 1. 이메일 주소가 중복된 사용자를 식별합니다. 
 2. 단일 프로필의 모든 속성을 내보냅니다. 
 3. API 또는 CSV를 통해 이러한 속성을 사용자 프로필로 가져옵니다. 
 4. API를 통해 사용자를 제거하면 기본적으로 위에서 설명한 중복 사용자 및 데이터를 삭제할 수 있습니다.

_마지막 업데이트 2023년 9월 13일_

