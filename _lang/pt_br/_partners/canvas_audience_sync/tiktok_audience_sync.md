---
nav_title: TikTok
article_title: Sincronização do público do Canvas com o TikTok
alias: /tiktok_audience_sync/
description: "Este artigo de referência abordará como usar o Braze Audience Sync no TikTok para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais."
Tool:
  - Canvas
page_order: 8

---

# Sincronização do público com o TikTok

Usando o Braze Audience Sync para o TikTok, as marcas podem optar por adicionar dados de usuários de sua própria integração Braze ao TikTok Audiences para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook, etc.) em um canva da Braze. 

**Os casos de uso comuns para a sincronização do público incluem**:

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários menos responsivos a outros canais de marketing
- Criar públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca
- Criação de públicos Actalike para adquirir novos usuários com mais eficiência

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o TikTok. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o TikTok é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta da Braze.
{% endalert %}

## Pré-requisitos

É necessário garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar a etapa do público do TikTok no Canvas.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Conta do TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Uma ferramenta centralizada para gerenciar os ativos do TikTok da sua marca (como contas de anúncios, páginas, apps). |
| Conta de anúncios do TikTok | [TikTok](https://ads.tiktok.com/) | Uma conta ativa de anúncios do TikTok vinculada à conta do Business Center da sua marca.<br><br>Certifique-se de que o administrador do TikTok Business Center tenha concedido a você permissões de administrador para as contas de anúncios do TikTok que você planeja usar com a Braze. |
| Termos e políticas do TikTok | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Concordar em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo TikTok relacionados ao seu uso do Pinterest Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência a eles, que podem incluir: os Termos de Serviço Comerciais, os Termos de Publicidade, a Política de Privacidade, os Termos de Público Personalizado, os Termos de Serviço do Desenvolvedor, o Contrato de Compartilhamento de Dados do Desenvolvedor, as Políticas de Publicidade, as Diretrizes da Marca e as Diretrizes da Comunidade. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração 

### Etapa 1: Conecte-se ao TikTok

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para conectar o TikTok à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Partner Integrations** > **Technology Partners** e selecione **TikTok**. Em TikTok Audience Sync, selecione **Connect TikTok**.

![A página de tecnologia do TikTok na Braze inclui uma seção de Visão Geral e uma seção de TikTok Audience Sync com o botão TikTok Conectado.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Em seguida, você será redirecionado para a página OAuth do TikTok para autorizar a Braze para o gerenciamento de contas de anúncios e o gerenciamento de público. Depois de selecionar **Confirm**, você será redirecionado de volta à Braze para selecionar com quais contas de anúncios do TikTok você deseja sincronizar. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Quando a conexão for bem-sucedida, você retornará à página do parceiro. Aqui, você pode ver quais contas estão conectadas e desconectar contas existentes.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Sua conexão com o TikTok será aplicada no nível do grupo de apps da Braze. Se o administrador do TikTok remover você do seu TikTok Business Center ou do acesso às contas TikTok conectadas, a Braze detectará um token inválido. Como resultado, seus canvas ativos que usam os componentes do público do TikTok mostrarão erros, e a Braze não poderá sincronizar os usuários.

### Etapa 2: Adicionar um componente do público do TikTok no Canvas

Adicione um componente ao seu canva e selecione **Audience Sync**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração de sincronização

Clique no botão **Custom Audience** para abrir o editor de componentes.

Selecione **TikTok** como parceiro desejado do Audience Sync.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione a conta de anúncios do TikTok desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Create a New Audience %}

**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience** e selecione os campos que deseja sincronizar com o TikTok. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com êxito ou se ocorrerem erros. Os usuários podem referenciar esse público para remoção de usuários mais tarde na jornada do canva, porque o público foi criado no modo de rascunho.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Ao lançar um canva com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram na etapa do público.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Sincronização com um público existente**<br>
A Braze também oferece a capacidade de adicionar usuários aos públicos existentes do TikTok para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará usuários quase em tempo real quando eles entrarem na etapa do TikTok Audience.

![Visualização expandida da etapa do canva de público personalizado. Aqui, a conta de anúncios desejada e o público existente são selecionados.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar o canva
Depois de configurar seu componente TikTok Audience, basta lançar o canva! Um novo público será criado, e os usuários que passarem pelo componente TikTok Audience serão transferidos para esse público no TikTok. Se o seu canva contiver componentes subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

Você pode visualizar o público no TikTok entrando em sua **conta do Ads Manager** e selecionando **Audiences** no menu suspenso **Assets**. Na página **Audience**, você pode ver o tamanho de cada público depois que ele atinge &#126;1.000.

![Página do TikTok listando as seguintes métricas para o público em questão.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Considerações sobre sincronização de usuários e limite de taxa

À medida que os usuários atingem a etapa de sincronização do público, a Braze os sincroniza quase em tempo real, respeitando os limites de taxa da API de marketing do TikTok. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao TikTok.

O limite de taxa da API de segmento do TikTok não permite mais do que 50 consultas por segundo e 10 mil usuários por solicitação. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por até &#126;13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Usuários com erro.

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente Audience Sync.

| Métrica | Descrição |
| ------ | ----------- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com o TikTok. |
| Avançaram para a etapa seguinte | Número de usuários que avançaram para o próximo componente, se houver. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o TikTok. Note que isso não equivale a usuários correspondidos no TikTok. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários que estão sendo processados pela Braze para sincronização com o TikTok. |
| Usuários com erro | Número de usuários que não foram sincronizados com o TikTok devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token TikTok inválido ou se o público foi excluído no TikTok. |
| Saíram do Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa de um canva é um componente de sincronização do público. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lembre-se de que haverá uma postergação nos relatórios das métricas de usuários sincronizados e usuários com erro devido à descarga em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes

### O que devo fazer em seguida se receber um erro de token inválido?

Você pode desconectar e reconectar sua conta do TikTok na página de parceiros do TikTok. Verifique com seu administrador do TikTok Business Center se você tem as permissões apropriadas para a conta de anúncios que deseja sincronizar.

### Por que meu canva não pode ser lançado?

Confirme que sua conta do TikTok se conecta com sucesso à Braze na página do parceiro do TikTok. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como posso saber se houve correspondência entre os usuários depois de passá-los para o TikTok?

O TikTok não fornece essas informações devido às suas políticas de privacidade de dados.

### Quanto tempo levará para que meus públicos sejam preenchidos no TikTok?

O tamanho do público será atualizado dentro de 24 a 48 horas na página Audiences no Ads Manager do TikTok.

### Qual é o número máximo de públicos que posso ter em minha conta de anúncios do TikTok?

Você pode ter até 400 públicos por conta de anúncios do TikTok.

### Por que o tamanho do meu público ou a taxa de correspondência no TikTok é maior do que a dos usuários sincronizados na Braze com o Audience Sync?

Isso ocorre porque, no TikTok, um ID pode estar associado a vários usuários do TikTok. Isso acontece com mais frequência quando os clientes usam IDs de anúncios móveis (iOS IDFA e Android GAID), porque um dispositivo pode ter vários usuários do TikTok conectados. 

Além disso, o TikTok também conta os usuários do Pangle como usuários correspondidos, o que, em alguns casos, pode resultar em uma taxa de correspondência elevada. No entanto, quando se usa o público para a entrega de anúncios, o tamanho real do público entregável pode não ser tão alto quanto o tamanho do usuário correspondente, pois depende do posicionamento e de outros fatores de influência.

### Por que estou recebendo um e-mail com o assunto "O público não existe para o Canvas"?

Isso pode ocorrer se o público que você escolheu para sincronizar não for um público de streaming (por exemplo, se for um público semelhante ou um público de arquivo de usuário). Tente criar um novo público por meio da etapa do canva do Braze Audience Sync.