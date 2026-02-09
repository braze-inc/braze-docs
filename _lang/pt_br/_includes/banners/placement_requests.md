Quando você [cria posicionamentos em seu aplicativo ou site]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), seu app envia uma solicitação ao Braze para buscar mensagens de banner para cada posicionamento.  

- Você pode solicitar até **10 colocações por solicitação de atualização**.  
- Para cada colocação, o Braze retorna o **Banner de maior prioridade** que o usuário é elegível para receber.  
- Se mais de 10 posicionamentos forem solicitados em uma atualização, apenas os 10 primeiros serão retornados; os demais serão descartados.  

Por exemplo, um app pode solicitar três posicionamentos em uma solicitação de atualização: `homepage_promo`, `cart_abandonment`, e `seasonal_offer`. Cada solicitação retorna o banner mais relevante para aquele posicionamento.

#### Limite de frequência para solicitações de atualização

Se você estiver em versões mais antigas do SDK (antes de Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 e Flutter 15.0.0), somente uma solicitação de atualização é permitida por sessão de usuário.

Se você estiver em versões mais recentes do SDK mínimo (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ e Flutter 15.0.0+), as solicitações de atualização serão controladas por um algoritmo de token bucket para evitar o polling excessivo:

- Cada sessão de usuário começa com cinco tokens de atualização.
- Os tokens são recarregados a uma taxa de um token a cada 180 segundos (3 minutos).

Cada chamada para `requestBannersRefresh` consome um token. Se tentar uma atualização quando não houver tokens disponíveis, o SDK não fará a solicitação e registrará um erro até que um token seja reabastecido. Isso é importante para atualizações no meio da sessão e disparadas por eventos. Para implementar atualizações dinâmicas (por exemplo, depois que um usuário concluir uma ação na mesma página), chame o método refresh depois que o evento personalizado for registrado, mas note a postergação necessária para que o Braze ingira e processe o evento antes que o usuário se qualifique para uma campanha de Banner diferente.
