---
nav_title: Crie uma mensagem RCS
article_title: Crie uma Mensagem RCS
page_order: 2
alias: /create_rcs_message/
description: "Este artigo aborda como criar uma mensagem RCS."
page_type: reference
channel:
  - RCS
---

# Crie uma mensagem RCS

> As campanhas RCS são ótimas para alcançar diretamente e conversar programaticamente com seus clientes. É possível usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com sua marca.

## Criando uma mensagem RCS

### Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e direcionadas, enquanto os Canvases são melhores para jornadas de usuários em múltiplas etapas.

{% tabs %}
{% tab Campaign %}
1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **SMS/MMS/RCS**, ou, para campanhas que visam múltiplos canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.

{: start="5"}
5\. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Teste de variantes SMS e RCS**: Braze permite que você inclua tanto variantes SMS quanto RCS dentro de uma única campanha, permitindo que você compare o desempenho de cada uma. Você pode adicionar variantes SMS e RCS durante o primeiro passo da composição da mensagem.

{: start="6"}
6\. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Ao selecionar um grupo de inscrições, o Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a campanha. Somente os códigos longos e curtos que pertencem a esse grupo de inscrições serão usados para enviar SMS aos usuários direcionados.
- **Fallback SMS**: Braze recomenda fortemente que todo grupo de inscrições que contém um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade nos casos em que mensagens RCS falham ao serem entregues. Algumas razões para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta da operadora em um determinado país ou região. Ao habilitar o fallback SMS, sua mensagem ainda será entregue ao seu usuário e você nunca perderá essa oportunidade de se conectar com eles.   

{: start="7"}
7\. Escolha entre SMS e RCS. Antes de compor mensagens RCS, escolha o canal pelo qual você enviará. Geralmente, recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre oferecemos a opção de enviar com SMS para que você tenha máxima flexibilidade e controle. 

![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canva, adicione uma etapa de Mensagem **SMS/MMS/RCS** no construtor de canva. 
3. Dê um nome claro e significativo à sua etapa.
4. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Ao selecionar um grupo de inscrições, o Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a campanha. Apenas códigos longos e códigos curtos que pertencem a esse grupo de inscrições serão usados para segmentar usuários.
- **Fallback SMS**: Braze recomenda fortemente que todo grupo de inscrições que contém um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade nos casos em que mensagens RCS falham ao serem entregues. Algumas razões para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta da operadora em um determinado país ou região. Ao habilitar o fallback SMS, sua mensagem ainda será entregue ao seu usuário e você nunca perderá essa oportunidade de se conectar com eles.

{: start="5"}
5\. Escolha entre SMS e RCS. Antes de compor mensagens RCS, escolha o canal pelo qual você enviará. Geralmente, recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre oferecemos a opção de enviar com SMS para que você tenha máxima flexibilidade e controle. 

![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione seu tipo de mensagem RCS

Para seu tipo de mensagem RCS, escolha entre **Texto** ou **Mídia**.

![Opções para selecionar entre um tipo de mensagem Texto ou Mídia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Como o nome sugere, mensagens de texto RCS focam no texto como meio. Se você digitar até 160 caracteres, a mensagem RCS é cobrada como uma mensagem apenas de texto (ou "básica"). Se você exceder 160 caracteres ou usar um elemento rico, a mensagem é cobrada como uma mensagem RCS rica (ou "única") (e o limite de caracteres aumenta para 3072 caracteres). 

#### Recursos

- Os tipos de mensagens de texto incluem todos os recursos de SMS. Apenas o Rastreamento Avançado é possível para rastreamento de cliques em URL, proporcionando granularidade de relatórios em nível de usuário. 
- Além disso, agora você tem a opção de incluir **Respostas Sugeridas** e **Ações Sugeridas** envolventes que impulsionam ações de usuário de alta interação, como visitar uma landing page ou fazer um pedido. 
    - **Respostas Sugeridas** são botões contendo respostas sugeridas para os usuários clicarem e preencherem automaticamente em sua entrada de texto, removendo a dificuldade de pensar em uma resposta ao fornecer um conjunto restrito de opções para eles. 
    - **Ações Sugeridas** são botões que iniciam uma ação no dispositivo do usuário. Eles geralmente consistem em uma das duas palavras descritivas e um ícone visual para ajudar o usuário a entender o que o botão faz. A Braze atualmente suporta Ações Sugeridas OpenURL. Isso funciona de maneira semelhante a uma URL, onde os usuários que selecionam o botão são redirecionados para uma página da web ou outro local identificado por URL. 

![Um GIF de três Ações Sugeridas para uma mensagem RCS promovendo estilos de moda em alta: "Realeza de conto de fadas", "Academia ousada" e "Mostre-me seus outros estilos".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considerações

- Para limites de caracteres em texto, você pode escrever até 160 caracteres para uma mensagem RCS apenas de texto (básica) ou até 3072 para uma mensagem RCS rica (única). 
- Para limites de botões, você pode adicionar até cinco botões por mensagem. Esses botões podem ser ações sugeridas ou respostas sugeridas.
- Blocos de texto mais longos e muitos botões podem frustrar os usuários, então, sempre que possível, recomendamos optar pela simplicidade. 
- Em alguns casos, pode ser mais econômico enviar mensagens de texto mais longas apenas por RCS do que por SMS. Isso ocorre porque mensagens SMS mais longas são divididas em vários segmentos, cada um dos quais é cobrado, enquanto mensagens RCS são cobradas por mensagem. Entre em contato com seu gerente de conta da Braze para mais detalhes e orientações.
{% endtab %}

{% tab Media %}
Mensagens de mídia RCS permitem que você use formatos de mídia envolventes que não são possíveis com SMS. Esses incluem arquivos de imagem, vídeo e documento. Essas opções de mídia existem para ajudar você a engajar seu público ainda mais profundamente e habilitar casos de uso totalmente novos. No momento, apenas o upload de imagens é suportado através da [Biblioteca de Mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Recursos

- Tipos de mensagens de mídia suportam tudo disponível nos tipos de mensagens de texto, que incluem texto, respostas sugeridas e ações sugeridas.
- Suporta arquivos de imagem, incluindo formatos de arquivo JPEG e PNG. Arquivos de imagem estão disponíveis através do upload da Biblioteca de Mídia. 
- Suporta arquivos de vídeo, incluindo formatos de arquivo MP4, MPEG e MV4. Arquivos de vídeo podem ser adicionados por URL diretamente no criador de mensagem. 
- Suporta arquivos de documento no formato PDF. Arquivos de documento podem ser adicionados através da URL diretamente no criador de mensagem. 

![Criador de RCS com uma opção para fazer upload de um arquivo de mídia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Especificações do arquivo

| Tipo de arquivo | Especificações |
| --- | --- |
| Tudo | \- O tamanho do arquivo é limitado a 100 MB <br><br>\- A URL do arquivo pode ter até 2048 caracteres |
| Arquivos de imagem | Os formatos de arquivo suportados incluem JPG, JPEG e GIF
| Arquivos de vídeo | Os formatos de arquivo suportados incluem H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Arquivos de documento | Formatos de arquivo suportados: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considerações

A experiência do usuário ao receber mensagens RCS pode variar ligeiramente com base em vários fatores, incluindo cobertura da operadora no país de destino, hardware do dispositivo móvel e sistema operacional do dispositivo móvel. 

De modo geral, o RCS se integra de forma mais natural com dispositivos Android (esse método foi amplamente implementado pelo Google, e a troca de mensagens RCS ponto a ponto é amplamente adotada pela comunidade Android). Dispositivos diferentes podem apresentar a experiência em diferentes velocidades e qualidades.  
{% endtab %}
{% endtabs %}

### Etapa 3: Componha sua mensagem RCS

Escreva sua mensagem usando idiomas e personalização ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) e emojis) conforme necessário. Certifique-se de respeitar nossos limites de cópia de mensagens para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de prosseguir, leia nossas [diretrizes para limites de mensagens RCS](#step-2-select-your-rcs-message-type). As mensagens RCS são [cobradas por mensagem]({{site.baseurl}}/sms_rcs_billing_calculators/), então é uma boa ideia entender as nuances do que pode ser incluído em cada tipo de mensagem RCS.
{% endalert %}

### Etapa 4: Pré-visualize e teste sua mensagem

Como a renderização do RCS é controlada pelo sistema operacional do usuário, fabricante do dispositivo, operadora e aplicativo de mensagens (por exemplo, Google Messages vs. Apple Messages), a aparência da mensagem pode variar. Como resultado, a prévia do RCS mostrada no Braze pode não corresponder exatamente ao que um usuário final recebe. As diferenças podem incluir layout, dimensionamento de mídia, botões, elementos de marca ou recursos suportados. O Braze sempre recomenda que você faça uma prévia e teste sua mensagem antes de enviá-la. Use a guia **Teste** para enviar um RCS de teste para grupos de teste de conteúdo ou usuários individuais e pré-visualizar a mensagem como um usuário diretamente no Braze. No entanto, a renderização final deve sempre ser validada em dispositivos reais sempre que possível, pois o Braze não pode garantir paridade perfeita entre todas as combinações de SO, dispositivo e operadora.


### Etapa 5: Crie o restante de sua campanha ou Canva

Em seguida, construa o restante da sua campanha ou canva. Consulte as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para construir mensagens RCS.

#### Etapa 5.1: Escolha a programação ou o disparo da entrega

As mensagens RCS podem ser entregues com base em um horário agendado, uma ação ou um disparador de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o horário de silêncio.

Especifique seus controles de entrega, como permitir que os usuários se tornem novamente elegíveis para receber a campanha ou habilitar regras de limitação de frequência.

#### Etapa 5.2: Escolha os usuários a serem direcionados

Alvo usuários escolhendo segmentos ou filtros para restringir seu público. Você já deve ter selecionado o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você.

{% multi_lang_include target_audiences.md %}

Em seguida, você seleciona o público maior de seus segmentos e restringe ainda mais esse segmento com filtros opcionais [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Você recebe automaticamente uma prévia de como é a população aproximada desse segmento. Lembre-se de que a associação exata ao segmento é sempre calculada antes que a mensagem seja enviada.

{% alert tip %}
Interessado em usar o redirecionamento RCS para direcionar usuários com base em suas interações SMS e RCS? Consulte [Redirecionamento]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Etapa 5.3: Selecionar eventos de conversão

Braze permite que você acompanhe com que frequência os usuários realizam ações específicas ou eventos de conversão após receber uma campanha. É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso de sua campanha. Por exemplo:
- Se você estiver usando geotargeting para disparar uma mensagem RCS que tem como objetivo final o usuário fazer uma compra, defina o evento de conversão para **Compra**.
- Se você estiver tentando levar o usuário ao seu app, defina o evento de conversão para **Inicia Sessão**.

Também é possível definir eventos personalizados de conversão com base em seu caso de uso específico. Seja criativo com a forma como você realmente deseja medir o sucesso da sua campanha.

### Etapa 6: Revisão e implementação

Depois de terminar de construir sua campanha ou canva, revise seus detalhes, teste-a e, em seguida, envie-a!

Em seguida, consulte [Relatório para SMS, MMS e RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) para aprender como você pode acessar os resultados de suas campanhas RCS.

## Dicas

### Usando Liquid para personalização de mensagens

Se você planeja usar Liquid, certifique-se de incluir um valor padrão para sua personalização escolhida, para que, se o perfil do usuário destinatário estiver incompleto, ele não receba um espaço reservado em branco `Hi, !` em vez de seu nome ou uma frase coerente.

### Geração de cópia de IA

Precisa de ajuda para criar textos envolventes? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira um nome ou descrição do produto, e a IA gerará textos de marketing semelhantes aos humanos para uso no seu envio de mensagens.

![Criador de mensagem com um ícone para abrir o assistente de copywriting IA.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Perguntas frequentes

### Posso enviar mensagens de voz pré-gravadas com RCS?

Sim, você pode usar mensagens de mídia para suportar arquivos de áudio.
