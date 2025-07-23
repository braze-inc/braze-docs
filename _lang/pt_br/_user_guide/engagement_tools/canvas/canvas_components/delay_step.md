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

As postergações podem fazer com que sua tela pareça mais limpa. Você também pode usar esse componente para postergar uma etapa diferente até uma data exata, até um dia específico ou até um dia específico da semana. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

## Criar uma postergação

Para criar uma postergação, adicione uma etapa do Canva. Arraste e solte o componente Postergação da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Postergação**.

Há vários detalhes a serem considerados ao criar uma postergação em sua jornada no canva.

- O limite de postergação é de 30 dias.
- Um componente de postergação só pode se conectar a uma etapa seguinte.

### Postergações personalizadas

{% alert important %}
As postergações personalizadas e estendidas estão em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

Selecione a opção **Personalizar postergação** para configurar uma postergação personalizada para seus usuários. Você pode usar isso com uma [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para selecionar a variável de contexto para a postergação.

O Braze encerrará um usuário na etapa se:

- A variável de contexto não retorna a nenhum valor.
- Uma chamada de Connected Content incorporada falha.
- Os tipos de variáveis de contexto não correspondem.

Digamos que queremos lembrar nossos clientes de comprar pasta de dente daqui a 30 dias. Usando uma combinação de uma etapa de Contexto e uma etapa de Postergação, podemos selecionar essa variável de contexto para postergar. Nesse caso, nossa etapa Context teria os seguintes campos:

- **Nome da variável de contexto:** product_reminder_interval
- **Tipo de dados:** Horário
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![O "product_reminder_interval" e seu valor.][2]

Em seguida, como queremos lembrar nossos clientes daqui a 30 dias, selecionaremos **Até um dia específico** como a opção de postergação e selecionaremos **Personalizar postergação** para usar as informações da etapa Contexto. Isso significa que nossos usuários sofrerão postergação até a variável de contexto selecionada.

![Exemplo de uso de variáveis de contexto com uma etapa de Atraso para postergar usuários com base no "product_reminder_interval".][3]

#### Postergações prolongadas

Agora você pode estender as etapas de postergação por até dois anos. Por exemplo, se você estiver integrando novos usuários ao seu app, poderá adicionar uma postergação estendida de dois meses antes de enviar uma etapa de Mensagem para incentivar os usuários que não iniciaram uma sessão.

### Opções de postergação

Você pode escolher o tipo de postergação antes da próxima mensagem em seu Canva. É possível definir uma postergação para que seus usuários durem até depois de um período de tempo designado, ou postergar seus usuários até uma data e hora específicas.

{% tabs %}
  {% tab Após uma duração %}

  A opção **Após uma duração** permite a postergação de usuários por um número definido de segundos, minutos, horas, dias ou semanas, e em um horário específico. Por exemplo, é possível fazer a postergação de usuários por quatro horas ou por um dia.
  
  Note a diferença entre a forma como os "dias" e os "dias corridos" são calculados.
  
    - A "day" is 24 hours and calculated from the time the user enters the Delay step. 
    - A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

  Também é possível selecionar **Em um horário específico** para especificar quando os usuários avançarão no Canva. Essa opção leva em conta a hora em que o usuário entrou na etapa de postergação. Se esse tempo estiver além do tempo configurado nas configurações, acrescentaremos mais horas à postergação. Por exemplo, digamos que hoje seja 11 de dezembro e que nossa etapa de postergação esteja definida como **Após uma semana** às 8 horas UTC. Se um usuário entrar na etapa de postergação em 4 de dezembro, ele será liberado da etapa de postergação para continuar sua jornada hoje se tiver entrado originalmente na etapa de postergação em um horário anterior às 8h UTC. Se entrar na etapa de postergação após esse horário, o usuário será postergado até o dia seguinte (a próxima ocorrência desse horário). 

  {% endtab %}
  {% tab Até uma data específica %}

  A opção **Até uma data específica** permite manter os usuários na etapa até uma data e hora específicas.

  {% alert important %}
  Se a data e a hora selecionadas já tiverem passado no momento em que os usuários prosseguirem para a etapa do canva, eles sairão do canva. Pode haver um máximo de 31 dias entre o início do Canva e as datas escolhidas para as etapas de "Aguardar até a data exata".
  {% endalert %}
  {% endtab %}
  {% tab Até um dia específico da semana %}

  A opção **Até um dia específico da semana** permite manter os usuários na etapa até um dia específico da semana, em um horário específico. Por exemplo, é possível fazer a postergação dos usuários até que a próxima quinta-feira chegue às 16 horas no fuso horário da empresa. 

  Para configurar isso com êxito, também será necessário selecionar o que acontecerá se o usuário entrar no Canva no dia da semana selecionado (por exemplo, quinta-feira), mas após o horário especificado. Você pode optar por adiantar o usuário no mesmo dia ou retê-lo até a semana seguinte.
  {% endtab %}
{% endtabs %}

## Uso de etapas de postergação

Digamos que seja 10 de junho. Em 11 de junho, você gostaria que os usuários entrassem no canva e recebessem uma mensagem sobre uma promoção futura. Em seguida, mantenha os usuários no canva até 17 de junho, às 15 horas, fuso local. Às 15 horas, fuso local, do dia 17 de junho, você deseja enviar aos usuários uma mensagem de lembrete sobre a promoção.

A sequência de etapas do Canva pode ser parecida com a seguinte:

1. Comece adicionando uma etapa de Mensagens que é enviada imediatamente após os usuários entrarem no Canva em 11 de junho.
2. Crie uma etapa de postergação que mantenha os usuários até as 13 horas, fuso local, do dia 17 de junho.
3. Vincule a etapa de postergação a outra etapa de mensagem que envia sua mensagem imediatamente.

### Componentes de postergação no final de uma tela {#delay-as-last-step}

Se você adicionar um componente Delay ao Canvas, mas não houver mais etapas após o componente de postergação, qualquer usuário que chegar à última etapa será automaticamente avançado para fora do Canvas. Isso é verdade mesmo que o tempo da etapa de postergação ainda não tenha sido atingido. Isso significa que, para os usuários que já atingiram a etapa de postergação, eles não receberão nenhuma mensagem que você adicionar após a etapa de postergação. No entanto, se um usuário não tiver atingido a etapa de postergação e uma mensagem for adicionada, ele receberá essa mensagem.

## Análise de dados de postergação

As postergações têm três estatísticas disponíveis na exibição de análise de dados de um Canva ativo ou previamente ativo.

| Métrico | Descrição |
|---|---|
| `Entered` | Reflete o número de vezes que a etapa foi inserida. Se o seu Canva tiver reelegibilidade e um usuário inserir uma etapa do canva duas vezes, duas entradas serão registradas. |
| `Proceeded to Next Step` | Reflete o número de entradas que prosseguiram para a próxima etapa do canva. |
| `Exited Canvas` | Reflete o número de entradas que saíram do Canva e não prosseguiram para a próxima etapa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As séries temporais para essas análises de dados estão disponíveis na exibição expandida do componente.

[1]: {% image_buster /assets/img/canvas_delay.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}
