---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o Canva
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artigo fornece respostas a perguntas frequentes sobre o Canva."
tool: Canvas

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o Canva.

### Quantas etapas posso incluir em um canva?

Você pode adicionar até 200 etapas em um canva.

### O que acontece se o público e o horário de envio forem idênticos para um canva que tem uma variante, mas várias ramificações?

Colocamos um trabalho na fila para cada etapa — eles são executados mais ou menos ao mesmo tempo, e um deles "vence". Na prática, isso pode ser distribuído de maneira um pouco uniforme, mas é provável que haja pelo menos uma ligeira tendência para a etapa que foi criada primeiro. 

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser uma divisão uniforme, adicione um filtro [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### Posso iniciar um canva com etapas desconectadas?

Sim. Você também pode salvar canvas após o lançamento com etapas desconectadas. 

### Para onde os usuários vão quando chegam a uma etapa desconectada?

Se um usuário estiver em uma etapa desconectada do seu fluxo de trabalho do canva, ele avançará para a etapa subsequente, se houver uma, e a configuração da etapa ditará como o usuário deve avançar. O objetivo é permitir que os usuários façam alterações nas etapas sem precisar conectá-las diretamente ao restante do canva. Isso também abre algum espaço para testes antes de entrar em operação imediatamente, permitindo efetivamente salvar um rascunho.

Recomendamos verificar a exibição de análise de dados para usuários pendentes em uma etapa do canva antes de desconectar uma etapa.

### O que acontece quando você para um canva?

Quando você interrompe um canva, aplica-se o seguinte:

- Os usuários serão impedidos de entrar no canva.
- Nenhuma outra mensagem será enviada, independentemente de onde um usuário esteja no fluxo.
- **Exceção:** Canvas com e-mails não serão interrompidos imediatamente. Depois que as solicitações de envio acessam o SendGrid, não há nada que possamos fazer para impedir que elas sejam entregues ao usuário.

### Devo construir um canva ou canvas separados por ciclo de vida do usuário?

Dependendo do que você está procurando realizar com seu canva, pode ser necessário adotar diferentes abordagens em como você constrói a jornada do usuário. A flexibilidade do canva permite que você mapeie jornadas de usuários para qualquer estágio do ciclo de vida do usuário. Confira nossos [modelos de canva da Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para vários exemplos de abordagens simplificadas para criar jornadas de usuário eficazes.

### Quando são enviadas as mensagens no app do canva?

Mensagens no app são enviadas no próximo início de sessão. Isso significa que, se o usuário entrar na etapa do canva antes de o canva ser interrompido, ele ainda receberá a mensagem no app no início da próxima sessão, desde que a mensagem no app ainda não tenha expirado.

É possível que um usuário inicie uma sessão antes que o canva seja interrompido, mas não veja a mensagem no app imediatamente. Isso pode ocorrer se a mensagem no app for acionada por um evento personalizado ou estiver com postergação. Isso significa que é possível para um usuário registrar uma impressão de mensagem no app e "receber" a mensagem no app após o canva ser interrompido. No entanto, o usuário teria que ter iniciado a sessão antes que o canva fosse interrompido, mas **depois** de ter recebido a etapa do canva.

{% alert note %}
A interrupção de um canva não fará com que os usuários que estão esperando para receber mensagens saiam da jornada do usuário. Se você reativar o canva e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).
{% endalert %}

### Quando um evento de exceção dispara?

Os eventos de exceção só são disparados enquanto o usuário está esperando para receber o componente do canva ao qual está associado. Se um usuário realizar uma ação com antecedência, o evento de exceção não disparará. Se quiser excluir usuários que tenham realizado um determinado evento com antecedência, use [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Como a edição de um canva afeta os usuários que já estão nele?

Se você editar algumas das etapas de um canva de várias etapas, os usuários que já estavam no público, mas não receberam as etapas, receberão a versão atualizada da mensagem. Observe que isso só acontecerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que pode ser editado após o lançamento, consulte [Alteração do Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

### Como são rastreadas as conversões de usuários em um canva?

Um usuário só pode converter uma vez por entrada no canva. As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de um canva reflete todas as conversões realizadas pelos usuários dentro daquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa era a etapa mais recente que o usuário recebeu.

{% alert note %}
Quando um usuário entra novamente em um canva, os eventos de conversão são rastreados apenas para a entrada mais recente. Os eventos de conversão não são registrados para entradas anteriores, mesmo que o evento de conversão seja preenchido retroativamente.
{% endalert %}

{% details Expandir para ver exemplos %}

**Exemplo 1**

Há uma jornada do canva com 10 notificações por push e o evento de conversão é "início da sessão" ("Abre o app"):

- O usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O usuário B abre o app após cada notificação por push.

**Resultado:** O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e zero para todas as etapas subsequentes.

{% alert note %}
Se o horário de silêncio estiver ativo quando o evento de conversão acontecer, as mesmas regras se aplicam.
{% endalert %}

**Exemplo 2**

Há um canva de uma etapa com o horário de silêncio ativado:

1. O usuário entra no canva.
2. A primeira etapa não tem uma postergação, mas está dentro do horário de silêncio definido, portanto, a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:** O usuário será contado como convertido na variante geral do canva, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

### Qual é a diferença entre os diferentes tipos de taxa de conversão?

- O total de conversões do canva reflete quantos usuários únicos completaram um evento de conversão, não quantas conversões cada um completou. 
- A taxa de conversão da variante ou o bloco de resumo no início de um canva reflete todas as conversões realizadas pelos usuários nessa jornada, independentemente de terem recebido ou não uma mensagem, como um total agregado. 
- A taxa de conversão da etapa reflete quantos indivíduos receberam essa etapa da mensagem e concluíram qualquer um dos eventos de conversão descritos.

### Qual é a diferença entre um componente e uma etapa?

Um [componente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) é uma parte individual do seu canva que pode ser usada para determinar a eficácia dele. Os componentes podem incluir ações como a divisão da jornada do usuário, a adição de uma postergação e até mesmo o teste de várias jornadas do canva. Uma etapa do canva refere-se à jornada personalizada do usuário em suas ramificações do canva. Essencialmente, seu canva é feito de componentes individuais que criam etapas para a jornada do usuário.

### Como posso visualizar a análise de dados de cada um dos meus componentes do canva?

Para visualizar a análise de dados de um componente do canva, acesse seu canva e role a página **Detalhes do Canvas** para baixo. Aqui, você pode visualizar a análise de dados de cada componente. Confira a [análise de dados do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obter mais detalhes.

### Ao analisar o número de usuários únicos, a análise de dados do canva ou o segmentador é mais preciso?

O segmentador é uma estatística mais precisa para dados de usuários únicos em comparação com as estatísticas de canva ou campanha. Isso ocorre porque as estatísticas de canva e campanha são números que a Braze incrementa quando algo acontece — o que significa que existem variáveis que podem resultar nesse número sendo diferente daquele do segmentador. Por exemplo, os usuários podem converter mais de uma vez para um canva ou campanha.

### Por que o número de usuários que entram em um canva não corresponde ao número esperado?

O número de usuários que entram em um canva pode ser diferente do número esperado devido à forma como o público e os disparadores são avaliados. Na Braze, um público é avaliado antes do disparador (a menos que esteja usando um disparador de [alteração de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Isso fará com que os usuários saiam do canva se não fizerem parte do seu público selecionado antes que qualquer ação-gatilho seja avaliada.

### O que acontece com os usuários anônimos durante sua jornada no canva?

Enquanto usuários anônimos podem entrar e sair de canvas, suas ações não estão associadas a um perfil de usuário específico até que sejam identificados, então suas interações podem não ser totalmente rastreadas em sua análise de dados. Você pode usar o [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para gerar um relatório dessas métricas.

### Por que minha taxa de conversão da etapa do canva não é igual à taxa de conversão total da variante do canva?

É comum que o total de conversão de uma variante do canva seja maior do que a soma do total de suas etapas. Isso ocorre porque um usuário pode realizar um evento de conversão para uma variante assim que entra na variante. Entretanto, esse mesmo evento de conversão não conta para uma etapa do canva. Portanto, qualquer usuário que entrar no canva e realizar o evento de conversão antes de receber a primeira etapa do canva será contabilizado no total de conversões da variante, e não no total de etapas. O mesmo se aplica a um usuário que entra no canva, mas sai dele antes de receber qualquer etapa.

### Como os públicos do canva são avaliados? 

Por padrão, os filtros e segmentos para etapas completas do canva são verificados no momento do envio. A etapa de divisão de decisão realiza uma avaliação logo após receber uma etapa anterior (ou antes de uma postergação).

{% alert tip %}
Para obter mais assistência com a solução de problemas dos canvas, entre em contato com o suporte da Braze em até 30 dias após a ocorrência do problema, pois só temos os registros de diagnóstico dos últimos 30 dias.
{% endalert %}

### Qual é a diferença entre "Has not entered Canvas variation" e "Is not in Canvas control group"?

Consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para obter definições completas de filtros.

#### Não entrou na variação do canva

O usuário nunca entrou em uma jornada de variação de um canva específico. Todos os usuários que não estão no grupo de controle são incluídos, independentemente de terem entrado no canva. Isso inclui usuários que entraram em outra variação e usuários que não entraram em nenhuma variação. 

#### Não está no grupo de controle do canva

O usuário entrou no canva, mas não está no grupo de controle e, consequentemente, recebeu uma variação. Isso inclui apenas os usuários que entraram no canva.

Note que a atribuição de variação ocorre na entrada do canva. Se um usuário não tiver entrado em um canva, não será atribuída nenhuma variante a ele. Em outras palavras, eles não estarão no grupo de controle ou em uma variante.

{% details Expandir para ver as perguntas frequentes do editor original do canva %}

### Como faço para converter um canva existente do editor original para o editor atual?

Você pode [clonar seu canva]({{site.baseurl}}/cloning_canvases/). Isso cria uma cópia do seu canva original no fluxo de trabalho mais atual do canva.

### Quais são as principais diferenças entre os editores atual e original do canva?

#### Barra de ferramentas do componente do canva

Anteriormente, com o editor original do canva, uma etapa completa era adicionada por padrão sempre que você criava qualquer etapa na jornada do usuário. Essas etapas completas são substituídas por diferentes componentes do canva, o que lhe dá o benefício de maior visibilidade e personalização para sua experiência de edição. Você pode ver imediatamente todos os componentes do canva na barra de ferramentas Etapa do canva.

#### Comportamento das etapas

Anteriormente, cada etapa completa incluía informações como configurações de postergação e programação, eventos de exceção, filtros de público, configuração de mensagens e opções de avanço de mensagens, tudo em um único componente. Essas são configurações separadas no editor atual para tornar a experiência de criação do canva mais personalizável e introduzem algumas diferenças na funcionalidade.

#### Avanço do componente de mensagem

Os [componentes de mensagens]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) adiantam todos os usuários que entram na etapa. Não há necessidade de especificar o comportamento de avanço de mensagens, o que simplifica a configuração da etapa geral. Se quiser implementar a opção **Advance when message sent**, adicione uma jornada do público separada para filtrar os usuários que não receberam a etapa anterior.  

#### Comportamento de postergação "in"

Os [componentes de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) aguardarão todo o tempo de postergação antes de prosseguir para a próxima etapa. 

Digamos que, em 12 de abril, tenhamos um componente de postergação em que a postergação é definida para enviar o usuário para a próxima etapa em um dia, às 14h. Um usuário entra no componente às 14h01 do dia 13 de abril. 
- No fluxo de trabalho original, o usuário passaria para a próxima etapa às 14h do dia 14 de abril, ou seja, menos de um dia após a hora de entrada. 
- No editor atual, o usuário passaria para a próxima etapa às 14h do dia 15 de abril. Note que esse é o mesmo horário, mas mais de um dia após o horário de entrada. 

#### Comportamento do Intelligent Timing

Como o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) é armazenado no componente de mensagem, as postergações serão aplicadas antes dos cálculos do Intelligent Timing. Isso significa que, dependendo de quando um usuário entra no componente, ele pode receber a mensagem mais tarde do que receberia em um canva criado com o fluxo de trabalho original do canva.

Digamos que sua postergação esteja definida para 2 dias, o Intelligent Timing esteja ativado e tenha determinado que o melhor horário para o envio de mensagens é às 14h. Um usuário entra na etapa de postergação às 14h01.
- **Fluxo de trabalho atual:** Serão necessárias 48 horas para que a postergação passe, de modo que o usuário receba a mensagem no terceiro dia, às 14h.
- **Fluxo de trabalho original:** O usuário recebe a mensagem no segundo dia, às 14h.

Note que, se o Intelligent Timing estiver ativado, a mensagem será enviada dentro de 24 horas após o usuário entrar no componente de mensagem no horário inteligente identificado (mesmo que nenhum componente de postergação esteja envolvido).

#### Eventos de exceção

##### Horário de silêncio

O evento de exceção é aplicado usando jornadas de ação, que são separadas das etapas de mensagens. O horário de silêncio é aplicado no componente de mensagem. Isso significa que, se um usuário já tiver passado pela jornada de ação (e não tiver sido excluído com o evento de exceção), encontrar o horário de silêncio quando chegar ao componente de mensagem e tiver o canva configurado de forma que a mensagem seja reenviada após o período de horário de silêncio, o evento de exceção não será mais aplicado. Note que esse caso de uso não é comum.

Para segmentos e filtros, a etapa de mensagem tem validações de entrega que permitem aos usuários configurar segmentos e filtros adicionais que são validados no momento do envio. Isso evita o caso extremo do horário de silêncio mencionado anteriormente.

##### Configuração de programação "In" ou "On the next"

Os eventos de exceção são criados usando jornadas de ação. As jornadas de ação suportam apenas "após uma janela de tempo X" e não "em X tempo" ou "na próxima vez X".

{% enddetails %}

### O que devo incluir ao enviar um ticket de suporte para um erro "Request Timed Out"?

Se você encontrar um erro "Request Timed Out" ao editar um canva e precisar entrar em contato com o [suporte da Braze]({{site.baseurl}}/braze_support/), inclua as seguintes informações para ajudar a agilizar a resolução:

- **Gravação de tela:** Uma gravação das etapas que você realizou antes de ver o erro, incluindo quaisquer transições de página.
- **Timestamp e fuso horário:** O horário exato em que o erro ocorreu e seu fuso horário.
- **Navegador e versão:** O navegador que você está usando (por exemplo, Chrome 120, Safari 17) e se você tentou reproduzir o erro em um navegador diferente.
- **Etapas para reproduzir:** Uma descrição clara das ações que disparam o erro, incluindo quaisquer etapas ou configurações específicas do canva envolvidas.
- **Logs de rede (opcional):** Abra as ferramentas de desenvolvedor do seu navegador (guia **Network**), reproduza o erro e exporte o log de rede como um arquivo de log HTTP Archive (HAR). Isso ajuda a equipe de suporte a identificar qual chamada de API está causando o timeout.