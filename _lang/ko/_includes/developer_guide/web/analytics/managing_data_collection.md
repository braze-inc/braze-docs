## 데이터 추적 비활성화하기

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
웹 소프트웨어 개발 키트에서 데이터 추적 활동을 비활성화하려면 방법 [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). 이렇게 하면 `disableSDK()` 호출 이전에 기록된 모든 데이터가 동기화되며, 이후 이 페이지 및 향후 페이지 로드에 대한 모든 Braze 웹 소프트웨어 개발 키트 호출이 무시됩니다.
{% endtab %}

{% tab google tag manager %}
**추적 비활성화** 또는 **추적 재개** 태그 유형을 사용하여 각각 웹 추적을 비활성화하거나 다시 활성화합니다. 이 두 가지 옵션은 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) 및 [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)를 호출합니다.
{% endtab %}
{% endtabs %}

### Best practices

사용자에게 추적 중지 옵션을 제공하려면 클릭 시 `disableSDK()` 으로 연결되는 링크와 `enableSDK()` 으로 연결되는 링크 또는 버튼 두 개로 구성된 간단한 페이지를 구축하여 사용자가 다시 옵트인할 수 있도록 하는 것이 좋습니다. 이러한 컨트롤을 사용하여 다른 데이터 하위 프로세서를 통한 추적을 시작하거나 중지할 수도 있습니다.

{% alert note %}
Braze 소프트웨어 개발 키트는 초기화할 필요 없이 `disableSDK()` 으로 호출하여 완전한 익명 사용자의 추적을 비활성화할 수 있습니다. 반대로 `enableSDK()`는 Braze SDK를 초기화하지 않으므로 추적을 활성화하려면 나중에 `initialize()`를 호출해야 합니다.
{% endalert %}

## 데이터 추적 재개하기

데이터 수집을 재개하려면 다음과 같이 [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) 메서드를 사용할 수 있습니다.
