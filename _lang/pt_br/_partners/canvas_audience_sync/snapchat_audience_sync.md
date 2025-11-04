---
nav_title: Snapchat
article_title: Sincronização do público do Canva com o Snapchat
description: "Este artigo de referência aborda como usar o Braze Audience Sync com o Snapchat para entregar anúncios com base em disparadores comportamentais, segmentação e muito mais."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# Sincronização do público com o Snapchat

Usando o Braze Audience Sync to Snapchat, as marcas podem adicionar dados de usuários de sua integração Braze às listas de clientes do Snapchat para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Braze Canvas com base nos dados de seu usuário agora pode ser usado para disparar um anúncio para esse usuário em suas listas de clientes do Snapchat.

**Os casos de uso comuns para sincronização de público incluem:**

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários menos responsivos para outros canais de marketing
- Criar públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca
- Criação de públicos semelhantes para adquirir novos usuários com mais eficiência

Esse recurso permite que os usuários controlem quais dados primários específicos são compartilhados com o Snapchat. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o Snapchat é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta da Braze.
{% endalert %}

## Pré-requisitos 

Você deve garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar a etapa do público do Snapchat no Canva.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Gerente de negócios do Snapchat | Snapchat | Uma ferramenta centralizada para gerenciar os ativos do Snapchat de sua marca (como contas de anúncios, páginas, apps). |
| Conta de anúncios do Snapchat | Snapchat | Uma conta ativa de anúncios do Snapchat vinculada ao Snapchat Business Manager de sua marca.<br><br>Certifique-se de que o administrador do Snapchat Business Manager lhe concedeu permissões de administrador para as contas de anúncios do Snapchat que você planeja usar com o Braze. |
| Termos e políticas do Snapchat | [Snapchat](https://www.snap.com/en-US/policies) | Concordar em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo Snapchat relacionados ao seu uso do Snapchat Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir: os Termos de Serviço, os Termos de Serviço para Empresas, os Termos do Desenvolvedor, o Audience Match, as Políticas de Publicidade, a Política de Conteúdo Comercial, as Diretrizes da Comunidade e a Responsabilidade do Fornecedor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração 

### Etapa 1: Conectar-se ao Snapchat

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Snapchat**. Em Snapchat Audience Sync, selecione **Connect Snapchat**.

![Página de tecnologia do Snapchat no Braze que inclui uma seção de visão geral e uma seção de sincronização do público do Snapchat com o botão Snapchat conectado.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Em seguida, você verá a página do Snapchat OAuth para autorizar a Braze a conceder as permissões relacionadas à sua integração com o Audience Sync.

Depois de selecionar confirmar, você será redirecionado de volta ao Braze para selecionar as contas de anúncios do Snapchat que deseja sincronizar. 

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Snapchat.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Uma vez conectado com sucesso, você retornará à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Snapchat mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Sua conexão com o Snapchat será aplicada no nível do espaço de trabalho do Braze. Se o administrador do Snapchat remover você do Snapchat Business Manager ou do acesso às contas de anúncios do Snapchat conectadas, o Braze detectará um token inválido. Como resultado, seus Canvas ativos usando o Snapchat mostrarão erros e o Braze não poderá sincronizar os usuários.

### Etapa 2: Adicionar uma etapa de sincronização de público com o Snapchat

Adicione um componente ao seu canva e selecione **Audience Sync**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração de sincronização

Clique no botão **Público personalizado** para abrir o editor de componentes.

Selecione **TikTok** como parceiro desejado do Audience Sync.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione sua conta de anúncio do Snapchat desejada. No menu suspenso **Choose a New or Existing Audience (Escolher um público novo ou existente** ), digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience (Adicionar usuários ao público**) e selecione os campos que deseja sincronizar com o Snapchat. Em seguida, salve seu público clicando no botão **Create Audience (Criar público** ) na parte inferior do editor de etapas.

![Visualização expandida da etapa do canva de público-alvo personalizado. Aqui a conta de anúncios desejada é selecionada, e um novo público é criado.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Os usuários serão notificados no topo do editor de etapas se o público for criado com sucesso ou se ocorrerem erros durante este processo. Os usuários também podem fazer referência a esse público para remoção de usuários posteriormente na jornada do Canva, pois o público foi criado no modo de rascunho.

![Um alerta que aparece depois que um novo público é criado no componente do canva.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Ao lançar um canva com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram no componente do Audience Sync.

{% endtab %}
{% tab Sincronização com um público existente %}
**Sincronização com um público existente**<br>
O Braze também oferece a capacidade de adicionar usuários aos públicos existentes do Snapchat para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público no menu suspenso e **adicione-o ao público**. A Braze adicionará usuários quase em tempo real quando eles entrarem no componente do Audience Sync.

![Visualização expandida da etapa do canva de público-alvo personalizado. Aqui a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar canva

Depois de configurar o Audience Sync para o Snapchat, inicie o canva! Um novo público será criado, e os usuários que passarem pela etapa do Audience Sync serão transferidos para esse público no Snapchat. Se o seu Canva contiver componentes subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

É possível visualizar o público no Snapchat entrando em sua conta do Gerenciador de Anúncios e selecionando **Públicos** na seção Ativos da navegação. Na página **Audiences (Públicos** ), você pode ver o tamanho de cada público depois que ele atinge ~1.000.

![Detalhes do público de um determinado público do Snapchat que incluem o nome do público, o tipo de público, o tamanho do público e a retenção do público em dias.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Considerações sobre sincronização de usuários e limite de frequência

Quando os usuários atingirem a etapa de sincronização do público, o Braze sincronizará esses usuários quase em tempo real, respeitando os limites de frequência da API do Snapchat. Na prática, o Braze tentará agrupar e processar o máximo de usuários a cada 5 segundos antes de enviar esses usuários para o Snapchat.

O limite de frequência da API do Snapchat estabelece não mais do que dez consultas por segundo e 100.000 usuários por solicitação. Se um cliente do Braze atingir esse limite de frequência, o Braze the Canvas tentará novamente a sincronização por até 13 horas. Se a sincronização não for possível, esses usuários são listados na métrica de Usuários com Erro.

### Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| Métrico | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com o Snapchat. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o Snapchat. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários que estão sendo processados pelo Braze para sincronização com o Snapchat. |
| Usuários com erro | Número de usuários que não foram sincronizados com o Snapchat devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do Snapchat ou se o público foi excluído do Snapchat. |
| Saíram do canva | Número de usuários que saíram da canva. Isso ocorre quando a última etapa de um canva é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lembre-se de que haverá uma postergação nos relatórios de usuários sincronizados e métricas com erro devido à descarga em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}   

## Perguntas frequentes

### Quantos públicos o Snapchat pode suportar?

No momento, você só pode ter 1.000 públicos na sua conta do Snapchat. 

Se você exceder esse limite, o Braze o notificará de que não é possível criar novos públicos. Você precisará remover os públicos que não está mais usando em sua conta de anúncios do Snapchat.

### Como posso saber se os usuários foram correspondidos depois de passá-los para o Snapchat?

O Snapchat não fornece essas informações para suas políticas de privacidade de dados.

### O que devo fazer em seguida se receber um erro de token inválido?

Você pode desconectar e reconectar sua conta do Snapchat na página de parceiros do Snapchat. Confirme com seu administrador do Snapchat Business Manager que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canva não pode ser iniciado?

Certifique-se de que sua conta de anúncios do Snapchat se conecte com sucesso ao Braze na página de parceiros do Snapchat. Verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.


