---
nav_title: Crowdin
article_title: Crowdin
description: "Use a integração com o Crowdin para traduzir campanhas, experiências no Canvas, modelos de e-mail e blocos de conteúdo com Translation Memory, glossários e tradução automática."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> O [Crowdin](https://crowdin.com/) é uma plataforma de gerenciamento de localização baseada em IA que ajuda equipes a automatizar a tradução de seus softwares, apps e conteúdos de marketing.

Conecte o Crowdin à Braze para gerenciar traduções das suas campanhas e experiências no Canvas. A sincronização automatizada funciona com tradução automática, Translation Memory e glossários para que os fluxos de trabalho humanos e automatizados permaneçam consistentes.

_Essa integração é mantida pelo Crowdin._

## Sobre a integração

O Crowdin oferece dois apps para a Braze: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) e [Braze Email Templates](https://store.crowdin.com/braze-app). Escolha com base nos recursos da Braze que você localiza. A tabela a seguir compara os dois.

### Escolha o app certo do Crowdin

| Canal ou recurso | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campanhas** | ✅ Compatível | ❌ Não compatível |
| **Etapas do canva** | ✅ Compatível | ❌ Não compatível |
| **Modelos de e-mail** | ❌ Não compatível | ✅ Compatível |
| **Blocos de conteúdo** | ❌ Não compatível | ✅ Compatível |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| **Conta do Crowdin** | É necessário ter uma [conta no Crowdin.com](https://accounts.crowdin.com/register) ou uma [conta no Crowdin Enterprise](https://accounts.crowdin.com/workspace/create). |
| **Projeto do Crowdin** | Antes de conectar a Braze, [crie um projeto de tradução](https://support.crowdin.com/creating-project/) no Crowdin ou no Crowdin Enterprise. |
| **Chave da API REST da Braze** | Uma chave da API REST da Braze com permissões para campanhas, Canvas, blocos de conteúdo, atributos personalizados, e-mail e modelos. |
| **Endpoint REST da Braze** | A URL específica do seu endpoint REST da Braze (por exemplo, `https://rest.iad-03.braze.com`). |
| **Configurações multilíngues da Braze** | Os locales devem estar configurados no dashboard da Braze em **Configurações** > **Configurações de localização**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração Braze Campaigns & Canvas

Se você localiza conteúdo dentro de mensagens ativas, use o [app Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) para sincronizar strings traduzíveis dos rascunhos de suas campanhas e canvas com o suporte multilíngue da Braze.

Para um passo a passo em vídeo, consulte [Integração Braze Campaigns & Canvas](https://youtu.be/ahG1ET4VRKA).

### Etapa 1: Configure as definições multilíngues na Braze

Antes de conectar o Crowdin, adicione seus idiomas de destino na Braze.

1. Na Braze, acesse **Configurações** > **Configurações de localização**.
2. Adicione os idiomas que você pretende suportar.

![Página de Locales da Braze em Configurações, mostrando nomes de locale, chaves de locale e Adicionar locale.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Anote cada **Chave de locale** (por exemplo, `en-US`, `fr-FR`, `es-ES`). Você usará esses valores ao mapear idiomas no Crowdin.

### Etapa 2: Configure o projeto da Braze no Crowdin

1. Na sua conta do Crowdin Enterprise ou Crowdin.com, acesse a **Store** no menu à esquerda.
2. Pesquise por **Braze Campaigns & Canvas** e selecione **Install**.

![Crowdin Store com Braze Campaigns & Canvas selecionado e Install destacado.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Selecione o projeto (ou projetos) onde deseja usar essa integração.
4. Para abrir a integração, acesse **Integrações** > **Braze Campaigns & Canvas** no seu projeto.

#### Conectando a Braze ao Crowdin

Autorize a conexão com suas credenciais de API da Braze:

![Formulário de conexão do Crowdin Braze Campaigns & Canvas com chave da API REST, endpoint REST e Log in with Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Chave da API REST da Braze:** Crie-a na Braze em **Configurações** > **APIs e identificadores** > **Chaves de API**. Conceda as permissões necessárias para essa integração (campanhas, Canvas, blocos de conteúdo e atributos personalizados).
- **Endpoint REST da Braze:** Insira a URL da sua instância da Braze (por exemplo, `https://rest.iad-03.braze.com`). Para saber mais, consulte [Endpoints da API REST]({{site.baseurl}}/api/basics/#endpoints).

![Página de chaves da API REST da Braze com Criar chave de API e o controle de cópia do endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Selecione **Log in with Braze Campaigns & Canvas**.

### Etapa 3: Configure o mapeamento de idiomas no Crowdin

Após conectar sua conta, mapeie cada idioma do projeto Crowdin para o locale correspondente da Braze.

1. No painel da integração **Braze Campaigns & Canvas**, selecione o ícone de engrenagem **Settings** no canto superior direito.

![Tela da integração Braze Campaigns & Canvas com Settings na barra de ações superior.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Abra a guia **General Settings**.
3. Insira as chaves de locale. O Crowdin lista os idiomas do seu projeto (por exemplo, francês, italiano). Em cada campo, insira a **chave de locale da Braze** correspondente.
   - Por exemplo, se a Braze usa `it` para italiano, insira `it` ao lado de italiano no Crowdin.
   - Cada entrada deve corresponder exatamente à **Chave de locale** daquele locale nas **Configurações de localização** da Braze.

![Modal de configurações na guia General Settings, mostrando campos de filtro de arquivo e linhas de mapeamento de idiomas (por exemplo, francês mapeado para fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Selecione **Save** para confirmar o mapeamento.

### Etapa 4: Adicione tags de tradução à sua mensagem na Braze

O Crowdin lê as mesmas **tags de tradução** Liquid que a Braze usa para mensagens multilíngues. Adicione {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} ao redor de cada trecho de texto, URL de imagem ou URL de link que você deseja traduzir. Cada bloco precisa de um `id` único (por exemplo, `greeting` ou `welcome_header`).

**Exemplo:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Para HTML, Liquid em links e outros padrões, siga as mesmas regras descritas em [Traduzindo locales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) (por exemplo, mantenha as tags ao redor dos menores segmentos possíveis e envolva apenas as partes específicas do idioma nas URLs ao localizar links).

Salve sua mensagem na Braze como **Rascunho** antes que o Crowdin possa detectar e extrair o conteúdo.

### Etapa 5: Gerencie traduções no Crowdin

A tela da integração tem dois lados:

- **Lado direito (Braze):** Suas campanhas e canvas.
- **Lado esquerdo (Crowdin):** Conteúdo já sincronizado para tradução.

![Painéis do Crowdin e Braze Campaigns & Canvas com pastas para campanhas e locales, Sync to Braze e Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Sincronizando conteúdo

1. No lado **Braze (Direito)**, marque a caixa de seleção da campanha ou do canva que deseja traduzir.
2. Selecione **Sync to Crowdin**.
3. Quando a sincronização for concluída, o arquivo aparecerá no lado **Crowdin (Esquerdo)**. Os tradutores podem abrir as strings no Editor do Crowdin.

#### Enviando traduções de volta para a Braze

1. Quando as traduções estiverem 100% concluídas no Crowdin, volte à guia **Integrações**.
2. Selecione o conteúdo concluído no lado **Crowdin (Esquerdo)**.
3. Selecione **Sync to Braze**. Isso envia as strings traduzidas para as variantes de idioma correspondentes na sua campanha da Braze.

### Etapa 6: Visualize a mensagem como um usuário multilíngue na Braze

Para confirmar a integração:

1. Abra sua campanha no **Criador de mensagens da Braze**.
2. Acesse a guia **Teste**.
3. Selecione **Visualizar mensagem como usuário**.
4. Pesquise um perfil de usuário que tenha um atributo `language` correspondente a um dos seus locales traduzidos.
5. Confirme que o conteúdo muda do idioma de origem para a versão traduzida.

## Integração Braze Email Templates

Se você localiza e-mails no nível do modelo, use o [app Braze Email Templates](https://store.crowdin.com/braze-app) para sincronizar HTML da sua Biblioteca de Mídia da Braze.

Para um passo a passo em vídeo, consulte [Integração Braze Email Templates](https://youtu.be/g0YMKW3jEjk).

### Etapa 1: Instale o app

1. No seu projeto do Crowdin, acesse a guia **Store**.
2. Pesquise por **Braze Email Templates** e selecione **Install**.

![Crowdin Store com Braze Email Templates selecionado e Install destacado.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Selecione o projeto (ou projetos) onde deseja usar essa integração.
4. Para abrir a integração, acesse **Integrações** > **Braze Email Templates** no seu projeto.

### Etapa 2: Conecte-se à Braze

Autorize a conexão com suas credenciais de API da Braze:

![Formulário de conexão do Crowdin Braze Email Templates com chave da API REST, endpoint REST e Log in with Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Chave da API REST da Braze:** Conceda permissões de `templates.email` e `content_blocks` (leitura e escrita). Crie a chave na Braze em **Configurações** > **APIs e identificadores** > **Chaves de API**.

![Página de chaves da API REST da Braze com Criar chave de API e o controle de cópia do endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Para o **Endpoint REST da Braze**, use a URL específica da sua instância (por exemplo, `https://rest.iad-03.braze.com`).
3. Selecione **Log in with Braze Email Templates**.

### Etapa 3: Sincronize conteúdo para tradução

A tela da integração mostra sua biblioteca da Braze:

- **Lado direito (Braze):** **Modelos de e-mail** e **Blocos de conteúdo** que você pode sincronizar.
- **Lado esquerdo (Crowdin):** Conteúdo em tradução.

1. No lado **Braze (Direito)**, marque a caixa de seleção ao lado dos modelos ou blocos que deseja localizar.
2. Selecione **Sync to Crowdin**.
3. O Crowdin extrai o código-fonte HTML. Os tradutores trabalham no Editor do Crowdin com uma **prévia WYSIWYG** ao vivo para que o layout permaneça intacto.

![Guia de prévia do Editor do Crowdin mostrando HTML de e-mail localizado e strings traduzíveis.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Etapa 4: Entregue os modelos traduzidos

Quando as traduções atingirem 100% de conclusão:

1. Selecione os arquivos concluídos no lado **Crowdin (Esquerdo)**.
2. Selecione **Sync to Braze**.
3. O Crowdin cria automaticamente versões localizadas desses ativos na sua biblioteca de mídia da Braze (por exemplo, `Template_Name_fr`).

![Painéis do Crowdin e Braze Email Templates listando modelos de e-mail e blocos de conteúdo, com Sync to Braze e Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})