---
nav_title: Insights de segmento
article_title: Insights de segmento
page_order: 4
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "Este artigo explica como usar, interpretar e compartilhar Insights de segmento."
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Insights de segmentos

> Saiba como usar, interpretar e compartilhar insights de segmento. 

O Segment Insights mostra como está a performance de um segmento em comparação com outro em um conjunto de KPIs pré-selecionados.

## Visualização de insights de segmento

Acesse a página **Segment Insights de** seu dashboard, em **Analytics**, e clique em <i class="fas fa-plus"></i> **Add Segment** para visualizar até quatro segmentos diferentes em comparação com uma linha de base.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Engajamento** > Segmentos > **Insights de segmento**.
{% endalert %}

![Dashboard de insights de segmento.][1]

O segmento de linha de base pode ser um segmento específico selecionado por você ou um segmento que contenha todos os seus usuários. Você pode comparar as seguintes estatísticas usando o Segment Insights:

| Medição | Descrição | Fórmula |
| --------------------- | ------------- | ------------- |
| Frequência das sessões | Número médio de sessões de usuários do segmento por dia | (total de sessões) / (número de dias desde a primeira sessão) |
| Tempo desde a primeira sessão | Tempo médio entre a primeira sessão dos usuários do segmento e agora | hoje - data da primeira sessão |
| Tempo desde a última sessão | Tempo médio entre a última sessão dos usuários do segmento e agora | today - data da última sessão |
| Receitas por tempo de vida | Receita média de tempo de vida para os usuários do segmento | gasto do usuário no tempo de vida |
| Tempo até a primeira compra | Tempo médio entre a primeira sessão dos segmentos dos usuários e a primeira compra | data da primeira compra - data da primeira sessão |
| Tempo desde a última compra | Tempo médio entre a última compra dos usuários do segmento e agora | today - data da última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode compartilhar facilmente comparações específicas com seus colegas de equipe usando o URL exclusivo da página e também pode clicar abaixo de cada segmento para revelar mais informações sobre esse segmento. Essas comparações serão redefinidas quando você alternar entre os espaços de trabalho.

![][2]

## Página de detalhes do segmento

Os insights de segmento também foram incorporados diretamente na visualização **de detalhes do segmento**. Ao examinar um segmento específico que você configurou anteriormente, é possível encontrar as mesmas seis estatísticas descritas na caixa cinza dinâmica Segment Statistics. A partir daqui, você pode iniciar rapidamente a ferramenta Segment Insights para comparar esse segmento específico com quaisquer outros que você tenha configurado anteriormente, mas note que isso substituirá quaisquer segmentos que você tenha selecionado anteriormente na ferramenta Segment Insights.

![][3]

## Casos de uso {#insights-use-cases}

### Comparação de padrões demográficos de uso e compra

Um dos melhores usos do Segment Insights é responder a perguntas sobre o impacto dos dados demográficos do usuário no uso do app e na eficácia da campanha, como, por exemplo:

- Determinados grupos demográficos de usuários estão apresentando desempenho significativamente melhor ou pior do que a média?
- Devo repensar a localização de uma determinada campanha?
- Uma campanha está engajando um determinado grupo demográfico?
- Que metas devo definir para uma campanha voltada para um determinado grupo demográfico?

Os insights de segmento podem ajudar a descobrir diferenças entre os dados demográficos dos usuários. O exemplo a seguir mostra uma comparação da base de usuários de um app por idioma, ilustrando como os falantes de inglês tendem a ter LTV e níveis de atividade mais altos do que os falantes de outros idiomas.

![][5]

Nesse exemplo, os falantes de alemão inscreveram-se há mais tempo, em média, o que pode explicar por que eles não estão mais tão ativos. Isso pode ser devido a uma série de fatores. Por exemplo, se o app foi lançado inicialmente na Europa, mas agora é mais popular nos EUA, onde a maioria das pessoas fala inglês ou espanhol. Para obter descobertas mais robustas, ao analisar os KPIs de acordo com a demografia, é sensato testar as descobertas de um estudo geral de demografia (por exemplo, se o idioma afeta o LTV em todos os usuários) analisando uma população menor e mais semelhante e verificando se as descobertas persistem.

Para melhorar as conversões entre falantes de outros idiomas que não o inglês, uma boa primeira etapa seria [localizar campanhas][10] para o idioma do dispositivo do usuário e certificar-se de que o texto dessas mensagens esteja engajando os usuários usando uma [campanha multivariante][11] para testar diferentes versões do texto em idioma estrangeiro.

### Compreensão dos indicadores de maior receita

Fazer com que os usuários se convertam em compradores pode ser difícil, e tentar empurrar usuários novos, inativos ou desengajados diretamente para a compra pode levar o usuário a desinstalar seu app. Os insights de segmento podem ajudá-lo a descobrir ações que levam os usuários mais adiante no funil de compras sem exigir que eles comprem ainda, por exemplo, adicionando itens à lista de desejos, compartilhando nas redes sociais ou favoritando conteúdo. Por exemplo, é possível mapear o impacto em diferentes comportamentos de compra em um app de comércio eletrônico.

![][7]

Nesse caso, relativamente poucos usuários estão inscritos no boletim informativo, mas esses usuários geralmente são mais ativos. Para manter os novos usuários engajados, seria uma boa ideia incluir um convite para solicitar o boletim informativo nas campanhas de integração. Para reengajar usuários inativos, é interessante enviar uma campanha típica de [usuários inativos][9]] e direcionar [usuários que converteram][12]] com uma campanha subsequente para inscrever-se na newsletter.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
