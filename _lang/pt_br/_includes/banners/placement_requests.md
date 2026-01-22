Quando você [cria posicionamentos em seu aplicativo ou site]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), seu app envia uma solicitação ao Braze para buscar mensagens de banner para cada posicionamento.  

- Você pode solicitar até **10 posicionamentos por sessão de usuário**.  
- Para cada colocação, o Braze retorna o **Banner de maior prioridade** que o usuário é elegível para receber.  
- Se mais de 10 colocações forem solicitadas em uma sessão, apenas as 10 primeiras serão retornadas; as demais serão descartadas.  

Por exemplo, um app pode solicitar três posicionamentos durante uma única sessão: `homepage_promo`, `cart_abandonment`, e `seasonal_offer`. Cada solicitação retorna o banner mais relevante para aquele posicionamento.
