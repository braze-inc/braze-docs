---
nav_title: Solução de problemas
article_title: Solução de problemas de envio de mensagens no app para iOS
platform: iOS
page_order: 7
description: "Este artigo de referência aborda os possíveis tópicos de solução de problemas de mensagens no app do iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Envio de mensagens no app para solução de problemas

## Impressões

#### A análise de dados de impressões ou cliques não está sendo registrada

Se tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com as ações de clique, será necessário registrar manualmente os cliques e as impressões na mensagem no app.

#### As impressões são menores do que o esperado

Os disparos levam tempo para serem sincronizados com o dispositivo no início da sessão, portanto, pode haver uma condição de corrida se os usuários registrarem um evento ou uma compra logo após iniciarem uma sessão. Uma possível solução alternativa poderia ser alterar a campanha para disparar a partir do início da sessão e, em seguida, segmentar o evento ou a compra pretendida. Note que isso entregaria a mensagem no app no próximo início de sessão após a ocorrência do evento.

## A mensagem no app esperada não foi exibida

A maioria dos problemas com mensagens no app pode ser dividida em duas categorias principais: entrega e exibição. Para solucionar o problema de não exibição de uma mensagem no app esperada no dispositivo, primeiro certifique-se de que a [mensagem no app foi entregue ao dispositivo](#troubleshooting-in-app-message-delivery) e, em seguida, [solucione o problema de exibição da mensagem](#troubleshooting-in-app-message-display).

### Envio de mensagens no app {#troubleshooting-in-app-message-delivery}

O SDK solicita mensagens no app dos servidores da Braze no início da sessão. Para verificar se as mensagens no app estão sendo entregues ao seu dispositivo, você precisará garantir que as mensagens no app estejam sendo solicitadas pelo SDK e retornadas pelos servidores Braze.

#### Verificar se as mensagens são solicitadas e retornadas

1. Adicione-se como um [usuário teste]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) no dashboard.
2. Configure uma campanha de mensagens no app direcionada ao seu usuário.
3. Confira se uma nova sessão está ocorrendo em seu aplicativo.
4. Use o [registro de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se o dispositivo está solicitando mensagens no app no início da sessão. Encontre a solicitação do SDK associada ao evento de início de sessão do usuário teste.
  - Se o seu app foi projetado para solicitar mensagens no app disparadas, você deverá ver `trigger` no campo **Respostas solicitadas** em **Dados de resposta**.
  - Se o seu app foi projetado para solicitar mensagens originais no app, você deverá ver `in_app` no campo **Respostas solicitadas** em **Dados de resposta**.
5. Use os registros de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se as mensagens no app corretas estão sendo retornadas nos dados de resposta.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Solução de problemas de mensagens que não estão sendo solicitadas

Se suas mensagens no app não estiverem sendo solicitadas, seu app pode não estar rastreando as sessões corretamente, pois as mensagens no app são atualizadas no início da sessão. Além disso, certifique-se de que o seu app esteja realmente iniciando uma sessão com base na semântica de tempo limite da sessão do seu app:

![A solicitação do SDK encontrada nos registros de usuários de eventos que exibem um evento de início de sessão bem-sucedido.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Solução de problemas de mensagens que não estão sendo retornadas

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

### Exibição de mensagens no app {#troubleshooting-in-app-message-display}

Se o seu app estiver solicitando e recebendo mensagens no app com êxito, mas elas não estiverem sendo exibidas, alguma lógica do lado do dispositivo pode estar impedindo a exibição:

- As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
- Se tiver definido um delegado para personalizar o envio de mensagens no app, verifique se o delegado não está afetando a exibição de mensagens no app.
- A falha no download de imagens impedirá a exibição de mensagens no app com imagens. Os downloads de imagens sempre falharão se o framework `SDWebImage` não estiver integrado corretamente. Verifique os registros do dispositivo para garantir que os downloads de imagens não estejam falhando.
- Se a orientação do dispositivo não corresponder à orientação especificada pela mensagem no app, a mensagem no app não será exibida. Certifique-se de que o dispositivo esteja na orientação correta.


