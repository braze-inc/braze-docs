---
nav_title: Postergação 
article_title: Postergação 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda como adicionar uma postergação ao seu Canva sem a necessidade de adicionar uma mensagem associada."
tool: Canvas

---

# Postergação

> Os componentes de postergação permitem adicionar uma postergação autônoma a um Canva. Você pode adicionar uma postergação ao seu Canva sem precisar adicionar uma mensagem associada. 

As postergações podem fazer com que sua tela pareça mais limpa. Você também pode usar esse componente para postergar uma etapa diferente até uma data exata, até um dia específico ou até um dia específico da semana. <br> ![Uma etapa de atraso com uma postergação de 1 dia como a primeira etapa de um Canva.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Criação de uma postergação

Para criar uma postergação, adicione uma etapa do Canva. Arraste e solte o componente Postergação da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Postergação**.

Há vários detalhes a serem considerados ao criar uma postergação em sua jornada no canva.

- O limite de postergação é de 30 dias.
- Um componente de postergação só pode se conectar a uma etapa seguinte.

### Postergações personalizadas

{% alert important %}
As postergações personalizadas e estendidas estão em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

Selecione a opção **Personalizar postergação** para configurar uma postergação personalizada para seus usuários. Você pode usar isso com uma [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para selecionar a variável de contexto para a postergação.

Digamos que você queira lembrar seus clientes de comprar pasta de dente daqui a 30 dias. Usando uma combinação de uma etapa de Contexto e uma etapa de Postergação, você pode selecionar essa variável de contexto para atrasar. Nesse caso, sua etapa Context teria os seguintes campos:

- **Nome da variável de contexto:** product_reminder_interval
- **Tipo de dados:** Horário
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![O "product_reminder_interval" e seu valor.]({% image_buster /assets/img/context_step1.png %})

Em seguida, como deseja lembrar seus clientes daqui a 30 dias, selecione **Until a specific day (Até um dia específico** ) como opção de postergação e selecione **Personalize delay (Personalizar postergação** ) para usar as informações da etapa Context (Contexto). Isso significa que seus usuários terão uma postergação até a variável de contexto selecionada.

![Exemplo de uso de variáveis de contexto com uma etapa de postergação para atrasar os usuários com base no "product_reminder_interval".]({% image_buster /assets/img/context_step2.png %})

#### Postergações prolongadas

Agora você pode estender as etapas de postergação por até dois anos. Por exemplo, se você estiver integrando novos usuários ao seu app, poderá adicionar uma postergação estendida de dois meses antes de enviar uma etapa de Mensagem para incentivar os usuários que não iniciaram uma sessão.

### Opções de postergação

Você pode escolher o tipo de postergação antes da próxima mensagem em seu Canva. É possível definir uma postergação para que seus usuários durem até depois de um período de tempo designado, ou postergar seus usuários até uma data e hora específicas.

{% tabs %}
{% tab Após uma duração %}

A opção **Após uma duração** permite a postergação de usuários por um número definido de segundos, minutos, horas, dias ou semanas, e em um horário específico. Por exemplo, é possível fazer a postergação de usuários por quatro horas ou por um dia.
  
Note a diferença entre a forma como os "dias" e os "dias corridos" são calculados.
  
- Um "dia" tem 24 horas e é calculado a partir do momento em que o usuário entra na etapa de postergação. 
- Um "dia do calendário" define um dia como 24 horas após um horário específico. Quando um dia do calendário é escolhido e a hora é especificada, é possível optar pela postergação no horário da empresa ou no fuso local do usuário. Se uma hora não for especificada, o usuário terá uma postergação até a meia-noite do dia seguinte no horário da empresa.

Também é possível selecionar **Em um horário específico** para especificar quando os usuários avançarão no Canva. Essa opção leva em conta a hora em que o usuário entrou na etapa de postergação. Se esse tempo estiver além do tempo configurado nas configurações, acrescentaremos mais horas à postergação. Por exemplo, digamos que hoje seja 11 de dezembro e que nossa etapa de postergação esteja definida como **Após uma semana** às 8 horas UTC. Se um usuário entrar na etapa de postergação em 4 de dezembro, ele será liberado da etapa de postergação para continuar sua jornada hoje se tiver entrado originalmente na etapa de postergação em um horário anterior às 8h UTC. Se entrar na etapa de postergação após esse horário, o usuário será postergado até o dia seguinte (a próxima ocorrência desse horário). 

{% endtab %}
{% tab Até uma data específica %}

A opção **Até uma data específica** permite manter os usuários na etapa até uma data e hora específicas.

#### Considerações

##### Os usuários não receberão etapas ou mensagens desatualizadas

Se a data e a hora selecionadas já tiverem passado no momento em que os usuários prosseguirem para a etapa do canva, eles sairão do canva. Pode haver até 31 dias entre o início do Canva e as datas escolhidas para as etapas de "Aguardar até a data exata". 

{% alert important %}
Se estiver participando do [acesso antecipado da etapa Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), poderá definir postergações de até 2 anos.
{% endalert %}

Por exemplo, os usuários não receberão etapas ou mensagens nesses cenários:
- Uma mensagem está programada para ser enviada no dia 3 de maio às 21 horas, mas a etapa de postergação expira no dia 3 de maio às 9 horas. 
- Uma etapa do Canva posterga até um horário específico no fuso local do usuário, mas os usuários não têm um fuso horário definido em seu perfil de usuário. A postergação, então, tem como padrão o fuso horário da empresa para esses usuários, que já ultrapassou a hora especificada. 
  
##### Os usuários sairão se uma etapa de postergação subsequente estiver dentro da linha do tempo de uma etapa de postergação anterior

Se o Canva tiver duas etapas de postergação usando "Wait until Exact Date" (Aguardar até a data exata), mas a primeira etapa de postergação for maior que a segunda etapa de postergação, os usuários também sairão do Canva. 

Por exemplo, digamos que um Canvas tenha as seguintes etapas:
- Etapa 1: Etapa da mensagem
- Etapa 2: Etapa de postergação até 13 de dezembro, às 22 horas
- Etapa 3: Etapa da mensagem
- Etapa 4: Etapa de postergação até 13 de dezembro, às 19 horas
- Etapa 5: Etapa da mensagem
  
Os usuários que entrarem na Etapa 4 sairão do Canva antes de receberem a Etapa 5 porque a postergação da Etapa 4 faz parte do período da Etapa 2.

{% endtab %}
{% tab Até um dia específico da semana %}

A opção **Até um dia específico da semana** permite manter os usuários na etapa até um dia específico da semana, em um horário específico. Por exemplo, é possível fazer a postergação dos usuários até que a próxima quinta-feira chegue às 16 horas no fuso horário da empresa. 

Para configurar isso com êxito, também será necessário selecionar o que acontecerá se o usuário entrar no Canva no dia da semana selecionado (por exemplo, quinta-feira), mas após o horário especificado. Você pode optar por adiantar o usuário no mesmo dia ou retê-lo até a semana seguinte.
{% endtab %}
{% endtabs %}

## Uso de etapas de postergação

Digamos que seja 10 de junho. Em 11 de junho, você gostaria que os usuários entrassem no canva e recebessem uma mensagem sobre uma promoção futura. Em seguida, mantenha os usuários no canva até 17 de junho, às 15 horas, fuso local. Às 15 horas, fuso local, do dia 17 de junho, você deseja enviar aos usuários uma mensagem de lembrete sobre a promoção.

A sequência de etapas do Canva pode ser semelhante à seguinte:

1. Comece adicionando uma etapa de Mensagens que é enviada imediatamente após os usuários entrarem no Canva em 11 de junho.
2. Crie uma etapa de postergação que mantenha os usuários até as 13 horas, fuso local, do dia 17 de junho.
3. Vincule a etapa de postergação a outra etapa de mensagem que envia sua mensagem imediatamente.

### Componentes de postergação no final de uma tela {#delay-as-last-step}

Se adicionar um componente de postergação ao seu Canvas e não houver etapas subsequentes, qualquer usuário que chegar à última etapa será automaticamente avançado para fora do Canvas. Isso é verdade mesmo que o tempo da etapa de postergação ainda não tenha sido atingido. Isso significa que os usuários que já atingiram a etapa de postergação não receberão nenhuma mensagem que você adicionar após essa etapa. No entanto, se um usuário não tiver atingido a etapa de postergação e uma mensagem for adicionada, ele receberá essa mensagem.

## Análise de dados de postergação

Os componentes de postergação têm as seguintes métricas disponíveis na exibição de análise de dados de um Canva ativo ou previamente ativo.

| Métrico | Descrição |
|---|---|
| _Entraram_ | Reflete o número de vezes que a etapa foi inserida. Se o seu Canva tiver reelegibilidade e um usuário inserir uma etapa do canva duas vezes, duas entradas serão registradas. |
| _Avançaram para a etapa seguinte_ | Reflete o número de entradas que prosseguiram para a próxima etapa do canva. |
| _Saíram do canva_ | Reflete o número de entradas que saíram do Canva e não prosseguiram para a próxima etapa. |
| _Falha na personalização_ | Reflete o número de vezes que uma mensagem ou conteúdo personalizado destinado a um usuário não pôde ser entregue devido ao seguinte:<br> {::nomarkdown}<ul><li>O valor da postergação está no passado</li><li>O valor da postergação é de mais de 2 anos no futuro</li><li><b>Depois que um</b> valor <b>de duração</b> não for um número</li><li><b>Até que</b> o valor <b>de um dia específico</b> não seja uma data ou uma string formatada com data</li></ul>{:/} <br>Consulte [Erros de falha na personalização](#personaliztion-failed-errors) para obter mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As séries temporais para essas análises de dados estão disponíveis na exibição expandida do componente.

## Solução de problemas

### Erros de falha na personalização

Se os usuários não estiverem disparando uma postergação personalizada, pode ser porque a etapa de Contexto que você definiu para qualificá-los para a etapa de Atraso não está funcionando como esperado. Quando uma [variável de contexto for inválida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), o usuário continuará no Canva sem ter seu contexto definido pela etapa do Context. Isso pode fazer com que eles não se qualifiquem para etapas posteriores do seu Canva, como postergações personalizadas.

