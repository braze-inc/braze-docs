---
nav_title: Acessando sua conta
article_title: Acessando Sua Conta
page_order: 2
page_type: reference
description: "Este artigo cobre como obter sua conta Braze, como fazer login após ter acesso concedido e como redefinir sua senha Braze."

---

# Acessando sua conta

> Este artigo cobre como obter sua conta Braze, como fazer login após ter acesso concedido e como solucionar problemas de acesso ao seu painel e desempenho do painel.

Se você é o primeiro usuário Braze da sua empresa e está fazendo login pela primeira vez, você receberá um e-mail de boas-vindas de `@alerts.braze.com` pedindo para confirmar seu e-mail e fazer login no primeiro dia do seu contrato.

Após confirmar sua conta, você pode adicionar usuários adicionais na página [Usuários da Empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) do seu painel. Todos os usuários receberão um e-mail pedindo para confirmar sua conta após serem adicionados.

Se você não é o primeiro usuário da conta Braze da sua empresa, entre em contato com o administrador da conta Braze da sua empresa e peça para criar sua conta. Você então receberá um e-mail de boas-vindas de `@alerts.braze.com` pedindo para confirmar seu e-mail e fazer login.

## Fazendo login

Vamos falar sobre como fazer login, seja a primeira vez ou a milionésima! Se você é o primeiro usuário da sua empresa, siga as orientações na seção anterior. Se não, você pode fazer login após o administrador Braze da sua empresa criar sua conta.

Você pode fazer login a partir do site inicial [Braze.com](https://www.braze.com), ou apenas usar a URL do seu painel que corresponde à sua [instância Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) específica. Para sua conveniência, a Braze tem várias opções de login único (SSO) como:

* [SSO SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Provisionamento SAML sob demanda]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [SSO Microsoft Entra]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Depois de fazer login no Braze com SSO, você não pode mais usar sua senha para fazer login no painel.
{% endalert %}

## Navegadores suportados

O painel do Braze suporta os seguintes navegadores:
- Chrome (versão 87 ou mais recente)
- Firefox (versão 85 ou mais recente)
- Safari (versão 15.4 ou mais recente)
- Edge (versão 87 ou mais recente)

Se o seu painel do Braze disser que você tem um erro inesperado e sua ferramenta de console do navegador mostrar o erro `ReferenceError: structuredClone is not defined`, seu navegador está desatualizado. Se esse erro continuar ocorrendo, desinstale e reinstale seu navegador.

## Acessando vários painéis do Braze

O Braze não permite que você registre o mesmo endereço de e-mail para vários usuários do painel no mesmo cluster (por exemplo, se você tiver dois painéis no US-01). Você pode usar o mesmo e-mail para criar contas em diferentes clusters (por exemplo, se você tiver um painel no US-01 e um no US-05). Se você precisar acessar vários painéis do Braze no mesmo cluster, você pode fazer o seguinte:

### Use aliases de e-mail

Se seu provedor de e-mail for o Gmail, você pode criar aliases adicionando um sinal `+` seguido de qualquer texto ao seu endereço de e-mail. Por exemplo:
- **Email original:** `rocky@gmail.com`
- **Email alias:** `rocky+1@gmail.com`

Ambos os endereços de e-mail direcionarão e-mails para a mesma caixa de entrada, mas o Braze os reconhecerá como contas separadas quando você fizer login.

### Crie aliases separados com outros provedores

Se o seu provedor de e-mail não suportar `+` alias, você ainda pode criar aliases separados, como configurar `rocky@braze.com` para encaminhar para `rocky.lotito@braze.com`. Isso permite que vários endereços sejam direcionados para a mesma caixa de entrada, enquanto são reconhecidos como e-mails diferentes pelo Braze.

### Use desenvolvedores de várias empresas

O recurso de desenvolvedores de várias empresas permite o compartilhamento de uma única conta de usuário entre várias empresas. Os usuários podem alternar entre diferentes painéis de empresas a partir do menu de perfil do usuário.

Se você tiver SSO e quiser configurar desenvolvedores de várias empresas, precisará habilitar um ID de Entidade SAML personalizado configurando uma integração SAML SSO personalizada. Siga os passos em [Login iniciado pelo Provedor de Serviço (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), mas aplique essas alterações:
- Altere **ID da Entidade** para `braze_dashboard_<companyID>` para cada integração de painel.
- Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para habilitar o `saml_sso_custom_entity_id` recurso de alternância para cada painel.

### Considerações para o Login Único (SSO)

Se você usar Login Único (SSO), esteja ciente de que ter vários endereços de e-mail diferentes pode levar a complicações. Confirme que suas configurações de SSO estão configuradas corretamente para evitar problemas de acesso.

## Solução de Problemas

### Redefinindo sua senha

Para redefinir sua senha, selecione o link **Esqueceu sua senha?** na página de login do painel. Você será solicitado a inserir seu e-mail para receber um link para redefinir sua senha.

\![Login do painel com o prompt "Esqueceu sua senha?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Limpar o cache e os cookies do seu navegador

Se você está tendo problemas com o desempenho do painel, como seu painel ou a lista de desempenho de segmentos não carregando, tente limpar o cache e os cookies do seu navegador seguindo os passos para o seu respectivo navegador.

{% alert important %}
Limpar cookies fará com que você saia, portanto, o trabalho não salvo será perdido.
{% endalert %}

- [Limpar cache & cookies no Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Limpar cookies no Safari no Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Limpar cookies e dados do site no Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Excluir todos os cookies no Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Se limpar o cache e os cookies do seu navegador não resolver seus problemas, entre em contato com [Suporte]({{site.baseurl}}/support_contact/).

### Acessando o editor de arrastar e soltar

Para a maioria dos usuários do Braze, o editor de arrastar e soltar deve carregar. No entanto, se você estiver usando uma VPN ou estiver atrás de um firewall, pode ser necessário permitir um domínio. Entre em contato com seu administrador de TI para verificar se `*.bz-rndr.com` está na lista de permissões.

O editor pode ter problemas de carregamento devido ao seguinte:

- **Erro transitório:** Essas são falhas temporárias que podem afetar a conectividade, comunicação ou transferência de dados. Felizmente, elas geralmente se resolvem sozinhas sem exigir intervenção significativa, pois são frequentemente causadas por condições de curta duração e não indicam problemas sistêmicos.
- **Erro maior:** Isso pode envolver um problema subjacente de infraestrutura ou produto.  Você pode verificar nossa [página de status do sistema Braze](https://braze.statuspage.io/) pois provavelmente estamos cientes da situação e trabalhando ativamente para resolvê-la.

{% alert important %}
Se você ainda estiver enfrentando problemas, [abra um chamado de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Antes de fazer isso, verifique se seu administrador de TI confirmou que `*.bz-rndr.com` está na lista de permissões do seu lado.
{% endalert %}

### Acessando o Braze Learning

Se você está enfrentando problemas para fazer login no Braze Learning e se encontra preso em um loop que o redireciona para o painel, siga os seguintes passos:

1. Se você tiver várias contas Braze, fazer login com a conta errada duas vezes o enviará para o painel do Braze. Confirme se você está fazendo login na conta correta. 
2. Se você tiver um bloqueador de anúncios, confirme se ele está desligado. Ele pode bloquear cookies necessários para a funcionalidade de login único.
3. Vá para Configurações da Empresa > Configurações de Segurança e verifique se o login único (SSO) está ativado.
4. Confirme que o perfil de usuário do seu painel inclui tanto um nome quanto um sobrenome. Não ter um sobrenome pode interromper o processo de login.
5. Acesse o Braze Learning a partir do seu painel indo para **Suporte** > **Braze Learning**. 
6. Se você continuar a ter problemas, considere recriar sua conta. Usuários que acessaram o Braze Learning durante a fase de teste gratuito podem ter dificuldades para acessá-lo agora.

### Problemas de autenticação de dois fatores (2FA)

Se um usuário está enfrentando problemas com a Autenticação de Dois Fatores (2FA) e não consegue acessar o painel do Braze, pode ser devido a várias razões. Mais comumente, eles podem não ter mais acesso ao número de telefone registrado ou ao dispositivo onde o aplicativo Authy está instalado.

Um administrador deve redefinir o 2FA para o usuário afetado fazendo o seguinte: 

1. Vá para **Gerenciar Usuários**.
2. Selecione **Editar Usuário** para o usuário que está enfrentando problemas com 2FA.
3. Escolha a opção para Redefinir 2FA.
4. Confirme a redefinição de 2FA quando solicitado.
5. Se a redefinição não resolver imediatamente o problema, limpe seus cookies e cache.

A Braze não pode redefinir o 2FA em nome dos usuários por razões de segurança, então, se o administrador não conseguir redefinir o 2FA, um ticket de suporte deve ser criado.

#### Considerações

- Se o 2FA for imposto no nível da empresa: Após a redefinição, o usuário será solicitado a configurar seu 2FA novamente na próxima vez que fizer login.
- Se o 2FA não for imposto no nível da empresa: O usuário fará login no painel sem precisar configurar o 2FA novamente. Se desejarem habilitar o 2FA, podem fazê-lo nas Configurações da Conta.

{% alert note %}
Esse processo de redefinição também se aplica a usuários que foram bloqueados de suas contas devido a solicitações de muitos tokens na última hora.
{% endalert %}