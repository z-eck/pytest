O mkdocs possui uma função nativa de exclusão

Porém, nativamente, ele não exclui arquivos específicos dentro de subpastas. O que é possível é excluir uma única pasta, ou um arquivo de todo ecossistema. 

Mas via plugin, isso é possível. Entretanto, eu pensei em um script que captura estes arquivos que iniciam com #Depreciado, e jogam eles dentro de uma única pasta, e a pasta em si é excluida. Dessa maneira evita de baixar plugin extra para deixar a imagem mais pesada, e também mantém todos o ecossistema do projeto fora de risco.