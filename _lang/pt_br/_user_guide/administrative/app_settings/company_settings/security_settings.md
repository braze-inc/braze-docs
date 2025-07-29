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

### Reutilização de senhas

Determina o número mínimo de novas senhas que devem ser definidas para que um usuário possa reutilizar uma senha. O padrão é três.

### Regras de expiração da senha

Use esse campo para definir quando deseja que os usuários da sua conta Braze redefinam a senha.

### Regras de duração da sessão

Use esse campo para definir por quanto tempo o Braze manterá sua sessão ativa. Depois que a Braze considerar sua sessão inativa (nenhuma atividade durante o número definido de minutos), o usuário será registrado. 

### Autenticação de logon único (SSO)

É possível restringir o registro de seus usuários usando uma senha ou SSO.

 Se os clientes usarem o SSO do Google, eles só precisarão aplicar a página de configurações de segurança sem nenhuma elevação adicional.

## Lista de permissões de IP do dashboard

Use o campo mostrado para listar endereços IP e sub-redes específicos a partir dos quais os usuários podem registrar a sua conta (por exemplo, a partir de uma rede da empresa ou VPN). Especifique endereços IP e sub-redes como intervalos CIDR em uma lista separada por vírgulas. Se isso não for especificado, os usuários poderão fazer login de qualquer endereço IP.

## autenticação de dois fatores

A autenticação de dois fatores é necessária para todos os usuários do Braze. Ele adiciona um segundo nível de verificação de identidade a um registro de conta, tornando-o mais seguro do que apenas um nome de usuário e uma senha. Se o seu dashboard não suportar a autenticação de dois fatores, entre em contato com o gerente de sucesso do cliente. 



-   
- 

Os usuários que não configurarem a autenticação de dois fatores serão bloqueados em sua conta Braze. Os usuários da conta Braze também podem configurar a autenticação de dois fatores por conta própria nas **Configurações da conta**, mesmo que não seja exigido pelo administrador.

Não se esqueça de salvar suas alterações antes de sair da página!

### 



 



Os clientes com várias contas em uma empresa dashboard podem ter problemas ao usar esse recurso devido ao fato de o cookie estar vinculado a um dispositivo específico. Se os usuários usarem o mesmo dispositivo para registrar várias contas, o cookie será substituído para as contas autorizadas anteriormente nesse dispositivo. O Braze espera que apenas um dispositivo seja associado a uma conta, e não um dispositivo para várias contas.

### Redefinição da autenticação do usuário

 

1. Acessar **Configurações** > **Usuários da Empresa**.
2. Selecione o usuário na lista fornecida.
3. Selecione **Reset (Redefinir** ) em **Two Factor Authentication (Autenticação de dois fatores**).

Uma redefinição pode resolver problemas comuns de autenticação, como problemas com apps de autenticação, envio de e-mail não enviado, falha de login devido a interrupções de SMS ou erro do usuário e muito mais.

## Elevated Access

O Elevated Access adiciona uma camada extra de segurança para ações confidenciais em seu dashboard do Braze. Quando ativo, os usuários precisam verificar novamente sua conta antes de exportar um segmento ou visualizar uma chave de API. Para usar o Acesso elevado, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança** e ative-o. 

Se um usuário não puder verificar novamente, ele será redirecionado para o ponto em que parou e não poderá continuar com a ação sensível. Depois de se verificarem novamente com sucesso, não precisarão fazer isso novamente na próxima hora, a menos que se desconectem primeiro.



## Baixando um relatório de evento de segurança

O relatório de eventos de segurança é um relatório CSV de eventos de segurança, como convites para contas, remoções de contas, tentativas de login bem-sucedidas e com falha e outras atividades. Você pode usá-lo para realizar auditorias internas.

Para baixar esse relatório, faça o seguinte:

1. Acesse **Configurações** > **Configurações administrativas**.
2. Selecione a guia **Security Settings (Configurações de segurança** ) e acesse a seção **Security Event Download (Baixar eventos de segurança** ).
2. Selecione **Baixar relatório**. 

Esse relatório contém apenas os 10.000 eventos de segurança mais recentes de sua conta. Se precisar de dados de eventos específicos, entre em contato com o suporte técnico.

{% details Eventos de segurança relatados %}

### Login e conta 
- Fazendo login
- Falha no login
- Configuração da autenticação de dois fatores concluída
- Reinicialização da autenticação de dois fatores concluída
- Desenvolvedor liberado 2FA
- Desenvolvedor adicional adicionado
- Desenvolvedor suspenso
- Desenvolvedor não suspenso
- 
- Desenvolvedor removido
- 
- 

### Acesso elevado
- Fluxo de acesso elevado iniciado
- Fluxo de acesso elevado concluído
- Falha na verificação 2FA para acesso elevado

### Campanha interrompida
- Campanha adicionada
- Campanha editada

### Canva
- Jornada adicionada
- Jornada editada

### Segmento
- Segmento adicionado
- Segmento editado
- Dados exportados para CSV
- Segmento exportado via API

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

### Configurações da empresa
- Grupo de app adicionado
- Aplicativo adicionado
- 

### Modelo de e-mail
- Modelo de e-mail adicionado
- Modelo de e-mail atualizado

### Credencial push
- Credencial push atualizada
- Credencial push removida

### Depurador do SDK
- Iniciou a sessão do depurador do SDK
- Registro do depurador SDK exportado
{% enddetails %}

## Visualização de informações de identificação pessoal (IPI) {#view-pii}

A permissão **View IPI** só pode ser acessada por alguns usuários selecionados do Braze.  Isso significa que eles podem ver os seguintes atributos padrão e personalizados em todo o dashboard. Quando essa permissão é desativada para os usuários, esses usuários não poderão ver essas informações.



### Definição de IPI

Você pode definir quais campos são designados como IPI no dashboard. Para fazer isso, acesse **Configurações da empresa** > **Configurações de segurança**.

Os campos a seguir podem ser ocultados dos usuários do Braze que não têm permissões para **Visualizar IPI**.

| Atribuições padrão | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Endereço de e-mail </li> <li> Número de telefone </li> <li> Nome </li> <li> Sobrenome </li> <li> Gênero </li> <li> Data de nascimento </li> <li> IDs de dispositivo </li> <li> Local mais recente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos os atributos personalizados<ul><li>Atributos personalizados individuais podem ser marcados como IPI se você não precisar ocultar todos os atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Áreas limitadas



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

Você pode usar essa configuração para definir preferências sobre se determinados campos devem ser excluídos durante o processo de exclusão de usuários para eventos.  

 Alguns campos definidos pelo usuário podem conter IPI se você enviar informações do usuário final para a Braze. Se esses campos contiverem IPI, você poderá aceitar a exclusão dos dados quando os dados do evento forem anonimizados para usuários excluídos; se os campos não contiverem IPI, eles poderão ser retidos para análise de dados.

Você é responsável por determinar as preferências corretas para seu espaço de trabalho. A melhor maneira de determinar as configurações apropriadas é revisar com as equipes internas que enviam dados de eventos para o Braze e com as equipes que usam extras de mensagens no Braze para confirmar se os campos podem conter IPI.  

### Campos relevantes  

| Nome ou tipo do evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | propriedades |  |
| Evento de compra | propriedades |  |
| Envio de mensagens | message_extras |   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**A exclusão é permanente!** Se houver aceitação de remover quaisquer campos do Snowflake para usuários excluídos, a configuração será aplicada a todos os dados históricos em seus espaços de trabalho e a quaisquer eventos para usuários excluídos no futuro. Depois que o Braze tiver executado o processo para aplicar as configurações aos dados de eventos históricos para usuários excluídos, os dados **não poderão ser restaurados**.
{% endalert %}

### Configurar preferências

Defina as preferências padrão marcando as caixas dos campos que devem ser removidos se um usuário for excluído. Selecione qualquer um dos campos que contenham IPI. Essa preferência será aplicada a todos os espaços de trabalho atuais e futuros, a menos que os espaços de trabalho sejam explicitamente adicionados a um grupo de preferências.

 Aplicamos as configurações padrão a todos os espaços de trabalho não adicionados a um grupo de preferências adicional, incluindo espaços de trabalho criados no futuro.  

![Seção Preferências de exclusão de dados com alternância ativada para personalizar as preferências de exclusão de dados por espaço de trabalho.]({% image_buster /assets/img/deletion_preferences_1.png %})


