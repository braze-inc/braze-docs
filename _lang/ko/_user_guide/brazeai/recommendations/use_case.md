---
nav_title: 사용 사례
article_title: 사용 사례 드라이브 콘텐츠 시청 후 검색
description: "이 예시는 가상의 브랜드가 Braze AI 상품 추천을 사용하여 주요 고객 순간에 개인화된 콘텐츠와 제품 추천을 제공하는 방법을 보여줍니다."
page_type: tutorial
---

# 사용 사례: 시청 후 콘텐츠 검색 유도

> 이 예시는 가상의 브랜드가 Braze AI 상품 추천을 사용하여 주요 고객 순간에 개인화된 콘텐츠와 제품 추천을 제공하는 방법을 보여줍니다. 추천 로직으로 참여도를 높이고 전환을 늘리며 수작업을 줄이는 방법을 알아보세요.

카밀라가 큐레이션된 영화 및 시리즈 기능을 갖춘 스트리밍 플랫폼인 MovieCanon의 CRM 매니저라고 가정해 보겠습니다. 

카밀라의 목표는 시청자가 시청을 마친 후에도 계속 참여하도록 하는 것입니다. 기존에는 MovieCanon의 '당신도 좋아할지도 모릅니다' 메시징이 광범위한 장르 매칭을 기반으로 세션이 끝난 후 몇 시간 또는 며칠이 지난 임의의 시간에 전송되었습니다. 참여도가 낮았고, 그녀의 팀은 더 잘할 수 있다는 것을 알고 있었습니다.

Camila는 [AI 항목 추천을]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/) 사용하여 각 시청자의 시청 기록을 기반으로 새로운 타이틀을 자동으로 추천하는 시스템을 구축하여 사용자가 영화나 에피소드를 마친 직후에 전달합니다. 이는 사용자가 실제로 다음에 보고 싶은 콘텐츠를 발견하고 플랫폼에 계속 참여할 수 있도록 도와주는 더 스마트하고 개인화된 방법입니다.

!"라는 인앱 메시지가 표시됩니다. "태양의 유목민"을 시청했으므로 이미지, 제목 이름, 설명, "지금 보기" 또는 다음 추천으로 "건너뛰기"를 위한 CTA가 표시됩니다.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

이 튜토리얼에서는 Camila:

- 사용자가 콘텐츠 시청을 완료하면 트리거된 개인화된 메시지입니다.
- 시청자의 선호도에 맞게 맞춤화된 추천 - MovieCanon의 카탈로그에서 자동으로 가져와 메시징에 삽입됩니다. 

## 1단계: 고객이탈 예측 모델 만들기

Camila는 사용자가 콘텐츠 시청을 마칠 때마다 관련 타이틀을 표시하는 추천을 생성하는 것으로 시작합니다. 그녀는 사용자가 최근에 시청한 콘텐츠에 따라 다른 추천을 받을 수 있도록 역동적인 기능을 원했습니다.

1. Braze 대시보드에서 Camila는 **AI 아이템 추천으로** 이동합니다.
2. 새 추천을 만들고 "시청 후 추천"이라는 이름을 지정합니다.
3. 추천 유형으로 **AI 개인화를** 선택하면 각 사용자는 과거 행동을 기반으로 한 맞춤형 추천을 볼 수 있습니다.
4. 사용자가 **이전에 상호 작용한 항목을 추천하지 않음을** 선택하여 사용자가 이미 시청한 콘텐츠에 대한 추천을 받지 않도록 합니다. 
5. 그녀는 MovieCanon의 현재 콘텐츠 라이브러리가 포함된 카탈로그를 선택합니다. 카밀라는 카탈로그의 모든 품목이 추천 대상 품목이 되기를 원하기 때문에 카탈로그 선택 항목을 추가하지 않습니다.
6. 카밀라는 추천을 완료된 조회수를 추적하는 `Watched Content` 커스텀 이벤트에 연결하고 **속성 이름을** 콘텐츠의 제목으로 설정합니다.
7. 추천을 작성합니다.

## 2단계: 인앱 메시지 설정하기

추천 학습이 완료된 후, 카밀라는 사용자가 타이틀을 완료한 직후라는 적절한 순간에 사용자에게 도달할 수 있는 메시징 플로우를 구축합니다. 이 메시지에는 카탈로그에서 직접 가져온 세 가지 개인화된 제안 목록이 포함되어 있습니다.

1. 카밀라는 드래그 앤 드롭 편집기를 사용하여 인앱 메시지 캠페인을 만듭니다.
2. 그녀는 트리거를 커스텀 이벤트로 설정합니다: `Watched Content`.
3. 그녀는 제목 이미지, 이름, "지금 보기" CTA가 포함된 여러 페이지의 인앱 메시지를 디자인합니다.

개인화 유형으로 "아이템 추천"을 선택한 상태에서 Braze 편집기에서 "개인화 추가" 모달이 열립니다.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. 메시지 본문에서 Camila는 [개인화 추가 모달을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) 사용하여 추천 제목의 이름, 설명, 썸네일 등의 변수를 추가하고 카탈로그에서 콘텐츠를 동적으로 채우는 Liquid를 사용합니다. 그녀는 `Last Watched Movie` 에 커스텀 속성을 템플릿으로 지정하여 사용자에게 이 추천이 시청 기록을 기반으로 한다는 사실을 알립니다. 

추천의 카탈로그 항목에서 특정 필드에 템플릿을 작성할 수 있는 원시 Liquid가 포함된 인앱 메시지 편집기.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Show Liquid used in image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. 그런 다음 Camila는 페이지를 복제하고 추천 목록의 다음 항목에서 템플릿으로 사용할 각 변수의 Liquid 배열 {% raw %} (`{{ items[0]}}` ~ `{{items[1]}}`) {% endraw %} 을 증가시킵니다.

## 3단계: 측정 및 최적화

캠페인을 실시간으로 진행하면서 카밀라는 열람율, CTR, 후속 시청 행동을 모니터링합니다. 이전의 정적 추천 캠페인과 성능/성과를 비교한 결과, 사용자당 더 높은 참여도와 더 많은 콘텐츠 세션을 확인할 수 있었습니다.

또한 A/B 테스트도 계획하고 있습니다:

- 타이밍(시청 즉시 또는 시청 후 10분)
- 콘텐츠 레이아웃(캐러셀 대 목록)
- CTA 변형("지금 보기" 대 "대기줄에 추가")

이벤트 기반 메시징과 AI 아이템 추천을 결합하여 콘텐츠 검색을 자동화된 개인화된 경험으로 전환합니다. MovieCanon은 추측 없이 사용자의 참여를 유도하고 적절한 타이밍에 관련 콘텐츠를 전달하여 세션의 깊이를 높이고 이탈 사용자를 줄입니다.





