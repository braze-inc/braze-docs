---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artigo fornece uma visão geral do Intelligent Timing (anteriormente Entrega Inteligente) e como você pode aproveitar esse recurso em suas campanhas e canvas."

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use Intelligent Timing para entregar sua mensagem a cada usuário quando a Braze determinar que o usuário tem maior probabilidade de interagir (abrir ou clicar), referido como o horário de envio ideal. Isso facilita para você verificar se está enviando mensagens para seus usuários no horário de preferência deles, o que pode levar a um maior engajamento.

## 

Braze calcula o horário de envio ideal com base em uma análise estatística das interações passadas do seu usuário com seu app, e suas interações com cada canal de envio de mensagens. São usados os seguintes dados de interação: 

- Horários das sessões
- Aberturas diretas push
- Aberturas por influência do push
- Cliques no e-mail
- 

Por exemplo, Sam pode abrir seus e-mails pela manhã regularmente, mas ela abre seu app e interage com as notificações à noite. Isso significa que Sam receberia uma campanha de e-mail com Intelligent Timing pela manhã, enquanto ela receberia campanhas com notificações por push à noite, quando é mais provável que ela se envolva.



## Casos de uso

- Envie campanhas recorrentes que não são sensíveis ao tempo
- Automatize campanhas com usuários de vários fusos horários
- Ao enviar mensagens para seus usuários mais engajados (eles terão os dados de engajamento mais relevantes)

## Usando Intelligent Timing

Esta seção descreve como configurar o Intelligent Timing para suas campanhas e canvas.



###  

1. Crie uma campanha e componha sua mensagem.
2. 
3. Em **Opções de Agendamento Baseado no Tempo**, selecione **Intelligent Timing**.
4.    
5. 
6.  Esta é a hora em que a mensagem será enviada se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal.



#### 

 


  


1. 
2. 



 



#### Prévia dos horários de entrega

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia (somente campanhas).

1. Adicione segmentos ou filtros na etapa de Públicos-Alvo.
2. Na seção **Prévia dos horários de entrega para** (que aparece em ambos os passos de Públicos-alvos e Agendar Entrega), selecione seu canal.
3. Clique em **Atualizar Dados**.



###  

 

#### 

Lance sua campanha pelo menos 48 horas antes da data de envio programada. Isso é por causa das variações nos fusos horários. Braze calcula o horário ideal à meia-noite no horário de Samoa (UTC+13), um dos primeiros fusos horários do mundo. Um único dia abrange cerca de 48 horas em todo o mundo, o que significa que se você lançar uma campanha dentro desse intervalo de 48 horas, é possível que o horário ideal de um usuário já tenha passado em seu fuso horário, e a mensagem não será enviada.

{% alert important %}
Se uma campanha for lançada e o horário ideal de um usuário for menos de uma hora no passado, a mensagem é enviada imediatamente. Se o horário ideal for mais há de uma hora atrás, a mensagem não será enviada.
{% endalert %}

#### 

Se você está direcionando um público que realizou uma ação em um determinado período, permita pelo menos um período de 3 dias em seus filtros de segmento. 



Isso também ocorre por causa dos fusos horários — selecionar um período de menos de 3 dias pode fazer com que alguns usuários saiam do segmento antes que seu horário ideal de envio seja alcançado.

 

#### 



  



###  

  

 



1. Ao configurar o Intelligent Timing, selecione **Apenas enviar mensagens dentro de horários específicos**.
2. Insira o horário de início e término do período de entrega.



###  







###  Prévia dos horários de entrega



1. Adicione segmentos ou filtros na etapa de Públicos-Alvo.
2. Na seção **Prévia dos horários de entrega para** (que aparece em ambos os passos de Públicos-alvos e Agendar Entrega), selecione seu canal.
3. 



Sempre que você alterar qualquer configuração sobre Intelligent Timing ou seu público de campanha, atualize os dados novamente para visualizar um gráfico atualizado.

O gráfico mostra os usuários que tinham dados suficientes para calcular um tempo ótimo em azul e os usuários que usarão o tempo fallback em vermelho. Use os filtros de cálculo para ajustar a {prévia} para uma visão mais granular de cada grupo de usuários.
{% endtab %}



 


###  



  Etapas de mensagens que têm como alvo vários canais podem enviar ou tentar enviar mensagens em horários diferentes para canais diferentes. Quando a primeira mensagem em uma etapa de Mensagem tenta enviar, todos os usuários são avançados automaticamente.

###  



###  





####  

 

- **Dias:** 1 dia são 24 horas, calculadas a partir do momento em que o usuário entra na etapa de postergação.
- **Dias corridos:** 1 dia é o período desde que o usuário entra na etapa de postergação até a meia-noite em seu fuso horário. Isso significa que 1 dia de calendário pode ser tão curto quanto alguns minutos.

Ao usar Intelligent Timing, recomendamos que você use dias de calendário para seus atrasos em vez de dias de 24 horas. Isso ocorre porque, com os dias de calendário, a mensagem será enviada no último dia da postergação, no momento ideal. Com um dia de 24 horas, há uma chance de que o horário ideal do usuário seja antes de eles entrarem na etapa, o que significa que haverá um dia extra adicionado à sua postergação.

Por exemplo, digamos que o horário ideal de Luka é 14:00. Ele entra na etapa de postergação às 14h01 do dia 1º de março, e a postergação é definida para 2 dias.

- O dia 1 termina em 2 de março às 14h01
- O dia 2 termina em 3 de março às 14h01

No entanto, Intelligent Timing está programado para entregar às 14h, o que já passou. Então Luka não receberá a mensagem até o dia seguinte: 4 de março às 14:00.

![Gráfico que mostra a diferença entre dias e dias corridos onde se o horário ideal de um usuário é 14h, mas ele entra na etapa de postergação às 14h01 e a postergação é definida para 2 dias. Dias entrega a mensagem 3 dias depois porque o usuário entrou na etapa após o seu tempo ideal, enquanto dias de calendário entrega a mensagem 2 dias depois, no último dia da postergação.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}



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

## 

### 

#### 



#### 

  

### 

#### 



1.  
  - Horários das sessões
  - 
  - 
  - 
  - 
2. 

#### 

 

#### 

   

#### 

 

### Campanhas

#### 

   

#### 

   

#### 

  

 

### 

#### 



1.  
2.  

  

#### 

  

####  

 

#### 

  



#### 

  

Isso pode fazer com que os segmentos mudem e se alterem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. 

#### 

 

#### 



#### 

   



