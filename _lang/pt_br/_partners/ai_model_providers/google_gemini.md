---
nav_title: Google Gemini
article_title: Google Gemini
description: "Este artigo de referência descreve a parceria entre a Braze e o Google Gemini, que permite que você conecte modelos Gemini à Braze para uso com agentes de IA personalizados."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [O Google Gemini](https://deepmind.google/technologies/gemini/) é a família de modelos de IA do Google que combina raciocínio avançado em texto, código e imagens para ajudar as marcas a oferecer experiências mais inteligentes e personalizadas.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Essa integração é mantida pelo Google._

## Sobre a integração

A integração entre a Braze e o Google Gemini permite conectar sua chave de API do Google Gemini ou chave do Vertex AI à Braze para que você possa usar modelos Gemini ao criar agentes de IA personalizados. Com essa integração, seus agentes podem gerar textos personalizados, tomar decisões em tempo real ou atualizar campos do catálogo usando os modelos Gemini do Google.

## Pré-requisitos

| Requisitos | Descrição |
|---|---|
| Conta do Google Cloud com chave de API do Gemini ou chave do Vertex AI | Uma conta do Google Cloud com uma chave de API do Gemini ou chave do Vertex AI. Para obter ajuda, entre em contato com seu administrador ou com o [suporte do Google Cloud](https://cloud.google.com/support). |
| Instância da Braze | Você pode encontrar sua instância da Braze na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints) ou com seu gerente de integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para conectar sua chave de API do Google Gemini à Braze:

1. Acesse **Partner Integrations** > **Technology Partners** no dashboard da Braze e encontre o Google Gemini.
2. Em **API Type**, selecione **Gemini API** ou **Vertex AI**.
3. Digite sua chave de API do Google. Para o Vertex AI, insira o ID do projeto.
4. Selecione **Save**.

Depois de salvar, você pode selecionar modelos Gemini ao [criar um agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) no Console do agente.

Entre em contato com o [suporte do Google Cloud](https://cloud.google.com/support) em caso de problemas ou dúvidas sobre sua integração.