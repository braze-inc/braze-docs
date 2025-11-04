---
nav_title: Campanha ou tela não acionada
article_title: Campanha ou tela não acionada
page_order: 5

page_type: solution
description: "Este artigo de ajuda o orienta nas etapas para resolver problemas com campanhas ou Canvas que não estão sendo disparados conforme o esperado."
tool: 
- Campaigns
- Canvas
---

# Campanha não acionada ou Canva

Há vários motivos pelos quais você não obteve o comportamento esperado do disparador. A solução para o erro mais comum é garantir que a campanha que você está disparando não use o mesmo evento de gatilho no segmento.

## Disparos de campanha

A associação ao segmento é avaliada antes das ações-gatilho. Isso significa que, se o usuário não se enquadrar no segmento primeiro, ele não receberá a campanha mesmo que ela seja disparada.

Se sua campanha for disparada a partir de um evento personalizado, você deverá certificar-se de que esse evento não seja pré-filtrado por um segmento que deseja usar na campanha. 

Por exemplo, se o segmento incluir o evento `SessionStart` "Has Used App more than once" (Usou o app mais de uma vez) e o evento que dispara a campanha for `SessionStart`, o usuário receberá a mensagem, mas não necessariamente na primeira sessão. Isso ocorre porque, durante a primeira etapa, ao verificar se um usuário deve receber uma campanha, a campanha está analisando o público-alvo do segmento. 

Em resumo, evite configurar uma campanha baseada em ação ou um Canva com o mesmo disparo que o filtro de público (como um atributo alterado ou a realização de um evento personalizado). Pode ocorrer uma [condição de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/) em que o usuário não esteja no público quando executar o evento de gatilho, o que significa que ele não receberá a campanha nem entrará no Canva.

{% alert tip %}
Para obter mais assistência com a solução de problemas da campanha, certifique-se de entrar em contato com o suporte da Braze dentro de 30 dias após a ocorrência do seu problema, pois só temos os últimos 30 dias de logs de diagnóstico.
{% endalert %}

_Última atualização em 25 de junho de 2024_

