---
nav_title: Mixpanel
article_title: Importação de coortes do Mixpanel
description: "Este artigo de referência descreve a funcionalidade de importação de coorte do Mixpanel, uma plataforma de análise de dados, permitindo a importação de coortes do Mixpanel para o Braze para criar segmentos do Braze que podem ser usados para direcionamento de usuários em futuras campanhas ou Canvas do Braze."
page_type: partner
search_tag: Partner
---

# Importação de coorte do Mixpanel

> Este artigo descreve como fazer a importação de coortes de usuários do [Mixpanel](https://mixpanel.com/) para o Braze. Para saber mais sobre a integração do Mixpanel e suas outras funcionalidades, consulte o [artigo principal do Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

## Integração de importação de dados

Qualquer integração que você configurar será contabilizada no volume de pontos de dados da sua conta.

{% alert important %}
Em conformidade com as políticas de retenção de dados do Mixpanel, os eventos enviados antes de 1º de janeiro de 2010 serão removidos durante a importação.
{% endalert %}

### Etapa 1: Obter a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Mixpanel**. Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. 

Após a geração, você pode criar outra chave ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard do Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Etapa 2: Configurar a integração do Braze no Mixpanel

No Mixpanel, navegue até **Data Management > Integrations** (Gerenciamento de dados > Integrações). Em seguida, selecione a guia de integração da Braze e clique em **Connect** (Conectar). No prompt exibido, forneça a chave de importação de dados e o endpoint REST da Braze, e clique em **Continue** (Continuar).

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Etapa 3: Exportar um coorte do Mixpanel para o Braze

No Mixpanel, navegue até **Data Management > Cohorts** (Gerenciamento de dados > Coortes). Selecione a coorte a ser enviada para a Braze e depois **Export to Braze** (Exportar para a Braze). Por fim, selecione uma sincronização única ou uma sincronização dinâmica. A seleção da sincronização dinâmica sincronizará seu coorte do Braze a cada 15 minutos para corresponder aos usuários no Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

### Etapa 4: Usuários do segmento no Braze

No Braze, para criar um segmento desses usuários, acesse **Público** > **Segmentos**, nomeie seu segmento e selecione **Mixpanel_Cohorts** como o filtro. Em seguida, use a opção "includes" (inclui) e escolha a coorte que você criou no Mixpanel. 

![No criador de segmentos da Braze, o filtro de atribuições do usuário "Coortes do Mixpanel" está definido como "inclui" e "Coorte da Braze".]({% image_buster /assets/img_archive/mixpanel1.png %})

Depois de salvar, você pode fazer referência a esse segmento durante a criação do Canva ou da campanha na etapa de direcionamento de usuários.

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.