---
nav_title: Acesse sua conta
article_title: Acesse sua conta
page_order: 0
page_type: reference
description: "Este artigo aborda como obter sua conta Braze, como fazer o registro após a concessão de acesso e como redefinir sua senha Braze."

---

# Acesse sua conta

> Este artigo cobre como obter sua conta Braze, como fazer login após receber acesso e como solucionar problemas de acesso ao seu dashboard e desempenho do dashboard.

Se for o primeiro usuário Braze da sua empresa e estiver se registrando pela primeira vez, receberá um e-mail de boas-vindas de `@alerts.braze.com` solicitando que confirme seu e-mail e se registre no primeiro dia do seu contrato.

Após confirmar sua conta, você pode adicionar usuários adicionais na página [Usuários da Empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) do seu dashboard. Todos os usuários receberão um e-mail solicitando a confirmação da conta depois de serem adicionados.

Se você não for o primeiro usuário na conta Braze da sua empresa, entre em contato com o administrador da conta Braze da sua empresa e peça para criar sua conta. Em seguida, você receberá um e-mail de boas-vindas do `@alerts.braze.com` solicitando a confirmação do seu e-mail e o registro.

## Login

Vamos falar sobre como fazer login, seja a primeira vez ou a milionésima! Se você for o primeiro usuário da sua empresa, siga as orientações da seção anterior. Se não, você pode fazer login após o administrador Braze da sua empresa criar sua conta.

Você pode fazer o registro a partir do [Braze.com](https://www.braze.com) ou simplesmente usar o URL do dashboard que corresponde à sua [instância específica da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Para sua conveniência, o Braze tem várias opções de logon único (SSO), como:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Provisionamento SAML just-in-time]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Depois de entrar no Braze com SSO, você não poderá mais usar sua senha para se registrar no dashboard.
{% endalert %}

## Navegadores compatíveis

O dashboard da Braze é compatível com os seguintes navegadores:
- Chrome (versão 87 ou mais recente)
- Firefox (versão 85 ou mais recente)
- Safari (versão 15.4 ou mais recente)
- Edge (versão 87 ou mais recente)

Se o seu dashboard Braze disser que você tem um erro inesperado e sua ferramenta de console do navegador mostrar o erro `ReferenceError: structuredClone is not defined`, seu navegador está desatualizado. Se esse erro continuar ocorrendo, desinstale e reinstale seu navegador.

## Acessando múltiplos dashboards Braze

A Braze não permite que você registre o mesmo endereço de e-mail para múltiplos usuários de dashboard no mesmo cluster (por exemplo, se você tiver dois dashboards no US-01). Você pode usar o mesmo e-mail para criar contas em diferentes clusters (por exemplo, se você tiver um dashboard no US-01 e um no US-05). Se você precisar acessar múltiplos dashboards Braze no mesmo cluster, você pode fazer o seguinte:

### Use aliases de e-mail

Se seu provedor de e-mail for o Gmail, você pode criar aliases adicionando um `+` seguido de qualquer texto ao seu endereço de e-mail. Por exemplo:
- **E-mail original:** `rocky@gmail.com`
- **E-mail alias:** `rocky+1@gmail.com`

Ambos os endereços de e-mail direcionarão e-mails para a mesma caixa de entrada, mas a Braze os reconhecerá como contas separadas quando você fizer login.

### Crie aliases separados com outros provedores

Se seu provedor de e-mail não suportar `+` alias, você ainda pode criar aliases separados, como configurar `rocky@braze.com` para encaminhar para `rocky.lotito@braze.com`. Isso permite que múltiplos endereços sejam direcionados para a mesma caixa de entrada enquanto são reconhecidos como e-mails diferentes pela Braze.

### Use desenvolvedores de múltiplas empresas

O recurso de desenvolvedores multiempresa permite o compartilhamento de uma única conta de usuário entre várias empresas. Os usuários podem alternar entre diferentes dashboards de empresas a partir do menu do perfil do usuário.

Se você tem SSO e deseja configurar desenvolvedores multiempresa, precisa ativar um ID de Entidade SAML personalizado configurando uma integração SSO SAML personalizada. Siga os passos em [Prestador de Serviço (SP) iniciado login]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), mas aplique estas alterações:
- Altere **ID da Entidade** para `braze_dashboard_<companyID>` para cada integração de dashboard.
- Entre em contato com seu gerente de sucesso do cliente ou gerente de contas para ativar o `saml_sso_custom_entity_id` recurso de alternância para cada dashboard.

### Considerações para Logon Único (SSO)

Se você usa Logon Único (SSO), esteja ciente de que ter vários endereços de e-mail diferentes pode levar a complicações. Confirme que suas configurações de SSO estão configuradas corretamente para evitar problemas de acesso.

## Solução de problemas

### Redefinição de sua senha

Para redefinir sua senha, selecione o link **Esqueceu sua senha?** na página de login do dashboard. Você será solicitado a inserir seu e-mail para receber um link para redefinir sua senha.

![Login do dashboard com o prompt "Esqueceu sua senha?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Limpar o cache e cookies do seu navegador

Se você está tendo problemas com o desempenho do dashboard, como seu dashboard ou lista de desempenho de segmentos não carregando, tente limpar o cache e os cookies do seu navegador seguindo os passos para o seu respectivo navegador.

{% alert important %}
Limpar cookies fará com que você saia, portanto, trabalhos não salvos serão perdidos.
{% endalert %}

- [Limpar cache & cookies no Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Limpar cookies no Safari no Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Limpar cookies e dados do site no Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Excluir todos os cookies no Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Se limpar o cache e os cookies do seu navegador não resolver seus problemas, entre em contato com o [Suporte]({{site.baseurl}}/support_contact/).

### Acessando o editor de arrastar e soltar

Para a maioria dos usuários da empresa, o editor de arrastar e soltar deve carregar. No entanto, se você estiver usando uma VPN ou estiver atrás de um firewall, pode ser necessário permitir um domínio. Entre em contato com seu administrador de TI para verificar se `*.bz-rndr.com` está na lista de permissões.

O editor pode ter problemas de carregamento devido ao seguinte:

- **Erro transitório:** Essas são falhas temporárias que podem afetar a conectividade, comunicação ou transferência de dados. Felizmente, elas geralmente se resolvem sozinhas sem exigir intervenção significativa, pois costumam ser causadas por condições de curta duração e não indicam problemas sistêmicos.
- **Erro maior:** Isso pode envolver um problema subjacente de infraestrutura ou produto.  Você pode verificar nossa [página de status do sistema Braze](https://braze.statuspage.io/) pois provavelmente estamos cientes da situação e trabalhando ativamente para resolvê-la.

{% alert important %}
Se você ainda estiver enfrentando problemas, [abra um chamado de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Antes de fazer isso, verifique se seu administrador de TI confirmou que `*.bz-rndr.com` está na lista de permissões do seu lado.
{% endalert %}

### Acessando o Braze Learning

Se você estiver enfrentando problemas para fazer login no Braze Learning e se encontrar preso em um loop que o redireciona para o dashboard, siga os seguintes passos:

1. Se você tiver várias contas Braze, fazer login com a conta errada duas vezes o enviará para o dashboard do Braze. Confirme se você está fazendo login na conta correta. 
2. Se você tiver um bloqueador de anúncios, confirme se ele está desativado. Ele pode bloquear cookies necessários para a funcionalidade de logon único.
3. Acesse Configurações da Empresa > Configurações de Segurança e verifique se o logon único (SSO) está ativado.
4. Confirme que o perfil de usuário do seu dashboard inclui tanto um nome quanto um sobrenome. Não ter um sobrenome pode interromper o processo de login.
5. Acesse o Braze Learning a partir do seu dashboard indo para **Suporte** > **Braze Learning**. 
6. Se você continuar a enfrentar problemas, considere recriar sua conta. Usuários que acessaram o Braze Learning durante a fase de teste gratuito podem ter dificuldades para acessá-lo agora.

### Problemas de autenticação de dois fatores (2FA)

Se um usuário estiver enfrentando problemas com a autenticação de dois fatores (2FA) e não conseguir acessar o dashboard do Braze, pode ser devido a várias razões. Mais comumente, eles podem não ter mais acesso ao número de telefone registrado ou ao dispositivo onde o app Authy está instalado.

Um administrador deve redefinir o 2FA para o usuário afetado fazendo o seguinte: 

1. Acessar **Gerenciar Usuários**.
2. Selecionar **Editar Usuário** para o usuário que está enfrentando problemas com o 2FA.
3. Escolher a opção para Redefinir 2FA.
4. Confirmar a redefinição do 2FA quando solicitado.
5. Se a redefinição não resolver imediatamente o problema, limpe seus cookies e cache.

O Braze não pode redefinir o 2FA em nome dos usuários por razões de segurança, então, se o administrador não conseguir redefinir o 2FA, crie um ticket de suporte.

#### Considerações

- Se o 2FA for imposto no nível da empresa: Após a redefinição, o Braze solicita ao usuário que configure seu 2FA novamente na próxima vez que ele fizer login.
- Se o 2FA não for imposto no nível da empresa: O usuário fará login no dashboard sem precisar configurar o 2FA novamente. Se desejar ativar o 2FA, pode fazê-lo nas Configurações da Conta.

{% alert note %}
Esse processo de redefinição também se aplica a usuários que foram bloqueados de sua conta devido a solicitações de muitos tokens na última hora.
{% endalert %}