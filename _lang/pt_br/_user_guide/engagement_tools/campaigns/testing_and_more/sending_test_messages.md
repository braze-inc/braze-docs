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

> Antes de enviar uma campanha de mensagens para os usuários, como prática recomendada, recomendamos que sejam feitos testes para garantir que a campanha tenha a aparência correta e funcione como pretendido. É possível criar e enviar mensagens de teste para dispositivos ou membros da equipe selecionados usando as ferramentas do dashboard do Braze.

{% alert important %}
Certifique-se de salvar o rascunho da campanha após o teste para evitar a exclusão da campanha. Você pode enviar mensagens de teste sem salvar a mensagem como rascunho.
{% endalert %}

## Etapa 1: Identifique seus usuários de teste

Antes de testar a campanha de mensagens, é importante identificar os usuários de teste. Esses usuários podem ser IDs de usuário ou endereços de e-mail existentes ou novos usuários usados exclusivamente para testar campanhas de mensagens. 

### Opcional: Criar um grupo de teste de conteúdo

Uma maneira conveniente de organizar seus usuários de teste é criar um [Grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que inclui um grupo de usuários que receberão mensagens de teste das campanhas. Você pode adicionar esse grupo de teste no campo **Adicionar grupos de teste de conteúdo** em **Destinatários de teste** na sua campanha e iniciar seus testes sem criar ou adicionar usuários de teste individuais.

## Etapa 2: Enviar mensagens de teste específicas do canal

Para saber as etapas de envio de mensagens de teste, consulte a seção a seguir para seu respectivo canal.

{% tabs %}
{% tab E-mail %}

1. Rascunhe sua mensagem de e-mail.
2. Clique em **Pré-visualização e teste**.
3. Selecione a guia **Test Send (Envio de teste** ) e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users (Adicionar usuários individuais** ). 
4. Clique em **Enviar teste** para enviar o e-mail rascunhado para sua caixa de entrada.

![Teste o envio de e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Push móvel

1. Elabore seu push móvel.
2. Selecione a guia **Settings (Configurações)** e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users (Adicionar usuários individuais** ).
3. Clique em **Enviar teste** para enviar a mensagem rascunhada para o dispositivo.

![Teste o push]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

1. Crie seu web push.
2. Selecione a guia **Teste**. 
3. Verificar **Enviar teste para mim mesmo**.
4. Clique em **Send Test (Enviar teste)** para enviar seu web push para o navegador da Web.

![Web push de teste]({% image_buster /assets/img_archive/testwebpush.png %})

Se já tiver aceitado mensagens push do dashboard do Braze, o push aparecerá no canto da tela. Caso contrário, clique em **Permitir** quando solicitado, e a mensagem será exibida.

{% endtab %}
{% tab Mensagem no app %}

Se você tiver notificações por push configuradas em seu aplicativo e no dispositivo de teste, poderá enviar mensagens no app para ver como ele se parece em tempo real. 

1. Redija sua mensagem no app.
2. Selecione a guia **Test (Teste** ) e adicione seu endereço de e-mail ou ID de usuário ao campo **Add Individual Users (Adicionar usuários individuais** ). 
3. Clique em **Send Test (Enviar teste)** para enviar sua mensagem push ao dispositivo.

Uma mensagem de push de teste será exibida na parte superior da tela do dispositivo.

![Teste no aplicativo]({% image_buster /assets/img_archive/test-in-app.png %})

Ao clicar diretamente e abrir a mensagem push, você será direcionado para o app, onde poderá visualizar o teste da mensagem no app. Note que esse recurso de teste de mensagem no app depende de o usuário clicar em uma notificação por push de teste para disparar a mensagem no app. Dessa forma, o usuário deve ser elegível para receber notificações por push no app relevante para a entrega bem-sucedida da notificação por push de teste.

#### Solução de problemas

* Se a sua campanha de mensagens no app não for disparada por uma campanha push, verifique a segmentação da campanha in-app para confirmar se o usuário atende ao público-alvo **antes de** receber a mensagem push.
* Para envios de teste no Android e no iOS, as mensagens no app que usam o comportamento ao clicar em **Solicitar permissão push** podem não ser exibidas em alguns dispositivos. Como solução alternativa:
  * **Android:** Os dispositivos devem estar usando o Android 13 e nosso Android SDK versão 21.0.0. Outro motivo pode ser o fato de o dispositivo em que a mensagem no app é exibida já ter um prompt no nível do sistema. Talvez você tenha selecionado **Não perguntar novamente**, portanto, talvez seja necessário reinstalar o app para redefinir as permissões de notificação antes de testar novamente.
  * **iOS:** Recomendamos que sua equipe de desenvolvedores revise a implementação de notificações por push para seu app e remova manualmente qualquer código que solicite permissões por push. Para saber mais, consulte [Mensagens no app do push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
* Para que uma campanha de mensagens no app baseada em ações seja entregue, os eventos personalizados devem ser registrados por meio do Braze SDK, e não das APIs REST, para que o usuário possa receber mensagens no app elegíveis diretamente em seu dispositivo. Os usuários podem receber a mensagem no app se realizarem o evento durante a sessão.

{% endtab %}
{% tab Cartão de conteúdo %}

Depois de criar seu cartão de conteúdo, você pode enviar um cartão de conteúdo de teste para seu app para ver como ele ficará em tempo real.

1. Elabore seu cartão de conteúdo.
2. Selecione a guia **Test (Teste** ) e selecione pelo menos um Content Test Group (Grupo de teste de conteúdo) ou um usuário individual para receber essa mensagem de teste. 
3. Clique em **Send Test (Enviar teste)** para enviar o cartão de conteúdo para o app.

![Cartão de conteúdo de teste]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Depois de criar sua mensagem SMS ou MMS, você pode enviar uma mensagem de teste para o telefone para ver como ela ficará em tempo real. 

1. Rascunhe sua mensagem SMS ou MMS.
2. Selecione a guia **Test (Teste** ) e selecione pelo menos um Content Test Group (Grupo de teste de conteúdo) ou um usuário individual para receber essa mensagem de teste. 
3. Clique em **Send Test (Enviar teste** ) para enviar sua mensagem de teste.

![Cartão de conteúdo de teste]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Depois de criar seu webhook, você pode fazer um envio de teste para verificar a resposta do webhook. Selecione a guia **Teste** e selecione **Enviar teste** para enviar um teste para o URL do webhook fornecido. Também é possível selecionar um usuário individual para fazer a prévia da resposta como um usuário específico. 

![Cartão de conteúdo de teste]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab Feed de notícias %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

O envio de um cartão de teste do Feed de notícias exige que você configure um segmento de teste e, posteriormente, envie uma campanha de teste.

##### Etapa 1: Criar um segmento de teste designado

Depois de configurar um segmento de teste, você pode usar esses canais de envio de mensagens. O processo leva algumas etapas curtas e, se configurado corretamente, só precisará ser feito uma vez.

1. Acesse a página **Segments (Segmentos** ) e [crie um novo segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 
2. Clique no menu suspenso em **Add Filter (Adicionar filtro** ) e localize os filtros de teste na parte inferior da lista <br><br>![Teste de filtros]({% image_buster /assets/img_archive/testmessages1.png %})<br><br>
3. Use os filtros de teste para selecionar usuários com endereços de e-mail específicos ou [IDs de usuários]({{site.baseurl}}/developer_guide/platforms/swift/analytics/setting_user_ids/) externos.<br><br>![Teste das opções de filtro]({% image_buster /assets/img_archive/testmessages2.png %})
<br><br>Esses filtros têm as seguintes opções:
- **É igual a**: Procura uma correspondência exata do e-mail ou ID de usuário fornecido. Use essa opção se quiser enviar as campanhas de teste apenas para dispositivos associados a um único e-mail ou ID de usuário.
- **Não é igual**: Exclui um e-mail ou ID de usuário específico das campanhas de teste.
- **Jogos**: Encontra usuários que têm endereços de e-mail ou IDs de usuário que correspondem a parte do termo de pesquisa fornecido. Isso pode ser usado para encontrar apenas os usuários com um endereço "@yourcompany.com", permitindo o envio de mensagens a todos da sua equipe.
<br><br>
Esses filtros também podem ser usados em conjunto para restringir a sua lista de usuários teste. Por exemplo, o segmento de teste poderia incluir um filtro de endereço de e-mail que `matches` "@braze.com" e outro filtro que `does not equal` "sales@braze.com". Você também pode selecionar vários e-mails específicos usando a opção `matches` e separando os endereços de e-mail com um caractere "|" (por exemplo, `matches` "email1@braze.com|email2@braze.com").
<br><br>
4. Adicione os filtros de teste ao seu segmento de teste.
5. Clique em **Pré-visualização** na parte superior do editor de segmentos ou exporte os dados de usuários desse segmento para CSV para verificar se selecionou apenas os usuários desejados.
6. Clique no menu suspenso **User Data (Dados do usuário** ) e selecione **CSV Export All User Data (Exportar todos os dados do usuário** ) para exportar os dados de usuários do segmento. 

![Verificar o segmento de teste]({% image_buster /assets/img_archive/testmessages3.png %})

> A exportação dos dados de usuários do segmento para CSV lhe dará a imagem mais precisa de quem se enquadra nesse segmento. A guia **Prévia** é apenas uma amostra dos usuários no segmento e, portanto, pode parecer que não selecionou todos os membros pretendidos. Para saber mais, consulte [Visualização e compreensão dos dados do segmento][7].

Depois de confirmar que está direcionando apenas os usuários que deseja receber a mensagem de teste, você pode selecionar esse segmento em uma campanha existente que deseja testar ou clicar no botão **Start Campaign (Iniciar campanha)** no menu de segmentos.

##### Etapa 2: Enviar uma campanha de teste

Para enviar cartões de teste do feed de notícias, você precisa direcionar o segmento de teste criado anteriormente. Comece criando uma campanha multicanal e seguindo as etapas habituais. Quando chegar à etapa **Target Users (Usuários-alvo** ), selecione seu segmento de teste, conforme mostrado na imagem a seguir.

![Segmento de teste]({% image_buster /assets/img_archive/test_segment.png %})

Termine de confirmar sua campanha e lance-a para testar seus cartões do Feed de notícias.

> Se pretender usar uma única campanha para enviar uma mensagem de teste para si mesmo mais de uma vez, marque a caixa intitulada "Allow users to become re-eligible to receive campaign" (Permitir que os usuários se tornem elegíveis para receber a campanha) na parte **Schedule (Programação)** do criador da campanha.

{% endtab %}
{% endtabs %}

## Teste de campanhas personalizadas 

Se estiver testando campanhas que preenchem dados de usuários ou usam propriedades de eventos personalizados, precisará realizar etapas adicionais ou diferentes.

### Teste de campanhas personalizadas com atribuições do usuário

Se estiver usando [personalização][26] em sua mensagem, precisará realizar etapas adicionais para fazer uma prévia adequada de sua campanha e verificar se os dados de usuários estão preenchendo adequadamente o conteúdo.

Ao enviar uma mensagem de teste, certifique-se de escolher a opção **Selecionar usuário existente** ou prévia como **usuário personalizado**.

![Teste de uma mensagem personalizada][23]{: style="max-width:70%;" }

#### Seleção de um usuário existente

Se estiver selecionando um usuário existente, digite o ID do usuário específico ou o e-mail no campo de pesquisa. Em seguida, use a prévia do dashboard para ver como sua mensagem apareceria para esse usuário e envie uma mensagem de teste para seu dispositivo que reflita o que esse usuário veria.

![Selecione um usuário][24]

#### Seleção de um usuário personalizado

Se a prévia for feita como um usuário personalizado, insira o texto de vários campos disponíveis para personalização, como o nome do usuário e quaisquer atributos personalizados. Mais uma vez, você pode inserir seu próprio endereço de e-mail para enviar um teste para seu dispositivo.

![Usuário personalizado][25]

### Teste de campanhas personalizadas com propriedades de eventos personalizados

O teste de campanhas personalizadas com [propriedades de eventos personalizados][19] difere um pouco do teste de outros tipos de campanhas delineadas. A maneira mais robusta de testar campanhas personalizadas usando propriedades de eventos personalizados é disparar a campanha você mesmo, fazendo o seguinte:

1. Escreva a cópia envolvendo a propriedade do evento. ![Criador de mensagem de teste com propriedades][15]
2. Use [entrega baseada em ação][21] para entregar a campanha quando o evento ocorrer.

{% alert note %}
Se estiver testando uma campanha push para iOS, defina a postergação para 1 minuto para ter tempo de sair do app, pois o iOS não fornece notificações por push para o app aberto no momento. Outros tipos de campanhas podem ser definidos para entrega imediata.
{% endalert %}

![Entrega de mensagens de teste][16]

{: start="3"}
3\. Direcione os usuários como faria para testes, usando um filtro de teste ou direcionando seu próprio endereço de e-mail, e termine de criar a campanha. 

![Direcionamento de mensagem de teste][17]

{: start="4"}
4\. Acesse seu app e conclua o evento personalizado.

A campanha será disparada e mostrará a mensagem personalizada com a propriedade de evento.

![Exemplo de envio de mensagens de teste][18]

Como alternativa, se estiver salvando IDs de usuário personalizados, também poderá testar a campanha enviando uma mensagem de teste personalizada para si mesmo.

1. Escreva o texto de sua campanha.
2. Selecione a guia **Teste** e escolha **Usuário personalizado**. 
3. Adicione a propriedade do evento personalizado na parte inferior da página e adicione seu ID de usuário ou endereço de e-mail na caixa superior.
4. Clique em **Enviar teste** para receber uma mensagem personalizada com a propriedade.

![Testes com usuários personalizados][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/
