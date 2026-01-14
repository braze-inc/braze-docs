---
nav_title: Usuários duplicados
article_title: Usuários duplicados
description: "Saiba como localizar e mesclar usuários duplicados em seu painel do Braze."
page_order: 0
---

# Usuários duplicados

> Saiba como localizar e mesclar usuários duplicados para maximizar a eficácia de suas campanhas e Canvases.

{% alert tip %}
Para mesclar usuários duplicados usando a Braze REST API, consulte [POST: Mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Fusão individual

Se uma pesquisa de usuário retornar perfis duplicados, você poderá mesclar cada perfil individualmente a partir do perfil do usuário no painel do Braze.

### Etapa 1: Procurar um perfil duplicado

No Braze, selecione **Audience** > **User Search**.

O bloco "User Search" (Pesquisa de usuários) destacado no menu de navegação.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Digite um identificador exclusivo, como um endereço de e-mail ou número de telefone, para o perfil duplicado e, em seguida, selecione **Search (Pesquisar**).

A página "User Search" no painel do Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Etapa 2: Mesclar duplicatas

Para iniciar o processo de mesclagem, selecione **Merge duplicates (Mesclar duplicatas**).

\![Um dos perfis de usuário duplicados.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Escolha qual perfil de usuário deve ser mantido e qual deve ser mesclado e, em seguida, selecione **Mesclar perfis**. Repita esse processo até que você tenha mesclado todos os perfis duplicados.

A página de mesclagem individual de um perfil duplicado.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Os perfis de usuário duplicados não podem ser recuperados após a fusão.
{% endalert %}

## Mesclagem em massa

Quando você mescla usuários duplicados em massa, o Braze encontra perfis com identificadores correspondentes (como um endereço de e-mail) e mescla todos os seus dados no perfil atualizado mais recentemente com um `external_id`. Se não houver perfis com um `external_id`, o perfil atualizado mais recentemente sem um `external_id` será usado em seu lugar.

### Etapa 1: Vá para Manage Audience (Gerenciar público)

No painel do Braze, selecione **Audience** > **Manage Audience**.

O bloco "Manage Audience" (Gerenciar público) destacado no menu de navegação.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Etapa 2: Visualizar os resultados (opcional)

Para visualizar os resultados antes de mesclar as duplicatas, selecione **Generate list of duplicates (Gerar lista de duplicatas**).

A página "Manage Audience" (Gerenciar público) com a opção "Generate list of duplicates" (Gerar lista de duplicatas) destacada.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

O Braze gerará sua visualização e a enviará para seu endereço de e-mail como um arquivo CSV.

\![Um e-mail da Braze com um link para o arquivo CSV gerado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

No exemplo a seguir, o Braze usa a ID externa do usuário para sinalizar perfis duplicados e identificar qual deles deve ser mantido. Se esses perfis forem mesclados em massa, o Braze usará o perfil com um ID externo como o novo perfil principal do usuário.

{% tabs local %}
{% tab example csv file %}
| Endereço de e-mail | ID externo | Número de telefone | ID do Braze | Identificador da regra | Perfil a ser mantido | Perfil a ser mesclado
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99 | (555) 123-4567 | 65fcaa547f470494d1370 | email | TRUE | FALSE |
| alex@company.com | | | (555) 987-6543 | 65fcaa547f47d004d1348 | email | FALSE | TRUE |
| alex@company.com | | | (555) 321-0987 | 65fcaa547f47d0049135c | email | FALSE | TRUE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Comportamento de mesclagem

O Braze preencherá os campos vazios no perfil mantido com valores do perfil mesclado. Para obter uma lista dos campos que serão preenchidos, consulte [Comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Etapa 3: Mesclar suas duplicatas

Se estiver satisfeito com os resultados da visualização, selecione **Merge all duplicates (Mesclar todas as duplicatas**).

{% alert warning %}
Os perfis de usuário duplicados não podem ser recuperados após a fusão.
{% endalert %}

A página "Manage Audience" (Gerenciar público) com a opção "Merge all duplicates" (Mesclar todas as duplicatas) destacada.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## Mesclagem baseada em regras

Você pode usar regras para controlar como os perfis duplicados são resolvidos ao executar uma mesclagem, de modo que o perfil de usuário mais relevante seja mantido. Quando as regras forem definidas, o Braze manterá os perfis que correspondem aos seus critérios.

### Etapa 1: Defina suas regras

1. Vá para **Audience** > **Manage Audience** > **Edit rules**( **Público** > **Gerenciar público** > **Editar regras**).
2. Na seção **Profile to keep (Perfil a ser mantido** ) do painel **Edit rules (Editar regras** ), selecione o **Identifier (Identificador** ) para os perfis que serão mantidos ao mesclar duplicatas. Pode ser o endereço de e-mail ou o número de telefone.
3. Na seção **Resolver ví** nculos, selecione os critérios para determinar como resolver vínculos entre perfis com critérios correspondentes de **Perfil para manter**. Você pode selecionar o seguinte:<br>
- **Resolva os empates usando**: Data de criação, Data de atualização, Última sessão
- **Priorização**: Mais novo, mais antigo

O painel "Edit rules" (Editar regras) com seções para selecionar opções para "Profile to keep" (Perfil a ser mantido) e "Resolving ties" (Resolver vínculos).]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Por exemplo, você pode manter o perfil que tem um número de telefone. Se vários usuários tiverem o mesmo número de telefone, você poderá resolver os empates usando o campo **Data de atualização** e priorizar o usuário atualizado mais recentemente.

### Etapa 2: Visualizar os resultados (opcional)

Depois de salvar suas regras, você pode visualizar como elas funcionarão selecionando **Generate a list of duplicates (Gerar uma lista de duplicatas**). O Braze gerará sua visualização e a enviará para seu endereço de e-mail como um arquivo CSV que mostra quais usuários seriam mantidos e mesclados se suas regras fossem aplicadas. 

### Etapa 3: Mesclar duplicatas

Se estiver satisfeito com os resultados da visualização, retorne à página **Manage Audience (Gerenciar público** ) e selecione **Merge all duplicates (Mesclar todas as duplicatas**).

{% alert warning %}
Os perfis de usuário duplicados não podem ser recuperados após a fusão.
{% endalert %}

## Mesclagem programada

Semelhante à mesclagem baseada em regras, a mesclagem programada permite automatizar a mesclagem de perfis de usuário diariamente usando regras pré-configuradas.

\![A página "Manage Audience" (Gerenciar público) com o botão "schedule" (agendar).]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Depois que o recurso for ativado, o Braze atribuirá automaticamente um intervalo de tempo para realizar o processo de mesclagem diariamente, aproximadamente às 12 horas, no fuso horário da empresa do usuário. Você pode desativar a mesclagem programada a qualquer momento. O Braze notificará os administradores de seu espaço de trabalho 24 horas antes da mesclagem programada, fornecendo um lembrete e tempo para revisar a configuração.

{% alert warning %}
Os perfis de usuário duplicados não podem ser recuperados após a fusão.
{% endalert %}
