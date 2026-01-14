---
nav_title: Heap
article_title: "Análise de dados de pilha"
description: "Este artigo de referência descreve como usar o Braze Currents para analisar automaticamente eventos de engajamento com o Heap, uma plataforma de insights digitais, que permite a importação de dados do Heap para o Braze, a criação de coortes de usuários e a exportação de dados do Braze para o Heap para criar segmentos."
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Análise de dados de pilha

> Este artigo descreve como enviar automaticamente eventos de engajamento da Braze para o Heap para análise. Para saber mais sobre a integração do Heap e suas outras funcionalidades, como [a sincronização de coortes do Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration) com a Braze, consulte o [artigo principal sobre o Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/).

## Integração de exportação de dados

Use o Braze Currents para enviar automaticamente eventos de engajamento (por exemplo, envio de e-mail ou de push) da Braze para o Heap para análise.

### Etapa 1: Obter credenciais de Heap

Você precisará de um URL de endpoint de webhook para configurar essa integração, que pode ser obtido com o gerente da sua conta Heap.

### Etapa 2: Configurar Braze Currents

Na Braze, navegue até **Integrações de parceiros** > **Exportação de dados**, clique em **Criar nova integração com o Currents** e selecione **Exportação do Heap**. 

Dê um nome à sua exportação e prossiga para a página **Current Details (Detalhes atuais** ). Nessa página, insira o endpoint e o token de portador opcional (se fornecido).

Depois de configurar as credenciais da integração, verifique todos os eventos de engajamento com mensagens, comportamento do cliente e do usuário que gostaria de exportar para o Heap e clique em **Abrir Current**.

![]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}

