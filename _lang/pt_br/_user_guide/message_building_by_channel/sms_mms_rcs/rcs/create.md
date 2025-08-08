---
nav_title: "Criação de uma mensagem RCS"
article_title: Criação de uma mensagem RCS
page_order: 2
alias: /create_rcs_message/
description: "Este artigo aborda como criar uma mensagem RCS."
page_type: reference
channel:
  - RCS
---

# Criação de uma mensagem RCS

> As campanhas de RCS são ótimas para alcançar diretamente e conversar de forma programática com seus clientes. É possível usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com sua marca.

## Criação de uma mensagem RCS

### Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campanha %}
1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **SMS/MMS/RCS**ou, para campanhas com direcionamento para vários canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.

{: start="5"}
5\. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Teste de variantes de SMS e RCS**: O Braze permite que você inclua as variantes de SMS e RCS em uma única campanha, o que lhe permite comparar a performance de cada uma. Você pode adicionar variantes de SMS e RCS durante a primeira etapa da composição da mensagem.

{: start="6"}
6\. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) ativado para RCS. Ao selecionar um grupo de inscrições, o Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a campanha. Somente os códigos longos e curtos que pertencem a esse grupo de inscrições serão usados para enviar SMS aos usuários direcionados.
- **SMS fallback**: A Braze recomenda enfaticamente que todo grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade, caso as mensagens RCS não sejam entregues. Alguns motivos para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta da operadora em um determinado país ou região. Ao ativar o fallback de SMS, sua mensagem ainda será entregue ao usuário e você nunca perderá a oportunidade de se conectar com ele.   

{: start="7"}
7\. Escolha entre SMS e RCS. Antes de criar as mensagens RCS, escolha o canal de envio de mensagens. Em geral, recomendamos o uso do RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre oferecemos a opção de enviar com SMS para que você tenha o máximo de flexibilidade e controle. 

![Opções para selecionar um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canva %}
1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa **SMS/MMS/RCS** Mensagem no construtor do Canva. 
3. Dê um nome claro e significativo à sua etapa.
4. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) ativado para RCS. Ao selecionar um grupo de inscrições, o Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a campanha. Somente códigos longos e códigos curtos que pertencem a esse grupo de inscrições serão usados para direcionamento de usuários.
- **SMS fallback**: A Braze recomenda enfaticamente que todo grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade, caso as mensagens RCS não sejam entregues. Alguns motivos para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta da operadora em um determinado país ou região. Ao ativar o fallback de SMS, sua mensagem ainda será entregue ao usuário e você nunca perderá a oportunidade de se conectar com ele.

{: start="5"}
5\. Escolha entre SMS e RCS. Antes de criar as mensagens RCS, escolha o canal de envio de mensagens. Em geral, recomendamos o uso do RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre oferecemos a opção de enviar com SMS para que você tenha o máximo de flexibilidade e controle. 

![Opções para selecionar um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione seu tipo de mensagem RCS

Para o tipo de mensagem RCS, escolha entre **Texto** ou **Mídia**.

![Opções para selecionar um tipo de mensagem de texto ou de mídia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Texto %}
Como o nome indica, as mensagens de texto RCS se concentram no texto como um meio. Se você digitar até 160 caracteres, a mensagem RCS será cobrada como uma mensagem somente de texto (ou "básica"). Se você exceder 160 caracteres ou usar um elemento rico, a mensagem será cobrada como uma mensagem RCS rica (ou "única") (e o limite de caracteres aumentará para 3072 caracteres). 

#### Recursos

- Os tipos de mensagens de texto incluem todos os recursos de SMS. Somente o rastreamento avançado é possível para o rastreamento de cliques em URLs, a fim de fornecer granularidade de relatório em nível de usuário. 
- Além disso, agora você tem a opção de incluir botões de **Suggested Replies** e **Suggested Actions** envolventes, que impulsionam ações de alto engajamento do usuário, como visitar uma landing page ou fazer um pedido. 
    - **As respostas sugeridas** são botões que contêm respostas sugeridas para os usuários clicarem e preencherem previamente em sua entrada de texto, eliminando o atrito de ter que pensar em uma resposta ao fornecer um conjunto restrito de opções para eles. 
    - **Ações sugeridas** são botões que iniciam uma ação no dispositivo do usuário. Normalmente, eles consistem em uma ou duas palavras descritivas e um ícone visual para ajudar o usuário a entender o que o botão faz. Atualmente, o Braze oferece suporte a ações sugeridas OpenURL. Isso funciona de forma semelhante a um URL, em que os usuários que selecionam o botão são redirecionados para uma página da Web ou outro local identificado pelo URL. 

![Um GIF de três ações sugeridas para uma mensagem RCS que promove estilos de moda em alta: "Fairytale royalty" (realeza de contos de fadas), "Edgy academia" (academia ousada) e "Show me your other styles" (mostre-me seus outros estilos).]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considerações

- Quanto aos limites de caracteres no texto, você pode escrever até 160 caracteres para uma mensagem RCS somente de texto (básica) ou até 3072 para uma mensagem RCS rica (única). 
- Para limites de botões, você pode adicionar até cinco botões por mensagem. Esses botões podem ser ações sugeridas ou respostas sugeridas.
- Blocos de texto mais longos e muitos botões podem frustrar os usuários, portanto, sempre que possível, recomendamos que se incline para a simplicidade. 
- Em alguns casos, pode ser mais econômico enviar mensagens de texto mais longas somente por meio de RCS do que por SMS. Isso ocorre porque as mensagens SMS mais longas são divididas em vários segmentos, cada um dos quais é cobrado, enquanto as mensagens RCS são cobradas por mensagem. Entre em contato com seu gerente de conta Braze para obter mais detalhes e orientações.
{% endtab %}

{% tab Mídia %}
As mensagens de mídia RCS permitem o uso de formatos de mídia envolventes que não são possíveis com SMS. Isso inclui arquivos de imagem, vídeo e documentos. Essas opções de mídia existem para ajudá-lo a engajar seu público ainda mais profundamente e ativar casos de uso totalmente novos. No momento, apenas o upload de imagens é suportado pela [Biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

#### Recursos

- Os tipos de mensagens de mídia suportam tudo o que está disponível nos tipos de mensagens de texto, o que inclui texto, respostas sugeridas e ações sugeridas.
- Oferece suporte a arquivos de imagem, incluindo os formatos de arquivo JPEG e PNG. Os arquivos de imagem estão disponíveis por meio de upload na Biblioteca de mídia. 
- Oferece suporte a arquivos de vídeo, incluindo os formatos de arquivo MP4, MPEG e MV4. Os arquivos de vídeo podem ser adicionados por URL diretamente no criador de mensagens. 
- Oferece suporte a arquivos de documentos no formato PDF. Os arquivos de documentos podem ser adicionados por meio do URL diretamente no criador de mensagens. 

![RCS criador com uma opção para fazer upload de um arquivo de mídia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Especificações do arquivo

| Tipo de arquivo | Especificações |
| --- | --- |
| Tudo | \- O tamanho do arquivo é limitado a 100 MB <br><br>\- O URL do arquivo pode ter até 2048 caracteres |
| Arquivos de imagem | Os formatos de arquivo suportados incluem JPG, JPEG e GIF
| Arquivos de vídeo | Os formatos de arquivo compatíveis incluem H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Arquivos de documentos | Formatos de arquivo compatíveis: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considerações

A experiência do usuário no recebimento de mensagens RCS pode variar ligeiramente com base em vários fatores, incluindo a cobertura da operadora no país de destino, o hardware do dispositivo móvel e o sistema operacional do dispositivo móvel. 

De modo geral, o RCS se integra mais naturalmente aos dispositivos Android (esse método foi amplamente implementado pelo Google, e o envio de mensagens RCS ponto a ponto é amplamente adotado pela comunidade Android). Dispositivos diferentes podem renderizar a experiência em velocidades e qualidades diferentes.  
{% endtab %}
{% endtabs %}

### Etapa 3: Crie sua mensagem RCS

Escreva sua mensagem usando idiomas e personalização[(Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) e emojis) conforme necessário. Certifique-se de respeitar nossos limites de cópia de mensagens para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de continuar, leia nossas [diretrizes para limites de mensagens RCS](#step-2-select-your-rcs-message-type). As mensagens RCS são [cobradas por mensagem]({{site.baseurl}}/sms_rcs_billing_calculators/), portanto, é uma boa ideia entender as nuances do que pode ser incluído em cada tipo de mensagem RCS.
{% endalert %}

### Etapa 4: Pré-visualize e teste sua mensagem

O Braze sempre recomenda que você faça uma prévia e teste sua mensagem antes de enviá-la. Acesse a guia **Test (Teste** ) para enviar um RCS de teste para grupos de teste de conteúdo ou usuários individuais, ou para fazer uma prévia da mensagem como um usuário diretamente no Braze.

### Etapa 5: Crie o restante de sua campanha ou Canva

Em seguida, crie o restante de sua campanha ou Canva. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar mensagens RCS.

#### Etapa 5.1: Escolha a programação ou o disparo da entrega

As mensagens RCS podem ser enviadas com base em um horário programado, em uma ação ou em um disparo da API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o Horário de silêncio.

Especifique seus controles de entrega, como permitir que os usuários se tornem elegíveis novamente para receber a campanha ou ativar regras de limite de frequência.

#### Etapa 5.2: Escolha os usuários a serem direcionados

Direcione os usuários escolhendo segmentos ou filtros para restringir seu público. Você já deve ter selecionado o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. 

Em seguida, você selecionará o público maior de seus segmentos e restringirá ainda mais esse segmento com [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) opcionais. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

{% alert tip %}
Interessado em usar o redirecionamento de RCS para direcionar os usuários com base em suas interações de SMS e RCS? Consulte [Redirecionamento]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Etapa 5.3: Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, ou eventos de conversão, após receberem uma campanha. É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso de sua campanha. Por exemplo:
- Se estiver usando a segmentação geográfica para disparar uma mensagem RCS que tenha como objetivo final que o usuário faça uma compra, defina o evento de conversão como **Purchase (Compra**).
- Se estiver tentando levar o usuário ao seu app, defina o evento de conversão como **Starts Session**.

Também é possível definir eventos personalizados de conversão com base em seu caso de uso específico. Seja criativo na forma como você realmente deseja medir o sucesso de sua campanha.

### Etapa 6: Revisão e implementação

Depois de terminar de criar sua campanha ou Canva, revise os detalhes, teste-o e envie-o!

Em seguida, consulte [Relatórios para SMS, MMS e RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber como acessar os resultados de suas campanhas de RCS.

## Dicas

### Uso do Liquid para personalização de mensagens

Se planeja usar o Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, se o perfil de usuário do destinatário estiver incompleto, ele não receba um espaço reservado em branco `Hi, !` em vez do nome ou de uma frase coerente.

### Geração de cópia de IA

Precisa de ajuda para criar um texto envolvente? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto, e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Criador de mensagens com um ícone para abrir o Assistente de Copywriting de IA.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Perguntas frequentes

### Posso enviar mensagens de voz pré-gravadas com o RCS?

Sim, é possível usar mensagens de mídia para suportar arquivos de áudio.
