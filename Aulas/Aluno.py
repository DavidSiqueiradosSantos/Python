class Aluno:
    def __init__(self, n, r):
        self.nome = "David"
        self.registro = '015949'
        self.historico = ["David", "015949"]

    def getNome(self):
        return self.nome

    def getRegistro(self):
        return self.registro

    def getHistorico(self):
        return self.historico


for aluno in turma:
    print(f"[{aluno.registro}] {aluno.nome} : ")
    tot = 0
    for carga in aluno.historico:
        tot = tot + carga

for aluno in turma:
    print(f"([{aluno.registro} {aluno.nome} : {aluno.getTotal()}] h")


class Turma:
    def __init__(self, registro, nome):
        self.registro = registro
        self.nome = nome
        self.historico = []

    def listaAlunos(self):
        print("Alunos da turma ", self.registro, self.historico)
        for a in self.alunos:
            print(a.getNome())

    def adicionaAluno(self, aluno):
        self.alunos += [aluno]
