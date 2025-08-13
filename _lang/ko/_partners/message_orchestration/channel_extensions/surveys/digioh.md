---
nav_title: Digioh
article_title: Digioh
description: "이 참고 문서에서는 Braze 캠페인을 통해 실질적인 참여를 유도하는 팝업, 양식, 설문조사 및 커뮤니케이션 선호 센터를 쉽게 만들 수 있는 설문조사 플랫폼인 Braze와 Digioh 간의 파트너십을 설명합니다."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/)는 목록을 늘리고 퍼스트파티 데이터를 수집하며 Braze 캠페인에서 데이터를 활용할 수 있도록 도와줍니다.

_이 통합은 Digioh에서 유지 관리합니다._

## 통합 정보

Braze와 Digioh 통합을 통해 유연한 드래그 앤 드롭 빌더를 사용하여 브랜드에 맞는 양식, 팝업, 성능/성과 센터, 랜딩 페이지 및 설문 조사를 생성하여 고객과 연결할 수 있습니다. Digioh는 통합 설정을 돕고 귀하를 위해 첫 번째 캠페인을 구축, 설계 및 시작하는 데 도움을 줄 것입니다.

!['Digioh와 함께 유연한 이메일 및 커뮤니케이션 환경 설정 센터를 만드세요'][5]{: style="border:0"}

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
|Digioh 계정 | 이 파트너십을 활용하려면 [Digioh 계정](https://www.digioh.com/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze API `/users/track/` 엔드포인트 | `/users/track/` 세부 정보가 추가된 REST 엔드포인트 URL. 사용자의 엔드포인트는 [인스턴스를 위한 Braze URL][6]에 따라 달라집니다.<br><br>예를 들어, REST API 엔드포인트가 `https://rest.iad-01.braze.com`인 경우 `/users/track/` 엔드포인트는 `https://rest.iad-01.braze.com/users/track/`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합 

Digioh을 통합하려면 먼저 Braze 커넥터를 구성해야 합니다. 완료되면 통합을 라이트박스(위젯)에 적용해야 합니다. [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/)을 방문하여 통합 기본 사항에 대해 자세히 알아보세요.

### 1단계: Digioh 통합 생성 

Digioh에서 **통합** 탭을 클릭한 다음 **새 통합** 버튼을 클릭합니다. **Braze** 드롭다운에서 **통합**을 선택하고 통합의 이름을 지정합니다. 

!["드롭다운에서 올바른 통합을 선택하십시오"][2]{: style="max-width:50%;"}

다음으로, Braze REST API 키와 Braze API `/users/track/` 엔드포인트를 입력합니다. 

마지막으로, 이메일 및 이름 외에 추가 커스텀 필드를 매핑하기 위해 맵 필드 섹션을 사용합니다. 다음 코드 스니펫은 예제 페이로드를 보여줍니다. 완료되면 **통합 생성**을 선택하십시오.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### 2단계: Digioh 라이트박스 생성

Digioh [디자인 편집기](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)를 사용하여 라이트박스(위젯)를 구축하십시오. <br>
디자인 편집기를 활용하는 방법의 갤러리를 보고 싶으신가요? Digioh [테마 갤러리](https://www.digioh.com/theme-gallery)를 방문하세요.

### 3단계: 통합 적용

이 통합을 Digioh [라이트박스](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)에 적용하려면, **박스** 페이지로 이동하여 **추가** 또는 **편집** 링크를 **통합** 열에서 선택하십시오. 이것은 편집기의 **통합** 섹션에서 추가할 수도 있습니다.

!['라이트박스에 통합 추가'][3]{: style="max-width:90%"}

여기에서 **통합 추가**를 선택하고 원하는 통합을 선택한 다음, **저장**합니다. Digioh는 이제 실시간으로 캡처된 리드를 Braze에 전달합니다.


[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints