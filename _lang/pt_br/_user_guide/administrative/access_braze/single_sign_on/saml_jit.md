---
nav_title: Provisionamento SAML Just-in-Time
article_title: Provisionamento SAML Just-in-Time
page_order: 1
page_type: tutorial
description: "Este artigo o orientará sobre como configurar o provisionamento SAML just-in-time para permitir que novos usuários do dashboard criem uma conta Braze em seu primeiro login." 

---

# Provisionamento SAML just-in-time 

> O provisionamento just-in-time funciona com o [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) para permitir que novos usuários do dashboard criem uma conta Braze em seu primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário do dashboard, escolherem suas permissões, atribuírem a ele um espaço de trabalho e esperarem que ele ative sua conta.

## Pré-requisitos

Esse recurso requer que o SAML SSO esteja configurado e integrado e não é compatível com o Google SSO.

## Configuração do provisionamento SAML just-in-time

Peça a um administrador do Braze que faça o seguinte:

1. Navegue até **Configurações** > **Configurações de segurança**.
2. Na seção **SAML SSO**, ative a opção **Automatic user provisioning (Provisionamento automático de usuários** ).
3. Selecione um espaço de trabalho padrão para adicionar um novo usuário do dashboard.
4. Selecione o conjunto de permissões padrão a ser atribuído a esse novo usuário do dashboard. Para saber como criar um conjunto de permissões, consulte [Definição de permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Selecione **Salvar alterações** na parte inferior da página
7. Nas configurações do seu provedor de SSO, adicione todos os usuários que precisam de acesso ao Braze ao diretório do seu provedor de SSO.
8. Agora os usuários podem inscrever-se ou fazer login.
