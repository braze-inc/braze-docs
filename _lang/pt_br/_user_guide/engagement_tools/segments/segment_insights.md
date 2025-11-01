---
nav_title: Informações sobre o segmento
article_title: Informações sobre o segmento
page_order: 8
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "Este artigo explica como usar, interpretar e compartilhar o Segment Insights."
---

# [Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Insights sobre o segmento

> Saiba como usar, interpretar e compartilhar o Segment Insights. 

O Segment Insights mostra o desempenho de um segmento em comparação com outro em um conjunto de KPIs pré-selecionados.

## Visualização de informações sobre o segmento

Vá para a página **Segment Insights** de seu painel, em **Analytics**, e visualize até 10 segmentos diferentes comparados com uma linha de base.

Painel do Segment Insights comparando três segmentos, "Usuários do Reino Unido", "Usuários da França" e "Usuários da Califórnia", com um segmento de linha de base, "Todos os usuários".]({% image_buster /assets/img_archive/segment_insights.png %})

O segmento de linha de base pode ser um segmento específico selecionado por você ou um segmento que contenha todos os seus usuários. Você pode comparar as seguintes estatísticas usando o Segment Insights:

| Medição | Descrição | Fórmula |
| --------------------- | ------------- | ------------- |
| Sessões por dia | Número médio de sessões de usuários do segmento por dia | (número total de sessões) / (número de dias desde a primeira sessão) |
| Dias desde a primeira sessão | Número médio de dias entre a primeira sessão dos usuários do segmento e agora | hoje - data da primeira sessão |
| Dias desde a última sessão | Número médio de dias entre a última sessão dos usuários do segmento e a atual | today - data da última sessão |
| Receita vitalícia em dólares | Receita média vitalícia em dólares para usuários do segmento | gasto vitalício do usuário |
| Dias desde a primeira compra | Número médio de dias entre a primeira sessão dos usuários do segmento e a primeira compra | data da primeira compra - data da primeira sessão |
| Dias desde a última compra | Número médio de dias entre a última compra dos usuários do segmento e agora | today - data da última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode compartilhar facilmente comparações específicas com seus colegas de equipe usando o URL exclusivo da página, e também pode selecionar o ícone de olho ao lado de cada segmento para revelar mais informações sobre esse segmento. Essas comparações serão redefinidas quando você alternar entre os espaços de trabalho.

Detalhes do segmento "Usuários Premium (iOS VideoApp)" com um gráfico que exibe o histórico de associação e um gráfico que divide o tamanho estimado para vários canais de mensagens.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Página de detalhes do segmento

O Segment Insights também foi incorporado diretamente na visualização **Segment Details**. Ao examinar um segmento específico que você configurou anteriormente, é possível encontrar as mesmas seis estatísticas descritas na caixa cinza dinâmica Segment Statistics. A partir daqui, você pode iniciar rapidamente a ferramenta Segment Insights para comparar esse segmento específico com qualquer outro que você tenha configurado anteriormente, mas observe que isso substituirá qualquer segmento que você tenha selecionado anteriormente na ferramenta Segment Insights.

\![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Casos de uso {#insights-use-cases}

### Comparação de padrões demográficos de uso e compra

Um dos melhores usos do Segment Insights é responder a perguntas sobre o impacto dos dados demográficos do usuário no uso do aplicativo e na eficácia da campanha, como, por exemplo:

- Determinados dados demográficos dos usuários têm um desempenho significativamente melhor ou pior do que a média?
- Devo repensar a localização de uma determinada campanha?
- Uma campanha está engajando um determinado grupo demográfico?
- Que metas devo definir para uma campanha voltada para um determinado grupo demográfico?

O Segment Insights pode ajudar a descobrir diferenças entre os dados demográficos dos usuários. O exemplo a seguir mostra uma comparação da base de usuários de um aplicativo por idioma, ilustrando como os falantes de inglês tendem a ter LTV e níveis de atividade mais altos do que os falantes de outros idiomas.

Detalhamento do Segment Insights para os segmentos inglês, alemão, francês e espanhol.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

Neste exemplo, os falantes de alemão se inscreveram há mais tempo, em média, o que pode explicar por que eles não estão mais tão ativos. Isso pode ser devido a uma série de fatores. Por exemplo, se o aplicativo foi lançado inicialmente na Europa, mas agora é mais popular nos EUA, onde a maioria das pessoas fala inglês ou espanhol. Para obter descobertas mais robustas, ao analisar os KPIs de acordo com a demografia, é sensato testar as descobertas de um estudo geral de demografia (por exemplo, se o idioma afeta o LTV em todos os usuários) analisando uma população menor e mais semelhante e verificando se as descobertas persistem.

Para melhorar as conversões entre falantes de outros idiomas que não o inglês, uma boa primeira etapa seria [localizar as campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) para o idioma do dispositivo do usuário e certificar-se de que o texto dessas mensagens está envolvendo os usuários usando uma [campanha multivariada]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests) para testar diferentes versões do texto em idioma estrangeiro.

### Compreensão dos indicadores de maior receita

Fazer com que os usuários se convertam em compradores pode ser difícil, e tentar empurrar usuários novos, inativos ou desengajados diretamente para a compra pode levar o usuário a desinstalar seu aplicativo. O Segment Insights pode ajudá-lo a descobrir ações que levam os usuários mais adiante no funil de compras sem exigir que eles comprem ainda, por exemplo, assinar seu boletim informativo, compartilhar nas mídias sociais ou inscrever-se para receber mensagens promocionais. Por exemplo, você pode mapear o impacto em compras de diferentes comportamentos em um aplicativo de comércio eletrônico.

Detalhamento do Segment Insights para usuários que compartilharam em mídias sociais, inscreveram-se em promoções e assinaram o boletim informativo.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

Nesse caso, relativamente poucos usuários estão atualmente inscritos para receber mensagens promocionais e não estão tão ativos, mas esses usuários geram uma receita vitalícia maior. Para aumentar a receita, pode ser uma boa ideia incluir um convite para se inscrever para receber mensagens promocionais nas campanhas de integração. Para reengajar os usuários que perderam a conexão, um bom plano seria enviar uma [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) típica para usuários que perderam a conexão e direcionar [os usuários que converteram]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter) com uma campanha subsequente para se inscreverem para receber mensagens promocionais.

