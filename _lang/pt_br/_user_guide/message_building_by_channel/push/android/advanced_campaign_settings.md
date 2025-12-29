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

> Há muitas configurações avançadas disponíveis para as notificações push do Android e do Fire OS enviadas por meio do painel do Braze. Este artigo descreverá esses recursos e como usá-los com sucesso.

## ID da notificação {#notification-id}

Um ID de notificação é um identificador exclusivo para uma categoria de mensagem de sua escolha que informa ao serviço de mensagens para respeitar apenas a mensagem mais recente desse ID. A definição de uma ID de notificação permite que você envie apenas a mensagem mais recente e relevante, em vez de uma pilha de mensagens desatualizadas e irrelevantes.

Para atribuir um ID de notificação, navegue até a página de composição do push ao qual você deseja adicionar o ID e selecione a guia **Settings (Configurações** ). Insira um número inteiro na seção **Notification ID (ID da notificação** ). Para atualizar essa notificação depois de emiti-la, envie outra notificação com a mesma ID usada anteriormente.

Campo ID da notificação.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Tempo de vida (TTL) {#ttl}

O campo **Time to Live** permite que você defina um período de tempo personalizado para armazenar mensagens com o serviço de mensagens por push. Se o dispositivo permanecer off-line além do TTL, a mensagem expirará e não será entregue.

Para editar o tempo de vida do seu push do Android, acesse o compositor e selecione a guia **Configurações**. Localize o campo **Time to Live** e digite um valor em dias, horas ou segundos.

Os valores padrão para o tempo de vida são definidos por seu administrador na página [Configurações de envio]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Por padrão, o Braze define o Push TTL como o valor máximo para cada serviço de mensagens push. Embora as configurações padrão de TTL se apliquem globalmente, você pode substituí-las no nível da mensagem durante a criação da campanha. Isso é útil quando diferentes campanhas exigem urgência ou janelas de entrega variadas.

Por exemplo, digamos que seu aplicativo realize um concurso semanal de perguntas e respostas. Você envia uma notificação por push uma hora antes do início do evento. Ao definir o TTL para 1 hora, você garante que os usuários que abrirem o aplicativo após o início do concurso não receberão uma notificação sobre um evento que já começou.

{% details Best practices %}

#### Quando usar o TTL mais curto

TTLs mais curtos garantem que os usuários recebam notificações oportunas sobre eventos ou promoções que perdem a relevância rapidamente. Por exemplo:

- **Varejo:** Envio de um push para uma venda relâmpago que termina em 2 horas (TTL: 1-2 horas)
- **Entrega de alimentos:** Notificar os usuários quando seu pedido estiver próximo (TTL: 10-15 minutos)
- **Aplicativos de transporte:** Compartilhamento de atualizações de chegada de carona (TTL: alguns minutos)
- **Lembretes de eventos:** Notificar os usuários quando um webinar estiver começando em breve (TTL: menos de 1 hora)

#### Quando evitar um TTL mais curto

- Se a mensagem de sua campanha permanecer relevante por vários dias ou semanas, como lembretes de renovação de assinatura ou promoções contínuas.
- Quando maximizar o alcance é mais importante do que a urgência, como em anúncios de atualização de aplicativos ou promoções de recursos.

{% enddetails %}

## Prioridade de entrega de mensagens do Firebase {#fcm-priority}

O campo **Firebase Messaging Delivery Priority (Prioridade de entrega de mensagens do Firebase** ) permite que você controle se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging. Essa configuração determina a rapidez com que as mensagens são entregues e como elas afetam a vida útil da bateria do dispositivo.

| Prioridade | Descrição | Melhor para |
|---------|-------------|----------|
| Normal | Entrega otimizada por bateria que pode ser atrasada para conservar a bateria | Conteúdo não urgente, ofertas promocionais, atualizações de notícias |
| Alta | Entrega imediata com maior consumo de bateria | Notificações sensíveis ao tempo, alertas críticos, atualizações de eventos ao vivo, alertas de conta, notícias de última hora ou lembretes urgentes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Considerações

- **Configuração padrão**: Você pode definir uma prioridade FCM padrão para todas as campanhas do Android em suas [configurações de push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Essa configuração em nível de campanha substituirá o padrão, se necessário.
- **Despriorização**: Se o FCM detectar que seu aplicativo envia com frequência mensagens de alta prioridade que não resultam em notificações visíveis para o usuário ou no envolvimento do usuário, essas mensagens poderão ser automaticamente despriorizadas para a prioridade normal.
- **Impacto da bateria**: As mensagens de alta prioridade despertam os dispositivos em repouso de forma mais agressiva e consomem mais bateria. Use essa prioridade de forma criteriosa.

Para obter informações mais detalhadas sobre o tratamento de mensagens e a despriorização, consulte [a documentação do FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) e [Tratamento de mensagens e despriorização no Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texto resumido

O texto de resumo permite que você defina um texto adicional na exibição de notificação expandida. Ele também serve como legenda para notificações com imagens.

\![Uma mensagem do Android com o título "Este é o título da notificação" e o texto de resumo "Este é o texto de resumo da notificação".]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

O texto do resumo será exibido sob o corpo da mensagem na exibição expandida. 

\![Uma mensagem do Android com o título "Este é o título da notificação" e o texto de resumo "Este é o texto de resumo da notificação".]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para notificações por push que incluem imagens, o texto da mensagem será mostrado na exibição recolhida, enquanto o texto do resumo será exibido como a legenda da imagem quando a notificação for expandida. 

## URIs personalizados

O recurso **Custom URI** permite que você especifique um URL da Web ou um recurso do Android para o qual navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação levará os usuários ao seu aplicativo. Você pode usar o URI personalizado para fazer links diretos dentro do seu aplicativo, bem como direcionar os usuários para recursos que também existem fora do seu aplicativo. Isso pode ser especificado por meio de nossa [API de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou na guia **Compor** do compositor de push.

\![Campo URI personalizado.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Prioridade de exibição de notificação

{% alert important %}
A configuração Prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta a forma como a notificação é exibida na bandeja de notificações em relação a outras notificações. Isso também pode afetar a velocidade e a forma de entrega, pois as mensagens normais e de prioridade mais baixa podem ser enviadas com latência um pouco maior ou em lotes para preservar a vida útil da bateria, enquanto as mensagens de alta prioridade são sempre enviadas imediatamente.

Esse recurso é útil para diferenciar suas mensagens com base em seu grau de importância ou urgência. Por exemplo, uma notificação sobre condições perigosas da estrada seria uma boa candidata a receber uma prioridade alta, enquanto uma notificação sobre uma venda em andamento deveria receber uma prioridade mais baixa. Você deve considerar se o uso de uma prioridade perturbadora é realmente necessário para a notificação que está enviando, pois ocupar constantemente o primeiro lugar na caixa de entrada dos usuários ou interromper suas outras atividades pode ter um impacto negativo.

No Android O, a prioridade de notificação tornou-se uma propriedade dos canais de notificação. Você precisará trabalhar com o desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o painel para selecionar o canal adequado ao enviar os sons de notificação. Para dispositivos que executam versões do Android anteriores ao O, a especificação de um nível de prioridade para notificações do Android e do Fire OS é possível por meio do painel do Braze e da API de mensagens.

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos que você especifique indiretamente a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance) (para direcionar dispositivos O+) e envie a prioridade individual do painel (para direcionar dispositivos <O).

Consulte a tabela a seguir para ver os níveis de prioridade que você pode definir nas notificações por push do Android ou do Fire OS:

| Prioridade | Descrição| `priority` valor (para mensagens de API) |
|------|-----------|----------------------------|
| Máximo | Mensagens urgentes ou de tempo crítico. | `2` |
| Alta | Comunicação importante, como uma nova mensagem de um amigo. | `1` |
| Padrão | A maioria das notificações. Use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade. | `0` |
| Baixa | Informações que você deseja que os usuários conheçam, mas que não exigem ação imediata. | `-1`|
| Mínimo | Informações contextuais ou de fundo. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para obter mais informações, consulte a documentação do Google sobre [as notificações do Android](http://developer.android.com/design/patterns/notifications.html).

## Categoria Push

As notificações por push do Android oferecem a opção de especificar se a notificação se enquadra em uma categoria predefinida. A interface de usuário do sistema Android pode usar essa categoria para tomar decisões de classificação ou filtragem sobre onde colocar a notificação na bandeja de notificações do usuário.

\![Guia Settings (Configurações) com a categoria definida como None (Nenhuma), que é a configuração padrão.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Categoria | Descrição |
|---|-------|
| Nenhum | Opção padrão. |
| Alarme | Alarme ou cronômetro. |
| Chamada | Chamada recebida (voz ou vídeo) ou solicitação de comunicação síncrona semelhante. |
| E-mail | Mensagem assíncrona em massa (e-mail). |
| Erro | Erro na operação em segundo plano ou no status de autenticação. |
| Evento | Evento do calendário. |
| Mensagem | Mensagem direta recebida (SMS, mensagem instantânea, etc.). |
| Progresso | Progresso de uma operação em segundo plano de longa duração. |
| Promoção | Promoção ou propaganda. |
| Recomendação | Uma recomendação específica e oportuna para uma única coisa. |
| Lembrete | Lembrete programado pelo usuário. |
| Serviço | Indicação de serviço em segundo plano em execução. |
| Social | Rede social ou atualização de compartilhamento. |
| Status | Informações contínuas sobre o status do dispositivo ou do contexto. |
| Sistema | Atualização do status do sistema ou do dispositivo. Reservado para uso do sistema. |
| Transporte | Controle de transporte de mídia para reprodução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilidade do push

As notificações por push do Android fornecem um campo opcional para determinar como uma notificação é exibida na tela de bloqueio do usuário. Consulte a tabela a seguir para ver as opções e descrições de visibilidade.

| Visibilidade | Descrição |
|---|-----|
| Público | A notificação aparece na tela de bloqueio |
| Privado | A notificação é exibida com a mensagem "Content hidden" (Conteúdo oculto) |
| Secreto | A notificação não é exibida na tela de bloqueio |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Além disso, os usuários do Android podem substituir a forma como as notificações push aparecem na tela de bloqueio alterando a configuração de privacidade da notificação no dispositivo. Essa configuração substituirá a visibilidade da notificação por push.

\![Local de prioridade de envio do painel com a opção Definir visibilidade ativada e definida como Privada.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Independentemente da visibilidade, todas as notificações serão mostradas na tela de bloqueio do usuário se a configuração de privacidade da notificação no dispositivo for **Mostrar todo o conteúdo** (configuração padrão). Da mesma forma, as notificações não serão exibidas na tela de bloqueio se a privacidade de notificação estiver definida como **Não mostrar notificações**. A visibilidade só terá efeito se a privacidade da notificação estiver definida como **Ocultar conteúdo confidencial**.

A visibilidade não tem efeito em dispositivos anteriores ao Android Lollipop 5.0.0, o que significa que todas as notificações serão exibidas nesses dispositivos.

Consulte nossa [documentação do Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) para obter mais informações.

## Sons de notificação

No Android O, os sons de notificação tornaram-se uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o painel para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos que executam versões do Android anteriores ao Android O, o Braze permite que você defina o som de uma mensagem push individual por meio do compositor do painel. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). 

A seleção de **Padrão** nesse campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio de nossa [API de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou nas **configurações** do compositor de envio.

\![O campo "Sound" (Som).]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Em seguida, digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do painel.

Para enviar mensagens para toda a sua base de usuários com um som específico, recomendamos que você especifique indiretamente o som por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels) (para dispositivos O+ de destino) e envie o som individual do painel (para dispositivos <O de destino).

