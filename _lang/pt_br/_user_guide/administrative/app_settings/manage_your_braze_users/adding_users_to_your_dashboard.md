---
nav_title: Usuários
article_title: Gerenciando usuários do Braze
page_order: 0
page_type: reference
description: "Este artigo de referência cobre como gerenciar usuários na conta da sua empresa, incluindo adicionar, suspender e excluir usuários."

---

# Gerenciamento de usuários na Braze

> Aprenda a gerenciar usuários na conta da sua empresa, incluindo adicionar, suspender e excluir usuários.

{% alert note %}
Várias seções nesta página referem-se à página **Usuários da Empresa**. Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **Usuários da Empresa** é chamado de **Gerenciar Usuários** e está localizado sob o ícone da sua conta.
{% endalert %}

## Adicionando usuários Braze

Você deve ter permissões de administrador para adicionar usuários à sua conta Braze. 

Adicionar um novo usuário:

1. Acessar **Configurações** > **Usuários da Empresa**.
2. Clique em **\+ Adicionar Novo Usuário**.
3. Insira as informações solicitadas, incluindo o e-mail, o departamento e [a função do usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
O departamento listado no perfil de um usuário determina quais tipos de comunicações eles recebem da Braze. Isso é para que todos recebam apenas as comunicações e alertas que são relevantes para como eles usam Braze.
{% endalert %}

![][2]

{:start="4"}

4. Para usuários que não são administradores, selecione as permissões de nível de empresa e de nível de espaço de trabalho [permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) que você deseja que este usuário tenha.

![][3]

### Requisitos de endereço de e-mail

Todo e-mail usado em uma [instância]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) deve ser único. Isso significa que, se você tentar adicionar um endereço de e-mail que já está associado a um usuário que teve ou ainda tem acesso a um espaço de trabalho da empresa nessa instância, verá uma mensagem de erro. 

Se a sua equipe usa o Gmail e você está tendo problemas para adicionar um endereço de e-mail, você pode criar um alias adicionando um sinal de mais (+) como "+1" ou "+teste" ao endereço de e-mail. Por exemplo, `contractor@braze.com` pode ter um alias de `contractor+1@braze.com`. E-mails para `contractor+1@braze.com` ainda serão entregues para `contractor@braze.com`, mas o alias será reconhecido como um endereço de e-mail único.

### Posso alterar o endereço de e-mail da minha conta Braze?

Por motivos de segurança, os usuários não podem alterar o endereço de e-mail associado à sua conta Braze. Se um usuário quiser atualizar seu endereço de e-mail, um administrador deverá [criar uma nova conta](#adding-braze-users) para ele com o endereço de e-mail preferido.

## Suspender usuários do Braze

Suspender um usuário coloca a conta dele em um estado inativo, onde o usuário não pode mais fazer login, mas os dados associados à conta são preservados. Somente administradores podem suspender ou reativar usuários do Braze.

Para suspender um usuário, acesse **Configurações** > **Usuários da empresa**, localize o nome de usuário e selecione <i class="fa-solid fa-user-lock"></i> **Suspender**.

![Suspender um usuário][4]

Os administradores também podem suspender um usuário selecionando seu nome na lista e clicando em **Suspender usuário** no rodapé.

![Suspender um usuário ao editar os detalhes do usuário.][5]

## Excluindo usuários do Braze

Para excluir um usuário, acessar **Configurações** > **Usuários da Empresa**, encontre o nome de usuário e selecione <i class="fa fa-trash-can"></i> **Excluir usuário**.

![Excluir um usuário][34]

Depois que um usuário é excluído, a Braze não mantém nenhum dos seguintes dados:

- Quaisquer atributos que o usuário tinha
- Endereço de e-mail
- Número de telefone
- ID de usuário externo
- Gênero
- País
- Idioma
- Outros dados semelhantes

[1]: {% image_buster /assets/img/add_new_user_1.png %}
[2]: {% image_buster /assets/img/add_new_user_2.png %}
[3]: {% image_buster /assets/img/add_new_user_3.png %}
[4]: {% image_buster /assets/img_archive/suspend_user.png %}
[5]: {% image_buster /assets/img_archive/suspend_user2.png %}
[27]: {% image_buster /assets/img/add-user.gif %} "Adicionar um Novo Processo de Usuário"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}