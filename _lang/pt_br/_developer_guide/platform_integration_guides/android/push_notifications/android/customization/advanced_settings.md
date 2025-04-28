---
nav_title: Configurações avançadas
article_title: Configurações avançadas de notificação por push para Android
platform: Android
page_order: 40
description: "Este artigo de referência cobre configurações avançadas de notificação por push do Android, como TTL, IDs de notificação, prioridade de notificação e mais."
channel:
  - push

---

# Configurações avançadas

> Há muitas configurações avançadas disponíveis para notificações por push do Android e FireOS enviadas pelo dashboard do Braze. Este artigo descreverá esses recursos e como usá-los com sucesso.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

## ID de notificação {#notification-id}

Um **ID de Notificação** é um identificador único para uma categoria de mensagem de sua escolha que informa o serviço de envio de mensagens a respeitar apenas a mensagem mais recente desse ID. Definir um ID de notificação permite que você envie apenas a mensagem mais recente e relevante, em vez de uma pilha de mensagens desatualizadas e irrelevantes.

## Prioridade de entrega de mensagem do Firebase {#fcm-priority}

O campo [Prioridade de entrega de mensagem do Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) permite que você controle se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging.

## Time to live (TTL) {#ttl}

O campo **TTL** permite que você defina um tempo personalizado para armazenar mensagens com o serviço de push de envio de mensagens. Os valores padrão para TTL são quatro semanas para FCM e 31 dias para ADM.

## Texto resumido {#summary-text}

O texto de resumo permite que você defina texto adicional na visualização expandida da notificação. Também serve como uma legenda para notificações com imagens.

![Uma mensagem do Android com o título "Saudações do Appboy!", a mensagem "Este é o corpo da mensagem!" Você pode até adicionar emojis." e texto de resumo "Este é o texto de resumo."]({% image_buster /assets/img_archive/summary_text.png %})

O texto do resumo será exibido sob o corpo da mensagem na visualização expandida.

Para notificações por push que incluem imagens, o texto da mensagem será exibido na visualização recolhida, enquanto o texto de resumo será exibido como a legenda da imagem quando a notificação for expandida. 

![Uma mensagem do Android com o título "Appboy!", a mensagem "Este é o corpo da mensagem..." e o texto de resumo "e este é o texto de resumo."]({% image_buster /assets/img_archive/messagesummary.gif %})

## URIs personalizados {#custom-uri}

O recurso **Custom URI** permite que você especifique um URL da Web ou um recurso do Android para navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação leva os usuários para o seu app. Você pode usar o URI personalizado para deep link dentro do seu app e direcionar os usuários para recursos que existem fora do seu app. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou de nosso dashboard, em **Advanced Settings (Configurações avançadas)**, no criador de mensagens push, conforme ilustrado:

![A configuração avançada de deep linking no criador do Braze.]({% image_buster /assets/img_archive/deep_link.png %})

## Prioridade de exibição de notificação {#notification-priority}

{% alert important %}
A configuração Prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta como sua notificação é exibida na bandeja de notificações em relação a outras notificações. Também pode afetar a velocidade e a maneira de entrega, pois mensagens normais e de baixa prioridade podem ser enviadas com uma latência ligeiramente maior ou agrupadas para preservar a vida útil da bateria, enquanto mensagens de alta prioridade são sempre enviadas imediatamente.

No Android O, a prioridade de notificação se tornou uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar seus sons de notificação. Para dispositivos executando versões do Android anteriores ao O, especificar um nível de prioridade para notificações do Android e FireOS é possível através do dashboard do Braze e da API de envio de mensagens. 

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos que especifique indiretamente a prioridade por meio da [configuração do canal de envio de mensagens](https://developer.android.com/training/notify-user/channels#importance) (para direcionar dispositivos O+) *e* envie a prioridade individual a partir do dashboard (para direcionar dispositivos <O).

Os níveis de prioridade que você pode definir em notificações por push do Android ou Fire OS são:

| Prioridade | Descrição/Utilização Pretendida | `priority` valor (para mensagens de API) |
|----------|--------------------------|-------------------------------------|
| Máx.      | Mensagens urgentes ou críticas de tempo | `2` |
| Alta     | Comunicação importante, como uma nova mensagem de um amigo | `1` |
| Padrão  | A maioria das notificações - use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade | `0` |
| Baixa      | Informações que você deseja que os usuários saibam, mas que não exigem ação imediata | `-1` |
| Mín.      | Informações contextuais ou de fundo. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Consulte a documentação de [notificação do Android](http://developer.android.com/design/patterns/notifications.html) do Google para saber mais.

## Sons {#sounds}

No Android O, os sons de notificação se tornaram uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos executando versões do Android anteriores ao O, o Braze permite que você defina o som de uma mensagem push individual através do criador do dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). Especificar "padrão" neste campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou do dashboard em **Configurações avançadas** no criador do push.

![A configuração avançada de som no criador do Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do dashboard.

Para enviar mensagens a toda a sua base de usuários com um som específico, recomendamos que especifique indiretamente o som por meio da [configuração do canal de envio de mensagens](https://developer.android.com/training/notify-user/channels) (para direcionar dispositivos O+) *e* envie o som individual a partir do dashboard (para direcionar dispositivos <O).

