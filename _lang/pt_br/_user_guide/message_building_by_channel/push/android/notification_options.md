---
nav_title: "Opções de notificação"
article_title: Opções de notificação do Android
page_order: 2
page_type: reference
description: "Este artigo de referência aborda várias opções de notificação do Android e a melhor maneira de usá-las nas campanhas do Braze."

platform: Android
channel:
  - Push

---

# Opções de notificação

> Estas são algumas das opções de notificação por push específicas do Android disponíveis através do Braze.

## Notificações silenciosas

Quando você [compõe sua notificação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), você **não pode** enviar uma mensagem push do Android sem um título—no entanto, você pode inserir um único espaço em vez disso. Tenha em mente que, se sua mensagem contiver apenas um único espaço, ela será enviada como uma notificação por push silenciosa. Para saber mais, veja [Notificações push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Grupos de notificação

Se quiser categorizar suas mensagens e agrupá-las na bandeja de notificação do usuário, poderá utilizar o recurso Canais de Notificação do Android por meio do Braze.

Primeiro, crie sua campanha de push Android, depois olhe para o topo da guia **Compor** para o menu suspenso **Canal de Notificação**.

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Selecione seu canal de notificação no menu suspenso. Você também deve selecionar um canal fallback caso as configurações do canal de notificação não funcionem corretamente.

Se você não tiver nenhum [canal de notificação]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) listado aqui, poderá adicionar um usando a ID do canal de notificação. Entre em contato com os desenvolvedores para identificar quais são as IDs dos canais de notificação ou para criar novas IDs, conforme necessário. 

Para adicionar um ID de notificação ao seu canal de notificação, clique em **Gerenciar canal de notificação** no menu suspenso **Canal de notificação** e preencha os campos obrigatórios. Os canais de notificação devem ser definidos no app antes de poderem ser usados na plataforma Braze.

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


