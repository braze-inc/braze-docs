---
nav_title: Página inicial do dashboard
article_title: Página inicial do dashboard (antes chamada de Visão geral)
page_order: 1
page_type: reference
description: "Este artigo de referência descreve seu dashboard Home e fornece definições para as estatísticas disponíveis nessa página."
tool: 
  - Reports

---

# Página inicial do dashboard

> A página **inicial** do dashboard fornece métricas importantes para que você rastreie e entenda a performance do seu app ou site, além de oferecer uma compreensão rápida e de alto nível da sua base de usuários.

A página **inicial** tem duas seções principais:
- [Continuar de onde parou](#pick-up-where-you-left-off)
- [Visão geral de performance](#peformance-overview)

![Home dashboard no Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Continuar de onde parou

Você pode continuar de onde parou no dashboard do Braze com acesso direto aos arquivos que editou ou criou recentemente. Essa seção aparece na parte superior da página **inicial** do dashboard do Braze.

Você pode revisitar campanhas, Canvas e segmentos recentemente editados ou criados. Cada cartão é emparelhado com tags que indicam o tipo de conteúdo (campanha, Canva, segmento) e o status (ativo, rascunho, arquivado, parado).

![Um rascunho do Canva, um segmento ativo e um rascunho de campanha na seção "Continue de onde parou".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Visão geral de performance

Por padrão, a seção **Visão geral da performance** mostra os últimos 30 dias de dados de todos os apps e sites. Suas métricas são todas calculadas com base no intervalo de datas selecionado.

![Intervalo de datas e campos de app no dashboard inicial.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

Os Currents são calculados com base no intervalo de datas atual em comparação com o intervalo de datas anterior, com exceção dos *Usuários ativos mensais* (MAU), que usam o último dia do período anterior em vez de um intervalo. 

Por exemplo, se você definir seu intervalo de datas como **Últimos 7 dias** e seus *Usuários ativos diários* mostrarem um aumento percentual de 1,8%, isso significa que você teve 1,8% mais usuários ativos diários nesta semana em comparação com a semana passada.

![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Mostrar detalhamento

Selecione **Show Breakdown** para cada linha das estatísticas da visão geral da performance para visualizar o valor de cada estatística por dia para o intervalo de datas especificado.

![Expandir]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

## Estatísticas disponíveis

Veja a seguir as definições de suas estatísticas disponíveis, como as calculamos e por que elas devem ser importantes para você.

### Usuários

*Usuários* é o número total de usuários criados nesse espaço de trabalho. Isso inclui todos os usuários que registramos usando seu app ou site em qualquer momento, e aqueles que podem não estar associados a um app ou site específico. Esse número é a porcentagem de quantos dos seus usuários vitalícios são representados como *Usuários ativos mensais* (MAU), o que é útil para ver a retenção de usuários durante um longo período de tempo.

Uma baixa relação MAU/usuário pode indicar que é necessário diversificar seus canais de envio de mensagens ou aumentar seus esforços para alcançar os usuários que estão perdendo tempo. Para obter mais informações, consulte nossa vitória rápida sobre a [captura de usuários com lapsos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users). Em geral, a relação MAU/vida útil inevitavelmente diminuirá com o tempo devido ao churn de usuários, mas as ferramentas do Braze podem ajudá-lo a minimizar esse efeito, mantendo os usuários engajados por mais tempo.

### Sessões vitalícias

*Sessões vitalícias* é a contagem total de sessões que o Braze registrou desde a integração. Em termos simples, uma sessão é cada vez que um usuário usa o app ou visita seu site. Para obter uma definição mais precisa sobre como as sessões são definidas por plataforma, consulte o
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), ou artigos de desenvolvedores sobre rastreamento de sessões na [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

### Usuários ativos mensais

*Usuários ativos mensais* (MAU) é o número de usuários que registraram uma sessão em seu app ou site nos últimos 30 dias. O MAU é calculado todas as noites em uma janela contínua de 30 dias. O MAU fornece uma boa compreensão da integridade de um app ou site durante um longo período de tempo, pois suaviza as inconsistências entre dias de intensidade de uso variável.

A porcentagem ao lado da contagem de MAU mostra a alteração em MAU para esse período em comparação com o período anterior.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

{% alert note %}
Os usuários anônimos também contam para o seu MAU. Para dispositivos móveis, os usuários anônimos dependem do dispositivo. Para usuários da Web, os usuários anônimos dependem do cache do navegador.
{% endalert %}

### Usuários ativos diários

*Os usuários ativos diários* (DAU) exibem o número de usuários exclusivos que registram pelo menos uma sessão no seu app ou site em um determinado dia. A DAU pode ser uma estatística útil para examinar a variabilidade diária do uso de seu app ou site e adaptar suas campanhas de mensagens para que sejam o mais eficazes possível. Por exemplo, o uso do seu app pode ter um aumento considerável nos fins de semana - isso informaria que você poderia alcançar mais usuários com mensagens no app nesses dias, em vez de nos dias úteis.

### de novos usuários

*Novos usuários* informa quantos usuários que nunca haviam registrado uma sessão começaram a usar seu app ou site. Esse número é um total de novos usuários durante o período de tempo determinado. Essa estatística pode ser muito valiosa para o rastreamento da eficácia de seus esforços de publicidade.

{% alert note %}
Ao integrar o Braze inicialmente, todos os usuários parecerão novos porque o Braze nunca registrou uma sessão para eles antes.
{% endalert %}

### Aderência

O valor de *aderência* é uma proporção entre o DAU e o MAU de um determinado período. Em essência, a aderência mede a porcentagem de seus MAUs que retornam diariamente.

Por exemplo, se o intervalo de datas for definido como 30 dias, uma proporção de 50% indica que, em média, um usuário ativo está usando o app ou o site por 15 dos 30 dias ou que cerca de metade dos seus usuários ativos voltam diariamente. A aderência é uma métrica importante para o sucesso porque a maioria dos usuários não deixa de usar um app porque o detesta, mas porque ele não se tornou parte de sua rotina diária. Portanto, é possível usar a aderência como um proxy para medir o grau de engajamento dos usuários.

A porcentagem ao lado do índice de aderência mostra a mudança na aderência para esse período em comparação com o período anterior.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Os períodos de tempo para "último período" e "este período" são determinados pelo intervalo de datas que você selecionar.

{% alert important %}
O valor MAU é calculado todas as noites e não será atualizado até o dia seguinte.
{% endalert %}

### Sessões diárias

*Sessões diárias* é o número de sessões registradas em um determinado dia. A comparação desse valor com sua contagem de DAU pode informá-lo sobre quantas vezes seus usuários abrem o app ou visitam seu site nos dias em que registram pelo menos uma sessão.

### Sessões diárias por MAU

*Sessões diárias por MAU* é a proporção de *sessões diárias* para MAU em um determinado dia. Essa estatística informa quantas sessões por dia podem ser registradas por MAU. Quando agregados e calculados, isso pode lhe dar uma ideia da frequência relativa de quando os usuários usam seu app ou site. Ou seja, se suas *sessões diárias por MAU* fossem, em média, 0,5, então você poderia esperar que cada MAU registrasse uma sessão a cada 2 dias.  

