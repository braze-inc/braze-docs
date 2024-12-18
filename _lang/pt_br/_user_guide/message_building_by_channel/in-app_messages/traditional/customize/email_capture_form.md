---
nav_title: Formulário de captura de e-mail
article_title: Formulário de captura de e-mail
page_order: 3
page_type: reference
description: "Este artigo fornece uma visão geral do tipo de mensagem no app de captura de e-mail."
channel:
  - in-app messages
---

# Formulário de captura de e-mail {#email-capture-form}

> As mensagens de captura de e-mail permitem solicitar facilmente que os usuários do seu site enviem o endereço de e-mail, que ficará disponível no perfil do usuário para uso em todas as suas campanhas de mensagens.

Quando um usuário final insere seu endereço de e-mail nesse formulário, o endereço de e-mail é adicionado ao seu perfil de usuário.

- Para [usuários anônimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) que ainda não têm uma conta, o endereço de e-mail ficará no perfil de usuário anônimo que está vinculado ao dispositivo do usuário.
- Se já existir um endereço de e-mail no perfil do usuário, o endereço de e-mail existente será substituído pelo endereço de e-mail recém-inserido.
- Se o usuário conhecido tiver um endereço de e-mail sinalizado como [hard bounce]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces), verificaremos se o endereço de e-mail recém-inserido é diferente do que está em seu perfil no Braze. Se o endereço de e-mail fornecido for diferente, o endereço de e-mail será atualizado e o status de hard bounce será removido. 
- Se um usuário inserir um endereço de e-mail inválido, verá a mensagem de erro: "Por favor, digite um e-mail válido."
    - Endereços de e-mail inválidos: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Endereços de e-mail válidos: 
        - `example@gmail.com`
        - `example@gnail.com` (com um erro de digitação)
    - Para saber mais sobre a validação de e-mails na Braze, consulte as [diretrizes e notas técnicas de e-mail]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation/).

{% details Mais informações sobre usuários identificados e anônimos %}

Em geral, a lógica por trás do formulário de captura de e-mail é simples. Isso definirá o endereço de e-mail no perfil do usuário no Braze para o usuário que está ativo no momento. No entanto, isso significa que o comportamento difere com base no fato de o usuário ser identificado (registrado, `changeUser` chamado) ou não.

Se um usuário anônimo inserir seu e-mail no formulário e enviá-lo, o Braze adicionará o endereço de e-mail ao seu perfil. Se o `changeUser` for chamado posteriormente em sua jornada na Web e um novo `external_id` for atribuído (como quando um novo usuário se registra no serviço), todos os dados anônimos do perfil do usuário serão mesclados, inclusive o envio de e-mail.

Se `changeUser` for chamado com um `external_id` existente, o perfil de usuário anônimo ficará órfão e os [campos de dados de usuários específicos]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) que ainda não existem no usuário identificado serão mesclados, mas os campos que já existem serão perdidos, inclusive o endereço de e-mail.

Para saber mais, consulte o [Ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Etapa 1: Crie uma campanha de mensagens no app

Para navegar até essa opção, você deve criar uma campanha de mensagens no app. A partir daí, dependendo do seu caso de uso, defina **Send To (Enviar para** ) como **Web Browsers (Navegadores da Web**), **Mobile Apps (Aplicativos Móveis**) ou **Both Mobile Apps & Web Browsers (Aplicativos Móveis e Navegadores da Web**) e, em seguida, selecione **Email Capture Form (Formulário de Captura de E-mail** ) como seu **Message Type (Tipo de Mensagem)**.

![][4]

{% alert note %}
Para ativar mensagens no app HTML através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no app podem executar JavaScript, portanto, exigimos que um mantenedor de site as ative.
{% endalert %}

## Etapa 2: Personalizar o formulário {#customizable-features}

Em seguida, personalize seu formulário conforme necessário. Você pode personalizar os seguintes recursos para seu formulário de captura de e-mail:

- Texto do cabeçalho, do corpo e do botão de envio
- Uma imagem opcional
- Um link opcional para os "Termos de Serviço"
- Cores diferentes para o texto do cabeçalho e do corpo, botões e plano de fundo
- Pares de valores chave
- Estilo para texto do cabeçalho e do corpo, botões, cor da borda do botão, plano de fundo e sobreposição

![Criador para formulário de captura de e-mail.][5]

Se precisar fazer mais personalizações, escolha **Custom Code (Código personalizado** ) para seu **Message Type (Tipo de mensagem**). Você pode usar este [modelo modal de captura de e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) do repositório do GitHub [Modelos da Braze](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) como seu código inicial.

## Etapa 3: Defina seu público de entrada

Se quiser enviar esse formulário apenas para usuários sem endereços de e-mail existentes, use o filtro `Email Available is false`.

![Filtrar por e-mail disponível é falso][10]{: style="max-width:50%"}

Se quiser enviar esse formulário apenas para usuários sem IDs externos (usuários anônimos), use o filtro `External User ID is blank`.

![O filtro por ID de usuário externo está em branco][11]{: style="max-width:50%"}

Você também pode combinar os dois filtros usando a lógica `AND`, se desejar.

## Etapa 4: Direcionamento para usuários que preencheram o formulário (opcional)

Depois de lançar o formulário de captura de e-mail e coletar os endereços de e-mail dos usuários, é possível direcionar esses usuários com o filtro `Clicked/Opened Campaign`. 

Defina o filtro como `Has clicked in-app message button 1` para a campanha `<CAMPAIGN_NAME>`. Substitua `<CAMPAIGN_NAME>` pelo nome de sua campanha de formulário de captura de e-mail.

![Filtro para clicar no botão 1 de mensagem no app para sua campanha de formulário de captura de e-mail na internet][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}
