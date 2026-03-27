Quando você [cria colocações no seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), seu app envia uma solicitação para a Braze buscar mensagens de Banner para cada colocação.  

- Você pode solicitar até **10 colocações por solicitação de atualização**.  
- Para cada colocação, a Braze retorna o **Banner de maior prioridade** que o usuário é elegível para receber.  
- Se mais de 10 colocações forem solicitadas em uma atualização, apenas as primeiras 10 são retornadas; as demais são descartadas.  

Por exemplo, um app pode solicitar três colocações em uma solicitação de atualização: `homepage_promo`, `cart_abandonment` e `seasonal_offer`. Cada solicitação retorna o Banner mais relevante para aquela colocação.

#### Limitação de taxa para solicitações de atualização

Se você estiver em versões mais antigas do SDK (antes do Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 e Flutter 15.0.0), apenas uma solicitação de atualização é permitida por sessão de usuário.

Se você estiver em versões mínimas mais novas do SDK (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ e Flutter 15.0.0+), as solicitações de atualização são controladas por um algoritmo de token bucket para evitar polling excessivo:

- Cada sessão de usuário começa com cinco tokens de atualização.
- Os tokens se reabastecem a uma taxa de um token a cada 180 segundos (3 minutos).

Cada chamada para `requestBannersRefresh` consome um token. Se você tentar uma atualização quando não houver tokens disponíveis, o SDK não faz a solicitação e registra um erro até que um token seja reabastecido. Isso é importante para atualizações durante a sessão e atualizações acionadas por eventos. Para implementar atualizações dinâmicas (por exemplo, após um usuário completar uma ação na mesma página), chame o método de atualização após o evento personalizado ser registrado, mas observe o atraso necessário para a Braze ingerir e processar o evento antes que o usuário se qualifique para uma campanha de Banner diferente.
