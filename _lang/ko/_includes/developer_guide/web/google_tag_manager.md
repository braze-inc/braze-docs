## 웹용 Google Tag Manager 정보 {#google-tag-manager}

Google Tag Manager(GTM)를 사용하면 프로덕션 코드 릴리스나 엔지니어링 리소스 없이도 웹사이트에 원격으로 태그를 추가, 제거, 편집할 수 있습니다. Braze는 웹 SDK를 위해 다음과 같은 템플릿을 제공합니다:

|태그 유형|사용 사례|
|--------|--------|
| 초기화 태그 | 이 태그를 사용하면 사이트의 코드를 수정할 필요 없이 [Web Braze SDK를 통합]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)할 수 있습니다.|
| 동작 태그 | 이 태그를 사용하면 [콘텐츠 카드를 생성]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)하고, [사용자 속성을 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)하고, [데이터 수집을 관리]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## GTM으로 커스텀 이벤트 로깅하기

GTM에서 **커스텀 HTML** 태그를 사용하여 커스텀 이벤트를 로깅할 수 있습니다. 이 방법은 GTM [데이터 레이어](https://developers.google.com/tag-platform/tag-manager/datalayer)를 사용하여 사이트에서 Braze 웹 SDK를 호출하는 GTM 태그로 이벤트 데이터를 전달합니다.

### 1단계: 데이터 레이어에 이벤트 푸시하기

사이트의 코드에서 커스텀 이벤트를 트리거하려는 위치에 이벤트를 데이터 레이어에 푸시합니다. 예를 들어, 버튼을 클릭할 때 커스텀 이벤트를 로깅하려면 다음과 같이 합니다:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### 2단계: GTM에서 트리거 생성하기

1. GTM 컨테이너에서 **트리거**로 이동하여 새 트리거를 생성합니다.
2. **트리거 유형**을 **커스텀 이벤트**로 설정합니다.
3. **이벤트 이름**을 데이터 레이어에 푸시한 값과 동일하게 설정합니다(예: `my_custom_event`).
4. 트리거가 실행될 시점을 선택합니다(예: **모든 커스텀 이벤트**).

### 3단계: 커스텀 HTML 태그 생성하기

1. GTM에서 **태그**로 이동하여 새 태그를 생성합니다.
2. **태그 유형**을 **커스텀 HTML**로 설정합니다.
3. HTML 필드에 다음을 추가합니다:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. **트리거** 아래에서 2단계에서 생성한 트리거를 선택합니다.
5. 컨테이너를 저장하고 게시합니다.

이벤트 등록정보를 포함하려면 두 번째 인수로 전달합니다:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Google의 EU 사용자 동의 정책

{% alert important %}
Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html) 개정 사항에 따라 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항에 따라 광고주는 EEA 및 영국 최종 사용자에게 특정 정보를 공개하고 해당 사용자로부터 필요한 동의를 얻어야 합니다. 자세한 내용은 다음 설명서를 참조하세요.
{% endalert %}

Google의 EU 사용자 동의 정책의 일환으로 다음 부울 커스텀 속성을 고객 프로필에 기록해야 합니다:

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 통합을 통해 설정하는 경우 커스텀 속성을 사용하려면 커스텀 HTML 태그를 생성해야 합니다. 다음은 이러한 값을 문자열이 아닌 부울 데이터 유형으로 기록하는 방법의 예시입니다:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

자세한 내용은 [Google에 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/)를 참조하세요.