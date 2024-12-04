---
nav_title: Comportamento do filtro X em Y
permalink: /x-in-y-behavior/
---

# Comportamento atual do filtro X em Y

O comportamento desses filtros permanecerá praticamente o mesmo e será definido pelas seguintes características:

- Execute definindo dias corridos (terminando à meia-noite).
- "Dias" são definidos como em UTC.
- O dia UTC atual é definido como "0".

## Caso de uso

A seguinte campanha exibida é enviada às 21 horas do dia 16 de abril. A segmentação do público é "Made More than 2 Purchases in the past 3 days" (Fizeram mais de duas compras nos últimos três dias).

![Cronograma da campanha][1]

21h ET de 16 de abril é 1h UTC de 17 de abril.

17 de abril seria o dia "0", 16 de abril seria o dia "1", 15 de abril seria o dia "2" e 14 de abril seria o dia "3".

O histórico desde as 0h UTC de 14 de abril até a hora atual (1h UTC de 17 de abril).
Isso se acumularia em uma janela que inclui 73 horas do histórico do usuário.

## Em dias de calendário

Os dias do calendário são usados em mais capacidades do que apenas nos filtros "X em Y":

- Agendamento de envio de mensagens
- Limite de frequência
- "Filtros "X em Y

`Calendar Days` referem-se ao período de tempo em um dia numerado, começando às 12:00AM e terminando às 11:59PM do mesmo dia (12:00AM de 8 de junho até 11:59PM de 8 de junho seria um único dia do calendário).

### Limite de frequência

Os dias do calendário são usados quando você seleciona "days" (dias) ou "weeks" (semanas) em `Frequency Capping`.

- `Every 1 day` limitará o limite ao dia do calendário atual no fuso local do usuário (terminando à meia-noite no horário local).
- `Every 2 days` limitará o limite aos dias anteriores e atuais do calendário no fuso local do usuário (terminando à meia-noite do dia atual do calendário no fuso local).

### Empresa e fuso local

O dia do calendário atual no fuso horário da empresa conta como o dia `0`.

`Send in 1 Calendar days at 11:05 am company time` ou `send in 1 Calendar days at 11:05 am local time` adicionaria o dia `1` ao dia do calendário atual no fuso horário da empresa ou no fuso local, respectivamente, e agendaria a mensagem para as próximas 11h05, horário da empresa.

Se o fuso local ou da empresa for o horário do Pacífico e o usuário inserir a etapa do canva às 20h PT do dia 13/04, a Braze agendará essa etapa do canvas para as 11h05 PT do dia 14/04.

## Comportamento anterior do filtro X em Y

O Braze tem uma categoria específica de filtros de segmentação chamada "Filtros X em Y". Cada um desses filtros tem uma funcionalidade semelhante definida pelas seguintes características:

- Execute definindo dias corridos (terminando à meia-noite).
- "Dias" são definidos como em UTC.
- O dia UTC atual é definido como "1".



[1]:{% image_buster /assets/img/campaign-schuedule-example.png %}
