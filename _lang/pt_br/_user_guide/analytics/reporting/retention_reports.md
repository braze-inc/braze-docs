---
nav_title: Relatórios de retenção
article_title: Relatórios de Retenção para Campanhas e Canvas
page_order: 5
tool: Reports
page_type: reference
description: "Esta página explica como medir a retenção de usuários que realizaram um evento de retenção selecionado em uma campanha ou Canva específico."
---

# Relatórios de retenção

> A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter os usuários engajados voltando para mais indica que o negócio está saudável. Braze permite que você meça a retenção de usuários diretamente na página de **análise de dados** da sua campanha ou canva.

{% alert important %}
Relatórios de Retenção não estão disponíveis para campanhas acionadas por API.
{% endalert %}

## Execução de um relatório de retenção

### Etapa 1: Selecione um intervalo de datas

![Data do relatório]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Comece visitando qualquer campanha ou canva no seu dashboard do Braze e selecione um intervalo de datas para o seu relatório. Selecionar um intervalo de datas apropriado é crucial por causa da maneira como isso afeta os relatórios de retenção. 

Este relatório incluirá todos os usuários que inicialmente entraram na campanha ou canva durante este período, e desses usuários, os dados daqueles que realizaram seu evento de retenção durante o intervalo de datas aparecerão no relatório.

Para selecionar um intervalo de datas, navegue até a página da campanha ou do Canva **Analytics** e selecione vários intervalos ou defina um intervalo personalizado para seu relatório.

### Etapa 2: Selecione um evento de retenção

{% tabs %}
{% tab Campanha %}

Em seguida, acesse a seção **Retenção de campanha**. A retenção da campanha mostra a taxa na qual qualquer usuário que recebeu esta campanha específica realizou um evento de retenção (especificado por você no relatório de retenção) ao longo dos 30 dias a partir do momento em que recebeu a campanha.

{% endtab %}
{% tab Canva %}

Em seguida, selecione **Analisar variantes**. A partir daqui, você pode analisar suas variantes, conferir seu relatório de funil e visualizar seu relatório de retenção. A retenção da canva mostra a taxa na qual qualquer usuário que recebeu esta canva específica realizou um evento de retenção (especificado por você no relatório de retenção) ao longo dos 30 dias a partir do momento em que recebeu a canva.

{% endtab %}
{% endtabs %}

![Selecione um evento de retenção]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Etapa 3: Gerar o relatório

Depois de selecionar um evento de retenção, selecione **Gerar relatório** para iniciar a consulta.

![Relatório de execução]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Essa consulta pode levar alguns minutos para ser executada, dependendo do volume de dados precisa ser recuperado para gerar os resultados. Se demorar muito, você verá uma notificação pedindo para tentar carregar o relatório novamente. Você pode precisar esperar até cinco minutos antes que o relatório seja carregado.

Depois que o relatório é gerado, ele não pode ser executado novamente com o mesmo evento de retenção por 24 horas. Você sempre verá um carimbo de data/hora de quando o relatório foi gerado pela última vez e uma opção para regenerar, se já tiver passado mais de um dia. Você pode, no entanto, alterar o evento de retenção e reexecutar o relatório para observar o impacto da campanha em diferentes KPIs.

O relatório listará apenas os dias em que a campanha ou canva estava enviando mensagens. Para algumas campanhas e canvas, isso pode significar que o relatório mostra apenas um dia se foi enviado apenas uma vez. Se for recorrente ou acionado, você pode ver vários dias na tabela.

{% tabs %}
{% tab Campanha %}

![Relatório Completo]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Relatório Completo]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explicação do relatório

O relatório de retenção oferece tanto uma fórmula de retenção contínua quanto uma fórmula de retenção de intervalo. Para visualizar sua campanha ou relatório de canva com um desses tipos de retenção, selecione **Retenção Contínua** ou **Retenção por Intervalo** para seu **Tipo de Retenção**.

### Retenção contínua

A retenção contínua mede quantos usuários retornam e realizam o evento de retenção no ou após qualquer um dos dias listados no topo do relatório. Portanto, se um usuário iniciou uma sessão entre o terceiro e o sétimo dia, ele será contado como retido nas colunas "3 dias", "1 dia" e "0 dias". Qualquer usuário que for contado como retido após o marco de 30 dias a partir do envio da campanha ou canva será contado na coluna "30 dias" nessa linha.

Um usuário que completa o evento várias vezes durante um período de 30+ dias será contado como parte de vários períodos de tempo. Por exemplo, um usuário que concluir uma sessão após um dia será incrementado nas colunas >0 e >1. Se eles concluírem o evento após três dias, eles serão novamente incrementados nas colunas anteriores (>0 e >1), o que pode resultar em uma taxa de retenção superior a 100%.

#### Como ler relatórios de retenção contínua

A maneira de ler o gráfico do relatório de retenção para uma coluna do terceiro dia seria Y% ou Y número de usuários (com base nas unidades escolhidas) que realizaram o evento três ou mais dias depois de receber a campanha no dia Z.

![Relatório Contínuo]({% image_buster /assets/img/campaign_retention3.png %})

Como outro exemplo, referindo-se à tabela na imagem anterior, no dia 25 de março, um total de 38 usuários realizaram o evento de retenção. A retenção no dia zero foi de 68,42%, o que significa que 68,42% dos usuários realizaram o evento de retenção zero ou mais dias (no dia zero ou depois) após o recebimento da campanha. A retenção no sétimo dia foi de 57,89%, o que significa que 57,89% dos usuários realizaram o evento sete ou mais dias (no sétimo dia ou depois) após receberem a campanha.

Esta informação pode ser útil se você quiser saber a porcentagem de usuários que usaram e não usaram seu produto 30+ dias após o primeiro uso. Um valor percentual ou numérico na coluna do dia 30 informa a porcentagem de usuários que retornaram no dia 30 ou depois.

### Retenção de alcance

As medidas de retenção de intervalo mostram quantos usuários retornam no intervalo de dias listados no topo do relatório. Portanto, se um usuário iniciasse uma sessão entre os dias três e sete e depois novamente no dia 13, ele seria contado como retido nos intervalos "Dia 3-7" e "Dia 7-14".

#### Como ler relatórios de retenção de alcance

Relatórios de Intervalo são alguns dos relatórios mais intuitivos de ler. Eles afirmam claramente, de todos os usuários em uma coorte, qual porcentagem desses usuários realizou o evento de retenção dentro de um intervalo de datas específico. Por exemplo, na imagem a seguir, referenciando a coorte de Todos os Usuários, no intervalo de datas "Dia 0 (0-24hrs)", 35,71% da coorte realizou o relatório de retenção. Se um usuário realizar vários eventos de retenção em vários intervalos de datas, ele será contado como retido para cada intervalo.

![Relatório de retenção]({% image_buster /assets/img/range_retention.png %})

### Componentes do relatório de retenção

- **Coluna de Usuários**: O valor mostrado é o número de usuários únicos que realizaram a ação de início dentro do período de tempo selecionado; a contagem de usuários para o dia presente será excluída, pois está sendo calculada. 
- **Linhas Z de coorte**: Mostra os dias em que a campanha ou canva estava enviando mensagens.
- **Dia X Colunas**: Dias variando entre 0 e 30 dias em vários incrementos.
- **Todos os Usuários**: Também conhecido como a Linha de Resumo do Relatório, resume os dados de retenção para todo o período de tempo. Nota que se um usuário recebeu a campanha ou canva em vários grupos, seus resultados serão contados duas vezes aqui. 
- **Percentagens/Números**: Mostra a porcentagem ou o número de usuários que realizaram o evento X ou mais dias após receberem a campanha ou canva no dia Z. Essas porcentagens são as porcentagens médias ponderadas. Valores incompletos serão denotados por um asterisco.
- **Intervalo de Datas**: Defina na página de campanha ou canva **Detalhes**, o intervalo de datas inclui todos os usuários que receberam a campanha ou canva durante este período, e desses usuários, os dados daqueles que realizaram seu evento de retenção durante o intervalo de datas aparecerão no relatório.
- **Unidades**: Você pode ajustar as unidades entre a porcentagem de usuários e o número de usuários no canto superior direito do gráfico, unidades específicas podem ser mais significativas ao julgar o impacto de uma campanha ou canva.
- **Mapeamento de Cores**: No seu relatório de retenção, maiores porcentagens ou número de usuários são atribuídos a tons mais escuros de azul. Porcentagens mais baixas ou número de usuários são atribuídos a tons mais claros de azul. Isso é feito para ajudar os usuários a visualizar esses dados.
- **Gráfico do relatório de retenção**: Este gráfico resume os resultados de todas as coortes para o intervalo de datas selecionado.

### performance por variante

Visualizar seu relatório de retenção por variante permite comparar a retenção contínua para cada variante ou variação de mensagem para o período de tempo selecionado, assim como o grupo de controle. Este relatório pode ser visualizado alternando **Mostrar Performance Para** para **Por Variante**.

Alguns casos de uso para mostrar performance por variante:

- Tem algumas variantes ou experimentos em que os resultados parecem um esforço desperdiçado ou não têm significância estatística? Dê outra olhada e veja se um ou outro teve um impacto de cauda mais longo.
- Veja como é a retenção se você não enviou uma mensagem, analisando os dados de retenção do grupo de controle.

{% tabs %}
{% tab Campanha %}

![Ver por Variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Ver por Variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Relatório de retenção por componentes variantes

- **Intervalo de Datas**: Definido na página **Detalhes** da Campanha ou Canva, o intervalo de datas inclui todos os usuários que receberam a campanha ou Canva durante este período, e, desses usuários, os dados daqueles que realizaram seu evento de retenção durante o intervalo de datas aparecerão no relatório. Cada dia a taxa de retenção, a variação percentual do grupo de controle, e a confiança são medidas.
- **Taxa de Retenção**: Mostra a taxa de retenção por variante. A taxa de retenção é equivalente ao número de usuários que realizaram o evento de retenção dividido pelo total de usuários que receberam a campanha ou canva.
- **Mudança Percentual em Relação ao Controle**: Quantifica a mudança percentual por variante do grupo de controle.
- **Confiança**: {% multi_lang_include metrics.md metric='Confidence' %} O Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle com um procedimento estatístico chamado Teste Z para calcular uma porcentagem de [confiança]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence).
- **Unidades**: Você pode ajustar as unidades entre a porcentagem de usuários e o número de usuários no canto superior direito do gráfico, unidades específicas podem ser mais significativas ao julgar o impacto de uma campanha ou canva.
- **Gráfico de Variantes**: Este gráfico resume os resultados por variante para o intervalo de datas selecionado.

## Coisas para procurar em seus relatórios de retenção

Relatórios de Retenção são fáceis de gerar, mas desafiadores de interpretar e agir. Para ajudar os profissionais de marketing, reunimos alguns tópicos e perguntas a serem considerados ao analisar seus Relatórios de Retenção.

- Considere as tendências do dia da semana para campanhas recorrentes (por exemplo, os grupos de segunda-feira têm um desempenho melhor do que os grupos de sábado?).
- Onde o impacto começa a diminuir? Isso pode ser um sinal de que uma nova campanha ou canva que visa os usuários naquele momento é necessária como outro impulso para a retenção. 
- Você está vendo fadiga de envio de mensagens?
- Uma otimização específica que você fez em uma campanha ou canva X dias atrás teve um impacto positivo?



