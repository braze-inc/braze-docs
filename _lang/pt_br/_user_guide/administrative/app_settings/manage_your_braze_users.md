---
nav_title: Usuários da empresa
article_title: Gerenciar usuários da empresa
page_order: 23
page_type: reference
description: "Esta página aborda o gerenciamento dos usuários da sua empresa, como adicionar e excluir usuários, definir permissões de usuário, criar Teams e gerenciar as configurações da empresa."
---

# Gerenciar usuários da empresa

> Aprenda a gerenciar usuários na conta da sua empresa, incluindo adicionar, suspender e excluir usuários.

{% alert note %}
Várias seções nesta página referem-se à página **Usuários da Empresa**. Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), **Usuários da Empresa** é chamado de **Gerenciar Usuários** e está localizado sob o ícone da sua conta.
{% endalert %}

## Adição de usuários da empresa

Você deve ter permissões de administrador para adicionar usuários à sua conta Braze. 

Adicionar um novo usuário:

1. Acessar **Configurações** > **Usuários da Empresa**.
2. Clique em **\+ Adicionar Novo Usuário**.
3. Insira as informações solicitadas, incluindo o e-mail, o departamento e a [função do usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
O departamento listado no perfil de um usuário determina quais tipos de comunicações eles recebem da Braze. Isso é para que todos recebam apenas as comunicações e alertas que são relevantes para como eles usam Braze.
{% endalert %}

![Campos de detalhes do usuário.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. Para usuários que não são administradores, selecione as permissões de nível de empresa e de nível de espaço de trabalho [permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) que você deseja que este usuário tenha.

![Permissões no nível do espaço de trabalho com uma seção para campos de permissões personalizadas.]({% image_buster /assets/img/add_new_user_3.png %})

### Requisitos de endereço de e-mail

Todo e-mail usado em uma [instância]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) deve ser único. Isso significa que, se você tentar adicionar um endereço de e-mail que já está associado a um usuário que teve ou ainda tem acesso a um espaço de trabalho da empresa nessa instância, verá uma mensagem de erro. 

Se a sua equipe usa o Gmail e você está tendo problemas para adicionar um endereço de e-mail, você pode criar um alias adicionando um sinal de mais (+) como "+1" ou "+teste" ao endereço de e-mail. Por exemplo, `contractor@braze.com` pode ter um alias de `contractor+1@braze.com`. E-mails para `contractor+1@braze.com` ainda serão entregues para `contractor@braze.com`, mas o alias será reconhecido como um endereço de e-mail único.

### Posso alterar o endereço de e-mail da minha conta Braze?

Por motivos de segurança, os usuários não podem alterar o endereço de e-mail associado à sua conta Braze. Se um usuário quiser atualizar seu endereço de e-mail, um administrador deverá [criar uma nova conta](#adding-braze-users) para ele com o endereço de e-mail preferido.

## Atribuindo acesso e responsabilidades do usuário

{% multi_lang_include permissions.md content="Differences" %}

## Suspensão de usuários da empresa

Suspender um usuário coloca a conta dele em um estado inativo, onde o usuário não pode mais fazer login, mas os dados associados à conta são preservados. Somente os administradores podem suspender ou cancelar a suspensão de usuários da empresa.

Para suspender um usuário, acesse **Configurações** > **Usuários da empresa**, localize o nome de usuário e selecione <i class="fa-solid fa-user-lock"></i> **Suspender**.

![Opção para suspender um usuário.]({% image_buster /assets/img_archive/suspend_user.png %})

Os administradores também podem suspender um usuário selecionando seu nome na lista e clicando em **Suspender usuário** no rodapé.

![Suspender um usuário ao editar os detalhes do usuário.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Exclusão de usuários da empresa

Para excluir um usuário, acessar **Configurações** > **Usuários da Empresa**, encontre o nome de usuário e selecione <i class="fa fa-trash-can"></i> **Excluir usuário**.

![Excluir um usuário]({% image_buster /assets/img_archive/delete_user_new.png %})

Depois que um usuário é excluído, a Braze não mantém nenhum dos seguintes dados:

- Quaisquer atributos que o usuário tinha
- Endereço de e-mail
- Número de telefone
- ID de usuário externo
- Gênero
- País
- Idioma
- Outros dados semelhantes

Braze manterá os seguintes dados da conta:

- Atributos personalizados ou dados de teste associados à sua conta
- Campanhas ou Canvases que criaram (mas o nome do usuário não aparecerá nelas, como aparece na **Última edição por** coluna)

### Impacto da exclusão de um usuário do dashboard

Quando um usuário do painel é excluído, não haverá impacto significativo nos ativos que ele criou no dashboard, como campanhas, segmentos e Canvas. No entanto, é importante notar que o campo **Criado por** para esses ativos exibirá um valor "nulo" em vez do endereço de e-mail do usuário excluído.

Se um novo usuário do dashboard for criado posteriormente com o mesmo endereço de e-mail do usuário excluído, o Braze não associará novamente os ativos criados pelo usuário excluído ao novo usuário. O novo usuário do painel começará do zero e não será creditado como o criador de nenhum ativo existente no dashboard.

## Solução de problemas

### "O e-mail já está ocupado" ao tentar adicionar um usuário

Se tentar adicionar um novo usuário e receber um erro dizendo que o e-mail já está ocupado, mas não conseguir encontrá-lo em sua lista de usuários, esse usuário provavelmente existe em uma instância diferente do mesmo cluster do Braze dashboard.

Para criar esse novo usuário, você pode fazer uma das seguintes opções:

1. Excluir o usuário da outra instância antes de poder criá-lo na nova instância, ou
2. Crie o usuário com uma string de e-mail diferente (como `testing+01@braze.com`) ou outro alias de e-mail. 

Se não receber a ativação da mensagem em sua caixa de entrada ao usar `testing+01@braze.com`, confirme com sua equipe de TI se é possível aceitar mensagens desse tipo de endereço de e-mail. Alguns administradores filtram as mensagens enviadas para endereços de e-mail com `+`.