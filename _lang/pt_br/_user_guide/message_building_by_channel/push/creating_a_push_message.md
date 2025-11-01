---
nav_title: "Criação de uma mensagem push"
article_title: Criação de uma campanha push
page_order: 4
page_type: tutorial
description: "Esta página de tutorial aborda os diferentes componentes envolvidos na criação de uma mensagem push, incluindo configuração, envio, direcionamento e muito mais."
channel: push
tool:
  - Campaigns
  
---

# Criação de uma mensagem push

> As notificações por push são excelentes para chamadas à ação sensíveis ao tempo, bem como para reengajar usuários que não acessam o aplicativo há algum tempo. Campanhas push bem-sucedidas levam o usuário diretamente ao conteúdo e demonstram o valor do seu aplicativo. Para ver exemplos de notificações por push, confira nossos [estudos de caso](https://www.braze.com/customers).

## Etapa 1: Escolha onde construir sua mensagem {#create-new-campaign-push}

{% alert tip %}
Não tem certeza se deve usar uma campanha ou um Canvas? As campanhas são melhores para campanhas de mensagens simples e únicas, enquanto os Canvases são melhores para jornadas de usuários em várias etapas.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Acesse **Messaging** > **Campaigns**( **Mensagens** > **Campanhas**) e selecione **Create campaign (Criar campanha**).
2. Para campanhas direcionadas a vários canais, selecione **Multicanal**. Caso contrário, selecione **Notificação por push**. Se ainda não tiver certeza, consulte a seção **Decidir entre uma campanha push regular ou multicanal** abaixo.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário. 

{% alert tip %}
As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
{% endalert %}

{: start="5"}
5\. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Deciding between regular or multichannel push campaign %}

Se você pretende segmentar vários dispositivos e plataformas, como qualquer combinação de celular, Web, Kindle, iOS e Android, sua seleção nesta etapa pode afetar a disponibilidade de alguns recursos e configurações posteriormente.

Consulte o gráfico de decisão a seguir antes de criar uma campanha multicanal ou de notificação por push:

\!["Fluxograma para selecionar o tipo de campanha. Comece decidindo se você está segmentando vários dispositivos e plataformas. Em caso negativo, será exibida a opção "Select Push Notification". Se sim, ele pergunta "Que tipo de mensagem push?" e as opções são "Push padrão", levando a um ponto de decisão "Você precisa usar configurações específicas do dispositivo?". Se a resposta for negativa, será exibida a mensagem 'Select Push Notification and use quick push'. Se sim, ele vai para "Select Multichannel" (Selecionar multicanal). De volta a "Que tipo de mensagem push?", se a resposta for "Push Stories ou Inline image", ele direcionará para "Select Multichannel".]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Se você selecionar **Push Notification** e optar por segmentar vários dispositivos e plataformas, estará criando automaticamente uma campanha de envio rápido. Com o envio rápido, algumas configurações específicas do dispositivo não estão disponíveis:

- Botões de ação
- Canais e grupos de notificação
- Tempo de vida do push (TTL)
- Prioridade de exibição
- Sons

Antes de continuar, consulte [as campanhas Quick push]({{site.baseurl}}/quick_push) para entender o que há de diferente nessa experiência de edição.

{% enddetails %}

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar outras variantes. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor do Canvas. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique um atraso conforme necessário.
4. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e acrescentando filtros adicionais. As opções de público serão verificadas após o atraso no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de mensagens que você gostaria de associar à sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Selecionar plataformas push

Em seguida, escolha qual combinação de plataforma e dispositivo móvel deve receber o push. Use essa seleção para limitar a entrega de uma notificação por push a um conjunto específico de aplicativos.

Há algumas maneiras diferentes de fazer isso, dependendo de suas seleções anteriores:

| Seleção anterior | Opções |
| --- | --- | 
| Campanha de notificação por push | Selecione uma ou mais plataformas e dispositivos. Se você optar por segmentar vários dispositivos e plataformas, estará criando automaticamente uma campanha de envio rápido. Isso proporciona uma experiência de edição otimizada para a elaboração de uma mensagem para todas as plataformas selecionadas em um único editor. Consulte [Campanhas de envio rápido]({{site.baseurl}}/quick_push) para entender o que há de diferente nessa experiência de edição. |
| Campanha multicanal | Selecione **Add Messaging Channel (Adicionar canal de mensagens** ) para adicionar plataformas push adicionais. Como as seleções de plataforma são específicas para cada variante, você pode tentar testar o envolvimento da mensagem por plataforma.
| Tela | Na etapa Mensagem, selecione **\+ Adicionar mais** para adicionar plataformas push adicionais. Semelhante às campanhas multicanal, as seleções de plataforma são específicas para cada variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Selecione o tipo de notificação (iOS e Android)

Se você estiver criando uma campanha de envio rápido, o tipo de notificação será automaticamente definido como **envio padrão** e não poderá ser alterado.

Tipo de notificação com Push padrão selecionado como exemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Caso contrário, para iOS e Android, selecione seu tipo de notificação:

- Empurrar padrão
- [Histórias de sucesso]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Imagem em linha (somente Android)

Se quiser incluir imagens em sua campanha push, consulte os guias a seguir sobre como criar uma notificação avançada para [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Etapa 4: Componha sua mensagem push

Agora é hora de escrever sua mensagem de envio! A guia **Compose** permite que você edite todos os aspectos do conteúdo e do comportamento da sua mensagem.

\![Guia Compose (Composição) para criar uma notificação por push.]({% image_buster /assets/img_archive/push_compose.png %})

O conteúdo da guia **Compose** varia de acordo com o tipo de notificação escolhido na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

#### Canal ou grupo de notificações (iOS e Android)

Para obter mais informações sobre as opções de notificação específicas da plataforma, consulte [Opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) ou [Opções de notificação do Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Idioma

Adicione cópia em vários idiomas usando o botão **Add Languages (Adicionar idiomas** ). Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto onde ele pertence no Liquid. Para ver a lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Se estiver adicionando uma cópia em um idioma escrito da direita para a esquerda, observe que a aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviços as processam. Para obter práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e corpo

{% tabs local %}
{% tab ios %}
Comece a digitar na caixa de mensagem e veja uma visualização aparecer na caixa de visualização à esquerda. As mensagens push devem ser formatadas em texto simples. 

Adicione um título usando o campo **Título**. Para tornar seu push personalizado e direcionado, você pode incluir [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab android %}
Comece a digitar na caixa de mensagem e veja uma visualização aparecer na caixa de visualização à esquerda. As mensagens push devem ser formatadas em texto simples. 

Para tornar seu push personalizado e direcionado, você pode incluir [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
**Não é possível** enviar uma mensagem push do Android sem um título; no entanto, em vez disso, você pode inserir um único espaço. Lembre-se de que, se sua mensagem contiver apenas um espaço, ela será enviada como uma notificação push silenciosa. Para obter mais informações, consulte [Notificações push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Tente usar o [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará um texto de marketing semelhante ao humano para ser usado em suas mensagens.

Botão Launch AI Copywriter, localizado no campo Body (Corpo) do compositor push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Imagem

Quando suportado, o ícone do aplicativo é adicionado automaticamente como a imagem da notificação por push. Você também tem a opção de enviar notificações avançadas, que permitem mais personalização em suas notificações push, acrescentando conteúdo adicional além do texto.

Para obter mais orientações sobre o uso de imagens em suas notificações por push, consulte os artigos a seguir:

- [Criar notificações avançadas para iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Criar notificações avançadas para Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportamento no clique

Especifique o que acontece quando um usuário seleciona o corpo de uma notificação por push com o **On-Click Behavior**. Por exemplo, você pode solicitar que os clientes abram seu aplicativo, redirecionar os clientes para um URL da Web especificado ou até mesmo abrir uma página específica do seu aplicativo com um [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Aqui, você também pode configurar avisos de botão na notificação por push, como, por exemplo

- Aceitar/Recusar
- Sim/Não
- Confirmar/Cancelar
- Mais informações 

#### Opções de envio

Se um usuário tiver seu aplicativo instalado em vários dispositivos, por padrão, sua mensagem push será enviada a todos os dispositivos com um token push válido atribuído. Se desejar, você pode selecionar **o dispositivo usado mais recentemente**.

Caixa de seleção Device options (Opções de dispositivo) para enviar esse push apenas para o dispositivo usado mais recentemente pelo usuário.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Há algumas nuances para essa configuração. Se essa opção for selecionada, o Braze limitará a ocorrência de vários envios, exceto quando uma campanha tiver como alvo várias plataformas, como iOS e Android. Se o usuário tiver seu aplicativo em um dispositivo iOS e Android, ele receberá um push para ambas as plataformas. Se o dispositivo usado mais recentemente por um usuário não estiver [habilitado para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled), a mensagem não será enviada.

No iOS, você pode limitar ainda mais o envio de mensagens enviando notificações push somente para dispositivos iPad ou somente para dispositivos iPhone e iPod.

## Etapa 5: Visualize e teste sua mensagem (opcional)

O teste é, sem dúvida, uma das etapas mais importantes. Depois de terminar de compor sua mensagem push perfeita, teste-a antes de enviá-la. Selecione a guia **Teste** para escolher entre as opções de como testar sua mensagem push. Em **Test Recipients (Destinatários do teste**), é possível selecionar um grupo de teste de conteúdo ou usuários individuais. Você também pode usar **Preview message as user (Visualizar mensagem como usuário** ) para ter uma ideia de como sua mensagem pode ser exibida no celular para um usuário aleatório, um usuário existente, um usuário personalizado ou um usuário multilíngue.

## Etapa 6: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Crie o restante da sua campanha; consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar notificações por push.

#### Escolha o cronograma de entrega ou o acionador

As mensagens push podem ser entregues com base em um horário programado, em uma ação ou em um acionador de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para a entrega baseada em ação, você também pode definir a duração da campanha e o [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem alvos

Em seguida, você precisa [segmentar os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente uma prévia de como é a população desse segmento aproximado no momento. As estatísticas detalhadas do público-alvo para os canais visados por sua campanha estão disponíveis no rodapé. Para ver qual porcentagem da sua base de usuários está sendo direcionada e o Lifetime Value desse segmento, selecione **Show Additional Stats (Mostrar estatísticas adicionais**).

{% multi_lang_include target_audiences.md %}

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

Ao visualizar o Total Reachable Users (Total de usuários alcançáveis) para o seu público filtrado, você poderá notar que a soma das colunas individuais é menor do que o Total Reachable Users (Total de usuários alcançáveis). Essa lacuna geralmente ocorre porque há vários usuários que se qualificam para o segmento ou filtros na campanha, mas não podem ser alcançados por push (por exemplo, porque não têm [tokens de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) válidos ou ativos).

{% enddetails %}

\![Tabela de estatísticas detalhadas de audiência para usuários alcançáveis.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

Você também pode optar por enviar sua campanha apenas para usuários que tenham um [status de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como aqueles que se inscreveram e optaram por receber o push.

Opcionalmente, você também pode limitar a entrega a um número especificado de usuários dentro do segmento ou permitir que os usuários recebam a mesma mensagem duas vezes em uma recorrência da campanha.

##### Campanhas multicanal com e-mail e push

Para campanhas multicanal direcionadas a canais de e-mail e push, talvez você queira limitar sua campanha de modo que somente os usuários que tenham optado explicitamente por receber a mensagem (excluindo usuários inscritos ou não inscritos). Por exemplo, digamos que você tenha três usuários com status de opt-in diferentes:

- **O usuário A** está inscrito no e-mail e está habilitado para push. Esse usuário não recebe o e-mail, mas receberá o push.
- **O usuário B** optou por receber e-mail, mas não está habilitado para push. Esse usuário receberá o e-mail, mas não receberá o push.
- **O usuário C** optou por receber e-mail e está habilitado para envio. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, em **Audience Summary (Resumo do público**), selecione para enviar essa campanha apenas para "usuários opt-in". Essa opção garantirá que apenas os usuários opt-in recebam seu e-mail, e o Braze enviará seu push apenas para os usuários que têm o push ativado por padrão.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Target Audiences** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canvas. Para obter mais detalhes sobre como criar o restante do seu Canvas, implementar testes multivariados e Intelligent Selection e muito mais, consulte a etapa [Criar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 7: Revisão e implementação {#review-and-deploy-push}

Depois de concluir a criação da última campanha ou Canvas, revise seus detalhes. Para campanhas, a página final fornecerá um resumo da campanha que você acabou de criar. Confirme todos os detalhes relevantes, certifique-se de ter testado sua mensagem, envie-a e veja os dados chegarem!

Em seguida, confira [Relatórios de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para saber como acessar os resultados de sua campanha de push. Para notificações por push, você poderá visualizar as estatísticas do número de mensagens enviadas, entregues, devolvidas, abertas e abertas diretamente.

