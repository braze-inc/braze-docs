---
nav_title: Usuários
article_title: Gerenciamento de usuários do Braze
page_order: 0
page_type: reference
description: "Este artigo de referência aborda como gerenciar usuários na conta da sua empresa, incluindo adição, suspensão e exclusão de usuários."

---

# Gerenciamento de usuários do Braze

> Saiba como gerenciar usuários na conta da sua empresa, incluindo adição, suspensão e exclusão de usuários.

{% alert note %}
Várias seções desta página fazem referência à página **Usuários da empresa**. Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), a opção **Usuários da empresa** se chama **Gerenciar usuários** e está localizada sob o ícone da sua conta.
{% endalert %}

## Adicionar usuários do Braze

Você deve ter permissões de administrador para adicionar usuários à sua conta Braze. 

Para adicionar um novo usuário:

1. Vá para **Configurações** > **Usuários da empresa**.
2. Clique em **\+ Add New User (Adicionar novo usuário**).
3. Insira as informações solicitadas, incluindo o e-mail, o departamento e [a função do usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
O departamento listado no perfil de um usuário determina os tipos de comunicações que ele recebe da Braze. Isso é feito para que todos recebam apenas as comunicações e os alertas relevantes para a forma como usam o Braze.
{% endalert %}

\![Campos de detalhes do usuário.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. Para usuários que não são administradores, selecione as [permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) no nível da empresa e do espaço de trabalho que deseja que esse usuário tenha.

\![Permissões no nível do espaço de trabalho com uma seção para campos de permissões personalizadas.]({% image_buster /assets/img/add_new_user_3.png %})

### Requisitos de endereço de e-mail

Cada endereço de e-mail usado em uma [instância]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) deve ser exclusivo. Isso significa que, se você tentar adicionar um endereço de e-mail que já esteja associado a um usuário que teve ou ainda tem acesso a um espaço de trabalho da empresa nessa instância, verá uma mensagem de erro. 

Se a sua equipe usa o Gmail e você está tendo problemas para adicionar um endereço de e-mail, é possível criar um alias adicionando um sinal de mais (+), como "+1" ou "+test", ao endereço de e-mail. Por exemplo, `contractor@braze.com` pode ter um alias de `contractor+1@braze.com`. Os e-mails para `contractor+1@braze.com` ainda serão entregues a `contractor@braze.com`, mas o alias será reconhecido como um endereço de e-mail exclusivo.

### Posso alterar o endereço de e-mail da minha conta Braze?

Por motivos de segurança, os usuários não podem alterar o endereço de e-mail associado à sua conta Braze. Se um usuário quiser atualizar seu endereço de e-mail, um administrador deverá [criar uma nova conta](#adding-braze-users) para ele com o endereço de e-mail preferido.

## Suspensão de usuários do Braze

A suspensão de um usuário coloca sua conta em um estado inativo, no qual o usuário não pode mais fazer login, mas os dados associados à sua conta são preservados. Somente os administradores podem suspender ou cancelar a suspensão de usuários do Braze.

Para suspender um usuário, vá para **Configurações** > **Usuários da empresa**, localize o nome de usuário e selecione <i class="fa-solid fa-user-lock"></i> **Suspender**.

\![Opção para suspender um usuário.]({% image_buster /assets/img_archive/suspend_user.png %})

Os administradores também podem suspender um usuário selecionando seu nome na lista e clicando em **Suspender usuário** no rodapé.

\![Suspenda um usuário ao editar os detalhes do usuário.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Atribuição de acesso e responsabilidades ao usuário

{% multi_lang_include permissions.md content="Differences" %}

## Exclusão de usuários do Braze

Para excluir um usuário, vá para **Configurações** > **Usuários da empresa**, localize o nome de usuário e selecione <i class="fa fa-trash-can"></i> **Excluir usuário**.

\![Excluir um usuário]({% image_buster /assets/img_archive/delete_user_new.png %})

Depois que um usuário é excluído, a Braze não mantém nenhum dos seguintes dados da conta:

- Quaisquer atributos que o usuário tenha
- Endereço de e-mail
- Número de telefone
- ID de usuário externo
- Gênero
- País
- Idioma
- Outros dados semelhantes

A Braze manterá os seguintes dados da conta:

- Atributos personalizados ou dados de teste associados à sua conta
- Campanhas ou Canvases que eles criaram (mas o nome do usuário não aparecerá nelas, como na coluna **Última edição por** )

### Impacto da exclusão de um usuário do painel

Quando um usuário do painel é excluído, não haverá impacto significativo sobre os ativos que ele criou no painel, como campanhas, segmentos e Canvases. No entanto, é importante observar que o campo **Criado por** para esses ativos exibirá um valor "nulo" em vez do endereço de e-mail do usuário excluído.

Se um novo usuário do painel for criado posteriormente com o mesmo endereço de e-mail do usuário excluído, o Braze não associará novamente os ativos criados pelo usuário excluído ao novo usuário. O novo usuário do painel começará do zero e não será creditado como o criador de nenhum ativo existente no painel.

## Solução de problemas

### "O e-mail já está ocupado" ao tentar adicionar um usuário

Se você tentar adicionar um novo usuário e receber um erro dizendo que o e-mail já está ocupado, mas não conseguir encontrá-lo na sua lista de usuários, esse usuário provavelmente existe em uma instância diferente do mesmo cluster de painel do Braze.

Para criar esse novo usuário, você pode fazer uma das seguintes opções:

1. Excluir o usuário da outra instância antes de poder criá-lo na nova instância, ou
2. Crie o usuário com uma string de e-mail diferente (como `testing+01@braze.com`) ou outro alias de e-mail. 

Se você não receber a ativação da mensagem na caixa de entrada ao usar `testing+01@braze.com`, confirme com sua equipe de TI se você pode aceitar mensagens desse tipo de endereço de e-mail. Alguns administradores filtram mensagens enviadas para endereços de e-mail com `+`.

