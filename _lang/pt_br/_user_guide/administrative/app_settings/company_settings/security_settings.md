---
nav_title: Configurações de segurança
article_title: Configurações de Segurança
page_order: 2
toc_headers: h2
page_type: reference
description: "Este artigo de referência cobre configurações de segurança genéricas entre empresas, incluindo regras de autenticação, lista de IPs permitidos, PII e autenticação de dois fatores (2FA)."

---

# Configurações de segurança

> Como administrador, a segurança é uma alta prioridade na sua lista de preocupações. A página **Configurações de Segurança** pode ajudá-lo a gerenciar as configurações de segurança genéricas entre empresas, incluindo regras de autenticação, lista de IPs permitidos e autenticação de dois fatores.

Para acessar esta página, vá para **Configurações** > **Configurações do Administrador** > **Configurações de Segurança**.

## Regras de autenticação

### Comprimento da senha

Use este campo para alterar o comprimento mínimo da senha exigido. O mínimo padrão é de oito caracteres.

### Complexidade da senha

Selecione **Impor senhas complexas** para exigir que as senhas incluam pelo menos um de cada um dos seguintes: 
- Letra maiúscula
- Letra minúscula
- Número
- Caractere especial

### Reutilização de senha

Determina o número mínimo de novas senhas que devem ser definidas antes que um usuário possa reutilizar uma senha. O padrão é três.

### Regras de expiração de senha

Use este campo para definir quando você deseja que os usuários da sua conta Braze redefinam suas senhas.

### Regras de duração da sessão

Use este campo para definir quanto tempo a Braze manterá sua sessão ativa. Após a Braze considerar sua sessão inativa (sem atividade pelo número definido de minutos), o usuário será desconectado. O número máximo de minutos que você pode inserir é 10.080 (igual a uma semana) se a autenticação de dois fatores for aplicada à sua empresa; caso contrário, a duração máxima da sessão será de 1.440 minutos (igual a 24 horas).

### Autenticação de login único (SSO)

Você pode restringir seus usuários de fazer login usando uma senha ou SSO.

Para [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/), os clientes precisam configurar suas configurações SAML antes de aplicar. Se os clientes usarem o SSO do Google, eles só precisam aplicar a página de configurações de segurança sem necessidade de ações adicionais.

## Lista de permissões de IP do painel

Use o campo mostrado para permitir endereços IP e sub-redes específicos dos quais os usuários podem fazer login na sua conta (por exemplo, de uma rede corporativa ou VPN). Especifique endereços IP e sub-redes como intervalos CIDR em uma lista separada por vírgulas. Se não especificado, os usuários poderão fazer login de qualquer endereço IP.

## Autenticação de dois fatores (2FA)

A autenticação de dois fatores é obrigatória para todos os usuários da Braze. Ela adiciona um segundo nível de verificação de identidade a um registro de conta, tornando-o mais seguro do que apenas um nome de usuário e senha. Se o seu painel não puder suportar a autenticação de dois fatores, entre em contato com seu gerente de sucesso do cliente. 

Quando a autenticação de dois fatores estiver ativada:

- Além de inserir uma senha, os usuários precisarão inserir um código de verificação ao fazer login em sua conta Braze. O código pode ser enviado através de um aplicativo autenticador, e-mail ou SMS. 
- A caixa de seleção **Lembre-se desta conta por 30 dias** fica disponível para os usuários.

Usuários que não configurarem a autenticação de dois fatores serão bloqueados de sua conta Braze. Os usuários da conta Braze também podem configurar a autenticação de dois fatores por conta própria em **Configurações da Conta**, mesmo que não seja exigido pelo administrador.

Certifique-se de salvar suas alterações antes de sair da página!

### Lembre-se desta conta por 30 dias {#remember-me}

Este recurso está disponível quando a autenticação de dois fatores está ativada.

Quando você seleciona **Lembre-se desta conta por 30 dias**, um cookie é armazenado em seu dispositivo, exigindo apenas que você faça login com autenticação de dois fatores uma vez ao longo de 30 dias. 

\![Caixa de seleção Lembre-se desta conta por 30 dias]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Clientes com várias contas sob uma empresa de painel podem enfrentar problemas ao usar este recurso devido ao cookie estar vinculado a um dispositivo específico. Se os usuários usarem o mesmo dispositivo para fazer login em várias contas, o cookie será substituído pelas contas autorizadas anteriormente nesse dispositivo. A Braze espera que apenas um dispositivo esteja associado a uma conta, não um dispositivo para várias contas.

### Redefinindo a autenticação do usuário

Se você estiver tendo problemas para fazer login com a autenticação de dois fatores, entre em contato com os administradores da sua empresa para redefinir sua autenticação de dois fatores. Os administradores podem realizar os seguintes passos:

1. Vá para **Configurações** > **Usuários da Empresa**.
2. Selecione o usuário da lista fornecida.
3. Selecione **Redefinir** em **Autenticação de Dois Fatores**.

Uma redefinição pode resolver problemas comuns de autenticação, como problemas com aplicativos autenticadores, verificação de e-mail não enviada, falha de login devido a interrupções de SMS ou erro do usuário, e mais.

### Requisitos para 2FA no nível da empresa

Primeiro, verifique se o 2FA está ativado para seu painel indo para **Configurações da Empresa** > **Configurações de Segurança** > **Autenticação de Dois Fatores**. Se o botão de alternância estiver cinza, o 2FA não foi ativado para sua empresa e não é obrigatório para todos os usuários do painel.

#### Opções do usuário quando o 2FA não é obrigatório

Se o 2FA não for aplicado a nível de empresa, os usuários individuais podem configurar o 2FA para si mesmos na página de Configurações da Conta. Nesse caso, os usuários não serão bloqueados de suas contas se não o configurarem. Você pode identificar quais usuários optaram por habilitar o 2FA verificando a página Gerenciar Usuários.

#### Requisitos quando o 2FA é obrigatório

Se o 2FA for aplicado a nível de empresa, os usuários que não o configurarem em suas próprias contas ao fazer login serão bloqueados do painel. Os usuários devem completar a configuração do 2FA para manter o acesso.

{% alert important %}
O 2FA é obrigatório para todos os usuários do Braze apenas se o Single Sign-On (SSO) não estiver habilitado. Se o SSO estiver em uso, o 2FA não precisa ser aplicado a nível de empresa.
{% endalert %}

## Configurando a autenticação de dois fatores (2FA)

### Configurando o 2FA com Authy

1. Baixe o aplicativo Authy da loja de aplicativos do seu dispositivo.
2. No Braze, insira seu número de telefone.
3. Toque na notificação enviada para o seu dispositivo solicitando que você abra o aplicativo Authy.
4. Inicie o aplicativo Authy no seu dispositivo para recuperar o código.
5. No Braze, insira o código de verificação que você recebeu do Authy.

Se você encontrar problemas durante o processo de configuração e for redirecionado para a página inicial do Braze ou tela de login, tente o seguinte:

- Use o modo de navegação anônima ou privada: Tente configurar novamente com uma janela de navegação anônima ou privada. Isso pode contornar problemas causados por extensões ou plugins do navegador.
- Tente um perfil de navegador diferente: Se o problema persistir, considere usar um perfil de navegador diferente para eliminar conflitos com plugins instalados.

### Configurando 2FA quando não é obrigatório

Para ativar manualmente a autenticação de dois fatores (2FA) na sua conta Braze quando não é obrigatório, siga estas etapas:

1. Baixe um aplicativo de 2FA como Authy, Google Authenticator, Okta Verify ou similar na App Store (iOS), Google Play Store (Android) ou na web. Ou, se preferir configurar 2FA com e-mail ou SMS, pule para a etapa 2.
2. No Braze, vá para Gerenciar Conta, role até a seção **Autenticação de Dois Fatores**, e selecione **Iniciar Configuração**.
3. Digite sua senha no modal de login e selecione **Verificar Senha**.
4. No modal de **Configuração da Autenticação de Dois Fatores**, insira seu número de telefone e selecione **Ativar**.
5. Copie o código gerado de sete dígitos do seu aplicativo de 2FA, e-mail ou mensagem SMS, e volte para o Braze e cole no modal de **Configuração da Autenticação de Dois Fatores**. Selecione **Verificar**.
6. (Opcional) Para evitar inserir 2FA pelos próximos 30 dias, ative a opção **Lembrar esta conta por 30 dias**.

## Acesso Elevado

O Acesso Elevado adiciona uma camada extra de segurança para ações sensíveis no seu painel Braze. Quando ativo, os usuários precisam re-verificar sua conta antes de exportar um segmento ou visualizar uma chave de API. Para usar o Acesso Elevado, vá para **Configurações** > **Configurações do Administrador** > **Configurações de Segurança** e ative-o. 

Se um usuário não conseguir re-verificar, será redirecionado para onde parou e não poderá continuar com a ação sensível. Após re-verificarem com sucesso, eles não precisarão fazer isso novamente na próxima hora—exceto se saírem primeiro.

\![Alternar Acesso Elevado.]({% image_buster /assets/img/elevated_access.png %})

## Baixando um relatório de evento de segurança {#security-event-report}

O relatório de Evento de Segurança é um relatório CSV de eventos de segurança, como convites de conta, remoções de conta, tentativas de login falhadas e bem-sucedidas, e outras atividades. Você pode usá-lo para realizar auditorias internas.

Para baixar este relatório, faça o seguinte:

1. Vá para **Configurações** > **Configurações do Admin**.
2. Selecione a aba **Configurações de Segurança** e vá para a seção **Download de Evento de Segurança**.
2. Selecione **Baixar relatório**. 

Este relatório contém apenas os 10.000 eventos de segurança mais recentes para sua conta. Se você precisar de dados de eventos específicos, entre em contato com o suporte técnico.

{% details Reported security events %}

### Login e conta 
- Conectado
- Login Falhado
- Configuração de Autenticação de Dois Fatores Concluída
- Redefinição de Autenticação de Dois Fatores Concluída
- Autenticação de Dois Fatores do Desenvolvedor Limpa
- Desenvolvedor Adicional Adicionado
- Conta Adicionada
- Desenvolvedor Suspenso
- Desenvolvedor Reativado
- Desenvolvedor Atualizado
- Desenvolvedor Removido
- Conta Removida
- Status da Assinatura do Usuário Atualizado
- Usuário Atualizado

### Acesso Elevado
- Iniciou o Fluxo de Acesso Elevado
- Fluxo de Acesso Elevado Concluído
- Falha na Verificação 2FA para Acesso Elevado

### Campanha
- Campanha Adicionada
- Campanha Editada

### Canvas
- Jornada Adicionada
- Jornada Editada

### Segmento
- Segmento Adicionado
- Segmento Editado
- Dados Exportados para CSV
- Segmento exportado via API

### chave da API REST
- Chave da API REST adicionada
- Chave da API REST removida

### Credencial de autenticação básica
- Credencial de autenticação básica adicionada
- Credencial de autenticação básica atualizada
- Credencial de autenticação básica removida

### Permissão
- Autenticação de Dois Fatores do Desenvolvedor Limpa
- Permissão da conta atualizada

### Configurações da empresa
- Grupo de aplicativos adicionado
- Aplicativo adicionado
- Configurações da empresa alteradas

### Modelo de e-mail
- Modelo de e-mail adicionado
- Modelo de e-mail atualizado

### Credencial de push
- Credencial de push atualizada
- Credencial de push removida

### Depurador SDK
- Iniciou a Sessão do Depurador SDK
- Log do Depurador SDK Exportado
{% enddetails %}

## Visualizando informações pessoalmente identificáveis (PII) {#view-pii}

A permissão **Visualizar PII** é acessível apenas a alguns usuários selecionados do Braze. Por padrão, todos os administradores têm sua permissão **Visualizar PII** ativada nas permissões de usuário. Isso significa que eles podem ver todos os atributos padrão e personalizados que sua empresa definiu como PII em todo o painel. Quando essa permissão é desativada para os usuários, esses usuários não poderão ver nenhum desses atributos.

Para as capacidades de permissão da equipe existente, consulte [Definindo permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Definindo PII

{% alert important %}
Selecionar e definir certos campos como campos PII afeta apenas o que os Usuários podem visualizar no painel do Braze e não impacta como os dados do Usuário Final em tais campos PII são tratados.<br><br>Consulte sua equipe jurídica para alinhar as configurações do seu painel com quaisquer regulamentos e políticas de privacidade aplicáveis à sua empresa, incluindo aqueles relacionados a [retenção de dados]({{site.baseurl}}/data_retention/).
{% endalert %}

Você pode selecionar os campos que sua empresa designa como PII no painel. Para fazer isso, vá para **Configurações da Empresa** > **Configurações do Administrador** > **Configurações de Segurança**.

Os seguintes atributos podem ser designados como PII e ocultados de usuários do Braze que não têm permissões **Visualizar PII**.

| Atributos padrão | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Endereço de e-mail </li> <li> Número de telefone </li> <li> Primeiro nome </li> <li> Sobrenome </li> <li> Gênero </li> <li> Data de nascimento </li> <li> IDs de dispositivos </li> <li> Localização mais recente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos os atributos personalizados<ul><li>Atributos personalizados individuais podem ser marcados como PII se você não precisar ocultar todos os atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Áreas limitadas

O seguinte assume que todos os campos estão definidos como PII, e os usuários mencionados são aqueles que usam a plataforma Braze.

| Navegação do painel | Resultado | Notas |
| -------------------- | ------ | ----- |
| Pesquisa de usuário | O usuário que faz login não consegue pesquisar por endereço de e-mail, número de telefone, primeiro nome ou sobrenome: {::nomarkdown} <ul> <li> Não será exibido os atributos padrão e personalizados anteriores ao visualizar um perfil de usuário. </li> <li> Não é possível editar os atributos padrão anteriores de um perfil de usuário a partir do painel Braze. </li> </ul> {:/} | O acesso a esta seção ainda requer acesso para visualizar o perfil do usuário. |
| Importação de usuário | O usuário não pode baixar arquivos da página **User Import**. | |
| {::nomarkdown} <ul> <li> Segmentos </li> <li> Campanhas </li> <li> Canvas </li> </ul> {:/} | No dropdown **User Data**: {::nomarkdown} <ul> <li> O usuário não terá a opção <b>CSV Export Email Address</b>. </li> <li> O usuário não receberá os atributos padrão e de cliente anteriores no arquivo CSV ao selecionar <b>CSV Export User Data</b>. </li> </ul> {:/} | |
| Grupo de teste interno | O usuário não terá acesso aos atributos padrão anteriores de qualquer usuário adicionado ao grupo de teste interno. | |
| Registro de atividade de mensagem | O usuário não terá acesso aos atributos padrão anteriores para qualquer usuário identificado no registro de atividade de mensagem. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Ao visualizar uma mensagem, a permissão **View PII** não é aplicada, então os usuários podem ver os atributos padrão anteriores se forem referenciados na mensagem através do Liquid.
{% endalert %}

## Preferências de exclusão de dados 

Você pode usar esta configuração para definir preferências sobre se certos campos devem ser excluídos durante o processo de exclusão de usuários para eventos. Essas preferências impactam apenas os dados de usuários que foram excluídos do Braze. 

Quando um usuário é excluído, o Braze remove todas as PII dos dados de eventos, mas retém os dados anonimizados para fins analíticos. Alguns campos definidos pelo usuário podem conter PII se você enviar informações do usuário final para o Braze. Se esses campos contiverem PII, você pode optar por excluir os dados quando os dados de eventos forem anonimizados para usuários excluídos; se os campos não contiverem PII, eles podem ser retidos para análise.

Você é responsável por determinar as preferências corretas para seu espaço de trabalho. A melhor maneira de determinar as configurações apropriadas é revisar com as equipes internas que enviam dados de eventos para o Braze e com as equipes que usam extras de mensagem no Braze para confirmar se os campos podem conter PII.  

### Campos relevantes  

| Nome ou tipo de evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | propriedades |  |
| Evento de compra | propriedades |  |
| Envio de mensagem | message_extras | Vários tipos de evento contêm um campo `message_extras`. A preferência se aplica a todos os tipos de evento de envio de mensagem que suportam `message_extras`, incluindo tipos de evento adicionados no futuro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**Exclusão é permanente!** Se você optar por remover quaisquer campos do Snowflake para usuários excluídos, a configuração se aplicará a todos os dados históricos em seus espaços de trabalho e a quaisquer eventos para usuários excluídos no futuro. Depois que o Braze executar o processo para aplicar as configurações aos dados de eventos históricos para usuários excluídos, os dados **não podem ser restaurados**.
{% endalert %}

### Configurar preferências

Defina preferências padrão marcando caixas para quaisquer campos que devem ser removidos se um usuário for excluído. Selecione quaisquer campos que contenham PII. Essa preferência se aplicará a todos os espaços de trabalho atuais e futuros, a menos que os espaços de trabalho sejam explicitamente adicionados a um grupo de preferência.

Para personalizar preferências por espaço de trabalho, você pode adicionar grupos de preferência com configurações diferentes da padrão. Aplicamos as configurações padrão a quaisquer espaços de trabalho não adicionados a um grupo de preferência adicional, incluindo espaços de trabalho criados no futuro.  

\![Seção de Preferências de Exclusão de Dados com alternância ativada para personalizar preferências de exclusão de dados por espaço de trabalho.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Solução de problemas 

### Problemas de loop na configuração de autenticação de dois fatores (2FA)

Se você se encontrar preso em um loop após inserir com sucesso seu número de telefone para 2FA e for redirecionado de volta para a página de login, isso provavelmente se deve a não ter verificado na primeira tentativa. Para resolver esse problema, siga estas etapas:

1. Desative qualquer bloqueador de anúncios.
2. Ative os cookies nas configurações do seu navegador.
3. Reinicie seu PC ou laptop.
4. Tente configurar o 2FA novamente.

Se o problema persistir após essas etapas, entre em contato com [Suporte]({{site.baseurl}}/braze_support/) para assistência.

### Não é possível ativar a autenticação de dois fatores (2FA)

Se o 2FA estiver ativado, mas nada acontecer quando você selecionar o botão **Ativar**, pode ser devido ao seu navegador bloquear o redirecionamento necessário para enviar o código de verificação por SMS. Aqui estão as etapas para solucionar esse problema:

1. Suspenda temporariamente qualquer bloqueador de anúncios que você tenha ativado no seu navegador.
2. Confirme que você ativou cookies de terceiros nas configurações do seu navegador.
3. Tente configurar o 2FA.

### O código de verificação não é enviado

Se você encontrar problemas ao inserir seu número de telefone na página do Authy e não receber um SMS, siga estas etapas:

1. Instale o aplicativo Authy no seu telefone e faça login no autenticador Authy.
2. Digite seu número de telefone e verifique o aplicativo Authy para quaisquer alterações ou notificações de SMS.
3. Se você ainda não receber o SMS, tente usar uma conexão de rede diferente, como sua rede doméstica ou um Wi-Fi não corporativo. Redes corporativas podem ter políticas de segurança que interferem na entrega de SMS.

Se os problemas persistirem, exclua o perfil antigo no aplicativo Authy e escaneie o código QR novamente para configurar o 2FA. Certifique-se de que você desativou qualquer bloqueador de anúncios, ativou cookies de terceiros ou usou um navegador diferente antes de tentar a configuração novamente.