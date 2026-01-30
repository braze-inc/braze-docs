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

### Quantas etapas posso incluir em um Canva?

Você pode adicionar até 200 etapas em um Canva.

### O que acontece se o público e o horário de envio forem idênticos para um canva que tem uma variante, mas várias ramificações?

Colocamos um trabalho na fila para cada etapa - eles são executados mais ou menos ao mesmo tempo, e um deles "vence". Na prática, isso pode ser classificado de maneira um pouco uniforme, mas é provável que haja pelo menos uma ligeira tendência para a etapa que foi criada primeiro. 

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser uma divisão uniforme, adicione um filtro [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### Posso iniciar um Canva com etapas desconectadas?

Sim. Você também pode salvar Canvas após o lançamento com etapas desconectadas. 

### Para onde os usuários acessam quando chegam a uma etapa desconectada?

Se um usuário estiver em uma etapa desconectada do seu fluxo de trabalho do Canva, ele avançará para a etapa subsequente, se houver uma, e a configuração da etapa ditará como o usuário deve avançar. O objetivo é permitir que os usuários façam alterações nas etapas sem precisar conectá-las diretamente ao restante do Canva. Isso também abre algum espaço para testes antes de entrar em operação imediatamente, permitindo efetivamente salvar um rascunho.

Recomendamos verificar a exibição de análise de dados para usuários pendentes em uma etapa do Canva antes de desconectar uma etapa.

### O que acontece quando você para uma canva?

Quando você interrompe um Canva, aplica-se o seguinte:

- Os usuários serão impedidos de entrar na canva.
- Nenhuma outra mensagem será enviada, independentemente de onde um usuário esteja no fluxo.
- **Exceção:** As telas com e-mails não serão interrompidas imediatamente. Depois que as solicitações de envio acessam o SendGrid, não há nada que possamos fazer para impedir que elas sejam entregues ao usuário.

### Devo construir um canva ou canvas separados por ciclo de vida do usuário?

Dependendo do que você está procurando realizar com seu canva, pode ser necessário adotar diferentes abordagens em como você constrói a jornada do usuário. A flexibilidade do canva permite que você mapeie jornadas de usuários para qualquer estágio do ciclo de vida do usuário. Confira nossos [modelos de canva Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para vários exemplos de abordagens simplificadas para criar jornadas de usuário eficazes.

### Quando são enviadas as mensagens no app do Canva?

Mensagens no app são enviadas na próxima sessão. Isso significa que, se o usuário entrar na etapa do Canva antes de o Canvas ser interrompido, ele ainda receberá a mensagem no app no início da próxima sessão, desde que a mensagem no app ainda não tenha expirado.

É possível que um usuário inicie uma sessão antes que o canva seja interrompido, mas não seja exibida a mensagem no app imediatamente. Isso pode ocorrer se a mensagem no app for acionada por um evento personalizado ou se estiver atrasada. Isso significa que é possível para um usuário registrar uma impressão de mensagem no app e "receber" a mensagem no app após o canva ser interrompido. No entanto, o usuário teria que ter iniciado a sessão antes que o canva fosse interrompido, mas **depois** que eles receberam a etapa do canva.

{% alert note %}
A interrupção de um Canva não fará com que os usuários que estão esperando para receber mensagens saiam da jornada do usuário. Se você reativar o Canva e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).
{% endalert %}

### Quando um evento de exceção dispara?

Os eventos de gatilho só são disparados enquanto o usuário está esperando para receber o componente do Canva ao qual está associado. Se um usuário realizar uma ação com antecedência, o evento de exceção não disparará. Se quiser excluir usuários que tenham realizado um determinado evento com antecedência, use [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Como a edição de um Canvas afeta os usuários que já estão no Canvas?

Se você editar algumas das etapas de um Canvas de várias etapas, os usuários que já estavam no público, mas não receberam as etapas, receberão a versão atualizada da mensagem. Observe que isso só acontecerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que pode ser editado após o lançamento, consulte [Alteração do Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

### Como são rastreadas as conversões de usuários em uma canva?

Um usuário só pode converter uma vez por entrada no Canva. As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de uma canva reflete todas as conversões realizadas pelos usuários dentro daquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa era a etapa mais recente que o usuário recebeu.

{% alert note %}
Quando um usuário entra novamente em um Canva, os eventos de conversão são rastreados apenas para a entrada mais recente. Os eventos de conversão não são registrados para entradas anteriores, mesmo que o evento de conversão seja preenchido novamente.
{% endalert %}

{% details Expand for examples %}

**Exemplo 1**

Há uma jornada do Canvas com 10 notificações por push e o evento de conversão é "início da sessão" ("Abre o app"):

- O usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O usuário B abre o app após cada notificação por push.

**Resultado:** O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão de uma na primeira etapa e zero para todas as etapas subsequentes.

{% alert note %}
Se o horário de silêncio estiver ativo quando o evento de conversão acontecer, as mesmas regras se aplicam.
{% endalert %}

**Exemplo 2**

Há uma etapa do Canva com o Horário de silêncio ativado:

1. O usuário entra no Canva.
2. A primeira etapa não tem uma postergação, mas está dentro do horário de silêncio definido, portanto, a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:** O usuário será contado como convertido na variante geral da canva, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

### Qual é a diferença entre os diferentes tipos de taxa de conversão?

- Total canva conversões refletem quantos usuários únicos completaram um evento de conversão, não quantas conversões cada um completou. 
- A taxa de conversão da variante ou o bloco de resumo no início de uma Canva reflete todas as conversões realizadas pelos usuários nessa jornada, independentemente de terem recebido ou não uma mensagem, como um total agregado. 
- A taxa de conversão da etapa reflete quantos indivíduos receberam essa etapa da mensagem e concluíram qualquer um dos eventos de conversão descritos.

### Qual é a diferença entre um componente e uma etapa?

Um [componente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) é uma parte individual do Canvas que pode ser usada para determinar a eficácia do Canva. Os componentes podem incluir ações como a divisão da jornada do usuário, a adição de uma postergação e até mesmo o teste de várias jornadas do Canva. Uma etapa do canva refere-se à jornada personalizada do usuário em suas filiais dos canvas. Essencialmente, seu Canva é feito de componentes individuais que criam etapas para a jornada do usuário.

### Como posso visualizar a análise de dados de cada um dos meus componentes do Canva?

Para visualizar a análise de dados de um componente do Canvas, acesse seu Canvas e role a página **Detalhes do Canvas** para baixo. Aqui, você pode visualizar a análise de dados de cada componente. Confira a [análise de dados do Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obter mais detalhes.

### Ao analisar o número de usuários únicos, a análise de dados do Canva ou o segmentador é mais preciso?

O segmentador é uma estatística mais precisa para dados de usuários únicos em comparação com canva ou estatísticas de campanha. Isso ocorre porque canva e as estatísticas de campanha são números que Braze incrementa quando algo acontece—o que significa que existem variáveis que podem resultar nesse número sendo diferente daquele do segmentador. Por exemplo, os usuários podem converter mais de uma vez para uma canva ou campanha.

### Por que o número de usuários que entram em um Canva não corresponde ao número esperado?

O número de usuários que entram em um Canva pode ser diferente do número esperado devido à forma como o público e os disparadores são avaliados. Na Braze, um público é avaliado antes do disparador (a menos que esteja usando um disparador de [alteração de atribuição]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Isso fará com que os usuários saiam da canva se não fizerem parte do seu público selecionado antes que qualquer ação de disparar seja avaliada.

### O que acontece com os usuários anônimos durante sua jornada no canva?

Enquanto usuários anônimos podem entrar e sair de Canvases, suas ações não estão associadas a um perfil de usuário específico até que sejam identificados, então suas interações podem não ser totalmente rastreadas em sua análise de dados. Você pode usar o [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para gerar um relatório dessas métricas.

### Por que minha taxa de conversão da etapa do Canva não é igual à taxa de conversão total da variante do Canvas?

É comum que o total de conversão de uma variante do Canva seja maior do que a soma do total de suas etapas. Isso ocorre porque um usuário pode realizar um evento de conversão para uma variante assim que entra na variante. Entretanto, esse mesmo evento de conversão não conta para uma etapa do canva. Portanto, qualquer usuário que entrar no Canvas e realizar o evento de conversão antes de receber a primeira etapa do Canva será contabilizado no total de conversões de variantes, e não no total de etapas. O mesmo se aplica a um usuário que entra no Canvas, mas sai dele antes de receber qualquer etapa do canva.

### Como os públicos do Canva são avaliados? 

Por padrão, os filtros e segmentos para etapas completas do Canva são verificados no momento do envio. A etapa de divisão de decisão realiza uma avaliação logo após receber uma etapa anterior (ou antes de uma postergação).

{% alert tip %}
Para obter mais assistência com a solução de problemas dos canvas, entre em contato com o suporte da Braze em até 30 dias após a ocorrência do problema, pois só temos os registros de diagnóstico dos últimos 30 dias.
{% endalert %}

### Qual é a diferença entre "Has not entered Canvas variation" e "Is not in Canvas control group"?

Consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para obter definições completas de filtros.

#### Não entrou na variação do Canva

O usuário nunca inseriu uma jornada de variação de um Canva específico. Todos os usuários que não estão no grupo de controle são incluídos, independentemente de terem entrado no Canva. Isso inclui usuários que inseriram outra variação e usuários que não inseriram nenhuma variação. 

#### Não está no grupo de controle do Canva

O usuário entrou no Canva, mas não está no grupo de controle e, consequentemente, recebeu uma variação. Isso inclui apenas os usuários que entraram no Canva.

Note que a atribuição de variação ocorre na entrada do Canva. Se um usuário não tiver inserido uma tela, não será atribuída nenhuma variante a ele. Em outras palavras, eles não estarão no grupo de controle ou em uma variante.

{% details Expand for original Canvas editor FAQs %}

### Como faço para converter uma tela existente do editor original para o editor atual?

Você pode [clonar seu Canva]({{site.baseurl}}/cloning_canvases/). Isso cria uma cópia de seu Canvas original no fluxo de trabalho mais atual do Canvas.

### Quais são as principais diferenças entre os editores atuais e originais do Canva?

#### Barra de ferramentas do componente canva

Anteriormente, com o editor do Canva original, uma etapa completa era adicionada por padrão sempre que você criava qualquer etapa na jornada do usuário. Essas etapas completas são substituídas por diferentes componentes do Canvas, o que lhe dá o benefício de maior visibilidade e personalização para sua experiência de edição. Você pode ver imediatamente todos os componentes do canva na barra de ferramentas Etapa do canva.

#### Comportamento das etapas

Anteriormente, cada etapa completa incluía informações como configurações de postergação e programação, eventos de exceção, filtros de público, configuração de mensagens e opções de avanço de mensagens, tudo em um único componente. Essas são configurações separadas no editor atual para tornar a experiência de criação do Canvas mais personalizável e introduzem algumas diferenças na funcionalidade.

#### Envio de mensagens

Os [componentes de mensagens]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) adiantam todos os usuários que entram na etapa. Não há necessidade de especificar o comportamento de avanço de mensagens, o que simplifica a configuração da etapa geral. Se quiser implementar a opção **Advance when message sent**, adicione uma jornada do público separada para filtrar os usuários que não receberam a etapa anterior.  

#### Comportamento de postergação

Os [componentes de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) aguardarão todo o tempo de postergação antes de prosseguir para a próxima etapa. 

Digamos que, em 12 de abril, tenhamos um componente Delay em que a postergação é definida para enviar o usuário para a próxima etapa em um dia, às 14h. Um usuário entra no componente às 14h01 do dia 13 de abril. 
- No fluxo de trabalho original, o usuário passaria para a próxima etapa às 14 horas do dia 14 de abril, ou seja, menos de um dia após a hora de entrada. 
- No editor atual, o usuário passaria para a próxima etapa às 14 horas do dia 15 de abril. Note que esse é o mesmo horário, mas mais de um dia após o horário de entrada. 

#### Comportamento Intelligent Timing

Como o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) é armazenado no componente Mensagem, as postergações serão aplicadas antes dos cálculos do Intelligent Timing. Isso significa que, dependendo de quando um usuário entra no componente, ele pode receber a mensagem mais tarde do que receberia em um Canvas criado com o fluxo de trabalho original do Canvas.

Digamos que sua postergação esteja definida para 2 dias, o Intelligent Timing esteja ativado e tenha determinado que o melhor horário para o envio de mensagens é às 14 horas. Um usuário entra na etapa de postergação às 2:01 pm.
- **Fluxo de trabalho atual:** Serão necessárias 48 horas para que a postergação passe, de modo que o usuário receba a mensagem no terceiro dia, às 14 horas.
- **Fluxo de trabalho original:** O usuário recebe a mensagem no segundo dia, às 14 horas.

Note que, se o Intelligent Timing estiver ativado, a mensagem será enviada dentro de 24 horas após o usuário inserir o componente Message no horário inteligente identificado (mesmo que nenhum componente de postergação esteja envolvido).

#### Eventos de exceção

##### Horário de silêncio

O evento de exceção é aplicado usando jornadas de ação, que são separadas das etapas de mensagens. O Horário de silêncio é aplicado no componente Mensagem. Isso significa que, se um usuário já tiver passado pela Jornada de ação (e não tiver sido excluído com o evento de exceção), encontrar o Horário de silêncio quando chegar ao componente Mensagem e tiver o Canva configurado de forma que a mensagem seja reenviada após o período de Horário de silêncio, o evento de exceção não será mais aplicado. Note que esse caso de uso não é comum.

Para segmentos e filtros, a etapa de mensagem tem validações de entrega que permitem aos usuários configurar segmentos e filtros adicionais que são validados no momento do envio. Isso evita o caso extremo do Horário de silêncio mencionado anteriormente.

##### Configuração de programação "In" ou "On the next"

Os eventos de exceção são criados usando jornadas de ação. As jornadas de ação suportam apenas "após uma janela de tempo X" e não "em X tempo" ou "na próxima vez X".

{% enddetails %}