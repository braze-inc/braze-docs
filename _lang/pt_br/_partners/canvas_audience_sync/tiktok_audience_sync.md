---
nav_title: TikTok
article_title: Sincronização do público do Canva com o TikTok
alias: /tiktok_audience_sync/
description: "Este artigo de referência abordará como usar o Braze Audience Sync no TikTok para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais."
Tool:
  - Canvas
page_order: 7

---

# Sincronização do público com o TikTok

Usando o Braze Audience Sync para o TikTok, as marcas podem optar por adicionar dados de usuários de sua própria integração Braze ao TikTok Audiences para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook, etc.) em um Braze Canvas. 

**Os casos de uso comuns para a sincronização do público incluem**:

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários menos responsivos para outros canais de marketing
- Criar públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca
- Criação de públicos Actalike para adquirir novos usuários com mais eficiência

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o TikTok. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o TikTok é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta da Braze.
{% endalert %}

## Pré-requisitos

É necessário garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar a etapa do público do TikTok no Canva.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Conta do TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Uma ferramenta centralizada para gerenciar os ativos do TikTok da sua marca (como contas de anúncios, páginas, apps). |
| Conta de anúncios do TikTok | [TikTok](https://ads.tiktok.com/) | Uma conta ativa de anúncios do TikTok vinculada à conta do Business Center de sua marca.<br><br>Certifique-se de que o administrador do TikTok Business Center tenha concedido a você permissões de administrador para as contas de anúncios do TikTok que você planeja usar com o Braze. |
| Termos e políticas do TikToK | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Concordar em cumprir todos os termos, políticas, diretrizes e documentação exigidos pela TikTok relacionados ao seu uso do Pinterest Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência a eles, que podem incluir: os Termos de Serviço Comerciais, os Termos de Publicidade, a Política de Privacidade, os Termos de Público Personalizado, os Termos de Serviço do Desenvolvedor, o Contrato de Compartilhamento de Dados do Desenvolvedor, as Políticas de Publicidade, as Diretrizes da Marca e as Diretrizes da Comunidade. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração 

### Etapa 1: Conecte-se ao TikTok

No dashboard do Braze, acesse **Partner Integrations** > **Technology Partners** e selecione **TikTok**. Sob a Sincronização de Público do TikTok, selecione **Conectar TikTok**.

![A página da tecnologia TikTok no Braze inclui uma seção de visão geral e uma seção de sincronização do público do TikTok com o botão Connected TikTok.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Em seguida, você será redirecionado para a página OAuth do TikTok para autorizar o Braze para o gerenciamento de contas de anúncios e o gerenciamento de público. Depois de selecionar **Confirm (Confirmar**), você será redirecionado de volta ao Braze para selecionar com quais contas de anúncios do TikTok você deseja sincronizar. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Quando a conexão for bem-sucedida, você retornará à página do parceiro. Aqui, você pode ver quais contas estão conectadas e desconectar contas existentes.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Sua conexão com o TikTok será aplicada no nível do grupo de app do Braze. Se o administrador do TikTok remover você do seu TikTok Business Center ou do acesso às contas TikTok conectadas, o Braze detectará um token inválido. Como resultado, suas telas ativas que usam os componentes do público do TikTok mostrarão erros, e o Braze não poderá sincronizar os usuários.

### Etapa 2: Adicionar um componente do público do TikTok no Canvas Flow

Adicione um componente ao seu canva e selecione **Audience Sync**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração de sincronização

Clique no botão **Público personalizado** para abrir o editor de componentes.

Selecione **TikTok** como parceiro desejado do Audience Sync.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione a conta de anúncios do TikTok desejada. No menu suspenso **Choose a New or Existing Audience (Escolher um público novo ou existente** ), digite o nome de um público novo ou existente.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience (Adicionar usuários ao público**) e selecione os campos que deseja sincronizar com o TikTok. Em seguida, salve seu público clicando no botão **Create Audience (Criar público** ) na parte inferior do editor de etapas.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Os usuários serão notificados na parte superior do editor de etapas se o público for criado com êxito ou se ocorrerem erros durante esse processo. Os usuários também podem fazer referência a esse público para remoção de usuários posteriormente na jornada do Canva, pois o público foi criado no modo de rascunho.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Ao lançar um canva com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram na etapa do público.

{% endtab %}
{% tab Sincronização com um público existente %}

**Sincronização com um público existente**<br>
O Braze também oferece a capacidade de adicionar usuários aos públicos existentes do TikTok para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e **adicione ao público**. O Braze adicionará usuários quase em tempo real quando eles entrarem na etapa do TikTok Audience.

![Visualização expandida da etapa do canva de público-alvo personalizado. Nesta etapa, a conta de anúncios desejada e o público existente são selecionados.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar canva
Depois de configurar seu componente TikTok Audience, basta iniciar o Canva! Um novo público será criado, e os usuários que passarem pelo componente TikTok Audience serão transferidos para esse público no TikTok. Se o seu Canva contiver componentes subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

Você pode visualizar o público no TikTok entrando em sua **conta do Gerenciador de Anúncios** e selecionando **Públicos** no menu suspenso **Ativos**. Na página **Audience (Público** ), você pode ver o tamanho de cada público depois que ele atinge ~1.000.

![Página do TikTok listando as seguintes métricas para o público em questão.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Considerações sobre sincronização de usuários e limite de frequência

Quando os usuários atingirem a etapa de sincronização do público, a Braze sincronizará esses usuários quase em tempo real, respeitando os limites de frequência da API de marketing do TikTok. Isso significa que o Braze tentará agrupar e processar o máximo de usuários a cada 5 segundos antes de enviar esses usuários ao TikTok.

O limite de frequência da API de segmento do TikTok determina que não haja mais de 50 consultas por segundo e 10 mil usuários por solicitação. Se um cliente da Braze atingir este limite de frequência, o canva tentará sincronizar novamente por até ~13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored (Usuários com erro).

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| Métrico | Descrição |
| ------ | ----------- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com o TikTok. |
| Avançaram para a etapa seguinte | Número de usuários que avançaram para o próximo componente, se houver. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o TikTok. Note que isso não equivale a usuários correspondidos no TikTok. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários que estão sendo processados pelo Braze para sincronização com o TikTok. |
| Usuários com erro | Número de usuários que não foram sincronizados com o TikTok devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token TikTok inválido ou se o público foi excluído no TikTok. |
| Saíram do canva | Número de usuários que saíram do Canva. Isso ocorre quando a última etapa de um Canva é um componente de sincronização do público. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lembre-se de que haverá uma postergação nos relatórios das métricas de usuários sincronizados e usuários com erro devido à descarga em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes

### O que devo fazer em seguida se receber um erro de token inválido?

Você pode desconectar e reconectar sua conta do TikTok na página de parceiros do TikTok. Verifique com seu administrador do TikTok Business Center se você tem as permissões apropriadas para a conta de anúncios que deseja sincronizar.

### Por que meu Canva não pode ser iniciado?

Confirme que sua conta do TikTok se conecta com sucesso ao Braze na página do parceiro do TikTok. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como posso saber se houve correspondência entre os usuários depois de passá-los para o TikTok?

O TikTok não fornece essas informações para suas políticas de privacidade de dados.

### Quanto tempo levará para que meus públicos sejam preenchidos no TikTok?

O tamanho do público será atualizado dentro de 24 a 48 horas na página Públicos no Gerenciador de Anúncios do TikTok.

### Qual é o número máximo de públicos que posso ter em minha conta de anúncios do TikTok?

Você pode ter até 400 públicos por conta de anúncio do TikTok.

### Por que o tamanho do meu público ou a taxa de correspondência no TikTok é maior do que a dos usuários sincronizados no Braze com o Audience Sync?

Isso ocorre porque, no TikTok, um ID pode estar associado a vários usuários do TikTok. Isso ocorre com mais frequência quando os clientes usam IDs de anúncios móveis (iOS IDFA e Android GAID) porque um dispositivo pode ter vários usuários do TikTok registrados. 

Além disso, o TikTok também conta os usuários do Pangle como usuários correspondidos, o que, em alguns casos, pode resultar em uma taxa de correspondência elevada. No entanto, quando se usa o público para a entrega de anúncios, o tamanho real do público entregável pode não ser tão alto quanto o tamanho do usuário correspondente, pois depende do posicionamento e de outros fatores de influência.


