---
nav_title: 오켄도
article_title: "오켄도"
description: "Okendo와 Braze를 통합하는 방법을 알아보세요."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# 오켄도

> [Okendo는](https://okendo.io/) 지지자를 육성하고, 입소문을 확장하고, 생애주기 가치를 극대화하여 고객을 동원하여 더 빠르고 효율적으로 성장할 수 있는 도구를 제공하는 통합 고객 마케팅 플랫폼입니다.

*이 통합은 Okendo에서 유지 관리합니다.*

## 통합 정보

Braze와 Okendo의 통합은 리뷰, 로열티, 추천, 설문조사, 퀴즈 등 Okendo 플랫폼의 여러 제품에서 작동합니다. Okendo는 고객 이벤트 및 사용자 속성을 Braze에 전송하여 메시지를 개인화 및 트리거하는 데 사용할 수 있습니다.  

## 필수 조건

| Requirement            | 설명                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 오켄도 계정         | 이 파트너십을 이용하려면 Okendo 계정이 필요합니다.        |
| Braze REST API key     | A Braze REST API key with `users.track` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint    | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1단계: Okendo에서 Braze 커넥터 설정하기

1. Okendo에서 **설정** > **통합** > **이메일 & SMS** > **Braze로** 이동합니다.
2. **통합** 설정에 API 엔드포인트와 API 키를 추가합니다.

### 2단계: 식별자 구성하기

`external_id` 필드는 각 이벤트와 관련된 사용자를 식별하는 데 사용됩니다. 필드를 Shopify 고객 ID와 연결하려면 **Braze 사용자 식별에 Shop** ify 고객 ID 사용을 토글합니다. 그렇지 않으면 토글을 해제하여 각 사용자의 이메일 주소와 연결합니다.

## 오켄도 이벤트와 속성을 Braze에 동기화하기

### 사용자 지정 이벤트

{% alert note %}
샘플 이벤트 데이터는 [Okendo 설명서를 참조](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c)하세요.
{% endalert %}

#### 이벤트 검토

- 오켄도 리뷰 생성됨
- 오켄도 검토 요청

#### 추천 이벤트

- 오켄도 추천 보내기
- 오켄도 추천 옵트인
- 오켄도 추천 초대장
- 오켄도 추천 쿠폰을 받았습니다.
- 교환된 오켄도 추천 쿠폰
- 오켄도 추천 거부됨

#### 로열티 이벤트

- 오켄도 로열티 등록
- 오켄도 로열티 포인트 부여
- 오켄도 로열티 포인트 교환
- 오켄도 로열티 등급 변경
- 오켄도 로열티 포인트 조정

#### 설문조사 이벤트

- 오켄도 설문조사 제출하기

#### 퀴즈 이벤트

- 오켄도 퀴즈 제출

### Custom attributes

Okendo는 사용자 프로필 데이터를 Braze에서 커스텀 속성으로 전송하여 오디언스 세그먼트를 생성하는 데 사용할 수 있습니다. 예를 들면 다음과 같습니다:

- 나이, 생일, 피부 타입, 머리 색깔 등 설문조사 및 리뷰 제출 시 묻는 프로필 질문
- _평균 리뷰 평점_ 및 _평균 리뷰 감정과_ 같은 리뷰 측정 기준
- _포인트 잔액_ 및 _VIP 등급과_ 같은 로열티 측정기준
- 추천 _성공 횟수_ 및 _총 추천 매출과_ 같은 추천 측정기준  
- 설문조사에서 수집한 순고객추천지수 점수

## Okendo 제품과 Braze 사용하기

Okendo 제품에 따라 Braze와 Okendo를 함께 사용하려면 추가 단계를 완료해야 합니다. 자세한 내용은 다음 문서를 참조하세요:

- [리뷰와 Braze 통합하기](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [로열티와 Braze의 통합](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [추천을 Braze와 통합하기](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [설문조사와 Braze 통합하기](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Braze와 퀴즈 통합하기](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
통합 구성에 대한 도움이 필요하면 Okendo 지원팀에 문의하세요.
{% endalert %}
