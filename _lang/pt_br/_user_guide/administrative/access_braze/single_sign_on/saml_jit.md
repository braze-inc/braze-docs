---
nav_title: Provisionamento SAML Just-in-Time
article_title: Provisionamento SAML Just-in-Time
page_order: 1
page_type: tutorial
description: "Este artigo o orientará sobre como configurar o provisionamento SAML just-in-time para permitir que os novos usuários da empresa criem uma conta Braze em seu primeiro login." 

---

# Provisionamento SAML just-in-time 

> O provisionamento just-in-time funciona com o [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) para permitir que os novos usuários da empresa criem uma conta Braze em seu primeiro fazer login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário da empresa, escolherem suas permissões, atribuírem a ele um espaço de trabalho e esperarem que ele ative sua conta.

Como medida de segurança, o provisionamento SAML just-in-time (JITP) só funciona para usuários com domínios de e-mail que já existem em sua empresa. O JITP só é possível para domínios em que já exista pelo menos um desenvolvedor confirmado e sem simulação na empresa. 

Por exemplo, digamos que a conta ```jon.smith@decorumsoft.com``` possa usar o JITP para registrar-se na Decorumsoft. A conta ```jane.smith@decorumsoft.com``` tem o mesmo domínio e também pode ter permissão de provisionamento. No entanto, se você tentar usar o JITP com ```jon.smith@decorumsoft.eu```, o provisionamento não será permitido porque não há uma conta ```decorumsoft.eu``` no dashboard do Decorumsoft Braze. 

Para abrir uma exceção para uma empresa, entre em contato com [o Suporte]({{site.baseurl}}/braze_support/).

## Pré-requisitos

O SAML JITP exige que o SAML SSO esteja configurado e integrado. Ele não é compatível com o Google SSO e só é compatível com fluxos de trabalho de login iniciados pelo provedor de identidade (iniciados pelo IdP).

## Configuração do provisionamento SAML just-in-time (JITP)

Peça a um administrador do Braze que faça o seguinte:

1. Navegue até **Configurações** > Configurações **administrativas** > **Configurações de segurança**.
2. Na seção **SAML SSO**, ative a opção **Automatic user provisioning (Provisionamento automático de usuários** ).
3. Selecione um espaço de trabalho padrão para adicionar um novo usuário da empresa.
4. Selecione o conjunto de permissões padrão a ser atribuído a esse novo usuário da empresa. Para saber como criar um conjunto de permissões, consulte [Definição de permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Selecione **Salvar alterações** na parte inferior da página
7. Nas configurações do seu provedor de SSO, adicione todos os usuários que precisam de acesso ao Braze ao diretório do seu provedor de SSO.
8. Instrua os usuários a acessar o Braze por meio do seu portal IdP para o primeiro login. Depois disso, o botão de logon único SAML será exibido para futuros logins.

## Perguntas frequentes

### Como faço para desativar o SAML JITP?

Depois de configurar o JITP, é necessário [entrar em contato com o Suporte]({{site.baseurl}}/braze_support/) para desativá-lo.

## Solução de problemas

### O botão de login único não aparece com o Microsoft Entra ID

O campo **URL de login** no formulário **Configuração básica de SAML** do Microsoft Entra para o Braze pode fazer com que os usuários vejam apenas uma opção de senha, e não um botão SSO, com login iniciado por IdP. Para evitar esse problema, deixe o campo **URL de logon** em branco ao configurar o Braze em seu centro de administração do Microsoft Entra.