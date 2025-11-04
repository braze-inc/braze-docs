---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre o Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artigo fornece respostas a perguntas frequentes sobre o Canvas."
tool: Canvas

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o Canvas.

### Quantas etapas posso incluir em um Canvas?

Você pode adicionar até 200 etapas em um Canvas.

### O que acontece se o público e o tempo de envio forem idênticos para um Canvas que tem uma variante, mas várias ramificações?

Colocamos um trabalho na fila para cada etapa - eles são executados mais ou menos ao mesmo tempo, e um deles "vence". Na prática, isso pode ser classificado de maneira um pouco uniforme, mas é provável que haja pelo menos uma leve tendência para a etapa que foi criada primeiro. 

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser uma divisão uniforme, adicione um filtro [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### Posso iniciar um Canvas com etapas desconectadas?

Sim. Você também pode salvar Canvases após o lançamento com etapas desconectadas. 

### Para onde os usuários vão quando chegam a uma etapa desconectada?

Se um usuário estiver em uma etapa desconectada do seu fluxo de trabalho do Canvas, ele avançará para a etapa subsequente, se houver uma, e a configuração da etapa determinará como o usuário deve avançar. O objetivo é permitir que os usuários façam alterações nas etapas sem precisar conectá-las diretamente ao restante do Canvas. Isso também lhe dá algum espaço para testes antes de entrar em operação imediatamente, permitindo efetivamente salvar um rascunho.

Recomendamos verificar a exibição de análise dos usuários pendentes em uma etapa do Canvas antes de desconectar uma etapa.

### O que acontece quando você interrompe um Canvas?

Quando você interrompe um Canvas, aplica-se o seguinte:

- Os usuários serão impedidos de entrar no Canvas.
- Nenhuma outra mensagem será enviada, independentemente de onde o usuário esteja no fluxo.
- **Exceção:** As telas com e-mails não serão interrompidas imediatamente. Depois que as solicitações de envio vão para o SendGrid, não há nada que possamos fazer para impedir que elas sejam entregues ao usuário.

### Devo criar um Canvas ou Canvases separados por ciclo de vida do usuário?

Dependendo do que você deseja realizar com o Canvas, talvez sejam necessárias abordagens diferentes para criar a jornada do usuário. A flexibilidade do Canvas permite mapear as jornadas do usuário para qualquer estágio do ciclo de vida do usuário. Confira nossos [modelos do Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para ver vários exemplos de abordagens simplificadas para a criação de jornadas de usuário eficazes.

### Quando são enviadas as mensagens in-app no Canvas?

As mensagens no aplicativo são enviadas no início da próxima sessão. Isso significa que se o usuário entrar na etapa do Canvas antes de o Canvas ser interrompido, ele ainda receberá a mensagem in-app no início da próxima sessão, desde que a mensagem in-app ainda não tenha expirado.

É possível que um usuário inicie uma sessão antes que o Canvas seja interrompido, mas que a mensagem no aplicativo não seja exibida imediatamente. Isso pode ocorrer se a mensagem in-app for acionada por um evento personalizado ou estiver atrasada. Isso significa que é possível que um usuário registre uma impressão de mensagem in-app e "receba" a mensagem in-app depois que o Canvas for interrompido. No entanto, o usuário teria que iniciar a sessão antes que o Canvas fosse interrompido, mas **depois de** receber a etapa do Canvas.

{% alert note %}
A interrupção de um Canvas não fará com que os usuários que estão esperando para receber mensagens saiam da jornada do usuário. Se você reativar o Canvas e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).
{% endalert %}

### Quando um evento de exceção é acionado?

Os eventos de exceção só são acionados enquanto o usuário está esperando para receber o componente do Canvas ao qual está associado. Se um usuário executar uma ação antecipadamente, o evento de exceção não será acionado. Se quiser excluir usuários que realizaram um determinado evento com antecedência, use [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Como a edição de um Canvas afeta os usuários que já estão no Canvas?

Se você editar algumas das etapas de um Canvas de várias etapas, os usuários que já estavam no público, mas não receberam as etapas, receberão a versão atualizada da mensagem. Observe que isso só ocorrerá se eles ainda não tiverem sido avaliados para a etapa.

Para obter mais informações sobre o que você pode editar após o lançamento, consulte [Alteração do Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

### Como as conversões de usuários são rastreadas em um Canvas?

Um usuário só pode converter uma vez por entrada no Canvas. As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários dentro desse caminho, independentemente de terem ou não recebido uma mensagem. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa foi a etapa mais recente que o usuário recebeu.

{% details Expand for examples %}

**Exemplo 1**

Há um caminho do Canvas com 10 notificações por push e o evento de conversão é "início da sessão" ("Abre o aplicativo"):

- O usuário A abre o aplicativo depois de entrar, mas antes de receber a primeira mensagem.
- O usuário B abre o aplicativo após cada notificação push.

**Resultado:** O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão de um na primeira etapa e zero em todas as etapas subsequentes.

{% alert note %}
Se o Quiet Hours estiver ativo quando o evento de conversão ocorrer, as mesmas regras se aplicam.
{% endalert %}

**Exemplo 2**

Há um Canvas de uma etapa com o Quiet Hours ativado:

1. O usuário entra no Canvas.
2. A primeira etapa não tem um atraso, mas está dentro das Quiet Hours definidas, portanto, a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:** O usuário será contado como convertido na variante geral do Canvas, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

### Qual é a diferença entre os diferentes tipos de taxa de conversão?

- O total de conversões do Canvas reflete quantos usuários únicos concluíram um evento de conversão, não quantas conversões cada um deles concluiu. 
- A taxa de conversão da variante ou o bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários nesse caminho, independentemente de terem recebido ou não uma mensagem, como um total agregado. 
- A taxa de conversão de etapas reflete quantos indivíduos receberam essa etapa da mensagem e concluíram qualquer um dos eventos de conversão descritos.

### Qual é a diferença entre um componente e uma etapa?

Um [componente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) é uma parte individual do seu Canvas que você pode usar para determinar a eficácia do seu Canvas. Os componentes podem incluir ações como a divisão da jornada do usuário, a adição de um atraso e até mesmo o teste de vários caminhos do Canvas. Uma etapa no Canvas refere-se à jornada personalizada do usuário em suas ramificações do Canvas. Essencialmente, o Canvas é feito de componentes individuais que criam etapas para a jornada do usuário.

### Como posso visualizar as análises de cada um dos meus componentes do Canvas?

Para visualizar as análises de um componente do Canvas, acesse seu Canvas e role a página **Detalhes do Canvas** para baixo. Aqui, você pode visualizar as análises de cada componente. Confira a [análise do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obter mais detalhes.

### Ao analisar o número de usuários únicos, o Canvas Analytics ou o segmentador é mais preciso?

O segmentador é uma estatística mais precisa para dados de usuários exclusivos em comparação com as estatísticas do Canvas ou da campanha. Isso ocorre porque as estatísticas do Canvas e da campanha são números que o Braze incrementa quando algo acontece, o que significa que há variáveis que podem fazer com que esse número seja diferente do número do segmentador. Por exemplo, os usuários podem converter mais de uma vez para um Canvas ou campanha.

### Por que o número de usuários que entram em um Canvas não corresponde ao número esperado?

O número de usuários que entram em um Canvas pode ser diferente do número esperado devido à forma como os públicos e os acionadores são avaliados. No Braze, um público é avaliado antes do acionador (a menos que seja usado um acionador de [alteração de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Isso fará com que os usuários saiam do Canvas se não fizerem parte do público selecionado antes que qualquer ação de acionamento seja avaliada.

### O que acontece com os usuários anônimos durante sua jornada no Canvas?

Embora os usuários anônimos possam entrar e sair do Canvases, suas ações não são associadas a um perfil de usuário específico até que sejam identificados, portanto, suas interações podem não ser totalmente rastreadas em suas análises. Você pode usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) para gerar um relatório dessas métricas.

### Por que minha taxa de conversão de etapas do Canvas não é igual à taxa de conversão total da variante do Canvas?

É comum que o total de conversão de uma variante do Canvas seja maior do que a soma de seu total de etapas. Isso ocorre porque um usuário pode executar um evento de conversão para uma variante assim que entra na variante. No entanto, esse mesmo evento de conversão não conta para uma etapa do Canvas. Portanto, qualquer usuário que entrar no Canvas e realizar o evento de conversão antes de receber a primeira etapa do Canvas será contabilizado no total de conversões de variantes, e não no total de etapas. O mesmo se aplica a um usuário que entra no Canvas, mas sai dele antes de receber qualquer etapa.

### Como os públicos do Canvas são avaliados? 

Por padrão, os filtros e segmentos para etapas completas no Canvas são verificados no momento do envio. A etapa Decision Split executa uma avaliação logo após receber uma etapa anterior (ou antes de um atraso).

{% alert tip %}
Para obter mais assistência com a solução de problemas do Canvas, entre em contato com o Suporte Braze dentro de 30 dias após a ocorrência do problema, pois só temos os registros de diagnóstico dos últimos 30 dias.
{% endalert %}

### Qual é a diferença entre "Has not entered Canvas variation" e "Is not in Canvas control group"?

Consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para obter definições completas de filtros.

#### Não entrou na variação do Canvas

O usuário nunca inseriu um caminho de variação de um Canvas específico. Todos os usuários que não estão no grupo de controle são incluídos, independentemente de terem entrado no Canvas. Isso inclui usuários que inseriram outra variação e usuários que não inseriram nenhuma variação. 

#### Não está no grupo de controle do Canvas

O usuário entrou no Canvas, mas não está no grupo de controle e, consequentemente, recebeu uma variação. Isso inclui apenas os usuários que entraram no Canvas.

Observe que a atribuição de variação ocorre na entrada do Canvas. Se um usuário não tiver inserido um Canvas, não lhe será atribuída nenhuma variante. Em outras palavras, eles não estarão no grupo de controle ou em uma variante.

{% details Expand for original Canvas editor FAQs %}

### Como faço para converter um Canvas existente do editor original para o editor atual?

Você pode [clonar seu Canvas]({{site.baseurl}}/cloning_canvases/). Isso cria uma cópia de seu Canvas original no fluxo de trabalho mais atual do Canvas.

### Quais são as principais diferenças entre os editores atuais e originais do Canvas?

#### Barra de ferramentas do componente Canvas

Anteriormente, com o editor original do Canvas, uma etapa completa era adicionada por padrão sempre que você criava qualquer etapa na jornada do usuário. Essas etapas completas são substituídas por diferentes componentes do Canvas, o que lhe dá o benefício de maior visibilidade e personalização para sua experiência de edição. Você pode ver imediatamente todos os seus componentes do Canvas na barra de ferramentas da etapa do Canvas.

#### Comportamento de etapas

Anteriormente, cada etapa completa incluía informações como configurações de atraso e programação, eventos de exceção, filtros de público, configuração de mensagens e opções de avanço de mensagens, tudo em um único componente. Essas são configurações separadas no editor atual para tornar a experiência de criação do Canvas mais personalizável e introduzem algumas diferenças na funcionalidade.

#### Avanço do componente de mensagem

[Os componentes da mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) adiantam todos os usuários que entram na etapa. Não há necessidade de especificar o comportamento de avanço da mensagem, o que simplifica a configuração da etapa geral. Se quiser implementar a opção **Advance when message sent**, adicione um Audience Paths separado para filtrar os usuários que não receberam a etapa anterior.  

#### Atraso no comportamento de "entrada

[Os componentes de atraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) aguardarão todo o tempo de atraso antes de prosseguir para a próxima etapa. 

Digamos que, em 12 de abril, tenhamos um componente Delay em que o atraso é definido para enviar o usuário para a próxima etapa em um dia, às 14h. Um usuário entra no componente às 14h01 do dia 13 de abril. 
- No fluxo de trabalho original, o usuário passaria para a próxima etapa às 14 horas do dia 14 de abril, ou seja, menos de um dia após o horário de entrada. 
- No editor atual, o usuário passaria para a próxima etapa às 14 horas do dia 15 de abril. Observe que esse é o mesmo horário, mas mais de um dia após o horário de entrada. 

#### Comportamento de tempo inteligente

Como [o Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) é armazenado no componente Message, os atrasos serão aplicados antes dos cálculos do Intelligent Timing. Isso significa que, dependendo de quando um usuário entra no componente, ele pode receber a mensagem mais tarde do que receberia em um Canvas criado com o fluxo de trabalho original do Canvas.

Digamos que seu atraso esteja definido para 2 dias, que o Intelligent Timing esteja ativado e que ele tenha determinado que o melhor horário para enviar sua mensagem é às 14 horas. Um usuário entra na etapa de atraso às 2:01 pm.
- **Fluxo de trabalho atual:** Serão necessárias 48 horas para que o atraso passe, de modo que o usuário receba a mensagem no terceiro dia, às 14 horas.
- **Fluxo de trabalho original:** O usuário recebe a mensagem no segundo dia, às 14 horas.

Observe que, se o Intelligent Timing estiver ativado, a mensagem será enviada dentro de 24 horas após o usuário inserir o componente Message no horário inteligente identificado (mesmo que nenhum componente Delay esteja envolvido).

#### Eventos de exceção

##### Horário de silêncio

O evento de exceção é aplicado usando caminhos de ação, que são separados das etapas de mensagem. As horas de silêncio são aplicadas no componente Mensagem. Isso significa que, se um usuário já tiver passado pelo Caminho de ação (e não tiver sido excluído com o evento de exceção), ele encontrará o Quiet Hours quando chegar ao componente Message e tiver seu Canvas configurado de forma que a mensagem seja reenviada após o período de Quiet Hours, o evento de exceção não será mais aplicado. Observe que esse caso de uso não é comum.

Para segmentos e filtros, a etapa Mensagem tem validações de entrega que permitem aos usuários configurar segmentos e filtros adicionais que são validados no momento do envio. Isso evita o caso extremo do Quiet Hours mencionado anteriormente.

##### Configuração de programação "In" ou "On the next"

Os eventos de exceção são criados usando caminhos de ação. Os Caminhos de Ação somente suportam "após uma janela de tempo X" e não "em X tempo" ou "no próximo X tempo".

{% enddetails %}