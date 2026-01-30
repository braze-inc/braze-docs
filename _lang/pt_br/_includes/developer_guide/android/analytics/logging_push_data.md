## Registro de dados com a API do Braze (recomendado)

É possível registrar análises de dados em tempo real fazendo chamadas para o [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Para análise de dados, envie o valor `braze_id` do dashboard do Braze para identificar qual perfil de usuário deve ser atualizado.

![Exemplo de dashboard push personalizado]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Registro manual de dados

Dependendo dos detalhes da carga útil, é possível registrar a análise de dados manualmente na implementação do `FirebaseMessagingService.onMessageReceived` ou na atividade de inicialização. Lembre-se de que sua subclasse `FirebaseMessagingService` deve terminar a execução em até 9 segundos após a invocação para evitar ser [sinalizada ou encerrada](https://firebase.google.com/docs/cloud-messaging/android/receive) pelo sistema Android.
