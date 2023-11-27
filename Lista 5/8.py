class EditorDeTexto:
    def __init__(self):
        self.historico_comandos = []
        self.texto = ""

    def executar_comando(self, comando):
        self.historico_comandos.append(self.texto)
        self.texto += comando

    def desfazer(self):
        if self.historico_comandos:
            self.texto = self.historico_comandos.pop()
        else:
            print("Nada para desfazer.")

    def refazer(self):
        print("Refazer ainda não implementado.")  # Implemente conforme necessário.

# Exemplo de uso:
editor = EditorDeTexto()
editor.executar_comando("InserirTexto1")
editor.executar_comando("InserirTexto2")
print(editor.texto)  # Saída: InserirTexto1InserirTexto2
editor.desfazer()
print(editor.texto)  # Saída: InserirTexto1
