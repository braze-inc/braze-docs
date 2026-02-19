## Sobre as notificações por push para a Android TV

![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Embora não seja um recurso nativo, a integração de push da Android TV é possível com o uso do SDK da Braze para Android e do Firebase Cloud Messaging para registrar um token por push para a Android TV. No entanto, é necessário criar uma interface do usuário para exibir a carga útil da notificação depois que ela for recebida.

## Pré-requisitos

Para usar esse recurso, você precisará concluir o seguinte:

- [Integrar o SDK da Braze para Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurar notificações por push para o SDK do Braze para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Configuração de notificações por push

Para configurar notificações por push para a Android TV:

1. Crie uma exibição personalizada em seu app para exibir suas notificações.
2. Criar uma [fábrica de notificações personalizada]({{site.baseurl}}/developer_guide/push_notifications/customization#customization-display). Isso substituirá o comportamento padrão do SDK e permitirá que você exiba manualmente as notificações. Ao retornar `null`, isso impedirá o processamento do SDK e exigirá um código personalizado para exibir a notificação. Depois que essas etapas forem concluídas, você poderá começar a enviar push para a Android TV!<br><br>
3. (Opcional) Para rastrear a análise de dados de cliques de forma eficaz, configure o rastreamento da análise de cliques. Isso pode ser obtido com a criação de um [retorno de chamada]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback) para ouvir as intenções de abertura e recebimento de push da Braze.

{% alert note %}
Essas notificações **não persistirão** e só ficarão visíveis para o usuário quando o dispositivo as exibir. Isso se deve ao fato de a central de notificações do Android TV não oferecer suporte a notificações históricas.
{% endalert %} 

## Teste das notificações por push da Android TV

Para testar se a implementação do push foi bem-sucedida, envie uma notificação do dashboard da Braze como faria normalmente em um dispositivo Android.

- **Se o aplicativo for fechado**: A notificação por push exibirá uma notificação de brinde na tela.
- **Se o aplicativo estiver aberto**: Você tem a oportunidade de exibir a mensagem em sua própria interface de usuário hospedada. Recomendamos seguir o estilo da interface do usuário de nossas mensagens no app do Android Mobile SDK.

## Melhores práticas

Para os profissionais de marketing que usam o Braze, o lançamento de uma campanha para a Android TV será idêntico ao lançamento de um push para os apps para mobile do Android. Para direcionar esses dispositivos exclusivamente, recomendamos selecionar o app Android TV na segmentação.

A resposta entregue e clicada retornada pelo FCM seguirá a mesma convenção de um dispositivo Android móvel; portanto, quaisquer erros serão visíveis no registro de atividades da mensagem.
