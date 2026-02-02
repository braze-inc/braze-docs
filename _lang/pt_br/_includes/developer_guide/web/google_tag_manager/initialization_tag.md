### Pré-requisitos

Antes de usar este método de integração, você precisará [criar uma conta e um contêiner para o Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Etapa 1: Abra a galeria de modelos de tag

No [Google Tag Manager](https://tagmanager.google.com/), escolha seu espaço de trabalho e, em seguida, selecione **Modelos**. No painel **Modelo de Tag**, selecione **Pesquisar Galeria**.

![A página de modelos para um espaço de trabalho de exemplo no Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Etapa 2: Adicione o modelo de tag de inicialização

Na galeria de modelos, procure por `braze-inc`, em seguida, selecione **Tag de Inicialização Braze**.

![A galeria de modelos mostrando os vários modelos 'braze-inc'.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecione **Adicionar ao espaço de trabalho** > **Adicionar**.

![A página 'Tag de Inicialização Braze' no Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Etapa 3: Configure a tag

Na seção **Modelos**, selecione seu modelo recém-adicionado.

![A página "Modelos" no Google Tag Manager mostrando o modelo de Tag de Inicialização Braze.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecione o ícone de lápis para abrir o dropdown de **Configuração da Tag**.

![O bloco de Configuração da Tag com o ícone de 'lápis' mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Insira as informações mínimas necessárias:

| Campo         | Descrição |
| ------------- | ----------- |
| **Chave de API**   | Sua [Chave de API Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), encontrada no painel Braze em **Configurações** > **Configurações do App**. |
| **Endpoint de API** | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| **Versão do SDK**  | A versão mais recente `MAJOR.MINOR` do SDK Web Braze listada no [changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Para mais informações, veja [Sobre o gerenciamento de versão do SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para configurações de inicialização adicionais, selecione **Opções de Inicialização Braze** e escolha quaisquer opções que você precisar.

![A lista de Opções de Inicialização do Braze está em 'Configuração da Tag'.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Etapa 4: Defina para Disparar em *todas as páginas*

A tag de inicialização deve ser executada em todas as páginas do seu site. Isso permite que você use os métodos do SDK do Braze e registre a análise de web push.

### Etapa 5: Verifique sua integração

Você pode verificar sua integração usando uma das seguintes opções:

- **Opção 1:** Usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager, você pode verificar se a Tag de Inicialização do Braze está disparando corretamente nas suas páginas ou eventos configurados.
- **Opção 2:** Verifique se há solicitações de rede feitas para o Braze a partir da sua página da web. Além disso, a biblioteca global `window.braze` deve agora estar definida.
