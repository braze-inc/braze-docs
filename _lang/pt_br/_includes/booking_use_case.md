# Caso de uso: Sistema de lembrete de e-mail de reserva

> Braze é uma plataforma abrangente de engajamento com clientes que foi projetada para ser altamente controlável programaticamente. Neste caso de uso, demonstraremos apenas algumas maneiras pelas quais o Braze fornece funcionalidades que você pode integrar em casos de uso que estão na interseção de produto e marketing, como sistemas de reserva.

Este caso de uso mostra como você pode usar os recursos do Braze para construir um serviço de envio de mensagens de lembrete de reserva por e-mail. O serviço permitirá que os usuários agendem compromissos e enviará mensagens aos usuários com lembretes de seus compromissos futuros. Embora este caso de uso utilize mensagens de e-mail, você pode enviar mensagens em qualquer canal, ou em múltiplos canais, com base em uma única atualização no perfil do usuário.

Outros benefícios de criar este serviço incluem:
- As mensagens enviadas terão rastreamento e relatórios completos.
- O conteúdo da mensagem pode ser atualizado por usuários do Braze que não são técnicos.
- As mensagens obedecem aos status de aceitação e recusa nos perfis dos usuários conforme a configuração da campanha.
- Tanto os dados de reserva quanto os dados de interação com mensagens podem ser usados para segmentar e direcionar usuários para mensagens adicionais. Por exemplo, você pode redirecionar aqueles que não abrem a mensagem de lembrete inicial com um lembrete adicional antes de seu compromisso.

Siga estas etapas para alcançar este caso de uso:
1. [Escreva os dados de reserva futuros em um perfil de usuário do Braze](#step-1)
2. [Configure e lance uma mensagem de lembrete de reserva](#step-2)
3. [Gerencie reservas e cancelamentos atualizados](#step-3)

## Etapa 1: Escreva os dados de reserva futuros em um perfil de usuário do Braze {#step-1}

Use o endpoint do Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para escrever um [atributo personalizado aninhado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) em um perfil de usuário cada vez que uma reserva ocorrer. Certifique-se de que o atributo personalizado aninhado contenha todas as informações necessárias para enviar e personalizar a mensagem de lembrete. Neste caso de uso, nomearemos o atributo personalizado aninhado como "viagens".

### Adicionar reserva

Quando um usuário cria uma reserva, use a seguinte estrutura para o array de objetos para enviar os dados para o Braze através do endpoint `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

O atributo personalizado aninhado "trips" será exibido no perfil do usuário assim.

![Dois atributos personalizados aninhados para uma viagem a Londres e uma viagem a Sydney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Atualizar reserva
Quando um usuário atualiza uma reserva, use a seguinte estrutura para o array de objetos para enviar os dados para o Braze através do endpoint `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### Remover reserva

{% tabs %}
{% tab /users/track endpoint %}
#### Enviar dados através do endpoint `/users/track`
Quando um usuário exclui uma reserva, use a seguinte estrutura para o array de objetos para enviar os dados para o Braze através do endpoint `/users/track`.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### Escrever atributos aninhados nos perfis de usuário através do SDK

Se você está coletando reservas de compromissos com seu app, site ou ambos e deseja escrever esses dados diretamente em um perfil de usuário, você pode usar o SDK do Braze para transmitir esses dados. Aqui está um exemplo utilizando o SDK Web:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

A reserva especificada será removida do atributo personalizado aninhado no perfil do usuário e exibirá quaisquer reservas restantes.

![Um atributo personalizado aninhado para uma viagem a Londres.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Etapa 2: Configurar e lançar uma mensagem de lembrete de reserva {#step-2}

### Etapa 2a: Criar um público-alvo
Criar um público-alvo para receber lembretes usando segmentação de múltiplos critérios. Por exemplo, se você quiser enviar um lembrete dois dias antes da data da reserva, selecione o seguinte:

- Uma data de início **em mais de 1 dia** e
- Uma data de início **em menos de 2 dias** 

![Um atributo personalizado aninhado "trips" com critérios para uma data de início que seja mais de um dia e menos de dois dias.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Etapa 2b: Crie sua mensagem

Crie a mensagem de e-mail de lembrete seguindo os passos em [Criando um e-mail com HTML personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/). Use Liquid para personalizar a mensagem com dados do atributo personalizado do cliente que você criou (“trips”), como neste exemplo.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}} 
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### Etapa 2c: Lance sua campanha

Lance a campanha para a mensagem de e-mail de lembrete. Agora, cada vez que a Braze receber o atributo personalizado “trips”, uma mensagem será agendada de acordo com os dados incluídos no objeto da respectiva reserva.

## Etapa 3: Gerencie atualizações de reservas e cancelamentos {#step-3}

Agora que você está enviando mensagens de lembrete, pode configurar mensagens de confirmação para enviar quando as reservas forem atualizadas ou canceladas.

### Etapa 3a: Envie dados atualizados

{% tabs %}
{% tab /users/track %}

#### Enviar dados através do endpoint `/users/track`
Use o endpoint Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para enviar um evento personalizado quando um usuário atualiza ou cancela uma reserva. Nesse evento, coloque os dados necessários nas propriedades do evento que confirmarão a alteração. 

Digamos que, neste caso de uso, um usuário atualizou a data de sua viagem para Sydney. O evento seria assim:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### Escrever atributos aninhados nos perfis de usuário através do SDK

Envie eventos personalizados para o perfil do usuário através do SDK. Por exemplo, se você estiver usando o SDK da web, poderá enviar:

{% raw %}
```json
braze.logCustomEvent("trip_updated", { 
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Etapa 3b: Crie uma mensagem para confirmar a atualização

Crie uma [campanha baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para enviar ao usuário uma confirmação de sua reserva atualizada. Você pode [usar Liquid para modelar propriedades do evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) que refletem o nome, o horário antigo e o novo horário da reserva (ou apenas o nome se for um cancelamento) na própria mensagem.

Por exemplo, você poderia compor a seguinte mensagem:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Etapa 3c: Modifique o perfil do usuário para refletir a atualização

Finalmente, para enviar os lembretes de reserva das etapas 1 e 2 com base nos dados mais recentes, atualize os atributos personalizados aninhados para refletir a mudança ou cancelamento na reserva.

#### Reserva atualizada

Se o usuário neste caso de uso atualizou sua viagem para Sydney, você usaria o endpoint `/users/track` para mudar a data com uma chamada como esta:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### Reserva cancelada

Se o usuário neste caso de uso cancelou sua viagem para Sydney, você enviaria a seguinte chamada para o endpoint `/users/track`:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

Depois que essas chamadas forem enviadas e o perfil do usuário for atualizado, as mensagens de lembrete de reserva refletirão os dados mais recentes sobre as datas de reserva do usuário.

