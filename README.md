<h1>Hipermidia - Motor de busca na Wikipedia</h1>

<p>Baixe o arquivo xml disponível em:</p>
<p>https://drive.google.com/file/d/1Tk6YGxxZbEU07swxRyALa8kEcP5kzV2G/view?usp=sharing</p>

<h2>Tarefa 1:</h2> 
<p>Quantas tags <page> tem no arquivo?</p>
 
<h2>Tarefa 2:</h2>
<p>Imprimir o <id> e <title> de cada uma das <page> do arquivo.</p>
 
<h2>Tarefa 3:</h2>
<p>O usuário informa uma string de busca. Você deve listar apenas os <id> e <title> daquelas páginas em que aparece aquela string de busca no <title>.</p>
 
<h2>Tarefa 4:</h2>
<p>Mostrar o resultado de busca de acordo com a contagem de ocorrências. As páginas com mais ocorrências devem aparecer na frente das demais. Aquelas com ocorrência no title contam como 10.</p>

<h2>Tarefa 5:</h2>
Há duas opções, você deve escolher aquela que preferir:
 
* Opção 1: Caching. <p>Crie um loop perguntando qual a string de busca. Quando houver uma busca, você deve armazenar o resultado em uma hash table, onde devem ficar armazenadas as buscas que já foram feitas. Assim, quando se procura novamente por uma mesma palavra de busca, o resultado sai mais rápido porque já está armazenado em uma hash table.</p>
 
* Opção 2: Hash invertida: <p>Para cada string encontrada no <title> de todas as páginas, você deve inserir o resultado daquela busca em uma hash invertida. É bem parecido com o cache, mas agora você insere no cache todas as strings que encontrar no <title> das páginas do arquivo. Dessa forma, antes mesmo de iniciar o loop pelas strings de busca, você já pré-computou todas as possíveis buscas que podem ser feitas.</p>
 
<h2>Tarefa 6:</h2>
<p>Fazer a busca por duas strings. "Science" dá um resultado de busca; já "computer" dá outro. Agora "computer science" vai dar qual resultado? Crei seu próprio critério.</p>