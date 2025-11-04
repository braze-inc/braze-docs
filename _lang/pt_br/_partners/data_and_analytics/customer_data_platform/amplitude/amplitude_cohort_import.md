---
nav_title: Amplitude
article_title: Importação do coorte Amplitude
description: "Este artigo de referência descreve a funcionalidade de importação de coorte da Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
search_tag: Partner
---

# Importação de coorte de Amplitude

> Este artigo aborda como fazer a importação de coortes de usuários do [Amplitude](https://amplitude.com/) para o Braze. Para saber mais sobre a integração da Amplitude e suas outras funcionalidades, consulte o artigo principal da [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Integração de importação de dados

Qualquer integração que você configurar será contabilizada no volume de pontos de dados da sua conta.

### Etapa 1: Obtenha a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Amplitude**. Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. 

Após a geração, você pode criar outra chave ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard do Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Etapa 2: Configurar a integração do Braze no Amplitude

Na Amplitude, navegue até **Sources & Destinations** > **[nome do projeto]** > **Destinations** > **Braze** (Fontes e destinos > nome do projeto > Destinos > Braze). No prompt exibido, forneça a chave de importação de dados e o endpoint REST da Braze, e clique em **Save** (Salvar).

![]({% image_buster /assets/img/amplitude.png %})

### Etapa 3: Exportar um coorte de Amplitude para o Braze

Primeiro, para exportar usuários da Amplitude para a Braze, crie uma [coorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) de usuários que deseja exportar. O Amplitude pode sincronizar coortes com o Braze usando os seguintes identificadores:
- Alias do usuário
- ID do dispositivo
- ID do usuário (ID externa)

Você pode configurar várias conexões Braze em sua conta Amplitude. Isso permite que você configure uma conexão para sincronizar IDs de usuários para usuários conhecidos e outra para sincronizar IDs de dispositivos para usuários anônimos.

Depois de criar um coorte, clique em **Sync to...** para exportar esses usuários para o Braze.

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

#### Definição da cadência de sincronização

As sincronizações de coorte podem ser definidas como uma sincronização única, programada diariamente ou a cada hora, ou até mesmo em tempo real, com atualizações a cada minuto. Certifique-se de selecionar uma opção que faça sentido para as necessidades de sua empresa e, ao mesmo tempo, tenha em mente o consumo de [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/).

### Etapa 4: Usuários do segmento no Braze

No Braze, para criar um segmento desses usuários, navegue até **Segments (Segmentos** ) em **Engagement (Engajamento)**, nomeie seu segmento e selecione **Amplitude Cohorts (Coortes de Amplitude** ) como filtro. Em seguida, use a opção "includes" (inclui) e escolha a coorte que você criou na Amplitude. 

![No criador de segmentos da Braze, o filtro "amplitude_cohorts" está definido como "includes_value" e "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

Depois de salvar, você pode fazer referência a esse segmento durante a criação do Canva ou da campanha na etapa de direcionamento de usuários.

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.
