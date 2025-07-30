---
nav_title: "Objeto de agendamento"
article_title: Objeto de agendamento da API
page_order: 12
page_type: reference
description: "Este artigo de referência lista e explica os diferentes objetos de agendamento usados na Braze."

---

# Objeto de agendamento

> Os parâmetros para os endpoints de criação de campanha e canva espelham os do endpoint de envio e adicionam o parâmetro `schedule`, que permite especificar quando você deseja que seus usuários-alvo recebam sua mensagem. Se você incluir apenas o parâmetro `time` no objeto `schedule`, todos os seus usuários serão notificados naquele momento.

Se você definir `in_local_time` para ser `true`, receberá uma resposta de erro se o parâmetro de tempo tiver passado em todos os fusos horários. Se você definir `at_optimal_time` como verdadeiro, seus usuários receberão a mensagem na data designada no momento ideal (independentemente do horário que você fornecer). Ao usar o envio no horário local ou no horário ideal, não forneça designadores de fuso horário no valor do parâmetro de tempo (por exemplo, use `"2015-02-20T13:14:47"` em vez de `"2015-02-20T13:14:47-05:00"`).

A resposta fornecerá a você um `schedule_id` que você deve salvar caso precise cancelar ou atualizar a mensagem que você agendou:

## Corpo do objeto

Insira este objeto conforme necessário para agendar suas mensagens.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## Resposta de ID de agendamento

Você receberá um `schedule_id` pela mensagem agendada que você criou.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

Se você usar a API para chamadas de servidor para servidor, pode ser necessário colocar na lista de permissões o URL apropriado da API se ela estiver atrás de um firewall.

As respostas do endpoint de agendamento de mensagens incluirão a `dispatch_id` da mensagem para referência ao despacho da mensagem. O `dispatch_id` é o ID do despacho da mensagem (ID único para cada 'transmissão' enviada pela Braze).

