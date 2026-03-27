---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artigo fornece uma visão geral do Intelligent Timing (anteriormente Entrega Inteligente) e como você pode aproveitar esse recurso em suas campanhas e canvas."

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use o Intelligent Timing para enviar sua mensagem a cada usuário quando a Braze determinar o horário ideal de envio, que é quando o usuário tem mais chances de interagir (abrir ou clicar). Isso facilita garantir que você está enviando mensagens aos usuários no horário preferido deles, o que pode levar a um maior engajamento.

## Sobre o Intelligent Timing

A Braze calcula o momento ideal para o envio com base em uma análise estatística das interações anteriores dos usuários com seu app e suas interações com cada canal de envio de mensagens. São usados os seguintes dados de interação: 

- Horários das sessões
- Aberturas diretas de push
- Aberturas por influência de push
- Cliques em e-mail
- Aberturas de e-mail (excluindo [aberturas por máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))
- Cliques em SMS (somente se [o encurtamento de links]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) e o rastreamento avançado estiverem ativados)

Por exemplo, Sam pode abrir seus e-mails pela manhã regularmente, mas ela abre seu app e interage com as notificações à noite. Isso significa que Sam receberia uma campanha de e-mail com Intelligent Timing pela manhã, enquanto receberia campanhas com notificações por push à noite, quando é mais provável que ela interaja.

Se um usuário não tiver dados de engajamento relevantes para que a Braze calcule o horário ideal de envio, você pode especificar um horário de fallback.

## Casos de uso

- Enviar campanhas recorrentes que não são sensíveis ao tempo
- Automatizar campanhas com usuários de vários fusos horários
- Enviar mensagens para seus usuários mais engajados (eles terão os dados de engajamento mais relevantes)

## Usando o Intelligent Timing

Esta seção descreve como configurar o Intelligent Timing para suas campanhas e canvas.

{% tabs local %}
{% tab Campaign %}
### Etapa 1: Adicionar Intelligent Timing

1. Crie uma campanha e redija sua mensagem.
2. Selecione **Entrega Programada** como seu tipo de entrega.
3. Em **Opções de Agendamento Baseado no Tempo**, selecione **Intelligent Timing**.
4. Defina a frequência de entrada. Para envios únicos, selecione **Uma vez** e escolha uma data de envio. Para envios recorrentes, selecione **Diariamente**, **Semanalmente** ou **Mensalmente** e configure as opções de recorrência. Consulte as [limitações](#limitations) para mais orientações.
5. Opcionalmente, configure o [horário de silêncio](#quiet-hours).
6. Especifique um [horário de fallback](#campaign-fallback). É quando a mensagem é enviada se o perfil do usuário não tiver nenhum evento relevante para calcular o horário ideal.

![Tela de programação da campanha mostrando o Intelligent Timing com configurações de tempo de fallback e horário de silêncio]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Horário de silêncio {#quiet-hours}

Use o horário de silêncio para impedir que mensagens sejam enviadas durante horários específicos. Isso é útil quando você quer evitar o envio de mensagens durante as primeiras horas da manhã ou durante a noite, mas ainda assim permitir que o Intelligent Timing determine a melhor janela de entrega.

{% alert note %}
O horário de silêncio substituiu a configuração **Enviar apenas em horários específicos**. Em vez de escolher quando as mensagens podem ser enviadas, agora você escolhe quando elas não devem ser enviadas. Por exemplo, para enviar mensagens entre 16h e 18h, defina o horário de silêncio das 18h às 16h do dia seguinte.
{% endalert %}

1. Selecione **Ativar Horário de Silêncio**.
2. Selecione o horário de início e término em que **não** deseja enviar mensagens.

![A opção Horário de silêncio está ativada, com o horário de início e término definidos para bloquear o envio de mensagens durante a noite.]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Quando o horário de silêncio está ativado, a Braze não enviará mensagens durante o período de silêncio, mesmo que esse horário corresponda ao horário ideal de envio do usuário. Se o horário ideal do usuário estiver dentro da janela de silêncio, a mensagem será enviada no limite mais próximo da janela.

Por exemplo, se o horário de silêncio for definido das 22h às 6h e o horário ideal do usuário for 5h30, a Braze reterá a mensagem e a entregará às 6h — o horário mais próximo fora do período de silêncio.

#### Prévia dos horários de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia (somente campanhas).

1. Adicione segmentos ou filtros na etapa de Públicos-Alvo.
2. Na seção **Prévia dos horários de entrega para** (que aparece tanto na etapa de Públicos-Alvo quanto na de Agendar Entrega), selecione seu canal.
3. Clique em **Atualizar Dados**.

![Gráfico de prévia de entrega para Android Push mostrando o pico de engajamento entre 12h e 14h, e o horário mais popular para o app sendo às 14h.]({% image_buster /assets/img/intel-timing-preview.png %})

### Etapa 2: Escolher uma data de envio

Em seguida, selecione uma data de envio para sua campanha. Tenha em mente o seguinte ao programar campanhas com o Intelligent Timing:

#### Lance a campanha com 48 horas de antecedência

Lance sua campanha pelo menos 48 horas antes da data de envio programada. Isso se deve às variações nos fusos horários. A Braze calcula o horário ideal à meia-noite no horário de Samoa (UTC+13), um dos primeiros fusos horários do mundo. Um único dia abrange cerca de 48 horas ao redor do globo, o que significa que, se você lançar uma campanha dentro desse intervalo de 48 horas, é possível que o horário ideal do usuário já tenha passado em seu fuso horário e a mensagem não seja enviada.

{% alert important %}
Se uma campanha for lançada e o horário ideal de um usuário tiver passado há menos de uma hora, a mensagem é enviada imediatamente. Se o horário ideal tiver passado há mais de uma hora, a mensagem não será enviada.
{% endalert %}

#### Janela de 3 dias para filtros de segmento

Se você está direcionando um público que realizou uma ação em um determinado período, permita pelo menos 3 dias nos seus filtros de segmento. Por exemplo, em vez de `First used app more than 1 day ago` e `First used app less than 3 days ago`, use 1 dia e 4 dias.

![Filtros para o público-alvo, onde a campanha tem como alvo usuários que utilizaram o app pela primeira vez entre 1 e 4 dias atrás.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Isso também se deve aos fusos horários — selecionar um período de menos de 3 dias pode fazer com que alguns usuários saiam do segmento antes que seu horário ideal de envio seja alcançado.

Para saber mais, consulte as [Perguntas Frequentes: Intelligent Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Agende variantes vencedoras 2 dias após os Testes A/B

Se você estiver utilizando [Testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), como o envio automático da **Variante Vencedora** ou o uso de uma **Variante Personalizada**, o Intelligent Timing poderá afetar a duração e o timing da sua campanha.

Ao usar o Intelligent Timing, recomendamos programar o envio da Variante Vencedora pelo menos **dois dias após** o início dos Testes A/B. Por exemplo, se o seu teste A/B começar em 16 de abril às 16h, programe a Variante Vencedora para ser enviada não antes de 18 de abril às 16h. Isso dá à Braze tempo suficiente para avaliar o comportamento do usuário e enviar mensagens no momento ideal.

![Seções de Testes A/B mostrando o teste A/B com a Variante Vencedora selecionada, com os critérios vencedores, a data de envio e a hora local de envio selecionados.]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Etapa 3: Configurar o horário de silêncio (opcional)

Opcionalmente, você pode configurar o horário de silêncio para impedir que mensagens sejam enviadas durante um intervalo de tempo específico. Isso pode ser útil se você não quiser entrar em contato com os usuários durante a noite ou em determinados horários, mas geralmente não é recomendado ao usar o Intelligent Timing. Para saber mais, consulte as [limitações](#limitations).

O horário de silêncio funciona como uma janela de não envio. O Intelligent Timing ainda determina o horário ideal de envio de cada usuário, mas se esse horário cair dentro do horário de silêncio, a Braze atrasa a mensagem até o próximo horário disponível fora do período de silêncio.

Para configurar o horário de silêncio:

1. Ao configurar o Intelligent Timing, selecione **Ativar Horário de Silêncio**.
2. Insira o horário de início e término da janela de silêncio.

### Etapa 4: Escolher um horário de fallback {#campaign-fallback}

Escolha um horário de fallback a ser usado caso o perfil do usuário não tenha eventos relevantes para calcular o horário ideal de entrega.

![Agendando uma campanha com Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Etapa 5: Prévia dos horários de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia.

1. Adicione segmentos ou filtros na etapa de **Públicos-Alvo**.
2. Na seção **Prévia dos horários de entrega para** (que aparece tanto na etapa de **Públicos-Alvo** quanto na de **Agendar Entrega**), selecione seu canal.
3. Selecione **Atualizar Dados**.

![Exemplo de prévia dos horários de entrega para Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Sempre que você alterar qualquer configuração do Intelligent Timing ou do público da campanha, atualize os dados novamente para visualizar um gráfico atualizado.

O gráfico mostra em azul os usuários que tiveram eventos relevantes para calcular um horário ideal e em vermelho os usuários que usarão o horário de fallback. Use os filtros de cálculo para ajustar a prévia e ter uma visão mais granular de cada grupo de usuários.
{% endtab %}

{% tab Canvas %}

### Etapa 1: Adicionar Intelligent Timing

No seu Canvas, adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), acesse as **Configurações de Entrega** e selecione **Usando Intelligent Timing**.

As mensagens serão enviadas aos usuários que entraram na etapa naquele dia, no horário local ideal. No entanto, se o horário ideal já tiver passado nesse dia, a entrega será feita nesse horário no dia seguinte. Etapas de mensagem que direcionam vários canais podem enviar ou tentar enviar mensagens em horários diferentes para canais diferentes. Quando a primeira mensagem em uma etapa de Mensagem tenta ser enviada, todos os usuários são avançados automaticamente.

### Etapa 2: Escolher um horário de fallback

Escolha um horário de fallback para enviar a mensagem aos usuários do seu público que não possuem dados de engajamento relevantes para que a Braze calcule o horário ideal de envio. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Etapa 4: Adicionar uma etapa de postergação

Ao contrário das campanhas, você não precisa lançar seu Canvas 48 horas antes da data de envio, pois o Intelligent Timing é definido no nível da etapa, e não no nível do Canvas.

Em vez disso, adicione uma [etapa de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) de pelo menos dois dias corridos entre o momento em que o usuário entra no Canvas e o momento em que recebe a etapa com Intelligent Timing.

#### Dias corridos vs. dias de 24 horas

Ao usar o Intelligent Timing após uma etapa de postergação, a data de entrega pode variar dependendo de como você calcula a postergação. Isso só se aplica quando sua postergação é definida como **Após uma duração**, pois há uma diferença entre como "dias" e "dias corridos" são calculados.

- **Dias:** 1 dia equivale a 24 horas, calculadas a partir do momento em que o usuário entra na etapa de postergação.
- **Dias corridos:** 1 dia é o período desde que o usuário entra na etapa de postergação até a meia-noite no seu fuso horário. Isso significa que 1 dia corrido pode durar apenas alguns minutos.

Ao utilizar o Intelligent Timing, recomendamos usar dias corridos para postergações em vez de dias de 24 horas. Isso porque, com dias corridos, a mensagem será enviada no último dia da postergação, no momento ideal. Com dias de 24 horas, há uma chance de que o horário ideal do usuário seja antes de ele entrar na etapa, o que significa que um dia extra será adicionado à postergação.

Por exemplo, digamos que o horário ideal de Luka é 14h. Ele entra na etapa de postergação às 14h01 do dia 1º de março, e a postergação é definida como 2 dias.

- O dia 1 termina em 2 de março às 14h01
- O dia 2 termina em 3 de março às 14h01

No entanto, o Intelligent Timing está programado para entregar às 14h, horário que já passou. Então Luka não receberá a mensagem até o dia seguinte: 4 de março às 14h.

![Gráfico que ilustra a diferença entre dias e dias corridos. Se o horário ideal do usuário for 14h, mas ele entrar na etapa de postergação às 14h01, e a postergação estiver definida como 2 dias: com dias de 24 horas, a mensagem é entregue 3 dias depois porque o usuário entrou na etapa após o horário ideal; com dias corridos, a mensagem é entregue 2 dias depois, no último dia da postergação.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limitações

- Mensagens no app e webhooks são entregues imediatamente e não recebem horários ideais.
- O Intelligent Timing não está disponível para campanhas baseadas em ações ou disparadas por API.
- O Intelligent Timing não deve ser usado nos seguintes cenários:
    - **Limite de taxa:** Se tanto o limite de taxa quanto o Intelligent Timing forem usados, não há garantia sobre quando a mensagem será entregue. Campanhas recorrentes diárias com Intelligent Timing não suportam com precisão um limite total de envio de mensagens.
    - **Campanhas de aquecimento de IP:** Alguns comportamentos do Intelligent Timing podem causar dificuldades em atingir os volumes diários necessários quando você está começando a aquecer seu IP. Isso ocorre porque o Intelligent Timing avalia os segmentos duas vezes — uma vez quando a campanha ou o canva é criado pela primeira vez, e novamente antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento. Isso pode fazer com que os segmentos mudem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. Esses usuários não são substituídos, impactando o quão próximo do limite máximo de usuários você consegue alcançar.

## Solução de problemas

### Gráfico de prévia mostrando poucos usuários com horários ideais

Se não houver eventos relevantes para um usuário (por exemplo, novos usuários com pouco ou nenhum engajamento), a Braze usa a configuração de fallback definida — seja o seu horário de fallback personalizado ou o horário mais popular para usar o app entre todos os usuários.

### Impacto do fuso horário na entrega do Intelligent Timing

O Intelligent Timing depende do fuso horário local especificado de cada usuário, portanto a data e a hora de entrega programadas podem variar entre os usuários.

Se os usuários não receberem as mensagens como esperado, verifique se o campo de fuso horário nos perfis deles está preenchido corretamente. Se o campo de fuso horário estiver vazio, o usuário poderá receber mensagens alinhadas ao fuso horário da empresa, em vez do seu fuso local.

### Envio além da data agendada

Sua campanha com Intelligent Timing pode estar sendo enviada após a data programada se você estiver utilizando [Testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Campanhas usando otimizações de Testes A/B podem enviar automaticamente a Variante Vencedora após o teste inicial, aumentando a duração da campanha. Por padrão, campanhas com uma otimização enviarão a Variante Vencedora para os usuários restantes no dia seguinte ao teste inicial, mas você pode alterar essa data de envio.

Se você usar o Intelligent Timing, recomendamos deixar mais tempo para o teste A/B terminar e agendar a Variante Vencedora para ser enviada 2 dias após o teste inicial, em vez de 1 dia.

## Perguntas Frequentes (FAQ) {#faq}

### Geral

#### O que o Intelligent Timing prevê?

O Intelligent Timing se concentra em prever quando um usuário tem mais chances de abrir ou clicar nas suas mensagens, garantindo que elas cheguem aos usuários nos momentos de maior engajamento.

#### O Intelligent Timing é calculado separadamente para cada dia da semana?

Não, o Intelligent Timing não está vinculado a dias específicos. Em vez disso, ele personaliza os horários de envio com base nos padrões de engajamento únicos de cada usuário e no canal que você está usando, como e-mail ou notificações por push. Isso garante que suas mensagens cheguem aos usuários quando eles estão mais receptivos.

### Cálculos

#### Quais dados são usados para calcular o horário ideal para cada usuário?

Para calcular o horário ideal, o Intelligent Timing:

1. Analisa os dados de interação de cada usuário registrados pelo SDK da Braze. Isso inclui:
  - Horários de sessão
  - Aberturas diretas de push
  - Aberturas por influência de push
  - Cliques em e-mail
  - Aberturas de e-mail (excluindo aberturas por máquina)
2. Agrupa esses eventos por horário, identificando o momento ideal de envio para cada usuário.

#### As aberturas por máquina são incluídas no cálculo do horário ideal?

Não, as [aberturas por máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) são excluídas dos cálculos do horário ideal. Isso significa que os horários de envio são baseados exclusivamente no engajamento genuíno do usuário, proporcionando um timing mais preciso para suas campanhas.

#### Quão preciso é o horário ideal?

O Intelligent Timing programa mensagens durante a "hora de maior engajamento" de cada usuário, com base nos inícios de sessão e eventos de abertura de mensagens. Dentro dessa hora, o horário da mensagem é arredondado para os cinco minutos mais próximos. Por exemplo, se o horário ideal de um usuário for calculado como 16h58, a mensagem será programada para 17h. Pode haver pequenos atrasos na entrega devido à atividade do sistema durante períodos de alta demanda.

#### Quais são os cálculos de fallback se não houver eventos relevantes?

Se não houver eventos relevantes para um usuário, o Intelligent Timing usa a configuração de fallback definida nas configurações da mensagem — seja um horário de fallback personalizado ou o horário mais popular para usar o app entre todos os usuários. 

### Campanhas

#### Com quanto tempo de antecedência devo lançar uma campanha com Intelligent Timing para entregá-la com sucesso a todos os usuários em todos os fusos horários?

A Braze calcula o horário ideal à meia-noite no horário de Samoa, um dos primeiros fusos horários do mundo. Em um único dia, isso abrange aproximadamente 48 horas. Por exemplo, uma pessoa cujo horário ideal é 0h01 e que mora na Austrália já teve seu horário ideal ultrapassado, e é "tarde demais" para enviar para ela. Por essas razões, você precisa programar com 48 horas de antecedência para entregar com sucesso a todos no mundo que usam seu app.

#### Por que minha campanha com Intelligent Timing está mostrando pouco ou nenhum envio?

Se não houver eventos de engajamento relevantes para um usuário (por exemplo, novos usuários com poucos ou nenhum clique ou abertura), o Intelligent Timing usa a configuração de fallback definida — seja o seu horário de fallback personalizado ou o horário mais popular para usar o app entre todos os usuários.

#### Por que minha campanha com Intelligent Timing está sendo enviada após a data programada?

Sua campanha com Intelligent Timing pode estar sendo enviada após a data programada porque você está usando Testes A/B. Campanhas que usam Testes A/B podem enviar automaticamente a Variante Vencedora após o término do teste A/B, aumentando a duração do envio da campanha. Por padrão, as campanhas com Intelligent Timing serão programadas para enviar a Variante Vencedora para os usuários restantes no dia seguinte, mas você pode alterar essa data de envio.

Recomendamos que, se você tiver campanhas com Intelligent Timing, deixe mais tempo para o teste A/B terminar e programe a Variante Vencedora para ser enviada em dois dias, em vez de um. 

### Funcionalidade

#### Quando a Braze verifica os critérios de elegibilidade para os filtros de segmento e público?

A Braze realiza duas verificações quando uma campanha é lançada:

1. **Verificação inicial:** À meia-noite no primeiro fuso horário no dia do envio.
2. **Verificação no horário programado:** Logo antes do envio, no horário que o Intelligent Timing selecionou para o usuário.

Tenha cuidado ao filtrar com base em outros envios de campanha para evitar direcionar segmentos inelegíveis. Por exemplo, se você enviar duas campanhas no mesmo dia em horários diferentes e adicionar um filtro que permite que os usuários recebam a segunda campanha apenas se tiverem recebido a primeira, os usuários não receberão a segunda campanha. Isso ocorre porque ninguém era elegível quando a campanha foi criada pela primeira vez e os segmentos foram formados.

#### Posso usar o horário de silêncio na minha campanha com Intelligent Timing?

O horário de silêncio pode ser usado em uma campanha que utiliza o Intelligent Timing. O algoritmo do Intelligent Timing evitará o horário de silêncio para que ainda envie a mensagem a todos os usuários elegíveis. Dito isso, recomendamos desativar o horário de silêncio, a menos que haja implicações de política, conformidade ou outras questões legais sobre quando as mensagens podem ou não ser enviadas.

#### O que acontece se o horário ideal de um usuário estiver dentro do horário de silêncio? 

Se o horário ideal determinado cair dentro do horário de silêncio, a Braze encontra o limite mais próximo do horário de silêncio e programa a mensagem para o próximo horário permitido antes ou depois do período de silêncio. A mensagem é enfileirada para envio no limite mais próximo do horário de silêncio em relação ao horário ideal.

#### Posso usar o Intelligent Timing com limite de taxa?

O limite de taxa pode ser usado em uma campanha que utiliza o Intelligent Timing. No entanto, a natureza do limite de taxa significa que alguns usuários podem receber suas mensagens em um momento menos ideal, especialmente se um grande número de usuários em relação ao tamanho do limite de taxa estiver programado para o horário de fallback por não terem eventos relevantes. 

Recomendamos usar o limite de taxa em uma campanha com Intelligent Timing apenas quando houver requisitos técnicos que precisem ser atendidos com o limite de taxa.

#### Posso usar o Intelligent Timing durante o aquecimento de IP?

A Braze não recomenda usar o Intelligent Timing quando os usuários estão começando o aquecimento de IP, pois alguns de seus comportamentos podem causar dificuldades em atingir os volumes diários necessários. Isso ocorre porque o Intelligent Timing avalia os segmentos de campanha duas vezes: uma vez quando a campanha é criada pela primeira vez, e uma segunda vez antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento.

Isso pode fazer com que os segmentos mudem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. Esses usuários não são substituídos, impactando o quão próximo do limite máximo de usuários você consegue alcançar.

#### Como é determinado o horário mais popular do app?

O horário mais popular do app é determinado pelo horário médio de início de sessão do espaço de trabalho (no horário local). Essa métrica pode ser encontrada no dashboard ao visualizar a prévia dos horários de uma campanha, mostrada em vermelho.

#### O Intelligent Timing leva em conta as aberturas por máquina?

Sim, as aberturas por máquina são filtradas pelo Intelligent Timing, de modo que não influenciam o resultado.

#### Como posso garantir que o Intelligent Timing funcione da melhor forma possível?

O Intelligent Timing usa o histórico individual de engajamento com mensagens de cada usuário, considerando os horários em que eles receberam mensagens. Antes de usar o Intelligent Timing, certifique-se de ter enviado mensagens aos usuários em diferentes horários do dia. Dessa forma, você consegue "amostrar" qual pode ser o melhor horário para cada usuário. Uma amostragem inadequada de diferentes horários do dia pode fazer com que o Intelligent Timing escolha um horário de envio abaixo do ideal para um usuário.