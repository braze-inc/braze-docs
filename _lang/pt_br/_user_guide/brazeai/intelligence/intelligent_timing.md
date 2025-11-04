---
nav_title: Cronograma inteligente
article_title: Cronograma inteligente
page_order: 1.3
description: "Este artigo fornece uma visão geral do Intelligent Timing (anteriormente Intelligent Delivery) e como você pode aproveitar esse recurso em suas campanhas e Canvases."

---

# [![Curso de aprendizado Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"} Intelligent Timing

> Use o Intelligent Timing para enviar sua mensagem a cada usuário quando o Braze determinar que ele tem maior probabilidade de se envolver (abrir ou clicar), o que é chamado de horário ideal de envio. Isso facilita a verificação de que você está enviando mensagens aos seus usuários no horário preferido deles, o que pode levar a um maior envolvimento.

## Sobre a Intelligent Timing

O Braze calcula o tempo de envio ideal com base em uma análise estatística das interações anteriores do usuário com seu aplicativo e das interações dele com cada canal de mensagens. São usados os seguintes dados de interação: 

- Horários das sessões
- Push Direct Opens
- Aberturas influenciadas por push
- Cliques em e-mails
- Aberturas de e-mail (excluindo [aberturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))

Por exemplo, Sam pode abrir seus e-mails regularmente pela manhã, mas abre seu aplicativo e interage com as notificações à noite. Isso significa que Sam receberia uma campanha de e-mail com Intelligent Timing pela manhã, enquanto receberia campanhas com notificações push à noite, quando é mais provável que ela se envolva.

Se um usuário não tiver dados de engajamento suficientes para que o Braze calcule o tempo de envio ideal, você poderá especificar um tempo de fallback.

## Casos de uso

- Enviar campanhas recorrentes que não sejam sensíveis ao tempo
- Automatize campanhas com usuários de vários fusos horários
- Ao enviar mensagens para seus usuários mais engajados (eles terão os dados de maior engajamento)

## Uso da temporização inteligente

Esta seção descreve como configurar o Intelligent Timing para suas campanhas e Canvases.

{% tabs local %}
{% tab Campaign %}
### Etapa 1: Adicionar sincronização inteligente

1. Crie uma campanha e escreva sua mensagem.
2. Selecione a **entrega programada** como seu tipo de entrega.
3. Em **Time-Based Scheduling Options (Opções de programação com base no tempo**), selecione **Intelligent Timing (Programação inteligente**).
4. Defina a frequência de entrada. Para envios únicos, selecione **Once (Uma vez** ) e selecione uma data de envio. Para envios recorrentes, selecione **Daily**, **Weekly** ou **Monthly** e configure as opções de recorrência. Consulte as [limitações](#limitations) para obter mais orientações.
5. Opcionalmente, configure o [Quiet Hours](#quiet-hours).
6. Especifique um [tempo de fallback](#campaign-fallback). É nesse momento que a mensagem será enviada se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal.

Tela de agendamento de campanha mostrando o Intelligent Timing com tempo de fallback e configurações de Quiet Hours]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Horário de silêncio {#quiet-hours}

Use Quiet Hours para impedir o envio de mensagens durante horários específicos. Isso é útil quando você deseja evitar o envio de mensagens durante a madrugada ou durante a noite, permitindo que o Intelligent Timing determine a melhor janela de entrega.

{% alert note %}
A opção Quiet Hours substituiu a configuração **Only send within specific hours**. Em vez de escolher quando as mensagens podem ser enviadas, agora você escolhe quando elas não devem ser enviadas. Por exemplo, para enviar mensagens entre 16h e 18h, defina Quiet Hours (Horas de silêncio) das 18h às 16h do dia seguinte.
{% endalert %}

1. Selecione **Enable Quiet Hours (Ativar horas de silêncio**).
2. Selecione o horário de início e término para **não** enviar mensagens.

\![Alternância de Quiet Hours ativada com horário de início e término definido para bloquear a entrega de mensagens durante a noite]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Quando o Quiet Hours estiver ativado, o Braze não enviará mensagens durante o período de silêncio, mesmo que esse horário corresponda ao horário ideal de envio de um usuário. Se o horário ideal de um usuário estiver dentro da janela de silêncio, a mensagem será enviada na borda mais próxima da janela.

Por exemplo, se o horário de silêncio estiver definido das 22h às 6h e o horário ideal de um usuário for 5h30, o Braze reterá a mensagem e a entregará às 6h - o horário mais próximo fora da janela de silêncio.

#### Visualizar prazos de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de visualização (somente campanhas).

1. Adicione segmentos ou filtros na etapa Target Audiences (Públicos-alvo).
2. Na seção **Preview Delivery Times for** (que aparece nas etapas Target Audiences e Schedule Delivery), selecione seu canal.
3. Clique em **Refresh Data (Atualizar dados**).

Gráfico de visualização de entrega para Android Push mostrando o horário de pico de engajamento entre 12 e 14 horas, e o horário mais popular do aplicativo sendo 14 horas.]({% image_buster /assets/img/intel-timing-preview.png %})

### Etapa 2: Escolha uma data de envio

Em seguida, selecione uma data de envio para sua campanha. Tenha em mente o seguinte ao programar campanhas com o Intelligent Timing:

#### Lançar a campanha com 48 horas de antecedência

Lance sua campanha pelo menos 48 horas antes da data de envio programada. Isso se deve às variações nos fusos horários. O Braze calcula a hora ideal à meia-noite no horário de Samoa (UTC+13), um dos primeiros fusos horários do mundo. Um único dia abrange cerca de 48 horas em todo o mundo, o que significa que, se você lançar uma campanha dentro desse intervalo de 48 horas, é possível que o horário ideal de um usuário já tenha passado em seu fuso horário, e a mensagem não será enviada.

{% alert important %}
Se uma campanha for lançada e o tempo ideal de um usuário for inferior a uma hora no passado, a mensagem será enviada imediatamente. Se o tempo ideal for superior a uma hora no passado, a mensagem não será enviada.
{% endalert %}

#### Janela de 3 dias para filtros de segmento

Se estiver segmentando um público-alvo que realizou uma ação em um determinado período de tempo, permita uma janela de pelo menos três dias em seus filtros de segmento. Por exemplo, em vez de `First used app more than 1 day ago` e `First used app less than 3 days ago`, use 1 dia e 4 dias.

\![Filtros para o público-alvo em que a campanha tem como alvo os usuários que usaram o aplicativo pela primeira vez entre 1 e 4 dias atrás.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Isso também se deve aos fusos horários - a seleção de um período inferior a 3 dias pode fazer com que alguns usuários saiam do segmento antes que o horário ideal de envio seja atingido.

Para obter mais informações, consulte [FAQ: Intelligent Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Programe as variantes vencedoras 2 dias após o teste A/B

Se estiver aproveitando o [teste A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), como o envio automático da **Variante vencedora** ou o uso de uma **Variante personalizada**, o Intelligent Timing poderá afetar a duração e o tempo da sua campanha.

Ao usar o Intelligent Timing, recomendamos programar o horário de envio da Variante vencedora pelo menos **dois dias após** o início do teste A/B. Por exemplo, se o seu teste A/B começar em 16 de abril às 16h, programe a Variante vencedora para ser enviada não antes de 18 de abril às 16h. Isso dá ao Braze tempo suficiente para avaliar o comportamento do usuário e enviar mensagens no momento ideal.

Seções de teste A/B mostrando o teste A/B com a Variante vencedora selecionada, com critérios vencedores, data de envio e horário de envio local selecionados]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Etapa 3: Escolha uma janela de entrega (opcional)

Opcionalmente, você pode optar por limitar a janela de entrega. Isso pode ser útil se sua campanha estiver relacionada a um evento, venda ou promoção específica, mas geralmente não é recomendado quando se usa o Intelligent Timing. Para obter mais informações, consulte as [limitações](#limitations).

Quando especificado, o Braze usa apenas os dados de engajamento dentro dessa janela para determinar o tempo de entrega ideal para o usuário. Se não houver dados de engajamento suficientes dentro dessa janela, a mensagem será enviada no horário de fallback definido.

Para definir uma janela de entrega:

1. Ao configurar o Intelligent Timing, selecione **Only send messages within specific hours (Somente enviar mensagens em horários específicos**).
2. Digite a hora de início e de término da janela de entrega.

Caixa de seleção de "Only send messages within specific hours" (Enviar mensagens somente em horários específicos) selecionada, em que a janela de horário é definida entre 8h e 12h no horário local do usuário.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Etapa 4: Escolha um horário alternativo {#campaign-fallback}

Escolha um horário alternativo para usar se o perfil de um usuário não tiver dados suficientes para calcular um horário de entrega ideal.

Programação de uma campanha com o Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Etapa 5: Visualizar prazos de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de visualização.

1. Adicione segmentos ou filtros na etapa Target Audiences (Públicos-alvo).
2. Na seção **Preview Delivery Times for** (que aparece nas etapas Target Audiences e Schedule Delivery), selecione seu canal.
3. Selecione **Atualizar dados**.

\![Exemplo de visualização dos tempos de entrega para o Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Sempre que você alterar alguma configuração do Intelligent Timing ou do público-alvo de sua campanha, atualize os dados novamente para visualizar um gráfico atualizado.

O gráfico mostra os usuários que tinham dados suficientes para calcular um horário ideal em azul e os usuários que usarão o horário alternativo em vermelho. Use os filtros de cálculo para ajustar a visualização prévia e obter uma visão mais detalhada de cada grupo de usuários.
{% endtab %}

{% tab Canvas %}

### Etapa 1: Adicionar temporização inteligente

Em seu Canvas, adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), vá para **Configurações de entrega** e selecione **Usando o Intelligent Timing**.

As mensagens serão enviadas aos usuários que entraram na etapa naquele dia em seu horário local ideal. No entanto, se o horário ideal já tiver passado naquele dia, ele será entregue naquele horário no dia seguinte. As etapas de mensagens que visam vários canais podem enviar ou tentar enviar mensagens em momentos diferentes para canais diferentes. Quando a primeira mensagem em uma etapa de Mensagem tenta ser enviada, todos os usuários são automaticamente avançados.

### Etapa 2: Escolha um horário alternativo

Escolha um horário alternativo para a mensagem a ser enviada aos usuários do seu público que não têm dados de engajamento suficientes para que o Braze calcule um horário de envio ideal. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Etapa 4: Adicionar uma etapa de atraso

Ao contrário das campanhas, você não precisa lançar seu Canvas 48 horas antes da data de envio porque o Intelligent Timing é definido no nível da etapa, não no nível do Canvas.

Em vez disso, adicione uma [etapa de Atraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) de pelo menos dois dias corridos entre o momento em que o usuário entra no Canvas e o momento em que ele recebe a etapa de Cronograma inteligente.

#### Calendário vs. Dias de 24 horas

Ao usar o Intelligent Timing após uma etapa de Atraso, a data de entrega pode variar dependendo de como você calcula o atraso. Isso só se aplica quando o atraso é definido como **Após uma duração**, pois há uma diferença entre o cálculo de "dias" e "dias corridos".

- **Dias:** 1 dia corresponde a 24 horas, calculadas a partir do momento em que o usuário insere a etapa Delay (Atraso).
- **Dias de calendário:** 1 dia é o período entre o momento em que o usuário insere a etapa de atraso e a meia-noite em seu fuso horário. Isso significa que um dia do calendário pode ser tão curto quanto alguns minutos.

Ao usar o Intelligent Timing, recomendamos que você use dias corridos para seus atrasos em vez de dias de 24 horas. Isso ocorre porque, com os dias do calendário, a mensagem será enviada no último dia do atraso, no horário ideal. Com um dia de 24 horas, há uma chance de que o horário ideal do usuário seja antes de ele entrar na etapa, o que significa que haverá um dia extra adicionado ao seu atraso.

Por exemplo, digamos que o horário ideal de Luka seja às 14:00 horas. Ele entra na etapa Atraso às 14h01 de 1º de março e o atraso é definido como 2 dias.

- O Dia 1 termina em 2 de março às 14h01
- O Dia 2 termina em 3 de março às 14h01

No entanto, o Intelligent Timing está programado para entregar às 14 horas, que já passou. Portanto, Luka não receberá a mensagem até o dia seguinte: 4 de março, às 14:00 horas.

Gráfico que mostra a diferença entre dias e dias corridos em que, se o horário ideal de um usuário é 14h, mas ele entra na etapa de atraso às 14h01 e o atraso é definido como 2 dias. Days entrega a mensagem 3 dias depois porque o usuário entrou na etapa após o horário ideal, enquanto calendar days entrega a mensagem 2 dias depois, no último dia do atraso.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limitações

- As mensagens no aplicativo, os Content Cards e os webhooks são entregues imediatamente e não recebem tempos ideais.
- O Intelligent Timing não está disponível para campanhas baseadas em ações ou acionadas por API.
- O Intelligent Timing não deve ser usado nos seguintes cenários:
    - **Limitação da taxa:** Se tanto a limitação de taxa quanto o Intelligent Timing forem usados, não haverá garantia de quando a mensagem será entregue. As campanhas recorrentes diárias com Intelligent Timing não suportam com precisão um limite total de envio de mensagens.
    - **Campanhas de aquecimento de IP:** Alguns comportamentos do Intelligent Timing podem causar dificuldades para atingir os volumes diários necessários quando você está aquecendo seu IP pela primeira vez. Isso ocorre porque o Intelligent Timing avalia os segmentos duas vezes - uma vez quando a campanha ou o Canvas é criado pela primeira vez e outra vez antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento. Isso pode fazer com que os segmentos se desloquem e mudem, muitas vezes fazendo com que alguns usuários saiam do segmento na segunda avaliação. Esses usuários não são substituídos, o que afeta a proximidade do limite máximo de usuários que você pode atingir.

## Solução de problemas

### Gráfico de visualização mostrando poucos usuários com horários ideais

O Braze precisa de uma certa quantidade de dados de engajamento para fazer uma boa estimativa. Se não houver dados de sessão suficientes ou se os usuários-alvo tiverem poucos ou nenhum clique ou abertura (como novos usuários), o Braze usará como padrão o tempo de fallback. Dependendo de sua configuração, esse pode ser o horário do aplicativo mais popular ou um horário de fallback personalizado.

### Impacto do fuso horário na entrega do Intelligent Timing

O Intelligent Timing se baseia no fuso horário local especificado de cada usuário, portanto, a data e a hora de entrega programada podem variar entre os usuários.

Se os usuários não receberem as mensagens como esperado, verifique se o campo de fuso horário no perfil deles está preenchido corretamente. Se o campo de fuso horário estiver vazio, o usuário poderá receber mensagens que se alinham com o fuso horário da empresa em vez de seu horário local.

### Envio após a data programada

Sua campanha Intelligent Timing pode estar sendo enviada após a data programada se você estiver usando [testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). As campanhas que usam otimizações de teste A/B podem enviar automaticamente a Variante vencedora após o término do teste inicial, aumentando a duração da campanha. Por padrão, as campanhas com uma otimização enviarão a Variante vencedora para os usuários restantes no dia seguinte ao teste inicial, mas você pode alterar essa data de envio.

Se você usar o Intelligent Timing, recomendamos deixar mais tempo para que o teste A/B termine e agendar o envio da Variante vencedora para 2 dias após o teste inicial, em vez de 1 dia.

## Perguntas frequentes (FAQ) {#faq}

### Geral

#### O que o Intelligent Timing prevê?

O Intelligent Timing se concentra na previsão de quando um usuário tem maior probabilidade de abrir ou clicar em suas mensagens para garantir que elas cheguem aos usuários nos momentos ideais de engajamento.

#### O Intelligent Timing é calculado separadamente para cada dia da semana?

Não, o Intelligent Timing não está vinculado a dias específicos. Em vez disso, ele personaliza os tempos de envio com base nos padrões de envolvimento exclusivos de cada usuário e no canal que você está usando, como e-mail ou notificações por push. Isso garante que suas mensagens cheguem aos usuários quando eles estiverem mais receptivos.

### Cálculos

#### Quais dados são usados para calcular o tempo ideal para cada usuário?

Para calcular o tempo ideal, o Intelligent Timing:

1. Analisa os dados de interação de cada usuário registrados pelo Braze SDK. Isso inclui:
  - Horários das sessões
  - Abertura direta por pressão
  - O empurrador influenciado abre
  - Cliques em e-mails
  - Aberturas de e-mail (excluindo aberturas de máquina)
2. Agrupa esses eventos por horário, identificando o horário ideal de envio para cada usuário.

#### Os Machine Opens são incluídos no cálculo do tempo ideal?

Não, [as aberturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) são excluídas dos cálculos de tempo ideal. Isso significa que os tempos de envio são baseados exclusivamente no envolvimento genuíno do usuário, proporcionando um tempo mais preciso para suas campanhas.

#### Qual é a precisão do tempo ideal?

O Intelligent Timing programa as mensagens durante a "hora de maior envolvimento" de cada usuário com base nos eventos de início de sessão e abertura de mensagens. Dentro dessa hora, o tempo da mensagem é arredondado para os cinco minutos mais próximos. Por exemplo, se o horário ideal de um usuário for calculado como 16:58, a mensagem será agendada para as 17:00 horas. Pode haver pequenos atrasos na entrega devido à atividade do sistema durante os períodos de maior movimento.

#### Quais são os cálculos alternativos se não houver dados suficientes?

Se houver menos de cinco eventos relevantes para um usuário, o Intelligent Timing usará o tempo de fallback nas configurações da mensagem. 

### Campanhas

#### Com quanto tempo de antecedência devo lançar uma campanha do Intelligent Timing para entregá-la com sucesso a todos os usuários em todos os fusos horários?

O Braze calcula o horário ideal à meia-noite no horário de Samoa, um dos primeiros fusos horários do mundo. Em um único dia, ele se estende por aproximadamente 48 horas. Por exemplo, uma pessoa cujo horário ideal é 12:01 e que mora na Austrália já teve seu horário ideal ultrapassado, e é "tarde demais" para enviar para ela. Por esses motivos, você precisa agendar com 48 horas de antecedência para entregar com sucesso a todas as pessoas do mundo que usam seu aplicativo.

#### Por que minha campanha do Intelligent Timing está apresentando poucos ou nenhum envio?

O Braze precisa de um número básico de pontos de dados para fazer uma boa estimativa. Se não houver dados de sessão suficientes ou se os usuários visados tiverem poucos ou nenhum clique ou abertura de e-mail (como novos usuários), o Intelligent Timing poderá usar como padrão a hora mais popular do espaço de trabalho naquele dia da semana. Se não houver informações suficientes sobre o espaço de trabalho, voltaremos ao horário padrão de 17 horas. Você também pode optar por definir um tempo de fallback específico.

#### Por que minha campanha do Intelligent Timing está sendo enviada após a data programada?

Sua campanha Intelligent Timing pode estar sendo enviada após a data programada porque você está usando testes A/B. As campanhas que usam testes A/B podem enviar automaticamente a Variante vencedora após o término do teste A/B, aumentando a duração do envio da campanha. Por padrão, as campanhas do Intelligent Timing serão programadas para enviar a Variante Vencedora para os usuários restantes no dia seguinte, mas você pode alterar essa data de envio.

Recomendamos que, se você tiver campanhas de Intelligent Timing, deixe mais tempo para o teste A/B terminar e programe a Variante vencedora para ser enviada em dois dias, em vez de um. 

### Funcionalidade

#### Quando o Braze verifica os critérios de elegibilidade para os filtros de segmento e público-alvo?

O Braze realiza duas verificações quando uma campanha é lançada:

1. **Verificação inicial:** À meia-noite do primeiro fuso horário no dia do envio.
2. **Verificação de horário programado:** Imediatamente antes do envio, no horário em que o Intelligent Timing for selecionado pelo usuário.

Tenha cuidado ao filtrar com base em outros envios de campanha para evitar a segmentação de segmentos inelegíveis. Por exemplo, se você enviar duas campanhas no mesmo dia, em horários diferentes, e adicionar um filtro que só permita que os usuários recebam a segunda campanha se tiverem recebido a primeira, os usuários não receberão a segunda campanha. Isso ocorre porque ninguém era elegível quando a campanha foi criada e os segmentos foram formados.

#### Posso usar o Quiet Hours em minha campanha de Intelligent Timing?

O Quiet Hours pode ser usado em uma campanha que usa o Intelligent Timing. O algoritmo Intelligent Timing evitará as horas de silêncio para que ainda envie a mensagem a todos os usuários qualificados. Dito isso, recomendamos desativar o Quiet Hours, a menos que haja implicações de política, conformidade ou outras implicações legais sobre quando as mensagens podem ou não ser enviadas.

#### O que acontece se o horário ideal para um usuário estiver dentro do horário de silêncio? 

Se o horário ideal determinado estiver dentro do horário de silêncio, o Braze encontrará a borda mais próxima do horário de silêncio e programará a mensagem para o próximo horário permitido antes ou depois do horário de silêncio. A mensagem é enfileirada para envio no limite mais próximo do Quiet Hours em relação ao horário ideal.

#### Posso usar o Intelligent Timing e a limitação de taxa?

A limitação de taxa pode ser usada em uma campanha que usa o Intelligent Timing. No entanto, a natureza da limitação de taxa significa que alguns usuários podem receber suas mensagens em um horário abaixo do ideal, principalmente se um grande número de usuários em relação ao tamanho do limite de taxa estiver programado no horário de fallback devido à insuficiência de dados. 

Recomendamos usar a limitação de taxa em uma campanha do Intelligent Timing somente quando houver requisitos técnicos que devam ser atendidos com a limitação de taxa.

#### Posso usar o Intelligent Timing durante o aquecimento do IP?

A Braze não recomenda o uso do Intelligent Timing quando os usuários estão fazendo o primeiro aquecimento de IP, pois alguns de seus comportamentos podem causar dificuldades para atingir os volumes diários. Isso é causado pelo fato de o Intelligent Timing avaliar os segmentos de campanha duas vezes. Uma vez, quando a campanha é criada pela primeira vez, e uma segunda vez antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento.

Isso pode fazer com que os segmentos se desloquem e mudem, muitas vezes fazendo com que alguns usuários saiam do segmento na segunda avaliação. Esses usuários não são substituídos, o que afeta a proximidade do limite máximo de usuários que você pode atingir.

#### Como é determinado o tempo do aplicativo mais popular?

O horário mais popular do aplicativo é determinado pelo horário médio de início da sessão para o espaço de trabalho (no horário local). Essa métrica pode ser encontrada no painel ao visualizar os horários de uma campanha, mostrada em vermelho.

#### O Intelligent Timing leva em conta as aberturas de máquina?

Sim, as aberturas da máquina são filtradas pelo Intelligent Timing, de modo que não influenciam sua saída.

#### Como posso garantir que o Intelligent Timing funcione da melhor forma possível?

O Intelligent Timing usa o histórico individual de engajamento de mensagens de cada usuário nos horários em que ele recebeu as mensagens. Antes de usar o Intelligent Timing, certifique-se de ter enviado mensagens aos usuários em diferentes horários do dia. Dessa forma, você pode "experimentar" qual é o melhor momento para cada usuário. A amostragem inadequada de diferentes horários do dia pode fazer com que o Intelligent Timing escolha um horário de envio abaixo do ideal para um usuário.



