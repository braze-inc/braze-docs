---
nav_title: LinkedIn
article_title: Sincronização do público do Canva com o LinkedIn
alias: /linkedin_audience_sync/
description: "Este artigo de referência abordará como usar o Braze Audience Sync no LinkedIn a fim de veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais."
Tool:
  - Canvas
page_order: 4

---

# Sincronização do público com o LinkedIn

Usando o Braze Audience Sync no LinkedIn, as marcas podem adicionar dados de usuários de sua integração da Braze às listas de clientes do LinkedIn para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Braze Canvas com base nos dados de seus usuários agora pode disparar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

**Os casos de uso comuns para a sincronização do público incluem**:

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing
- Criar públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o LinkedIn. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
O Audience Sync to LinkedIn está atualmente na versão beta. Entre em contato com o gerente da sua conta Braze se quiser participar da versão beta.
{% endalert %}

## Pré-requisitos

Certifique-se de que os seguintes itens tenham sido criados, concluídos ou aceitos antes de configurar a etapa do LinkedIn Audience Sync no canva.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Conta de anúncios do LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Uma conta ativa de anúncios do LinkedIn vinculada à sua marca.<br><br>Certifique-se de que aceitou todos os termos e condições relevantes do LinkedIn para acessar e usar essa conta e que seu administrador do LinkedIn lhe concedeu as permissões apropriadas para gerenciar públicos. |
| Termos e políticas do LinkedIn | LinkedIn | Concorde em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo LinkedIn relacionados ao seu uso do LinkedIn Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir os do LinkedIn: Termos de Serviços, Contrato de Anúncios, Contrato de Processamento de Dados e Diretrizes da Comunidade Profissional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: Conecte-se ao LinkedIn

No dashboard da Braze, acesse **Parceiros de tecnologia** e selecione **LinkedIn**. Na seção **Sincronização de Público do LinkedIn**, selecione **Conectar LinkedIn**.

![A página de tecnologia do LinkedIn no Braze inclui uma seção de visão geral e uma seção de sincronização de público do LinkedIn com o botão LinkedIn conectado.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Em seguida, você será redirecionado para a página do LinkedIn OAuth para autorizar a Braze a conceder as permissões relacionadas à integração do Audience Sync. Depois de selecionar **Confirm (Confirmar)**, você será redirecionado de volta ao Braze para selecionar com quais contas de anúncios do LinkedIn você deseja sincronizar. 

!["Braze Self Service" está selecionado como a conta de anúncio a ser conectada.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Após a conexão bem-sucedida, você retornará à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma conta do LinkedIn conectada com sucesso.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Sua conexão com o LinkedIn será aplicada no nível do espaço de trabalho do Braze. Se o administrador do LinkedIn remover você de sua conta de anúncios do LinkedIn, a Braze detectará um token inválido. Como resultado, seus Canvas ativos usando o LinkedIn mostrarão erros e o Braze não poderá sincronizar os usuários.

### Etapa 2: Configure seus critérios de entrada no Canva

Ao criar públicos para o rastreamento de anúncios, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canva. Abaixo, listamos algumas opções. 

Se você coletou o [IDFA do iOS por meio do SDK do Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection), poderá usar o filtro **Ads Tracking Enabled (Rastreamento de anúncios ativado** ). Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync que eles aceitaram. 

![Um público de entrada com o filtro "A capacitação do rastreamento de anúncios é verdadeira".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluir esses dentro dos seus critérios de entrada da canva como um filtro:

![Um Canva com um público de entrada de "opted_in_marketing" é igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte a [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance/).

### Etapa 3: Adicionar uma etapa de sincronização de público com o LinkedIn

Adicione um componente em seu canva e selecione Audience Sync. Clique no botão **Público personalizado** para abrir o editor de componentes.

![O editor do Canvas com a lista de componentes disponíveis.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![O componente Audience Sync selecionado.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Etapa 4: Configuração de sincronização

Selecione **LinkedIn** como o parceiro desejado do Audience Sync.

![Os detalhes de "Set up Audience Sync" (Configurar sincronização do público) com vários parceiros para escolher.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Em seguida, selecione a conta de anúncios do LinkedIn desejada. No menu suspenso **Choose a New or Existing Audience (Escolher um público novo ou existente** ), digite o nome de um público novo ou existente.

![Sincronização do público com o LinkedIn com o Braze selecionado como a conta do anúncio.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience (Adicionar usuários ao público**) e selecione os campos que deseja sincronizar com o LinkedIn. Para essa integração, no momento, oferecemos suporte aos seguintes itens: 
- E-mail
- Nome e sobrenome
- GAID para Android

Em seguida, salve seu público clicando no botão **Create Audience (Criar público)** na parte inferior do editor de etapas.

![Um exemplo de público "leads" com a conta de anúncio Braze selecionada, público "leads", a ação de adicionar usuários ao público, e e-mail, GAID do Android e primeiro e último nome como campos para correspondência.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Os usuários serão notificados no topo do editor de etapas se o público for criado com sucesso ou se ocorrerem erros durante este processo. Os usuários também podem fazer referência a esse público para remoção de usuários posteriormente na jornada do Canva, pois o público foi criado no modo de rascunho.

![Confirmação de que o público "leads" foi criado.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Ao lançar um canva com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram no componente do Audience Sync.

{% endtab %}
{% tab Sincronização com um público existente %}

**Sincronização com um público existente**<br>
O Braze também oferece a capacidade de adicionar usuários a públicos existentes no LinkedIn para confirmar que esses públicos estão atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e **adicione ao público**. A Braze adicionará usuários quase em tempo real quando eles entrarem no componente do Audience Sync.

![Visualização expandida da etapa do canva de público-alvo personalizado. Nesta etapa, a conta de anúncios desejada e o público existente são selecionados.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar canva

Depois de configurar o Audience Sync para o LinkedIn, basta iniciar o canva! O novo público será criado, e os usuários que passarem pela etapa Audience Sync serão transferidos para esse público no LinkedIn. Se o seu Canva contiver componentes subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

É possível visualizar o público no LinkedIn acessando sua conta de anúncios e selecionando **Públicos** na seção **Ativos** da navegação. Na página **Audiences (Públicos** ), você pode ver o tamanho de cada público após atingir mais de 300 membros.

![Página do LinkedIn listando as seguintes métricas para o público em questão.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Considerações sobre sincronização de usuários e limite de frequência

Quando os usuários atingirem a etapa de sincronização do público, o Braze sincronizará esses usuários quase em tempo real, respeitando os limites de frequência da API do LinkedIn. Na prática, a Braze tentará agrupar e processar o maior número de usuários a cada 5 segundos antes de enviar esses usuários para o LinkedIn.

O limite de frequência da API do LinkedIn afirma que não são permitidas mais de dez consultas por segundo e 100.000 usuários por solicitação. Se um cliente Braze atingir este limite de frequência, Braze o canva irá tentar a sincronização por até cerca de 13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored (Usuários com erro).

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| MÉTRICO | DESCRIÇÃO |
| ------ | ----------- | 
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com o LinkedIn. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o LinkedIn. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários atualmente sendo processados pelo Braze para sincronização no LinkedIn. |
| Usuários com erro | Número de usuários que não foram sincronizados com o LinkedIn devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do LinkedIn ou se o público foi excluído no LinkedIn. |
| Saíram do canva | Número de usuários que saíram da canva. Isso ocorre quando a última etapa de um canva é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lembre-se de que haverá uma postergação nos relatórios das métricas de usuários sincronizados e usuários com erro devido à descarga em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

{% alert important %}
O LinkedIn fornece métricas adicionais sobre as taxas de correspondência em sua plataforma. Para revisar a correspondência do seu público específico de Sincronização, selecione as métricas da etapa de Sincronização do Público para ir para a página **Detalhes da Etapa do Canva**.
<br><br>
Selecione o parceiro como **LinkedIn**, sua conta de anúncios e o público para ver o tamanho do público e a taxa de correspondência do LinkedIn.

![Um exemplo de métricas de etapa de sincronização de público com 10.000 usuários inseridos.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Perguntas frequentes

### Quanto tempo levará para que os tamanhos do público sejam preenchidos no LinkedIn?

Pode haver uma demora de até 48 horas para visualizar os públicos em sua conta do LinkedIn.

### Qual é o tamanho mínimo do público para o LinkedIn preencher sua conta de anúncios?

O público deve incluir pelo menos 300 membros para preencher o tamanho do público em sua conta do LinkedIn.

### O que devo fazer em seguida se receber um erro de token inválido?

Você pode desconectar e reconectar sua conta do LinkedIn na página de parceiros do LinkedIn. Confirme com seu administrador do LinkedIn que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canva não pode ser iniciado?

Confirme se sua conta de anúncios do LinkedIn foi conectada com sucesso ao Braze na página de parceiros do LinkedIn. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como posso saber se houve correspondência entre os usuários depois de passá-los para o LinkedIn?

O LinkedIn fornece informações sobre as taxas de correspondência em seu dashboard. Você pode revisá-lo no LinkedIn na seção **Públicos**. Você pode revisar a taxa de correspondência do seu público do LinkedIn nos detalhes da etapa do Canva da etapa de sincronização do público.

### Quantos públicos o LinkedIn pode suportar?

Atualmente, não há limite para o número de públicos em sua conta de anúncios do LinkedIn.

### Por que um segmento está preso no status BUILDING e não é atualizado?

Um segmento é considerado não utilizado e definido como ARQUIVADO depois de não ser usado continuamente por 30 dias em um rascunho ou em uma campanha ativa. Por esse motivo, um segmento pode parecer "preso" em COMPILANDO quando as atualizações são transmitidas para um segmento ARQUIVADO, empurrando-o para o estado COMPILANDO e, logo antes de ser arquivado novamente, novas atualizações são transmitidas para o segmento não utilizado.


