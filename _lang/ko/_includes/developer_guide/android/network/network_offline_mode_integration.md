# 네트워크 오프라인 모드

> [네트워크 오프라인 모드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean)는 런타임 중 언제든지 Braze SDK의 아웃바운드 네트워크 요청을 일시 중지하거나 재개할 수 있는 선택적 기능입니다. 오프라인 상태에서도 이벤트는 손실되지 않습니다. 이 참조 문서에서는 이 모드를 통합하는 방법에 대해 설명합니다.

## 사용 예

Braze SDK에서 네트워크 오프라인 모드를 활성화하려면 다음 예제를 참조하세요.

{% tabs %}
{% tab 자바 %}

```java
Braze.setOutboundNetworkRequestsOffline(true);
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.setOutboundNetworkRequestsOffline(true)
```

{% endtab %}
{% endtabs %}

