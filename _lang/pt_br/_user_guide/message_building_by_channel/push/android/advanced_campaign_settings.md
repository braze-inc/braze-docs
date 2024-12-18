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

![]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:80%;" }

## TTL (Time-to-live) {#ttl}

O campo TTL (time-to-live) permite que você defina um período de tempo personalizado para armazenar mensagens com o serviço de envio de mensagens push. Os valores padrão do TTL são 4 semanas para o Firebase Cloud Messaging (FCM) e 31 dias para o Amazon Device Messaging (ADM).

Por exemplo, suponha que o seu app seja um jogo e que você ofereça aos usuários um bônus em moeda do jogo se eles mantiverem uma sequência de jogos diários. Você pode enviar um push alertando um usuário de que essa sequência corre o risco de ser quebrada se ele tiver ultrapassado um determinado número de dias. No entanto, se um usuário reconectasse seu dispositivo ao app do jogo quatro semanas depois com o TTL definido como padrão, essas mensagens já teriam expirado no serviço de envio de mensagens e não seriam entregues.

## Prioridade de envio de mensagens do Firebase {#fcm-priority}

O campo **Prioridade de entrega de mensagens do Firebase** permite controlar se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging. Consulte [a documentação do FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) para saber mais.

## Texto do resumo

O texto de resumo permite que você defina um texto adicional na exibição **de notificação expandida**. O texto do resumo será exibido sob o corpo da mensagem na exibição expandida. Ele também serve como legenda para notificações com imagens.

![][9]

Para notificações por push que incluem imagens, o texto da mensagem será mostrado na exibição recolhida, enquanto o texto do resumo será exibido como a legenda da imagem quando a notificação for expandida. Dê uma olhada na animação a seguir para ver um exemplo desse comportamento.

![Resumo do comportamento do texto][15]

## URIs personalizados

O recurso **URI personalizado** permite especificar um URL da Web ou um recurso do Android para o qual navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação levará os usuários ao seu app. Você pode usar o URI personalizado para fazer deep linking dentro do seu app, bem como direcionar os usuários para recursos que existem fora do seu app também. Isso pode ser especificado por meio de nossa [API de envio de mensagens][13] ou nas **configurações** do criador de mensagens push.

![URI personalizado][12]

## Prioridade de exibição de notificação

{% alert important %}
A configuração Prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta a forma como a notificação é exibida na bandeja de notificações em relação a outras notificações. Isso também pode afetar a velocidade e a forma de entrega, pois as mensagens normais e de prioridade mais baixa podem ser enviadas com latência um pouco maior ou em lotes para preservar a vida útil da bateria, enquanto as mensagens de alta prioridade são sempre enviadas imediatamente.

Esse recurso é útil para diferenciar suas mensagens com base em seu grau de criticidade ou urgência. Por exemplo, uma notificação sobre condições perigosas da estrada seria uma boa candidata a receber uma prioridade alta, enquanto uma notificação sobre uma venda em andamento deveria receber uma prioridade mais baixa. Você deve considerar se o uso de uma prioridade perturbadora é realmente necessário para a notificação que está enviando, pois ocupar constantemente o primeiro lugar na caixa de entrada dos usuários ou interromper suas outras atividades pode ter um impacto negativo.

No Android O, a prioridade de notificação tornou-se uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar seus sons de notificação. Para dispositivos que executam versões do Android anteriores ao O, é possível especificar um nível de prioridade para notificações do Android e do Fire OS por meio do dashboard do Braze e da API de envio de mensagens.

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos que especifique indiretamente a prioridade por meio da [configuração do canal de envio de mensagens][17] (para direcionar dispositivos O+) e envie a prioridade individual a partir do dashboard (para direcionar dispositivos <O).

Consulte a tabela a seguir para ver os níveis de prioridade que você pode definir nas notificações por push do Android ou do Fire OS:

| Prioridade | Descrição| `priority` valor da mensagem (para envios de mensagens da API) |
|------|-----------|----------------------------|
| Máx. | Envios de mensagens urgentes ou de tempo crítico. | `2` |
| Alta | Comunicação importante, como uma nova mensagem de um amigo. | `1` |
| Padrão | A maioria das notificações. Use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade. | `0` |
| Baixa | Informações que você deseja que os usuários conheçam, mas que não exigem ação imediata. | `-1`|
| Mín. | Informações contextuais ou de fundo. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais, consulte a documentação do Google sobre [as notificações do Android][2].

## Categoria push

As notificações por push do Android oferecem a opção de especificar se a notificação se enquadra em uma categoria predefinida. A interface de usuário do sistema Android pode usar essa categoria para tomar decisões de classificação ou filtragem sobre onde colocar a notificação na bandeja de notificações do usuário.

![Guia Configurações com a Categoria definida como Nenhuma, que é a configuração padrão.][52]

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

![Local de prioridade push do dashboard com Visibilidade ativada e definida como Privada.][53]{: style="float:right;max-width:60%;margin-left:15px;"}

Independentemente da visibilidade, todas as notificações serão mostradas na tela de bloqueio do usuário se a configuração de privacidade da notificação no dispositivo for **Mostrar todo o conteúdo** (configuração padrão). Da mesma forma, as notificações não serão exibidas na tela de bloqueio se a privacidade de notificação estiver definida como **Não mostrar notificações**. A visibilidade só terá efeito se a privacidade da notificação estiver definida como **Ocultar conteúdo confidencial**.

A visibilidade não tem efeito em dispositivos anteriores ao Android Lollipop 5.0.0, o que significa que todas as notificações serão exibidas nesses dispositivos.

Consulte nossa [documentação do Android][51] para saber mais.

## Sons de notificação

No Android O, os sons de notificação se tornaram uma propriedade dos canais de notificação. Será necessário trabalhar com o desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos que executam versões do Android anteriores ao Android O, o Braze permite que você defina o som de uma mensagem push individual por meio do criador do dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). 

A seleção de **Padrão** nesse campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio de nossa [API de envio de mensagens][13] ou nas **configurações** do criador de mensagens push.

![][11]

Em seguida, digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do dashboard.

Para enviar mensagens a toda a sua base de usuários com um som específico, recomendamos que especifique indiretamente o som por meio da [configuração do canal de envio de mensagens][16] (para direcionar dispositivos O+) e envie o som individual a partir do dashboard (para direcionar dispositivos <O).

[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
Daqui a [17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels
Daqui a [51]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
