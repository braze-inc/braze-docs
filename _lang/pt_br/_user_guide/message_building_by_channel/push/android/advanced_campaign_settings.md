---
nav_title: "Configurações avançadas de campanhas push"
article_title: Configurações avançadas de campanhas push
page_order: 5
page_layout: reference
description: "Este artigo de referência aborda algumas configurações do Advanced Push Campaign, como prioridade, URLs personalizados, opções de entrega e muito mais."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Configurações avançadas de campanhas push

> Há muitas configurações avançadas disponíveis para as notificações por push do Android e do Fire OS enviadas pelo dashboard do Braze. Este artigo descreverá esses recursos e como usá-los com sucesso.

## ID da notificação {#notification-id}

Um ID de notificação é um identificador exclusivo para uma categoria de mensagem de sua escolha que informa ao serviço de envio de mensagens para respeitar apenas a mensagem mais recente desse ID. A definição de uma ID de notificação permite que você envie apenas a mensagem mais recente e relevante, em vez de uma pilha de mensagens desatualizadas e irrelevantes.

Para atribuir um ID de notificação, navegue até a página de composição do push ao qual deseja adicionar o ID e selecione a guia **Configurações**. Insira um número inteiro na seção **Notification ID (ID da notificação** ). Para atualizar essa notificação depois de emiti-la, envie outra notificação com a mesma ID usada anteriormente.

![Campo de ID da notificação.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Time-To-Live (TTL) {#ttl}

O campo **Time to Live** permite que você defina um tempo personalizado para armazenar mensagens com o serviço de envio de mensagens por push. Se o dispositivo permanecer offline além do TTL, a mensagem expirará e não será entregue.

Para editar o tempo de vida do seu push Android, acesse o criador e selecione a guia **Configurações**. Encontre o campo **Time to Live** e insira um valor em dias, horas ou segundos.

Os valores padrão para o tempo de vida são definidos pelo seu administrador na página [Configurações de Push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Por padrão, a Braze define o TTL do Push para o valor máximo para cada serviço de envio de mensagens por push. Embora as configurações padrão de TTL se apliquem globalmente, você pode substituí-las no nível da mensagem durante a criação da campanha. Isso é útil quando diferentes campanhas exigem urgência ou janelas de entrega variadas.

Por exemplo, digamos que seu app hospede um concurso de trivia semanal. Você envia uma notificação por push uma hora antes de começar. Ao definir o TTL para 1 hora, você garante que os usuários que abrem o app após o início do concurso não receberão uma notificação sobre um evento que já começou.

{% details Melhores práticas %}

#### Quando usar TTLs mais curtos

TTLs mais curtos garantem que os usuários recebam notificações oportunas para eventos ou promoções que rapidamente perdem relevância. Por exemplo:

- **Varejo:** Enviando um push para uma venda relâmpago que termina em 2 horas (TTL: 1–2 horas)
- **Entrega de alimentos:** Notificando os usuários quando seu pedido está próximo (TTL: 10–15 minutos)
- **Apps de transporte:** Compartilhando atualizações de chegada de caronas (TTL: alguns minutos)
- **Lembretes de eventos:** Notificando os usuários quando um webinar está prestes a começar (TTL: menos de 1 hora)

#### Quando evitar TTL mais curtos

- Se a mensagem da sua campanha permanecer relevante por vários dias ou semanas, como lembretes de renovação de inscrição ou promoções em andamento.
- Quando maximizar o alcance é mais importante do que a urgência, como em anúncios de atualização de app ou promoções de recursos.

{% enddetails %}

## Prioridade de envio de mensagens do Firebase {#fcm-priority}

O campo **Prioridade de entrega de mensagens do Firebase** permite controlar se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging. Essa configuração determina quão rapidamente as mensagens são entregues e como elas afetam a vida útil da bateria do dispositivo.

| Prioridade | Descrição | Melhor para |
|---------|-------------|----------|
| Normal | Entrega otimizada para bateria que pode ser atrasada para conservar a bateria | Conteúdo não urgente, ofertas promocionais, atualizações de notícias |
| Alta | Entrega imediata com maior consumo de bateria | Notificações sensíveis ao tempo, alertas críticos, atualizações de eventos ao vivo, alertas de conta, notícias de última hora ou lembretes urgentes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Considerações

- **Configuração padrão**: Você pode definir uma prioridade padrão do FCM para todas as campanhas Android em suas [Configurações de Push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Essa configuração em nível de campanha substituirá a padrão, se necessário.
- **Despriorização**: Se o FCM detectar que seu app frequentemente envia mensagens de alta prioridade que não resultam em notificações visíveis para o usuário ou engajamento do usuário, essas mensagens podem ser automaticamente despriorizadas para prioridade normal.
- **Impacto na bateria**: Mensagens de alta prioridade despertam dispositivos adormecidos de forma mais agressiva e consomem mais bateria. Use essa prioridade com cautela.

Para informações mais detalhadas sobre o manuseio de mensagens e despriorização, consulte [documentação do FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) e [Manuseio de mensagens e despriorização no Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texto do resumo

O texto de resumo permite que você defina texto adicional na visualização expandida da notificação. Ele também serve como legenda para notificações com imagens.

![Uma mensagem Android com o título "Este é o título da notificação." e texto resumo "Este é o texto resumo da notificação."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

O texto do resumo será exibido sob o corpo da mensagem na exibição expandida. 

![Uma mensagem Android com o título "Este é o título da notificação." e texto resumo "Este é o texto resumo da notificação."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para notificações por push que incluem imagens, o texto da mensagem será mostrado na exibição recolhida, enquanto o texto do resumo será exibido como a legenda da imagem quando a notificação for expandida. 

## URIs personalizados

O recurso **URI personalizado** permite especificar um URL da Web ou um recurso do Android para o qual navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação levará os usuários ao seu app. Você pode usar o URI personalizado para fazer deep linking dentro do seu app, bem como direcionar os usuários para recursos que existem fora do seu app também. Isso pode ser especificado através da nossa [API de Mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou na aba **Compor** do criador de push.

![Campo URI personalizado.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Prioridade de exibição de notificação

{% alert important %}
A configuração Prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta a forma como a notificação é exibida na bandeja de notificações em relação a outras notificações. Isso também pode afetar a velocidade e a forma de entrega, pois as mensagens normais e de prioridade mais baixa podem ser enviadas com latência um pouco maior ou em lotes para preservar a vida útil da bateria, enquanto as mensagens de alta prioridade são sempre enviadas imediatamente.

Esse recurso é útil para diferenciar suas mensagens com base em seu grau de criticidade ou urgência. Por exemplo, uma notificação sobre condições perigosas da estrada seria uma boa candidata a receber uma prioridade alta, enquanto uma notificação sobre uma venda em andamento deveria receber uma prioridade mais baixa. Você deve considerar se o uso de uma prioridade perturbadora é realmente necessário para a notificação que está enviando, pois ocupar constantemente o primeiro lugar na caixa de entrada dos usuários ou interromper suas outras atividades pode ter um impacto negativo.

No Android O, a prioridade de notificação tornou-se uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar seus sons de notificação. Para dispositivos que executam versões do Android anteriores ao O, é possível especificar um nível de prioridade para notificações do Android e do Fire OS por meio do dashboard do Braze e da API de envio de mensagens.

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos que você especifique indiretamente a prioridade através da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance) (para direcionar dispositivos O+) e envie a prioridade individual do dashboard (para direcionar dispositivos <O).

Consulte a tabela a seguir para ver os níveis de prioridade que você pode definir nas notificações por push do Android ou do Fire OS:

| Prioridade | Descrição| `priority` valor da mensagem (para envios de mensagens da API) |
|------|-----------|----------------------------|
| Máx. | Envios de mensagens urgentes ou de tempo crítico. | `2` |
| Alta | Comunicação importante, como uma nova mensagem de um amigo. | `1` |
| Padrão | A maioria das notificações. Use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade. | `0` |
| Baixa | Informações que você deseja que os usuários conheçam, mas que não exigem ação imediata. | `-1`|
| Mín. | Informações contextuais ou de fundo. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais, consulte a documentação do Google sobre [as notificações do Android](http://developer.android.com/design/patterns/notifications.html).

## Categoria push

As notificações por push do Android oferecem a opção de especificar se a notificação se enquadra em uma categoria predefinida. A interface de usuário do sistema Android pode usar essa categoria para tomar decisões de classificação ou filtragem sobre onde colocar a notificação na bandeja de notificações do usuário.

![A guia Configurações com a Categoria definida como Nenhum, que é a configuração padrão.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Categoria | Descrição |
|---|-------|
| Nenhuma | Opção padrão. |
| Alarme | Alarme ou cronômetro. |
| Chamada | Chamada recebida (voz ou vídeo) ou solicitação de comunicação síncrona semelhante. |
| E-mail | Envio assíncrono de mensagens em massa (e-mail). |
| Erro | Erro na operação em segundo plano ou no status de autenticação. |
| Evento | Evento do calendário. |
| Mensagem | Mensagem direta recebida (SMS, mensagem instantânea, etc.). |
| Progresso | Progresso de uma operação em segundo plano de longa duração. |
| Promoção | Promoção ou propaganda. |
| Recomendação | Uma recomendação específica e oportuna para uma única coisa. |
| Lembrete | Lembrete programado pelo usuário. |
| Atendimento | Indicação de serviço em segundo plano em execução. |
| Mídia social | Rede social ou atualização de compartilhamento. |
| Status | Informações contínuas sobre o status do dispositivo ou do contexto. |
| Sistema | Atualização do status do sistema ou do dispositivo. Reservado para uso do sistema. |
| Transporte | Controle de transporte de mídia para reprodução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilidade do push

As notificações por push do Android fornecem um campo opcional para determinar como uma notificação aparece na tela de bloqueio do usuário. Consulte a tabela a seguir para ver as opções e descrições de visibilidade.

| Visibilidade | Descrição |
|---|-----|
| Público | A notificação aparece na tela de bloqueio |
| Privado | A notificação é exibida com a mensagem "Content hidden" (Conteúdo oculto) |
| Secreto | A notificação não é exibida na tela de bloqueio |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Além disso, os usuários do Android podem substituir a forma como as notificações por push aparecem na tela de bloqueio, alterando a configuração de privacidade da notificação no dispositivo. Essa configuração substituirá a visibilidade da notificação por push.

![Localização da prioridade de push do Dashboard com Visibilidade Definida habilitada e configurada como Privada.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Independentemente da visibilidade, todas as notificações serão mostradas na tela de bloqueio do usuário se a configuração de privacidade da notificação no dispositivo for **Mostrar todo o conteúdo** (configuração padrão). Da mesma forma, as notificações não serão exibidas na tela de bloqueio se a privacidade de notificação estiver definida como **Não mostrar notificações**. A visibilidade só terá efeito se a privacidade da notificação estiver definida como **Ocultar conteúdo confidencial**.

A visibilidade não tem efeito em dispositivos anteriores ao Android Lollipop 5.0.0, o que significa que todas as notificações serão exibidas nesses dispositivos.

Consulte nossa [documentação do Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) para saber mais.

## Sons de notificação

No Android O, os sons de notificação se tornaram uma propriedade dos canais de notificação. Será necessário trabalhar com o desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos que executam versões do Android anteriores ao Android O, o Braze permite que você defina o som de uma mensagem push individual por meio do criador do dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). 

A seleção de **Padrão** nesse campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado através da nossa [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou nas **Configurações** no criador de push.

![O campo "Som".]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Em seguida, digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do dashboard.

Para enviar mensagens para toda a sua base de usuários com um som específico, recomendamos que você especifique indiretamente o som através da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels) (para direcionar dispositivos O+) e envie o som individual do dashboard (para direcionar dispositivos <O).

