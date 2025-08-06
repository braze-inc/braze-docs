---
nav_title: Facebook
article_title: Sincronização de canva público com o Facebook
description: "Este artigo de referência abordará como usar a sincronização de público do Braze para o Facebook, para entregar anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Sincronização de público com o Facebook

> Usando o Braze Audience Sync to Facebook, você pode optar por adicionar os dados de seus próprios usuários da integração do Braze aos públicos personalizados do Facebook para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais.

Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS ou webhook) em um Braze Canvas com base nos dados de seu usuário agora pode ser usado para disparar um anúncio para esse usuário no Facebook usando públicos personalizados. Por exemplo, ao configurar uma sincronização de público do Facebook, você poderá usar uma ampla variedade de campos primários, como e-mail, telefone, nome e sobrenome.

**Os casos de uso comuns para a sincronização de públicos personalizados incluem**:

- Direcionamento de usuários de alto valor com vários canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.
- Criação de públicos semelhantes para adquirir novos usuários com mais eficiência.

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Facebook. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Considerações sobre sincronização de usuário e limite de frequência
 
À medida que os usuários atingirem a etapa de sincronização de público, o Braze sincronizará esses usuários quase em tempo real, respeitando também os limites de frequência da API de marketing do Facebook. O que isso significa na prática é que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviar esses usuários para o Facebook. 

O limite de frequência da API de marketing do Facebook determina que não haja mais do que ~190.000 solicitações de API para cada conta de anúncio em um período de uma hora. Se um cliente do Braze atingir esse limite de frequência, o Braze the Canvas tentará novamente a sincronização por até 13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored (Usuários com erro).

## Pré-requisitos

Você precisará confirmar que os itens a seguir foram criados e concluídos antes de configurar a etapa do Facebook Audience no Canva. 

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps). |
| Conta de Anúncio do Facebook | [Facebook][2] | Uma conta de anúncio ativa do Facebook vinculada ao gerente de negócios da sua marca.<br><br>Certifique-se de que o administrador do Facebook Business Manager tenha concedido permissões de "Gerenciar campanhas" ou "Gerenciar contas de anúncios" para as contas de anúncios do Facebook que você planeja usar com o Braze. Além disso, verifique se você aceitou os termos e condições de sua conta de anúncios. |
| Termos de públicos personalizados do Facebook | [Facebook][3] | Aceite os Termos de Públicos Personalizados do Facebook para suas contas de anúncios do Facebook que você planeja usar com o Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: conecte-se ao Facebook

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**. Em Facebook Audience Export, selecione **Connect Facebook**.

![Página de tecnologia do Facebook no Braze que inclui uma seção de Visão geral e uma seção de Exportação de público do Facebook com o botão Conectado ao Facebook.][4]{: style="max-width:85%;"}

Uma janela de diálogo oAuth do Facebook aparecerá para autorizar a Braze a criar Públicos Personalizados em suas contas de anúncios do Facebook.

![A primeira caixa de diálogo do Facebook solicitando para "Conectar como X", em que X é seu nome de usuário do Facebook.][6]{: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios para suas contas de anúncios.][5]{: style="max-width:40%;"}

Depois de vincular o Braze à sua conta do Facebook, você poderá selecionar quais contas de anúncios deseja sincronizar no seu espaço de trabalho do Braze. 

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Facebook.][7]{: style="max-width:70%;"}

Depois de se conectar com sucesso, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.][8]{: style="max-width:85%;"}

Sua conexão com o Facebook é aplicada no nível do espaço de trabalho do Braze. Se o administrador do Facebook remover você do seu Facebook Business Manager ou o acesso às contas do Facebook conectadas, a Braze detectará um token inválido. Como resultado, seus canvas ativos usando componentes do público do Facebook mostrarão erros, e o Braze não poderá sincronizar usuários. 

{% alert important %}
Para clientes que já passaram pelo processo de Revisão de App do Facebook para [Gerenciamento de Anúncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Acesso Padrão de Gerenciamento de Anúncios](https://developers.facebook.com/docs/marketing-api/access#standard), seu Token de Usuário do Sistema ainda será válido para o componente público do Facebook. Você não poderá editar ou revogar o Token de Usuário do Sistema do Facebook através da página de parceiro do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir seu Token de Usuário do Sistema do Facebook dentro do seu espaço de trabalho do Braze. 

<br><br>A configuração do Facebook oAuth também se aplicará às [exportações do Facebook usando Segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Etapa 2: Aceitar os termos de serviço de públicos personalizados

Antes de criar seu Canva, você deve aceitar os seguintes termos de serviço do Facebook nos links a seguir:

- **Lista de clientes Termos de públicos personalizados para sua conta pessoal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Termos das ferramentas comerciais do Facebook para sua conta comercial:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Um exemplo dos termos a serem aceitos para públicos personalizados da lista de clientes.][24]{: style="max-width:85%;"}
![Um exemplo dos termos a serem aceitos para as ferramentas de negócios do Facebook.][25]{: style="max-width:85%;"}

Consulte a [seção Perguntas frequentes](#terms) para obter mais detalhes sobre a auditoria da sua conta do Facebook durante a integração.

### Etapa 3: adicione um componente de público do Facebook no Canvas Flow

Adicione um componente na sua canva e selecione **público do Facebook**.

![Uma lista de componentes a serem adicionados ao Canva.][18]{: style="max-width:35%;"} ![O componente Audience Sync.][20]{: style="max-width:28%;"}

### Etapa 4: Configuração de sincronização

Selecione o botão **Público personalizado** para abrir o editor de componentes. Em seguida, selecione **Facebook** como parceiro do Audience Sync.

!["Set up Audience Sync" (Configurar sincronização do público) com opções para escolher um parceiro.][19]{: style="max-width:80%;"}

Selecione a conta de anúncio do Facebook desejada. No menu suspenso **Escolher um Público Novo ou Existente**, digite o nome de um novo ou existente público. 

{% tabs %}
{% tab Criar um novo público %}

1. Digite um nome para o novo público personalizado.
2. Selecione **Add Users to Audience (Adicionar usuários ao público do** Facebook) e escolha os campos que deseja sincronizar com o Facebook. 
3. Em seguida, selecione **Create Audience (Criar público** ) para salvar seu público.

![Configuração de sincronização de público-alvo para o público "abandono de carrinho" com as informações de e-mail, telefone, nome e sobrenome para corresponder.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Você será notificado na parte superior do editor de etapas se o público for criado com êxito ou se ocorrer um erro durante esse processo. Também é possível fazer referência a esse público para remoção de usuários posteriormente na jornada do Canva, pois o público foi criado no modo de rascunho.

![Uma mensagem de sucesso informando que o público "abandoned_cart" foi criado.]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

Ao lançar um Canvas com um novo público, o Braze criará o novo público personalizado ao lançar o Canvas e, posteriormente, sincronizará os usuários quase em tempo real quando eles entrarem na etapa do Audience Sync.

{% endtab %}
{% tab Sincronização com um público existente %}

O Braze oferece a capacidade de adicionar ou remover usuários de públicos personalizados existentes do Facebook para confirmar que esses públicos estão atualizados. Para sincronizar com um público existente, faça o seguinte:

1. Digite o nome do público existente no menu suspenso.
2. Escolha se você deseja **Adicionar ao público** ou **Remover do público**. 
3. O Braze adicionará ou removerá usuários quase em tempo real quando eles entrarem na etapa de público do Facebook. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
O Facebook proíbe a remoção de usuários de públicos personalizados quando o tamanho do público é muito baixo (normalmente, menos de 1.000 usuários). Como resultado, o Braze não poderá sincronizar usuários para uma remoção da etapa de sincronização de público até que o público atinja o tamanho apropriado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar canva

Depois de configurar seu componente do público do Facebook, é hora de lançar o Canva! O novo público personalizado será criado, e os usuários que passarem pela etapa do Facebook Audience serão transferidos para esse público personalizado no Facebook. Se o seu Canva contiver etapas subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

A guia **Histórico** do público personalizado no Gerenciador de Público do Facebook refletirá o número de usuários enviados para o público do Braze. Se um usuário reentrar na etapa, ele será enviado para o Facebook novamente.

![Detalhes do público e a guia de histórico para um determinado público do Facebook, com uma tabela de histórico do público com colunas de atividade, detalhes da atividade, itens alterados e data e hora.][9]{: style="max-width:80%;"}

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| Métrico | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram neste componente para serem sincronizados com o Facebook. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso ao Facebook. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários atualmente sendo processados pela Braze para sincronizar com o Facebook. |
| Usuários com erro | Número de usuários que não foram sincronizados com o Facebook devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do Facebook ou a exclusão do público personalizado do Facebook. |
| Saíram do canva | Número de usuários que saíram da canva. Isso ocorre quando a última etapa de um canva é uma etapa do Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Haverá uma postergação nos relatórios de métricas de usuários sincronizados e usuários com erro devido ao processamento interno.
{% endalert %}

## Perguntas frequentes

### Quanto tempo leva para que meus públicos sejam preenchidos no meu dashboard de parceiro do Audience Sync?

O tempo necessário para preencher um público depende do parceiro específico. Todas as redes processarão as solicitações do Braze e tentarão combinar os usuários. Pode levar até 24 horas para que os públicos personalizados sejam atualizados.

### O que devo fazer em seguida se receber um erro de token inválido?

Você pode simplesmente desconectar e reconectar sua conta do Facebook na página de parceiros do Facebook. Confirme com seu administrador do Facebook Business Manager que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canva não pode ser iniciado?

- Certifique-se de que o token de usuário do sistema esteja autenticado e tenha acesso às contas de anúncios desejadas no Facebook Business Manager.
- Certifique-se de ter selecionado uma conta de anúncios, inserido um nome para o novo público personalizado e selecionado os campos correspondentes.
- Você pode ter atingido o limite de 500 públicos personalizados no Facebook. Acesse o Facebook Audience Manager para excluir alguns públicos desnecessários antes de criar novos públicos personalizados usando o Canva.

### Como posso saber se os usuários foram correspondidos depois de passá-los para o Facebook?

O Facebook não fornece essas informações por motivos de privacidade.

### O Braze oferece suporte a públicos personalizados baseados em valor?

No momento, os públicos personalizados baseados em valor não são suportados pela Braze. Se você estiver interessado em sincronizar esses tipos de públicos personalizados, envie [comentários sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### O Braze faz hash dos dados antes de enviá-los aos parceiros do Audience Sync?

Depois que os dados de e-mail são normalizados, o Braze faz o hash com SHA256.

**IDFA/AAID/phone:** Braze hashes com SHA256. Os tipos de público com os quais sincronizamos são sempre um dos seguintes:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256\.

Em termos de frequência, o Braze só fará o hash das informações de identificação pessoal (IPI) do usuário quando os usuários entrarem na etapa de sincronização do público na jornada do usuário em preparação para a sincronização.

### Como faço para resolver um problema com a sincronização de um público personalizado semelhante baseado em valor?

Neste momento, públicos personalizados semelhantes baseados em valor não são suportados pela Braze. Se você tentar sincronizar com este público, isso pode causar erros para sua etapa de Sincronização de Público. Para resolver isso, siga estas etapas:

1. Acessar seu dashboard do Facebook Ad Manager e selecionar **Audiences**.
2. Selecione **Criar público** > **Público personalizado**.
3. Selecione **Lista de clientes**.
4. Faça upload do seu CSV ou lista sem a coluna **Value**. Selecione **No, continue with a customer list that doesn't include customer value** (Não, continue com uma lista de clientes que não inclui o valor do cliente).
5. Conclua a criação do seu público personalizado.
6. Na Braze, atualize a etapa Facebook Audience Sync com o público personalizado que você criou.

### Recebi um e-mail relacionado aos termos de serviço do público personalizado do Facebook. O que devo fazer para resolver isso?

Para usar o público do Facebook, você precisa aceitar estes termos do contrato de serviço. 

- Se a sua conta de anúncios estiver diretamente associada à sua conta pessoal do Facebook, você poderá aceitar os termos de serviço da sua conta pessoal aqui: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Se sua conta de anúncios estiver vinculada à conta do Business Manager de sua empresa, será necessário aceitar os termos de serviço em sua conta do Facebook Business Manager aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Depois de aceitar os termos de serviço do público personalizado do Facebook, faça o seguinte:

1. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
2. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva.

Em seguida, o Braze poderá sincronizar os usuários assim que eles chegarem à etapa de sincronização do público do Facebook.

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
      <td>As causas típicas são se o usuário que conectou a integração alterar sua senha, se as credenciais expirarem e muito mais.</td>
      <td>Acesse <b>Partner Integrations</b> > <b>Facebook</b> e desconecte e reconecte sua conta. Consulte <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta seção</a> de solução de problemas esta seção de solução de problemas para obter etapas adicionais para auditar sua conta do Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamanho do público muito baixo</b></td>
      <td>Esse erro pode ocorrer se você tiver criado uma etapa de Audience Sync que remove usuários de seus públicos. Se o tamanho de seu público se aproximar de zero, a rede poderá sinalizar que ele é muito baixo para ser atendido.</td>
      <td> Use uma estratégia de sincronização de público que adicione e remova usuários regularmente, de modo a não esgotar totalmente o tamanho do público.</td>
    </tr>
    <tr>
      <td><b>O público não existe</b></td>
      <td>A etapa Audience Sync usa um público que não existe ou foi excluído. Isso também pode ser disparado se você não tiver mais a permissão necessária para acessar o público.</td>
      <td>Faça uma verificação administrativa na plataforma do parceiro para ver se o público ainda existe. <br><br>Se existir, confirme se o usuário que conectou a integração tem permissão para o público. Caso contrário, o usuário deve receber acesso a esse público. <br><br>Se o público tiver sido removido intencionalmente, adicione um público ativo e crie um novo público na etapa.</td>
    </tr>
    <tr>
      <td><b>Tentativa de acesso à conta de anúncios</b></td>
      <td>Você não tem permissões para a conta de anúncios ou o público selecionado.</td>
      <td>Trabalhe com os administradores de sua conta de anúncios para obter acesso e permissões adequados.</td>
    </tr>
    <tr>
      <td><b>Termos de serviço não aceitos</b></td>
      <td>Para alguns destinos do Audience Sync, como o Facebook, a rede de anúncios exige que você aceite termos de serviços específicos para usar o recurso Audience Sync. Esse erro será disparado se você não tiver aceitado os termos apropriados. Como resultado, você também pode ter recebido um e-mail da Braze com esse assunto: "Suas credenciais de autorização para o Facebook são inválidas."</td>
      <td>Verifique se você aceitou os termos exigidos pelo Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos os usuários estão apresentando erros</b></td>
      <td>Se todos os usuários apresentarem erros em uma etapa, apesar da confirmação de que esses usuários têm valores para os campos selecionados na etapa, isso pode indicar um problema com a sua conta do Facebook.</td>
      <td>Siga as etapas <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>desta seção de solução de problemas</a> para verificar se há algum problema na sua conta.
      </td>
    </tr>
    <tr>
      <td><b>Falha ao criar público</b></td>
      <td>Na página Parceiro de tecnologia do Facebook, você está vendo "Conectado", mas há um erro na etapa Sincronização de público do Facebook ao sincronizar um público, "Falha ao criar o público "nome do público"". A autorização de sua conta do Facebook falhou. Visite a página Parceiros de tecnologia para reconectar sua conta.</td>
      <td>Siga as etapas <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>desta seção de solução de problemas</a> para verificar se há algum problema na sua conta.
      </td>
    </tr>
  </tbody>
</table>

### Audite sua conta do Facebook

Se tiver problemas adicionais com a integração, consulte as seções e etapas a seguir para auditar sua conta do Facebook. 

#### Revisar as permissões da conta

1. Consulte [a documentação do Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre como gerenciar essas permissões em sua plataforma. Para o Facebook Business Manager, você precisa, no mínimo, de uma função de **administrador** ou de **colaborador** Business Manager com acesso às contas de anúncios necessárias.
2. Como **funcionário**, confirme se o administrador concede a você permissões completas de **Gerenciar conta de** anúncios para cada conta de anúncios para criar um público ou sincronizar usuários com o público. 
3. Depois que isso for concedido, você deverá desconectar e reconectar sua conta.

#### Aceitar os termos de serviço {#terms}

Aceitar quaisquer Termos de serviços (TOS) pendentes do Facebook. O Facebook solicitará periodicamente que você (o usuário) e o gerente de negócios aprovem novamente os termos de serviço.

1. O usuário conectado precisa aceitar todos os termos de serviço de cada uma de suas contas de anúncios:
- Termos de serviço do público personalizado para sua conta pessoal do Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- TOS de público-alvo personalizado com base em valor:
  - Se a sua conta de anúncios estiver vinculada à conta do Business Manager da sua empresa, você deverá aceitar os Termos de Serviço na sua conta do Business Manager aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.
  - Se a sua conta de anúncios estiver vinculada à sua conta pessoal (não associada a nenhuma empresa), você deverá aceitar os Termos de Serviço aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>`

![Uma conta com permissões de controle total para gerenciar uma conta de anúncios.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar sua conta e ID comercial, siga estas etapas:

1. Acesse sua [conta do Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Confirme que está usando a conta de anúncios correta, verificando-a no menu suspenso.
3. No URL, localize o ID da conta após `act=` e o ID da empresa após `business_id=`

![O URL com o ID da conta e o ID da empresa destacados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Leia e selecione **Aceitar** para os Termos do público personalizado. Recomendamos confirmar para qual conta os termos de serviços estão sendo feitos login usando o menu suspenso na parte superior dos termos.

![O menu suspenso que mostra a conta que está fazendo login nos termos de serviço.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\. Você deve selecionar **Aceitar** para os termos de serviços. Depois, você verá esta mensagem: "Você aceitou estes termos de serviço em nome da Braze".
6\. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
7\. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva. A partir daí, a Braze conseguirá sincronizar os usuários assim que eles chegarem à etapa de público do Facebook.
8\. Se o problema persistir, tente usar um usuário separado com permissões de administrador para aceitar manualmente os termos por meio do Gerenciador de Anúncios.

#### Concluir todas as tarefas pendentes 

Verifique se você tem alguma tarefa pendente com o Facebook que possa estar bloqueando o uso dos serviços do Facebook Ads:

1. [Registre-se no Gerenciador de anúncios do Facebook](https://adsmanager.facebook.com/).
2. Selecione a conta de anúncios com a qual você está tendo problemas.
3. Na navegação, selecione a **Visão geral da conta**. <br> ![A navegação com a Visão geral da conta selecionada.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Verifique se há algum alerta que precise ser resolvido. <br> ![Uma conta com um cartão de crédito expirado.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Verifique se há alguma tarefa de configuração que precise ser concluída. <br> ![Uma conta com uma configuração de conta parcialmente concluída.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conecte-se com um usuário diferente

Como outra etapa de solução de problemas, recomendamos que um usuário administrador diferente tente conectar sua conta fazendo o seguinte:

1. Desconecte a integração atual.
2. Um usuário separado com permissões de administrador conecta sua conta de usuário do Facebook.

[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}