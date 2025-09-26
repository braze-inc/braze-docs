---
nav_title: Extole
article_title: Extole
description: "Este artigo descreve a parceria entre o Braze e a Extole, uma empresa de marketing de referência, que permite que você transfira eventos e atributos personalizados de clientes dos programas de indicação de amigos e de crescimento para o Braze."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [A Extole](https://www.extole.com/), uma empresa de SaaS, é líder do setor em marketing de indicação de amigos, ajudando a criar e otimizar programas eficazes de marketing de indicação para aumentar a aquisição de clientes.

_Essa integração é mantida pela Extole._

## Sobre a integração

Com a integração entre o Braze e a Extole, você pode puxar eventos e atributos personalizados de clientes dos programas de indicação de amigos e de crescimento da Extole para o Braze, o que lhe permite criar campanhas de marketing mais personalizadas que aumentam a aquisição, o engajamento e a fidelidade dos clientes. Também é possível extrair dinamicamente atribuições de conteúdo da Extole, como códigos de compartilhamento e links personalizados, para as comunicações da Braze.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Extole | É necessário ter uma conta da Extole para usar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com a permissão `users.track`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| URL da API do Braze | Seu URL da API do Braze é específico para sua [instância do Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Os casos de uso a seguir mostram algumas maneiras de aproveitar a integração do Extole com o Braze. Trabalhe com seus gerentes de implementação e de sucesso do cliente da Extole para desenvolver uma opção que atenda às necessidades específicas de sua empresa.

- Aproveite os eventos personalizados de seus programas de indicação e engajamento para disparar uma campanha Braze ou Canvas
- Crie segmentos, dashboards e relatórios personalizados usando os dados de seus programas com tecnologia Extole
- Cancelar automaticamente a inscrição ou inscrever usuários em sua lista de marketing no Braze

## Integração

Conclua as etapas a seguir para sua integração entrar em funcionamento. Seus gerentes de implementação e de sucesso do cliente da Extole o apoiarão durante todo o processo e responderão a quaisquer perguntas que você possa ter.

### Conecte-se à sua conta da Braze

1. Selecione a integração com [parceiros](https://my.extole.com/partners) na página Parceiros de sua conta My Extole.
2. Na integração da Braze, selecione **Install** (Instalar) para iniciar a conexão entre a Extole e a Braze.
3. Preencha os campos obrigatórios, começando com sua chave da API REST da Braze. 
4. Digite seu URL da API do Braze. Esse URL depende da instância em que sua conta Braze está provisionada.
5. Adicione todos os eventos do Extole que você gostaria de enviar para o Braze. Os eventos padrão, as propriedades do evento e os atributos de usuário são descritos na [tabela de eventos da Extole](https://dev.extole.com/docs/braze#extole-program-events).
6. Adicione quaisquer estados de recompensas que você gostaria de enviar à Braze, além do estado `FULFILLED`. Consulte a [tabela de recompensas da Extole](https://dev.extole.com/docs/braze#extole-rewards) para obter descrições dos estados de recompensas disponíveis.
7. Selecione o mapeamento de sua chave de ID externa Braze. É assim que a Extole atualiza os perfis de usuário no Braze. É possível mapear a chave de ID externa da Braze para `email_address` ou `partner_user_id` da Extole para o usuário. Recomendamos usar `external_id` em vez de `email_address`, pois é mais seguro.
8. Salve suas configurações para concluir a conexão. Agora, os eventos do Extole podem fluir para sua conta do Braze.

### Eventos do programa Extole

Abaixo estão os eventos padrão, as propriedades do evento e as atribuições do usuário que a Extole enviará à Braze. Entre em contato com os gerentes de implementação ou de sucesso do cliente do Extole para identificar e adicionar outros eventos do Extole à sua integração.

| Evento | Descrição | Propriedades do evento | Atributos do usuário |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Um participante cria seu link de compartilhamento inserindo seu e-mail no Extole Share Experience. | Nome do evento  <br>Hora do evento  <br>Parceiro (Extole)  <br>Funil (defensor ou amigo)  <br>Programa | <br>ID externo <br>E-mail  <br>Compartilhar link |
| `extole_shared` | Um participante compartilha seu link de indicação com um amigo. | Nome do evento  <br>Hora do evento  <br>Parceiro (Extole)  <br>ID externo  <br>Funil (defensor ou amigo)  <br>Programa  <br>Canal de compartilhamento | E-mail <br>Nome <br>Sobrenome |
| `outcome` - O resultado é dinâmico com base na configuração de seu programa (como `extole_shipped`, `extole_converted`)| Um participante converteu ou concluiu o evento de resultado desejado configurado para o programa. | Dinâmica por programa | E-mail <br>Nome <br>Sobrenome |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Estados de inscrição da Extole

| Estado da inscrição | Descrição | Propriedades do evento | Atributos do usuário |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Um participante fez a aceitação para receber mensagens de marketing. | N/D | E-mail  <br>Tipo de lista  <br>ID externo  <br>Inscrição de e-mail (aceitação) |
| `unsubscribed` | Um participante cancelou o recebimento das comunicações por e-mail da Extole.| E-mail  <br>ID externo  <br>Estado da inscrição (inscrição cancelada)  <br>ID do grupo de inscrições  | Tipo de lista |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Recompensas da Extole

Por padrão, o Extole enviará eventos de recompensas no estado `FULFILLED` para o Braze para que você possa disparar notificações de recompensas por meio de uma campanha do Braze ou do Canva. Consulte a tabela a seguir para ver mais estados de recompensas.

| Estado da recompensa | Descrição | Propriedades do evento | Atributos do usuário |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | O estado padrão. Foi atribuído um valor (como cupom ou cartão-presente) à recompensa por um fornecedor de recompensas da Extole. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `EARNED` | Uma recompensa foi criada e associada a uma pessoa. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `SENT` | A recompensa foi processada e enviada por e-mail ou em um dispositivo para o destinatário. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `REDEEMED` | A recompensa foi usada pelo destinatário, conforme evidenciado em um evento de conversão ou resgate enviado à Extole.| E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `FAILED` | Um problema impediu que a recompensa fosse emitida ou enviada, exigindo atenção. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `CANCELED` | A recompensa foi desativada e retornará ao inventário. | E-mail <br>Valor nominal  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `REVOKED` | A recompensa cumprida foi invalidada. Por exemplo, a Extole solicitou um cartão-presente de um fornecedor e depois determinou que o cartão foi enviado por engano. Se o fornecedor oferecer recursos de revogação da recompensa, a Extole solicitará a devolução dos fundos, e a recompensa não será mais válida. | E-mail <br>Valor nominal   <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Personalização

### Localizar e criar usuários no Braze

Para determinados casos de uso, como uma nova inscrição de e-mail ou SMS em que a Extole não tem uma ID externa (ID de usuário), a Extole pode verificar o identificador do usuário usando o endpoint [Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) da Braze. O Extole adicionará e atualizará quaisquer atribuições de perfil se o usuário existir no Braze. Se a solicitação não retornar um perfil de usuário, o Extole usará o ponto de extremidade `/users/track` para criar um alias de usuário com o endereço de e-mail do usuário como o nome do alias.

## Usando esta integração

Depois de conectar suas contas, os eventos começarão a fluir automaticamente do Extole para o Braze sem nenhuma ação de sua parte. Uma visualização em tempo real dos eventos enviados à Braze pode ser encontrada na central de webhooks de saída da Extole para solução de problemas. 

