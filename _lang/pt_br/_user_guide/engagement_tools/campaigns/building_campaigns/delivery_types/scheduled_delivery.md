---
nav_title: Entrega programada
article_title: Entrega programada
page_order: 0
page_type: reference
description: "Este artigo de referência descreve as diferenças entre as opções de programação baseadas em tempo para a entrega de campanhas."
tool: Campaigns

---

# Entrega programada

> As campanhas enviadas usando a entrega programada com base no tempo são entregues em dias específicos.

## Opção 1: Envie assim que a campanha for lançada

Se você optar por enviar uma mensagem assim que ela for lançada, sua mensagem começará a ser enviada assim que você terminar de criar sua campanha.

![A seção "Entrega" com a opção "Agendado" selecionada e a opção de programação baseada em tempo de envio assim que a campanha for lançada.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Esse tipo de programação foi criado para campanhas únicas que você deseja enviar imediatamente, como mensagens sobre um evento atual. Um app de esportes, por exemplo, pode programar notificações por push sobre atualizações de pontuação usando essa opção. Além disso, ao enviar mensagens de teste destinadas apenas a você ou à sua equipe, essa opção permite que você as entregue imediatamente. 

Se planeja editar a campanha e reenviá-la depois de visualizar o teste, certifique-se de marcar a caixa que torna os usuários [novamente elegíveis]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) para receber a campanha. Por padrão, a Braze envia uma campanha para um usuário apenas uma vez, a menos que essa caixa esteja marcada.

## Opção 2: Enviar em um horário determinado

O agendamento de uma campanha para um horário determinado permite que você especifique os dias e horários em que sua campanha será enviada. É possível enviar uma mensagem uma vez, diariamente, semanalmente ou mensalmente em um determinado horário do dia, além de especificar quando a campanha deve começar e terminar. Essa data final é inclusiva, o que significa que o último envio será na data final.

Se você selecionar uma programação mensal recorrente, observe que alguns meses podem não ter o dia selecionado. Por exemplo, digamos que você configure uma campanha para enviar mensalmente no dia 31. Nesse cenário, a Braze envia no último dia daquele mês, como 30 de abril, porque 31 de abril não existe.

Se selecionar **Entrega programada** e não optar por enviar no horário local do usuário, sua campanha será enviada de acordo com o fuso horário especificado na página **Configurações da Empresa**.

![As opções de agendamento baseadas em tempo para enviar uma campanha em um horário designado.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campanhas de fuso horário local

É possível enviar a mensagem nos fusos horários locais dos usuários para que os membros do seu público internacional não recebam uma notificação em horários inconvenientes. As campanhas de fuso horário local precisam ser programadas com 24 horas de antecedência para garantir que os usuários elegíveis de todos os fusos horários possam recebê-las. Confira as [Perguntas frequentes sobre campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/) para entender como funcionam as campanhas de fuso horário local e as regras de entrega associadas.

Os segmentos direcionados com campanhas de fuso horário local devem incluir, no mínimo, um período de dois dias para incorporar usuários de todos os fusos horários. Por exemplo, se a sua campanha estiver programada para ser enviada à noite, mas tiver apenas um período de 1 dia, alguns usuários podem ter saído do segmento quando o fuso horário deles for atingido. Exemplos de filtros que criam um período de 2 dias são "último uso há mais de 1 dia" e "último uso há menos de 3 dias", ou "primeira compra há mais de 7 dias" e "primeira compra há menos de 9 dias".

### Casos de uso

Os cronogramas designados são mais adequados para mensagens programadas com antecedência e campanhas recorrentes, como integração e retenção, que são executadas regularmente para todos os usuários qualificados.

## Opção 3: Intelligent Timing

O [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) permite que você entregue uma campanha a cada usuário em um horário diferente. A Braze calcula o horário de cada indivíduo com base no momento em que esse usuário normalmente interage com seu app e suas notificações. Você também pode especificar que as campanhas de Intelligent Timing sejam enviadas apenas durante uma determinada parte do dia. Por exemplo, se estiver notificando os usuários sobre uma promoção que termina à meia-noite, talvez queira que as mensagens sejam enviadas até as 22h, no máximo.

![As opções de agendamento com base no tempo para usar o Intelligent Timing para enviar uma campanha no horário mais popular de uso do app entre todos os usuários.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Regras de entrega

Como o horário ideal de um usuário pode ser qualquer horário ao longo de 24 horas, todas as campanhas de Intelligent Timing devem ser agendadas com 24 horas de antecedência. Além disso, de forma semelhante às campanhas de horários designados, as mensagens com um período de 1 dia perderão os usuários que saírem do segmento antes que o horário ideal em seu fuso horário seja alcançado. Os segmentos das campanhas de Intelligent Timing devem incorporar, no mínimo, um período de três dias para levar isso em conta.

Se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal, é possível escolher um método de backup para enviar durante o horário mais popular de uso do app entre todos os usuários ou definir um horário de fallback personalizado. 

### Casos de uso

As campanhas de Intelligent Timing funcionam melhor para mensagens únicas e recorrentes em que há alguma flexibilidade com relação ao horário de entrega, ou seja, quando não são adequadas para notícias de última hora ou anúncios cronometrados.