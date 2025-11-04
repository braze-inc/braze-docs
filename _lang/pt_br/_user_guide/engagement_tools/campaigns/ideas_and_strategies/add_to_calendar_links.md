---
nav_title: Links para adicionar ao calendário
article_title: Links para adicionar ao calendário
page_order: 1
page_type: tutorial
description: "Este artigo descreve como incluir um link para adicionar ao calendário em suas campanhas de e-mail."
channel: email

---

# Links para adicionar ao calendário

> Ao promover um evento, venda ou compromisso, você pode ajudar os usuários a salvar facilmente o evento no calendário deles adicionando um link "adicionar ao calendário" aos seus e-mails.

Para fazer isso, elabore o rascunho de seu e-mail e determine onde deseja que seus links estejam. Em seguida, adicione duas opções: uma para o Google Calendar e outra para outros calendários (como o iCal ou o Outlook). Por exemplo, "Add to Google Calendar" e "Add to iCal or Outlook".

Caixa de diálogo Link ao adicionar um link no painel. A guia "Link Info" é selecionada e o texto é definido como "Add to Google Calendar".]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## Formato do URL

Adicione o seguinte URL aos seus links, substituindo os espaços reservados. A única diferença entre esses dois URLs é que o Google Calendar precisa de um parâmetro adicional: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Substitua o seguinte:

- `EVENT_SUBJECT`: Título do evento
- `EVENT_LOCATION`: Local do evento
- `START_TIME`: A hora de início do evento no formato ISO 8601 (AAAA-MM-DDTHH:MM:SSZ) como UTC
- `END_TIME`: O horário de término do evento no formato ISO 8601 (AAAA-MM-DDTHH:MM:SSZ) como UTC
- `EVENT_DESCRIPTION`: Descrição do evento

Substitua todos os espaços pelo código de escape HTML `%20`. Por exemplo, um assunto de "Meet Braze" seria "Meet%20Braze".

Aqui está um exemplo de um URL "Add to Google Calendar":

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Parâmetros adicionais

Os parâmetros a seguir são opcionais e podem ser usados para definir aspectos adicionais de um evento.

- **Nome do organizador:** `&organizer=name`
- **Anexe o URL relacionado ao evento:** `&attach=http://www.example.com/`
- **Duração:** `duration=30M` Como alternativa à hora de término do evento (dtend), especifique uma duração como 1H ou 30M
- **Hora do alarme do lembrete, em minutos:** `&reminder=15`
- **Evento durante todo o dia:** `&allday=1`
- **UID:** parâmetro opcional para codificar o identificador exclusivo do evento, permitindo que alguns aplicativos de calendário atualizem o evento ao longo do tempo. A string @ics.agical.io é automaticamente anexada ao valor.

Você também pode adicionar parâmetros adicionais para eventos recorrentes:
- **Eventos semanais:** `&recur=weekly`
- **Eventos mensais:** `&recur=monthly`
- **Fim da recorrência:** `&recuruntil=END_DATE`, em que `END_DATE` é a data e a hora em que a recorrência termina no formato ISO 8601 (AAAA-MM-DDTHH:MM:SSZ) como UTC

## Comportamento do link

Quando um usuário clica no link, os calendários transformam automaticamente os carimbos de data e hora UTC nos URLs para refletir o fuso horário do usuário definido em seu calendário.

Por exemplo, se você abrir o link de exemplo "Add to Google Calendar" (Adicionar ao Google Agenda) e sua agenda estiver definida como CST, o horário do evento será pré-preenchido de acordo com o horário das 15h UTC em CST (10h).

### Google Agenda

Quando clicado, o Google Agenda é aberto em uma nova guia ou janela com os detalhes do evento pré-preenchidos no convite e prontos para serem salvos pelo usuário. Isso acontece tanto no celular quanto no computador.

Caixa de diálogo do Google Agenda para adicionar um evento com os detalhes do evento adicionados e prontos para serem salvos.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal ou Outlook

Quando clicado na área de trabalho, é feito o download de um arquivo ICS. O usuário precisa então abrir o arquivo ICS, que abrirá o iCal ou o Outlook e solicitará que o usuário adicione o evento ao seu calendário.

Calendário do iCal com uma caixa de diálogo para adicionar um novo evento, que solicita que o usuário selecione um calendário e confirme.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

\![Calendário do iCal com o evento adicionado.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

No celular, os usuários precisam pressionar e manter pressionado o link, o que os leva a adicioná-lo ao calendário.

\![pop-up do iOS quando você pressiona e segura um link de calendário, que inclui um botão para "Add to Calendar".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Para obter mais informações, consulte:
* [Criar eventos para o Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Criar um link Add to calendar em uma mensagem de e-mail](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


