---
nav_title: Tratamento personalizado de palavras-chave
article_title: Manuseio de palavras-chave personalizadas
page_order: 3
description: "Este artigo de referência aborda como o Braze lida com mensagens SMS, MMS e RCS bidirecionais e respostas automáticas. Isso inclui explicações sobre como funciona o acionamento de palavras-chave, bem como categorias de palavras-chave personalizadas e suporte a vários idiomas."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Tratamento personalizado de palavras-chave

> Este artigo de referência aborda como o Braze lida com mensagens SMS, MMS e RCS bidirecionais e respostas automáticas. Isso inclui explicações sobre como funciona o acionamento de palavras-chave, bem como categorias de palavras-chave personalizadas e suporte a vários idiomas.

## Mensagens bidirecionais (respostas personalizadas com palavras-chave)

As mensagens bidirecionais permitem que você envie mensagens e processe as respostas a essas mensagens. Ele exige que os usuários finais enviem uma palavra-chave para o Braze, para a qual o usuário receberá uma resposta automática. Aplicadas corretamente, as mensagens bidirecionais podem ser uma solução simples, imediata e dinâmica para o marketing do cliente, economizando tempo e recursos ao longo do processo.

## Gerenciamento de palavras-chave e respostas automáticas

O SMS, o MMS e o RCS com o Braze oferecem a opção de criar acionadores de palavras-chave, respostas personalizadas, definir conjuntos de palavras-chave para vários idiomas e estabelecer categorias de palavras-chave personalizadas. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Adicionar acionadores de palavras-chave

Além das palavras-chave padrão de opt-in e opt-out, você também pode definir suas próprias palavras-chave para acionar respostas de Opt-In, Opt-Out e Ajuda.

Para definir suas próprias palavras-chave, faça o seguinte:

1. No painel do Braze, vá para **Audience** > **Subscription Group Management** e selecione um grupo de assinatura **SMS/MMS/RCS**.<br><br>
2. Em **Global Keywords (Palavras-chave globais**), selecione o ícone de lápis ao lado da categoria de palavra-chave à qual você deseja adicionar uma palavra-chave. \![Palavras-chave de opt-in com o ícone de lápis sendo exibido.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Na guia que se abre, adicione uma palavra-chave que deseja acionar essa categoria de palavra-chave. Observe que as palavras-chave não diferenciam maiúsculas de minúsculas e que as palavras-chave universais como `START`, `YES` e `UNSTOP` não podem ser alteradas. ![Editando palavras-chave para a categoria "Opt-In". As palavras-chave adicionadas são "START" (iniciar), "UNSTOP" (parar) e "YES" (sim). O campo da mensagem de resposta diz: "Você cancelou a assinatura de mensagens deste número. Responder HELP para obter ajuda. Responda STOP para cancelar a assinatura. Podem ser aplicadas taxas de mensagens e dados."]({% image_buster /assets/img/sms/keyword_edit2.png %})

As regras a seguir se aplicam a palavras-chave e respostas a palavras-chave:

| Palavras-chave | Respostas de palavras-chave |
| -------- | ----------------- |
| \- Caracteres codificados em UTF-8 válidos<br>\- Máximo de 20 palavras-chave por categoria no total<br>\- Comprimento máximo de 34 caracteres<br>\- Comprimento mínimo de 1 caractere <br>\- Não pode conter espaços<br>\- É necessário que não diferencie maiúsculas de minúsculas e que seja exclusivo no grupo de assinaturas | \- Não pode estar em branco<br>\- Comprimento máximo de 300 caracteres<br>\- Caracteres UTF-8 válidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Interessado em ver como essas palavras-chave podem ser usadas em suas campanhas e Canvases para redirecionar e acionar mensagens? Visite [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) para obter mais informações.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Gerenciar respostas

Você pode gerenciar suas próprias respostas que são enviadas aos usuários depois que eles digitam uma palavra-chave para uma categoria de palavra-chave específica.

1. No painel do Braze, vá para **Audience** > **Subscription Group Management** e selecione um grupo de assinatura **SMS/MMS/RCS**. <br><br>
2. Em **Palavras-chave globais**, selecione uma categoria de palavra-chave para editar uma resposta selecionando o ícone de lápis. \![Palavras-chave opt-in com o ícone de lápis sendo exibido.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. Na guia que se abre, edite sua resposta. Lembre-se de nossas [seis regras para obter a conformidade correta]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) ao criar sua resposta e leia as regras a seguir que se aplicam a palavras-chave e respostas com palavras-chave. \![Respostas]({% image_buster /assets/img/sms/keyword_home.png %}){: style="max-width:70%;"}<br><br>
4. Para encurtar automaticamente URLs estáticos em sua resposta, selecione a opção **Encurtamento de links**. O contador de caracteres será atualizado para mostrar o tamanho esperado do URL encurtado. \![Um GIF mostrando a atualização do contador de caracteres quando a opção "Link Shortening" está ativada.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

##### Considerações

| Palavras-chave | Respostas de palavras-chave |
| -------- | ----------------- |
| \- Caracteres codificados em UTF-8 válidos<br>\- Máximo de 20 palavras-chave por categoria no total<br>\- Comprimento máximo de 34 caracteres<br>\- Comprimento mínimo de 1 caractere <br>\- Não pode conter espaços<br>\- É necessário que não diferencie maiúsculas de minúsculas e que seja exclusivo no grupo de assinaturas | \- Não pode estar em branco<br>\- Comprimento máximo de 300 caracteres<br>\- Caracteres UTF-8 válidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Se um Canvas baseado em ação for acionado por uma mensagem SMS, MMS ou RCS recebida, você poderá fazer referência às propriedades de SMS, MMS ou RCS na primeira [etapa de mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) do Canvas.
{% endalert %}

## Suporte a vários idiomas

Ao enviar para determinados países, pode ser necessário que o remetente ofereça suporte a palavras-chave de entrada e respostas de saída em um idioma local. Para dar suporte a isso, o Braze permite que você crie uma configuração de palavra-chave específica do idioma.
\![Menu suspenso que exibe os idiomas a serem adicionados como uma configuração de palavra-chave.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Criação de palavras-chave específicas do idioma

Selecione **Add a Language (Adicionar um idioma** ) e selecione o idioma de destino ou pesquise um idioma no menu suspenso.

{% alert important %}
Os idiomas que não são o inglês não vêm com palavras-chave e respostas predefinidas, portanto, os remetentes precisarão trabalhar com suas equipes jurídicas e de marketing para adicionar quaisquer palavras-chave necessárias a esse conjunto. Caso contrário, o Braze não tratará as mensagens recebidas localizadas para esses idiomas.
{% endalert %}

Se você precisar excluir um idioma, selecione o botão **Excluir idioma** no canto inferior direito.

Página de palavras-chave globais com a guia "Italiano" selecionada. Existem guias adicionais para cada idioma adicionado.]({% image_buster /assets/img/sms/multi-language2.png %})

## Categorias de palavras-chave personalizadas

Além das três categorias de palavras-chave padrão (Opt-in, Opt-out e Help), você também pode criar até 25 categorias de palavras-chave próprias. Isso permite que você identifique palavras-chave arbitrárias e configure respostas específicas para sua empresa. Um exemplo de categoria pode ser "PROMO" ou "DISCOUNT", que pode gerar uma resposta sobre promoções que estão acontecendo neste mês. 

Essas palavras-chave personalizadas operam em uma capacidade "sempre ativa", o que significa que qualquer usuário inscrito no seu serviço de mensagens pode enviar mensagens de texto com palavras-chave e receber uma resposta a qualquer momento. Além desse comportamento, você também tem a opção de definir palavras-chave específicas que só podem ser enviadas em [determinados pontos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) do ciclo de vida do usuário. 

\![Palavras-chave para uma categoria "Promo". Se um usuário enviar a mensagem de texto "YO", ele receberá a mensagem com um código promocional.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Criação de uma categoria personalizada

Para criar uma categoria de palavra-chave personalizada, faça o seguinte:

1. Edite o grupo de assinaturas apropriado.
2. Selecione **Adicionar palavra-chave personalizada**. \![Fields to add new keywords (Campos para adicionar novas palavras-chave).]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Forneça um nome de categoria de palavra-chave e defina quais palavras-chave um usuário pode digitar para receber a mensagem de resposta.

Depois que essa categoria de palavra-chave for criada, ela estará disponível para ser filtrada [e acionada]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) em suas campanhas e Canvases.

As palavras-chave criadas em categorias de palavras-chave personalizadas obedecem a todas as regras e validações para a criação de novas palavras-chave. 

### Palavras-chave específicas do ciclo de vida

Se você tiver um caso de uso em que gostaria de limitar o momento em que um cliente pode enviar uma palavra-chave específica durante o ciclo de vida (por exemplo, durante a primeira integração inicial) para receber uma resposta, poderá usar o acionador **Enviar SMS de entrada para o grupo de assinatura dentro da categoria de palavra-chave OUTROS** em sua campanha ou Canvas e definir palavras-chave que seus usuários podem enviar em um determinado momento.

Esse acionador é compatível com a filtragem da mensagem de entrada específica usando comparações de "é" ou "não é" da mensagem, bem como com regras regex de "corresponde" ou "não corresponde" para validar a entrada do usuário.

#### Tela

Etapa do Canvas baseada em ação com o acionador Send inbound SMS to subscription group "Messaging Service" within keyword category "Other" where the message body matches the regular expression "caret symbol skip."]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campanha

Campanha baseada em ação com o acionador Enviar SMS de entrada para o grupo de assinatura "Serviço de mensagens de marketing A" dentro da categoria de palavra-chave "Outro" em que o corpo da mensagem é "Palavra-chave1" ou é "Palavra-chave2" ou não é "Palavra-chave A".]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Lidando com palavras-chave desconhecidas

Embora não seja obrigatório, recomendamos fortemente a configuração de uma resposta automática para quando os usuários enviarem palavras-chave de entrada que não correspondam a uma palavra-chave existente. Essa mensagem notificará o usuário de que a palavra-chave não foi reconhecida e oferecerá algumas orientações. 

Isso pode ser feito com a criação de uma campanha de SMS, MMS ou RCS com uma mensagem como "Sorry! Não reconhecemos essa palavra-chave, enviamos a mensagem STOP para parar ou HELP para ajudar." Em seguida, na etapa de entrega, selecione **Action-Based Delivery** e use o acionador **Sent inbound SMS to subscription group within keyword category OTHER**.

Envio baseado em ação para uma campanha com o acionador "Enviou SMS de entrada para o grupo de assinatura dentro da categoria de palavra-chave "Outro".]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Interessado em ver como essas palavras-chave e categorias de palavras-chave podem ser usadas em suas campanhas e Canvases para redirecionar e acionar mensagens? Visite [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) para obter mais informações.
{% endalert %}

