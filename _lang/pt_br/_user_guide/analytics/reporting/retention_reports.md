---
nav_title: Relatórios de retenção
article_title: Relatórios de retenção para campanhas e telas
page_order: 5
tool: Reports
page_type: reference
description: "Esta página explica como medir a retenção de usuários para usuários que realizaram um evento de retenção selecionado em uma campanha ou Canvas específico."
---

# Relatórios de retenção

> A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter os usuários engajados voltando para mais indica que os negócios estão saudáveis. O Braze permite que você meça a retenção de usuários diretamente na página do **Analytics** da sua campanha ou tela.

{% alert important %}
Os Relatórios de retenção não estão disponíveis para campanhas acionadas por API.
{% endalert %}

## Execução de um relatório de retenção

### Etapa 1: Selecione um intervalo de datas

\![Data do relatório]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Comece visitando qualquer campanha ou tela em seu painel do Braze e selecione um intervalo de datas para seu relatório. A seleção de um intervalo de datas apropriado é crucial devido à maneira como afeta os relatórios de retenção. 

Esse relatório incluirá todos os usuários que entraram inicialmente na campanha ou no Canvas durante essa janela e, dentre esses usuários, os dados daqueles que realizaram o evento de retenção durante o intervalo de datas aparecerão no relatório.

Para selecionar um intervalo de datas, navegue até a página da campanha ou do Canvas **Analytics** e selecione vários intervalos ou defina um intervalo personalizado para seu relatório.

### Etapa 2: Selecione um evento de retenção

{% tabs %}
{% tab Campaign %}

Em seguida, vá para a seção **Campaign Retention (Retenção de campanha** ). A retenção de campanha mostra a taxa na qual qualquer usuário que recebeu essa campanha específica realizou um evento de retenção (especificado por você no relatório de retenção) durante os 30 dias a partir do momento em que recebeu a campanha.

{% endtab %}
{% tab Canvas %}

Em seguida, selecione **Analyze Variants (Analisar variantes**). A partir daí, você pode analisar suas variantes, verificar o relatório do funil e visualizar o relatório de retenção. A retenção do Canvas mostra a taxa na qual qualquer usuário que tenha recebido esse Canvas específico realizou um evento de retenção (especificado por você no relatório de retenção) nos 30 dias a partir do momento em que recebeu o Canvas.

{% endtab %}
{% endtabs %}

\![Selecione um evento de retenção]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Etapa 3: Gerar o relatório

Depois de selecionar um evento de retenção, selecione **Executar relatório** para iniciar a consulta.

Relatório de execução]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Essa consulta pode levar alguns minutos para ser executada, dependendo da quantidade de dados que precisam ser recuperados para gerar os resultados. Se demorar muito, você verá uma notificação solicitando que tente carregar o relatório novamente. Talvez seja necessário aguardar até cinco minutos para que o relatório seja carregado.

Depois que o relatório é gerado, ele não pode ser executado novamente com o mesmo evento de retenção por 24 horas. Você sempre verá um registro de data e hora de quando o relatório foi gerado pela última vez e uma opção para gerá-lo novamente, se já tiver passado mais de um dia. No entanto, você pode alterar o evento de retenção e executar novamente o relatório para analisar o impacto da campanha em diferentes KPIs.

O relatório listará apenas os dias em que a campanha ou o Canvas estava enviando mensagens. Para algumas campanhas e Canvases, isso pode significar que o relatório só mostra um dia se tiver sido enviado apenas uma vez. Se for recorrente ou acionado, você poderá ver vários dias na tabela.

{% tabs %}
{% tab Campaign %}

\![Relatório completo]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

\![Relatório completo]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explicação do relatório

O relatório de retenção oferece uma fórmula de retenção contínua e de retenção de intervalo. Para visualizar sua campanha ou relatório do Canvas com um desses tipos de retenção, selecione **Retenção contínua** ou **Retenção de intervalo** para o **Tipo de retenção**.

### Retenção de rolagem

A retenção contínua mede quantos usuários retornam e fazem o evento de retenção em ou após qualquer um dos dias listados na parte superior do relatório. Portanto, se um usuário iniciou uma sessão entre o terceiro e o sétimo dia, ele será contado como retido nas colunas "3 dias", "1 dia" e "0 dias". Qualquer usuário que seja contado como retido após a marca de 30 dias a partir da data de envio da campanha ou do Canvas será contado na coluna "30 dias" dessa linha.

Um usuário que concluir o evento várias vezes durante uma janela de mais de 30 dias será contado como parte de vários períodos de tempo. Por exemplo, um usuário que concluir uma sessão após um dia será incrementado nas colunas >0 e >1. Se eles concluírem o evento após três dias, eles serão novamente incrementados nas colunas anteriores (>0 e >1), o que pode resultar em uma taxa de retenção superior a 100%.

#### Como ler relatórios de retenção contínuos

A maneira de ler o gráfico do relatório de retenção para uma coluna do terceiro dia seria Y% ou Y número de usuários (com base nas unidades escolhidas) que realizaram o evento três ou mais dias depois de receber a campanha no dia Z.

\![Rolling Report]({% image_buster /assets/img/campaign_retention3.png %})

Como outro exemplo, referindo-se à tabela na imagem anterior, no dia 25 de março, um total de 38 usuários realizou o evento de retenção. A retenção no dia zero foi de 68,42%, o que significa que 68,42% dos usuários realizaram o evento de retenção zero ou mais dias (no dia zero ou depois) após o recebimento da campanha. A retenção no sétimo dia foi de 57,89%, o que significa que 57,89% dos usuários realizaram o evento sete ou mais dias (no sétimo dia ou depois) após receberem a campanha.

Essas informações podem ser úteis se você quiser saber a porcentagem de usuários que usaram e não usaram seu produto mais de 30 dias após o primeiro uso. Um valor percentual ou numérico na coluna do dia 30 informa a porcentagem de usuários que retornaram no dia 30 ou depois.

### Retenção de alcance

A retenção por intervalo mede quantos usuários retornam no intervalo de dias listado na parte superior do relatório. Portanto, se um usuário iniciasse uma sessão entre os dias três e sete e depois novamente no dia 13, ele seria contado como retido nos intervalos "Dia 3-7" e "Dia 7-14".

#### Como ler relatórios de retenção de alcance

Os relatórios de intervalo são alguns dos relatórios mais intuitivos de ler. Eles indicam claramente, de todos os usuários em uma coorte, qual porcentagem desses usuários realizou o evento de retenção dentro de um determinado intervalo de datas. Por exemplo, na imagem a seguir, com referência à coorte de todos os usuários, no intervalo de datas "Dia 0 (0-24 horas)", 35,71% da coorte executou o relatório de retenção. Se um usuário realizar vários eventos de retenção em vários intervalos de datas, eles serão contados como retidos para cada intervalo.

Relatório de retenção]({% image_buster /assets/img/range_retention.png %})

### Componentes do relatório de retenção

- **Coluna de usuários**: O valor mostrado é o número de usuários únicos que executaram a ação inicial dentro do período de tempo selecionado; a contagem de usuários para o dia atual será excluída, pois está sendo calculada. 
- **Linhas da Coorte Z**: Mostra os dias em que a campanha ou o Canvas estava enviando mensagens.
- **Dia X Colunas**: Dias que variam de 0 a 30 dias em vários incrementos.
- **Todos os usuários Row**: Também conhecida como Linha de resumo do relatório, resume os dados de retenção para todo o período. Observe que, se um usuário tiver recebido a campanha ou o Canvas em várias coortes, seus resultados serão contados duas vezes aqui. 
- **Porcentagens/números**: Mostra a porcentagem ou o número de usuários que realizaram o evento X ou mais dias após receberem a campanha ou o Canvas no dia Z. Essas porcentagens são as porcentagens médias ponderadas. Os valores incompletos serão indicados por um asterisco.
- **Intervalo de datas**: Definido na página **Detalhes da** campanha ou do Canvas, o intervalo de datas inclui todos os usuários que receberam a campanha ou o Canvas durante essa janela e, entre esses usuários, os dados daqueles que realizaram o evento de retenção durante o intervalo de datas serão exibidos no relatório.
- **Unidades**: É possível ajustar as unidades entre a porcentagem de usuários e o número de usuários no canto superior direito do gráfico. Unidades específicas podem ser mais significativas ao avaliar o impacto de uma campanha ou Canvas.
- **Mapeamento de cores**: No seu relatório de retenção, as porcentagens ou o número de usuários mais altos recebem tons mais escuros de azul. As porcentagens ou o número de usuários mais baixos recebem tons mais claros de azul. Isso é feito para ajudar os usuários a visualizar esses dados.
- **Gráfico do relatório de retenção**: Esse gráfico resume os resultados de todas as coortes para o intervalo de datas selecionado.

### Desempenho por variante

A visualização do relatório de retenção por variante permite comparar a retenção contínua de cada variante ou variação de mensagem para o período de tempo selecionado, bem como o Grupo de Controle. Esse relatório pode ser visualizado alternando **Mostrar desempenho para** para **Por variante**.

Alguns casos de uso para mostrar o desempenho por variante:

- Tem algumas variantes ou experimentos em que os resultados parecem ser um esforço inútil ou não têm significância estatística? Dê outra olhada e veja se um ou outro teve um impacto de cauda mais longa.
- Veja como seria a retenção se você não tivesse enviado uma mensagem, analisando os dados de retenção do grupo de controle.

{% tabs %}
{% tab Campaign %}

Visualização por variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

Visualização por variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Relatório de retenção por componentes de variantes

- **Intervalo de datas**: Definido na página **Detalhes** da campanha ou do Canvas, o intervalo de datas inclui todos os usuários que receberam a campanha ou o Canvas durante essa janela e, entre esses usuários, os dados daqueles que realizaram o evento de retenção durante o intervalo de datas serão exibidos no relatório. A cada dia, a taxa de retenção, a alteração percentual em relação ao grupo de controle e a confiança são medidas.
- **Taxa de retenção**: Mostra a taxa de retenção por variante. A taxa de retenção é equivalente ao número de usuários que realizaram o evento de retenção dividido pelo total de usuários que receberam a campanha ou o Canvas.
- **Alteração percentual em relação ao controle**: Quantifica a alteração percentual por variante do grupo de controle.
- **Confiança**: {% multi_lang_include analytics/metrics.md metric='Confidence' %} A Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle com um procedimento estatístico chamado Teste Z para calcular uma porcentagem de [confiança]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence).
- **Unidades**: É possível ajustar as unidades entre a porcentagem de usuários e o número de usuários no canto superior direito do gráfico. Unidades específicas podem ser mais significativas ao avaliar o impacto de uma campanha ou Canvas.
- **Gráfico de variantes**: Esse gráfico resume os resultados por variante para o intervalo de datas selecionado.

## Coisas a serem observadas em seus relatórios de retenção

Os relatórios de retenção são fáceis de gerar, mas difíceis de interpretar e de agir. Para ajudar os profissionais de marketing, reunimos alguns tópicos e perguntas a serem considerados ao analisar seus Relatórios de retenção.

- Considere as tendências do dia da semana para campanhas recorrentes (por exemplo, as coortes de segunda-feira têm melhor desempenho do que as coortes de sábado?)
- Onde o impacto começa a diminuir? Isso pode ser um sinal de que uma nova campanha ou Canvas direcionado aos usuários naquele momento é necessário como outro impulso para a retenção. 
- Você está sentindo cansaço com as mensagens?
- Uma otimização específica que você fez em uma campanha ou Canvas há X dias teve um impacto positivo?



