---
nav_title: Configurações de segurança
article_title: Configurações de segurança
page_order: 2
page_type: reference
description: "Este artigo de referência aborda configurações genéricas de segurança entre empresas, incluindo regras de autenticação, lista de permissões de IP, IPI e autenticação de dois fatores (2FA)."

---

# Configurações de segurança

> Como administrador, a segurança é uma alta prioridade em sua lista de preocupações. A página **Configurações de segurança** pode ajudá-lo a gerenciar as configurações de segurança genéricas e entre empresas, incluindo regras de autenticação, lista de permissões de IP e autenticação de dois fatores.

Para acessar essa página, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), selecione o menu suspenso da sua conta e acesse **Configurações da empresa** > **Configurações de segurança**.
{% endalert %}

## Regras de autenticação

### Comprimento da senha

Use esse campo para alterar o comprimento mínimo de senha exigido. O mínimo padrão é de oito caracteres.

### Complexidade da senha

Selecione **Aplicar senhas complexas** para exigir que as senhas incluam pelo menos um dos seguintes itens: 
- Letra maiúscula
- Letra minúscula
- Número
- Caractere especial

### Reusabilidade da senha

Determina o número mínimo de novas senhas que devem ser definidas para que um usuário possa reutilizar uma senha. O padrão é três.

### Regras de expiração da senha

Use esse campo para definir quando deseja que os usuários da sua conta Braze redefinam a senha.

### Regras de duração da sessão

Use esse campo para definir por quanto tempo o Braze manterá sua sessão ativa. Depois que a Braze considerar sua sessão inativa (nenhuma atividade durante o número definido de minutos), o usuário será registrado. O número máximo de minutos que você pode inserir é 10.080 (igual a uma semana) se a autenticação de dois fatores for aplicada em sua empresa; caso contrário, a duração máxima da sessão será de 1.440 minutos (igual a 24 horas).

### Autenticação de logon único (SSO)

É possível restringir o registro de seus usuários usando uma senha ou SSO.

Para [SAML SSO][15], os clientes precisam definir suas configurações de SAML antes de aplicar. Se os clientes usarem o SSO do Google, eles só precisarão aplicar a página de configurações de segurança sem nenhuma elevação adicional.

## Lista de permissões de IP do dashboard

Use o campo mostrado para listar endereços IP e sub-redes específicos a partir dos quais os usuários podem registrar a sua conta (por exemplo, a partir de uma rede da empresa ou VPN). Especifique endereços IP e sub-redes como intervalos CIDR em uma lista separada por vírgulas. Se isso não for especificado, os usuários poderão fazer login de qualquer endereço IP.

## autenticação de dois fatores

A autenticação de dois fatores é necessária para todos os usuários do Braze. Ele adiciona um segundo nível de verificação de identidade a um registro de conta, tornando-o mais seguro do que apenas um nome de usuário e uma senha. Se o seu dashboard não suportar a autenticação de dois fatores, entre em contato com o gerente de sucesso do cliente. 

Quando a autenticação de dois fatores estiver ativada, além de digitar uma senha, os usuários precisarão digitar um código de verificação ao registrar sua conta Braze. O código pode ser enviado por meio de um app autenticador, e-mail ou SMS.

Os usuários que não configurarem a autenticação de dois fatores serão bloqueados em sua conta Braze. Os usuários da conta Braze também podem configurar a autenticação de dois fatores por conta própria nas **Configurações da conta**, mesmo que não seja exigido pelo administrador.

### Lembre-se de mim

![Caixa de seleção Lembrar esta conta por 30 dias][04]{: style="float:right;max-width:40%;margin-left:15px;"}

Depois de ativar a autenticação de dois fatores para sua empresa, a caixa de seleção **Lembrar de mim** fica disponível para os usuários. Esse recurso armazena um cookie no dispositivo, exigindo o registro com a autenticação de dois fatores apenas uma vez ao longo de 30 dias.

Os clientes com várias contas em uma empresa dashboard podem ter problemas ao usar esse recurso devido ao fato de o cookie estar vinculado a um dispositivo específico. Se os usuários usarem o mesmo dispositivo para registrar várias contas, o cookie será substituído para as contas autorizadas anteriormente nesse dispositivo. O Braze espera que apenas um dispositivo seja associado a uma conta, e não um dispositivo para várias contas.

Não se esqueça de salvar suas alterações antes de sair da página!

### Redefinição da autenticação do usuário

Os usuários que tiverem problemas para registrar a autenticação de dois fatores podem entrar em contato com os administradores da empresa para redefinir a autenticação de dois fatores. Para fazer isso, peça a um administrador que execute as seguintes etapas:

1. Acessar **Configurações** > **Usuários da Empresa**.
2. Selecione o usuário na lista fornecida.
3. Selecione **Reset (Redefinir** ) em **Two Factor Authentication (Autenticação de dois fatores**).

Uma redefinição pode resolver problemas comuns de autenticação, como problemas com apps de autenticação, envio de e-mail não enviado, falha de login devido a interrupções de SMS ou erro do usuário e muito mais.

## Baixando um relatório de evento de segurança

O relatório de eventos de segurança é um relatório CSV de eventos de segurança, como convites para contas, remoções de contas, tentativas de login bem-sucedidas e com falha e outras atividades. Você pode usá-lo para realizar auditorias internas.

Para baixar esse relatório, faça o seguinte:

1. Acesse **Configurações** > **Configurações administrativas**.
2. Selecione a guia **Security Settings (Configurações de segurança** ) e acesse a seção **Security Event Download (Baixar eventos de segurança** ).
2. Selecione **Baixar relatório**. 

Esse relatório contém apenas os 10.000 eventos de segurança mais recentes de sua conta. Se precisar de dados de eventos específicos, entre em contato com o suporte técnico.

{% details Eventos de segurança relatados %}
### Login e conta 
- EVENTO_DO_DESENVOLVEDOR REMOVIDO
- EVENTO_DO_DESENVOLVEDOR_ADICIONADO
- SIGNED_IN_EVENT
- FAILED_LOGIN_EVENT
- TWO_FACTOR_AUTH_SETUP_COMPLETED
- TWO_FACTOR_AUTH_RESET_COMPLETED
- CLEARED_DEVELOPER_TWO_FACTOR_AUTH_EVENT
- DEVELOPER_SUSPENDED_EVENT
- DEVELOPER_UNSUSPENDED_EVENT

### Acesso elevado
- EVENTO_DE_FLUXO_DE_ACESSO_ELEVADO_INICIADO
- EVENTO_DE_FLUXO_DE_ACESSO_ELEVADO_COMPLETADO
- ELEVATED_ACCESS_FLOW_2FA_FAILED_EVENT

### Campanha interrompida
- EVENTO_DE_CAMPANHA_ADICIONADO
- EVENTO_DE_CAMPANHA_EDITADO

### Canva
- EVENTO_DE_FLUXO_ADICIONADO
- EVENTO_DE_FLUXO_DE_TRABALHO_EDITADO

### Segmento
- EVENTO_DE_SEGMENTO_ADICIONADO
- EVENTO_DE_SEGMENTO_EDITADO
- EXPORTED_SEGMENT_TO_CSV
- EXPORTED_SEGMENT_VIA_API

### Chave da API REST
- CHAVE_DE_API_ADICIONADA
- REMOVED_REST_API_KEY

### Credencial de autenticação básica
- CREDENCIAL_BASIC_AUTH_ADICIONADA
- UPDATED_BASIC_AUTH_CREDENTIAL
- REMOVED_BASIC_AUTH_CREDENTIAL

### Permissão
- CLEARED_DEVELOPER_TWO_FACTOR_AUTH_EVENT
- UPDATED_DEVELOPER_PERMISSION_EVENT

### Configurações da empresa
- GRUPO_APP_ADICIONADO
- EVENTO_APLICATIVO_ADICIONADO

### Modelo de e-mail
- ADDED_EMAIL_TEMPLATE
- UPDATED_EMAIL_TEMPLATE

### Credencial push
- UPDATED_PUSH_CREDENTIAL
- REMOVED_PUSH_CREDENTIAL

### Depurador do SDK
- STARTED_SDK_DEBUGGER_SESSION
- EXPORTED_SDK_DEBUGGER_LOGS
{% enddetails %}

## Visualização de informações de identificação pessoal (IPI) {#view-pii}

A permissão **View IPI** só pode ser acessada por alguns usuários selecionados do Braze. Para conhecer os recursos de permissão de equipe existentes, consulte [Definição de permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

Por padrão, todos os administradores têm a permissão **View IPI** ativada nas [permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Isso significa que eles podem ver os seguintes atributos padrão e personalizados em todo o dashboard. Quando essa permissão é desativada para os usuários, esses usuários não poderão ver essas informações.

### Definição de IPI

Você pode definir quais campos são designados como IPI no dashboard. Para fazer isso, acesse **Configurações da empresa** > **Configurações de segurança**.

Os campos a seguir podem ser ocultados dos usuários do Braze que não têm permissões para **Visualizar IPI**.

| Atribuições padrão | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Endereço de e-mail </li> <li> Número de telefone </li> <li> Nome </li> <li> Sobrenome </li> <li> Gênero </li> <li> Data de nascimento </li> <li> IDs de dispositivo </li> <li> Local mais recente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos os atributos personalizados<ul><li>Atributos personalizados individuais podem ser marcados como IPI se você não precisar ocultar todos os atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Áreas limitadas

A seguir, presume-se que todos os campos estão definidos como IPI e que os usuários mencionados são aqueles que usam a plataforma Braze.

| Navegação no dashboard | Resultado | Notas |
| -------------------- | ------ | ----- |
| Pesquisa de usuários | O usuário que faz o registro não consegue pesquisar por endereço de e-mail, número de telefone, nome ou sobrenome: {::nomarkdown} <ul> <li> Não serão mostrados os atributos padrão e personalizados anteriores ao visualizar um perfil de usuário. </li> <li> Não é possível editar as atribuições padrão anteriores de um perfil de usuário no dashboard do Braze. </li> </ul> {:/} | O acesso a essa seção ainda requer acesso para visualizar o perfil do usuário. |
| Importação de usuário | O usuário não pode baixar arquivos da página **Importação de usuário**. | |
| {::nomarkdown} <ul> <li> Segmentos </li> <li> Campanhas </li> <li> Canva </li> </ul> {:/} | No menu suspenso **Dados de usuários**: {::nomarkdown} <ul> <li> O usuário não terá a opção <b>Exportar endereço de e-mail CSV</b>. </li> <li> O usuário não receberá os atributos padrão e de cliente anteriores no arquivo CSV ao selecionar <b>Exportar dados do usuário CSV</b>. </li> </ul> {:/} | |
| Grupo de teste interno | O usuário não terá acesso às atribuições padrão anteriores de nenhum usuário adicionado ao grupo de teste interno. | |
| Registro de atividades de mensagens | O usuário não terá acesso às atribuições padrão anteriores para nenhum usuário identificado no registro de atividades de mensagens. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Ao fazer a prévia de uma mensagem, a permissão **Exibir IPI** não é aplicada, de modo que os usuários podem ver os atributos padrão anteriores se eles foram referenciados na mensagem por meio do Liquid.
{% endalert %}

## Preferências de exclusão de dados 

Você pode usar essa configuração para definir preferências sobre se determinados campos devem ser excluídos durante o processo de exclusão de usuários para eventos. Essas preferências afetam apenas os dados de usuários que foram excluídos do Braze. 

Quando um usuário é excluído, a Braze remove todos os IPI dos dados dos eventos, mas retém os dados anônimos para fins de análise de dados. Alguns campos definidos pelo usuário podem conter IPI se você enviar informações do usuário final para a Braze. Se esses campos contiverem IPI, você poderá aceitar a exclusão dos dados quando os dados do evento forem anonimizados para usuários excluídos; se os campos não contiverem IPI, eles poderão ser retidos para análise de dados.

Você é responsável por determinar as preferências corretas para seu espaço de trabalho. A melhor maneira de determinar as configurações apropriadas é revisar com as equipes internas que enviam dados de eventos para o Braze e com as equipes que usam extras de mensagens no Braze para confirmar se os campos podem conter IPI.  

### Campos relevantes  

| Nome ou tipo do evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | propriedades |  |
| Evento de compra | propriedades |  |
| Envio de mensagens | message_extras | Vários tipos de eventos contêm um campo message_extras. A preferência se aplica a todos os tipos de eventos de envio de mensagens que suportam message_extras, inclusive os tipos de eventos adicionados no futuro. |

{% alert warning %}
**A exclusão é permanente!** Se houver aceitação de remover quaisquer campos do Snowflake para usuários excluídos, a configuração será aplicada a todos os dados históricos em seus espaços de trabalho e a quaisquer eventos para usuários excluídos no futuro. Depois que o Braze tiver executado o processo para aplicar as configurações aos dados de eventos históricos para usuários excluídos, os dados **não poderão ser restaurados**.
{% endalert %}

### Configurar preferências

Defina as preferências padrão marcando as caixas dos campos que devem ser removidos se um usuário for excluído. Selecione qualquer um dos campos que contenham IPI. Essa preferência será aplicada a todos os espaços de trabalho atuais e futuros, a menos que os espaços de trabalho sejam explicitamente adicionados a um grupo de preferências.

Para personalizar as preferências por espaço de trabalho, você pode adicionar grupos de preferências com configurações diferentes das padrão. Aplicamos as configurações padrão a todos os espaços de trabalho não adicionados a um grupo de preferências adicional, incluindo espaços de trabalho criados no futuro.  

![]({% image_buster /assets/img/deletion_preferences_1.png %})


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "perfil de usuário ofuscado1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "perfil de usuário ofuscado2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "perfil de usuário ofuscado3"

[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
