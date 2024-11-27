---
nav_title: Formulário de inscrição de e-mail
article_title: Formulário de inscrição de e-mail
alias: "/email_capture/"
description: "Esta página de referência aborda como criar um formulário de envio de e-mail com o editor de arrastar e soltar mensagens no app."
---

# Formulário de inscrição de e-mail

> Use o modelo de mensagem no app de arrastar e soltar para fazer a inscrição por e-mail para coletar os endereços de e-mail dos usuários e aumentar seus grupos de inscrições.

## Requisitos do SDK

### Versões mínimas do SDK

As mensagens criadas usando o editor de arrastar e soltar só podem ser enviadas a usuários com as seguintes versões mínimas do SDK. Consulte a seção [Pré-requisitos][1] do artigo [Criando uma mensagem no app com o recurso de arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) para obter mais detalhes e nuances que devem ser observados.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versões do SDK para links de texto

Se quiser incluir links de texto que não descartem a mensagem, os usuários devem ter as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Se você incluir um link em sua mensagem no app que redireciona para um URL e o usuário não estiver nas versões mínimas do SDK especificadas, clicar no link fechará a mensagem e o usuário não poderá retornar à mensagem para enviar o formulário.
{% endalert %}

## Criação de um formulário de envio de e-mail

Ao criar uma mensagem no app do tipo arrastar e soltar, selecione **Envio de e-mail** para seu modelo e selecione **Criar mensagem**. Esse modelo é compatível tanto com apps móveis quanto com navegadores da Web.

### Etapa 1: Configure seus estilos de mensagens

Antes de começar a personalizar seu modelo, você pode definir estilos no nível da mensagem para toda a mensagem usando o menu lateral. Por exemplo, talvez você queira personalizar a fonte de todo o texto ou a cor de todos os links incluídos em sua mensagem. Também é possível tornar a mensagem um tipo de exibição modal ou de tela cheia.

### Etapa 2: Personalize o componente de envio de e-mail

Para começar a criar seu formulário de envio de e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed (Inscrito**). Para fazer a aceitação de usuários em grupos de inscrições específicos, consulte [Atualização de estados de envio de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Você pode personalizar o texto do espaço reservado e o texto do rótulo do elemento de captura de e-mail.

#### Validação de e-mail

Se o usuário inserir um endereço de e-mail que inclua caracteres especiais não aceitos, ele verá um indicador de erro genérico e não poderá enviar o formulário. Essa mensagem de erro não pode ser enviada de mensagens personalizadas. É possível visualizar o comportamento do erro na guia **Preview & Test** e em seu dispositivo de teste. Saiba mais sobre como a Braze formata endereços de e-mail em [Validação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Etapa 3: Adicionar linguagem de isenção de responsabilidade (opcional)

Recomendamos incluir em sua mensagem uma linguagem de aceitação e links para a política de privacidade e os termos e condições de sua marca. Fornecemos um aviso de isenção de responsabilidade no modelo apenas como exemplo, mas isso não deve ser considerado para fins de conformidade. Certifique-se de trabalhar com sua equipe jurídica para desenvolver uma linguagem adaptada à sua marca específica.

{% alert note %}
As práticas recomendadas de entregabilidade geralmente excedem os requisitos legais, e nossa recomendação é sempre obter o consentimento explícito para o envio de e-mails e permitir que os usuários recusem facilmente.
{% endalert %}

### Etapa 4: Estilize sua mensagem

Você pode personalizar a aparência de sua mensagem usando os [componentes de mensagem no app do][3] tipo arrastar e soltar.

## Relatórios

Após o lançamento da campanha, é possível analisar os resultados em tempo real para ver quantos usuários se engajaram na campanha. Para ver quantos usuários aceitaram o grupo de inscrições, é possível [criar um segmento][5] de usuários que se inscreveram no grupo de inscrições filtrando os usuários que receberam a mensagem no app e enviaram o formulário.

## Práticas recomendadas

### Verificação de aceitação dupla

Para ter certeza de que quem se inscreveu na sua lista quis se inscrever nela e forneceu o endereço de e-mail correto, recomendamos obter uma segunda confirmação de quem se inscreveu por meio do formulário de inscrição de e-mail, enviando um fluxo de [aceitação dupla](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in).

Uma das maneiras de configurar isso é por meio do Canvas Flow:

1. Crie uma tela baseada em ação e configure-a para disparar quando um usuário adicionar um endereço de e-mail ao Braze. Certifique-se de permitir o direcionamento de usuários que são novos na plataforma (por exemplo, usando um segmento sem filtros na tela).
2. Crie uma etapa de envio de e-mail com uma CTA que tenha um hiperlink para a tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid. Isso mudará o estado da inscrição de e-mail do usuário para `opted_in` quando ele clicar no botão.
3. Adicione uma [etapa de jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. Para a primeira jornada, dispare um e-mail quando um usuário alterar seu status de inscrição de e-mail para `opted_in`. Esse e-mail deve informar aos usuários que seu e-mail foi confirmado.
5. Configure a outra jornada para sair do Canva depois que a janela expirar.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
