---
nav_title: "Formulário de inscrição para SMS, RCS e WhatsApp"
article_title: "Formulário de inscrição para SMS, RCS e WhatsApp"
alias: "/phone_number_capture/"
page_order: 1
description: "Esta página aborda como criar um formulário de inscrição de SMS, RCS e WhatsApp com o editor de arrastar e soltar de mensagens no aplicativo."
---

# Formulário de inscrição para SMS, RCS e WhatsApp

> Os formulários de registro de SMS, RCS e WhatsApp são modelos disponíveis no editor de arrastar e soltar para mensagens no aplicativo. Use esses modelos para coletar os números de telefone dos usuários e aumentar seus grupos de assinatura de SMS, MMS, RCS e WhatsApp.

\![Três exemplos de mensagens in-app criadas usando o modelo de formulário de registro telefônico.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criação de um formulário de registro de número de telefone

### Etapa 1: Escolha seu modelo

Ao criar uma mensagem no aplicativo com a função arrastar e soltar, selecione **Inscrição de SMS** (isso acomoda a inscrição de RCS) ou **Inscrição de WhatsApp** para seu modelo e, em seguida, selecione **Criar mensagem**. Esses modelos são compatíveis tanto com aplicativos móveis quanto com navegadores da Web.

Modal para selecionar o registro de SMS ou o registro do WhatsApp como modelo ao criar uma mensagem no aplicativo.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Etapa 2: Configure seus estilos de mensagem

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

Fluxo de trabalho de carregamento e seleção de uma fonte personalizada.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Etapa 3: Personalize o componente de entrada do número de telefone

Para começar a criar seu formulário de inscrição, selecione o componente de entrada de número de telefone no editor.

\![Área de visualização ao criar um formulário de inscrição com o componente de entrada de número de telefone selecionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

No menu lateral, especifique para qual grupo de assinatura esse modelo coletará números de telefone. Para aderir às práticas recomendadas de conformidade, você só pode coletar consentimento para um grupo de assinatura por formulário de inscrição de número de telefone. No entanto, se desejar, você pode usar vários formulários para coletar consentimento para outros grupos de assinatura.

dropdown Grupo de assinaturas com um grupo de assinaturas selecionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Por padrão, coletamos números globalmente, mas você pode limitar o número de países para coletar números. Isso é útil se você pretende enviar mensagens apenas para usuários que tenham números de telefone em países específicos e pode ajudar na limpeza da lista. Para fazer isso, desative a opção **Coletar números de todos os países** e use o menu suspenso para selecionar países específicos. Seus usuários só poderão selecionar os países que você adicionou explicitamente.

Selecione o menu suspenso Países para selecionar os países dos quais deseja coletar números.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Números telefônicos inválidos

Se os seus usuários inserirem um número de telefone que inclua caracteres especiais não aceitos, eles verão um indicador de erro genérico que não é personalizável e não poderão enviar o formulário. Você pode visualizar o comportamento do erro na guia **Preview & Test** e em seu dispositivo de teste. Consulte este artigo para saber [como o Braze formata números telefônicos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Etapa 4: Adicionar linguagem de isenção de responsabilidade (para formulários de registro de SMS e RCS)

Para formulários de inscrição de SMS e RCS, é importante comunicar claramente o tipo de SMS ou RCS que você enviará. Certifique-se de que o crescimento de sua lista esteja em conformidade, incluindo as seguintes informações em seu formulário:

- Descrição dos tipos de mensagens SMS e RCS que seus clientes podem esperar (lembretes de carrinho, promoções e ofertas, lembretes de compromissos, etc.). Não é necessário listar todos os casos de uso, mas você deve fornecer uma descrição dos tipos de mensagens que sua marca enviará.
- Observe que o consentimento não é uma condição para qualquer compra (se aplicável).
- Frequência de mensagens e lembrete de que se aplicam taxas de mensagens e dados. Se você não souber a frequência exata da mensagem, pode dizer que a frequência pode variar.
- Links para seus Termos & Condições e Política de Privacidade de SMS e RCS.
- Lembrete de ajuda e palavras-chave de cancelamento (HELP para ajuda; STOP para cancelar).

Fornecemos um aviso de isenção de responsabilidade no modelo apenas como exemplo - ele não constitui aconselhamento jurídico e não deve ser considerado para fins de conformidade. É importante trabalhar com sua equipe jurídica para desenvolver uma linguagem adaptada à sua marca específica.

{% alert note %}
Esta documentação não tem a intenção de fornecer, nem pode ser considerada como aconselhamento jurídico.
{% endalert %}

Para obter mais informações sobre conformidade com SMS e RCS, consulte [Leis e regulamentos para SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Etapa 5: Estilize sua mensagem

Personalize a aparência de sua mensagem usando os [componentes de mensagem no aplicativo do]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) tipo arrastar e soltar.

## Análise dos resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

Painel de desempenho da mensagem in-app mostrando os cliques de cada link na mensagem in-app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


