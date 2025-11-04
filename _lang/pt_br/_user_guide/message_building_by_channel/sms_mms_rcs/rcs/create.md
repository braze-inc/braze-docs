---
nav_title: "Criando uma mensagem RCS"
article_title: Criando uma Mensagem RCS
page_order: 2
alias: /create_rcs_message/
description: "Este artigo cobre como criar uma mensagem RCS."
page_type: reference
channel:
  - RCS
---

# Criando uma mensagem RCS

> Campanhas RCS são ótimas para alcançar diretamente e conversar programaticamente com seus clientes. Você pode usar Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promove e melhora uma experiência de usuário discreta com sua marca.

## Criando uma mensagem RCS

### Passo 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada usando uma campanha ou um Canvas? Campanhas são melhores para campanhas de mensagens únicas e simples, enquanto Canvases são melhores para jornadas de usuários em múltiplas etapas.

{% tabs %}
{% tab Campaign %}
1. Vá para **Mensagens** > **Campanhas** e selecione **Criar Campanha**.
2. Selecione **SMS/MMS/RCS**, ou, para campanhas que visam múltiplos canais, selecione **Multicanal**.
3. Dê um nome claro e significativo à sua campanha.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * Tags tornam suas campanhas mais fáceis de encontrar e construir relatórios. Por exemplo, ao usar o [Construtor de Relatórios]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.

{: start="5"}
5\. Adicione e nomeie quantas variantes precisar para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para mais informações sobre este tópico, consulte [Testes Multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Teste de variantes de SMS e RCS**: A Braze permite que você inclua tanto variantes de SMS quanto de RCS dentro de uma única campanha, permitindo que você compare o desempenho de cada uma. Você pode adicionar variantes de SMS e RCS durante o primeiro passo da composição da mensagem.

{: start="6"}
6\. Selecione um [grupo de assinatura]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Ao selecionar um grupo de assinatura, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos receberão a campanha. Apenas códigos longos e curtos que pertencem a esse grupo de assinatura serão usados para enviar SMS aos usuários-alvo.
- **Fallback de SMS**: A Braze recomenda fortemente que todo grupo de assinatura que contém um remetente de RCS também inclua pelo menos um código de SMS para fallback. Isso é importante para a entregabilidade nos casos em que as mensagens de RCS falham ao serem entregues. Algumas razões para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura de operadora incompleta em um determinado país ou região. Ao habilitar o fallback de SMS, sua mensagem ainda será entregue ao seu usuário e você nunca perderá essa oportunidade de se conectar com eles.   

{: start="7"}
7\. Escolha entre SMS e RCS. Antes de compor mensagens de RCS, escolha o canal com o qual você enviará. Geralmente, recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre fornecemos a opção de enviar com SMS para que você tenha máxima flexibilidade e controle. 

\![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar variantes adicionais. Você pode então escolher **Copiar da Variante** no menu suspenso **Adicionar Variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione um passo de Mensagem **SMS/MMS/RCS** no construtor de Canvas. 
3. Nomeie seu passo de forma clara e significativa.
4. Selecione um [grupo de assinatura]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Ao selecionar um grupo de assinatura, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos receberão a campanha. Apenas códigos longos e curtos que pertencem a esse grupo de assinatura serão usados para direcionar os usuários.
- **Fallback de SMS**: A Braze recomenda fortemente que todo grupo de assinatura que contém um remetente de RCS também inclua pelo menos um código de SMS para fallback. Isso é importante para a entregabilidade nos casos em que as mensagens de RCS falham ao serem entregues. Algumas razões para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura de operadora incompleta em um determinado país ou região. Ao habilitar o fallback de SMS, sua mensagem ainda será entregue ao seu usuário e você nunca perderá essa oportunidade de se conectar com eles.

{: start="5"}
5\. Escolha entre SMS e RCS. Antes de compor mensagens de RCS, escolha o canal com o qual você enviará. Geralmente, recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre fornecemos a opção de enviar com SMS para que você tenha máxima flexibilidade e controle. 

\![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Passo 2: Selecione seu tipo de mensagem RCS

Para seu tipo de mensagem RCS, escolha entre **Texto** ou **Mídia**.

\![Opções para selecionar entre um tipo de mensagem de Texto ou Mídia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Como o nome sugere, mensagens de texto RCS focam no texto como meio. Se você digitar até 160 caracteres, a mensagem RCS é cobrada como uma mensagem apenas de texto (ou "básica"). Se você exceder 160 caracteres ou usar um elemento rico, a mensagem é cobrada como uma mensagem RCS rica (ou "única") (e o limite de caracteres aumenta para 3072 caracteres). 

#### Recursos

- Os tipos de mensagens de texto incluem todos os recursos de SMS. Apenas o Rastreamento Avançado é possível para rastreamento de cliques em URLs, proporcionando granularidade de relatórios em nível de usuário. 
- Além disso, agora você tem a opção de incluir **Respostas Sugeridas** e **Ações Sugeridas** que impulsionam ações de usuário de alta interação, como visitar uma página de destino ou fazer um pedido. 
    - **Respostas Sugeridas** são botões contendo respostas sugeridas para os usuários clicarem e preencherem automaticamente em sua entrada de texto, removendo a fricção de ter que pensar em uma resposta, fornecendo um conjunto restrito de escolhas para eles. 
    - **Ações Sugeridas** são botões que iniciam uma ação no dispositivo do usuário. Eles geralmente consistem em uma das duas palavras descritivas e um ícone visual para ajudar o usuário a entender o que o botão faz. Atualmente, o Braze suporta Ações Sugeridas OpenURL. Isso funciona de maneira semelhante a uma URL, onde os usuários que selecionam o botão são redirecionados para uma página da web ou outro local identificado por URL. 

\![Um GIF de três Ações Sugeridas para uma mensagem RCS promovendo estilos de moda em alta: "Realeza de conto de fadas", "Academia ousada" e "Mostre-me seus outros estilos".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considerações

- Para limites de caracteres em texto, você pode escrever até 160 caracteres para uma mensagem RCS apenas de texto (básica) ou até 3072 para uma mensagem RCS rica (única). 
- Para limites de botões, você pode adicionar até cinco botões por mensagem. Esses botões podem ser ações sugeridas ou respostas sugeridas.
- Blocos de texto mais longos e muitos botões podem frustrar os usuários, então, sempre que possível, recomendamos optar pela simplicidade. 
- Em alguns casos, pode ser mais econômico enviar mensagens mais longas apenas de texto através do RCS do que com SMS. Isso ocorre porque mensagens SMS mais longas são divididas em vários segmentos, cada um dos quais é cobrado, enquanto mensagens RCS são cobradas por mensagem. Entre em contato com seu gerente de conta Braze para mais detalhes e orientações.
{% endtab %}

{% tab Media %}
Mensagens de mídia RCS permitem que você use formatos de mídia envolventes que não são possíveis com SMS. Esses incluem arquivos de imagem, vídeo e documento. Essas opções de mídia existem para ajudar você a envolver ainda mais seu público e possibilitar casos de uso totalmente novos. No momento, apenas o upload de imagens é suportado através da [Biblioteca de Mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

#### Recursos

- Os tipos de mensagens de mídia suportam tudo disponível nos tipos de mensagens de texto, que incluem texto, respostas sugeridas e ações sugeridas.
- Suporta arquivos de imagem, incluindo formatos de arquivo JPEG e PNG. Arquivos de imagem estão disponíveis para upload a partir da Biblioteca de Mídia. 
- Suporta arquivos de vídeo, incluindo formatos de arquivo MP4, MPEG e MV4. Os arquivos de vídeo podem ser adicionados por URL diretamente no compositor de mensagens. 
- Suporta arquivos de documentos no formato PDF. Os arquivos de documentos podem ser adicionados através da URL diretamente no compositor de mensagens. 

\![Compositor RCS com uma opção para enviar um arquivo de mídia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Especificações do arquivo

| Tipo de arquivo | Especificações |
| --- | --- |
| Todos | \- O tamanho do arquivo é limitado a 100 MB <br><br>\- A URL do arquivo pode ter até 2048 caracteres |
| Arquivos de imagem | Os formatos de arquivo suportados incluem JPG, JPEG e GIF
| Arquivos de vídeo | Os formatos de arquivo suportados incluem H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Arquivos de documentos | Formatos de arquivo suportados: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considerações

A experiência do usuário ao receber mensagens RCS pode variar ligeiramente com base em vários fatores, incluindo cobertura da operadora no país de destino, hardware do dispositivo móvel e sistema operacional do dispositivo móvel. 

De modo geral, o RCS se integra mais naturalmente com dispositivos Android (esse método foi amplamente implementado pelo Google, e a troca de mensagens RCS ponto a ponto é amplamente adotada pela comunidade Android). Dispositivos diferentes podem apresentar a experiência em diferentes velocidades e qualidades.  
{% endtab %}
{% endtabs %}

### Passo 3: Componha sua mensagem RCS

Escreva sua mensagem usando idiomas e personalização ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) e emojis) conforme necessário. Certifique-se de respeitar nossos limites de cópia de mensagem para reduzir suas chances de cobranças adicionais.

{% alert important %}
Antes de prosseguir, leia nossas [diretrizes para limites de mensagens RCS](#step-2-select-your-rcs-message-type). As mensagens RCS são [cobradas por mensagem]({{site.baseurl}}/sms_rcs_billing_calculators/), então é uma boa ideia entender as nuances do que pode ser incluído em cada tipo de mensagem RCS.
{% endalert %}

### Passo 4: Visualize e teste sua mensagem

A Braze sempre recomenda visualizar e testar sua mensagem antes de enviar. Vá para a aba **Teste** para enviar um RCS de teste para grupos de teste de conteúdo ou usuários individuais, ou visualize a mensagem como um usuário diretamente na Braze.

### Passo 5: Construa o restante de sua campanha ou Canvas

Em seguida, construa o restante de sua campanha ou Canvas. Consulte as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para construir mensagens RCS.

#### Passo 5.1: Escolha o cronograma de entrega ou gatilho

As mensagens RCS podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para mais informações, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e as Horas Silenciosas.

Especifique seus controles de entrega, como permitir que os usuários se tornem re-eligíveis para receber a campanha ou habilitar regras de limitação de frequência.

#### Passo 5.2: Escolha os usuários a serem segmentados

Segmentar usuários escolhendo segmentos ou filtros para restringir seu público. Você já deve ter selecionado o grupo de assinatura, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você.

{% multi_lang_include target_audiences.md %}

Em seguida, você selecionará o público maior de seus segmentos e restringirá ainda mais esse segmento com filtros opcionais [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Você receberá automaticamente uma prévia de como essa população de segmento aproximada se parece agora. Tenha em mente que a associação exata do segmento é sempre calculada pouco antes da mensagem ser enviada.

{% alert tip %}
Interessado em usar retargeting RCS para segmentar usuários com base em suas interações SMS e RCS? Consulte [Retargeting]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Passo 5.3: Escolha eventos de conversão

Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, ou eventos de conversão, após receber uma campanha. Você pode permitir uma janela de até 30 dias durante a qual uma conversão será contada se o usuário realizar a ação especificada.

Eventos de conversão ajudam você a medir o sucesso de sua campanha. Por exemplo:
- Se você estiver usando geotargeting para acionar uma mensagem RCS que tem como objetivo final o usuário realizar uma compra, defina o evento de conversão como **Compra**.
- Se você estiver tentando levar o usuário ao seu aplicativo, defina o evento de conversão como **Inicia Sessão**.

Você também pode definir eventos de conversão personalizados com base em seu caso de uso específico. Seja criativo com a forma como você realmente deseja medir o sucesso de sua campanha.

### Passo 6: Revise e implante

Depois de terminar de construir sua campanha ou Canvas, revise seus detalhes, teste-o e, em seguida, envie-o!

Em seguida, consulte [Relatório para SMS, MMS e RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) para aprender como você pode acessar os resultados de suas campanhas RCS.

## Dicas

### Usando Liquid para personalização de mensagens

Se você planeja usar Liquid, certifique-se de incluir um valor padrão para sua personalização escolhida, para que, se o perfil do usuário do destinatário estiver incompleto, ele não receba um espaço reservado em branco `Hi, !` em vez de seu nome ou uma frase coerente.

### Gerando cópia de IA

Precisa de ajuda para criar cópias envolventes? Tente usar o [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira um nome ou descrição de produto, e a IA gerará uma cópia de marketing semelhante à humana para uso em suas mensagens.

\![Compositor de mensagens com um ícone para abrir o assistente de redação de IA.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Perguntas frequentes

### Posso enviar mensagens de voz pré-gravadas com RCS?

Sim, você pode usar mensagens de mídia para suportar arquivos de áudio.
