---
nav_title: Formulário de inscrição para SMS e WhatsApp
article_title: Formulário de inscrição para SMS e WhatsApp
alias: "/phone_number_capture/"
description: "Esta página de referência aborda como criar um formulário de inscrição para SMS e WhatsApp com o editor de arrastar e soltar mensagens no app."
---

# Formulário de inscrição para SMS e WhatsApp

> Os formulários de inscrição para SMS e WhatsApp são modelos disponíveis no editor de arrastar e soltar para mensagens no app. Use esses modelos para coletar números de telefone de usuários e aumentar seus grupos de inscrições de SMS e WhatsApp.

![Três exemplos de mensagens no app criadas usando o modelo de formulário de inscrição por telefone.][img7]

## Requisitos do SDK

### Versões mínimas do SDK

As mensagens criadas usando o editor de arrastar e soltar só podem ser enviadas a usuários com as seguintes versões mínimas do SDK. Consulte a seção [Pré-requisitos][1] de [Criação de uma mensagem no app com arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) para obter mais detalhes e nuances que devem ser observados.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versões do SDK para links de texto

Se quiser incluir links de texto que não descartem a mensagem, os usuários devem ter as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Se você incluir um link em sua mensagem no app que redirecione para um URL e o usuário final não estiver nas versões mínimas do SDK especificadas, clicar no link fechará a mensagem e o usuário não poderá retornar à mensagem para enviar o formulário.
{% endalert %}

## Criação de um formulário de inscrição-se para número de telefone

Ao criar uma mensagem no app do tipo arrastar e soltar, selecione **inscrição por SMS** ou **inscrição por WhatsApp** como modelo.

![Modal para selecionar o registro de SMS ou o registro de WhatsApp como modelo ao criar uma mensagem no app.][img2]{: style="max-width:70%"}

Esses modelos são compatíveis tanto com apps móveis quanto com navegadores da Web.

### Etapa 1: Configure seus estilos de mensagens

Antes de começar a personalizar seu modelo, você pode definir estilos no nível da mensagem para toda a mensagem usando o menu lateral. Por exemplo, talvez você queira personalizar a fonte de todo o texto ou a cor de todos os links incluídos em sua mensagem. Também é possível tornar a mensagem um tipo de exibição modal ou de tela cheia.

![Fluxo de trabalho para fazer upload e selecionar uma fonte personalizada.][img6]

### Etapa 2: Personalize o componente de entrada do número de telefone

Para começar a criar seu formulário de inscrição, selecione o componente de entrada de número de telefone no editor.

![Área prévia ao criar um formulário de inscrição-se com o componente de entrada de número de telefone selecionado.][img3]{: style="max-width:40%"}

No menu lateral, especifique para qual grupo de inscrições esse modelo coletará números de telefone. Para aderir às práticas recomendadas de conformidade, você só pode coletar o consentimento para um grupo de inscrições por formulário de inscrição de número de telefone. No entanto, se desejar, você pode usar vários formulários para coletar o consentimento de outros grupos de inscrições.

![Menu suspenso do grupo de inscrições com um grupo de inscrições selecionado.][img4]{: style="max-width:40%"}

Por padrão, coletamos números globalmente, mas você pode limitar o número de países para coletar números. Isso é útil se você pretende enviar mensagens apenas para usuários que tenham números de telefone em países específicos e pode ajudar na limpeza da lista. Para fazer isso, desative a opção **Coletar números de todos os países** e use o menu suspenso para selecionar países específicos. Seus usuários só poderão selecionar os países que você adicionou explicitamente.

![Lista suspensa Países para selecionar os países dos quais você deseja coletar números.][img5]{: style="max-width:40%"}

#### Números de telefone inválidos

Se os seus usuários inserirem um número de telefone que inclua caracteres especiais não aceitos, eles verão um indicador de erro genérico que não é personalizável e não poderão enviar o formulário. É possível visualizar o comportamento do erro na guia **Preview & Test** e em seu dispositivo de teste. Consulte este artigo para saber [como o Braze formata números telefônicos][2].

### Etapa 3: Adicionar linguagem de isenção de responsabilidade (para formulários de inscrição em SMS)

Para formulários de inscrição por SMS, é importante comunicar claramente o tipo de SMS que será enviado. Confira se o crescimento de sua lista está em conformidade, incluindo as seguintes informações em seu formulário:

- Descrição dos tipos de mensagens SMS que seus clientes podem esperar (lembretes de carrinho, promoções e ofertas, lembretes de compromissos, etc.). Não é necessário listar todos os casos de uso, mas você deve fornecer uma descrição dos tipos de mensagens que sua marca enviará.
- Note que o consentimento não é uma condição para qualquer compra (se aplicável).
- Frequência de mensagens e lembrete de que se aplicam taxas de mensagens e dados. Se não souber a frequência exata das mensagens, você pode dizer que a frequência pode variar.
- Links para seus Termos e Condições e Política de Privacidade de SMS.
- Lembrete de ajuda e palavras-chave de aceitação (HELP para ajuda; STOP para cancelar).

Fornecemos um aviso de isenção de responsabilidade no modelo apenas como exemplo - ele não constitui aconselhamento jurídico e não deve ser considerado para fins de conformidade. É importante trabalhar com sua equipe jurídica para desenvolver uma linguagem adaptada à sua marca específica.

{% alert note %}
Esta documentação não tem a intenção de fornecer, nem pode ser considerada como aconselhamento jurídico.
{% endalert %}

Para saber mais sobre a conformidade com SMS, consulte [Leis e regulamentos de SMS][4].

### Etapa 4: Estilize sua mensagem

Você pode personalizar a aparência de sua mensagem usando os [componentes de mensagem no app do][3] tipo arrastar e soltar.

## Relatórios

Após o lançamento da campanha, é possível analisar os resultados em tempo real para ver quantos usuários se engajaram na campanha. Para ver quantos usuários aceitaram o grupo de inscrições, é possível [criar um segmento][5] de usuários que se inscreveram no grupo de inscrições filtrando os usuários que receberam a mensagem no app e enviaram o formulário.

![Painel de performance da mensagem no app mostrando os cliques para cada link na mensagem no app.][img8]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}
