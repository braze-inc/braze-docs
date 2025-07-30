---
nav_title: Usuário caduco
article_title: Usuário caduco
page_order: 4
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para trazer os usuários de volta ao seu app com incentivos baseados em seus engajamentos anteriores."
tool: Canvas
---

# Usuário desistente

> Use o modelo de usuário desistente para lembrar os usuários do valor que sua marca traz para eles e incentive o retorno com ofertas e incentivos interessantes com base nos engajamentos anteriores.

Este artigo o guiará por um caso de uso do modelo **Lapsed User (Usuário caduco)**, que foi projetado para a etapa de retenção e fidelidade do ciclo de vida do usuário. Ao terminar, você terá criado um Canva que incentiva os usuários a retornarem ao seu aplicativo com promoções que variam de acordo com o comportamento deles, como, por exemplo, se eles iniciaram uma sessão no aplicativo após receberem uma mensagem promocional.

## Pré-requisitos

Para usar com êxito o modelo de usuário expirado, é necessário configurar o [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) com os parceiros e públicos que você usa.

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando para a MovieCanon, um serviço de streaming que tem conteúdo exclusivo para filmes e programas. Podemos usar o modelo de usuário expirado para promover vantagens e conteúdo premium para usuários que não visitam nosso app há 30 dias.

Antes de criar o Canva, configuramos a integração [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) para que possamos adicionar dados de usuários do Braze ao público do Google para enviar anúncios com base em disparadores comportamentais, segmentação e muito mais.

Para acessar o modelo de usuário de lapidação, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos de Braze**. Em seguida, ao lado de **Lapsing User**, selecione **Apply Template (Aplicar modelo)**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes 

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que esse Canvas enviará mensagens aos usuários com promoções e fará uma sincronização de público para aqueles que iniciarem uma sessão.
3\. Atualize a descrição para explicar que essa tela contém vantagens e promoções.
4\. Adicione a tag **Lapsing/Retention** para que possamos filtrar esse Canvas na página inicial do Canvas.

![Etapa "Set Up Canvas Details" (Configurar detalhes do Canvas) com o nome do Canvas "Lapsed User - Visit App" (Usuário expirado - Visitar app) e uma breve descrição do Canva]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Etapa 2: Atribua seus eventos de conversão

Atualize o **evento de conversão primária - A** para direcionar os usuários do nosso app (MovieCanon) e deixe **o evento de conversão primária - B** como o padrão para fazer qualquer compra.

![Seção "Atribuir eventos de conversão" com uma conversão primária, mesmo de um usuário iniciando uma sessão em um app específico.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter a programação de entrada como **Agendada** e as opções padrão baseadas em tempo, para que o Canva verifique diariamente se há usuários expirados.

Faremos dois ajustes nesta etapa: 

1. Selecione uma data e hora de início.
2. Selecione os parâmetros de término de **Em uma data específica** e uma data com dois meses de defasagem. Digamos que tenhamos outro Canva de usuário caduco que queremos iniciar depois deste.

![Etapa do "Entry Schedule" para um Canva programado que entra nos usuários em um horário designado.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Etapa 4: Selecionar nosso público-alvo

Manteremos as configurações padrão para o público de entrada, que é definido como usuários que não usam nosso app há mais de 30 dias. Também manteremos os controles de entrada padrão para que os usuários possam entrar novamente no Canva após quatro semanas. Isso significa que toda vez que um usuário não visitar nosso app por mais de 30 dias seguidos, ele será incluído no Canva.

![Etapa "Público-alvo" direcionada a usuários que usaram os apps pela última vez em 30 dias.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Etapa 5: Selecione suas configurações de envio

Manteremos a maioria das configurações de inscrição padrão:

- Envie apenas aos usuários que se inscreveram ou aceitaram receber mensagens ou notificações.
- Aplique nossas [regras de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) para que não sobrecarreguemos nosso público com a quantidade de mensagens que ele recebe. Nesse caso, definimos nosso limite de frequência para limitar o número de campanhas ou etapas do Canva marcadas com "Lapsing/Retention" que um usuário pode receber a duas por semana.
- Não envie mensagens durante o horário de silêncio no fuso local do usuário (das 12h às 8h).

A única configuração que mudaremos é o que fazer quando uma mensagem for disparada durante o horário de silêncio. Em vez de cancelar a mensagem, selecione **Enviar no próximo horário disponível** para que nossos usuários não percam nenhuma promoção.

![Seção "Horário de silêncio" com horário de início às 12 horas e de ponta a ponta às 8 horas.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Etapa 6: Personalize sua tela

Agora, criaremos nosso Canvas personalizando as etapas do modelo:

1. Personalize o primeiro e-mail que será enviado a todos os usuários que não visitam nosso app há mais de 30 dias. Para nosso caso de uso, personalizaremos um e-mail que informa aos usuários que eles desbloquearão novas vantagens quando visitarem nosso app hoje. 

![Etapa do canva Message para um e-mail que diz aos usuários para desbloquear novas vantagens quando visitarem o site hoje.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2\. Personalize o componente da jornada de ação chamado "Start Session?" selecionando nosso app para a jornada **Started Session**. 

![Jornada de ação para sessões iniciadas em um app específico.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3\. Mantenha o padrão para a etapa de divisão de decisão chamada "Sessions?", que define o grupo ">1 Session" como usuários que usaram nosso app mais de uma vez no último dia do calendário.
4\. Personalize a etapa de mensagens para usuários que se enquadram no grupo ">1 sessão". Em nosso caso de uso, agradeceremos aos usuários por visitarem nosso app e destacaremos as vantagens que eles desbloquearam.
5\. Certifique-se de que a sincronização do público do Google esteja configurada na etapa Ad Audience Update, para que atualizemos e sincronizemos os dados de usuários que tiveram várias sessões depois de receber nosso primeiro e-mail.
6\. Mantenha o padrão para o componente [Jornada experimental]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) chamado "Testes A/B". Isso enviará aleatoriamente uma das duas promoções (que personalizaremos na próxima etapa) aos usuários que tiveram menos de duas sessões.
7\. Personalize as duas promoções que serão enviadas aos usuários como parte da jornada experimental. Em nosso caso de uso, faremos uma promoção de 20% para uma inscrição de três meses e a outra uma promoção de 10% para uma inscrição de um mês.

![Etapas do canva com jornadas ramificadas com base em quantas sessões um usuário teve.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Etapa 7: Teste e inicie o Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Launch Canvas**. Agora, nossos usuários que não visitam nosso app há mais de 30 dias e que se inscreveram em nossos canais de envio de mensagens receberão e-mails incentivando-os a voltar!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}

