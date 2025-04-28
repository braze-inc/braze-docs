{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Layout de notificação personalizado

As notificações do Braze são enviadas como [mensagens de dados](https://firebase.google.com/docs/cloud-messaging/concept-options), o que significa que seu aplicativo sempre terá a chance de responder e executar o comportamento de acordo, mesmo em segundo plano (em contraste com as mensagens de notificação, que podem ser tratadas automaticamente pelo sistema quando seu app está em segundo plano). Dessa forma, seu aplicativo terá a chance de personalizar a experiência, por exemplo, exibindo elementos personalizados da interface do usuário na notificação entregue na bandeja de notificações. Embora a implementação do push dessa maneira possa não ser familiar para alguns, um de nossos recursos bem conhecidos no Braze, o [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), é um excelente exemplo do uso de componentes de exibição personalizados para criar uma experiência envolvente!

{% alert important %}
O Android impõe algumas limitações quanto aos componentes que podem ser usados para implementar exibições de notificação personalizadas. Os layouts de exibição de notificação devem conter _apenas_ objetos de exibição compatíveis com a estrutura [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).
{% endalert %}

## Notificações por push personalizadas

As notificações por push podem exibir informações específicas do usuário dentro de uma hierarquia de visualização personalizada. No exemplo a seguir, um disparador de API é usado para enviar notificações por push personalizadas a um usuário para que ele possa verificar seu progresso atual depois de concluir uma tarefa específica no app.

![Exemplo de dashboard push personalizado]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Para configurar um push personalizado no dashboard, registre a categoria específica que deseja exibir e, em seguida, defina quaisquer atribuições de usuário relevantes que gostaria de exibir usando o Liquid.

![Exemplo de dashboard push personalizado]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
