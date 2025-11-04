---
nav_title: Envio de mensagens de teste
article_title: Envio de mensagens de teste
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Este artigo de referência aborda como enviar mensagens de teste pelos diferentes canais do Braze e como incorporar propriedades de eventos personalizados ou atributos de usuário."

---

# Envio de mensagens de teste

> Antes de enviar uma campanha de mensagens aos seus usuários, como prática recomendada, recomendamos fazer testes para garantir que ela tenha a aparência correta e funcione como pretendido. Você pode criar e enviar mensagens de teste para dispositivos ou membros da equipe selecionados usando as ferramentas no painel do Braze.

{% alert important %}
Certifique-se de salvar o rascunho da campanha após o teste para evitar a exclusão da campanha. Você pode enviar mensagens de teste sem salvar a mensagem como rascunho.
{% endalert %}

## Etapa 1: Identifique seus usuários de teste

Antes de testar sua campanha de mensagens, é importante identificar seus usuários de teste. Esses usuários podem ser IDs de usuário ou endereços de e-mail existentes ou novos usuários usados exclusivamente para testar campanhas de mensagens. 

### Opcional: Criar um grupo de teste de conteúdo

Uma maneira conveniente de organizar seus usuários de teste é criar um [Grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que inclui um grupo de usuários que receberão mensagens de teste das campanhas. Você pode adicionar esse grupo de teste ao campo **Adicionar grupos de teste de conteúdo** em **Destinatários de teste** na sua campanha e iniciar seus testes sem criar ou adicionar usuários de teste individuais.

## Etapa 2: Enviar mensagens de teste específicas do canal

Para saber as etapas de envio de mensagens de teste, consulte a seção a seguir para o seu respectivo canal.

{% tabs local %}
{% tab Email %}

1. Redija sua mensagem de e-mail.
2. Selecione **Preview and Test (Visualizar e testar**).
3. Selecione a guia **Test Send (Envio de teste** ) e adicione seu endereço de e-mail ou ID de usuário no campo **Add individual users (Adicionar usuários individuais** ). 
4. Selecione **Enviar teste** para enviar o e-mail rascunhado para sua caixa de entrada.

\![E-mail de teste]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Push móvel

1. Elabore seu push móvel.
2. Selecione a guia **Settings (Configurações** ) e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users (Adicionar usuários individuais** ).
3. Selecione **Enviar teste** para enviar a mensagem rascunhada para o dispositivo.

\![Test push]({% image_buster /assets/img_archive/testpush.png %})

#### Empurrar pela Web

1. Crie seu web push.
2. Selecione a guia **Teste**. 
3. Selecione **Send Test to Myself (Enviar teste para mim mesmo**).
4. Selecione **Send Test (Enviar teste** ) para enviar o push da Web para o navegador da Web.

\![Test web push]({% image_buster /assets/img_archive/testwebpush.png %})

Se você já tiver aceitado mensagens push do painel do Braze, o push aparecerá no canto da tela. Caso contrário, clique em **Permitir** quando solicitado, e a mensagem será exibida.

{% endtab %}
{% tab In-App Message %}

Se você tiver notificações push configuradas no aplicativo e no dispositivo de teste, poderá enviar mensagens in-app de teste para o aplicativo para ver como ele se comporta em tempo real. 

1. Redija sua mensagem no aplicativo.
2. Selecione a guia **Test (Teste** ) e adicione seu endereço de e-mail ou ID de usuário ao campo **Add Individual Users (Adicionar usuários individuais** ). 
3. Selecione **Send Test (Enviar teste** ) para enviar a mensagem push para o dispositivo.

Uma mensagem de envio de teste será exibida na parte superior da tela do dispositivo.

\![Teste no aplicativo]({% image_buster /assets/img_archive/test-in-app.png %})

Ao clicar diretamente e abrir a mensagem push, você será direcionado para o aplicativo, onde poderá visualizar o teste da mensagem in-app. Observe que esse recurso de teste de mensagem in-app depende de o usuário clicar em uma notificação push de teste para acionar a mensagem in-app. Dessa forma, o usuário deve estar qualificado para receber notificações push no aplicativo relevante para que a entrega da notificação push de teste seja bem-sucedida.

{% endtab %}
{% tab Content Card %}

Depois de criar seu Content Card, você pode enviar um Content Card de teste para seu aplicativo para ver como ele ficará em tempo real.

1. Elabore seu cartão de conteúdo.
2. Selecione a guia **Teste** e selecione pelo menos um Grupo de teste de conteúdo ou usuário individual para receber essa mensagem de teste. 
3. Selecione **Enviar teste** para enviar seu Content Card para o aplicativo.

Cartão de conteúdo de teste]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Depois de criar sua mensagem SMS ou MMS, você pode enviar uma mensagem de teste para o seu telefone para ver como ela ficará em tempo real. 

1. Rascunhe sua mensagem SMS ou MMS.
2. Selecione a guia **Teste** e selecione pelo menos um Grupo de teste de conteúdo ou usuário individual para receber essa mensagem de teste. 
3. Selecione **Send Test (Enviar teste** ) para enviar sua mensagem de teste.

Cartão de conteúdo de teste]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Depois de criar seu webhook, você pode fazer um envio de teste para verificar a resposta do webhook. Selecione a guia **Test (Teste** ) e selecione **Send Test (Enviar teste** ) para enviar um teste para o URL do webhook fornecido. Também é possível selecionar um usuário individual para visualizar a resposta como um usuário específico. 

Cartão de conteúdo de teste]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% endtabs %}

## Teste de campanhas personalizadas 

Se estiver testando campanhas que preencham dados do usuário ou usem propriedades de eventos personalizados, será necessário executar etapas adicionais ou diferentes.

### Teste de campanhas personalizadas com atributos do usuário

Se estiver usando [personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) em sua mensagem, será necessário tomar medidas adicionais para visualizar adequadamente sua campanha e verificar se os dados do usuário estão preenchendo adequadamente o conteúdo.

Ao enviar uma mensagem de teste, certifique-se de escolher a opção **Selecionar usuário existente** ou visualizar como um **usuário personalizado**.

\![Testando uma mensagem personalizada]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleção de um usuário existente

Se estiver selecionando um usuário existente, digite o ID ou o e-mail do usuário específico no campo de pesquisa. Em seguida, use a visualização do painel para ver como sua mensagem apareceria para esse usuário e envie uma mensagem de teste para seu dispositivo que reflita o que esse usuário veria.

\![Selecione um usuário]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleção de um usuário personalizado

Se estiver visualizando como um usuário personalizado, insira texto para vários campos disponíveis para personalização, como o primeiro nome do usuário e quaisquer atributos personalizados. Mais uma vez, você pode inserir seu próprio endereço de e-mail para enviar um teste ao seu dispositivo.

\![Usuário personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

### Teste de campanhas personalizadas com propriedades de eventos personalizados

O teste de campanhas personalizadas com [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) é um pouco diferente do teste de outros tipos de campanhas descritas. 

{% tabs local %}
{% tab Trigger manually %}

#### Método 1: Acionamento manual da campanha

Você mesmo pode acionar a campanha como uma forma robusta de testar campanhas personalizadas usando propriedades de eventos personalizados:

1. Escreva a cópia envolvendo a propriedade do evento. 

\![Composição de mensagem de teste com propriedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2\. Use [a entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para entregar a campanha quando o evento ocorrer.

{% alert note %}
Se estiver testando uma campanha push para iOS, defina o atraso para um minuto para ter tempo de sair do aplicativo, pois o iOS não envia notificações push para o aplicativo aberto no momento. Outros tipos de campanhas podem ser definidos para entrega imediata.
{% endalert %}

Entrega de mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Direcione os usuários como faria para o teste, usando um filtro de teste ou direcionando seu próprio endereço de e-mail, e termine de criar a campanha. 

Teste de direcionamento de mensagens]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Entre em seu aplicativo e conclua o evento personalizado.

A campanha será acionada e mostrará a mensagem personalizada com a propriedade de evento.

\![Exemplo de mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Método 2: Enviar uma mensagem de teste para você mesmo

Como alternativa, se você estiver salvando IDs de usuário personalizados, também poderá testar a campanha enviando uma mensagem de teste personalizada para si mesmo.

1. Escreva o texto de sua campanha.
2. Selecione a guia **Teste** e escolha **Usuário personalizado**. 
3. Adicione a propriedade de evento personalizado na parte inferior da página e adicione seu ID de usuário ou endereço de e-mail à caixa superior.
4. Selecione **Enviar teste** para receber uma mensagem personalizada com a propriedade.

Testes com usuários personalizados]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Usando líquido

Você pode testar as propriedades de eventos personalizados inserindo valores manualmente com o Liquid. 

1. No editor de mensagens, insira valores para suas propriedades de evento personalizadas.
2. Selecione a guia **Preview as a User (Visualizar como usuário** ) para verificar se a mensagem correta é exibida.

{% endtab %}
{% endtabs %}

## Solução de problemas

### Mensagens no aplicativo

Se a sua campanha de mensagem in-app não for acionada por uma campanha push, verifique a segmentação da campanha in-app para confirmar se o usuário atende ao público-alvo **antes de** receber a mensagem push.

Para envios de teste no Android e no iOS, as mensagens no aplicativo que usam o comportamento **Solicitar permissão de envio** no clique podem não ser exibidas em alguns dispositivos. Como solução alternativa:
- **Android:** Os dispositivos devem ter o Android 13 e o nosso Android SDK versão 21.0.0. Outro motivo pode ser o fato de o dispositivo no qual a mensagem no aplicativo é exibida já ter um prompt no nível do sistema. Talvez você tenha selecionado a opção **Não perguntar novamente**, portanto, talvez seja necessário reinstalar o aplicativo para redefinir as permissões de notificação antes de testar novamente.
- **iOS:** Recomendamos que a sua equipe de desenvolvedores revise a implementação de notificações push para o seu aplicativo e remova manualmente qualquer código que solicite permissões push. Para obter mais informações, consulte [Mensagens in-app do primer Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Para que uma campanha de mensagem in-app baseada em ação seja entregue, os eventos personalizados devem ser registrados por meio do Braze SDK, e não das APIs REST, para que o usuário possa receber mensagens in-app qualificadas diretamente em seu dispositivo. Os usuários podem receber a mensagem in-app se realizarem o evento durante a sessão.
