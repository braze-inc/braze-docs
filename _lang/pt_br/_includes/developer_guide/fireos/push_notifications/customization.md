{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Configurações

Existem muitas configurações avançadas disponíveis para notificações por push do FireOS enviadas através do dashboard da Braze. Este artigo descreverá esses recursos e como usá-los com sucesso.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### Time-To-Live (TTL) {#ttl}

O campo **TTL** permite que você defina um tempo personalizado para armazenar mensagens com o serviço de push de envio de mensagens. Os valores padrão para TTL são quatro semanas para FCM e 31 dias para ADM.

### Texto resumido {#summary-text}

O texto de resumo permite que você defina texto adicional na visualização expandida da notificação. Ele também serve como legenda para notificações com imagens.

![Uma mensagem Android com o título "Este é o título da notificação." e texto resumo "Este é o texto resumo da notificação."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

O texto do resumo será exibido sob o corpo da mensagem na exibição expandida. 

![Uma mensagem Android com o título "Este é o título da notificação." e texto resumo "Este é o texto resumo da notificação."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para notificações por push que incluem imagens, o texto da mensagem será mostrado na exibição recolhida, enquanto o texto do resumo será exibido como a legenda da imagem quando a notificação for expandida. 

### URIs personalizados {#custom-uri}

O recurso **Custom URI** permite que você especifique um URL da Web ou um recurso do Android para navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação leva os usuários para o seu app. Você pode usar o URI personalizado para deep link dentro do seu app e direcionar os usuários para recursos que existem fora do seu app. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) ou de nosso dashboard, em **Advanced Settings (Configurações avançadas)**, no criador de mensagens push, conforme ilustrado:

![A configuração avançada de deep linking no criador do Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Prioridade de exibição de notificação

{% alert important %}
A configuração Prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta como sua notificação é exibida na bandeja de notificações em relação a outras notificações. Também pode afetar a velocidade e a maneira de entrega, pois mensagens normais e de baixa prioridade podem ser enviadas com uma latência ligeiramente maior ou agrupadas para preservar a vida útil da bateria, enquanto mensagens de alta prioridade são sempre enviadas imediatamente.

No Android O, a prioridade de notificação se tornou uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar seus sons de notificação. Para dispositivos que executam versões do Android anteriores ao O, especificar um nível de prioridade para notificações do FireOS é possível através do dashboard da Braze e da API de envio de mensagens. 

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos que você especifique indiretamente a prioridade através da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance) (para direcionar dispositivos O+) *e* envie a prioridade individual a partir do dashboard (para direcionar dispositivos <O).

Os níveis de prioridade que você pode definir nas notificações por push do Fire OS são:

| Prioridade | Descrição/Utilização Pretendida | `priority` valor (para mensagens de API) |
|----------|--------------------------|-------------------------------------|
| Máx.      | Mensagens urgentes ou críticas de tempo | `2` |
| Alta     | Comunicação importante, como uma nova mensagem de um amigo | `1` |
| Padrão  | A maioria das notificações - use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade | `0` |
| Baixa      | Informações que você deseja que os usuários saibam, mas que não exigem ação imediata | `-1` |
| Mín.      | Informações contextuais ou de fundo. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais, consulte a documentação de [notificação do Android](http://developer.android.com/design/patterns/notifications.html) do Google.

### Sons {#sounds}

No Android O, os sons de notificação se tornaram uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos executando versões do Android anteriores ao O, o Braze permite que você defina o som de uma mensagem push individual através do criador do dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). Especificar "padrão" neste campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) ou do dashboard em **Configurações** no criador de mensagens push.

![A configuração avançada de som no criador do Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do dashboard.

Para enviar mensagens para toda a sua base de usuários com um som específico, recomendamos que você especifique indiretamente o som através da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels) (para direcionar dispositivos O+) *e* envie o som individual a partir do dashboard (para direcionar dispositivos <O).
