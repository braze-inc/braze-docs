## Verificações básicas

#### Minha mensagem no app não foi exibida para um usuário

1. O usuário estava no segmento no início da sessão, quando o SDK solicita novas mensagens no app?
2. O usuário era elegível ou reelegível para receber a mensagem no app de acordo com as regras de direcionamento da campanha?
3. O usuário foi afetado por um limite de frequência?
4. O usuário estava em um grupo de controle? Verifique se sua campanha está configurada para testes AB.
5. Uma mensagem no app diferente e de prioridade mais alta foi exibida no lugar da mensagem esperada?
6. Meu dispositivo estava na orientação correta especificada pela campanha?
7. Minha mensagem foi suprimida pelo intervalo de tempo mínimo padrão de 30 segundos entre disparos, imposto pelo SDK?

#### Minha mensagem no app não foi exibida para todos os usuários nesta plataforma

1. Sua campanha está configurada para direcionamento a aplicativos móveis ou navegadores da Web, conforme apropriado? Por exemplo, se sua campanha tiver como alvo apenas navegadores da Web, ela não será enviada para dispositivos Android.
2. Você implementou uma interface de usuário personalizada e ela está funcionando como pretendido? Há outra manipulação ou supressão personalizada no lado do app que possa estar interferindo na exibição? 
3. Essa plataforma específica e essa versão do app já exibiram mensagens no app com êxito?
4. O disparo ocorreu localmente no dispositivo? Note que uma chamada REST não pode ser usada para disparar uma mensagem no app no SDK.

#### Minha mensagem no app não foi exibida para todos os usuários

1. A ação-gatilho foi configurada corretamente no dashboard, bem como na integração do app?
2. Uma mensagem no app diferente e de prioridade mais alta foi exibida no lugar da mensagem esperada?
3. Você está usando uma versão recente do SDK? Alguns tipos de mensagens no app têm requisitos de versão do SDK.
4. As sessões foram integradas corretamente em sua integração? A análise de dados da sessão está funcionando para esse app?

Para uma discussão mais aprofundada sobre esses cenários, visite [a seção de solução de problemas avançada](#troubleshooting-in-app-advanced).

## Problemas com impressões e análise de dados de cliques

{% if include.sdk == "iOS" %}
#### As impressões e os cliques não estão sendo registrados

Se você tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com ações de clique, deverá [registrar](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) manualmente [os cliques](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) e [as impressões](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) na mensagem no app.
{% elsif include.sdk == "Android" %}
#### As impressões e os cliques não estão sendo registrados
Se você tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com ações de clique, deverá registrar manualmente os cliques e as impressões na mensagem no app.
{% endif %}

#### As impressões são menores do que o esperado

Os disparos levam tempo para serem sincronizados com o dispositivo no início da sessão, portanto, pode haver uma condição de corrida se os usuários registrarem um evento ou uma compra logo após iniciarem uma sessão. Uma possível solução alternativa poderia ser alterar a campanha para disparar a partir do início da sessão e, em seguida, segmentar o evento ou a compra pretendida. Note que isso entregaria a mensagem no app no próximo início de sessão após a ocorrência do evento.

## Solução de problemas avançada {#troubleshooting-in-app-advanced}

A maioria dos problemas com mensagens no app pode ser dividida em duas categorias principais: entrega e exibição. Para solucionar o motivo pelo qual uma mensagem no app esperada não foi exibida em seu dispositivo, confirme se a [mensagem no app foi entregue ao dispositivo](#troubleshooting-in-app-message-delivery) e, em seguida, [solucione o problema da exibição da mensagem](#troubleshooting-in-app-message-display).

### Solução de problema de entrega de mensagens no app {#troubleshooting-in-app-message-delivery}

O SDK solicita mensagens no app dos servidores da Braze no início da sessão. Para verificar se as mensagens no app estão sendo entregues ao seu dispositivo, você precisará ter certeza de que as mensagens no app estão sendo solicitadas pelo SDK e retornadas pelos servidores Braze.

#### Verificar se as mensagens são solicitadas e retornadas

1. Adicione-se como um [usuário teste]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) no dashboard.
2. Configure uma campanha de mensagens no app direcionada ao seu usuário.
3. Confira se uma nova sessão está ocorrendo em seu aplicativo.
4. Use o [registro de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se o dispositivo está solicitando mensagens no app no início da sessão. Encontre a solicitação do SDK associada ao evento de início de sessão do usuário teste.
  - Se o seu app foi projetado para solicitar mensagens no app disparadas, você deverá ver `trigger` no campo **Respostas solicitadas** em **Dados de resposta**.
  - Se o seu app foi projetado para solicitar mensagens originais no app, você deverá ver `in_app` no campo **Respostas solicitadas** em **Dados de resposta**.
5. Use os registros de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se as mensagens no app corretas estão sendo retornadas nos dados de resposta.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Solução de problemas de mensagens que não estão sendo solicitadas

Se suas mensagens no app não estiverem sendo solicitadas, seu app pode não estar rastreando as sessões corretamente, pois as mensagens no app são atualizadas no início da sessão. Além disso, certifique-se de que o seu app esteja realmente iniciando uma sessão com base na semântica de tempo limite da sessão do seu app:

![A solicitação do SDK encontrada nos registros de usuários de eventos que exibem um evento de início de sessão bem-sucedido.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Solução de problemas de mensagens que não estão sendo retornadas

Se suas mensagens no app não estiverem sendo retornadas, é provável que haja um problema de direcionamento de campanha:

- Seu segmento não contém seu usuário.
  - Verifique a guia [\*\*Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) do seu usuário para ver se o segmento correto aparece em **Segments (Segmentos**).
- Seu usuário já recebeu anteriormente a mensagem no app e não era elegível para recebê-la novamente.
  - Verifique as [configurações de reelegibilidade da campanha]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) na etapa **Delivery (Entrega)** do **criador da campanha** e certifique-se de que as configurações de reelegibilidade estejam alinhadas com sua configuração de teste.
- Seu usuário atingiu o limite de frequência da campanha.
  - Verifique as configurações de limite de frequência da campanha]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) e certifique-se de que estejam alinhadas com sua configuração de teste.
- Se havia um grupo de controle na campanha, seu usuário pode ter caído no grupo de controle.
  - É possível verificar se isso aconteceu criando um segmento com um filtro de variante de campanha recebida, em que a variante de campanha está definida como **Controle**, e verificando se o usuário se enquadra nesse segmento.
  - Ao criar campanhas para fins de teste de integração, é importante não aceitar a adição de um grupo de controle.


### Solução de problema de exibição de mensagens no app {#troubleshooting-in-app-message-display}

Se o seu app estiver solicitando e recebendo mensagens no app com êxito, mas elas não estiverem sendo exibidas, a lógica do lado do dispositivo pode estar impedindo a exibição:

{% if include.sdk == "iOS" %}
- As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
{% elsif include.sdk == "Android" %}
- As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
{% elsif include.sdk == "Web" %}
- As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
{% endif %}
- A falha no download de imagens impedirá a exibição de mensagens no app com imagens. Verifique os registros do dispositivo para garantir que os downloads de imagens não estejam falhando.
{% case include.sdk %}
  {% when "iOS", "Android" %}
- Se tiver definido um delegado para personalizar o envio de mensagens no app, verifique se o delegado não está afetando a exibição de mensagens no app.
  {% when "Web" %}
- Se você tiver um `braze.subscribeToInAppMessage` ou `appboy.subscribeToNewInAppMessages` de manipulação de mensagens no app personalizado, verifique essa inscrição para garantir que não esteja afetando a exibição de mensagens no app.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
- Se a orientação do dispositivo não corresponder à orientação especificada pela mensagem no app, a mensagem no app não será exibida. Certifique-se de que o dispositivo esteja na orientação correta.
{% endcase %}