---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artigo de referência aborda os grupos internos, uma ótima maneira de obter insights sobre os registros de SDK ou API do seu dispositivo de teste ao testar a integração de SDK."

---

# Grupos internos

> Os grupos internos são uma ótima maneira de criar e organizar grupos de teste internos ou de terceiros. Eles fornecem insight sobre os registros do SDK ou da API e são úteis ao testar a integração do SDK. É possível criar um número ilimitado de grupos internos personalizados com até 1.000 usuários.

{% alert tip %}
Também recomendamos que você confira nosso curso [Testes e Solução de Problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting) do Braze Learning, que aborda como usar grupos internos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

## Pré-requisitos

Antes de poder criar e gerenciar grupos internos, você precisa da [permissão Access Dev Console]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) para o seu espaço de trabalho.

## Criação de um grupo interno

Para criar um grupo interno, faça o seguinte: 

1. Acesse **Configurações** > **Grupos internos**.
2. Selecione **Criar grupo interno**.
3. Dê um nome ao seu grupo, como "Grupo de teste de e-mail".
4. Escolha um ou mais tipos de grupo, conforme listado na tabela a seguir.

| Tipo de grupo         | Descrição                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuários**   | Usado para verificar eventos ou registros do seu dispositivo de teste.                                    |
| **Grupo de teste de conteúdo** | Pode ser usado em mensagens push, de e-mail e no app para enviar uma cópia renderizada da mensagem. |
| **Grupo de teste**         | Envia automaticamente uma cópia do e-mail para todos os membros do grupo de teste após o envio.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Um grupo interno chamado "Grupo de teste de e-mail".]({% image_buster /assets/img_archive/internal_group.png %})

### Adição de usuários de teste

Depois de criar o grupo interno, é possível adicionar usuários de teste como membros desse grupo. 

1. Na página de gerenciamento do seu grupo interno, selecione **Add test users (Adicionar usuários de teste**).
2. Escolha um dos seguintes métodos para pesquisar e selecionar seus usuários teste.

| Método                  | Descrição                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Adicionar usuário identificado** | Pesquise o usuário por sua ID de usuário externo, endereço de e-mail, número de telefone ou token por push.                                                                                                                                                           |
| **Adicionar usuário anônimo**  | Pesquise por endereço IP. Em seguida, forneça um nome para cada usuário teste adicionado. Esse é o nome ao qual todos os registros de eventos serão associados na página [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Adicionar usuários em massa**      | Copie e cole uma lista de endereços de e-mail ou IDs externos. Só é possível adicionar usuários que já sejam conhecidos no dashboard. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configurações do grupo interno ao criar um novo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de teste de conteúdo

Semelhante ao envio de um teste prévio de uma mensagem, o Grupo de teste de conteúdo economiza seu tempo e permite lançar testes para uma lista predefinida de usuários do Braze simultaneamente. Isso está disponível para mensagens push, mensagens no app, SMS, e-mail e cartões de conteúdo no Braze. Somente os grupos marcados como Grupos de teste de conteúdo estarão disponíveis na seção de prévia de uma mensagem.

{% alert note %}
As mensagens de teste [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) só podem ser enviadas para números de telefone válidos no banco de dados.
{% endalert %}

É possível selecionar usuários individuais do Braze ou tantos grupos internos para os quais enviar a mensagem. Se a sua mensagem incluir qualquer Liquid ou outra personalização dinâmica, o Braze usará as atribuições disponíveis para cada usuário para personalizar o conteúdo da mensagem. Para usuários que não têm atribuições, a Braze usará o valor padrão definido.

Além disso, se você visualizar a mensagem como um usuário aleatório, personalizado ou existente, poderá enviar essa versão prévia. Desmarcar a caixa de seleção permite enviar com base nas atribuições de cada usuário em relação à versão prévia.

Se você usar um pool de IP para enviar um e-mail, poderá selecionar de qual pool de IP gostaria que o e-mail fosse enviado, selecionando o pool no menu suspenso disponível.

![A seção Teste do editor de mensagens no app para selecionar o Grupo de teste de conteúdo.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos de teste

Os grupos de teste são compatíveis apenas com o canal de e-mail. É possível adicionar usuários a um grupo de teste para enviar cópias de cada mensagem de variante de e-mail a todos os membros do grupo.

Os grupos de teste não estão disponíveis para campanhas da API, mas você pode incluir grupos de teste usando uma entrada disparada pela API na campanha. Isso pode ser usado para medir as métricas de entregabilidade e para manter um registro do conteúdo do e-mail para fins de histórico e arquivamento. 

Depois de criar um grupo interno e marcá-lo para ser usado como um grupo de teste, você pode selecioná-lo na etapa de **públicos-alvo** do editor de campanhas ou na etapa de **configurações de envio** em um Canva. 

Os e-mails semente terão o endereço `[SEED]` anexado ao início da linha de assunto do e-mail. Observe que os e-mails semente **não o fazem**:

- O incremento envia a análise de dados do dashboard.
- Impacto da análise de dados de e-mail ou redirecionamento. 
- Atualize a lista **Campaign Received** de um perfil de usuário.
- Limite de frequência de impacto.

{% alert tip %}
Se os membros do Seed Group informarem que não estão vendo a mensagem na caixa de entrada, verifique se eles estão listados no grupo interno, verifique se as linhas de assunto são diferentes e se o Gmail não agrupou os e-mails ou peça que verifiquem as pastas de spam.
{% endalert %}

#### Para campanhas

Ao criar uma campanha de e-mail, você pode editar seus grupos de teste na seção **Públicos-alvo** do editor.

Os grupos de teste são enviados para cada variante de e-mail uma vez e são entregues na primeira vez que o usuário recebe essa variante específica. No caso de mensagens programadas, normalmente é a primeira vez que a campanha é lançada. Para campanhas baseadas em ações ou disparadas por API, esse será o momento em que o primeiro usuário receberá uma mensagem.

Se sua campanha for multivariante e sua variante tiver uma porcentagem de envio de 0%, ela não será enviada para os grupos de teste. Além disso, se a variante já tiver sido enviada e não tiver sido atualizada para reenvio em **Edit Seed Groups (Editar grupos de teste** ) na etapa **Target** (Destino), ela não será enviada novamente por padrão.

{% alert note %}
Se você tiver uma campanha recorrente e qualquer uma das variantes for atualizada, poderá optar por enviar novamente apenas para as variantes atualizadas ou para todas as variantes, ou desativar o envio do grupo de teste após a atualização.
{% endalert %}

![O grupo de teste "Email seed test" selecionado para receber a campanha de envio de e-mail da variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para Canvas

Os grupos de teste no Canvas funcionam de forma semelhante à de qualquer campanha disparada. O Braze detecta automaticamente todas as etapas que contêm uma mensagem de e-mail e enviará para elas quando o usuário chegar a essa etapa específica de e-mail pela primeira vez.

Se uma etapa de e-mail tiver sido atualizada após o envio do grupo de teste, será apresentada a opção de enviar apenas para etapas atualizadas, todas as etapas ou desativar as sementes.

