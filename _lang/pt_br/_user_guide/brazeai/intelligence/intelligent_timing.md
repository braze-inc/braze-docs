---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artigo fornece uma visão geral do Intelligent Timing (anteriormente Entrega Inteligente) e como você pode aproveitar esse recurso em suas campanhas e canvas."

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use Intelligent Timing para entregar sua mensagem a cada usuário quando a Braze determinar que o usuário tem maior probabilidade de interagir (abrir ou clicar), referido como o horário de envio ideal. Isso facilita para você verificar se está enviando mensagens para seus usuários no horário de preferência deles, o que pode levar a um maior engajamento.

## Sobre a Intelligent Timing

Braze calcula o horário de envio ideal com base em uma análise estatística das interações passadas do seu usuário com seu app, e suas interações com cada canal de envio de mensagens. São usados os seguintes dados de interação: 

- Horários das sessões
- Aberturas diretas push
- Aberturas por influência do push
- Cliques no e-mail
- Aberturas de e-mail (excluindo [aberturas por máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))

Por exemplo, Sam pode abrir seus e-mails pela manhã regularmente, mas ela abre seu app e interage com as notificações à noite. Isso significa que Sam receberia uma campanha de e-mail com Intelligent Timing pela manhã, enquanto ela receberia campanhas com notificações por push à noite, quando é mais provável que ela se envolva.

Se um usuário não tiver dados de engajamento suficientes para que o Braze calcule o tempo de envio ideal, você poderá especificar um tempo de fallback.

## Casos de uso

- Envie campanhas recorrentes que não são sensíveis ao tempo
- Automatize campanhas com usuários de vários fusos horários
- Ao enviar mensagens para seus usuários mais engajados (eles terão os dados de engajamento mais relevantes)

## Usando Intelligent Timing

Esta seção descreve como configurar o Intelligent Timing para suas campanhas e canvas.

{% tabs local %}
{% tab Campaign %}
### Etapa 1: Adicionar Intelligent Timing

1. Crie uma campanha e componha sua mensagem.
2. Selecione a **entrega programada** como seu tipo de entrega.
3. Em **Opções de Agendamento Baseado no Tempo**, selecione **Intelligent Timing**.
4. Defina a frequência de entrada. Para envios únicos, selecione **Once (Uma vez** ) e selecione uma data de envio. Para envios recorrentes, selecione **Daily**, **Weekly** ou **Monthly** e configure as opções de recorrência. Consulte as [limitações](#limitations) para obter mais orientações.
5. Opcionalmente, configure [o Horário de silêncio](#quiet-hours).
6. Especifique um [prazo de fallback](#campaign-fallback). Esta é a hora em que a mensagem será enviada se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal.

![Tela de programação de campanha mostrando o Intelligent Timing com configurações de horário de fallback e horário de silêncio]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Horário de silêncio {#quiet-hours}

Use o Horário de silêncio para impedir o envio de mensagens durante horários específicos. Isso é útil quando você deseja evitar o envio de mensagens durante a madrugada ou durante a noite, permitindo que o Intelligent Timing determine a melhor janela de entrega.

{% alert note %}
O Horário de silêncio substituiu a configuração **Somente enviar em horários específicos**. Em vez de escolher quando as mensagens podem ser enviadas, agora você escolhe quando elas não devem ser enviadas. Por exemplo, para enviar mensagens entre as 16h e as 18h, defina o Horário de silêncio das 18h às 16h do dia seguinte.
{% endalert %}

1. Selecione **Ativar horário de silêncio**.
2. Selecione a hora de início e de ponta para **não** enviar mensagens.

![Horário de silêncio ativado com horário de início e de ponta a ponta definido para bloquear o envio de mensagens durante a noite]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Quando o Quiet Hours estiver ativado, o Braze não enviará mensagens durante o horário de silêncio, mesmo que esse horário corresponda ao horário ideal de envio de um usuário. Se o horário ideal de um usuário estiver dentro da janela de silêncio, a mensagem será enviada na borda mais próxima da janela.

Por exemplo, se o horário de silêncio for definido das 22h às 6h e o horário ideal de um usuário for 5h30, o Braze reterá a mensagem e a entregará às 6h - o horário mais próximo fora da janela de silêncio.

#### Prévia dos horários de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia (somente campanhas).

1. Adicione segmentos ou filtros na etapa de Públicos-Alvo.
2. Na seção **Prévia dos horários de entrega para** (que aparece em ambos os passos de Públicos-alvos e Agendar Entrega), selecione seu canal.
3. Clique em **Atualizar Dados**.

![Gráfico de prévia de entrega para Android Push mostrando o horário de pico de engajamento entre 12 e 14 horas, e o horário mais popular do app sendo 14 horas.]({% image_buster /assets/img/intel-timing-preview.png %})

### Etapa 2: Escolha uma data de envio

Em seguida, selecione uma data de envio para sua campanha. Tenha em mente o seguinte ao programar campanhas com o Intelligent Timing:

#### Lançar a campanha com 48 horas de antecedência

Lance sua campanha pelo menos 48 horas antes da data de envio programada. Isso é por causa das variações nos fusos horários. Braze calcula o horário ideal à meia-noite no horário de Samoa (UTC+13), um dos primeiros fusos horários do mundo. Um único dia abrange cerca de 48 horas em todo o mundo, o que significa que se você lançar uma campanha dentro desse intervalo de 48 horas, é possível que o horário ideal de um usuário já tenha passado em seu fuso horário, e a mensagem não será enviada.

{% alert important %}
Se uma campanha for lançada e o horário ideal de um usuário for menos de uma hora no passado, a mensagem é enviada imediatamente. Se o horário ideal for mais há de uma hora atrás, a mensagem não será enviada.
{% endalert %}

#### Janela de 3 dias para filtros de segmento

Se você está direcionando um público que realizou uma ação em um determinado período, permita pelo menos um período de 3 dias em seus filtros de segmento. Por exemplo, em vez de `First used app more than 1 day ago` e `First used app less than 3 days ago`, use 1 dia e 4 dias.

![Filtros para o público-alvo em que a campanha direciona os usuários que usaram o app pela primeira vez entre 1 e 4 dias atrás.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Isso também ocorre por causa dos fusos horários — selecionar um período de menos de 3 dias pode fazer com que alguns usuários saiam do segmento antes que seu horário ideal de envio seja alcançado.

Para saber mais, consulte [FAQ: Intelligent Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Programe as variantes vencedoras 2 dias após o teste A/B

Se estiver aproveitando [os Testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), como o envio automático da **Variante Vencedora** ou o uso de uma **Variante Personalizada**, o Intelligent Timing poderá afetar a duração e o momento da sua campanha.

Ao usar o Intelligent Timing, recomendamos programar o horário de envio da variante vencedora pelo menos **dois dias após** o início do teste A/B. Por exemplo, se seu Testes A/B começar em 16 de abril às 16h, programe a Variante vencedora para ser enviada antes de 18 de abril às 16h. Isso dá ao Braze tempo suficiente para avaliar o comportamento do usuário e enviar mensagens no momento ideal.

![Seções de teste A/B mostrando o teste A/B com a Variante vencedora selecionada, com critérios vencedores, data de envio e fuso local de envio selecionados]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Etapa 3: Escolha uma janela de entrega (opcional)

Opcionalmente, você pode optar por limitar a janela de entrega. Isso pode ser útil se sua campanha estiver relacionada a um evento, venda ou promoção específica, mas geralmente não é recomendado quando se usa o Intelligent Timing. Para saber mais, consulte as [limitações](#limitations).

Quando especificado, o Braze usa apenas os dados de engajamento dentro dessa janela para determinar o tempo de entrega ideal para o usuário. Se não houver dados de engajamento suficientes dentro dessa janela, a mensagem será enviada em seu horário de fallback definido.

Para definir uma janela de entrega:

1. Ao configurar o Intelligent Timing, selecione **Apenas enviar mensagens dentro de horários específicos**.
2. Insira o horário de início e término do período de entrega.

![Caixa de seleção de "Only send messages within specific hours" (Enviar mensagens somente dentro de horas específicas) selecionada, em que a janela de tempo é definida entre 8h e 12h no fuso local do usuário.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Etapa 4: Escolha um horário de fallback {#campaign-fallback}

Escolha um tempo de fallback para usar se o perfil de um usuário não tiver dados suficientes para calcular um tempo de entrega ideal.

![Agendamento de uma campanha com o Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Etapa 5: Prévia dos horários de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia.

1. Adicione segmentos ou filtros na etapa de Públicos-Alvo.
2. Na seção **Prévia dos horários de entrega para** (que aparece em ambos os passos de Públicos-alvos e Agendar Entrega), selecione seu canal.
3. Selecione **Atualizar dados**.

![Exemplo de prévia dos tempos de entrega para o Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Sempre que você alterar qualquer configuração sobre Intelligent Timing ou seu público de campanha, atualize os dados novamente para visualizar um gráfico atualizado.

O gráfico mostra os usuários que tinham dados suficientes para calcular um tempo ótimo em azul e os usuários que usarão o tempo fallback em vermelho. Use os filtros de cálculo para ajustar a {prévia} para uma visão mais granular de cada grupo de usuários.
{% endtab %}

{% tab Canva %}
{% alert important %}
A partir de 28 de fevereiro de 2023, as telas que usam o editor original não poderão mais ser criadas ou duplicadas. Para saber como passar para o novo Canvas Flow, consulte [Clonagem de telas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

### Etapa 1: Adicionar Intelligent Timing

Em seu Canvas, adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), acesse **Configurações de entrega** e selecione **Usar Intelligent Timing**.

As mensagens serão enviadas aos usuários que entraram na etapa naquele dia em seu fuso local ideal. No entanto, se o horário ideal já tiver passado naquele dia, ele será entregue naquele horário no dia seguinte. Etapas de mensagens que têm como alvo vários canais podem enviar ou tentar enviar mensagens em horários diferentes para canais diferentes. Quando a primeira mensagem em uma etapa de Mensagem tenta enviar, todos os usuários são avançados automaticamente.

### Etapa 2: Escolha um horário de fallback

Escolha um horário de fallback para a mensagem a ser enviada aos usuários do seu público que não têm dados de engajamento suficientes para que o Braze calcule um horário de envio ideal. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Etapa 4: Adicionar uma etapa de postergação

Ao contrário das campanhas, não é necessário lançar o Canvas 48 horas antes da data de envio porque o Intelligent Timing é definido no nível da etapa do canva, não no nível do Canvas.

Em vez disso, adicione uma [etapa de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) de pelo menos dois dias corridos entre a entrada do usuário no Canva e o recebimento da etapa do Intelligent Timing.

#### Calendário vs. Dias de 24 horas

Ao usar o Intelligent Timing após uma etapa de postergação, a data de entrega pode variar dependendo de como você calcula a postergação. Isso só se aplica quando sua postergação é definida para **Após uma duração**, pois há uma diferença entre como "dias" e "dias de calendário" são calculados.

- **Dias:** 1 dia são 24 horas, calculadas a partir do momento em que o usuário entra na etapa de postergação.
- **Dias corridos:** 1 dia é o período desde que o usuário entra na etapa de postergação até a meia-noite em seu fuso horário. Isso significa que 1 dia de calendário pode ser tão curto quanto alguns minutos.

Ao usar Intelligent Timing, recomendamos que você use dias de calendário para seus atrasos em vez de dias de 24 horas. Isso ocorre porque, com os dias de calendário, a mensagem será enviada no último dia da postergação, no momento ideal. Com um dia de 24 horas, há uma chance de que o horário ideal do usuário seja antes de eles entrarem na etapa, o que significa que haverá um dia extra adicionado à sua postergação.

Por exemplo, digamos que o horário ideal de Luka é 14:00. Ele entra na etapa de postergação às 14h01 do dia 1º de março, e a postergação é definida para 2 dias.

- O dia 1 termina em 2 de março às 14h01
- O dia 2 termina em 3 de março às 14h01

No entanto, Intelligent Timing está programado para entregar às 14h, o que já passou. Então Luka não receberá a mensagem até o dia seguinte: 4 de março às 14:00.

![Gráfico que mostra a diferença entre dias e dias corridos onde se o horário ideal de um usuário é 14h, mas ele entra na etapa de postergação às 14h01 e a postergação é definida para 2 dias. Dias entrega a mensagem 3 dias depois porque o usuário entrou na etapa após o seu tempo ideal, enquanto dias de calendário entrega a mensagem 2 dias depois, no último dia da postergação.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limitações

- Mensagens in-app, Cartões de Conteúdo e webhooks são entregues imediatamente e não são dados tempos ótimos.
- Intelligent Timing não está disponível para campanhas baseadas em ações ou acionadas por API.
- Intelligent Timing não deve ser usado nos seguintes cenários:
    - **Limitação de taxa:** Se tanto a limitação de taxa quanto o Intelligent Timing forem usados, não há garantia sobre quando a mensagem será entregue. Campanhas recorrentes diárias com Intelligent Timing não suportam com precisão um limite total de envio de mensagens.
    - **Campanhas de aquecimento de IP:** Alguns comportamentos de Intelligent Timing podem causar dificuldades em atingir os volumes diários necessários quando você está começando a aquecer seu IP. Isso ocorre porque o Intelligent Timing avalia os segmentos duas vezes — uma vez quando a campanha ou canva é criada pela primeira vez, e novamente antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento. Isso pode fazer com que os segmentos mudem e se alterem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. Esses usuários não são substituídos, impactando a proximidade do limite máximo de usuários você pode alcançar.

## Solução de problemas

### Prévia do gráfico mostrando poucos usuários com horários ideais

Braze precisa de uma certa quantidade de dados de engajamento para fazer uma boa estimativa. Se não houver dados de sessão suficientes ou se os usuários segmentados tiverem poucos ou nenhum clique ou abertura (como novos usuários), a Braze usará o tempo de fallback padrão. Dependendo da sua configuração, isso pode ser o tempo de app mais popular ou um tempo de fallback personalizado.

### Envio além da data agendada

Sua campanha de Intelligent Timing pode estar sendo enviada após a data programada se você estiver utilizando [Testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Campanhas usando otimizações de Testes A/B podem enviar automaticamente a Variante Vencedora após o teste inicial, aumentando a duração da campanha. Por padrão, campanhas com uma otimização enviarão a Variante Vencedora para os usuários restantes no dia seguinte ao teste inicial, mas você pode alterar essa data de envio.

Se você usar Intelligent Timing, recomendamos deixar mais tempo para o teste A/B terminar e agendar a Variante Vencedora para enviar 2 dias após o teste inicial, em vez de 1 dia.

## Perguntas Frequentes (FAQ) {#faq}

### Geral

#### O que o Intelligent Timing prevê?

O Intelligent Timing se concentra em prever quando um usuário é mais provável de abrir ou clicar em suas mensagens para garantir que suas mensagens cheguem aos usuários em momentos de engajamento ideais.

#### O Intelligent Timing é calculado separadamente para cada dia da semana?

Não, o Intelligent Timing não está vinculado a dias específicos. Em vez disso, ele personaliza os horários de envio com base nos padrões de engajamento únicos de cada usuário e no canal que você está usando, como e-mail ou notificações por push. Isso garante que suas mensagens cheguem aos usuários quando eles estão mais receptivos.

### Cálculos

#### Quais dados são usados para calcular o horário ideal para cada usuário?

Para calcular o horário ideal, o Intelligent Timing:

1. Analisa os dados de interação de cada usuário registrados pelo SDK da Braze. Isso inclui:
  - Horários de sessão
  - Aberturas diretas por push
  - Aberturas por influência por push
  - Cliques em e-mail
  - Aberturas de e-mail (excluindo aberturas de máquina)
2. Agrupa esses eventos por tempo, identificando o horário de envio ideal para cada usuário.

#### As Aberturas de Máquina estão incluídas ao calcular o horário ideal?

Não, as [Aberturas por máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) são excluídas dos cálculos para o horário ideal. Isso significa que os horários de envio são baseados exclusivamente no engajamento genuíno do usuário, proporcionando um timing mais preciso para suas campanhas.

#### Quão preciso é o horário ideal?

O Intelligent Timing programa mensagens durante a "hora mais engajada" de cada usuário com base em seus inícios de sessão e eventos de abertura de mensagens. Dentro dessa hora, o tempo da mensagem é arredondado para o minuto mais próximo de cinco. Por exemplo, se o tempo ideal de um usuário for calculado como 16:58, a mensagem será programada para 17:00. Pode haver pequenos atrasos na entrega devido à atividade do sistema durante períodos de alta demanda.

#### Quais são os cálculos de fallback se não houver dados suficientes?

Se houver menos de cinco eventos relevantes para um usuário, o Intelligent Timing usará o tempo de fallback nas configurações de mensagem. 

### Campanhas

#### Com quanto tempo de antecedência devo lançar uma campanha do Intelligent Timing para entregá-la com sucesso a todos os usuários em todos os fusos horários?

A Braze calcula o horário ideal à meia-noite no horário de Samoa, um dos primeiros fusos horários do mundo. Em um único dia, ele se estende por aproximadamente 48 horas. Por exemplo, uma pessoa cujo horário ideal é 12h01 e que mora na Austrália já teve seu horário ideal ultrapassado e é "tarde demais" para enviar para ela. Por essas razões, você precisa programar com 48 horas de antecedência para entregar com sucesso a todos no mundo que usam seu app.

#### Por que minha campanha Intelligent Timing está mostrando pouco ou nenhum envio?

A Braze precisa de um número básico de pontos de dados para fazer uma boa estimativa. Se não houver dados de sessão suficientes ou se os usuários direcionados tiverem poucos ou nenhum clique ou abertura de e-mail (como novos usuários), o Intelligent Timing poderá usar como padrão a hora mais popular do espaço de trabalho naquele dia da semana. Se não houver informações suficientes sobre o espaço de trabalho, voltaremos ao horário padrão de 17 horas. Você também pode optar por definir um tempo de fallback específico.

#### Por que minha campanha do Intelligent Timing está sendo enviada após a data programada?

Sua campanha Intelligent Timing pode estar sendo enviada após a data programada porque você está usando testes A/B. As campanhas que usam Testes A/B podem enviar automaticamente a variante vencedora após o término do teste A/B, aumentando a duração do envio da campanha. Por padrão, as campanhas do Intelligent Timing serão programadas para enviar a Variante Vencedora para os usuários restantes no dia seguinte, mas você pode alterar essa data de envio.

Recomendamos que, se você tiver campanhas Intelligent Timing, deixe mais tempo para o teste A/B terminar e programe a variante vencedora para ser enviada em dois dias, em vez de um. 

### Funcionalidade

#### Quando a Braze verifica os critérios de elegibilidade para os filtros de segmento e público?

A Braze realiza duas verificações quando uma campanha é lançada:

1. **Verificação inicial:** À meia-noite no primeiro fuso horário no dia do envio.
2. **Verificação do horário programado:** Logo antes do envio, no horário que o Intelligent Timing selecionou para o usuário.

Tenha cuidado ao filtrar com base em outros envios de campanha para evitar direcionar segmentos inelegíveis. Por exemplo, se você enviar duas campanhas no mesmo dia em horários diferentes e adicionar um filtro que permite que os usuários recebam a segunda campanha apenas se tiverem recebido a primeira, os usuários não receberão a segunda campanha. Isso se deve ao fato de que ninguém era elegível quando a campanha foi criada pela primeira vez e os segmentos foram formados.

#### Posso usar o horário de silêncio em minha campanha Intelligent Timing?

Os Horários de Silêncio podem ser usados em uma campanha que utiliza o Intelligent Timing. O algoritmo Intelligent Timing evitará os Horários de Silêncio para que ainda envie a mensagem a todos os usuários elegíveis. Dito isso, recomendamos desativar os Horários de Silêncio, a menos que haja implicações de política, conformidade ou outras questões legais sobre quando as mensagens podem e não podem ser enviadas.

#### O que acontece se o horário ideal para um usuário estiver dentro dos Horários de Silêncio? 

Se o horário ideal determinado cair dentro dos Horários de Silêncio, o Braze encontra a borda mais próxima dos Horários de Silêncio e programa a mensagem para a próxima hora permitida antes ou depois dos Horários de Silêncio. A mensagem é enfileirada para ser enviada no limite mais próximo do horário de silêncio em relação ao tempo ideal.

#### Posso usar o Intelligent Timing e o limite de frequência?

O limite de frequência pode ser usado em uma campanha que utiliza Intelligent Timing. No entanto, a natureza do limite de frequência significa que alguns usuários podem receber sua mensagem em um horário menos que ideal, particularmente se um grande número de usuários em relação ao tamanho do limite de frequência estiver agendado para o horário de fallback devido à falta de dados. 

Recomendamos usar o limite de frequência em uma campanha de Intelligent Timing apenas quando houver requisitos técnicos que devem ser atendidos usando o limite de frequência.

#### Posso usar o Intelligent Timing durante o aquecimento de IP?

A Braze não recomenda usar Intelligent Timing quando os usuários estão primeiro aquecendo o IP, pois alguns de seus comportamentos podem causar dificuldades em atingir volumes diários. Isso é causado pelo fato de o Intelligent Timing avaliar os segmentos de campanha duas vezes. Uma vez, quando a campanha é criada pela primeira vez, e uma segunda vez antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento.

Isso pode fazer com que os segmentos mudem e se alterem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. Esses usuários não são substituídos, impactando quão próximo do limite máximo de usuários você pode alcançar.

#### Como é determinado o tempo do app mais popular?

O horário mais popular do app é determinado pelo horário médio de início da sessão para o espaço de trabalho (no fuso local). Essa métrica pode ser encontrada no dashboard durante a prévia dos tempos de uma campanha, mostrada em vermelho.

#### O Intelligent Timing leva em conta as aberturas de máquina?

Sim, as aberturas por máquina são filtradas pelo Intelligent Timing, de modo que não influenciam o resultado.

#### Como posso garantir que o Intelligent Timing funcione da melhor forma possível?

Intelligent Timing usa o histórico individual de engajamento com mensagens de cada usuário em qualquer horário que eles receberam mensagens. Antes de usar o Intelligent Timing, certifique-se de ter enviado mensagens aos usuários em diferentes momentos do dia. Dessa forma, você pode "amostrar" quando pode ser o melhor horário para cada usuário. A amostragem inadequada de diferentes horários do dia pode fazer com que o Intelligent Timing escolha um horário de envio abaixo do ideal para um usuário.



