---
nav_title: Criar uma mensagem do WhatsApp
article_title: Como criar uma mensagem do WhatsApp
page_order: 0
description: "Este artigo de referência aborda as etapas envolvidas na construção e criação de uma mensagem do WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Criar uma mensagem do WhatsApp

> As campanhas do WhatsApp são ótimas para alcançar diretamente e conversar de forma programática com seus clientes. Você pode usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com a sua marca. 

## Pré-requisitos

Antes de poder criar mensagens do WhatsApp, você precisa revisar e concluir o seguinte na [visão geral do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/):
  - Reconhecer políticas, limites e regras de conteúdo
  - Configure sua conexão com o WhatsApp
  - Crie modelos iniciais no Meta para usar em suas mensagens

## Criar uma mensagem

### Etapa 1: Escolha onde construir sua mensagem

{% alert note %}
O WhatsApp cria [modelos de mensagens](#template-messages) diferentes para cada idioma. Crie uma campanha para cada idioma com segmentação para fornecer o modelo correto aos usuários ou use o Canvas.
{% endalert %}

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canvas? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto os Canvases são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

**Passos:**

1. Vá para a página **Campaigns (Campanhas** ) e clique em <i class="fas fa-plus"></i> **Create Campaign (Criar campanha**).
2. Selecione **WhatsApp** ou, para campanhas direcionadas a vários canais, selecione **Multichannel Campaign (Campanha multicanal**).
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para obter mais informações sobre esse tópico, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar outras variantes. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Passos:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor do Canvas. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique um atraso conforme necessário.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e acrescentando filtros adicionais. As opções de público serão verificadas após o atraso no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha qualquer outro canal de mensagens que você queira associar à sua mensagem.

{% alert tip %}
Se um Canvas baseado em ação for acionado por uma mensagem recebida do WhatsApp, você poderá fazer referência às propriedades do WhatsApp em qualquer etapa do Canvas até o próximo caminho de ação.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 2: Escreva sua mensagem do WhatsApp

Selecione se você deseja criar uma [mensagem modelo](#template-messages) do WhatsApp ou uma mensagem de resposta, dependendo do seu caso de uso. Qualquer conversa iniciada pela empresa deve começar com um modelo aprovado, enquanto as mensagens de resposta podem ser usadas em respostas a mensagens recebidas de usuários dentro de um período de 24 horas.

\![A seção Variantes de mensagem permite selecionar um grupo de assinatura e um dos dois tipos de mensagem: Mensagem modelo do WhatsApp e mensagem de resposta.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Template messages %}

Você pode usar [mensagens modelo aprovadas do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) para iniciar conversas com seus usuários no WhatsApp. Essas mensagens são enviadas com antecedência ao WhatsApp para aprovação de conteúdo, o que pode levar até 24 horas para ser aprovado. Todas as edições que você fizer na cópia precisam ser editadas e reenviadas ao WhatsApp.

Os campos de texto desativados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Para fazer atualizações no texto desativado, você deve editar seu modelo e obtê-lo novamente aprovado.

#### Idiomas

Cada modelo tem um idioma atribuído, portanto, é necessário criar uma campanha ou etapa do Canvas para cada idioma a fim de configurar corretamente a correspondência de usuários. Por exemplo, se você estiver criando um Canvas que usa modelos atribuídos em indonésio e inglês, precisará criar uma etapa do Canvas para o modelo indonésio e uma etapa do Canvas para o modelo inglês.

Lista de modelos, incluindo visualizações de suas mensagens, seus idiomas atribuídos e seu status de aprovação.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Se estiver adicionando uma cópia em um idioma escrito da direita para a esquerda, observe que a aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviços as processam. Para obter práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Variáveis

Se você adicionou variáveis ao criar o modelo do WhatsApp no Meta Business Manager, essas variáveis aparecerão como espaços em branco no compositor de mensagens. Substitua esses espaços em branco por Liquid ou texto simples. Para usar texto simples, use o formato "texto aqui" entre colchetes duplos. Se você optou por incluir imagens ao criar o modelo, poderá carregar ou adicionar imagens da biblioteca de mídia ou fazer referência a um URL de imagem.

Observe que os campos de texto desativados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Se quiser fazer atualizações no texto desativado, você deverá editar seu modelo e obtê-lo novamente aprovado.

{% alert tip %}
{% raw %}
Se você planeja usar o Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, caso o perfil de usuário do destinatário esteja incompleto, ele não receba uma mensagem. As mensagens com variáveis Liquid ausentes não serão enviadas pelo WhatsApp.
{% endraw %}
{% endalert %}

\![A ferramenta Adicionar personalização com o atributo "first_name" e o valor padrão "você".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Links dinâmicos 

Os URLs de call-to-action podem conter variáveis, embora o Meta exija que elas estejam no final do URL, como `{% raw %}https://example.com/{{variable}}{% endraw %}`, onde a variável pode ser substituída no Braze pelo Liquid. Os links também podem ser incluídos no corpo do texto como parte do modelo. Esses dois links podem ser encurtados e rastreados por meio do [rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/).

{% endtab %}
{% tab Response messages %}

É possível usar mensagens de resposta para responder a mensagens recebidas de seus usuários. Essas mensagens são criadas no aplicativo Braze durante sua experiência de composição e podem ser editadas a qualquer momento. Você pode usar o Liquid para fazer a correspondência do idioma da mensagem de resposta com os usuários apropriados.

Há cinco layouts de mensagem de resposta que você pode usar:
- Resposta rápida
- Mensagem de texto
- Mensagem da mídia
- Botão de chamada para ação
- Mensagem da lista

O compositor da mensagem de resposta para uma mensagem de resposta que dá as boas-vindas a novos usuários com um código de desconto.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Etapa 3: Visualize e teste sua mensagem

A Braze sempre recomenda visualizar e testar sua mensagem antes de enviá-la. Mude para a guia **Teste** para enviar uma mensagem de teste do WhatsApp para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, ou visualize a mensagem como um usuário diretamente no Braze.

\![Uma mensagem de visualização para um usuário personalizado chamado Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
É necessária uma janela de conversação para enviar mensagens de resposta, inclusive mensagens de teste. Para iniciar uma janela de conversa, envie uma mensagem do WhatsApp para o número de telefone associado ao grupo de assinatura que você está usando para essa mensagem. O número de telefone associado é listado no alerta na guia **Teste**.
{% endalert %}

\![Um alerta que diz: "Para testar, primeiro abra uma janela de conversa enviando uma mensagem do WhatsApp para +1 217-582-9414. Em seguida, envie sua mensagem de resposta para o usuário de teste."]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

### Etapa 4: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Em seguida, crie o restante de sua campanha. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar mensagens do WhatsApp.

#### Escolha uma programação de entrega ou um acionador

As mensagens do WhatsApp podem ser entregues com base em um horário programado, em uma ação ou em um acionador de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para a entrega baseada em ação, você também pode definir a duração da campanha e o [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem alvos

Em seguida, você precisa [segmentar os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de assinatura, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. Nesta etapa, você selecionará o público-alvo maior de seus segmentos e restringirá ainda mais esse segmento com nossos filtros. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

{% multi_lang_include target_audiences.md %}

#### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Você também pode definir eventos de conversão personalizados com base em seu caso de uso específico. Seja criativo e pense em como você realmente deseja medir o sucesso dessa campanha.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canvas. Para obter mais detalhes sobre como criar o restante do seu Canvas, implementar testes multivariados e Intelligent Selection e muito mais, consulte a etapa [Criar seu Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) da nossa documentação do Canvas.

Como as janelas de conversação só podem durar 24 horas por mensagem de entrada, o Braze verificará se não há atrasos superiores a 24 horas entre uma mensagem de entrada e uma mensagem de resposta. 

{% endtab %}
{% endtabs %}

### Etapa 5: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canvas, revise seus detalhes, teste-a e envie-a!

Em seguida, confira [os relatórios do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) para saber como você pode acessar os resultados de suas campanhas do WhatsApp.

## Recursos compatíveis com o WhatsApp

### Mensagens de saída

Os recursos a seguir são compatíveis com as mensagens de saída do WhatsApp que você envia pelo Braze:

| Recurso | Detalhes | Tamanho máximo | Formatos suportados |
| ------- | ------- | ------------- | ---------------------- |
| Texto do cabeçalho | Há suporte para cadeias de caracteres e parâmetros variáveis. | - | -
| Texto do corpo | Há suporte para cadeias de caracteres e parâmetros variáveis. | - | - |
| Texto do rodapé | Há suporte para cadeias de caracteres e parâmetros variáveis. | - | - |
| Links de CTA | Há suporte para vários tipos de CTA (call-to-action). Para obter mais detalhes, consulte [Tipos de call-to-action](#ctas). | - | - |
| Imagens | As imagens podem ser incorporadas no corpo do texto. Eles devem ser de 8 bits e usar um modelo de cor RGB ou RGBA. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documentos | Os documentos podem ser incorporados ao corpo do texto. Os arquivos devem ser hospedados por meio de URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vídeos | Os vídeos podem ser incorporados no corpo do texto. Os arquivos devem ser hospedados por meio de URL ou na [biblioteca de mídia do Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library). | < 16 MB | `.3gp`, `.mp4` |
| Áudio | O áudio só é suportado por meio de mensagens de resposta. Os arquivos devem ser hospedados por meio de URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Mensagens de entrada

Os seguintes recursos são compatíveis com as mensagens recebidas do WhatsApp que você recebe por meio do Braze:

| Recurso | Detalhes | Formatos suportados |
| ------- | ------- | ------------------ |
| Texto do corpo | Somente cadeias de caracteres padrão são suportadas. | - |
| Imagens | As imagens devem ser de 8 bits e usar um modelo de cor RGB ou RGBA. Os arquivos devem ter menos de 5 MB. | `.jpg`, `.png` |
| Áudio | Somente os arquivos Ogg codificados com o codec Opus são compatíveis. Outros formatos Ogg não são. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documentos | Os documentos são suportados por meio de anexos de mensagens. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Vídeo | Somente o codec de vídeo H.264 e o codec de áudio AAC são compatíveis. Os vídeos devem ter um único fluxo de áudio ou nenhum fluxo de áudio. | `.mp4`, `.3gp` |
| Links de CTA | Há suporte para vários tipos de CTA (call-to-action). Para obter mais detalhes, consulte [Tipos de call-to-action](#ctas). | - |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Tipos de chamadas para ação {#ctas}

Os seguintes tipos de call-to-action são compatíveis com as mensagens do WhatsApp que você envia pelo Braze:

| Tipo de CTA    | Detalhes |
| ----------- |---------------- | 
| Visite o site | No máximo um botão (incluindo parâmetros variáveis). |
| Ligar para o número de telefone | Disponível apenas para modelos de mensagem. <br>No máximo um botão. |
| Botões personalizados de resposta rápida | No máximo três botões. |
| Botão de desativação de marketing | Por padrão, os status de assinatura não são atualizados automaticamente. Para obter um passo a passo completo, consulte [Opt-ins & Opt-Outs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection). |
| Modelos de mensagem de código de cupom | Disponível apenas para modelos de mensagem. <br>Eles podem ser abertos e editados como outros modelos de mensagem e são compatíveis com os códigos promocionais Liquid e Braze. |
| Mensagens de resposta de CTA  | Crie uma mensagem de resposta que inclua um botão de chamada para ação. |
| [Listar mensagens de resposta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#list-messages) | Crie uma mensagem de resposta que inclua uma lista de até 10 opções para os usuários escolherem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

