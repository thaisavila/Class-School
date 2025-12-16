class SchoolMember:
  students = []
  teachers = []

  def __init__(self,name:str,registration:str,role:str):
    self.name = name
    self.registration = registration
    self.role = role
  
  def view_class(self):
    """Função para ver todos os alunos de uma turma"""
    for student in SchoolMember.students:
      print(f"Aluno: {student.name} - Matrícula: {student.registration}")

  def proof_affiliation(self, name,role):
    """Função para visualizar as informções de um aluno/professor específico"""
    if role == "student":
      lista = SchoolMember.students
    elif role == "teacher":
      lista = SchoolMember.teachers
    else:
      print("ERRO")
      return
    print("Comprovante de vínculo")
    for i in lista:
      if i.name == name:
        print(f"Nome: {i.name}  \nMatrícula: {i.registration}")
        if i.role == "student":
          print("Estudante")
        elif i.role == "teacher":
          print("Professor")