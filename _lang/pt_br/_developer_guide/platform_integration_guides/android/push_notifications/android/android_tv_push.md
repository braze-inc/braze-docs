---
nav_title: Android TV Push
article_title: Android TV Push
platform: Android
page_order: 8
description: "Este artigo mostra como implementar e testar o Android TV Push."
channel:
  - push

---

# Push da Android TV
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> Embora não seja um recurso nativo, a integração de push da Android TV é possível com o uso do SDK da Braze para Android e do Firebase Cloud Messaging para registrar um token por push para a Android TV. No entanto, é necessário criar uma interface do usuário para exibir a carga útil da notificação depois que ela for recebida.

## Implementação

1. **Integrar o SDK da Braze para Android**<br>
Primeiro, você precisa integrar o [Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true) (se ainda não tiver concluído).<br><br>
2. **Integrar notificações por push**<br>
Em seguida, você deve integrar [as notificações por push do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) (se ainda não tiver concluído).<br><br>
3. **Criar um modo de exibição de torradas personalizado**<br>
Em seguida, crie uma exibição personalizada em seu app para suas notificações.<br><br>
4. **Criar uma fábrica de notificações personalizada**<br>
Por fim, você precisa criar uma [fábrica de notificações personalizada]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications). Isso substituirá o comportamento padrão do SDK e permitirá que você exiba manualmente as notificações. Ao retornar `null`, isso impedirá o processamento do SDK e exigirá um código personalizado para exibir a notificação. Depois que essas etapas forem concluídas, você poderá começar a enviar push para a Android TV!<br><br>
5. **Configure o rastreamento da análise de dados de cliques (opcional)**<br>
Para rastrear a análise de dados de cliques de forma eficaz, é necessário lidar com isso manualmente, pois a Braze não lida com a exibição das mensagens automaticamente. Isso pode ser obtido com a criação de um [retorno de chamada]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) para ouvir as intenções de abertura e recebimento de push da Braze.

{% alert note %}
Note que essas notificações **não persistirão** e só ficarão visíveis para o usuário quando o dispositivo as exibir. Isso se deve ao fato de a central de notificações do Android TV não oferecer suporte a notificações históricas.
{% endalert %} 

## Como testar o push na Android TV

Para testar se a implementação do push foi bem-sucedida, envie uma notificação do dashboard da Braze como faria normalmente em um dispositivo Android.

- **Se o aplicativo for fechado**: A notificação por push exibirá uma notificação de brinde na tela.
- **Se o aplicativo estiver aberto**: Você tem a oportunidade de exibir a mensagem em sua própria interface de usuário hospedada. Recomendamos seguir o estilo da interface do usuário de nossas mensagens no app do Android Mobile SDK.

## Informações adicionais
Para um usuário final de marketing na Braze, o lançamento de uma campanha para a Android TV será idêntico ao lançamento de um push para aplicativos móveis Android. Para direcionar esses dispositivos exclusivamente, recomendamos selecionar o app Android TV na segmentação. 

A resposta entregue e clicada retornada pelo FCM seguirá a mesma convenção de um dispositivo Android móvel; portanto, quaisquer erros serão visíveis no registro de atividades da mensagem.

