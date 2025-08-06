---
nav_title: Facebook
article_title: Sincronização de canva público com o Facebook
description: "Este artigo de referência abordará como usar a Sincronização de Público do Braze com o Facebook para entregar anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 2
alias: /audience_sync_facebook/

Tool:
  - Canvas

---

# Sincronização de público com o Facebook

> Usando a Sincronização de Público do Braze com o Facebook, você pode optar por adicionar os dados dos seus próprios usuários da sua integração Braze aos públicos personalizados do Facebook para entregar anúncios com base em gatilhos comportamentais, segmentação e mais.

Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS ou webhook) em um Canvas do Braze com base nos dados dos seus usuários pode agora ser usado para disparar um anúncio para esse usuário no Facebook usando públicos personalizados. Por exemplo, quando você configura uma Sincronização de Público com o Facebook, você poderá usar uma ampla variedade de campos de primeira parte, como e-mail, telefone, nome e sobrenome.

**Casos de uso comuns para sincronizar públicos personalizados incluem**:

- Direcionar usuários de alto valor com múltiplos canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.
- Criar públicos semelhantes para adquirir novos usuários de forma mais eficiente.

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Facebook. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Considerações sobre sincronização de usuários e limite de frequência
 
À medida que os usuários alcançam a etapa de Sincronização de Público, o Braze sincronizará esses usuários em quase tempo real, respeitando também os limites de taxa da API de Marketing do Facebook. O que isso significa na prática é que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviar esses usuários para o Facebook. 

O limite de taxa da API de Marketing do Facebook afirma que não mais que ~190.000 solicitações de API para cada conta de anúncio em um período de uma hora. Se um cliente do Braze atingir esse limite de frequência, o Braze the Canvas tentará novamente a sincronização por até 13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored (Usuários com erro).

## Pré-requisitos

Você precisará confirmar que tem os seguintes itens criados e concluídos antes de configurar sua etapa de Público do Facebook no Canvas. 

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps). |
| Conta de Anúncio do Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Uma conta de anúncio ativa do Facebook vinculada ao gerente de negócios da sua marca.<br><br>Certifique-se de que o administrador do seu Gerenciador de Negócios do Facebook lhe concedeu permissões de "Gerenciar Campanhas" ou "Gerenciar contas de anúncios" para as contas de anúncios do Facebook que você planeja usar com o Braze. Além disso, verifique se você aceitou os termos e condições de sua conta de anúncios. |
| Termos de públicos personalizados do Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Aceite os Termos de Públicos Personalizados do Facebook para suas contas de anúncios do Facebook que você planeja usar com o Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: conecte-se ao Facebook

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**. Em Facebook Audience Export, selecione **Connect Facebook**.

![Página de tecnologia do Facebook no Braze que inclui uma seção de Visão Geral e uma seção de Exportação de Público do Facebook com o botão Conectar Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Uma janela de diálogo oAuth do Facebook aparecerá para autorizar a Braze a criar Públicos Personalizados em suas contas de anúncios do Facebook.

![A primeira caixa de diálogo do facebook solicitando para "Conectar como X", onde X é seu nome de usuário do Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios para suas contas de anúncios.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Após vincular o Braze à sua conta do Facebook, selecione as contas de anúncios que você gostaria de sincronizar dentro do seu espaço de trabalho do Braze. Quando você estiver conectado, será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Sua conexão com o Facebook é aplicada no nível do espaço de trabalho do Braze. Se o administrador do Facebook remover você do seu Facebook Business Manager ou o acesso às contas do Facebook conectadas, a Braze detectará um token inválido. Como resultado, seus canvas ativos usando componentes do público do Facebook mostrarão erros, e o Braze não poderá sincronizar usuários. 

{% alert important %}
Para clientes que já passaram pelo processo de Revisão de App do Facebook para [Gerenciamento de Anúncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Acesso Padrão de Gerenciamento de Anúncios](https://developers.facebook.com/docs/marketing-api/access#standard), seu Token de Usuário do Sistema ainda será válido para o componente público do Facebook. Você não poderá editar ou revogar o Token de Usuário do Sistema do Facebook através da página de parceiro do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir seu Token de Usuário do Sistema do Facebook dentro do seu espaço de trabalho do Braze. 

<br><br>A configuração do oAuth do Facebook também se aplicará a [exportações do Facebook usando Segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Etapa 2: Aceitar os termos de serviço de públicos personalizados

Antes de construir seu Canvas, você deve aceitar os seguintes termos de serviço do Facebook nos seguintes links:

- **Termos de Públicos Personalizados da Lista de Clientes para sua conta pessoal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Termos das Ferramentas de Negócios do Facebook para sua conta comercial:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Um exemplo dos termos a serem aceitos para listas de clientes de públicos personalizados.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Um exemplo dos termos a serem aceitos para ferramentas de negócios do Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consulte a [seção de FAQ](#terms) para mais detalhes sobre a auditoria da sua conta do Facebook ao integrar.

### Etapa 3: adicione um componente de público do Facebook no Canvas Flow

Adicione um componente na sua canva e selecione **público do Facebook**.

![Uma lista de componentes a serem adicionados ao Canva.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![O componente de Sincronização de Público.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 4: Configuração de sincronização

Selecione o botão **Público Personalizado** para abrir o editor de componentes. Em seguida, selecione **Facebook** como o parceiro de Sincronização de Público.

!["Configurar Sincronização de Público" com opções para escolher um parceiro.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Selecione a conta de anúncio do Facebook desejada. No menu suspenso **Escolher um Público Novo ou Existente**, digite o nome de um novo ou existente público. 

{% tabs %}
{% tab Criar um novo público %}

1. Digite um nome para o novo público personalizado.
2. Selecione **Adicionar Usuários ao Público** e escolha os campos que você gostaria de sincronizar com o Facebook. 
3. Em seguida, selecione **Criar Público** para salvar seu público.

![Configuração de sincronização de público para um público com as informações de e-mail, telefone, primeiro nome e sobrenome para correspondência.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Você será notificado na parte superior do editor de etapas se o público for criado com sucesso ou se ocorrer um erro durante este processo. Você também pode referenciar este público para remoção de usuários mais tarde na jornada do Canva, pois o público foi criado em modo de rascunho.

Quando você lançar um Canva com um novo público, a Braze criará o novo público personalizado ao lançar o Canva e, subsequentemente, sincronizará usuários em tempo quase real à medida que eles entrarem na etapa de Sincronização de Público.

{% endtab %}
{% tab Sincronização com um público existente %}

A Braze oferece a capacidade de adicionar ou remover usuários de públicos personalizados existentes do Facebook para confirmar que esses públicos estão atualizados. Para sincronizar com um público existente, faça o seguinte:

1. Digite o nome do público existente no dropdown.
2. Escolha se deseja **Adicionar ao Público** ou **Remover do Público**. 
3. A Braze irá adicionar ou remover usuários em tempo quase real à medida que eles entrarem na etapa de Público do Facebook. 

![Configuração de sincronização de público para remover as informações de e-mail, telefone, primeiro nome e sobrenome.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
O Facebook proíbe a remoção de usuários de públicos personalizados onde o tamanho do público é muito baixo (tipicamente menos de 1.000 usuários). Como resultado, a Braze não poderá sincronizar usuários para remoção da etapa de Sincronização de Público até que o público atinja o tamanho apropriado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar canva

Depois de configurar seu componente de Público do Facebook, é hora de lançar o Canvas! O novo público personalizado será criado, e os usuários que passarem pela etapa de Público do Facebook serão inseridos neste público personalizado no Facebook. Se o seu Canvas contiver etapas subsequentes, seus usuários avançarão para a próxima etapa em sua jornada de usuário.

A guia **Histórico** do público personalizado no Gerenciador de Público do Facebook refletirá o número de usuários enviados para o público do Braze. Se um usuário reentrar na etapa, ele será enviado para o Facebook novamente.

![Detalhes do público e a guia Histórico para um determinado público do Facebook que inclui uma tabela de Histórico de Público com colunas para a atividade, detalhes da atividade, itens alterados e a data e hora.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| Métrico | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram neste componente para serem sincronizados com o Facebook. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso ao Facebook. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. Os campos são correspondidos usando um operador "OU", o que significa que, desde que um usuário tenha um dos campos no Facebook, o Facebook corresponderá o usuário mesmo que não haja correspondência em todos os outros campos. |
| Usuários pendentes | Número de usuários atualmente sendo processados pela Braze para sincronizar com o Facebook. |
| Usuários com erro | Número de usuários que não foram sincronizados com o Facebook devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do Facebook ou a exclusão do público personalizado do Facebook. |
| Saíram do canva | Número de usuários que saíram da canva. Isso ocorre quando a última etapa de um canva é uma etapa do Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Haverá uma postergação na reportagem para usuários sincronizados e métricas de usuários com erro devido ao processamento interno.
{% endalert %}

## Perguntas frequentes

### Quanto tempo leva para que meus públicos sejam preenchidos no meu dashboard de parceiro do Audience Sync?

O tempo necessário para preencher um público depende do parceiro específico. Todas as redes processarão as solicitações do Braze e tentarão combinar os usuários. Pode levar até 24 horas para que os públicos personalizados sejam atualizados.

### O que devo fazer a seguir se eu receber um erro de token inválido?

Você pode simplesmente desconectar e reconectar sua conta do Facebook na página de parceiros do Facebook. Confirme com o administrador do seu Gerenciador de Negócios do Facebook que você tem as permissões apropriadas para a conta de anúncios que deseja sincronizar.

### Por que meu Canvas não pode ser lançado?

- Certifique-se de que o token de usuário do sistema esteja autenticado e tenha acesso às contas de anúncios desejadas no Facebook Business Manager.
- Certifique-se de ter selecionado uma conta de anúncios, inserido um nome para o novo público personalizado e selecionado os campos correspondentes.
- Você pode ter atingido o limite de 500 públicos personalizados no Facebook. Acesse o Gerenciador de Públicos do Facebook para excluir alguns que não são necessários antes de criar novos públicos personalizados usando o Canvas.

### Como posso saber se os usuários foram correspondidos após passar os usuários para o Facebook?

O Facebook não fornece essas informações por motivos de privacidade.

### A Braze suporta públicos personalizados baseados em valor?

No momento, os públicos personalizados baseados em valor não são suportados pela Braze. Se você estiver interessado em sincronizar esses tipos de públicos personalizados, envie [comentários sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### A Braze faz hash dos dados antes de enviá-los para parceiros de Sincronização de Público?

Uma vez que os dados de e-mail são normalizados, a Braze os faz hash com SHA256.

**IDFA/AAID/phone:** A Braze faz hash com SHA256. Os tipos de público que sincronizamos são sempre um dos seguintes:

- IDFA_SHA256
- AAID_SHA256
- E-MAIL_SHA256
- PHONE_SHA256\.

Em termos de frequência, o Braze só irá hash informações pessoalmente identificáveis (PII) à medida que os usuários entram na etapa de Sincronização de Público na jornada do usuário em preparação para a sincronização.

### Como resolvo um problema com a sincronização de um público personalizado baseado em valor?

Neste momento, públicos personalizados baseados em valor não são suportados pelo Braze. Se você tentar sincronizar com este público, isso pode causar erros para sua etapa de Sincronização de Público. Para resolver isso, siga estas etapas:

1. Acessar seu dashboard do Facebook Ad Manager e selecionar **Audiences**.
2. Selecione **Criar público** > **Público personalizado**.
3. Selecione **Lista de clientes**.
4. Faça upload do seu CSV ou lista sem a coluna **Value**. Selecione **No, continue with a customer list that doesn't include customer value** (Não, continue com uma lista de clientes que não inclui o valor do cliente).
5. Conclua a criação do seu público personalizado.
6. Na Braze, atualize a etapa Facebook Audience Sync com o público personalizado que você criou.

### Recebi um e-mail relacionado aos termos de serviço do público personalizado do Facebook. O que devo fazer para resolver isso?

Para usar o público do Facebook, você precisa aceitar estes termos do contrato de serviço. 

- Se sua conta de anúncios estiver diretamente associada à sua conta pessoal do Facebook, você pode aceitar os termos de serviço na sua conta pessoal aqui: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Se sua conta de anúncios estiver vinculada à conta do Gerenciador de Negócios da sua empresa, você precisa aceitar os termos de serviço na sua conta do Gerenciador de Negócios do Facebook aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Depois de aceitar os termos de serviço do público personalizado do Facebook, faça o seguinte:

1. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
2. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva.

Então, o Braze pode sincronizar usuários assim que eles chegarem à etapa de Sincronização de Público do Facebook.

## Solução de problemas

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Erro</th>
      <th>Descrição</th>
      <th>Etapas para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token inválido</b></td>
      <td>Causas típicas são se o usuário que conectou a integração mudar sua senha, as credenciais expirarem, e mais.</td>
      <td>Acesse <b>Integrações de Parceiros</b> > <b>Facebook</b> e desconecte e reconecte sua conta. Consulte <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta seção de solução de problemas</a> para etapas adicionais para auditar sua conta do Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamanho do público muito baixo</b></td>
      <td>Esse erro pode ocorrer se você criou uma etapa de Sincronização de Público que remove usuários dos seus públicos. Se o tamanho do seu público se aproximar de zero, a rede pode sinalizar que o tamanho do público é muito pequeno para ser atendido.</td>
      <td> Use uma estratégia de Sincronização de Público que adicione e remova usuários regularmente, onde não esvazie completamente o tamanho do público.</td>
    </tr>
    <tr>
      <td><b>O público não existe</b></td>
      <td>A etapa de Sincronização de Público usa um público que não existe ou foi excluído. Isso também pode ser acionado se você não tiver mais a permissão necessária para acessar o público.</td>
      <td>Peça a um administrador para verificar na plataforma parceira se o público ainda existe. <br><br>Se existir, confirme se o usuário que conectou a integração tem permissão para o público. Se não tiver, o usuário deve receber acesso a esse público. <br><br>Se o público foi removido intencionalmente, adicione um público ativo e crie um novo público na etapa.</td>
    </tr>
    <tr>
      <td><b>Tentativa de acesso à conta de anúncios</b></td>
      <td>Você não tem permissões para a conta de anúncios ou público que selecionou.</td>
      <td>Trabalhe com os administradores da sua conta de anúncios para obter acesso e permissões adequadas.</td>
    </tr>
    <tr>
      <td><b>Termos de Serviço Não Aceitos</b></td>
      <td>Para alguns destinos de Sincronização de Público, como o Facebook, é exigido pela rede de anúncios que você aceite termos específicos de serviço para usar o recurso de Sincronização de Público. Esse erro será disparado se você não tiver aceitado os termos apropriados. Como resultado, você também pode ter recebido um e-mail com este assunto da Braze: “Suas credenciais de autorização para o Facebook são inválidas.”</td>
      <td>Verifique se você aceitou os termos exigidos pelo Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos os Usuários Estão Com Erro</b></td>
      <td>Se todos os usuários estiverem com erro em uma etapa, apesar de confirmar que esses usuários têm valores para os campos selecionados na etapa, isso pode indicar um problema com sua conta do Facebook.</td>
      <td>Siga os passos na <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta seção de solução de problemas</a> para verificar sua conta quanto a quaisquer problemas.
      </td>
    </tr>
    <tr>
      <td><b>Falha ao criar público</b></td>
      <td>Na página de Parceiros de Tecnologia do Facebook, você está vendo “Conectado”, mas há um erro na etapa de Sincronização de Público do Facebook ao sincronizar um público, “Falha ao criar público 'nome do público'". A autorização da sua conta do Facebook falhou. Visite a página de Parceiros de Tecnologia para reconectar sua conta.</td>
      <td>Siga os passos na <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta seção de solução de problemas</a> para verificar sua conta quanto a quaisquer problemas.
      </td>
    </tr>
  </tbody>
</table>

### Audite sua conta do Facebook

Se você encontrar problemas adicionais com sua integração, consulte as seções e etapas a seguir para auditar sua conta do Facebook. 

#### Revisar permissões da conta

1. Revisar [documentação do Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre como gerenciar essas permissões em sua plataforma. Para o Facebook Business Manager, você precisa de pelo menos um **Admin** ou **colaborador** com acesso às contas de anúncios necessárias.
2. Como um **colaborador**, confirme que o Admin lhe concede permissões completas de **Gerenciar Conta de Anúncio** para cada conta de anúncio para criar um público ou sincronizar usuários com o público. 
3. Depois que isso for concedido, você deve desconectar e reconectar sua conta.

#### Aceitar os termos de serviço {#terms}

Aceitar quaisquer Termos de Serviço (TOS) pendentes do Facebook. O Facebook periodicamente exigirá que você (o usuário) e o gerente de negócios reaprovar seus termos de serviço.

1. O usuário conectado precisa aceitar todos os termos de serviço para cada uma de suas contas de anúncios:
- TOS de Público Personalizado para sua conta pessoal do Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Uma conta com permissões de controle total para gerenciar uma conta de anúncio.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar seu ID de conta e de negócios, siga estas etapas:

1. Acesse sua [conta do Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Confirme que você está usando a conta de anúncio correta verificando no menu suspenso.
3. Na URL, encontre o ID da conta após `act=` e o ID do negócio após `business_id=`

![A URL com o ID da conta e o ID do negócio destacados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Leia e selecione **Aceitar** para os Termos do Público Personalizado. Recomendamos confirmar para qual conta os termos de serviço estão sendo assinados usando o menu suspenso no topo dos termos.

![O menu suspenso que mostra a conta que está assinando os termos de serviço.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\. Você deve selecionar **Aceitar** para os termos de serviço. Depois, você verá esta mensagem: "Você aceitou estes termos de serviço em nome da Braze".
6\. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
7\. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva. A partir daí, a Braze conseguirá sincronizar os usuários assim que eles chegarem à etapa de público do Facebook.
8\. Se o problema persistir, tente usar um usuário separado com permissões de administrador para aceitar manualmente os termos através do Gerenciador de Anúncios.

#### Complete quaisquer tarefas pendentes 

Verifique se você tem alguma tarefa pendente com o Facebook que possa estar bloqueando você de usar os serviços de anúncios do Facebook:

1. [Faça login no Gerenciador de Anúncios do Facebook](https://adsmanager.facebook.com/).
2. Selecione a conta de anúncio com a qual você está tendo problemas.
3. Na navegação, selecione sua **Visão Geral da Conta**. <br> ![A navegação com Visão Geral da Conta selecionada.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Verifique se há alertas que precisam ser resolvidos. <br> ![Uma conta com um cartão de crédito expirado.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Verifique se há tarefas de configuração que precisam ser concluídas. <br> ![Uma conta com uma configuração de conta parcialmente concluída.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conecte-se com um usuário diferente

Como um passo adicional de solução de problemas, recomendamos que um usuário administrador diferente tente conectar sua conta fazendo o seguinte:

1. Desconecte a integração atual.
2. Um usuário separado com permissões de administrador conecta sua conta de usuário do Facebook.

