---
nav_title: LILT
article_title: LILT
description: "이 참고 문서에서는 Braze와 LILT의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILT는](https://lilt.com/) 기업용 번역 및 콘텐츠 제작을 위한 완벽한 AI 솔루션입니다. LILT는 글로벌 조직이 AI 에이전트와 완전 자동화된 워크플로우를 통해 콘텐츠, 제품, 커뮤니케이션 및 지원 운영을 확장하고 최적화할 수 있도록 지원합니다.

_이 통합은 LILT에서 유지 관리합니다._

## 이 통합 정보

LILT Braze 커넥터는 AI 속도와 엔터프라이즈급 품질로 HTML 이메일 템플릿을 번역할 수 있는 인에이블먼트입니다. 브랜드에 맞는 즉석 번역 또는 품질이 보장된 검증 번역을 요청하고 Braze에서 바로 LILT의 다국어 이메일 콘텐츠를 받아보세요. 

## 사용 사례

LILT Braze 통합은 번역 프로세스를 자동화하고 가속화하여 글로벌 마케팅 팀이 브랜드 일관성을 유지하면서 신속하게 다국어 캠페인을 시작할 수 있도록 지원합니다.

### 간소화된 글로벌 캠페인 출시

수동 번역 핸드오프로 인한 지연 없이 여러 지역에서 동시에 마케팅 캠페인을 시작할 수 있습니다.

- **시나리오:** 귀사에서 10개국에 신제품을 출시합니다.
- **솔루션:** 마케팅 팀이 Braze에서 영문 이메일 템플릿을 완성하고 `LILT: Ready` 으로 태그를 지정하면 LILT 커넥터가 자동으로 콘텐츠를 가져옵니다. 도메인별 언어 전문가가 품질 보증을 위해 LILT 플랫폼에서 AI 번역 프롬프트를 검토하고 커넥터가 번역된 버전을 다시 Braze에 푸시합니다.
- **혜택:** 글로벌 캠페인의 출시 시간을 며칠에서 몇 시간으로 단축하여 모든 고객이 최적의 타이밍에 신제품 소식을 받아볼 수 있습니다.

### 브랜드에 맞춘 즉각적인 현지화

시간이 촉박한 커뮤니케이션을 위해 LILT의 AI를 사용하여 즉각적인 브랜드 내 번역을 수행하세요.

- **시나리오:** 5개 지역 시장에서 반짝 세일, 기간 한정 혜택 또는 긴급 서비스 중단에 대한 이메일을 즉시 배포해야 합니다.
- **솔루션:** 이메일 템플릿에 `LILT: Instant` 으로 태그를 지정합니다. LILT는 AI와 귀사에 특화된 언어 자산(예: 용어 및 스타일 가이드)을 사용하여 몇 분 안에 고품질의 브랜드 일관성 있는 번역을 생성합니다.
- **혜택:** 시간에 민감한 마케팅에 필수적인 브랜드 목소리나 품질 저하 없이 반응성이 뛰어난 실시간 커뮤니케이션이 가능합니다.

## 필수 조건

| Prerequisite       | 설명 |                        
|-----------------------|-----------------|
| LILT 계정   | 이 파트너십을 이용하려면 LILT 계정이 필요합니다.  |
| A Braze REST API key  | A Braze REST API key with the following permissions:<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> **설정** > **API 키에서** Braze 대시보드에서 이 키를 생성하세요. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}


## Integration

### 1단계: LILT Braze 커넥터 구성하기

1. LILT에 로그인한 다음 **연결** > **새 커넥터** > **Braze로** 이동합니다.
	
![LILT의 Braze 커넥터.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2\. Braze 콘텐츠에 대해 원하는 현지화 워크플로를 선택합니다.

![LILT의 Braze 워크플로.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})	

{: start="3"}
3\. 필요한 구성 세부 정보를 입력하고 확인합니다:
- Braze API 키
- Braze REST endpoint

![API 자격 증명 완료.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})	

{: start="4"}
4\. **확인을** 선택하여 설정을 테스트합니다. 연결이 확인되면 구성을 저장합니다.

### 2단계: Braze 작업 공간 준비하기

1. Braze 작업 공간 설정에서 다국어 기능을 활성화하세요.

![Braze에서 현지화 설정하기.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})	

{: start="2"}
2\. LILT 워크플로우를 위해 Braze에서 다음 태그를 생성하세요: 
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![Braze에서 LILT 태그를 설정합니다.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})	

{: start="3"}
### 3단계: 번역을 위해 LILT에 콘텐츠 보내기 

1. LILT Braze 커넥터를 설정한 후, Braze 이메일 템플릿 내에서 Liquid 번역 태그를 사용하여 번역할 콘텐츠를 식별하세요. 
- 예시:  {% raw %}`{% translation id_0 %}`안녕하세요, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. 원하는 워크플로우를 표시하도록 템플릿 태그를 업데이트하여 번역을 시작합니다: 
- 인증된 번역을 보려면 `LILT: Ready` 을 선택하세요.
- 브랜드에 맞는 즉석 번역을 원하시면 `LILT: Instant` 을 선택하세요.
3. 미리 설정한 타이밍에 맞춰 LILT Braze 커넥터가 실행되어 태그가 지정된 콘텐츠를 LILT로 가져옵니다. 콘텐츠 태그가 프로젝트의 단계를 반영하여 Braze에서 자동으로 업데이트되므로 번역 진행 상황을 추적할 수 있습니다. 
	
![번역 태그가 있는 Braze 이메일 템플릿.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})	