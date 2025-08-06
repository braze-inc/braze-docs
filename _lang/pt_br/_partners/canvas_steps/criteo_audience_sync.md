---
nav_title: Criteo
article_title: Sincronização do público do Canva com o Criteo
description: "Este artigo de referência abordará como usar o Braze Audience Sync na Criteo a fim de veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais."
page_order: 1
alias: "/audience_sync_criteo/"

Tool:
  - Canvas
---

# Sincronização do público com a Criteo

 

**Os casos de uso comuns para sincronização de público incluem:**

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing
- Criar públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca
- Criação de públicos semelhantes para adquirir novos usuários com mais eficiência

Este recurso oferece às marcas a opção de controlar quais dados primários específicos são compartilhados com a Criteo. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com a Criteo é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta da Braze. <br> 
{% endalert %}

## Pré-requisitos 

Você precisará garantir que os itens a seguir tenham sido criados e/ou concluídos antes de configurar a sincronização do público com a Criteo.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Conta de anúncios da Criteo | [Criteo](https://marketing.criteo.com/) | Uma conta ativa de anúncios da Criteo vinculada à sua marca.<br><br>Certifique-se de que o administrador da Criteo lhe concedeu as permissões apropriadas para acessar o público. |
| [Diretrizes para publicidade da Criteo](https://www.criteo.com/advertising-guidelines/)<br>e<br>[Diretrizes de segurança da marca Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Como cliente ativo da Criteo, você precisa confirmar se está em conformidade com as diretrizes de publicidade e segurança de marca da Criteo antes de lançar qualquer campanha na Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração 

### Etapa 1: conecte-se à Criteo

No dashboard do Braze, acesse **Partner Integrations** > **Technology Partners** e selecione **Criteo**. Em Criteo Audience Export, selecione **Connect Criteo**.

![Página da tecnologia Criteo no Braze que inclui uma seção Visão geral e uma seção Criteo com o botão Criteo conectado.][5]{: style="max-width:80%;"}

Uma página de oAuth da Criteo será exibida para você autorizar a Braze a conceder as permissões relacionadas à integração do Audience Sync.

Depois de confirmar, você voltará à Braze para selecionar as contas de anúncios da Criteo que deseja sincronizar. 

![Uma lista de contas de anúncios disponíveis que você pode conectar à Criteo.][7]{: style="max-width:80%;"}

Depois de se conectar com sucesso, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia da Criteo mostrando as contas de anúncios conectadas com sucesso.][4]{: style="max-width:80%;"}

Sua conexão com a Criteo será aplicada no nível do espaço de trabalho do Braze. Se o administrador da Criteo remover você de sua conta de anúncios da Criteo, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam o Criteo mostrarão erros e o Braze não poderá sincronizar os usuários.

### Etapa 2: Configure seus critérios de entrada no Canva

Ao criar públicos para o rastreamento de anúncios, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canva. Abaixo, listamos algumas opções.

Se você tiver coletado o [IDFA do iOS por meio do SDK do Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro Ads Tracking Enabled (Rastreamento de anúncios ativado). Selecione o valor como "true" para enviar apenas usuários para destinos do Audience Sync nos quais eles optaram por participar.

![][11]

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluir esses dentro dos seus critérios de entrada da canva como um filtro:

![][12]

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte a [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance/).

### Etapa 3: Adicionar uma etapa de sincronização do público com a Criteo

Adicione um componente na sua canva e selecione **Sincronização de público**.

![Fluxo de trabalho das etapas anteriores para adicionar um componente do público da Criteo no Canvas Flow.][9]{: style="max-width:35%;"} ![Fluxo de trabalho das etapas anteriores para adicionar um componente do público da Criteo no Canvas Flow.][10]{: style="max-width:28%;"}

### Etapa 4: Configuração de sincronização

Clique no botão **Público personalizado** para abrir o editor de componentes.

Selecione **Criteo** como parceiro desejado do Audience Sync. 

![][6]

Em seguida, selecione sua conta de anúncio da Criteo desejada. No menu suspenso **Escolha um público novo ou existente**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}
**Crie um Novo Público**<br>
 Em seguida, salve seu público clicando no botão **Criar Público** na parte inferior do editor de etapas.

![Visualização expandida da etapa do canva de público-alvo personalizado. Aqui a conta de anúncios desejada é selecionada, e um novo público é criado.]({% image_buster /assets/img/criteo/criteo3.png %})

Os usuários serão notificados no topo do editor de etapas se o público for criado com sucesso ou se ocorrerem erros durante este processo. Os usuários também podem fazer referência a esse público para remoção de usuários posteriormente na jornada do Canva, pois o público foi criado no modo de rascunho.

![Um alerta que aparece depois que um novo público é criado no componente do canva.]({% image_buster /assets/img/criteo/criteo1.png %})

Ao lançar um canva com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram no componente do Audience Sync.
{% endtab %}
{% tab Sincronização com um público existente %}
**Sincronizar com um Público Existente**<br>
 Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e **adicione ao público**. A Braze adicionará usuários quase em tempo real quando eles entrarem no componente do Audience Sync.

![Visualização expandida da etapa do canva de público-alvo personalizado. Aqui a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar canva

Depois de configurar o Audience Sync para a Criteo, basta iniciar o canva!  Se o seu Canva contiver componentes subsequentes, os usuários avançarão para a próxima etapa da jornada do usuário.

Você pode visualizar o público na Criteo acessando sua conta do Gerenciador de anúncios e selecionando Segmentos na **Biblioteca de públicos** da navegação. Na página **Segments (Segmentos** ), você pode ver o tamanho de cada público depois que ele atinge ~1.000.

![A biblioteca de público mostra o segmento, o ID, a origem, o tipo, o tamanho, o uso atual e a última atualização.][0]

## Considerações sobre sincronização de usuário e limite de frequência

Quando os usuários atingirem a etapa de sincronização do público, o Braze sincronizará esses usuários quase em tempo real, respeitando também os limites de frequência da API da Criteo. 

 Se um cliente do Braze atingir esse limite de frequência, o Braze the Canvas tentará novamente a sincronização por até 13 horas. Se a sincronização não for possível, esses usuários são listados na métrica de Usuários com Erro. 

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| Métrico | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com a Criteo. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com a Criteo. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários atualmente sendo processados pelo Braze para sincronização com a Criteo. |
| Usuários com erro | Número de usuários que não foram sincronizados com a Criteo devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido da Criteo ou se o público foi excluído na Criteo. |
| Saíram do canva | Número de usuários que saíram da canva. Isso ocorre quando a última etapa de um canva é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lembre-se de que haverá uma postergação nos relatórios das métricas de usuários sincronizados e usuários com erro devido à descarga em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes

### 
Você pode simplesmente desconectar e reconectar sua conta da Criteo na página de parceiros da Criteo. Verifique com seu administrador da Criteo se você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### 

 

### 

A Criteo não fornece essas informações devido às suas políticas internas de privacidade de dados.

### 

No momento, você só pode ter 1.000 públicos na sua conta da Criteo.  


[0]: {% image_buster /assets/img/criteo/criteo.png %}
[1]: {% image_buster /assets/img/criteo/criteo1.png %}
[2]: {% image_buster /assets/img/criteo/criteo2.png %}
[3]: {% image_buster /assets/img/criteo/criteo3.png %}
[4]: {% image_buster /assets/img/criteo/criteo4.png %}
[5]: {% image_buster /assets/img/criteo/criteo5.png %}
[6]: {% image_buster /assets/img/criteo/criteo6.png %}
[7]: {% image_buster /assets/img/criteo/criteo7.png %}
[8]: {% image_buster /assets/img/criteo/criteo8.png %}
[9]: {% image_buster /assets/img/criteo/criteo9.png %}
[10]: {% image_buster /assets/img/criteo/criteo10.png %}
[11]: {% image_buster /assets/img/criteo/criteo11.png %}
[12]: {% image_buster /assets/img/criteo/criteo12.png %}
