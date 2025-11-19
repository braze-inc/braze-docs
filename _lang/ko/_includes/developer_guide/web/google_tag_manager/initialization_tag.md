### 필수 조건

이 통합 방법을 사용하려면 먼저 [Google 태그 매니저용 계정과 컨테이너를 만들어야](https://support.google.com/tagmanager/answer/14842164) 합니다.

### 1단계: 태그 템플릿 갤러리 열기

[Google 태그 관리자에서](https://tagmanager.google.com/) 작업 공간을 선택한 다음 **템플릿을** 선택합니다. **태그 템플릿** 창에서 **갤러리 검색을** 선택합니다.

![Google Tag Manager의 예제 워크스페이스에 대한 템플릿 페이지]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### 2단계: 초기화 태그 템플릿 추가하기

템플릿 갤러리에서 `braze-inc` 를 검색한 다음 **Braze 초기화 태그를** 선택합니다.

![다양한 'Braze-inc' 템플릿을 보여주는 템플릿 갤러리.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**작업 공간에** **추가**> **추가를** 선택합니다.

![Google Tag Manager의 'Braze 초기화 태그' 페이지]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### 3단계: 태그 구성

**템플릿** 섹션에서 새로 추가한 템플릿을 선택합니다.

![Braze 초기화 태그 템플릿이 표시된 Google Tag Manager의 "템플릿" 페이지]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

연필 아이콘을 선택하여 **태그 구성** 드롭다운을 엽니다.

!['연필' 아이콘이 표시된 태그 구성 타일]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

최소한의 필수 정보를 입력합니다:

| 필드         | 설명 |
| ------------- | ----------- |
| **API 키**   | Braze 대시보드의 **설정** > **앱 설정에서** [API 키를]({{site.baseurl}}/api/basics/#about-rest-api-keys) 찾을 수 있습니다. |
| **API 엔드포인트** | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
| **SDK 버전**  | [체인지로그에]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web) 나열된 가장 최신 버전의 Web Braze 소프트웨어 개발 키트( `MAJOR.MINOR` )입니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. 자세한 내용은 [소프트웨어 개발 키트 버전 관리 정보를]({{site.baseurl}}/developer_guide/sdk_integration/version_management/) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

추가 초기화 설정을 하려면 **Braze 초기화 옵션을** 선택하고 필요한 옵션을 선택합니다.

!['태그 구성' 아래의 Braze 초기화 옵션 목록]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### 4단계: *모든 페이지에서* 트리거하도록 설정

초기화 태그는 사이트의 모든 페이지에서 실행되어야 합니다. 이를 통해 Braze 소프트웨어 개발 키트 메소드를 사용하고 웹 푸시 분석을 기록할 수 있습니다.

### 5단계: 통합 확인

다음 옵션 중 하나를 사용하여 통합을 확인할 수 있습니다:

- **Option 1:** Google Tag Manager의 [디버깅 툴을](https://support.google.com/tagmanager/answer/6107056?hl=en) 사용하여 구성된 페이지 또는 이벤트에서 Braze 초기화 태그가 올바르게 트리거되는지 확인할 수 있습니다.
- **Option 2:** 웹 페이지에서 Braze에 대한 네트워크 요청이 있는지 확인하세요. 또한 이제 글로벌 `window.braze` 라이브러리를 정의해야 합니다.
