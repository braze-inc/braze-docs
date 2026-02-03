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

Uma maneira conveniente de organizar seus usuários de teste é criar um [Grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que inclui um grupo de usuários que receberão mensagens de teste das campanhas. Você pode adicionar esse grupo de teste ao campo **Adicionar grupos de teste de conteúdo** em **Destinatários de teste** na sua campanha e iniciar seus testes sem criar ou adicionar usuários de teste individuais.

## Etapa 2: Enviar mensagens de teste específicas do canal

Para saber as etapas de envio de mensagens de teste, consulte a seção a seguir para seu respectivo canal.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Antes de testar o envio de mensagens de banner no Braze, você precisará criar uma campanha de banner no Braze. Além disso, verifique se o posicionamento que deseja testar já está [colocado em seu app ou site]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Depois de criar sua mensagem de Banner, você pode fazer uma prévia do Banner ou enviar uma mensagem de teste.

1. Elabore sua mensagem de banner.
2. Selecione **Preview** para fazer uma prévia de seu banner ou enviar uma mensagem de teste.
3. Para enviar uma mensagem de teste, adicione um grupo de teste de conteúdo ou um ou mais usuários individuais como **Destinatários do teste** e, em seguida, selecione **Enviar teste**. 

Você poderá visualizar sua mensagem de teste no dispositivo por até 5 minutos.

![Guia Pré-visualização do criador do banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Lembre-se de que a prévia pode não ser idêntica à renderização final no dispositivo do usuário devido às diferenças entre os hardwares.
{% endalert %}

### Lista de verificação de teste

- Sua campanha de banner está atribuída a um posicionamento?
- As imagens e a mídia são exibidas e funcionam conforme o esperado nos tipos de dispositivos e tamanhos de tela direcionados?
- Seus links e botões direcionam o usuário para onde ele deve acessar?
- O Liquid funciona conforme o esperado? Você considerou um valor de atribuição padrão no caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?

{% endtab %}
{% tab Content Card %}

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve estar ativado nos dispositivos de teste com tokens por push válidos registrados para o usuário teste antes do envio. Para usuários de iOS, é necessário tocar na notificação por push enviada pelo Braze para visualizar o cartão de conteúdo do teste. Esse comportamento só se aplica a cartões de conteúdo de teste.
{% endalert %}

Depois de criar seu cartão de conteúdo, você pode enviar um cartão de conteúdo de teste para seu app para ver como ele ficará em tempo real.

1. Elabore seu cartão de conteúdo.
2. Selecione a guia **Test (Teste** ) e selecione pelo menos um Content Test Group (Grupo de teste de conteúdo) ou um usuário individual para receber essa mensagem de teste. 
3. Selecione **Enviar teste** para enviar o cartão de conteúdo para seu app.

![Cartão de conteúdo do teste]({% image_buster /assets/img/contentcard_test.png %})

### Prévia

Você pode fazer uma prévia do cartão à medida que o cria na guia **Preview (Pré-visualização** ). Isso deve ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário.

{% alert note %}
Na guia **Pré-visualização** do seu criador, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste para um dispositivo para garantir que a mídia, o texto, a personalização e os atributos personalizados sejam gerados corretamente.
{% endalert %}

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atribuição padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) se o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus links direcionam o usuário para onde ele deve acessar?

### Depurar

Depois que os cartões de conteúdo forem enviados, você poderá analisar ou depurar quaisquer problemas no [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) no console do desenvolvedor. 

Um caso de uso comum é tentar depurar por que um usuário não consegue ver um determinado cartão de conteúdo. Para isso, é possível procurar nos **registros de usuários de eventos** os cartões de conteúdo entregues ao SDK no início da sessão, mas antes de uma impressão, e rastreá-los até uma campanha específica:

1. Acesse **Configurações** > Registro de usuários de eventos.
2. Localize e expanda a Solicitação de SDK para seu usuário teste.
3. Clique em **Raw Data (Dados brutos**).
4. Encontre o `id` para sua sessão. A seguir, um exemplo de trecho:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```
    
{: start="5"}
5\. Use uma ferramenta de decodificação como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar o `id` do formato Base64 e encontrar o `campaign_id` associado. Em nosso exemplo, isso resulta no seguinte:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Where `4861692e-6fce-4215-bd05-3254fb9e9057` is the `campaign_id`.<br><br>

6. Acesse a página **Campanhas** e pesquise o endereço `campaign_id`.

![Pesquise por campaign_id na página Campanhas]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir daí, é possível revisar as configurações e o conteúdo das mensagens para detalhar e determinar por que um usuário não consegue ver um determinado cartão de conteúdo.

{% endtab %}
{% tab Email %}

1. Rascunhe sua mensagem de e-mail.
2. Selecione **Pré-visualização e teste**.
3. Selecione a guia **Test Send (Envio de teste** ) e adicione seu endereço de e-mail ou ID de usuário no campo **Add individual users (Adicionar usuários individuais** ). 
4. Selecione **Enviar teste** para enviar o e-mail rascunhado para sua caixa de entrada.

![Envio de e-mail de teste]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab In-app message %}

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve ser ativado nos dispositivos de teste antes do envio. Por exemplo, é necessário ter o push ativado em seu dispositivo iOS para tocar na notificação antes da exibição da mensagem de teste. {% endalert %}

Se você tiver notificações por push configuradas em seu aplicativo e no dispositivo de teste, poderá enviar mensagens no app para ver como ele se parece em tempo real. 

1. Redija sua mensagem no app.
2. Selecione a guia **Test (Teste** ) e adicione seu endereço de e-mail ou ID de usuário ao campo **Add Individual Users (Adicionar usuários individuais** ). 
3. Selecione **Send Test (Enviar teste)** para enviar sua mensagem push para o dispositivo.

Uma mensagem de push de teste será exibida na parte superior da tela do dispositivo.

![Teste no aplicativo]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Os envios de teste podem resultar em mais de uma mensagem no app sendo enviada para cada destinatário.
{% endalert %}

Ao clicar diretamente e abrir a mensagem push, você será direcionado para o app, onde poderá visualizar o teste da mensagem no app. Note que esse recurso de teste de mensagem no app depende de o usuário clicar em uma notificação por push de teste para disparar a mensagem no app. Dessa forma, o usuário deve ser elegível para receber notificações por push no app relevante para a entrega bem-sucedida da notificação por push de teste.

### Prévia

Você pode fazer uma prévia da sua mensagem no app à medida que a cria na guia **Preview (Pré-visualização** ). Isso deve ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário. É possível fazer uma prévia de como será a mensagem para um usuário aleatório, um usuário específico ou um usuário personalizado. Também é possível fazer a prévia das mensagens em dispositivos móveis ou tablets.

![Guia "Criar" ao criar uma mensagem no app mostrando a prévia de como será a mensagem. Um usuário não é selecionado, portanto, o Liquid adicionado na seção do corpo é exibido como está.]({% image_buster /assets/img/in-app-message-preview.png %})

O Braze tem três gerações de mensagens no app disponíveis. Você pode ajustar para quais dispositivos suas mensagens devem ser enviadas, com base na geração que eles suportam.

![Alternância entre gerações ao visualizar uma mensagem no app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
Na **Prévia**, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Sempre recomendamos o envio de uma mensagem de teste para um dispositivo para garantir que a mídia, o texto, a personalização e os atributos personalizados sejam gerados corretamente.
{% endalert %}

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atribuição padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) se o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deve acessar?

### Scanner de acessibilidade

Para dar suporte às práticas recomendadas de acessibilidade, o Braze verifica automaticamente o conteúdo das mensagens no app criadas usando o editor de HTML tradicional em relação aos padrões de acessibilidade. Esse scanner ajuda a identificar o conteúdo que pode não atender aos padrões[das WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines). As WCAG são um conjunto de padrões técnicos reconhecidos internacionalmente e desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo da Web mais acessível a pessoas com deficiências.

![Resultados da varredura de acessibilidade]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
O scanner de acessibilidade de mensagens no app só funciona em mensagens criadas com HTML personalizado.
{% endalert %}

#### Como funciona?

O scanner é executado automaticamente em mensagens HTML personalizadas e avalia toda a sua mensagem HTML em relação ao [conjunto](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) completo [de regras WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema sinalizado, ele mostra:

- O elemento HTML específico envolvido
- Uma descrição do problema de acessibilidade
- Um link para contexto adicional ou orientação de correção

#### Compreensão dos testes automatizados de acessibilidade

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Crie sua mensagem LINE.
2. Selecione a guia **Test (Teste** ) e selecione pelo menos um Content Test Group (Grupo de teste de conteúdo) ou um usuário individual para receber essa mensagem de teste.
3. Selecione **Send Test (Enviar teste** ) para enviar sua mensagem.

![Mensagem LINE de teste.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push móvel

1. Elabore seu push móvel.
2. Selecione a guia **Test (Teste** ) e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users (Adicionar usuários individuais** ).
3. Selecione **Enviar teste** para enviar a mensagem rascunhada para o dispositivo.

![Teste push]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

1. Crie seu web push.
2. Selecione a guia **Teste**. 
3. Selecione **Send Test to Myself (Enviar teste para mim mesmo**).
4. Selecione **Send Test (Enviar teste** ) para enviar seu web push para o navegador da Web.

![Teste o web push]({% image_buster /assets/img_archive/testwebpush.png %})

Se já tiver aceitado mensagens push do dashboard do Braze, o push aparecerá no canto da tela. Caso contrário, clique em **Permitir** quando solicitado, e a mensagem será exibida.

{% endtab %}
{% tab SMS/MMS and RCS %}

Depois de criar sua mensagem SMS, MMS ou RCS, você pode enviar uma mensagem de teste para o seu telefone para ver como ela ficará em tempo real. 

1. Rascunhe sua mensagem SMS, MMS ou RCS.
2. Selecione a guia **Test (Teste** ) e selecione pelo menos um Content Test Group (Grupo de teste de conteúdo) ou um usuário individual para receber essa mensagem de teste. 
3. Selecione **Send Test (Enviar teste** ) para enviar sua mensagem de teste.

![Cartão de conteúdo do teste]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Depois de criar seu webhook, você pode fazer um envio de teste para verificar a resposta do webhook. Selecione a guia **Teste** e selecione **Enviar teste** para enviar um teste para o URL do webhook fornecido. Também é possível selecionar um usuário individual para fazer a prévia da resposta como um usuário específico. 

![Cartão de conteúdo do teste]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab WhatsApp %}

1. Crie sua mensagem do WhatsApp.
2. Selecione a guia **Test (Teste** ) e selecione pelo menos um Content Test Group (Grupo de teste de conteúdo) ou um usuário individual para receber essa mensagem de teste.
3. Inicie uma janela de conversa enviando uma mensagem do WhatsApp para o número de telefone associado ao grupo de inscrições que está usando para essa mensagem. O número de telefone associado é listado no alerta na guia **Teste**.
4. Selecione **Send Test (Enviar teste** ) para enviar sua mensagem.

![Teste o envio de mensagens do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Teste de campanhas personalizadas 

Se estiver testando campanhas que preenchem dados de usuários ou usam propriedades de eventos personalizados, precisará realizar etapas adicionais ou diferentes.

### Teste de campanhas personalizadas com atribuições do usuário

Se estiver usando [a personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) em sua mensagem, precisará realizar etapas adicionais para fazer uma prévia adequada da campanha e verificar se os dados de usuários estão preenchendo adequadamente o conteúdo.

Ao enviar uma mensagem de teste, certifique-se de escolher a opção **Selecionar usuário existente** ou prévia como **usuário personalizado**.

![Teste de uma mensagem personalizada]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleção de um usuário existente

Se estiver selecionando um usuário existente, digite o ID do usuário específico ou o e-mail no campo de pesquisa. Em seguida, use a prévia do dashboard para ver como sua mensagem apareceria para esse usuário e envie uma mensagem de teste para seu dispositivo que reflita o que esse usuário veria.

![Selecione um usuário]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleção de um usuário personalizado

Se a prévia for feita como um usuário personalizado, insira o texto de vários campos disponíveis para personalização, como o nome do usuário e quaisquer atributos personalizados. Mais uma vez, você pode inserir seu próprio endereço de e-mail para enviar um teste para seu dispositivo.

![Usuário personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personalização de um usuário existente

É possível editar campos individuais de um usuário aleatório ou existente para ajudar a testar o conteúdo dinâmico da sua mensagem. Selecione **Edit (Editar** ) para converter o usuário selecionado em um usuário personalizado que possa ser modificado.

![A guia "Pré-visualização como usuário" com um botão "Editar".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Teste de campanhas personalizadas com propriedades de eventos personalizados

O teste de campanhas personalizadas com [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) é um pouco diferente do teste de outros tipos de campanhas descritas. 

{% tabs local %}
{% tab Trigger manually %}

#### Método 1: Como disparar a campanha manualmente

Você mesmo pode disparar a campanha como uma forma robusta de testar campanhas personalizadas usando propriedades de eventos personalizados:

1. Escreva a cópia envolvendo a propriedade do evento. 

![Criador de mensagem de teste com propriedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2\. Use [a entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para entregar a campanha quando o evento ocorrer.

{% alert note %}
Se estiver testando uma campanha push para iOS, defina a postergação para um minuto para ter tempo de sair do app, pois o iOS não fornece notificações por push para o app aberto no momento. Outros tipos de campanhas podem ser definidos para entrega imediata.
{% endalert %}

![Entrega de mensagens de teste]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Direcione os usuários como faria para testes, usando um filtro de teste ou direcionando seu próprio endereço de e-mail, e termine de criar a campanha. 

![Direcionamento de mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Acesse seu app e conclua o evento personalizado.

A campanha será disparada e mostrará a mensagem personalizada com a propriedade de evento.

![Exemplo de envio de mensagens de teste]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Método 2: Envio de mensagens de teste para você mesmo

Como alternativa, se estiver salvando IDs de usuário personalizados, também poderá testar a campanha enviando uma mensagem de teste personalizada para si mesmo.

1. Escreva o texto de sua campanha.
2. Selecione a guia **Teste** e escolha **Usuário personalizado**. 
3. Adicione a propriedade do evento personalizado na parte inferior da página e adicione seu ID de usuário ou endereço de e-mail na caixa superior.
4. Selecione **Enviar teste** para receber uma mensagem personalizada com a propriedade.

![Testes com usuários personalizados]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Usando Liquid

Você pode testar as propriedades de eventos personalizados inserindo valores manualmente com o Liquid. 

1. No editor de mensagens, insira os valores das propriedades de seus eventos personalizados.
2. Selecione a guia **Pré-visualização como usuário** para verificar se a mensagem correta é exibida.

{% endtab %}
{% endtabs %}

## Solução de problemas

### Mensagem no app

Se a sua campanha de mensagens no app não for disparada por uma campanha push, verifique a segmentação da campanha in-app para confirmar se o usuário atende ao público-alvo **antes de** receber a mensagem push.

Para envios de teste no Android e no iOS, as mensagens no app que usam o comportamento ao clicar em **Solicitar permissão push** podem não ser exibidas em alguns dispositivos. Como solução alternativa:
- **Android:** Os dispositivos devem estar usando o Android 13 e nosso Android SDK versão 21.0.0. Outro motivo pode ser o fato de o dispositivo em que a mensagem no app é exibida já ter um prompt no nível do sistema. Talvez você tenha selecionado **Não perguntar novamente**, portanto, talvez seja necessário reinstalar o app para redefinir as permissões de notificação antes de testar novamente.
- **iOS:** Recomendamos que sua equipe de desenvolvedores revise a implementação de notificações por push para seu app e remova manualmente qualquer código que solicite permissões por push. Para saber mais, consulte [Mensagens no app do push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Para que uma campanha de mensagens no app baseada em ação seja entregue, é necessário o registro de usuários de eventos personalizados por meio do Braze SDK, e não de APIs REST, para que os usuários possam receber mensagens no app elegíveis diretamente em seus dispositivos. Os usuários recebem a mensagem no app se realizarem o evento durante a sessão.
