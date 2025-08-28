---
nav_title: Criando um e-mail
article_title: Criação de um envio de e-mail com HTML personalizado
page_order: 1
description: "Este artigo de referência aborda como criar um e-mail usando a plataforma da Braze. Estão incluídas práticas recomendadas sobre como criar suas mensagens, fazer uma prévia do conteúdo e programar sua campanha ou Canva."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# Criação de um envio de e-mail com HTML personalizado

> As mensagens de e-mail são ótimas para fornecer conteúdo aos seus usuários nos termos deles. Eles também são excelentes ferramentas para reengajar usuários que podem até mesmo ter desinstalado seu app. O envio de mensagens de e-mail personalizadas e sob medida aprimorará a experiência dos usuários e os ajudará a obter o máximo valor do seu app. 

Para ver exemplos de campanhas de e-mail, confira nossos [estudos de caso](https://www.braze.com/customers). 

{% alert tip %}
Se esta é a sua primeira vez criando uma campanha de e-mail, recomendamos fortemente que você confira estes cursos de aprendizado da Braze:<br><br>
- [Opt-Ins e Permissões de E-mail](https://learning.braze.com/messaging-channels-email)
- [Projeto: Crie um programa básico de envio de e-mail marketing](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campanha %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **e-mail**, ou, para campanhas de direcionamento para múltiplos canais, selecione **Multichannel**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções do público serão conferidas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de envio de mensagens que gostaria de associar à sua mensagem.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop_access.md variable_name='email html editor' %}

## Etapa 2: Selecione sua experiência de edição {#step-2-choose-your-template-and-compose-your-email}

O Braze oferece duas experiências de edição ao criar uma campanha de e-mail: nosso [editor de arrastar e soltar]({{site.baseurl}}/dnd/) e nosso editor de HTML padrão. Escolha o tile apropriado para a experiência de edição que você prefere. 

![Escolhendo entre o editor de arrastar e soltar, editor de HTML ou modelos para sua experiência de edição de e-mail.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Então, você pode selecionar um [modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) existente, [fazer upload de um modelo]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) de um arquivo (somente editor de HTML), ou usar um modelo em branco. 

{% alert tip %}
Recomendamos selecionar uma experiência de edição por campanha de e-mail. Por exemplo, escolha o **HTML Clássico** ou **Editor de Blocos** em uma única campanha de e-mail em vez de alternar entre editores.
{% endalert %}

## Etapa 3: Crie seu e-mail

Depois de selecionar o modelo, você verá uma visão geral do e-mail, onde poderá ir diretamente para o editor de tela cheia para redigir o e-mail, alterar as informações de envio e visualizar avisos sobre entregabilidade ou conformidade com a lei. Você pode alternar entre as guias HTML, clássica, texto simples e [AMP]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) enquanto compõe. 

![O botão "Regenerar a partir do HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

A versão em texto simples do seu e-mail será sempre atualizada automaticamente a partir da versão em HTML até que uma edição na versão em texto simples seja detectada. Quando uma edição é detectada, a Braze não atualizará mais o texto simples, pois assumimos que você fez alterações intencionais que não devem ser sobrescritas. Você pode reverter para a sincronização automática na guia **Texto simples** selecionando o ícone **Regenerar a partir do HTML**, que só aparece se o texto simples não estiver sincronizando.

{% alert tip %}
Para adicionar movimento em um e-mail com uma prévia precisa, use GIFs em vez de elementos que exijam JavaScript, pois a maioria das caixas de entrada não oferece suporte a JavaScript.
{% endalert %}

![Painel de Variantes de E-mail para compor seu e-mail.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
O Braze removerá automaticamente os manipuladores de eventos HTML referenciados como atribuições. Isso modificará o HTML, portanto, é recomendável verificar novamente o e-mail depois que ele for concluído. Saiba mais sobre [os manipuladores de HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Inicie o botão AI Copywriter, localizado no campo "Corpo" do criador de e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Precisa de ajuda para criar mensagens da direita para a esquerda em idiomas como árabe e hebraico? Consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) para conhecer as práticas recomendadas.

### Etapa 3a: Adicione suas informações de envio

Depois de terminar de projetar e criar sua mensagem de e-mail, é hora de adicionar as informações de envio na seção **Configurações de envio**.

1. Em **Informações de envio**, selecione um e-mail como **Nome de exibição + Endereço de origem**. Você também pode personalizar isso selecionando **Personalizar a partir do nome de exibição + endereço**.
2. Selecione um e-mail como **endereço de resposta**. Você também pode personalizar essa opção selecionando **Personalizar endereço de resposta**.
3. Em seguida, selecione um e-mail como **endereço BCC** para tornar seu e-mail visível para esse endereço.
4. Adicione uma linha de assunto ao seu e-mail. Opcionalmente, você também pode adicionar um pré-cabeçalho e um espaço em branco após o pré-cabeçalho.

Uma prévia no painel direito será preenchida com as informações de envio que você adicionou. Esta informação também pode ser atualizada indo para **Configurações** > **Preferências de E-mail** > **Configuração de Envio**.

#### Avançado

Em **Configurações de envio** > **Avançado**, você pode ativar o CSS em linha e adicionar personalização para cabeçalhos de e-mail e extras de e-mail, o que permite enviar dados adicionais de volta para outros prestadores de serviço de e-mail.

##### Cabeçalhos de e-mail

Para adicionar cabeçalhos de e-mail, selecione **Adicionar novo cabeçalho**. Os cabeçalhos de e-mail contêm informações sobre o e-mail que está sendo enviado. Esses [pares de valores-chave]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) normalmente têm informações sobre o remetente, o destinatário, os protocolos de autenticação e as informações de envio de e-mail. O Braze adiciona automaticamente as informações de cabeçalho necessárias exigidas pela RFC para que os e-mails sejam entregues corretamente ao provedor de sua caixa de entrada.

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
    <td>dkim-signature</td>
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
    <td>Content-Type</td>
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

Os extras de e-mail permitem o envio de dados adicionais para outros prestadores de serviço de e-mail. Isso só se aplica a casos de uso avançados, portanto, você só deve usar envios de e-mail extras se a sua empresa já tiver essa configuração.

Para adicionar extras de e-mail, Acessar as **Informações de Envio** e selecionar **Adicionar Novo Extra**.

{% alert warning %}
O total de pares chave-valor adicionados não deve exceder 1 KB. Caso contrário, as mensagens serão abortadas.
{% endalert %}

Os valores extras de e-mail não são publicados no Currents ou no Snowflake. Se estiver procurando enviar metadados adicionais ou valores dinâmicos para Currents ou Snowflake, use [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) em vez disso.

### Etapa 3b: Pré-visualize e teste sua mensagem

Depois de terminar de criar o e-mail perfeito, você precisa testá-lo antes de enviá-lo. Do fundo da tela de visão geral, selecione **Prévia e Teste**. 

Aqui, você pode fazer uma prévia de como seu e-mail aparecerá na caixa de entrada do cliente. Com a opção **Preview as User** selecionada, é possível fazer a prévia do e-mail como um usuário aleatório, selecionar um usuário específico ou criar um usuário personalizado. Isso permite que você teste se o Connected Content e as chamadas de personalização estão funcionando como deveriam. 

Então, você pode **Copiar link de prévia** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link durará sete dias antes de precisar ser regenerado.

Também é possível alternar entre as visualizações de desktop, celular e texto simples para ter uma ideia de como sua mensagem aparecerá em diferentes contextos.

{% alert tip %}
Quer saber como é o seu e-mail para os usuários no modo escuro? Selecione o botão de alternância **Pré-visualização do modo escuro**, localizado na seção **Pré-visualização e teste** (somente no editor de arrastar e soltar).
{% endalert %}

Quando estiver pronto para uma verificação final, selecione **Test Send (Envio de teste)** e envie uma mensagem de teste para você mesmo ou para um grupo de testadores de conteúdo para garantir que seu e-mail seja exibido corretamente em uma variedade de dispositivos e clientes de e-mail.

![Opção de Testar Envio e exemplo de prévia de e-mail ao compor seu e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Se você ver algum problema com seu e-mail, ou quiser fazer alguma alteração, selecione **Editar E-mail** para voltar ao editor.

{% alert tip %}
Os clientes de e-mail que oferecem suporte a texto de prévia sempre puxam caracteres suficientes para preencher todo o espaço de texto de prévia disponível. No entanto, isso pode deixá-lo em situações em que o texto da prévia está incompleto ou não otimizado.
<br><br>Para evitar isso, você pode criar um espaço em branco após o texto de prévia desejado, para que os clientes de e-mail não puxem outros textos ou caracteres que distraiam o conteúdo do envelope. Para fazer isso, adicione uma cadeia de não juntores de largura zero (`&zwnj;`) e espaços sem quebra (`&nbsp;`) após o texto da prévia que você deseja exibir. <br><br>Quando adicionado ao final do texto da prévia na seção pré-cabeçalho, o seguinte trecho de código para o editor de HTML adicionará o espaço em branco que você está procurando:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
Para o editor de arrastar e soltar, adicione apenas quem não entrou de largura zero (`&zwnj;`) sem a formatação `<div>` diretamente no pré-cabeçalho na seção **Configurações de envio**.

{% endalert %}

### Etapa 3c: Verifique se há erros de e-mail

O editor indicará todos os problemas que encontrar em sua mensagem antes de enviá-la. Aqui está uma lista de erros que são contabilizados em nosso editor:

- **De Display Name** e **Header** não especificados juntos
- Endereços **de** **resposta** e **de** **remetente** inválidos
- Chaves **de cabeçalho** duplicadas
- Problemas de sintaxe do Liquid
- Corpos de e-mail maiores que 400kb (corpos são altamente recomendados para serem [menores que 102kb]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size))
- E-mails com um **corpo** ou **assunto** em branco
- E-mails sem um link de cancelamento de inscrição
- O e-mail do qual está enviando não está na lista de permissões (os envios serão altamente limitados para garantir a entregabilidade)

## Etapa 4: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}
Em seguida, crie o restante da campanha! Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar sua campanha de e-mail.

#### Escolha a programação ou o disparo da entrega

Os e-mails podem ser enviados com base em um horário programado, em uma ação ou em um disparo da API. Para saber mais, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Para campanhas acionadas por API, quando a ação-gatilho estiver definida como **Interagir com a campanha**, a seleção de uma opção **Receber** como interação fará com que sua nova campanha seja disparada assim que o Braze marcar a campanha selecionada como enviada, mesmo que essa mensagem seja devolvida ou não seja entregue.
{% endalert %}

Você também pode definir a duração da campanha, especificar o [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) e definir regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem direcionados

Em seguida, é necessário direcionar os [usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo de como está a população desse segmento no momento, incluindo quantos usuários desse segmento podem ser contatados por e-mail. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

Também é possível optar por enviar a campanha somente para usuários que tenham um [status de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como aqueles que estão inscritos e aceitaram o envio de e-mail.

Opcionalmente, também é possível limitar a entrega a um número especificado de usuários dentro do segmento ou permitir que os usuários recebam a mesma mensagem duas vezes em caso de recorrência da campanha.

##### Campanhas multicanal com envio de e-mail e push

Para campanhas em vários canais direcionadas tanto para e-mail quanto para canais de envio de mensagens, talvez você queira limitar sua campanha para que somente os usuários com aceitação explícita recebam a mensagem (excluindo usuários inscritos ou cancelados). Por exemplo, digamos que você tenha três usuários com diferentes status de aceitação:

- **O usuário A** está inscrito no e-mail e tem a capacitação push ativada. Esse usuário não recebe o e-mail, mas receberá o push.
- O **usuário B** tem aceitação de e-mail, mas não tem a capacitação push ativada. Esse usuário receberá o e-mail, mas não receberá o push.
- O **usuário C** tem aceitação de e-mail e está ativado para push. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, em **Resumo do público**, selecione enviar essa campanha apenas para "usuários com aceitação". Essa opção verificará se apenas os usuários com aceitação receberão seu e-mail, e o Braze enviará seu push apenas para os usuários que têm a capacitação push ativada por padrão.

{% alert important %}
Com esta configuração, não inclua filtros na etapa **Públicos Alvo** que limitem o público a um único canal (por exemplo, `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você pode especificar qualquer uma das seguintes ações como um evento de conversão:

- Abre o aplicativo
- Faz uma compra (pode ser uma compra genérica ou um item específico)
- Executa um evento personalizado específico
- Abre e-mail

É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada. Embora o Braze rastreie automaticamente as aberturas e os cliques da sua campanha, talvez você queira definir o evento de conversão como sendo quando um usuário abre ou clica em um endereço de e-mail para aproveitar as vantagens da [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Se ainda não tiver feito isso, conclua as seções restantes dos componentes do canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nossa documentação do Canvas.
{% endtab %}
{% endtabs %}

## Etapa 5: Revisão e implementação

A seção final fornecerá um resumo da campanha que você acabou de criar. Confirme todos os detalhes relevantes e selecione **Iniciar Campanha**. Agora, é hora de esperar que todos os dados cheguem! 

Para aprender como você pode acessar os resultados de suas campanhas de e-mail, confira [Relatório de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

