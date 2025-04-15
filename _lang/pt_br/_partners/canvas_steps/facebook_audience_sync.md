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

Usando o Braze Audience Sync to Facebook, as marcas podem optar por adicionar os dados de seus próprios usuários de sua própria integração do Braze ao Facebook Custom Audiences para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS ou webhook) em um Braze Canvas com base nos dados de seu usuário agora pode ser usado para disparar um anúncio para esse usuário no Facebook usando públicos personalizados.

**Casos de uso comuns para sincronização de Audiências Personalizadas incluem**:

- Direcionamento de usuários de alto valor por meio de múltiplos canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.
- Criação de públicos semelhantes para adquirir novos usuários de forma mais eficiente.

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Facebook. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Pré-requisitos

Você precisará confirmar que os seguintes itens foram criados e concluídos antes de configurar sua etapa de público do Facebook no canva. 

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps). |
| Conta de Anúncio do Facebook | [Facebook][2] | Uma conta de anúncio ativa do Facebook vinculada ao gerente de negócios da sua marca.<br><br>Certifique-se de que o administrador do seu Facebook business manager tenha concedido a você permissões de "Gerenciar campanhas" ou "Gerenciar contas de anúncios" para as contas de anúncios do Facebook que você planeja usar com a Braze. Além disso, verifique se você aceitou os termos e condições de sua conta de anúncios. |
| Termos de públicos personalizados do Facebook | [Facebook][3] | Aceite os Termos de Públicos Personalizados do Facebook para suas contas de anúncios do Facebook que você planeja usar com o Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: conecte-se ao Facebook

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**. Em Facebook Audience Export, selecione **Connect Facebook**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar **Parceiros de Tecnologia** em **Integrações**.
{% endalert %}

![Página de tecnologia do Facebook no Braze que inclui uma seção de Visão geral e uma seção de Exportação de público do Facebook com o botão Conectado ao Facebook.][4]{: style="max-width:70%;"}

Uma janela de diálogo oAuth do Facebook aparecerá para autorizar a Braze a criar Públicos Personalizados em suas contas de anúncios do Facebook.

![A primeira caixa de diálogo do Facebook solicitando para "Conectar como X", em que X é seu nome de usuário do Facebook.][6]{: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios para suas contas de anúncios.][5]{: style="max-width:40%;"}

Depois de vincular o Braze à sua conta do Facebook, você poderá selecionar quais contas de anúncios deseja sincronizar no seu espaço de trabalho do Braze. 

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Facebook.][7]{: style="max-width:70%;"}

Depois de se conectar com sucesso, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.][8]{: style="max-width:70%;"}

Sua conexão com o Facebook será aplicada no nível do espaço de trabalho do Braze. Se o administrador do Facebook remover você do seu Facebook Business Manager ou o acesso às contas do Facebook conectadas, a Braze detectará um token inválido. Como resultado, seus canvas ativos usando componentes do público do Facebook mostrarão erros, e o Braze não poderá sincronizar usuários. 

{% alert important %}
Para clientes que já passaram pelo processo de Revisão de App do Facebook para [Gerenciamento de Anúncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Acesso Padrão de Gerenciamento de Anúncios](https://developers.facebook.com/docs/marketing-api/access#standard), seu Token de Usuário do Sistema ainda será válido para o componente público do Facebook. Você não poderá editar ou revogar o Token de Usuário do Sistema do Facebook através da página de parceiro do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir seu Token de Usuário do Sistema do Facebook dentro do seu espaço de trabalho do Braze. 

<br><br>A configuração do oAuth do Facebook também se aplicará às [exportações do Facebook via Segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Etapa 2: Aceitar os termos de serviço de públicos personalizados

Antes de construir sua canva, você deve primeiro aceitar os termos de serviço de públicos personalizados do Facebook. Seus termos de serviço podem ser encontrados no seguinte link:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### Etapa 3: adicione um componente de público do Facebook no Canvas Flow

Adicione um componente na sua canva e selecione **público do Facebook**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Etapa 4: Configuração de sincronização

Clique no botão **Público personalizado** para abrir o editor de componentes.

Selecione **Facebook** como o parceiro de sincronização de público desejado.

![][19]{: style="max-width:80%;"}

Selecione a conta de anúncio do Facebook desejada. No menu suspenso **Escolher um Público Novo ou Existente**, digite o nome de um novo ou existente público. 

{% tabs %}
{% tab Criar um novo público %}
**Crie um Novo Público**<br>
Digite um nome para o novo público personalizado, selecione **Adicionar Usuários ao Público** e selecione quais campos você gostaria de sincronizar com o Facebook. Em seguida, salve seu público clicando no botão **Criar Público** na parte inferior do editor de etapas.

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Em seguida, salve seu público clicando no botão "Criar público" na parte inferior do editor de etapas. Os usuários serão notificados no topo do editor de etapas se o público for criado com sucesso ou se erros surgirem durante este processo. Os usuários também podem fazer referência a esse público para remoção de usuários posteriormente na jornada do Canva, pois o público foi criado no modo de rascunho.

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

Quando você lança uma canva com um novo público, a Braze criará o novo público personalizado ao lançar a canva e, subsequentemente, sincronizará os usuários em quase tempo real à medida que eles entrarem na etapa de sincronização de público.

{% endtab %}
{% tab Sincronização com um público existente %}
**Sincronizar com um Público Existente**<br>
A Braze também oferece a capacidade de adicionar ou remover usuários de audiências personalizadas existentes do Facebook para confirmar que essas audiências estão atualizadas. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e escolha se deseja **Adicionar ao Público** ou **Remover do Público**. Em seguida, a Braze adiciona ou remove usuários em tempo quase real à medida que eles entram na etapa do público do Facebook. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

É importante notar que o Facebook proíbe a remoção de usuários de públicos personalizados muito pequenos (geralmente menos de 1.000). Como resultado, a Braze não poderá sincronizar usuários para uma etapa de Remover do público até que o público atinja o tamanho apropriado.

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar canva

Depois de configurar seu componente de público do Facebook, basta iniciar o canva. O novo público personalizado será criado, e os usuários que passarem pelo componente público do Facebook serão incluídos neste público personalizado no Facebook. Se a sua canva contiver componentes subsequentes, seus usuários avançarão para a próxima etapa em sua jornada de usuário.

A guia **Histórico** do público personalizado no Gerenciador de Público do Facebook refletirá o número de usuários enviados para o público do Braze. Se um usuário reentrar na etapa, ele será enviado para o Facebook novamente.

![Detalhes do público e a guia de histórico para um determinado público do Facebook, com uma tabela de histórico do público com colunas de atividade, detalhes da atividade, itens alterados e data e hora.][9]{: style="max-width:80%;"}

## Migração para contas de trabalho da Meta

A partir de julho de 2023, a Meta lançou as contas de trabalho da Meta para um pequeno conjunto de empresas interessadas em adotar esse novo tipo de conta. Se você tiver uma Conta Comercial integrada com a Braze, certifique-se de desconectar e reconectar à [página de parceiro do Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) com sua Conta Comercial para preservar essa implementação e não interromper nenhum canvas ativo.

## Considerações sobre sincronização de usuário e limite de frequência
 
À medida que os usuários alcançam a Etapa de Sincronização de Público, a Braze sincronizará esses usuários em quase tempo real, respeitando também os limites de taxa da API de Marketing do Facebook. O que isso significa na prática é que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviar esses usuários para o Facebook. 

O limite de frequência da API de Marketing do Facebook estabelece no máximo ~190 mil solicitações de API para cada conta de anúncio em um período de 1 hora. Se um cliente do Braze atingir esse limite de frequência, o Braze the Canvas tentará novamente a sincronização por até 13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored (Usuários com erro).

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
Lembre-se de que haverá uma postergação nos relatórios das métricas de usuários sincronizados e usuários com erro devido à descarga em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}   

## Solução de problemas

{% details O que devo fazer a seguir se receber um erro de token inválido? %}
Você pode simplesmente desconectar e reconectar sua conta do Facebook na página de parceiros do Facebook. Confirme com o administrador do Facebook Business Manager que você tem as permissões apropriadas para a conta de anúncio que deseja sincronizar.
{% enddetails %}

{% details Por que meu canva não pode ser iniciado? %}
- Certifique-se de que o token de usuário do sistema esteja autenticado e tenha acesso às contas de anúncios desejadas no Facebook Business Manager.
- Certifique-se de ter selecionado uma conta de anúncios, inserido um nome para o novo público personalizado e selecionado os campos correspondentes.
- Você pode ter atingido o limite de 500 públicos personalizados no Facebook. Acesse o Gerenciador de público do Facebook para excluir alguns desnecessários antes de criar novos Públicos Personalizados usando o canva.
{% enddetails %}

{% details Como faço para saber se houve correspondência dos usuários depois de passá-los para o Facebook? %}
O Facebook não fornece essas informações por motivos de privacidade.
{% enddetails %}

{% details A Braze suporta públicos personalizados baseados em valor? %}
No momento, os públicos personalizados baseados em valor não são suportados pela Braze. Se você estiver interessado em sincronizar esses tipos de públicos personalizados, envie [comentários sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Como resolvo um problema com a sincronização de um público personalizado semelhante baseado em valor? %}

Neste momento, públicos personalizados semelhantes baseados em valor não são suportados pela Braze. Se você tentar sincronizar com este público, isso pode causar erros para sua etapa de Sincronização de Público. Para resolver isso, siga estas etapas:

1. Acessar seu dashboard do Facebook Ad Manager e selecionar **Audiences**.
2. Selecione **Criar público** > **Público personalizado**.
3. Selecione **Lista de clientes**.
4. Faça upload do seu CSV ou lista sem a coluna **Value**. Selecione **No, continue with a customer list that doesn't include customer value** (Não, continue com uma lista de clientes que não inclui o valor do cliente).
5. Conclua a criação do seu público personalizado.
6. Na Braze, atualize a etapa Facebook Audience Sync com o público personalizado que você criou.
{% enddetails %}

{% details Recebi um e-mail relacionado aos termos de serviço de público personalizado do Facebook. O que devo fazer para resolver isso? %}
Para usar o público do Facebook, você precisa aceitar estes termos do contrato de serviço. 

- Se a sua conta de anúncios estiver diretamente associada à sua conta pessoal do Facebook, você poderá aceitar os Termos de Serviço na sua conta pessoal aqui: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=ACCOUNT_ID`.
- Se a sua conta de anúncios estiver vinculada à conta do Business Manager da sua empresa, você precisará aceitar os Termos de Serviço na sua conta do Business Manager aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID`.

Depois de aceitar os termos de serviço do público personalizado do Facebook, faça o seguinte:
1. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
2. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva.
A partir daí, a Braze conseguirá sincronizar os usuários assim que eles chegarem à etapa de público do Facebook.
{% enddetails %}


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
