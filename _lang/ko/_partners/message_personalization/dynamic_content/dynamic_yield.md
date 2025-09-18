---
nav_title: 동적 수익률
article_title: 동적 수익률
description: "이 참조 문서에서는 Braze와 Dynamic Yield 간의 파트너십을 간략히 설명합니다. 이 파트너십을 통해 Dynamic Yield의 추천 및 세분화 엔진을 활용하여 Braze 메시지에 포함될 수 있는 경험 블록을 만들 수 있습니다."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# 동적 수익률

> [Dynamic Yield](https://www.dynamicyield.com/), 마스터카드 회사는 산업 전반에 걸쳐 기업들이 디지털 고객 경험을 개인화하고 최적화하며 동기화할 수 있도록 돕습니다. Dynamic Yield의 [Experience OS](http://www.dynamicyield.com/experience-os)를 사용하면 마케터, 제품 관리자, 개발자 및 디지털 Teams가 각 고객에게 콘텐츠, 제품 및 제안을 알고리즘적으로 일치시켜 매출 및 고객 로열티를 가속화할 수 있습니다.

_This integration is maintained by Dynamic Yield._

## 통합 정보

Braze와 Dynamic Yield 파트너십을 통해 Dynamic Yield의 추천 및 세분화 엔진을 활용하여 Braze 메시지에 포함될 수 있는 경험 블록을 생성할 수 있습니다. 경험 블록은 다음으로 만들 수 있습니다.
- **추천 블록**: 알고리즘과 필터링을 설정하여 이메일이 열릴 때 전파되는 사용자의 개인화된 콘텐츠를 소싱합니다. 
- **동적 콘텐츠 블록**: 다양한 사용자에게 다양한 프로모션과 메시지를 타겟팅합니다. 타겟팅은 친밀도 또는 오디언스를 기반으로 할 수 있습니다. Dynamic Yield는 이메일을 열 때 지원할 개인화된 경험을 결정합니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 다이나믹 수익 계정 | 이 파트너십을 활용하려면 [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) 계정이필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 경험 블록 생성

Dynamic Yield에서 경험 블록을 생성하려면 **이메일 > 경험 이메일 > 새로 생성**으로 이동합니다.

다음으로, **경험 블록 생성**을 선택하여 Braze 이메일 템플릿에 삽입할 동적 콘텐츠 또는 추천 블록을 디자인합니다.<br>![][8]

### 2단계: 메시징 초안 작성

다음 이미지는 빌더에서 처음부터 이메일을 보여줍니다.<br>![][6]

1. 캠페인 이름, 메모 및 라벨을 제목 영역에 입력하세요.<br><br>
2. 경험 블록을 삽입합니다. 이 블록에는 다음이 포함됩니다.
  - [추천](#configure-a-recommendations-block): 사용자에게 완전히 개인화된 추천을 제공하는 위젯.
  - [동적 콘텐츠](#configure-a-dynamic-content-block): 다양한 오디언스에게 다양한 프로모션과 메시지를 타겟팅합니다.<br><br>
3. 설정 업데이트:
  - URL 매개변수를 사용하여 분석 소프트웨어 내에서 클릭을 추적합니다(선택 사항). 필요에 따라 기본값 디스플레이에 매개변수를 추가하십시오.
  - 속성 창을 선택합니다. 7일(기본값) 또는 1일 중에서 선택합니다.<br><br>
4. 저장하고 종료합니다. 코드가 생성되기 전에 언제든지 이메일의 모든 요소를 편집할 수 있습니다. 코드가 생성된 후에는 코드에 영향을 미치지 않는 [모든 것을 편집할 수 있습니다](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### 추천 블록 구성

추천 블록을 사용하면 알고리즘과 필터링을 설정하여 이메일을 열 때 전파되는 사용자의 개인화된 콘텐츠를 소싱할 수 있습니다. 

1. 편집 창에서 추천 블록을 이메일 본문으로 끌어다 습니다.<br><br>
2. 원하는 알고리즘을 선택합니다(인기도, 사용자 친밀도, 유사성 등). 선택한 알고리즘에 따라 추가 옵션이 표시됩니다: 
  - 추천이 인기도에 기반한 경우 시청자가 열람한 다른 이메일에서 동일한 추천을 제공하지 않도록 결과를 섞을 수 있습니다.
  - 다른 알고리즘(예: 유사성)은 추천을 제공하기 위해 컨텍스트에 의존하므로 포함할 항목을 선택해야 합니다. 이 항목은 빌더에 추가하거나 [임베드 코드에 병합 태그를 추가](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced)하여 동적으로 만들 수 있습니다. 예를 들어, 유사한 항목을 배송 확인 이메일에 추가할 수 있습니다. <br><br>
3. 사용자가 이미 구매한 제품을 제외하여 이러한 제품을 추천하지 않도록 할 수 있습니다.<br><br>
4. 특정 제품을 슬롯에 고정하거나 제품 속성에 따라 제품을 포함 및 제외하도록 [커스텀 필터 규칙](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD)을 추가할 수 있습니다. 예를 들어, 코드가 $5 미만인 제품이나 반바지 카테고리의 제품만 표시하지 마세요.<br><br>
5. 마지막으로 추천 블록 디자인을 구성합니다. 이 작업을 수행하려면 항목 템플릿을 선택하고 표시할 항목 수와 행 수를 설정합니다. 

### 동적 콘텐츠 블록 구성
동적 콘텐츠를 사용하여 다양한 사용자에게 다양한 프로모션과 메시지를 타겟팅합니다. 타겟팅은 친밀도 또는 오디언스를 기반으로 할 수 있습니다. Dynamic Yield는 이메일을 열 때 지원할 개인화된 경험을 결정합니다. 

1. 편집 창에서 동적 콘텐츠 블록을 이메일 본문으로 끌어다 놓으세요.<br><br> 
2. 첫 번째 변형에 대한 템플릿을 선택하십시오. 이제 디자인 및 콘텐츠 변수를 정의할 수 있습니다. 완료되면 변형을 저장합니다. <br>![][4]<br><br> 
3. 동적 콘텐츠 창에서 오디언스를 설정합니다.<br>![][5]<br><br> 
4. 다른 특정 오디언스 또는 모든 사용자를 타겟팅하도록 다른 변형을 추가합니다. 필요한 만큼 반복하십시오.<br><br> 
5. 위아래 화살표를 사용하여 변형의 우선순위를 설정하십시오. <br><br> 
6. 우선순위는 사용자가 둘 이상의 경험을 받을 자격이 있을 때 지원할 변형을 결정합니다.

### 3단계: Braze와 이메일 통합

이 통합을 통해 개인화된 추천 위젯과 Dynamic Yield에서 제공하는 동적 콘텐츠를 Braze 이메일 캠페인에 추가할 수 있습니다. 이 캠페인을 Braze 캠페인에 포함시키는 것은 Braze 이메일 편집기에 붙여넣는 간단한 임베드 코드로 수행됩니다.

1. 경험 이메일 목록 페이지에서 ESP 통합 아이콘을 클릭하세요.<br><br> 
2. Braze에서 사용자의 CUID와 이메일 ID를 삽입하는 관련 토큰을 입력합니다.<br>![][3]
  
이메일에 만족하면 다음 단계는 Braze에 포함할 코드를 생성하는 것입니다.
1. **경험 이메일**에서 **코드 생성**을 클릭하십시오.<br><br> 
2. 다음으로, **클립보드에 복사**를 클릭하십시오.<br>![][1]<br><br> 
3. 코드를 Braze 이메일 캠페인에 붙여넣고, 이메일 캠페인의 디자인, 테스트 및 게시를 계속 진행합니다.


[1]: {% image_buster /assets/img/dynamic_yield/dynamic_yield.png %}
[2]: {% image_buster /assets/img/dynamic_yield/dynamic_yield1.png %}
[3]: {% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %}
[4]: {% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %}
[5]: {% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %}
[6]: {% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %}
[7]: {% image_buster /assets/img/dynamic_yield/dynamic_yield6.png %}
[8]: {% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %}
