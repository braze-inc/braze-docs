---
nav_title: "Opções de notificação"
article_title: Opções de Notificação do Android
page_order: 2
page_type: reference
description: "Este artigo de referência cobre várias opções de notificação do Android e como usá-las da melhor forma nas campanhas do Braze."

platform: Android
channel:
  - Push

---

# Opções de notificação

> Estas são algumas das opções de notificação push específicas do Android disponíveis através do Braze.

## Notificações silenciosas

Quando você [compõe sua mensagem de notificação push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), você **não pode** enviar uma mensagem push do Android sem um título—no entanto, você pode inserir um único espaço em vez disso. Tenha em mente que, se sua mensagem contiver apenas um único espaço, ela será enviada como uma notificação push silenciosa. Para mais informações, veja [Notificações push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Grupos de notificação

Se você quiser categorizar suas mensagens e agrupá-las na bandeja de notificações do seu usuário, pode utilizar o recurso de Canais de Notificação do Android através do Braze.

Primeiro, crie sua campanha de push do Android, depois olhe para o topo da aba **Compor** para o menu suspenso **Canal de Notificação**.

\![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Selecione seu Canal de Notificação no menu suspenso. Você também deve selecionar um canal de fallback caso as configurações do seu Canal de Notificação falhem.

Se você não tiver nenhum [Canal de Notificação]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) listado aqui, pode adicionar um usando o ID do Canal de Notificação. Entre em contato com seus desenvolvedores para identificar quais são os IDs do seu Canal de Notificação ou para criar novos IDs conforme necessário. 

Para adicionar um ID de Notificação ao seu Canal de Notificação, clique em **Gerenciar Canal de Notificação** no menu suspenso **Canal de Notificação** e preencha os campos obrigatórios. Os Canais de Notificação devem ser definidos no aplicativo antes de poderem ser usados na plataforma Braze.

\![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


