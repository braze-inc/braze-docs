## 웹용 Google 태그 관리자 정보 {#google-tag-manager}

Google 태그 관리자(GTM)를 사용하면 프로덕션 코드 릴리스나 엔지니어링 리소스 없이도 웹사이트에 원격으로 태그를 추가, 제거, 편집할 수 있습니다. Braze는 웹 소프트웨어 개발 키트를 위해 다음과 같은 템플릿을 제공합니다:

|태그 유형|사용 사례|
|--------|--------|
| 초기화 태그 | 이 태그를 사용하면 사이트의 코드를 수정할 필요 없이 [Web Braze SDK를 통합할]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) 수 있습니다.|
| 액션 태그 | 이 태그를 사용하면 [콘텐츠 카드를 만들고]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [사용자 속성을 설정하고]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web), [데이터 수집을 관리할]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web) 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Google의 EU 사용자 동의 정책

{% alert important %}
Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html) 개정 사항에 따라 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항에 따라 광고주는 EEA 및 영국 최종 사용자에게 특정 정보를 공개하고 해당 사용자로부터 필요한 동의를 얻어야 합니다. 자세한 내용은 다음 문서를 참조하세요.
{% endalert %}

Google의 EU 사용자 동의 정책의 일환으로 다음 부울 커스텀 속성을 고객 프로필에 기록해야 합니다.

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 통합을 통해 설정하는 경우 커스텀 속성을 사용하려면 커스텀 HTML 태그를 생성해야 합니다. 다음은 이러한 값을 문자열이 아닌 부울 데이터 유형으로 기록하는 방법의 예시입니다:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

자세한 내용은 [Google에 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/)를 참조하세요.
