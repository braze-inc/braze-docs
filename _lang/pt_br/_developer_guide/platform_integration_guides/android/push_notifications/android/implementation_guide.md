---
nav_title: Guia de implementação avançada (opcional)
article_title: Implementação avançada de notificações por push para Android (opcional)
platform: Android
page_order: 29
description: "Este guia de implementação avançada aborda como personalizar o layout das notificações por push para exibir informações específicas do usuário em suas mensagens. Também está incluído um exemplo de caso de uso criado por nossa equipe, acompanhando snippets e orientações sobre análises de dados."
channel:
  - push
---

<br>
{% alert important %}
Está procurando o guia básico de integração de desenvolvedores de notificações por push? Acesse [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# Guia de implementação avançada

> Este guia de implementação opcional e avançado aborda maneiras de aproveitar uma subclasse personalizada do FirebaseMessagingService para obter o máximo de suas mensagens push. Também está incluído um caso de uso personalizado criado por nossa equipe, acompanhando snippets e orientações sobre análises de dados. Consulte nosso Repositório de Demonstrações da Braze [aqui](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Note que este guia de implementação está centrado em uma implementação Kotlin, mas são fornecidos trechos em Java para os interessados.

## Layout de notificação personalizado

As notificações do Braze são enviadas como [mensagens de dados](https://firebase.google.com/docs/cloud-messaging/concept-options), o que significa que seu aplicativo sempre terá a chance de responder e executar o comportamento de acordo, mesmo em segundo plano (isso contrasta com as mensagens de notificação, que podem ser tratadas automaticamente pelo sistema quando seu app está em segundo plano). Dessa forma, seu aplicativo terá a chance de personalizar a experiência, por exemplo, exibindo elementos personalizados da interface do usuário na notificação entregue na bandeja de notificações. Embora a implementação do push dessa maneira possa não ser familiar para alguns, um de nossos recursos bem conhecidos no Braze, o [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), é um excelente exemplo do uso de componentes de exibição personalizados para criar uma experiência envolvente!

#### Solicitações

O Android impõe algumas limitações quanto aos componentes que podem ser usados para implementar exibições de notificação personalizadas. Os layouts de exibição de notificação devem conter _apenas_ objetos de exibição compatíveis com a estrutura [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).

### Notificações por push personalizadas

As notificações por push podem exibir informações específicas do usuário dentro de uma hierarquia de visualização personalizada. O exemplo a seguir mostra uma notificação por push após um usuário ter concluído uma tarefa específica (curso do Braze Learning) e agora é incentivado a expandir essa notificação para verificar seu progresso. As informações fornecidas aqui são específicas do usuário e podem ser disparadas quando uma sessão é concluída ou quando uma ação específica do usuário é realizada, aproveitando um disparo da API. 

![Exemplo de dashboard push personalizado]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### Configuração do dashboard

Para configurar um push personalizado no dashboard, você deve registrar a categoria específica que deseja exibir. Defina as atribuições de usuário apropriadas que deseja que a mensagem mostre nos pares de valores-chave usando o Liquid padrão. Essas visualizações podem ser personalizadas com base em atribuições específicas de um perfil de usuário específico.

![Exemplo de dashboard push personalizado]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### Pronto para fazer a análise de dados?
Visite a [seção a seguir](#logging-analytics) para entender melhor como deve ser o fluxo de dados.

## Análise de dados de registro

### Registro com a API do Braze (recomendado)

A análise de dados de registro só pode ser feita em tempo real com a ajuda do servidor do cliente que chega ao nosso [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Para análise de dados, envie o valor chave-valor `braze_id` (como visto na captura de tela a seguir) para identificar qual perfil de usuário deve ser atualizado.

![Exemplo de dashboard push personalizado]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### Registro manual 

O registro manual pode ser feito registrando os elementos que desejar, seja na implementação do `FirebaseMessagingService.onMessageReceived` ou na atividade de inicialização, com base nos extras presentes na carga útil. No entanto, uma advertência importante a ser lembrada é que a subclasse `FirebaseMessagingService` _deve_ terminar a execução em até 10 segundos após a invocação para evitar ser [sinalizada ou encerrada](https://firebase.google.com/docs/cloud-messaging/android/receive) pelo sistema Android. 


