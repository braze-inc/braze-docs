---
nav_title: Criação de um e-mail
article_title: Criação de um e-mail com HTML personalizado
page_order: 1
description: "Este artigo de referência aborda como criar um e-mail usando a plataforma Braze. Estão incluídas práticas recomendadas sobre como compor suas mensagens, visualizar seu conteúdo e programar sua campanha ou Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# Criação de um e-mail com HTML personalizado

> As mensagens de e-mail são ótimas para fornecer conteúdo aos seus usuários nos termos deles. Eles também são excelentes ferramentas para reengajar usuários que podem até mesmo ter desinstalado seu aplicativo. O envio de mensagens de e-mail personalizadas e sob medida aprimorará a experiência dos usuários e os ajudará a obter o máximo de valor do seu aplicativo. 

Para ver exemplos de campanhas de e-mail, confira nossos [estudos de caso](https://www.braze.com/customers). 

{% alert tip %}
Se esta é a primeira vez que você está criando uma campanha de e-mail, recomendamos que dê uma olhada nestes cursos do Braze Learning:<br><br>
- [Opt-ins e permissões de e-mail](https://learning.braze.com/messaging-channels-email)
- [Projeto: Criar um programa básico de marketing por e-mail](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canvas? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto os Canvases são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

1. Vá para **Messaging** > **Campaigns** ( **Mensagens** > **Campanhas** ) e selecione **Create Campaign (Criar campanha**).
2. Selecione **Email** ou, para campanhas direcionadas a vários canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Para obter mais informações sobre esse tópico, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar outras variantes. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor do Canvas. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique um atraso conforme necessário.
4. Filtre seu Audience para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e acrescentando filtros adicionais. As opções de público serão verificadas após o atraso, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de mensagens que você gostaria de associar à sua mensagem.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Etapa 2: Selecione sua experiência de edição {#step-2-choose-your-template-and-compose-your-email}

O Braze oferece duas experiências de edição ao criar uma campanha de e-mail: nosso [editor de arrastar e soltar]({{site.baseurl}}/dnd/) e nosso editor HTML padrão. Escolha o bloco apropriado para a experiência de edição que você preferir. 

Escolha entre o editor de arrastar e soltar, o editor HTML ou os modelos para sua experiência de edição de e-mail.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Em seguida, você pode selecionar um [modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) existente, [carregar um modelo]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) de um arquivo (somente no editor HTML) ou usar um modelo em branco. 

{% alert tip %}
Recomendamos selecionar uma experiência de edição por campanha de e-mail. Por exemplo, escolha o **editor** **HTML Classic** ou **Block** em uma única campanha de e-mail, em vez de alternar entre os editores.
{% endalert %}

## Etapa 3: Escreva seu e-mail

Depois de selecionar o modelo, você verá uma visão geral do e-mail, onde poderá ir diretamente para o editor de tela cheia para redigir o e-mail, alterar as informações de envio e visualizar avisos sobre capacidade de entrega ou conformidade com a lei. Você pode alternar entre as guias HTML, clássica, texto simples e [AMP]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) enquanto escreve. 

\![O botão "Regenerate from HTML" (Regenerar a partir de HTML).]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

A versão em texto simples de seu e-mail sempre será atualizada automaticamente a partir da versão em HTML até que seja detectada uma edição na versão em texto simples. Quando uma edição for detectada, o Braze não atualizará mais o texto simples, pois presumimos que você fez alterações intencionais que não devem ser substituídas. Você pode reverter a sincronização automática na guia **Plaintext** selecionando o ícone **Regenerate from HTML**, que só aparece se o texto simples não estiver sendo sincronizado.

{% alert tip %}
Para adicionar movimento em um e-mail com uma visualização precisa, use GIFs em vez de elementos que exijam JavaScript, pois a maioria das caixas de entrada não é compatível com JavaScript.
{% endalert %}

Painel Email Variants para compor seu e-mail.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
O Braze removerá automaticamente os manipuladores de eventos HTML referenciados como atributos. Isso modificará o HTML, portanto, é recomendável verificar novamente o e-mail depois de concluído. Saiba mais sobre [os manipuladores de HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Tente usar o [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará um texto de marketing semelhante ao humano para ser usado em suas mensagens.

Abra o botão AI Copywriter, localizado na guia Body (Corpo) do compositor de e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Precisa de ajuda para criar mensagens da direita para a esquerda em idiomas como o árabe e o hebraico? Consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) para conhecer as práticas recomendadas.

### Etapa 3a: Adicione suas informações de envio

Depois de concluir o design e a criação da mensagem de e-mail, é hora de adicionar as informações de envio na seção **Sending Settings (Configurações de envio** ).

1. Em **Sending Info (Informações de envio**), selecione um e-mail como **From Display Name + Address (Nome de exibição + endereço**). Você também pode personalizar isso selecionando **Personalizar a partir do nome de exibição + endereço**.
2. Selecione um e-mail como o **endereço de resposta**. Você também pode personalizá-lo selecionando **Customize Reply-To Address (Personalizar endereço de resposta**).
3. Em seguida, selecione um e-mail como **endereço BCC** para tornar seu e-mail visível para esse endereço.
4. Adicione uma linha de assunto ao seu e-mail. Opcionalmente, você também pode adicionar um pré-cabeçalho e um espaço em branco após o pré-cabeçalho.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Uma visualização no painel direito será preenchida com as informações de envio que você adicionou. Essas informações também podem ser atualizadas em **Configurações** > **Preferências de e-mail** > **Configuração de envio**.

#### Avançado

Em **Configurações de envio** > **Avançado**, você pode ativar o CSS em linha e adicionar personalização para cabeçalhos de e-mail e extras de e-mail, o que permite enviar dados adicionais de volta para outros provedores de serviços de e-mail.

##### Cabeçalhos de e-mail

Para adicionar cabeçalhos de e-mail, selecione **Add New Header (Adicionar novo cabeçalho**). Os cabeçalhos de e-mail contêm informações sobre o e-mail que está sendo enviado. Esses [pares de valores-chave]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) normalmente têm informações sobre o remetente, o destinatário, os protocolos de autenticação e as informações de roteamento de e-mail. O Braze adiciona automaticamente as informações de cabeçalho necessárias exigidas pela RFC para que os e-mails sejam entregues corretamente ao seu provedor de caixa de entrada.

O Braze lhe permite a flexibilidade de adicionar cabeçalhos de e-mail adicionais, conforme necessário, para casos de uso avançados. Há alguns campos reservados que a plataforma Braze sobrescreverá durante o envio. 

Evite usar as seguintes teclas:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>Campos reservados</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>Assinatura dkim</td>
    <td>Responder a</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>De</td>
    <td>Assunto</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>Versão MIME</td>
    <td>Para</td>
  </tr>
  <tr>
    <td>Tipo de conteúdo</td>
    <td>Recebido</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>Assinatura DKIM</td>
    <td>recebido</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Adição de extras de e-mail

Os extras de e-mail permitem que você envie dados adicionais de volta para outros provedores de serviços de e-mail. Isso só se aplica a casos de uso avançados, portanto, você só deve usar extras de e-mail se a sua empresa já tiver isso configurado.

Para adicionar extras de e-mail, vá para as **Informações de envio** e selecione **Adicionar novo extra**.

{% alert warning %}
O total de pares de valores-chave adicionados não deve exceder 1 KB. Caso contrário, as mensagens serão canceladas.
{% endalert %}

Os valores extras de e-mail não são publicados no Currents ou no Snowflake. Se estiver procurando enviar metadados adicionais ou valores dinâmicos para o Currents ou Snowflake, use [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) em vez disso.

### Etapa 3b: Visualize e teste sua mensagem

Depois de terminar de redigir o e-mail perfeito, você precisa testá-lo antes de enviá-lo. Na parte inferior da tela de visão geral, selecione **Preview and Test**. 

Aqui, você pode visualizar como seu e-mail aparecerá na caixa de entrada de um cliente. Com a opção **Preview as User** selecionada, você pode visualizar seu e-mail como um usuário aleatório, selecionar um usuário específico ou criar um usuário personalizado. Isso permite que você teste se o Connected Content e as chamadas de personalização estão funcionando como deveriam. 

Em seguida, você pode **Copiar link de visualização** para gerar e copiar um link de visualização compartilhável que mostra como será o e-mail para um usuário aleatório. O link terá duração de sete dias antes de precisar ser regenerado.

Você também pode alternar entre as visualizações de desktop, celular e texto simples para ter uma ideia de como sua mensagem aparecerá em diferentes contextos.

{% alert tip %}
Está curioso para saber como é o seu e-mail para os usuários do modo escuro? Selecione o botão de alternância **Dark Mode Preview** ( **Visualização** **do modo escuro** ) localizado na seção **Preview and Test (Visualização e teste** ) (somente no editor de arrastar e soltar).
{% endalert %}

Quando estiver pronto para uma verificação final, selecione **Test Send (Enviar teste)** e envie uma mensagem de teste para você mesmo ou para um grupo de testadores de conteúdo para garantir que seu e-mail seja exibido corretamente em vários dispositivos e clientes de e-mail.

Opção de envio de teste e visualização de exemplo de e-mail ao redigir seu e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Se você encontrar algum problema com seu e-mail ou quiser fazer alterações, selecione **Edit Email (Editar e-mail)** para retornar ao editor.

{% alert tip %}
Os clientes de e-mail que oferecem suporte a texto de visualização sempre inserem caracteres suficientes para preencher todo o espaço de texto de visualização disponível. No entanto, isso pode deixá-lo em situações em que o texto de visualização está incompleto ou não otimizado.
<br><br>Para evitar isso, você pode criar um espaço em branco após o texto de visualização desejado, para que os clientes de e-mail não puxem outros textos ou caracteres que distraiam o conteúdo do envelope. Para fazer isso, adicione uma cadeia de não juntores de largura zero (`&zwnj;`) e espaços sem quebra (`&nbsp;`) após o texto de visualização que você deseja exibir. <br><br>Quando adicionado ao final do texto de visualização na seção de pré-cabeçalho, o seguinte trecho de código para o editor de HTML adicionará o espaço em branco que você está procurando:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
Para o editor de arrastar e soltar, adicione apenas os não juntores de largura zero (`&zwnj;`) sem a formatação `<div>` diretamente no pré-cabeçalho na seção **Configurações de envio**.

{% endalert %}

### Etapa 3c: Verifique se há erros de e-mail

O editor indicará todos os problemas que encontrar em sua mensagem antes que você a envie. Aqui está uma lista de erros que são contabilizados em nosso editor:

- **De Display Name** e **Header** não especificados juntos
- Endereços inválidos **de** e **para resposta** 
- Chaves **de cabeçalho** duplicadas
- Problemas de sintaxe líquida
- Corpos de e-mail maiores que 400kb (é altamente recomendável que os corpos sejam [menores que 102kb]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size))
- E-mails com um **corpo** ou **assunto** em branco
- E-mails sem um link para cancelar a assinatura
- O e-mail do qual você está enviando não está na lista de permissões (os envios serão altamente limitados para garantir a capacidade de entrega)

## Etapa 4: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}
Em seguida, crie o restante de sua campanha! Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar sua campanha de e-mail.

#### Escolha o cronograma de entrega ou o acionador

Os e-mails podem ser entregues com base em um horário programado, em uma ação ou em um acionador de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Para campanhas acionadas por API, quando a ação de acionamento estiver definida como **Interagir com a campanha**, a seleção de uma opção **Receber** como interação fará com que sua nova campanha seja acionada assim que o Braze marcar a campanha selecionada como enviada, mesmo que essa mensagem seja devolvida ou não seja entregue.
{% endalert %}

Você também pode definir a duração da campanha, especificar o [horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) e definir regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem alvos

Em seguida, você precisa [segmentar os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente uma prévia de como está a população desse segmento no momento, incluindo quantos usuários desse segmento podem ser contatados por e-mail. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

{% multi_lang_include target_audiences.md %}

Você também pode optar por enviar sua campanha somente para usuários que tenham um [status de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como aqueles que estão inscritos e optaram por receber e-mails.

Opcionalmente, você também pode limitar a entrega a um número especificado de usuários dentro do segmento ou permitir que os usuários recebam a mesma mensagem duas vezes em uma recorrência da campanha.

##### Campanhas multicanal com e-mail e push

Para campanhas multicanal direcionadas a canais de e-mail e push, talvez você queira limitar sua campanha de modo que somente os usuários que tenham optado explicitamente por receber a mensagem (excluindo usuários inscritos ou não inscritos). Por exemplo, digamos que você tenha três usuários com status de opt-in diferentes:

- **O usuário A** está inscrito no e-mail e está habilitado para push. Esse usuário não recebe o e-mail, mas receberá o push.
- **O usuário B** optou por receber e-mail, mas não está habilitado para push. Esse usuário receberá o e-mail, mas não receberá o push.
- **O usuário C** optou por receber e-mail e está habilitado para envio. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, em **Audience Summary (Resumo do público**), selecione para enviar essa campanha apenas para "usuários opt-in". Essa opção verificará se apenas os usuários opt-in receberão seu e-mail, e o Braze enviará seu push apenas para os usuários que têm o push ativado por padrão.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Target Audiences** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você pode especificar qualquer uma das seguintes ações como um evento de conversão:

- Abre o aplicativo
- Faz uma compra (pode ser uma compra genérica ou um item específico)
- Executa um evento personalizado específico
- Abrir e-mail

É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada. Embora o Braze rastreie automaticamente as aberturas e os cliques da sua campanha, talvez você queira definir o evento de conversão como sendo quando um usuário abre ou clica em um endereço de e-mail para aproveitar as vantagens da [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Se ainda não tiver feito isso, conclua as seções restantes dos componentes do Canvas. Para obter mais detalhes sobre como criar o restante do seu Canvas, implementar testes multivariados e Intelligent Selection e muito mais, consulte a etapa [Criar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.
{% endtab %}
{% endtabs %}

## Etapa 5: Revisão e implementação

A seção final apresentará um resumo da campanha que você acabou de criar. Confirme todos os detalhes relevantes e selecione **Launch Campaign**. Agora, é hora de esperar que todos os dados cheguem! 

Para saber como acessar os resultados de suas campanhas de e-mail, consulte [Relatórios de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

