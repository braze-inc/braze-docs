---
nav_title: Configurações de segurança
article_title: Configurações de segurança
page_order: 2
toc_headers: h2
page_type: reference
description: "Este artigo de referência aborda configurações genéricas de segurança entre empresas, incluindo regras de autenticação, lista de permissões de IP, IPI e autenticação de dois fatores (2FA)."

---

# Configurações de segurança

> Como administrador, a segurança é uma alta prioridade em sua lista de preocupações. A página **Configurações de segurança** pode ajudá-lo a gerenciar as configurações de segurança genéricas e entre empresas, incluindo regras de autenticação, lista de permissões de IP e autenticação de dois fatores.

Para acessar essa página, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança**.

## Regras de autenticação

### Comprimento da senha

Use esse campo para alterar o comprimento mínimo de senha exigido. O mínimo padrão é de oito caracteres.

### Complexidade da senha

Selecione **Aplicar senhas complexas** para exigir que as senhas incluam pelo menos um dos seguintes itens: 
- Letra maiúscula
- Letra minúscula
- Número
- Caractere especial

### Reutilização de senha

Determina o número mínimo de novas senhas que devem ser definidas para que um usuário possa reutilizar uma senha. O padrão é três.

### Regras de expiração da senha

Use esse campo para definir quando deseja que os usuários da sua conta Braze redefinam a senha.

### Regras de duração da sessão

Use esse campo para definir por quanto tempo o Braze manterá sua sessão ativa. Após o Braze considerar sua sessão inativa (sem atividade pelo número definido de minutos), o Braze desconecta o usuário. O número máximo de minutos que você pode inserir é 10.080 (igual a uma semana) se a autenticação de dois fatores for aplicada à sua empresa, caso contrário, a duração máxima da sessão é de 1.440 minutos (igual a 24 horas).

### Autenticação de logon único (SSO)

É possível restringir o registro de seus usuários usando uma senha ou SSO.

Para [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/), os clientes precisam configurar suas configurações SAML antes de aplicar. Se os clientes usarem o SSO do Google, eles só precisarão aplicar a página de configurações de segurança sem nenhuma elevação adicional.

## Lista de permissões de IP do dashboard

Use o campo mostrado para listar endereços IP e sub-redes específicos a partir dos quais os usuários podem registrar a sua conta (por exemplo, a partir de uma rede da empresa ou VPN). Especifique endereços IP e sub-redes como intervalos CIDR em uma lista separada por vírgulas. Se não especificado, os usuários podem fazer login de qualquer endereço IP.

## Autenticação de dois fatores (2FA)

A autenticação de dois fatores é necessária para todos os usuários do Braze. Ele adiciona um segundo nível de verificação de identidade a um registro de conta, tornando-o mais seguro do que apenas um nome de usuário e uma senha. Se o seu dashboard não suportar a autenticação de dois fatores, entre em contato com o gerente de sucesso do cliente. 

Quando a autenticação de dois fatores está ativada:

- Além de inserir uma senha, os usuários precisam inserir um código de verificação ao fazer login em sua conta Braze. O código pode ser enviado através de um aplicativo autenticador, e-mail ou SMS. 
- A caixa de seleção **Lembrar esta conta por 30 dias** fica disponível para os usuários.

O Braze bloqueia usuários que não configuram sua autenticação de dois fatores em sua conta Braze. Os usuários da conta Braze também podem configurar a autenticação de dois fatores por conta própria nas **Configurações da conta**, mesmo que não seja exigido pelo administrador.

Não se esqueça de salvar suas alterações antes de sair da página!

### Lembrar esta conta por 30 dias {#remember-me}

Este recurso está disponível quando a autenticação de dois fatores está ativada.

Quando você seleciona **Lembrar esta conta por 30 dias**, um cookie é armazenado em seu dispositivo, exigindo apenas que você faça login com autenticação de dois fatores uma vez ao longo de 30 dias. 

![Caixa de seleção Lembrar esta conta por 30 dias]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Os clientes com várias contas em uma empresa dashboard podem ter problemas ao usar esse recurso devido ao fato de o cookie estar vinculado a um dispositivo específico. Se os usuários usarem o mesmo dispositivo para registrar várias contas, o cookie será substituído para as contas autorizadas anteriormente nesse dispositivo. O Braze espera que apenas um dispositivo seja associado a uma conta, e não um dispositivo para várias contas.

### Redefinição da autenticação do usuário

Se você estiver tendo problemas para fazer login com autenticação de dois fatores, entre em contato com os administradores da sua empresa para redefinir sua autenticação de dois fatores. Os administradores podem realizar os seguintes passos:

1. Acessar **Configurações** > **Usuários da Empresa**.
2. Selecione o usuário na lista fornecida.
3. Selecione **Reset (Redefinir** ) em **Two Factor Authentication (Autenticação de dois fatores**).

Uma redefinição pode resolver problemas comuns de autenticação, como problemas com apps de autenticação, envio de e-mail não enviado, falha de login devido a interrupções de SMS ou erro do usuário e muito mais.

### Requisitos para 2FA no nível da empresa

Primeiro, verifique se o 2FA está habilitado para seu dashboard indo em **Configurações da Empresa** > **Configurações de Segurança** > **Autenticação de Dois Fatores**. Se o botão estiver cinza, o 2FA não foi ativado para sua empresa e não é obrigatório para todos os usuários do dashboard.

#### Opções do usuário quando o 2FA não é obrigatório

Se o 2FA não for aplicado a nível de empresa, os usuários individuais podem configurar o 2FA para si mesmos na página de Configurações da Conta. Nesse caso, os usuários não serão bloqueados de suas contas se não o configurarem. Você pode identificar quais usuários optaram por ativar o 2FA verificando a página Gerenciar Usuários.

#### Requisitos quando o 2FA é obrigatório

Se o 2FA for aplicado a nível de empresa, os usuários que não o configurarem em suas próprias contas ao fazer login serão bloqueados do dashboard. Os usuários devem completar a configuração do 2FA para manter o acesso.

{% alert important %}
O 2FA é obrigatório para todos os usuários do Braze apenas se o Logon Único (SSO) não estiver ativado. Se o SSO estiver em uso, o 2FA não precisa ser aplicado a nível de empresa.
{% endalert %}

## Configurando a autenticação de dois fatores (2FA)

### Configurando o 2FA com Authy

1. Baixe o aplicativo Authy da loja de aplicativos do seu dispositivo.
2. No Braze, insira seu número de telefone.
3. Toque na notificação enviada para o seu dispositivo que solicita que você abra o aplicativo Authy.
4. Inicie o aplicativo Authy no seu dispositivo para recuperar o código.
5. No Braze, insira o código de verificação que você recebeu do Authy.

Se você encontrar problemas durante o processo de configuração e for redirecionado para a página inicial do Braze ou tela de login, tente o seguinte:

- Use o modo de navegação anônima ou privada: Tente configurar novamente com uma janela de navegação anônima ou privada. Isso pode contornar problemas causados por extensões ou plugins do navegador.
- Tente um perfil de navegador diferente: Se o problema persistir, considere usar um perfil de navegador diferente para eliminar conflitos com plugins instalados.

### Configurando 2FA quando não é obrigatório

Para ativar manualmente a autenticação de dois fatores (2FA) na sua conta Braze quando não é obrigatório, siga estas etapas:

1. Baixe um aplicativo de 2FA como Authy, Google Authenticator, Okta Verify ou similar da App Store (iOS), Google Play Store (Android) ou da web. Ou, se preferir configurar 2FA com e-mail ou SMS, pule para a etapa 2.
2. No Braze, acesse Gerenciar Conta, role até a seção **Autenticação de Dois Fatores**, e selecione **Iniciar Configuração**.
3. Digite sua senha no modal de login e selecione **Verificar Senha**.
4. No modal de **Configuração de Autenticação de Dois Fatores**, insira seu número de telefone e selecione **Ativar**.
5. Copie o código gerado de sete dígitos do seu aplicativo de 2FA, e-mail ou mensagem SMS, e volte para o Braze e cole no modal de **Configuração de Autenticação de Dois Fatores**. Selecione **Verificar**.
6. (Opcional) Para evitar inserir 2FA pelos próximos 30 dias, ative a opção **Lembrar desta conta por 30 dias**.

## Elevated Access

O Elevated Access adiciona uma camada extra de segurança para ações confidenciais em seu dashboard do Braze. Quando ativo, os usuários precisam verificar novamente sua conta antes de exportar um segmento ou visualizar uma chave de API. Para usar o Acesso elevado, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança** e ative-o. 

Se um usuário não puder verificar novamente, ele será redirecionado para o ponto em que parou e não poderá continuar com a ação sensível. Depois de se verificarem novamente com sucesso, não precisarão fazer isso novamente na próxima hora, a menos que se desconectem primeiro.

![Alternância de acesso elevado.]({% image_buster /assets/img/elevated_access.png %})

## Baixando um relatório de eventos de segurança {#security-event-report}

O relatório de eventos de segurança é um relatório CSV de eventos de segurança, como convites para contas, remoções de contas, tentativas de login bem-sucedidas e com falha e outras atividades. Você pode usá-lo para realizar auditorias internas.

Para baixar esse relatório, faça o seguinte:

1. Acesse **Configurações** > **Configurações administrativas**.
2. Selecione a guia **Security Settings (Configurações de segurança** ) e acesse a seção **Security Event Download (Baixar eventos de segurança** ).
3. Selecione **Baixar relatório**. 

Este download de relatório manual contém apenas os 10.000 eventos de segurança mais recentes para sua conta.

Para exportar eventos de segurança para a Amazon S3 sem esse limite de linha, veja [Exportação de eventos de segurança com Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/).

{% details Reported security events %}
### Login e conta
- Fazendo login
- Falha no login
- Configuração da autenticação de dois fatores concluída
- Reinicialização da autenticação de dois fatores concluída
- Desenvolvedor liberado 2FA
- Desenvolvedor adicional adicionado
- Conta Adicionada
- Desenvolvedor Suspenso
- Desenvolvedor não suspenso
- Desenvolvedor Atualizado
- Desenvolvedor Removido
- Conta Removida
- Status de Inscrição do Usuário Atualizado
- Usuário Atualizado
- Conta de Desenvolvedor Atualizada

### Acesso elevado
- Fluxo de acesso elevado iniciado
- Fluxo de acesso elevado concluído
- Falha na verificação 2FA para acesso elevado
- Acesso Elevado Habilitado
- Acesso Elevado Desabilitado

Campanha interrompida
- Campanha Adicionada
- Campanha Editada

Canva
- Jornada adicionada
- Jornada editada

### Segmento
- Segmento Adicionado
- Segmento Editado
- Dados exportados para CSV
- Segmento exportado via API
- Usuários do Segmento Excluídos
- Coorte Limpa

### Chave da API REST
- Adicionada a chave da API REST
- Remoção da chave da API REST

### Credencial de autenticação básica
- Adição da credencial de autenticação básica
- Credencial de autenticação básica atualizada
- Remoção da credencial de autenticação básica

### Permissão
- Desenvolvedor liberado 2FA
- Permissão de conta atualizada
- Equipe Adicionada
- Equipe Editada
- Equipe Arquivada
- Equipe Desarquivada
- Conjunto de Permissões do Grupo de App Criado
- Conjunto de Permissões do Grupo de App Editado
- Conjunto de Permissões do Grupo de App Removido
- Função Personalizada Criada
- Função Personalizada Atualizada
- Função Personalizada Excluída

### Configurações da empresa
- Grupo de app adicionado
- Aplicativo adicionado
- Configurações da Empresa Alteradas
- Configurações de Segurança da Empresa Atualizadas
- Exportação de Evento de Segurança na Nuvem Atualizada
- Domínio Personalizado de Páginas de Destino Adicionado
- Domínio Personalizado de Páginas de Destino Removido
- Domínio Personalizado Criado
- Domínio Personalizado Excluído
- Grupo de Controle Global Habilitado
- Grupo de Controle Global Desabilitado
- Exclusões de Controle Global Atualizadas
- Lista de Permissão de SMS do Grupo de Inscrições Atualizada

### Modelo de e-mail
- Modelo de e-mail adicionado
- Modelo de e-mail atualizado

### Credencial push
Credencial push atualizada
Credencial push removida

### Depurador do SDK
- Iniciou a sessão do depurador do SDK
- Registro do depurador SDK exportado

### Usuários
- Usuários Excluídos
- Usuários Visualizados
- Importação de Usuário Iniciada
- Status do Grupo de Inscrição do Usuário Atualizado
- Usuário excluído
- Exclusão de Usuário Único Cancelada
- Exclusão em Massa de Usuários Cancelada

### Catálogos
- Catálogo Criado
- Catálogo Excluído

### Agentes da Braze
- Agente Criado
- Agente Editado

### Operador BrazeAI 
- Resposta do Operador BrazeAI Solicitada
- Operador BrazeAI Respondeu
{% enddetails %}

## Visualização de informações de identificação pessoal (IPI) {#view-pii}

A permissão **View IPI** só pode ser acessada por alguns usuários selecionados do Braze. Por padrão, todos os administradores têm sua permissão **Ver PII** ativada nas permissões de usuário. Isso significa que eles podem ver todos os atributos padrão e personalizados que sua empresa definiu como PII em todo o painel. Quando essa permissão é desativada para os usuários, esses usuários não poderão ver nenhum desses atributos.

{% alert note %}
Você precisa da permissão **Ver PII** para usar [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), porque isso permite acesso direto a alguns dados de clientes.
{% endalert %}

Para conhecer os recursos de permissão de equipe existentes, consulte [Definição de permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Definição de IPI

{% alert important %}
Selecionar e definir certos campos como campos PII afeta apenas o que os Usuários podem ver no painel da Braze e não impacta como os dados do Usuário Final em tais campos PII são tratados.<br><br>Consulte sua equipe jurídica para alinhar as configurações do seu painel com quaisquer regulamentos e políticas de privacidade aplicáveis à sua empresa, incluindo aqueles relacionados à [retenção de dados]({{site.baseurl}}/data_retention/).
{% endalert %}

Você pode selecionar os campos que sua empresa designa como PII no painel. Para fazer isso, acesse **Configurações da Empresa** > **Configurações do Administrador** > **Configurações de Segurança**.

Os seguintes atributos podem ser designados como PII e ocultados de usuários da Braze que não têm permissões **Ver PII**.

#### Atributos PII potenciais

| Atributos padrão | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Endereço de e-mail </li> <li> Número de telefone </li> <li> Nome </li> <li> Sobrenome </li> <li> Gênero </li> <li> Data de nascimento </li> <li> IDs de dispositivo </li> <li> Local mais recente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos os atributos personalizados<ul><li>Atributos personalizados individuais podem ser marcados como IPI se você não precisar ocultar todos os atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Áreas limitadas

O seguinte assume que todos os campos estão definidos como PII, e os usuários mencionados são aqueles que usam a plataforma Braze. Além disso, atributos "precedentes" referem-se àqueles na tabela [Atributos PII potenciais](#potential-pii-attributes). Remover permissões PII de um usuário pode impactar a usabilidade além dessas áreas listadas.

| Navegação no dashboard | Resultado | Notas |
| -------------------- | ------ | ----- |
| Pesquisa de usuários | O usuário que faz o registro não consegue pesquisar por endereço de e-mail, número de telefone, nome ou sobrenome: {::nomarkdown} <ul> <li> Não serão mostrados os atributos padrão e personalizados anteriores ao visualizar um perfil de usuário. </li> <li> Não é possível editar as atribuições padrão anteriores de um perfil de usuário no dashboard do Braze. </li> <li> Não é possível atualizar o status de inscrição em um perfil de usuário. </li></ul> {:/} | O acesso a esta seção ainda requer acesso para visualizar um perfil de usuário. |
| importação de usuário | O usuário não pode baixar arquivos da página **Importação de usuário**. | |
| {::nomarkdown} <ul> <li> Segmentos </li> <li> Campanhas </li> <li> Canva </li> </ul> {:/} | No menu suspenso **Dados de usuários**: {::nomarkdown} <ul> <li> O usuário não terá a opção <b>Exportar endereço de e-mail CSV</b>. </li> <li> O usuário não receberá os atributos padrão e personalizados precedentes no arquivo CSV ao selecionar <b>Exportar Dados de Usuário CSV</b>. </li> </ul> {:/} | |
| Grupo de teste interno | O usuário não terá acesso às atribuições padrão anteriores de nenhum usuário adicionado ao grupo de teste interno. | |
| Registro de atividades de mensagens | O usuário não terá acesso às atribuições padrão anteriores para nenhum usuário identificado no registro de atividades de mensagens. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Ao visualizar uma mensagem, a permissão **Ver PII** não é aplicada, então os usuários podem ver os [atributos padrão anteriores](#potential-pii-attributes) se forem referenciados na mensagem através do Liquid.
{% endalert %}

## Preferências de exclusão de dados 

Você pode usar esta configuração para definir preferências sobre se o Braze deve excluir certos campos durante o processo de exclusão de usuários para eventos. Essas preferências impactam apenas os dados de usuários que o Braze excluiu. 

Quando um usuário é excluído, o Braze remove todos os PII dos dados de eventos, mas retém os dados anonimizados para fins de análise. Alguns campos definidos pelo usuário podem conter IPI se você enviar informações do usuário final para a Braze. Se esses campos contiverem PII, você pode optar por excluir os dados quando o Braze anonimiza os dados de eventos para usuários excluídos; se os campos não contiverem PII, você pode mantê-los para análise.

Você é responsável por determinar as preferências corretas para seu espaço de trabalho. A melhor maneira de determinar as configurações apropriadas é revisar com as equipes internas que enviam dados de eventos para o Braze e com as equipes que usam extras de mensagens no Braze para confirmar se os campos podem conter IPI.  

### Campos relevantes  

| Nome ou tipo do evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | propriedades |  |
| Evento de compra | propriedades |  |
| Envio de mensagens | message_extras | Vários tipos de eventos contêm um campo `message_extras`. A preferência se aplica a todos os tipos de eventos de envio de mensagens que suportam `message_extras`, incluindo tipos de eventos adicionados no futuro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**A exclusão é permanente!** Se você optar por remover quaisquer campos do Snowflake para usuários excluídos, a configuração se aplica a todos os dados históricos em seus espaços de trabalho e a quaisquer eventos para usuários excluídos no futuro. Depois que o Braze executou o processo para aplicar as configurações aos dados de eventos históricos para usuários excluídos, você **não pode restaurar** os dados.
{% endalert %}

### Configurar preferências

Defina preferências padrão marcando caixas para quaisquer campos que o Braze deve remover se um usuário for excluído. Selecione qualquer um dos campos que contenham IPI. Essa preferência se aplica a todos os espaços de trabalho atuais e futuros, a menos que os espaços de trabalho sejam explicitamente adicionados a um grupo de preferências.

Para personalizar preferências por espaço de trabalho, você pode adicionar grupos de preferências com configurações diferentes das padrão. Aplicamos as configurações padrão a todos os espaços de trabalho não adicionados a um grupo de preferências adicional, incluindo espaços de trabalho criados no futuro.  

![Seção de Preferências de Exclusão de Dados com o botão ativado para personalizar preferências de exclusão de dados por espaço de trabalho.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Solução de problemas 

### Problemas de loop na configuração de autenticação de dois fatores (2FA)

Se você se encontrar preso em um loop após inserir com sucesso seu número de telefone para 2FA e for redirecionado de volta para a página de login, isso provavelmente se deve a não ter verificado na primeira tentativa. Para resolver esse problema, siga estas etapas:

1. Desative qualquer bloqueador de anúncios.
2. Ative os cookies nas configurações do seu navegador.
3. Reinicie seu PC ou laptop.
4. Tente configurar o 2FA novamente.

Se o problema persistir após essas etapas, entre em contato com [Suporte]({{site.baseurl}}/braze_support/) para assistência.

### Não é possível ativar a autenticação de dois fatores (2FA)

Se a 2FA estiver ativada, mas nada acontecer ao selecionar o botão **Ativar**, pode ser devido ao seu navegador bloquear o redirecionamento necessário para enviar o código de verificação por SMS. Aqui estão as etapas para solucionar esse problema:

1. Suspenda temporariamente qualquer bloqueador de anúncios que você tenha ativado em seu navegador.
2. Confirme que você ativou cookies de terceiros nas configurações do seu navegador.
3. Tente configurar a 2FA.

### Código de verificação não enviado

Se você encontrar problemas ao inserir seu número de telefone na página do Authy e não receber um SMS, siga estas etapas:

1. Instale o app Authy no seu telefone e faça login no autenticador Authy.
2. Digite seu número de telefone e verifique o app Authy para quaisquer alterações ou notificações de SMS.
3. Se você ainda não receber o SMS, tente usar uma conexão de rede diferente, como sua rede doméstica ou um Wi-Fi não corporativo. Redes corporativas podem ter políticas de segurança que interferem na entrega de SMS.

Se os problemas persistirem, exclua o perfil antigo no app Authy e escaneie o código QR novamente para configurar a 2FA. Certifique-se de que você desativou qualquer bloqueador de anúncios, ativou cookies de terceiros ou usou um navegador diferente antes de tentar a configuração novamente.