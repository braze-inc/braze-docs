### Pré-requisitos

Antes de usar esse método de integração, será necessário [criar uma conta e um contêiner para o Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Etapa 1: Abra a galeria de modelos de tag

No [Google Tag Manager](https://tagmanager.google.com/), escolha seu espaço de trabalho e, em seguida, selecione **Modelos**. No painel **Modelo de tag**, selecione **Pesquisar galeria**.

![A página de modelos para um espaço de trabalho de exemplo no Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Etapa 2: Adicionar o modelo de tag de inicialização

Na galeria de modelos, procure por `braze-inc` e selecione **Braze Initialization Tag**.

![A galeria de modelos que mostra os vários modelos do 'Braze-inc'.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecione **Adicionar ao espaço de trabalho** > **Adicionar**.

![A página "Braze Initialization Tag" no Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Etapa 3: Configurar a tag

Na seção **Modelos**, selecione o modelo recém-adicionado.

![A página "Templates" no Google Tag Manager mostra o modelo Braze Initialization Tag.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecione o ícone de lápis para abrir o menu suspenso **Tag Configuration (Configuração de tag** ).

![O bloco de Configuração de tag com o ícone de "lápis" mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Insira as informações mínimas necessárias:

| Campo         | Descrição |
| ------------- | ----------- |
| **Chave de API**   | Sua [chave de API do Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), encontrada no dashboard do Braze em **Configurações** > **Configurações do app**. |
| **Endpoint de API** | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| **Versão do SDK**  | A versão `MAJOR.MINOR` mais recente do Web Braze SDK listada no [changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Para saber mais, consulte [Sobre o gerenciamento de versões do SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para configurações adicionais de inicialização, selecione **Braze Initialization Options (Opções de inicialização do Braze** ) e escolha as opções necessárias.

![A lista de opções de inicialização do Braze está em "Tag Configuration" (Configuração da tag).]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Etapa 4: Definido para disparar em *todas as páginas*

A tag de inicialização deve ser executada em todas as páginas de seu site. Isso permite que você use os métodos do Braze SDK e registre a análise de dados web push.

### Etapa 5: Verifique sua integração

Você pode verificar sua integração usando uma das seguintes opções:

- **Opção 1:** Usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager, é possível verificar se a tag de inicialização do Braze está disparando corretamente em suas páginas ou eventos configurados.
- **Opção 2:** Verifique se há alguma solicitação de rede feita ao Braze a partir de sua página da Web. Além disso, a biblioteca global `window.braze` deve ser definida agora.
