---
nav_title: Formulário de captura de e-mail
article_title: Formulário de captura de e-mail
page_order: 3
page_type: reference
description: "Este artigo fornece uma visão geral do tipo de mensagem in-app de captura de e-mail."
channel:
  - in-app messages
---

# Formulário de captura de e-mail {#email-capture-form}

> As mensagens de captura de e-mail permitem que você solicite facilmente aos usuários do seu site que enviem o endereço de e-mail, que ficará disponível no perfil do usuário para uso em todas as suas campanhas de mensagens.

Quando um usuário final insere seu endereço de e-mail nesse formulário, o endereço de e-mail é adicionado ao seu perfil de usuário.

- Para [usuários anônimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) que ainda não têm uma conta, o endereço de e-mail ficará no perfil de usuário anônimo que está vinculado ao dispositivo do usuário.
- Se já existir um endereço de e-mail no perfil do usuário, o endereço de e-mail existente será substituído pelo endereço de e-mail recém-inserido.
- Se o usuário conhecido tiver um endereço de e-mail sinalizado como tendo sofrido [hard bounce]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces), verificaremos se o endereço de e-mail recém-inserido é diferente do que está em seu perfil no Braze. Se o endereço de e-mail fornecido for diferente, o endereço de e-mail será atualizado e o status de hard bounce será removido. 
- Se um usuário inserir um endereço de e-mail inválido, ele verá a mensagem de erro: "Digite um e-mail válido."
    - Endereços de e-mail inválidos: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Endereços de e-mail válidos: 
        - `example@gmail.com`
        - `example@gnail.com` (com um erro de digitação)
    - Para obter mais informações sobre a validação de e-mail no Braze, consulte [as diretrizes e notas técnicas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

{% details More on identified versus anonymous users %}

Em geral, a lógica por trás do formulário de captura de e-mail é simples. Isso definirá o endereço de e-mail no perfil do usuário no Braze para o usuário que está ativo no momento. No entanto, isso significa que o comportamento difere com base no fato de o usuário estar identificado (conectado, `changeUser` chamado) ou não.

Se um usuário anônimo inserir seu e-mail no formulário e enviá-lo, o Braze adicionará o endereço de e-mail ao seu perfil. Se o `changeUser` for chamado posteriormente em sua jornada na Web e um novo `external_id` for atribuído (por exemplo, quando um novo usuário se registrar no serviço), todos os dados anônimos do perfil do usuário serão mesclados, inclusive o endereço de e-mail.

Se `changeUser` for chamado com um `external_id` existente, o perfil de usuário anônimo ficará órfão e [os campos de dados específicos do perfil de usuário]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) que ainda não existirem no usuário identificado serão mesclados, mas os campos que já existirem serão perdidos, inclusive o endereço de e-mail.

Para obter mais informações, consulte o [Ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Etapa 1: Crie uma campanha de mensagens in-app

Para navegar até essa opção, você deve criar uma campanha de mensagens in-app. A partir daí, dependendo do seu caso de uso, defina **Send To (Enviar para** ) como **Web Browsers (Navegadores da** **Web**), **Mobile Apps (Aplicativos Móveis**) ou **Both Mobile Apps (Ambos os Aplicativos Móveis) & Web Browsers (Navegadores da Web)** e, em seguida, selecione **Email Capture Form (Formulário de Captura de E-mail** ) como seu **Message Type (Tipo de Mensagem)**.

{% alert note %}
**Segmentação de usuários da Web?** <br>Para habilitar mensagens HTML in-app por meio do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` ao Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no aplicativo podem executar JavaScript, portanto, exigimos que um mantenedor de site as habilite.
{% endalert %}

## Etapa 2: Personalizar o formulário {#customizable-features}

Em seguida, personalize seu formulário conforme necessário. Você pode personalizar os seguintes recursos para seu formulário de captura de e-mail:

- Texto do cabeçalho, do corpo e do botão de envio
- Uma imagem opcional
- Um link opcional para os "Termos de Serviço"
- Cores diferentes para o texto do cabeçalho e do corpo, botões e plano de fundo
- Pares de valores-chave
- Estilo para texto do cabeçalho e do corpo, botões, cor da borda do botão, plano de fundo e sobreposição

Composer para formulário de captura de e-mail.]({% image_buster /assets/img/email_capture.png %})

Se você precisar fazer mais personalizações, escolha **Custom Code (Código personalizado** ) para seu **Message Type (Tipo de mensagem**). Você pode usar esse [modelo modal de captura de e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) do repositório do GitHub [do Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) como seu código inicial.

## Etapa 3: Defina seu público-alvo

Se você estiver usando uma mensagem in-app para capturar e-mails de usuários, talvez queira limitar o público a usuários que ainda não forneceram essas informações.

- **Para segmentar usuários sem um endereço de e-mail:** Use o filtro `Email Available` é `false`. Isso faz com que o formulário apareça apenas para os usuários que não têm um e-mail registrado, o que ajuda a evitar solicitações redundantes para usuários conhecidos.
- **Para direcionar usuários anônimos sem IDs externos:** Use o filtro `External User ID` `is blank`. Isso é útil quando se deseja identificar usuários que ainda não foram autenticados ou registrados.

Você também pode combinar os dois filtros usando a lógica `AND`, se desejar. Isso faz com que o formulário apareça apenas para usuários que não tenham um endereço de e-mail e um ID de usuário externo - ideal para capturar novos leads ou solicitar a criação de contas.

## Etapa 4: Usuários-alvo que preencheram o formulário (opcional)

Depois de lançar o formulário de captura de e-mail e coletar os endereços de e-mail dos usuários, você pode segmentar os usuários que preencheram o formulário.

1. Em qualquer filtro de segmento no Braze, selecione o filtro `Clicked/Opened Campaign`. 
2. No menu suspenso, selecione `clicked in-app message button 1`
3. Selecione sua campanha de formulário de captura de e-mail.

