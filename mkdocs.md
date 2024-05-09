# Implementação do MkDocs via Docker

Para a execução do MkDocs através do Docker, é imperativo que os arquivos “Dockerfile” e “exclude.sh” estejam localizados na pasta raiz do projeto. Este procedimento pode ser automatizado futuramente, permitindo que, dentro de uma pipeline, a montagem completa da estrutura do projeto seja realizada através de poucos comandos.

## Justificativa para a Localização dos Arquivos na Pasta Raiz
A razão para a localização desses arquivos na pasta raiz é que eles se estendem a alguns arquivos que são fundamentais para o funcionamento do MkDocs. Estes incluem:

- Pasta `libs`: Contém todos os códigos e seus respectivos comentários.
- Pasta `docs`: Contém toda a documentação atual do projeto que será utilizada pelo MkDocs.
- Arquivo `pyproject.toml`: Este arquivo é essencial, pois contém os pacotes principais necessários para o funcionamento do MkDocs.
- Arquivo `mkdocs.yml`: Este é o arquivo de configuração principal da ferramenta MkDocs.


## Função do Script exclude.sh
O script exclude.sh é uma automação que será executada assim que a imagem Docker for gerada. Sua função é realizar uma varredura na pasta docs, procurando por arquivos que começam com **`#depreciado`**. Se esses arquivos forem encontrados, eles serão movidos para uma pasta chamada exclude, que é criada pelo próprio script.

**Nota Importante**: É necessário escrever exatamente **`#depreciado`** se desejar que um arquivo Markdown localizado dentro de /docs seja ocultado no site. Alternativamente, é possível criar manualmente a pasta `exclude` e adicionar os arquivos que deseja ocultar lá dentro.