---
nav_title: Painel de controle doméstico
article_title: Home Dashboard (Visão geral anterior)
page_order: 1
page_type: reference
description: "Este artigo de referência descreve seu painel Home e fornece definições para as estatísticas disponíveis nessa página."
tool: 
  - Reports

---

# Painel inicial

> A página **inicial** do painel fornece as principais métricas para que você acompanhe e compreenda o desempenho do seu aplicativo ou site e oferece uma compreensão rápida e de alto nível da sua base de usuários.

A página **inicial** tem duas seções principais:
- [Continue de onde você parou](#pick-up-where-you-left-off)
- [Visão geral do desempenho](#peformance-overview)

Painel de controle doméstico no Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Continue de onde você parou

Você pode continuar de onde parou no painel de controle do Braze com acesso direto aos arquivos que editou ou criou recentemente. Essa seção aparece na parte superior da página **inicial** do painel de controle do Braze.

Você pode revisitar campanhas, Canvases e segmentos recentemente editados ou criados. Cada cartão é associado a tags que indicam o tipo de conteúdo (campanha, Canvas, segmento) e o status (ativo, rascunho, arquivado, parado).

{% alert note %}
A seção **Continuar de onde parou** aparece depois que você editou ou criou uma campanha, um Canvas ou um segmento.
{% endalert %}

\![Um rascunho do Canvas, um segmento ativo e um rascunho de campanha na seção "Continue de onde parou".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Visão geral do desempenho

Por padrão, a seção **Visão geral do desempenho** mostra os últimos 30 dias de dados de todos os aplicativos e sites. Suas métricas são todas calculadas com base no intervalo de datas selecionado.

Campos de intervalo de datas e aplicativos no painel inicial.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

As porcentagens são calculadas com base no intervalo de datas atual em comparação com o intervalo de datas anterior, com exceção dos *usuários ativos mensais* (MAU), que usam o último dia do período anterior em vez de um intervalo. 

Por exemplo, se você definir seu intervalo de datas como **Last 7 Days (Últimos 7 dias** ) e seus *Daily Active Users (Usuários ativos diários* ) mostrarem um aumento percentual de 1,8%, isso significa que você teve 1,8% mais usuários ativos diários nesta semana em comparação com a semana passada.

\![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Mostrar detalhamento

Selecione **Show Breakdown** para cada linha das estatísticas da visão geral do desempenho para visualizar o valor de cada estatística por dia para o intervalo de datas especificado.

\![Expandir]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

## Estatísticas disponíveis

Veja a seguir as definições de suas estatísticas disponíveis, como as calculamos e por que elas devem ser importantes para você.

### Usuários

*Usuários* é o número total de usuários criados nesse espaço de trabalho. Isso inclui todos os usuários que registramos usando seu aplicativo ou site em qualquer momento, e aqueles que podem não estar associados a um aplicativo ou site específico. Esse número é a porcentagem de quantos dos seus usuários vitalícios são representados como *usuários ativos mensais* (MAU), o que é útil para ver a retenção de usuários por um longo período de tempo.

Uma baixa relação MAU/usuário pode indicar que você precisa diversificar seus canais de mensagens ou aumentar seus esforços para alcançar os usuários que estão perdendo tempo. Para obter mais informações, consulte nossa vitória rápida sobre a [captura de usuários com lapsos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users). Em geral, a relação MAU/vida útil inevitavelmente diminuirá com o tempo devido à rotatividade de usuários, mas as ferramentas do Braze podem ajudá-lo a minimizar esse efeito, mantendo os usuários engajados por mais tempo.

### Sessões vitalícias

*Sessões vitalícias* é a contagem total de sessões que o Braze registrou desde a integração. Em termos simples, uma sessão é cada vez que um usuário usa o aplicativo ou visita seu site. Para obter uma definição mais precisa sobre como as sessões são definidas por plataforma, consulte o
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), ou artigos de desenvolvedor de rastreamento de sessão [da Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

### Usuários ativos mensais

*Usuários ativos mensais* (MAU) é o número de usuários que registraram uma sessão em seu aplicativo ou site nos últimos 30 dias. As MAUs são calculadas todas as noites com uma janela contínua de 30 dias. O MAU fornece uma boa compreensão da saúde de um aplicativo ou site durante um longo período de tempo, pois suaviza as inconsistências entre dias de intensidade de uso variável.

A porcentagem ao lado da contagem de MAU mostra a mudança na MAU para esse período em comparação com o período anterior.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

{% alert note %}
Os usuários anônimos também contam para o seu MAU. Para dispositivos móveis, os usuários anônimos dependem do dispositivo. Para usuários da Web, os usuários anônimos dependem do cache do navegador.
{% endalert %}

### Usuários ativos diários

*Usuários ativos diários* (DAU) exibe o número de usuários únicos que registram pelo menos uma sessão no seu aplicativo ou site em um determinado dia. A DAU pode ser uma estatística útil para examinar a variabilidade diária do uso de seu aplicativo ou site e adaptar suas campanhas de mensagens para que sejam o mais eficazes possível. Por exemplo, o uso do seu aplicativo pode ter um aumento considerável nos fins de semana - isso informaria que você poderia alcançar mais usuários com mensagens no aplicativo nesses dias, em vez de nos dias úteis.

### Novos usuários

*Novos usuários* informa quantos usuários que nunca haviam registrado uma sessão começaram a usar seu aplicativo ou site. Esse número é um total de novos usuários durante o período de tempo determinado. Essa estatística pode ser muito valiosa para monitorar a eficácia de seus esforços de publicidade.

{% alert note %}
Quando você integrar o Braze inicialmente, todos os usuários parecerão novos porque o Braze nunca registrou uma sessão para eles antes.
{% endalert %}

### Aderência

O valor de *aderência* é uma relação entre DAU e MAU de um determinado período. Em essência, a aderência mede a porcentagem de seus MAUs que retornam diariamente.

Por exemplo, se o intervalo de datas for definido como 30 dias, uma proporção de 50% indica que, em média, um usuário ativo está usando o aplicativo ou o site por 15 dos 30 dias ou que cerca de metade dos seus usuários ativos retorna diariamente. A aderência é uma métrica importante para o sucesso, pois a maioria dos usuários não deixa de usar um aplicativo porque o detesta, mas sim porque ele não se tornou parte de sua rotina diária. Portanto, você pode usar a aderência como um indicador para medir o grau de envolvimento dos usuários.

A porcentagem ao lado do índice de aderência mostra a mudança na aderência para esse período em comparação com o período anterior.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Os períodos de tempo para "último período" e "este período" são determinados pelo intervalo de datas que você selecionar.

{% alert important %}
O valor MAU é calculado todas as noites e não será atualizado até o dia seguinte.
{% endalert %}

### Sessões diárias

*Sessões diárias* é o número de sessões registradas em um determinado dia. A comparação desse valor com sua contagem de DAU pode informá-lo sobre quantas vezes seus usuários abrem o aplicativo ou visitam seu site nos dias em que registram pelo menos uma sessão.

### Sessões diárias por MAU

*Sessões diárias por MAU* é a proporção de *sessões diárias* para MAU em um determinado dia. Essa estatística informa quantas sessões por dia podem ser registradas por MAU. Quando agregados e calculados, isso pode lhe dar uma ideia da frequência relativa de quando os usuários usam seu aplicativo ou site. Ou seja, se suas *sessões diárias por MAU* forem, em média, 0,5, então você pode esperar que cada MAU registre uma sessão a cada dois dias.  

