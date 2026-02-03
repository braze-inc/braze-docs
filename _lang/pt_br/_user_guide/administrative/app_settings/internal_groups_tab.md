---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artigo de referência descreve os grupos internos, uma ótima maneira de obter insights sobre os registros de SDK ou API do seu dispositivo de teste ao testar a integração de SDK."

---

# Grupos internos

> Os grupos internos são uma ótima maneira de criar e organizar grupos de teste internos ou de terceiros. Eles fornecem insight sobre os registros do SDK ou da API e são úteis ao testar a integração do SDK. É possível criar um número ilimitado de grupos internos personalizados com até 1.000 usuários.

{% alert tip %}
Também recomendamos que você confira nosso curso [Testes e Solução de Problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting) do Braze Learning, que aborda como usar grupos internos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

## Pré-requisitos

Para criar e gerenciar grupos internos, é necessário ter a [permissão Access Dev Console]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) para o seu espaço de trabalho.

## Criação de um grupo interno

Para criar um grupo interno: 

1. Acesse **Configurações** > **Grupos internos**.
2. Selecione **Criar grupo interno**.
3. Dê um nome ao seu grupo, como "Grupo de teste de e-mail".
4. Escolha um ou mais tipos de grupo, conforme listado na tabela a seguir.

| Tipo de grupo         | Descrição                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuários**   | Use-o para verificar eventos ou registros do seu dispositivo de teste.                                    |
| **Grupo de teste de conteúdo** | Use isso em mensagens push, de e-mail e no app para enviar uma cópia renderizada da mensagem. |
| **Grupo de teste**         | Envia automaticamente uma cópia do e-mail para todos no grupo de teste após o envio.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Um grupo interno chamado "Grupo de teste de e-mail".]({% image_buster /assets/img_archive/internal_group.png %})

### Adição de usuários de teste

Depois de criar o grupo interno, adicione os usuários teste como membros desse grupo. 

1. Na página de gerenciamento do seu grupo interno, selecione **Add test users (Adicionar usuários de teste**).
2. Escolha um dos seguintes métodos para pesquisar e selecionar seus usuários teste.

| Método                  | Descrição                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Adicionar usuário identificado** | Pesquise o usuário por sua ID de usuário externo, endereço de e-mail, número de telefone ou token por push.                                                                                                                                                           |
| **Adicionar usuário anônimo**  | Pesquise por endereço IP. Em seguida, forneça um nome para cada usuário teste que adicionar. Esse é o nome ao qual todos os registros de eventos estão associados na página [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Adicionar usuários em massa**      | Copie e cole uma lista de endereços de e-mail ou IDs externos. Você pode adicionar apenas usuários que já são conhecidos no dashboard. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configurações do grupo interno ao criar um novo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de teste de conteúdo

Semelhante ao envio de um teste prévio de uma mensagem, o Grupo de teste de conteúdo economiza seu tempo e permite lançar testes para uma lista predefinida de usuários do Braze simultaneamente. Isso está disponível para push, mensagens no app, SMS, e-mail e cartões de conteúdo no Braze. Somente os grupos marcados como Grupos de teste de conteúdo estão disponíveis na seção de prévia de uma mensagem.

{% alert note %}
As mensagens de teste [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) só podem ser enviadas para números de telefone válidos no banco de dados.
{% endalert %}

Selecione usuários individuais do Braze ou qualquer número de grupos internos para os quais enviar a mensagem. Se a sua mensagem incluir qualquer Liquid ou outra personalização dinâmica, o Braze usará as atribuições disponíveis para cada usuário para personalizar o conteúdo da mensagem. Para usuários que não têm atribuições, o Braze usa o conjunto de valores padrão.

Além disso, se você visualizar a mensagem como um usuário aleatório, um usuário personalizado ou um usuário existente, poderá enviar essa versão prévia. Desmarcar a caixa de seleção permite enviar com base nas atribuições de cada usuário em relação à versão prévia.

Se você usar um pool de IP para enviar um e-mail, selecione de qual pool de IP enviar o e-mail selecionando o pool no menu suspenso disponível.

![A seção Teste do editor de mensagens no app para selecionar o Grupo de teste de conteúdo.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos de teste

Os grupos de teste são compatíveis apenas com o canal de e-mail. Adicione usuários a um grupo de teste para enviar cópias de cada mensagem de variante de e-mail a todos os membros do grupo.

Os grupos de teste não estão disponíveis para campanhas da API, mas você pode incluir grupos de teste usando uma entrada disparada pela API na campanha. Use isso para medir as métricas de entregabilidade e para manter um registro do conteúdo do e-mail para fins de histórico e arquivamento. 

Depois de criar um grupo interno e marcá-lo para ser usado como um grupo de teste, selecione-o na etapa de **públicos-alvo** do editor de campanhas ou na etapa de **configurações de envio** em um Canvas. 

Os e-mails semente terão o endereço `[SEED]` anexado ao início da linha de assunto do e-mail. Observe que os e-mails semente **não o fazem**:

- O incremento é enviado na análise de dados do dashboard.
- Impacto da análise de dados de e-mail ou redirecionamento. 
- Atualize a lista **Campaign Received** de um perfil de usuário.
- Limite de frequência de impacto.
- Contabilizar ou afetar os limites de frequência da velocidade de entrega.

#### Comportamento da inscrição

Os envios semeados são projetados para controle de qualidade e revisão internos, portanto, eles intencionalmente ignoram as verificações de inscrição para os usuários do dashboard semeado. Isso significa que os usuários com endereços de e-mail válidos que fazem parte de um Seed Group recebem a mensagem mesmo que não estejam inscritos. No entanto, a mensagem deve ser configurada para enviar cópias de teste para esse grupo.

{% alert tip %}
Se os membros do Seed Group informarem que não estão vendo a mensagem na caixa de entrada, verifique se eles estão listados no grupo interno, verifique se as linhas de assunto são diferentes e se o Gmail não agrupou os e-mails ou peça que verifiquem as pastas de spam.
{% endalert %}

#### Para campanhas

Ao criar uma campanha de e-mail, edite seus grupos de teste na seção **Públicos-alvo** do editor.

{% alert important %}
Se você configurar um grupo de teste para ser anexado automaticamente a todas as campanhas, ele só se aplicará a novas campanhas. Isso não se aplica quando você copia campanhas existentes. É necessário aplicar manualmente os grupos de teste desejados à campanha copiada na seção **Públicos-alvo**.
{% endalert %}

Os grupos de teste são enviados para cada variante de e-mail uma vez e são entregues na primeira vez que o usuário recebe essa variante específica. No caso de mensagens programadas, normalmente é a primeira vez que a campanha é lançada. Para campanhas baseadas em ações ou disparadas por API, esse é o momento em que o primeiro usuário recebe uma mensagem.

Se sua campanha for multivariante e sua variante tiver uma porcentagem de envio de 0%, ela não será enviada para os grupos de teste. Além disso, se a variante já tiver sido enviada e não tiver sido atualizada para reenvio em **Edit Seed Groups (Editar grupos de teste** ) na etapa **Target** (Destino), ela não será enviada novamente por padrão.

{% alert note %}
Se você tiver uma campanha recorrente e qualquer uma das variantes for atualizada, poderá optar por enviar novamente apenas para as variantes atualizadas ou para todas as variantes, ou desativar o envio do grupo de teste após a atualização.
{% endalert %}

![O grupo de teste "Email seed test" selecionado para receber a campanha de e-mail da variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para Canvas

Os grupos de teste no Canva funcionam de forma semelhante a qualquer campanha disparada. O Braze detecta automaticamente todas as etapas que contêm uma mensagem de e-mail e envia para elas quando o usuário chega pela primeira vez a essa etapa específica de e-mail.

Se uma etapa de e-mail tiver sido atualizada após o envio do grupo de teste, o Braze apresentará a opção de enviar somente para etapas atualizadas, para todas as etapas ou desativar as sementes.