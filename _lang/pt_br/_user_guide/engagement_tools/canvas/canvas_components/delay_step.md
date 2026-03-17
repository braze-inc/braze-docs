---
nav_title: Postergação 
article_title: Postergação 
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Este artigo de referência aborda como adicionar uma postergação ao seu Canva sem a necessidade de adicionar uma mensagem associada."
tool: Canvas

---

# Postergação

> Os componentes de postergação permitem adicionar uma postergação autônoma a um Canva. Você pode adicionar uma postergação ao seu Canva sem precisar adicionar uma mensagem associada. 

As postergações podem fazer com que sua tela pareça mais limpa. Você também pode usar esse componente para postergar uma etapa diferente até uma data exata, até um dia específico ou até um dia específico da semana. <br> ![Uma etapa de postergação com um atraso de 1 dia como a primeira etapa de um canva.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Criando uma postergação

Para criar uma postergação, adicione uma etapa do Canva. Arraste e solte o componente Postergação da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Postergação**.

Há vários detalhes a serem considerados ao criar uma postergação em sua jornada no canva.

- O limite de postergação é de 30 dias.
- Um componente de postergação só pode se conectar a uma etapa seguinte.

#### Postergações prolongadas

Agora você pode estender as etapas de postergação por até dois anos. Por exemplo, se você estiver integrando novos usuários ao seu app, poderá adicionar uma postergação estendida de dois meses antes de enviar uma etapa de Mensagem para incentivar os usuários que não iniciaram uma sessão.

## Tipos de postergação de tempo

Você pode escolher o tipo de postergação antes da próxima mensagem em seu Canva. É possível definir uma postergação para que seus usuários durem até depois de um período de tempo designado, ou postergar seus usuários até uma data e hora específicas.

{% tabs %}
{% tab Duration %}

Selecionar **Duração** permite que você atrase os usuários por um número definido de segundos, minutos, horas, dias ou semanas, e em um horário específico. Por exemplo, é possível fazer a postergação de usuários por quatro horas ou por um dia.
  
Note a diferença entre a forma como os "dias" e os "dias corridos" são calculados.
  
- Um "dia" tem 24 horas e é calculado a partir do momento em que o usuário entra na etapa de postergação. 
- Um "dia calendário" define o tempo a esperar até o próximo horário especificado, que pode ser inferior a 24 horas. Você pode escolher atrasar no horário da empresa ou no horário local do usuário. Se um horário não for especificado, o usuário será atrasado até a meia-noite do dia seguinte no horário da empresa.

Também é possível selecionar **Em um horário específico** para especificar quando os usuários avançarão no Canva. Essa opção leva em conta a hora em que o usuário entrou na etapa de postergação. Se esse tempo estiver além do tempo configurado nas configurações, acrescentaremos mais horas à postergação. 

Como exemplo, digamos que hoje é 11 de dezembro, e nossa etapa de postergação está definida para **Duracao** de uma semana às 8 da manhã UTC. Se um usuário entrar na etapa de postergação em 4 de dezembro, ele será liberado da etapa de postergação para continuar sua jornada hoje se tiver entrado originalmente na etapa de postergação em um horário anterior às 8h UTC. Se entrar na etapa de postergação após esse horário, o usuário será postergado até o dia seguinte (a próxima ocorrência desse horário). 

{% endtab %}
{% tab Calendar date %}

Selecionar **Data do calendário** permite que você mantenha os usuários na etapa até uma data e hora específicas.

#### Considerações

##### Os usuários não receberão etapas ou mensagens com data retroativa

Se a data e a hora selecionadas já tiverem passado no momento em que os usuários prosseguirem para a etapa do canva, eles sairão do canva. Pode haver até 31 dias entre o início do canva e as datas escolhidas para as etapas de "esperar até um dia exato".

{% alert important %}
Se você estiver participando do [acesso antecipado ao contexto do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), poderá definir atrasos de até 2 anos.
{% endalert %}

Por exemplo, os usuários não receberão etapas ou mensagens nesses cenários:

- Uma mensagem está programada para ser enviada no dia 3 de maio às 21h, mas a etapa de postergação expira no dia 3 de maio às 9h. 
- Uma etapa de canva atrasa até um horário específico no fuso horário local do usuário, mas os usuários não têm um fuso horário definido em seu perfil de usuário. O atraso então padrão para o fuso horário da empresa para esses usuários, que já passou do horário especificado. 
  
##### Os usuários sairão se uma etapa de postergação subsequente estiver dentro da linha do tempo de uma etapa de postergação anterior

Se o canva tiver duas etapas de postergação, mas a primeira etapa de postergação for mais longa que a segunda etapa de postergação, os usuários também sairão do canva. 

Por exemplo, digamos que um canva tenha estas etapas:
- Etapa 1: Etapa da mensagem
- Etapa 2: Posterga a etapa até 13 de dezembro às 22h
- Etapa 3: Etapa da mensagem
- Etapa 4: Posterga a etapa até 13 de dezembro às 19h
- Etapa 5: Etapa da mensagem
  
Os usuários que entrarem na Etapa 4 sairão do Canva antes de receber a Etapa 5, pois o atraso da Etapa 4 faz parte do período da Etapa 2.

{% endtab %}
{% tab Day of the week %}

Selecionar **Dia da semana** permite que você mantenha os usuários na etapa até um dia específico da semana, em um horário específico. Por exemplo, é possível fazer a postergação dos usuários até que a próxima quinta-feira chegue às 16 horas no fuso horário da empresa. 

Para configurar isso com êxito, também será necessário selecionar o que acontecerá se o usuário entrar no Canva no dia da semana selecionado (por exemplo, quinta-feira), mas após o horário especificado. Você pode optar por adiantar o usuário no mesmo dia ou retê-lo até a semana seguinte.
{% endtab %}
{% endtabs %}

## Uso de etapas de postergação

Digamos que seja 10 de junho. Em 11 de junho, você gostaria que os usuários entrassem no canva e recebessem uma mensagem sobre uma promoção futura. Em seguida, mantenha os usuários no canva até 17 de junho, às 15 horas, fuso local. Às 15 horas, fuso local, do dia 17 de junho, você deseja enviar aos usuários uma mensagem de lembrete sobre a promoção.

A sequência de etapas do Canva pode parecer a seguinte:

1. Comece adicionando uma etapa de Mensagens que é enviada imediatamente após os usuários entrarem no Canva em 11 de junho.
2. Crie uma etapa de postergação que mantenha os usuários até as 13 horas, fuso local, do dia 17 de junho.
3. Vincule a etapa de postergação a outra etapa de mensagem que envia sua mensagem imediatamente.

### Componentes de postergação no final de uma tela {#delay-as-last-step}

Se você adicionar um componente de postergação ao seu Canva e não houver etapas subsequentes, qualquer usuário que chegar à última etapa será automaticamente avançado para fora do Canva. Isso é verdade mesmo que o tempo da etapa de postergação ainda não tenha sido atingido. Isso significa que os usuários que já chegaram à etapa de postergação não receberão nenhuma mensagem que você adicionar após essa etapa. No entanto, se um usuário não tiver atingido a etapa de postergação e uma mensagem for adicionada, ele receberá essa mensagem.

### Postergações personalizadas

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Selecione a opção **Personalizar postergação** para configurar uma postergação personalizada para seus usuários. Você pode usar isso com uma [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para selecionar a variável de contexto para a postergação. Isso substituirá o horário do dia definido no atributo ou propriedade selecionada. Isso é útil ao aplicar um deslocamento em dias ou semanas, e você deseja que os usuários avancem em um horário específico. O fuso horário vem do atributo ou propriedade, ou usa o fallback se nenhum estiver disponível. 

#### Comportamento do fuso horário para "em horário específico"

Ao configurar atrasos personalizados com a opção **em horário específico**, o comportamento do fuso horário depende do tipo de dados do seu atributo ou variável de contexto:

- **Tipo de dado String com fuso horário:** Se o atributo ou variável de contexto for um tipo de dado string que inclui informações de fuso horário, ele se conforma ao fuso horário especificado na string. Por exemplo, `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de dado String sem fuso horário:** Se o atributo ou variável de contexto for um tipo de dado string sem informações de fuso horário, ele se conforma ao fuso horário de fallback. Por exemplo, `2025-06-10` usa o fuso horário de fallback.
- **Tipo de dado Hora:** Se o atributo ou variável de contexto for um tipo de dado hora, ele se conforma ao UTC. Isso ocorre porque o tipo de dado de tempo é sempre convertido para UTC quando salvo no banco de dados, então "em um horário específico" sempre fará referência ao UTC quando a variável estiver definida como tipo de dado de tempo. Por exemplo, `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
É possível que um atributo personalizado ou variável de contexto não tenha um horário específico nem um fuso horário se for um tipo de dado string. Se for um tipo de dado de tempo, você precisará especificar o horário e o fuso horário. No entanto, se o atributo personalizado ou variável de contexto for uma string "irrelevante" (como "product_name"),, o usuário sairá do canva.
{% endalert %}

#### Caso de uso

Vamos supor que você queira lembrar seus clientes de comprar pasta de dente em 30 dias a partir de agora. Usando uma combinação de uma etapa de Contexto e uma etapa de Postergação, você pode selecionar essa variável de contexto para atrasar. Neste caso, sua etapa de Contexto teria os seguintes campos:

- **Nome da variável de contexto:** product_reminder_interval
- **Tipo de dados:** Horário
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![O "product_reminder_interval" e seu valor.]({% image_buster /assets/img/context_step1.png %})

Em seguida, porque você quer lembrar seus clientes em 30 dias a partir de agora, você selecionará **Até um dia específico** como a opção de postergação e selecionará **Personalizar postergação** para usar as informações da sua etapa de Contexto. Isso significa que seus usuários serão atrasados até a variável de Contexto selecionada.

## Análise de dados de postergação

Os componentes de postergação têm as seguintes métricas disponíveis na visualização de análise de um canva ativo ou anteriormente ativo.

| Métrico | Descrição |
|---|---|
| _Entraram_ | Reflete o número de vezes que a etapa foi inserida. Se o seu Canva tiver reelegibilidade e um usuário inserir uma etapa do canva duas vezes, duas entradas serão registradas. |
| _Avançaram para a etapa seguinte_ | Reflete o número de entradas que prosseguiram para a próxima etapa do canva. |
| _Saíram do canva_ | Reflete o número de entradas que saíram do Canva e não prosseguiram para a próxima etapa. |
| _Falha na personalização_ | Reflete o número de vezes que uma mensagem ou conteúdo personalizado destinado a um usuário não pôde ser entregue devido ao seguinte:<br> {::nomarkdown}<ul><li>O valor da postergação está no passado</li><li>O valor da postergação está mais de 2 anos no futuro</li><li><b>Após uma duração</b> o valor não é um número</li><li><b>Até um dia específico</b> o valor não é uma data ou string formatada como data</li></ul>{:/} <br>Veja [Erros de falha de personalização](#personaliztion-failed-errors) para mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As séries temporais para essas análises de dados estão disponíveis na exibição expandida do componente.

## Solução de problemas

### Erros de falha de personalização

Se os usuários não estão acionando uma postergação personalizada, pode ser porque a etapa de Contexto que você definiu para qualificá-los para a etapa de postergação não está funcionando como você esperava. Quando uma [variável de contexto é inválida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), um usuário continuará através do seu canva sem ter seu contexto definido pela etapa de Contexto. Isso pode fazer com que eles não se qualifiquem para etapas posteriores no seu canva, como postergações personalizadas.

