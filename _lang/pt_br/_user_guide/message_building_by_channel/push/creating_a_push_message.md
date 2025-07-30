---
nav_title: "Como criar uma mensagem de push"
article_title: Criação de uma campanha push
page_order: 4
page_type: tutorial
description: "Esta página de tutorial aborda os diferentes componentes envolvidos na criação de uma mensagem push, incluindo configuração, envio de mensagens, direcionamento e muito mais."
channel: push
tool:
  - Campaigns
  
---

# Criação de uma mensagem push

> As notificações por push são excelentes para chamadas à ação sensíveis ao tempo, bem como para o reengajamento de usuários que não acessam o app há algum tempo. Campanhas push bem-sucedidas levam o usuário diretamente ao conteúdo e demonstram o valor do seu app. Para ver exemplos de notificações por push, confira nossos [estudos de caso](https://www.braze.com/customers).

## Etapa 1: Escolha onde construir sua mensagem {#create-new-campaign-push}

{% alert tip %}
Não tem certeza se deve usar uma campanha ou um Canva? As campanhas são melhores para campanhas simples e de envio de mensagens únicas, enquanto as canvas são melhores para jornadas de usuário de várias etapas.
{% endalert %}

{% tabs %}
{% tab Campanha %}
1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Para campanhas com direcionamento para vários canais, selecione **Multicanal**. Caso contrário, selecione **Notificação por push**. Se ainda não tiver certeza, consulte a seção **Decidir entre uma campanha push regular ou multicanal** abaixo.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário. 

{% alert tip %}
As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
{% endalert %}

{: start="5"}
5\. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Decidir entre uma campanha push regular ou multicanal %}

Se você pretende direcionar vários dispositivos e plataformas, como qualquer combinação de celular, Web, Kindle, iOS e Android, sua seleção nessa etapa pode afetar a disponibilidade de alguns recursos e configurações posteriormente.

Consulte o gráfico de decisão a seguir antes de criar uma campanha multicanal ou de notificação por push:

!["Fluxograma para selecionar o tipo de campanha. Comece decidindo se está direcionando para vários dispositivos e plataformas. Em caso negativo, será exibida a mensagem "Selecionar notificação por push". Em caso positivo, ele pergunta "Que tipo de mensagem por push?" e as opções são "Push padrão", levando a uma decisão "Você precisa usar configurações específicas do dispositivo?". Se a resposta for negativa, será exibida a mensagem 'Select Push Notification and use quick push'. Em caso positivo, você verá a opção "Selecionar multicanal". De volta a "Que tipo de mensagem por push?", se a resposta for "Stories por push" ou "Imagem inline", ele direciona para "Selecionar Multicanal"]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Se você selecionar **Notificação por push** e optar pelo direcionamento para vários dispositivos e plataformas, estará criando automaticamente uma campanha de push rápido. Certas configurações específicas do dispositivo não estão disponíveis com o quick push: 

- Botões de ação por push
- Canais e grupos de notificação
- Push time-to-live (TTL)
- Prioridade de exibição
- Sons

Antes de continuar, consulte [as campanhas Quick push]({{site.baseurl}}/quick_push) para entender o que há de diferente nessa experiência de edição.

{% enddetails %}

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canva %}
1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário.
4. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de envio de mensagens que gostaria de associar à sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Selecione plataformas push

Em seguida, escolha qual combinação de plataforma e dispositivo móvel deve receber o push. Use essa seleção para limitar a entrega de uma notificação por push a um conjunto específico de aplicativos.

Há algumas maneiras diferentes de fazer isso, dependendo de suas seleções anteriores:

| Seleção anterior | Opções |
| --- | --- | 
| Campanha de notificação por push | Selecione uma ou mais plataformas e dispositivos. Se optar pelo direcionamento para vários dispositivos e plataformas, estará criando automaticamente uma campanha de push rápido. Isso proporciona uma experiência de mensagens otimizada para o envio de mensagens para todas as plataformas selecionadas em um único editor. Consulte [Campanhas push rápidas]({{site.baseurl}}/quick_push) para entender o que há de diferente nessa experiência de edição. |
| Campanha multicanal | Selecione **Adicionar canal de envio de mensagens** para adicionar plataformas push adicionais. Como as seleções de plataforma são específicas para cada variante, você pode tentar testar o engajamento com mensagens por plataforma.
| Canva | Em sua etapa de Mensagem, selecione **\+ Adicionar mais** para adicionar plataformas push adicionais. Semelhante às campanhas multicanal, as seleções de plataforma são específicas para cada variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Selecione o tipo de notificação (iOS e Android)

Se estiver criando uma campanha de push rápido, o tipo de notificação será automaticamente definido como **Standard push** e não poderá ser alterado.

![Tipo de notificação com Push padrão selecionado como exemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Caso contrário, para iOS e Android, selecione seu tipo de notificação:

- Push padrão
- [Stories por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Imagem em linha (somente Android)

Se quiser incluir imagens em sua campanha push, consulte os guias a seguir sobre como criar uma notificação por push para [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Etapa 4: Crie sua mensagem push

Agora é hora de escrever sua mensagem push! A guia **Criador de** mensagem permite que você edite todos os aspectos do conteúdo e do comportamento da sua mensagem.

![Guia de criação de uma notificação por push.]({% image_buster /assets/img_archive/push_compose.png %})

O conteúdo da guia **Criador** varia de acordo com o tipo de notificação escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

#### Canal ou grupo de notificações (iOS e Android)

Para saber mais sobre as opções de notificação específicas da plataforma, consulte [Opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) ou [Opções de notificação do Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Idioma

Adicione textos em vários idiomas usando o botão **Adicionar idiomas**. Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que possa preencher o texto onde ele pertence no Liquid. Para nossa lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Se estiver adicionando cópia em um idioma escrito da direita para a esquerda, note que a aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre o envio de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e corpo

{% tabs local %}
{% tab ios %}
Comece a digitar na caixa de mensagem e veja uma prévia na caixa de visualização à esquerda. As mensagens push devem ser formatadas em texto simples. 

Adicione um título usando o campo **Título**. Para tornar seu push personalizado e direcionado, você pode incluir o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab Android %}
Comece a digitar na caixa de mensagem e veja uma prévia na caixa de visualização à esquerda. As mensagens push devem ser formatadas em texto simples. 

Para tornar seu push personalizado e direcionado, você pode incluir o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
**Não é possível** enviar uma mensagem push do Android sem um título; no entanto, você pode inserir um único espaço. Lembre-se de que, se sua mensagem contiver apenas um espaço, ela será enviada como uma notificação por push silenciosa. Para saber mais, consulte [Notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Inicie o botão AI Copywriter, localizado no campo "Corpo" do criador do push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Imagem

Quando suportado, o ícone do seu app é automaticamente adicionado como a imagem da notificação por push. Você também tem a opção de enviar notificações Rich, que permitem mais personalização em suas notificações por push, acrescentando conteúdo adicional além da cópia.

Para obter mais orientações sobre o uso de imagens em suas notificações por push, consulte os artigos a seguir:

- [Crie notificações Rich para iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Crie notificações Rich para Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportamento ao clicar

Especifique o que acontece quando um usuário seleciona o corpo de uma notificação por push com o **comportamento ao clicar**. Por exemplo, você pode solicitar que os clientes abram o aplicativo, redirecionar os clientes para um URL da Web especificado ou até mesmo abrir uma página específica do aplicativo com um [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Aqui, você também pode configurar avisos de botão na notificação por push, como, por exemplo

- Aceitar/Recusar
- Sim/Não
- Confirmar/Cancelar
- Mais 

#### Opções de envio

Se um usuário tiver seu app instalado em vários dispositivos, por padrão, sua mensagem no app será enviada a todos os dispositivos com um token push válido atribuído. Se desejar, você pode selecionar **o dispositivo usado mais recentemente**.

![Caixa de seleção das opções do dispositivo para enviar esse push apenas para o dispositivo usado mais recentemente pelo usuário.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Há algumas nuances para essa configuração. Se essa opção for selecionada, a Braze limitará a ocorrência de vários envios, exceto quando uma campanha direcionar para várias plataformas, como iOS e Android. Se o usuário tiver seu app em um dispositivo iOS e Android, ele receberá um push para ambas as plataformas. Se o dispositivo usado mais recentemente por um usuário não estiver [ativado para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled), a mensagem não será enviada.

No iOS, você pode limitar ainda mais o envio de mensagens enviando notificações por push somente para dispositivos iPad ou somente para dispositivos iPhone e iPod.

## Etapa 5: Pré-visualize e teste sua mensagem (opcional)

O teste é, sem dúvida, uma das etapas mais críticas. Depois de terminar de criar sua mensagem push perfeita, teste-a antes de enviá-la. Selecione a guia **Teste** para escolher entre as opções de como testar sua mensagem push. Em **Test Recipients (Destinatários do teste**), é possível selecionar um grupo de teste de conteúdo ou usuários individuais. Também é possível usar **Pré-visualizar mensagem como usuário** para ter uma ideia de como sua mensagem pode ser exibida no celular para um usuário aleatório, um usuário existente, um usuário personalizado ou um usuário multilíngue.

## Etapa 6: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}

Crie o restante da sua campanha; consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar notificações por push.

#### Escolha a programação ou o disparo da entrega

As mensagens por push podem ser enviadas com base em um horário programado, em uma ação ou em um disparo da API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem direcionados

Em seguida, é necessário direcionar [os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Estatísticas detalhadas do público para os canais direcionados por sua campanha estão disponíveis no rodapé. Para ver qual porcentagem da sua base de usuários está sendo direcionada e o valor do tempo de vida desse segmento, selecione **Show Additional Stats (Mostrar estatísticas adicionais)**.

{% details Por que minha métrica Total Reachable Users não corresponde à soma de todos os canais? %}

Ao visualizar o "Total de usuários contatáveis" do público filtrado, você poderá notar que a soma das colunas individuais é menor do que esse total. Essa lacuna geralmente ocorre porque há vários usuários que se qualificam para o segmento ou filtros na campanha, mas não podem ser alcançados por push (por exemplo, porque não têm [tokens por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) válidos ou ativos).

{% enddetails %}

![Tabela de estatísticas detalhadas do público para usuários acessíveis.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

Também é possível optar por enviar a campanha apenas para usuários que tenham um [status de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como aqueles que se inscreveram e aceitaram o push.

Opcionalmente, também é possível limitar a entrega a um número especificado de usuários dentro do segmento ou permitir que os usuários recebam a mesma mensagem duas vezes em caso de recorrência da campanha.

##### Campanhas multicanal com envio de e-mail e push

Para campanhas em vários canais direcionadas tanto para e-mail quanto para canais de envio de mensagens, talvez você queira limitar sua campanha para que somente os usuários com aceitação explícita recebam a mensagem (excluindo usuários inscritos ou cancelados). Por exemplo, digamos que você tenha três usuários com diferentes status de aceitação:

- **O usuário A** está inscrito no e-mail e tem a capacitação push ativada. Esse usuário não recebe o e-mail, mas receberá o push.
- O **usuário B** tem aceitação de e-mail, mas não tem a capacitação push ativada. Esse usuário receberá o e-mail, mas não receberá o push.
- O **usuário C** tem aceitação de e-mail e está ativado para push. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, em **Resumo do público**, selecione enviar essa campanha apenas para "usuários com aceitação". Essa opção garantirá que apenas os usuários com aceitação receberão seu e-mail, e o Braze enviará seu push apenas para os usuários que estiverem ativados para push por padrão.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Target Audiences (Públicos-alvo** ) que limite o público a um único canal (por exemplo, `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 7: Revisão e implementação {#review-and-deploy-push}

Depois de terminar de criar a última campanha ou Canva, revise seus detalhes. Para campanhas, a página final fornecerá um resumo da campanha que você acabou de criar. Confirme todos os detalhes relevantes, certifique-se de ter testado sua mensagem, envie-a e veja os dados chegarem!

Em seguida, confira [Relatórios push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para saber como acessar os resultados de sua campanha push. Para notificações por push, você poderá visualizar as estatísticas do número de mensagens enviadas, entregues, devolvidas, abertas e abertas diretamente.

