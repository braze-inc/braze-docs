---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o Canva
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artigo fornece respostas a perguntas frequentes sobre o Canvas e o Canvas Flow."
tool: Canvas

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o Canvas e o [Canvas Flow](#canvas-flow).

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow. É uma experiência de edição aprimorada para melhor construir e gerenciar canvas. Saiba mais sobre a [clonagem de canvas no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

## Geral

### O que acontece se o público e o horário de envio forem idênticos para um Canva que tenha uma variante, mas várias ramificações?

Colocamos um trabalho na fila para cada etapa - eles são executados mais ou menos ao mesmo tempo, e um deles "vence". Na prática, isso pode ser classificado de maneira um pouco uniforme, mas é provável que haja pelo menos uma ligeira tendência para a etapa que foi criada primeiro. 

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser uma divisão uniforme, adicione um filtro [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### O que acontece quando você interrompe um Canva?

Quando você interrompe um Canva, aplica-se o seguinte:

- Os usuários serão impedidos de entrar na canva.
- Nenhuma outra mensagem será enviada, independentemente de onde um usuário esteja no fluxo.
- **Exceção:** As telas com e-mails não serão interrompidas imediatamente. Depois que as solicitações de envio acessam o SendGrid, não há nada que possamos fazer para impedir que elas sejam entregues ao usuário.

### Devo construir um canva ou canvas separados por ciclo de vida do usuário?

Dependendo do que você está procurando realizar com seu canva, pode ser necessário adotar diferentes abordagens em como você constrói a jornada do usuário. A flexibilidade do canva permite que você mapeie jornadas de usuários para qualquer estágio do ciclo de vida do usuário. Confira nossos [modelos de canva Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para vários exemplos de abordagens simplificadas para criar jornadas de usuário eficazes.

#### Mensagens no app no Canva

Mensagens no app são enviadas na próxima sessão. Isso significa que, se o usuário entrar na etapa do Canva antes de o Canvas ser interrompido, ele ainda receberá a mensagem no app no início da próxima sessão, desde que a mensagem no app ainda não tenha expirado.

É possível que um usuário inicie uma sessão antes que o canva seja interrompido, mas não seja exibida a mensagem no app imediatamente. Isso pode ocorrer se a mensagem no app for acionada por um evento personalizado ou se estiver atrasada. Isso significa que é possível para um usuário registrar uma impressão de mensagem no app e "receber" a mensagem no app após o canva ser interrompido. No entanto, o usuário teria que ter iniciado a sessão antes que o canva fosse interrompido, mas **depois** que eles receberam a etapa do canva.

{% alert note %}
A interrupção de um Canva não fará com que os usuários que estão esperando para receber mensagens saiam da jornada do usuário. Se você reativar o Canva e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).
{% endalert %}

### Quando um evento de exceção é disparado?

Eventos de exceção só disparam enquanto o usuário está esperando para receber o componente canva com o qual está associado. Se um usuário executar uma ação antecipadamente, o evento de exceção não será disparado. Se quiser excluir usuários que tenham realizado um determinado evento com antecedência, use [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Como a edição de um Canvas afeta os usuários que já estão no Canvas?

Se você editar algumas das etapas de um Canvas de várias etapas, os usuários que já estavam no público, mas não receberam as etapas, receberão a versão atualizada da mensagem. Note que isso só ocorrerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que pode ser editado após o lançamento, consulte [Alterar seu canva após o lançamento]({{site.baseurl}}/post-launch_edits/).

### Como as conversões de usuários são rastreadas em um Canva?

Um usuário só pode converter uma vez por entrada no Canva. As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de uma canva reflete todas as conversões realizadas pelos usuários dentro daquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa foi a etapa mais recente que o usuário recebeu.

{% details Exemplos %}

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

O segmentador é uma estatística mais precisa para dados de usuários exclusivos em comparação com as estatísticas do Canva ou da campanha. Isso ocorre porque canva e as estatísticas de campanha são números que Braze incrementa quando algo acontece—o que significa que existem variáveis que podem resultar nesse número sendo diferente daquele do segmentador. Por exemplo, os usuários podem converter mais de uma vez em um Canva ou em uma campanha.

### Por que o número de usuários que entram em um Canva não corresponde ao número esperado?

O número de usuários que entram em um Canva pode ser diferente do número esperado devido à forma como o público e os disparadores são avaliados. Na Braze, um público é avaliado antes do disparador (a menos que esteja usando um disparador de [alteração de atribuição]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Isso fará com que os usuários saiam do Canva se não fizerem parte do público selecionado antes que qualquer ação-gatilho seja avaliada.

### O que acontece com os usuários anônimos durante sua jornada no canva?

Enquanto usuários anônimos podem entrar e sair de Canvases, suas ações não estão associadas a um perfil de usuário específico até que sejam identificados, então suas interações podem não ser totalmente rastreadas em sua análise de dados. Você pode usar o [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para gerar um relatório dessas métricas.

### Por que minha taxa de conversão da etapa do Canva não é igual à taxa de conversão total da variante do Canvas?

É comum que o total de conversão de uma variante do Canva seja maior do que a soma do total de suas etapas. Isso ocorre porque um usuário pode realizar um evento de conversão para uma variante assim que entra na variante. Entretanto, esse mesmo evento de conversão não conta para uma etapa do canva. Portanto, qualquer usuário que entrar no Canvas e realizar o evento de conversão antes de receber a primeira etapa do Canva será contabilizado no total de conversões de variantes, e não no total de etapas. O mesmo se aplica a um usuário que entra no Canvas, mas sai dele antes de receber qualquer etapa do canva.

### Como os públicos do Canva são avaliados? 

Por padrão, os filtros e segmentos para etapas completas do Canva são verificados no momento do envio. Para o Canvas Flow, o componente Divisão de decisão realiza uma avaliação logo após receber uma etapa anterior (ou antes de uma postergação).

{% alert tip %}
Para obter mais assistência com a solução de problemas dos canvas, entre em contato com o suporte da Braze em até 30 dias após a ocorrência do problema, pois só temos os registros de diagnóstico dos últimos 30 dias.
{% endalert %}

## Canvas Flow

### O que é o Canvas Flow?

O Canvas Flow é a experiência de edição aprimorada que simplifica a forma como os profissionais de marketing podem criar e gerenciar suas jornadas de usuário do Canvas. Você pode esperar visualizar e usar facilmente os componentes do Canvas no construtor do Canvas. Você também tem acesso a mais recursos de edição pós-lançamento para editar conexões entre etapas, excluir etapas e variantes e redirecionar usuários para etapas diferentes.

### Como faço para converter um Canvas existente em Canvas Flow?

Você pode [clonar seu Canvas para o Canvas Flow]({{site.baseurl}}/cloning_canvases/). Isso cria uma cópia de seu Canvas original no fluxo de trabalho do Canvas Flow.

### O que acontecerá com os canvas que criei usando o editor original?

Todas as suas canvas existentes e o editor de canvas original continuarão a existir e serão suportados pela Braze. Os clientes que optarem por participar do Canvas Flow para acesso antecipado terão a opção de criar um Canvas usando o fluxo de trabalho original ou do Flow.

### Há um limite para quantos passos posso incluir?

Sim. Um canva criado com o Canvas Flow pode conter até 200 etapas.

### Posso iniciar um Canva com etapas desconectadas?

Sim! O Canvas Flow permite que você inicie seu Canvas com etapas desconectadas. Você também pode salvar Canvas após o lançamento com etapas desconectadas. 

### Para onde os usuários acessam quando chegam a uma etapa desconectada?

Se um usuário estiver em uma etapa desconectada do fluxo de trabalho do Canvas Flow, ele avançará para a etapa subsequente, se houver uma, e a configuração da etapa ditará como o usuário deve avançar. O objetivo é permitir que os usuários façam alterações nas etapas sem precisar conectá-las diretamente ao restante do Canva. Isso também abre algum espaço para testes antes de entrar em operação imediatamente, permitindo efetivamente salvar um rascunho.

Recomendamos verificar a exibição de análise de dados para usuários pendentes em uma etapa do Canva antes de desconectar uma etapa.

### Quais são as principais diferenças entre o Canvas Flow e o editor original do Canvas?

#### Barra de ferramentas do componente canva

Anteriormente, com o editor do Canva original, uma etapa completa era adicionada por padrão sempre que você criava qualquer etapa na jornada do usuário. Agora, com o Canvas Flow, essas etapas completas são substituídas por diferentes componentes do Canvas, o que lhe dá o benefício de maior visibilidade e personalização para sua experiência de edição. Você pode ver imediatamente todos os componentes do canva na barra de ferramentas Etapa do canva.

#### Comportamento das etapas

Anteriormente, cada etapa completa incluía informações como configurações de postergação e programação, eventos de exceção, filtros de público, configuração de mensagens e opções de avanço de mensagens, tudo em um único componente. Essas são configurações separadas no Canvas Flow para tornar sua experiência de construção do Canvas mais personalizável e introduz algumas diferenças na funcionalidade.

#### Envio de mensagens

Os [componentes de mensagens]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) adiantam todos os usuários que entram na etapa. Não há necessidade de especificar o comportamento de avanço de mensagens, o que simplifica a configuração da etapa geral. Se quiser implementar a opção **Advance when message sent**, adicione uma jornada do público separada para filtrar os usuários que não receberam a etapa anterior.  

#### Comportamento de postergação

Os [componentes de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) aguardarão todo o tempo de postergação antes de prosseguir para a próxima etapa. 

Digamos que, em 12 de abril, tenhamos um componente Delay em que a postergação é definida para enviar o usuário para a próxima etapa em um dia, às 14h. Um usuário entra no componente às 14h01 do dia 13 de abril. 
- No fluxo de trabalho original, o usuário passaria para a próxima etapa às 14 horas do dia 14 de abril, ou seja, menos de um dia após a hora de entrada. 
- Para o Canvas Flow, o usuário passaria para a próxima etapa às 14 horas do dia 15 de abril. Note que esse é o mesmo horário, mas mais de um dia após o horário de entrada. 

#### Comportamento Intelligent Timing

Como o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) é armazenado no componente Mensagem, as postergações serão aplicadas antes dos cálculos do Intelligent Timing. Isso significa que, dependendo de quando um usuário entra no componente, ele pode receber a mensagem mais tarde do que receberia em um Canvas criado com o fluxo de trabalho original do Canvas.

Digamos que sua postergação esteja definida para 2 dias, o Intelligent Timing esteja ativado e tenha determinado que o melhor horário para o envio de mensagens é às 14 horas. Um usuário entra na etapa de postergação às 2:01 pm.
- **Canvas Flow:** Serão necessárias 48 horas para que a postergação passe, de modo que o usuário receba a mensagem no terceiro dia, às 14 horas.
- **Fluxo de trabalho original:** O usuário recebe a mensagem no segundo dia, às 14 horas.

Note que, se o Intelligent Timing estiver ativado, a mensagem será enviada dentro de 24 horas após o usuário inserir o componente Message no horário inteligente identificado (mesmo que nenhum componente de postergação esteja envolvido).

#### Eventos de exceção

##### Horário de silêncio

A funcionalidade de evento de exceção no Canvas Flow é aplicada usando jornadas de ação, que são separadas das etapas de mensagens. O Horário de silêncio é aplicado no componente Mensagem. Isso significa que, se um usuário já tiver passado pela jornada de ação (e não tiver sido excluído com o evento de exceção lá), então atingiu o Horário de silêncio quando chegou ao componente Mensagem e teve seu Canva configurado de forma que a mensagem seja reenviada após o período de Horário de silêncio, o evento de exceção não será mais aplicado. Note que esse caso de uso não é comum.

Para segmentos e filtros, o componente Canvas Flow Message tem um novo recurso chamado Validações de entrega que permite aos usuários configurar segmentos e filtros adicionais que são validados no momento do envio. Isso evita o caso extremo do Horário de silêncio mencionado anteriormente.

##### Configuração de programação "In" ou "On the next"

Os eventos de exceção no Canvas Flow são criados usando jornadas de ação. As jornadas de ação suportam apenas "após uma janela de tempo X" e não "em X tempo" ou "na próxima vez X".
