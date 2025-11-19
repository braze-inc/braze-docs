[앱이나 웹사이트에 게재 위치를 만들면]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh) 앱은 각 게재 위치에 대한 배너 메시지를 가져오기 위해 Braze에 요청을 보냅니다.  

- **사용자 세션당** 최대 **10개의 게재 위치를** 요청할 수 있습니다.  
- 각 배치에 대해 Braze는 사용자가 받을 수 있는 **가장 높은 우선순위의 배너를** 반환합니다.  
- 한 세션에 10개 이상의 게재 위치가 요청되면 처음 10개만 반환되고 나머지는 삭제됩니다.  

예를 들어 앱이 단일 세션 동안 세 번의 게재 위치를 요청할 수 있습니다: `homepage_promo`, `cart_abandonment`, 그리고 `seasonal_offer`. 각 요청은 해당 게재 위치에 가장 관련성이 높은 배너를 반환합니다.
