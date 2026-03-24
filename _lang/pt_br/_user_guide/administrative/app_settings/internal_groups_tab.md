---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artigo de referência descreve grupos internos, uma ótima maneira de obter insights sobre os logs de SDK ou API do seu dispositivo de teste ao testar a integração do SDK."

---

# Grupos internos

> Grupos internos são uma ótima maneira de construir e organizar grupos de teste internos ou de terceiros. Eles fornecem insights sobre os logs de SDK ou API e são úteis ao testar sua integração de SDK. Você pode criar um número ilimitado de grupos internos personalizados com até 1.000 usuários.

{% alert tip %}
Também recomendamos conferir nosso curso do Braze Learning [Testes e Solução de Problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting), que aborda como usar grupos internos para realizar sua própria solução de problemas e depuração.
{% endalert %}

## Pré-requisitos

Para criar e gerenciar grupos internos, você precisa da [permissão de acesso ao console de desenvolvedor legado]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) ou dessas [permissões granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions):

- Exibir chaves de API
- Editar chaves de API
- Ver Grupos Internos
- Editar Grupos Internos
- Visualizar registro de atividades de envio de mensagem
- Exibir registro de usuários de eventos
- Ver identificadores de API
- Exibir o dashboard de uso da API
- Exibir limites da API
- Exibir alertas de uso da API
- Editar alertas de uso da API
- Editar depurador do SDK
- Exibir depurador do SDK

{% multi_lang_include deprecations/user_permissions.md %}

## Criando um grupo interno

Para criar um grupo interno: 

1. Acesse **Configurações** > **Grupos internos**.
2. Selecione **Criar grupo interno**.
3. Dê um nome ao seu grupo, como "Grupo de teste de e-mail".
4. Escolha um ou mais tipos de grupo, conforme listado na tabela a seguir.

| Tipo de grupo         | Descrição                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuários**   | Use isso para verificar eventos ou logs do seu dispositivo de teste.                                    |
| **Grupo de teste de conteúdo** | Use isso em push, e-mail e mensagens no aplicativo para enviar uma cópia renderizada da mensagem. |
| **Grupo de teste**         | Envia automaticamente uma cópia do e-mail para todos no Grupo de Teste ao enviar.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Um grupo interno chamado "Grupo de teste de e-mail".]({% image_buster /assets/img_archive/internal_group.png %})

### Adição de usuários de teste

Após criar seu grupo interno, adicione usuários de teste como membros desse grupo. 

1. Na página de gerenciamento do seu grupo interno, selecione **Adicionar usuários teste**.
2. Escolha entre os seguintes métodos para pesquisar e selecionar seus usuários teste.

| Método                  | Descrição                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Adicionar usuário identificado** | Pesquise o usuário pelo ID externo, endereço de e-mail, número de telefone ou token por push.                                                                                                                                                           |
| **Adicionar usuário anônimo**  | Pesquise por endereço IP. Em seguida, forneça um nome para cada usuário teste que você adicionar. Este é o nome com o qual todos os registros de eventos estão associados na página [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Adicionar usuários em massa**      | Copie e cole uma lista de endereços de e-mail ou IDs externos. Você pode adicionar apenas usuários que já são conhecidos no dashboard. Para saber mais, consulte [importação de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configurações do Grupo Interno ao criar um novo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de teste de conteúdo

Semelhante ao envio de uma prévia de teste de uma mensagem, o Grupo de Teste de Conteúdo economiza seu tempo e permite que você lance testes para uma lista pré-definida de usuários Braze simultaneamente. Isso está disponível para push, mensagens no app, SMS, e-mail e Cartões de Conteúdo no Braze. Apenas grupos marcados como Grupos de Teste de Conteúdo estão disponíveis na seção de prévia de uma mensagem.

{% alert note %}
As mensagens de teste [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) só podem ser enviadas para números de telefone válidos no banco de dados.
{% endalert %}

Selecione usuários Braze individuais ou qualquer número de grupos internos para enviar a mensagem. Se sua mensagem incluir qualquer Liquid ou outra personalização dinâmica, o Braze usa os atributos disponíveis para cada usuário para personalizar o conteúdo da mensagem. Para usuários que não têm atributos, o Braze usa o valor padrão definido.

Além disso, se você visualizar a mensagem como um usuário aleatório, um usuário personalizado ou um usuário existente, você pode enviar essa versão pré-visualizada em vez disso. Desmarcar a caixa de seleção permite que você envie com base nos atributos de cada usuário em vez da versão pré-visualizada.

Se você usar um pool de IP para enviar um e-mail, selecione de qual pool de IP enviar o e-mail selecionando o pool no menu suspenso disponível.

![A seção de Teste do editor de mensagens no app para selecionar o Grupo de Teste de Conteúdo.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos de teste

Grupos Seed são suportados apenas para o canal de e-mail. Adicione usuários a um grupo de teste para enviar cópias de cada variante de mensagem de e-mail para todos os membros do grupo.

Grupos de teste não estão disponíveis para campanhas de API, mas você pode incluir grupos de teste usando uma entrada acionada por API na campanha. Use isso para medir métricas de entregabilidade e para manter um registro do conteúdo do seu e-mail para fins históricos e de arquivamento. 

Após criar um grupo interno e marcá-lo para ser usado como um grupo de teste, selecione-o na etapa **Públicos-Alvo** do editor de campanha, ou na etapa **Configurações de Envio** em um canva. 

E-mails de teste terão `[SEED]` anexado ao início da linha de assunto do e-mail. Observe que os e-mails de teste **não**:

- Incrementar envios nas análises do dashboard.
- Impactar análises de e-mail ou redirecionamento. 
- Atualizar a lista **Campanha Recebida** do perfil de um usuário.
- Impactar limites de frequência.
- Considerar ou impactar os limites de taxa de velocidade de entrega.

#### Comportamento da inscrição

Envios de teste são projetados para QA interno e revisão, portanto, eles intencionalmente ignoram verificações de inscrição para os usuários da empresa testada. Isso significa que usuários com endereços de e-mail válidos que fazem parte de um grupo de teste recebem a mensagem mesmo que não estejam inscritos. No entanto, a mensagem deve ser configurada para enviar cópias de teste para esse grupo.

{% alert tip %}
Se os membros do seu grupo de teste relatarem que não estão vendo a mensagem em suas caixas de entrada, verifique se eles estão listados no grupo interno, verifique se suas linhas de assunto são diferentes e se o Gmail não agrupou os e-mails, ou peça que verifiquem suas pastas de spam.
{% endalert %}

#### Para campanhas

Ao compor uma campanha de e-mail, edite seus grupos de teste na seção **Públicos-Alvo** do editor.

{% alert important %}
Se você configurar um grupo de teste para anexar automaticamente a todas as campanhas, isso se aplica apenas a novas campanhas. Não se aplica quando você copia campanhas existentes. Você deve aplicar manualmente os grupos de teste desejados à campanha copiada na seção **Públicos-Alvo**.
{% endalert %}

Os grupos de teste são enviados para cada variante de e-mail uma vez e são entregues na primeira vez que o usuário recebe essa variante específica. No caso de mensagens programadas, normalmente é a primeira vez que a campanha é lançada. Para campanhas baseadas em ação ou acionadas por API, este é o momento em que o primeiro usuário recebe uma mensagem.

Se sua campanha é multivariante e sua variante tem uma porcentagem de envio de 0%, ela não é enviada para os Grupos de Teste. Além disso, se a variante já foi enviada e não foi atualizada para reenviar em **Editar Grupos de Teste** na etapa **Alvo**, ela não é enviada novamente por padrão.

{% alert note %}
Se você tem uma campanha recorrente e qualquer uma das variantes for atualizada, você pode escolher enviar novamente apenas as variantes atualizadas ou todas as variantes, ou desativar o envio para Grupos de Teste ao atualizar.
{% endalert %}

![O "teste de e-mail seed" Grupo de Teste selecionado para receber a campanha de e-mail da Variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para Canvas

Os grupos de teste no Canva funcionam de maneira semelhante a qualquer campanha acionada. O Braze detecta automaticamente todas as etapas que contêm uma mensagem de e-mail e envia para essas quando seu usuário atinge pela primeira vez essa etapa de e-mail específica.

Se uma etapa de e-mail foi atualizada após o Grupo de Teste ter sido enviado, o Braze apresenta a opção de enviar apenas para etapas atualizadas, todas as etapas ou desativar os seeds.