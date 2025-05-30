---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 2
description: "Este artigo fornece uma visão geral do Intelligent Timing (anteriormente Entrega Inteligente) e como você pode aproveitar esse recurso em suas campanhas e canvas."

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use Intelligent Timing para entregar sua mensagem a cada usuário quando a Braze determinar que o usuário tem maior probabilidade de interagir (abrir ou clicar), referido como o horário de envio ideal. Isso facilita para você verificar se está enviando mensagens para seus usuários no horário de preferência deles, o que pode levar a um maior engajamento.

## Casos de uso

- Envie campanhas recorrentes que não são sensíveis ao tempo
- Automatize campanhas com usuários de vários fusos horários
- Ao enviar mensagens para seus usuários mais engajados (eles terão os dados de engajamento mais relevantes)

## Como funciona?

Braze calcula o horário de envio ideal com base em uma análise estatística das interações passadas do seu usuário com seu app, e suas interações com cada canal de envio de mensagens. São usados os seguintes dados de interação: 

- Horários das sessões
- Aberturas diretas push
- Aberturas por influência do push
- Cliques no e-mail
- Aberturas de e-mail (excluindo [aberturas por máquina]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens))

Por exemplo, Sam pode abrir seus e-mails pela manhã regularmente, mas ela abre seu app e interage com as notificações à noite. Isso significa que Sam receberia uma campanha de e-mail com Intelligent Timing pela manhã, enquanto ela receberia campanhas com notificações por push à noite, quando é mais provável que ela se envolva.

Se um usuário não tiver dados de engajamento suficientes para a Braze calcular o horário ideal de envio, você pode especificar um [horário de fallback](#fallback-time).

## Usando Intelligent Timing

Esta seção descreve como configurar o Intelligent Timing para suas campanhas e canvas.

### Campanhas

Para usar Intelligent Timing em suas campanhas:

1. Crie uma campanha e componha sua mensagem.
2. Selecione **Entrega Programada** como seu tipo de entrega.
3. Em **Opções de Agendamento Baseado no Tempo**, selecione **Intelligent Timing**.
4. Selecione a data de envio. Veja [nuances da campanha](#campaign-nuances) para considerações.
5. Determine se você deseja [enviar mensagens apenas dentro de horários específicos](#sending-within-specific-hours).
6. Especifique um [prazo de fallback](#fallback-time). Esta é a hora em que a mensagem será enviada se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal.

![Agendando uma campanha com Intelligent Timing][1]

#### Enviando mensagens dentro de horas específicas {#sending-within-specific-hours}

Se desejar, você pode optar por limitar o tempo ideal a uma janela de tempo específica. Isso é útil se sua campanha se refere a um evento, venda ou promoção específica, mas geralmente não é recomendado de outra forma. O envio dentro de horas específicas funciona de forma semelhante ao horário de silêncio, o que não é recomendado com Intelligent Timing, pois é contraproducente. Veja a seção deste artigo sobre [limitações](#limitations) para mais informações.

1. Ao configurar o Intelligent Timing, selecione **Apenas enviar mensagens dentro de horários específicos**.
2. Insira o horário de início e término do período de entrega.

![Caixa de seleção para "Enviar mensagens apenas dentro de horários específicos" selecionada, onde a janela de tempo é definida entre 8h e 12h no fuso local do usuário.][4]

Quando uma janela de entrega é especificada, a Braze analisa apenas os dados de engajamento dentro da janela para determinar o horário ideal de um usuário. Se não houver dados de engajamento suficientes dentro desse período, a mensagem será enviada no horário de [fallback](#fallback-time) especificado.

#### Prévia dos horários de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia (somente campanhas).

1. Adicione segmentos ou filtros na etapa de Públicos-Alvo.
2. Na seção **Prévia dos horários de entrega para** (que aparece em ambos os passos de Públicos-alvos e Agendar Entrega), selecione seu canal.
3. Clique em **Atualizar Dados**.

![][2]

Sempre que você alterar qualquer configuração sobre Intelligent Timing ou seu público de campanha, atualize os dados novamente para visualizar um gráfico atualizado.

O gráfico mostra os usuários que tinham dados suficientes para calcular um tempo ótimo em azul e os usuários que usarão o tempo fallback em vermelho. Use os filtros de cálculo para ajustar a {prévia} para uma visão mais granular de cada grupo de usuários.

#### Nuances da campanha

Aqui estão algumas nuances que você deve estar ciente ao agendar campanhas com Intelligent Timing.

##### Lançamento da campanha

Lance sua campanha pelo menos 48 horas antes da data de envio programada. Isso é por causa das variações nos fusos horários. Braze calcula o horário ideal à meia-noite no horário de Samoa (UTC+13), um dos primeiros fusos horários do mundo. Um único dia abrange cerca de 48 horas em todo o mundo, o que significa que se você lançar uma campanha dentro desse intervalo de 48 horas, é possível que o horário ideal de um usuário já tenha passado em seu fuso horário, e a mensagem não será enviada.

{% alert important %}
Se uma campanha for lançada e o horário ideal de um usuário for menos de uma hora no passado, a mensagem é enviada imediatamente. Se o horário ideal for mais há de uma hora atrás, a mensagem não será enviada.
{% endalert %}

##### Escolhendo segmentos

Se você está direcionando um público que realizou uma ação em um determinado período, permita pelo menos um período de 3 dias em seus filtros de segmento. Por exemplo, em vez de `First used these apps more than 1 day ago` e `First used these apps less than 3 days ago`, use 1 dia e 4 dias.

![Filtros para o público-alvo onde a campanha tem como alvo usuários que usaram esses aplicativos pela primeira vez entre 1 e 4 dias atrás.][3]

Isso também ocorre por causa dos fusos horários — selecionar um período de menos de 3 dias pode fazer com que alguns usuários saiam do segmento antes que seu horário ideal de envio seja alcançado.

Saiba mais sobre [quando a Braze verifica os critérios de elegibilidade para segmentos e filtros]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

##### Testes A/B com otimizações

Se você estiver aproveitando [Testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), como enviar automaticamente a Variante Vencedora após o término do teste A/B, a duração da campanha aumentará. Por padrão, as campanhas de Intelligent Timing enviarão a Variante Vencedora para os usuários restantes no dia seguinte ao teste inicial, mas você pode alterar essa data de envio.

Recomendamos que, se você estiver usando tanto o Intelligent Timing quanto os Testes A/B, agende a Variante Vencedora para ser enviada 2 dias após o teste inicial, em vez de 1 dia.

![Seção de Testes A/B da etapa de Públicos-Alvo onde o teste termina e envia a Variante Vencedora dois dias após o início do teste inicial.][5]

### Canva

Esta seção descreve como usar Intelligent Timing em seus canvas. As etapas variam ligeiramente dependendo de qual fluxo de trabalho da canva você está usando.

{% alert important %}
Desde 28 de fevereiro de 2023, não é mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível para referência para entender como o Intelligent Timing funciona no editor original.<br><br>A Braze recomenda que os clientes que usam a experiência original do canva mudem para o Canvas Flow. É uma experiência de edição aprimorada para melhor construir e gerenciar canvas. Saiba mais sobre a [clonagem de canvas no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

{% tabs %}
{% tab Canvas Flow %}

No Canvas Flow, o Intelligent Timing é definido nas etapas de Mensagem. Para usar Intelligent Timing no seu Canva:

1. Adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) ao seu canva.
2. Acessar **Configurações de Entrega**.
3. Selecione **Using Intelligent Timing**.
4. Especifique um [prazo de fallback](#fallback-time).

Um usuário que entra nesta etapa receberá a mensagem no horário ideal no dia em que entrar, SE esse horário ainda não tiver passado. Nota que se o tempo ótimo de um usuário (em fuso local) já passou no dia em que ele entra em uma etapa de mensagem, ela será enviada no próximo dia no horário ótimo. Etapas de mensagens que têm como alvo vários canais podem enviar ou tentar enviar mensagens em horários diferentes para canais diferentes. Quando a primeira mensagem em uma etapa de Mensagem tenta enviar, todos os usuários são avançados automaticamente.

#### Postergação de etapas e Intelligent Timing

Ao usar o Intelligent Timing após uma [etapa de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), a data de entrega pode ser diferente dependendo de como você calcula sua postergação. Isso só se aplica quando sua postergação é definida para **Após uma duração**, pois há uma diferença entre como "dias" e "dias de calendário" são calculados.

- **Dias:** 1 dia são 24 horas, calculadas a partir do momento em que o usuário entra na etapa de postergação.
- **Dias corridos:** 1 dia é o período desde que o usuário entra na etapa de postergação até a meia-noite em seu fuso horário. Isso significa que 1 dia de calendário pode ser tão curto quanto alguns minutos.

Ao usar Intelligent Timing, recomendamos que você use dias de calendário para seus atrasos em vez de dias de 24 horas. Isso ocorre porque, com os dias de calendário, a mensagem será enviada no último dia da postergação, no momento ideal. Com um dia de 24 horas, há uma chance de que o horário ideal do usuário seja antes de eles entrarem na etapa, o que significa que haverá um dia extra adicionado à sua postergação.

Por exemplo, digamos que o horário ideal de Luka é 14:00. Ele entra na etapa de postergação às 14h01 do dia 1º de março, e a postergação é definida para 2 dias.

- O dia 1 termina em 2 de março às 14h01
- O dia 2 termina em 3 de março às 14h01

No entanto, Intelligent Timing está programado para entregar às 14h, o que já passou. Então Luka não receberá a mensagem até o dia seguinte: 4 de março às 14:00.

![Gráfico que mostra a diferença entre dias e dias corridos onde se o horário ideal de um usuário é 14h, mas ele entra na etapa de postergação às 14h01 e a postergação é definida para 2 dias. Dias entrega a mensagem 3 dias depois porque o usuário entrou na etapa após o seu tempo ideal, enquanto dias de calendário entrega a mensagem 2 dias depois, no último dia da postergação.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}

{% endtab %}
{% tab Fluxo de trabalho original da canva %}

No fluxo de trabalho original da canva, o Intelligent Timing é definido na seção de postergação de uma etapa completa. Para usar Intelligent Timing no seu Canva:

1. Adicione uma etapa ao seu canva.
2. Abra a **Postergação** para sua etapa.
3. Selecione **Programado**.
4. Defina uma postergação usando *depois*, *em* ou *na próxima*.
   - Se você selecionar *após*, defina a postergação em dias ou semanas. Postergações são calculadas automaticamente usando dias de calendário, o que significa que a mensagem é enviada no último dia da postergação no horário ideal do usuário. Intelligent Timing não está disponível para atrasos inferiores a 1 dia.
5. Selecione **Using Intelligent Timing**.
6. Especifique um [prazo de fallback](#fallback-time).

{% endtab %}
{% endtabs %}

#### Lançando o canva

Ao contrário das campanhas, você não precisa se preocupar em lançar sua canva 48 horas antes da data de envio. Isso ocorre porque o Intelligent Timing é definido no nível de etapa, não no nível de canva. Em vez disso, recomendamos que haja pelo menos uma postergação de 48 horas entre o usuário entrar no canva e receber a etapa onde o Intelligent Timing é usado.

### Tempo de fallback {#fallback-time}

Você precisa escolher um horário de fallback para a mensagem ser enviada aos usuários do seu público que não têm dados de engajamento suficientes para a Braze calcular um horário de envio ideal. Existem duas opções:

- o horário mais popular para usar o app entre todos os usuários
- um horário específico do fallback personalizado (no horário local do usuário)

#### Tempo de app mais popular

O horário de app mais popular é determinado pelo horário médio de início da sessão para o seu espaço de trabalho (em fuso local). Este tempo é exibido em vermelho no [gráfico de prévia](#preview-delivery-times) (somente campanhas).

Para campanhas, se você especificou uma [janela de entrega](#sending-within-specific-hours) e o horário mais popular para usar seu app estiver fora dessa janela, a mensagem será enviada o mais próximo possível da borda da janela de entrega. Por exemplo, se seu período de entrega for das 13h às 20h e o horário mais popular do app for às 22h, a mensagem será enviada às 20h.

**Dados de sessão insuficientes**<br>
No raro caso de que seu app não tenha dados de sessão suficientes para calcular quando o app é mais usado (um app completamente novo sem dados), a mensagem será enviada às 17h no fuso local do usuário. Se o fuso local do usuário for desconhecido, ele será enviado às 17h no fuso horário da sua empresa.

É importante estar ciente das limitações de usar Intelligent Timing no início do ciclo de vida de um usuário quando dados limitados estão disponíveis. Ainda pode ser valioso, pois mesmo usuários com poucas sessões registradas podem oferecer insights sobre seu comportamento. No entanto, a Braze pode calcular de forma mais eficaz o momento ideal para envio mais tarde no ciclo de vida de um usuário.

#### Tempo de fallback personalizado

Use o tempo de fallback personalizado para escolher um horário diferente para enviar a mensagem. Similar ao tempo do app mais popular, a mensagem será enviada no horário de fallback no fuso local do usuário. Se o fuso local do usuário for desconhecido, ele será enviado no fuso horário da sua empresa.

Para campanhas com um tempo de fallback personalizado especificado, se você lançar a campanha dentro de 24 horas da data de envio, os usuários cujos horários ideais já passaram receberão a campanha no tempo de fallback personalizado. Se o tempo de fallback personalizado já tiver passado no fuso horário deles, a mensagem será enviada imediatamente.

## Limitações

- Mensagens in-app, Cartões de Conteúdo e webhooks são entregues imediatamente e não são dados tempos ótimos.
- Intelligent Timing não está disponível para campanhas baseadas em ações ou acionadas por API.
- Intelligent Timing não deve ser usado nos seguintes cenários:
    - **Horário de silêncio:** Usar tanto o horário de silêncio quanto o Intelligent Timing é contraproducente, pois o horário de silêncio é baseado em uma suposição de cima para baixo sobre o comportamento do usuário, como não enviar mensagens para alguém no meio da noite, enquanto o Intelligent Timing é baseado na atividade do usuário. Talvez Sam verifique as notificações do seu app às 3 da manhã com frequência. Nós não julgamos.
    - **Limitação de taxa:** Se tanto a limitação de taxa quanto o Intelligent Timing forem usados, não há garantia sobre quando a mensagem será entregue. Campanhas recorrentes diárias com Intelligent Timing não suportam com precisão um limite total de envio de mensagens.
    - **Campanhas de aquecimento de IP:** Alguns comportamentos de Intelligent Timing podem causar dificuldades em atingir os volumes diários necessários quando você está começando a aquecer seu IP. Isso ocorre porque o Intelligent Timing avalia os segmentos duas vezes — uma vez quando a campanha ou canva é criada pela primeira vez, e novamente antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento. Isso pode fazer com que os segmentos mudem e se alterem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. Esses usuários não são substituídos, impactando a proximidade do limite máximo de usuários você pode alcançar.

## Solução de problemas

### Prévia do gráfico mostrando poucos usuários com horários ideais

Braze precisa de uma certa quantidade de dados de engajamento para fazer uma boa estimativa. Se não houver dados de sessão suficientes ou se os usuários segmentados tiverem poucos ou nenhum clique ou abertura (como novos usuários), a Braze usará o tempo de fallback padrão. Dependendo da sua configuração, isso pode ser o tempo de app mais popular ou um tempo de fallback personalizado.

### Envio além da data agendada

Sua campanha de Intelligent Timing pode estar sendo enviada após a data programada se você estiver utilizando [Testes A/B com uma otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Campanhas usando otimizações de Testes A/B podem enviar automaticamente a Variante Vencedora após o teste inicial, aumentando a duração da campanha. Por padrão, campanhas com uma otimização enviarão a Variante Vencedora para os usuários restantes no dia seguinte ao teste inicial, mas você pode alterar essa data de envio.

Se você usar Intelligent Timing, recomendamos deixar mais tempo para o teste A/B terminar e agendar a Variante Vencedora para enviar 2 dias após o teste inicial, em vez de 1 dia.


[1]: {% image_buster /assets/img/intelligent_timing_1.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
[4]: {% image_buster /assets/img/intelligent_timing_hours.png %}
[5]: {% image_buster /assets/img/intelligent_timing_ab_test_duration.png %}
