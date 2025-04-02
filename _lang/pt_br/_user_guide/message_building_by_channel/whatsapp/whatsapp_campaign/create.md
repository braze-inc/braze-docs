---
nav_title: Como criar um envio de mensagens do WhatsApp
article_title: Como criar um envio de mensagens do WhatsApp
page_order: 4
description: "Este artigo de referência aborda as etapas envolvidas na construção e criação de uma mensagem do WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Criação de uma mensagem do WhatsApp

> As campanhas do WhatsApp são ótimas para alcançar diretamente e conversar de forma programática com seus clientes. É possível usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com sua marca. 

## Pré-requisitos

Para criar uma mensagem do WhatsApp e aproveitar o canal do WhatsApp, você deve primeiro ler a [visão geral]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) do WhatsApp e fazer o seguinte:
  - Reconhecer políticas, limites e regras de conteúdo
  - Configure sua conexão com o WhatsApp
  - Crie modelos iniciais no Meta para usar em seus envios de mensagens

## Etapa 1: Escolha onde construir sua mensagem

{% alert note %}
O WhatsApp cria [modelos de mensagens](#template-messages) diferentes para cada idioma. Crie uma campanha para cada idioma com segmentação para fornecer o modelo correto aos usuários ou use o Canva.
{% endalert %}

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campanha %}

**Etapas:**

1. Acesse a página **Campaigns (Campanhas** ) e clique em <i class="fas fa-plus"></i> **Create Campaign (Criar campanha**).
2. Selecione **WhatsApp** ou, para campanhas com direcionamento para vários canais, selecione **Multichannel Campaign (Campanha multicanal**).
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha qualquer outro canal de envio de mensagens que queira associar à sua mensagem.

{% alert tip %}
Se um Canvas baseado em ação for disparado por uma mensagem recebida do WhatsApp, você poderá fazer referência às propriedades do WhatsApp em qualquer etapa do Canva até a próxima jornada de ação.
{% endalert %}

{% endtab %}
{% endtabs %}

## Etapa 2: Crie sua mensagem do WhatsApp

Selecione se deseja criar uma [mensagem modelo](#template-messages) do WhatsApp ou uma mensagem de resposta, dependendo do seu caso de uso. Qualquer conversa iniciada pela empresa deve começar com um modelo aprovado, enquanto as mensagens de resposta podem ser usadas em respostas a mensagens recebidas de usuários dentro de um período de 24 horas.

![A seção Variantes de mensagem permite selecionar um grupo de inscrições e um dos dois tipos de mensagem: Mensagem modelo do WhatsApp e mensagem de resposta.][5]{: style="max-width:80%;"}

### Envio de mensagens de modelo

Você pode usar [mensagens modelo aprovadas do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) para iniciar conversas com seus usuários no WhatsApp. Essas mensagens são enviadas antecipadamente ao WhatsApp para aprovação de conteúdo, que pode levar até 24 horas para ser aprovado. Todas as edições que você fizer na cópia precisam ser editadas e reenviadas ao WhatsApp.

Os campos de texto desativados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Para fazer atualizações no texto desativado, você deve editar seu modelo e obtê-lo novamente aprovado.

#### Idiomas

Cada modelo tem um idioma atribuído, portanto, é necessário criar uma campanha ou etapa do Canva para cada idioma para configurar corretamente a correspondência de usuários. Por exemplo, se estiver criando um canva que usa modelos atribuídos com indonésio e inglês, será necessário criar uma etapa do canva para o modelo indonésio e uma etapa do canvas para o modelo inglês.

![Lista de modelos, incluindo prévias de suas mensagens, idiomas atribuídos e status de aprovação.][8]{: style="max-width:80%;"}

Se estiver adicionando cópia em um idioma escrito da direita para a esquerda, note que a aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre o envio de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/right_to_left_messages/).

#### Variáveis

Se você adicionou variáveis ao criar o modelo do WhatsApp no Meta Business Manager, essas variáveis aparecerão como espaços em branco no criador de mensagens. Substitua esses espaços em branco por Liquid ou texto simples. Para usar texto simples, use o formato "texto aqui" entre colchetes duplos. Se tiver aceitado incluir imagens ao criar o modelo, poderá fazer upload ou adicionar imagens da biblioteca de mídia ou fazer referência a um URL de imagem.

Note que os campos de texto desativados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Se quiser fazer atualizações no texto desativado, você deverá editar seu modelo e aprová-lo novamente.

{% alert tip %}
{% raw %}
Se planeja usar o Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, caso o perfil de usuário do destinatário esteja incompleto, ele não receba uma mensagem. As mensagens com variáveis Liquid ausentes não serão enviadas pelo WhatsApp.
{% endraw %}
{% endalert %}

![A ferramenta Adicionar personalização com a atribuição "first_name" e o valor padrão "you".][2]{: style="max-width:80%;"}

### Links dinâmicos 

Os URLs de chamada para ação podem conter variáveis, embora o Meta exija que elas estejam no final do URL, como `{% raw %}https://example.com/{{variable}}{% endraw %}`, onde a variável pode ser substituída na Braze pelo Liquid. Os links também podem ser incluídos no corpo do texto como parte do modelo. No momento, nenhum desses links pode ser encurtado. 

### Envio de mensagens de resposta

É possível usar mensagens de resposta para responder às mensagens recebidas de seus usuários. Essas mensagens são criadas no app do Braze durante sua experiência de composição e podem ser editadas a qualquer momento. É possível usar o Liquid para fazer a correspondência entre o idioma da mensagem de resposta e os usuários apropriados.

Há três layouts de mensagens de resposta que você pode usar:
- Resposta rápida
- Mensagem
- Mensagem de mídia

![O criador da mensagem de resposta para uma Reply Message que dá as boas-vindas a novos usuários com um código de desconto.][6]{: style="max-width:80%;"}

## Etapa 3: Pré-visualize e teste sua mensagem

O Braze sempre recomenda que você faça uma prévia e teste sua mensagem antes de enviá-la. Mude para a guia **Test (Teste** ) para enviar uma mensagem de teste do WhatsApp para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, ou faça uma prévia da mensagem como um usuário diretamente no Braze.

![Uma mensagem prévia para um usuário existente chamado Suzanne.][3]{: style="max-width:80%;"}

{% alert note %}
É necessária uma janela de conversação para enviar mensagens de resposta, inclusive mensagens de teste. Para iniciar uma janela de conversa, envie uma mensagem do WhatsApp para o número de telefone associado ao grupo de inscrições que está usando para essa mensagem. O número de telefone associado é listado no alerta na guia **Teste**.
{% endalert %}

![Um alerta que diz: "Para testar, primeiro abra uma janela de conversa enviando uma mensagem do WhatsApp para +1 631-202-0907. Em seguida, envie sua mensagem de resposta para o usuário teste."][7]{: style="max-width:80%;"}

## Etapa 4: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}

Em seguida, crie o restante de sua campanha. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar mensagens do WhatsApp.

#### Escolha uma programação ou disparo de entrega

As mensagens do WhatsApp podem ser entregues com base em um horário programado, em uma ação ou em um disparo da API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem direcionados

Em seguida, é necessário direcionar [os usuários]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. Nessa etapa, você selecionará o público maior de seus segmentos e restringirá ainda mais esse segmento com nossos filtros. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes do envio da mensagem.

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), após receberem uma campanha. É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Também é possível definir eventos personalizados de conversão com base em seu caso de uso específico. Seja criativo e pense em como você realmente deseja medir o sucesso dessa campanha.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) de nossa documentação do Canvas.

Como as janelas de conversação só podem durar 24 horas por mensagem de entrada, o Braze verificará se não há postergações superiores a 24 horas entre uma mensagem de entrada e uma mensagem de resposta. 

{% endtab %}
{% endtabs %}

## Etapa 5: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canva, revise seus detalhes, teste-a e envie-a!

Em seguida, confira [os relatórios do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) para saber como você pode acessar os resultados de suas campanhas do WhatsApp.

## Recursos compatíveis com o WhatsApp

O Braze oferece suporte aos seguintes recursos de envio de mensagens do WhatsApp.

### Mensagens de saída

Você pode enviar aos usuários o seguinte em suas mensagens do WhatsApp:

Recurso de mensagens    | Informações
----------- |---------------- 
Cabeçalhos | 
Texto | Suporta parâmetros variáveis
Imagens (JPEG e PNG) | Deve ser de 8 bits, RGB ou RGBA, e até cinco MB para qualquer tipo 
Vídeos | Atualmente, deve estar hospedado em uma URL e ter menos de dezesseis MB. Também deve ter um tipo de vídeo 3GPP ou MP4. <br><br>As mensagens de vídeo estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
Áudio | Suportado apenas para envio de mensagens de resposta. Deve ser de áudio AAC, AMR, MP3, MP4 ou OGG, hospedado em um URL e com menos de dezesseis MB. <br><br>As mensagens de áudio estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
Documentos | Deve estar hospedado em um URL e ter menos de 100 MB. Também deve ter um tipo de documento de texto (`.txt`), Microsoft Excel (`.xls`, `.xlsx`), Microsoft Word (`.doc`, `.docx`), Microsoft PowerPoint (`.ppt`, `pttx`) ou PDF (`.pdf`). <br><br>As mensagens do documento estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
Texto do corpo | Suporta parâmetros variáveis
Texto do rodapé | Suporta parâmetros variáveis 
CTAs | Consulte [Chamadas para ações](#ctas).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Chamadas para ações {#ctas}

Você pode adicionar as seguintes chamadas para ação em suas mensagens do WhatsApp:

Tipo de CTA    | Informações
----------- |---------------- 
Visite o site | No máximo um botão (incluindo parâmetros variáveis).
Ligar para o número de telefone | Disponível apenas para modelos de mensagens. <br>No máximo um botão.
Botões personalizados de resposta rápida | No máximo três botões. 
Botão de cancelamento de inscrição para comunicações de marketing | Essa opção não atualiza automaticamente os status da inscrição. <br><br>Para obter instruções de configuração, consulte [Aceitação e cancelamento de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection).
Modelos de mensagens de código de cupom | Disponível apenas para modelos de mensagens. <br>Eles podem ser abertos e editados como outros modelos de mensagens e são compatíveis com os códigos promocionais do Liquid e do Braze. 
Envio de mensagens de resposta de CTA  | Crie uma mensagem de resposta que inclua um botão de chamada para ação.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Envios de mensagens de entrada

Os usuários podem enviar o seguinte em suas mensagens do WhatsApp:

Recurso de mensagens    | Informações
----------- |---------------- 
Texto | 
Imagens (JPEG e PNG)| Deve ser de 8 bits, RGB ou RGBA, e até 5 MB para qualquer tipo 
Áudio| áudio/aac<br>áudio/mp4<br>áudio/mpeg<br>áudio/amr<br>audio/ogg (somente Codecs Opus, não há suporte para audio/ogg básico)
Documentos | text/plain<br>aplicativo/pdf<br>application/vnd.ms-powerpoint<br>application/msword<br>application/vnd.ms-excel<br>application/vnd.openxmlformats-officedocument.wordprocessingml.document<br>application/vnd.openxmlformats-officedocument.presentationml.presentation<br>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
CTAs | Consulte [Chamadas para ações](#ctas).
Vídeo | vídeo/mp4, vídeo/3gp<br><br>Somente o codec de vídeo H.264 e o codec de áudio AAC são compatíveis. Oferecemos suporte a vídeos com um único fluxo de áudio ou sem fluxo de áudio.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
