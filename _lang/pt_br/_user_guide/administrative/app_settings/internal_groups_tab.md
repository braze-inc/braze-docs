---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artigo de referência aborda os Grupos internos, uma ótima maneira de obter insights sobre os registros de SDK ou API do seu dispositivo de teste ao testar a integração de SDK."

---

# Grupos internos

> Os grupos internos são uma ótima maneira de criar e organizar grupos de teste internos ou de terceiros. Eles fornecem insights sobre os registros do SDK ou da API e são úteis ao testar a integração do SDK. Você pode criar um número ilimitado de grupos internos personalizados com até 1.000 membros.

Você precisa das [permissões]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **do Access Dev Console** do seu espaço de trabalho para criar e gerenciar grupos internos.

{% alert tip %}
Além deste artigo, também recomendamos que você confira nosso curso [Ferramentas de garantia de qualidade e depuração](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) do Braze Learning, que aborda como usar grupos internos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

## Criação de um grupo

Para criar um grupo interno, execute as etapas a seguir: 

1. Acesse **Configurações** > **Grupos internos**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Settings** > **Developer Console** > **Internal Groups**.
{% endalert %}

{:start="2"}
2\. Clique em **Criar grupo interno**.
3\. Dê ao seu grupo um nome significativo.
4\. Escolha um ou mais tipos de grupo, conforme listado na tabela a seguir.

![Criação de um grupo interno no Braze][7]

| Tipo de grupo     | Caso de uso     |
| :------------- | :------------- |
| Grupo de eventos de usuários| Usado para verificar eventos ou registros do seu dispositivo de teste.|
| Grupo de teste de conteúdo | Um conceito semelhante ao das Listas de teste. Pode ser usado em mensagens push, de e-mail e no app para enviar uma cópia renderizada da mensagem.|
| Grupo de teste | Envia automaticamente uma cópia do e-mail para todos os membros do grupo de teste após o envio.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Adição de usuários de teste

Depois de criar o grupo interno, é possível adicionar usuários de teste como membros desse grupo. Na página de gerenciamento do seu grupo interno, clique em **Add Test User (Adicionar usuário teste** ) e adicione-os como usuários identificados ou anônimos em massa.

![Configurações do grupo interno ao criar um novo grupo interno][8]

| Método de adição | Descrição |
| :------------- | :------------- |
| Usuários identificados |Pesquise o usuário pelo seu ID de usuário externo ou endereço de e-mail.|
|Usuários anônimos| Pesquise por endereço IP. Em seguida, forneça um nome para cada usuário teste adicionado. Esse é o nome ao qual todos os registros de eventos serão associados na página [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/).|
|Adicionar usuários em massa|Copie e cole uma lista de endereços de e-mail ou IDs externos na seção fornecida. Só é possível adicionar usuários que já sejam conhecidos no dashboard. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Grupos de teste de conteúdo

Semelhante ao envio de um teste prévio de uma mensagem, o Grupo de teste de conteúdo economiza seu tempo e permite lançar testes para uma lista predefinida de usuários do Braze simultaneamente. Essa funcionalidade está disponível para mensagens push, mensagens no app, SMS, e-mail e cartões de conteúdo no Braze.

{% alert note %}
As mensagens de teste [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) só podem ser enviadas para números de telefone válidos no banco de dados.
{% endalert %}

É possível selecionar usuários individuais do Braze ou tantos grupos internos para os quais enviar a mensagem. Se a sua mensagem incluir qualquer Liquid ou outra personalização dinâmica, o Braze usará as atribuições disponíveis para cada usuário para personalizar o conteúdo da mensagem. Para usuários que não têm atribuições, a Braze usará o valor padrão definido.

Além disso, se você visualizar a mensagem como um usuário aleatório, personalizado ou existente, poderá enviar essa versão prévia. Desmarcar a caixa de seleção permite enviar com base nas atribuições de cada usuário em relação à versão prévia.

Por fim, se você usar um pool de IP para enviar um e-mail, poderá selecionar de qual pool de IP gostaria que o e-mail fosse enviado, selecionando o pool no menu suspenso disponível.

Somente os grupos marcados como Grupos de teste de conteúdo estarão disponíveis na seção de prévia de uma mensagem.

![Envio de teste para grupos de teste de conteúdo][9]{: style="max-width:50%" }

### Grupos de teste

Os grupos de teste destinam-se apenas ao canal de envio de mensagens e permitem que você envie uma cópia de cada mensagem variante de e-mail para os membros desse grupo. Os grupos de teste não estão disponíveis para campanhas da API, embora você possa incluir grupos de teste por meio de uma entrada disparada pela API na campanha. Esse recurso é normalmente usado com parceiros como Return Path ou 250OK para medir as métricas de entregabilidade. Ele pode ser usado para manter um registro do conteúdo do e-mail para fins históricos e de arquivamento. 

Depois de criar um grupo interno e marcá-lo para ser usado como um grupo de teste, é possível selecioná-lo na etapa **Usuários-alvo** do criador da campanha ou na etapa **Configurações de envio** em um Canvas. Os e-mails semente terão o identificador `[SEED]` anexado ao início da linha de assunto do e-mail. Observe que os e-mails enviados como sementes não incrementam os envios na análise de dados do dashboard e não afetarão a análise de e-mail ou o redirecionamento. Eles também não atualizam a lista de **campanhas recebidas** do perfil de um usuário.

{% alert tip %}
Se os membros do Grupo de Sementes informarem que não estão vendo a mensagem na caixa de entrada, verifique se eles estão listados no Grupo Interno, verifique se as linhas de assunto são diferentes e se o Gmail não agrupou os e-mails ou peça que verifiquem as pastas de SPAM.
{% endalert %}

#### Para campanhas

Os grupos de teste podem ser editados na página **Direcionamento** ao criar uma campanha de e-mail.

Os grupos de teste são enviados para cada variante de e-mail uma vez e são entregues na primeira vez que o usuário recebe essa variante específica. No caso de mensagens programadas, normalmente é a primeira vez que a campanha é lançada. Para campanhas baseadas em ações ou disparadas por API, esse será o momento em que o primeiro usuário receberá uma mensagem.

Se sua campanha for multivariante e sua variante tiver uma porcentagem de envio de 0%, ela não será enviada para grupos de teste. Além disso, se a variante já tiver sido enviada e não tiver sido atualizada para reenvio em **Edit Seed Groups (Editar grupos de teste** ) na etapa **Target (Destino** ), ela não será enviada novamente por padrão.

{% alert note %}
Se houver uma campanha recorrente e for realizada uma atualização em qualquer uma das variantes, você terá a opção de reenviar somente para as variantes atualizadas, para todas as variantes ou de desativar o envio do grupo de teste após a atualização.
{% endalert %}

![Prévia de grupos de teste para uma campanha][11]

#### Para Canvas

Os grupos de teste no Canvas funcionam de forma semelhante à de qualquer campanha disparada. O Braze detecta automaticamente todas as etapas que contêm uma mensagem de e-mail e enviará para elas quando o usuário chegar a essa etapa específica de e-mail pela primeira vez.

Se uma etapa de e-mail tiver sido atualizada após o envio do grupo de teste, será apresentada a opção de enviar apenas para etapas atualizadas, todas as etapas ou desativar as sementes.


[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
