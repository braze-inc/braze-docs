---
nav_title: Atraso 
article_title: Atraso 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda como adicionar um atraso ao Canvas sem a necessidade de adicionar uma mensagem associada."
tool: Canvas

---

# Atraso

> Os componentes de atraso permitem adicionar um atraso autônomo a um Canvas. Você pode adicionar um atraso ao seu Canvas sem precisar adicionar uma mensagem associada. 

Os atrasos podem fazer com que seu Canvas pareça mais limpo. Você também pode usar esse componente para atrasar uma etapa diferente até uma data exata, até um dia específico ou até um dia específico da semana. <br> \![Uma etapa de Atraso com um atraso de 1 dia como a primeira etapa de um Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Criação de um atraso

Para criar um atraso, adicione uma etapa ao seu Canvas. Arraste e solte o componente Delay (Atraso) da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Delay (Atraso**).

Há vários detalhes a serem considerados ao criar um atraso em sua jornada no Canvas.

- O limite de atraso é de 30 dias.
- Um componente Delay só pode se conectar a uma etapa seguinte.

#### Atrasos prolongados

Agora você pode estender as etapas do Delay em até dois anos. Por exemplo, se você estiver integrando novos usuários ao seu aplicativo, poderá adicionar um atraso estendido de dois meses antes de enviar uma etapa de mensagem para incentivar os usuários que não iniciaram uma sessão.

## Tipos de atraso de tempo

Você pode escolher o tipo de atraso antes da próxima mensagem em seu Canvas. Você pode definir um atraso para que os usuários durem até depois de um período de tempo designado ou atrasar os usuários até uma data e hora específicas.

{% tabs %}
{% tab Duration %}

A seleção de **Duration** permite atrasar os usuários por um número definido de segundos, minutos, horas, dias ou semanas, e em um horário específico. Por exemplo, você pode atrasar os usuários por quatro horas ou por um dia.
  
Observe a diferença entre como os "dias" e os "dias corridos" são calculados.
  
- Um "dia" corresponde a 24 horas e é calculado a partir do momento em que o usuário insere a etapa de atraso. 
- Um "dia do calendário" define o tempo de espera até o próximo horário especificado, que pode ser inferior a 24 horas. Você pode optar por atrasar no horário da empresa ou no horário local de um usuário. Se não for especificado um horário, o usuário será adiado até a meia-noite do dia seguinte no horário da empresa.

Você também pode selecionar **At a specific time (Em um horário específico** ) para especificar quando os usuários avançarão no Canvas. Essa opção leva em conta a hora em que o usuário inseriu a etapa Delay (Atraso). Se esse tempo estiver além do tempo configurado nas configurações, acrescentaremos mais horas ao atraso. 

Por exemplo, digamos que hoje seja 11 de dezembro e que nossa etapa de atraso esteja definida como **Duration** of one week ( **Duração** de uma semana) às 8 horas UTC. Se um usuário entrar na etapa de Atraso em 4 de dezembro, ele será liberado da etapa de Atraso para continuar sua jornada hoje se tiver entrado originalmente na etapa de Atraso em um horário anterior às 8h UTC. Se entrarem na etapa de atraso após esse horário, o usuário será atrasado até o dia seguinte (a próxima ocorrência desse horário). 

{% endtab %}
{% tab Calendar date %}

A seleção da **data do calendário** permite manter os usuários na etapa até uma data e hora específicas.

#### Considerações

##### Os usuários não receberão etapas ou mensagens desatualizadas

Se a data e a hora selecionadas já tiverem passado no momento em que os usuários prosseguirem para a etapa Delay (Atraso), eles sairão do Canvas. Pode haver até 31 dias entre o início do Canvas e as datas escolhidas para as etapas de "esperar até um dia exato".

{% alert important %}
Se você estiver participando do [acesso antecipado do Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), poderá definir atrasos de até 2 anos.
{% endalert %}

Por exemplo, os usuários não receberão etapas ou mensagens nesses cenários:

- Uma mensagem está programada para ser enviada no dia 3 de maio às 21 horas, mas a etapa de atraso expira no dia 3 de maio às 9 horas. 
- Uma etapa do Canvas atrasa até um horário específico no fuso horário local do usuário, mas os usuários não têm um fuso horário definido em seu perfil de usuário. Em seguida, o atraso é padronizado para o fuso horário da empresa para esses usuários, que já ultrapassou o horário especificado. 
  
##### Os usuários sairão se uma etapa de Atraso subsequente estiver dentro da linha do tempo de uma etapa de Atraso anterior

Se o Canvas tiver duas etapas de Atraso, mas a primeira etapa de Atraso for maior que a segunda etapa de Atraso, os usuários também sairão do Canvas. 

Por exemplo, digamos que um Canvas tenha as seguintes etapas:
- Etapa 1: Etapa da mensagem
- Etapa 2: Atrasar a etapa até 13 de dezembro às 22 horas
- Etapa 3: Etapa da mensagem
- Etapa 4: Atrasar a etapa até 13 de dezembro, às 19 horas
- Etapa 5: Etapa da mensagem
  
Os usuários que entrarem na Etapa 4 sairão do Canvas antes de receberem a Etapa 5, pois o atraso da Etapa 4 faz parte do cronograma da Etapa 2.

{% endtab %}
{% tab Day of the week %}

A seleção de **Dia da semana** permite manter os usuários na etapa até um dia específico da semana, em um horário específico. Por exemplo, você pode atrasar os usuários até a próxima quinta-feira, às 16h, no fuso horário da empresa. 

Para configurar isso com êxito, você também precisará selecionar o que acontecerá se o usuário entrar no Canvas no dia da semana selecionado (por exemplo, quinta-feira), mas após o horário especificado. Você pode optar por adiantar o usuário no mesmo dia ou retê-lo até a semana seguinte.
{% endtab %}
{% endtabs %}

## Usando etapas de atraso

Digamos que seja 10 de junho. Em 11 de junho, você gostaria que os usuários entrassem no Canvas e recebessem uma mensagem sobre uma promoção futura. Em seguida, você deseja manter os usuários no Canvas até 17 de junho, às 15h, horário local. Às 15 horas, horário local, do dia 17 de junho, você deseja enviar aos usuários uma mensagem de lembrete sobre a promoção.

A sequência de etapas do Canvas pode ser parecida com a seguinte:

1. Comece adicionando uma etapa de Mensagem que é enviada imediatamente após os usuários entrarem no Canvas em 11 de junho.
2. Crie uma etapa de Atraso que mantenha os usuários até as 13 horas, horário local, do dia 17 de junho.
3. Vincule a etapa Delay a outra etapa Message que envia sua mensagem imediatamente.

### Componentes de atraso no final de um Canvas {#delay-as-last-step}

Se você adicionar um componente Delay (Atraso) ao seu Canvas e não houver etapas subsequentes, qualquer usuário que chegar à última etapa será automaticamente avançado para fora do Canvas. Isso é verdade mesmo que o tempo da etapa de atraso ainda não tenha sido atingido. Isso significa que os usuários que já atingiram a etapa de Atraso não receberão nenhuma mensagem que você adicionar após essa etapa. No entanto, se um usuário não tiver atingido a etapa de atraso e uma mensagem for adicionada, ele receberá essa mensagem.

### Atrasos personalizados

{% alert important %}
Atrasos personalizados e atrasos estendidos estão em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

Selecione o botão de alternância **Personalizar atraso** para configurar um atraso personalizado para seus usuários. Você pode usar isso com uma [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para selecionar a variável de contexto para atrasar. Isso substituirá a hora do dia definida no atributo ou na propriedade selecionada. Isso é útil quando se aplica uma compensação em dias ou semanas e se deseja que os usuários avancem em um momento específico. O fuso horário vem do atributo ou da propriedade, ou usa o fallback se não houver nenhum disponível. 

#### Comportamento do fuso horário para "em um horário específico"

Ao configurar atrasos personalizados com a opção de **horário específico**, o comportamento do fuso horário depende do tipo de dados do atributo ou da variável de contexto:

- **Tipo de dados String com fuso horário:** Se o atributo ou a variável de contexto for um tipo de dados de cadeia de caracteres que inclui informações de fuso horário, ele estará em conformidade com o fuso horário especificado na cadeia. Por exemplo, o site `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de dados String sem fuso horário:** Se o atributo ou a variável de contexto for um tipo de dados de cadeia de caracteres sem informações de fuso horário, ele estará em conformidade com o fuso horário de fallback. Por exemplo, o site `2025-06-10` usa o fuso horário de fallback.
- **Tipo de dados de tempo:** Se o atributo ou a variável de contexto for um tipo de dados de tempo, ele estará em conformidade com o UTC. Isso ocorre porque o tipo de dados de hora é sempre convertido para UTC quando salvo no banco de dados, portanto, "at specific time" sempre fará referência a UTC quando a variável for definida como tipo de dados de hora. Por exemplo, o site `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
É possível que um atributo personalizado ou uma variável de contexto não tenha uma hora específica nem um fuso horário se for um tipo de dados de cadeia de caracteres. Se for um tipo de dados de tempo, você precisará especificar a hora e o fuso horário. No entanto, se o atributo personalizado ou a variável de contexto for uma cadeia de caracteres "irrelevante" (como "product_name"), ), o usuário sairá do Canvas.
{% endalert %}

#### Caso de uso

Digamos que você queira lembrar seus clientes de comprar pasta de dente daqui a 30 dias. Usando uma combinação de uma etapa de Contexto e uma etapa de Atraso, você pode selecionar essa variável de contexto para atrasar. Nesse caso, sua etapa de Contexto teria os seguintes campos:

- **Nome da variável de contexto:** product_reminder_interval
- **Tipo de dados:** Tempo
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

\![O "product_reminder_interval" e seu valor.]({% image_buster /assets/img/context_step1.png %})

Em seguida, como você deseja lembrar seus clientes daqui a 30 dias, selecione **Until a specific day (Até um dia específico** ) como a opção de atraso e selecione **Personalize delay (Personalizar atraso** ) para usar as informações da etapa Contexto. Isso significa que seus usuários serão atrasados até a variável de contexto selecionada.

## Análise de atrasos

Os componentes de atraso têm as seguintes métricas disponíveis na exibição de análise de um Canvas ativo ou previamente ativo.

| Métrico | Descrição |
|---|---|
| _Entrou_ | Reflete o número de vezes que a etapa foi inserida. Se o seu Canvas tiver reelegibilidade e um usuário inserir uma etapa de Atraso duas vezes, duas entradas serão registradas. |
| _Prosseguiu para a próxima etapa_ | Reflete o número de entradas que prosseguiram para a próxima etapa do Canvas. |
| _Tela de saída_ | Reflete o número de entradas que saíram do Canvas e não prosseguiram para a próxima etapa. |
| _Falha na personalização_ | Reflete o número de vezes que uma mensagem ou conteúdo personalizado destinado a um usuário não pôde ser entregue devido ao seguinte:<br> {::nomarkdown}<ul><li>O valor do atraso está no passado</li><li>O valor do atraso é de mais de 2 anos no futuro</li><li><b>Depois que um</b> valor <b>de duração</b> não for um número</li><li><b>Até que um</b> valor <b>de dia específico</b> não seja uma data ou uma cadeia de caracteres formatada por data</li></ul>{:/} <br>Consulte [Erros de falha na personalização](#personaliztion-failed-errors) para obter mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As séries temporais para essas análises estão disponíveis na visualização expandida do componente.

## Solução de problemas

### Erros de falha na personalização

Se os usuários não estiverem acionando um atraso personalizado, pode ser porque a etapa de contexto que você definiu para qualificá-los para a etapa de atraso não está funcionando como esperado. Quando uma [variável de contexto for inválida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), o usuário continuará no Canvas sem ter seu contexto definido pela etapa Context (Contexto). Isso pode fazer com que eles não se qualifiquem para as etapas posteriores do Canvas, como atrasos personalizados.

