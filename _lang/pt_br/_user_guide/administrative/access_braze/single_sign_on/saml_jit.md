---
nav_title: Provisionamento SAML Just-in-Time
article_title: Provisionamento SAML Just-in-Time
page_order: 1
page_type: tutorial
description: "Este artigo irá guiá-lo sobre como configurar o provisionamento SAML just-in-time para permitir que novos usuários do painel criem uma conta Braze em seu primeiro login." 

---

# Provisionamento SAML just-in-time 

> O provisionamento just-in-time funciona com [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) para permitir que novos usuários do painel criem uma conta Braze em seu primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário do painel, escolher suas permissões, atribuí-los a um espaço de trabalho e esperar que ativem sua conta.

Como medida de segurança, o provisionamento SAML just-in-time (JITP) só funciona para usuários com domínios de e-mail que já existem em sua empresa. O JITP só é possível para domínios onde já existe pelo menos um desenvolvedor confirmado, não-impersonador na empresa. 

Por exemplo, digamos que a conta ```jon.smith@decorumsoft.com``` pode usar JITP para fazer login no Decorumsoft. A conta ```jane.smith@decorumsoft.com``` tem o mesmo domínio e também pode ter o provisionamento permitido. No entanto, se você tentar usar JITP com ```jon.smith@decorumsoft.eu```, o provisionamento não será permitido porque não há uma conta ```decorumsoft.eu``` dentro do painel Braze do Decorumsoft. 

Para fazer uma exceção para uma empresa, entre em contato com [Suporte]({{site.baseurl}}/braze_support/).

## Pré-requisitos

O SAML JITP requer que o SAML SSO esteja configurado e integrado. Não é compatível com o Google SSO e é suportado apenas para fluxos de login iniciados pelo Provedor de Identidade (IdP-initiated).

## Configurando o provisionamento SAML just-in-time (JITP)

Peça a um administrador Braze para fazer o seguinte:

1. Navegue até **Configurações** > **Configurações do Administrador** > **Configurações de Segurança**.
2. Na seção **SAML SSO**, ative a opção **Provisionamento automático de usuários**.
3. Selecione um espaço de trabalho padrão para adicionar um novo usuário do painel.
4. Selecione o conjunto de permissões padrão a ser atribuído a esse novo usuário do painel. Para aprender como criar um conjunto de permissões, veja [Definindo permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Selecione **Salvar alterações** na parte inferior da página
7. Nas configurações do seu provedor de SSO, adicione todos os usuários que precisam de acesso ao Braze ao diretório do seu provedor de SSO.
8. Agora os usuários podem se inscrever ou fazer login.

## Perguntas frequentes

### Como desabilito o SAML JITP?

Após configurar o JITP, você deve [contatar o Suporte]({{site.baseurl}}/braze_support/) para que ele seja desativado.

## Solução de problemas

### O botão de login único não aparece com o Microsoft Entra ID

O campo **URL de Login** no formulário **Configuração SAML Básica** do Microsoft Entra para o Braze pode fazer com que os usuários vejam apenas uma opção de senha, e não um botão SSO, com login iniciado pelo IdP. Para evitar esse problema, deixe o campo **URL de Login** em branco ao configurar o Braze no seu centro de administração do Microsoft Entra.