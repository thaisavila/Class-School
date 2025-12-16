from membroEscola import SchoolMember
from aluno import Student

class Teacher(SchoolMember):
  # criar um init pra salario
  def __init__(self, group:str, name:str, registration:str, role ="teacher"):
    self.group = group # Turma
    super().__init__(name, registration,role)
    
  def release_grade(self, registration,grade):
     """Função que permite o professor lançar as notas"""
     for i in SchoolMember.students:
      if i.registration == registration:
        i.grades.append(grade)
        print("Nota lançada com sucesso!")
        return
     
  def launch_present(self,registration):
    """Função que permite o professor lançar presenças"""
    for i in SchoolMember.students:
      if i.registration == registration:
        i.presents += 1

  def launch_absences(self,registration):
    """Função que permite o porfessor lançar faltas"""
    for i in SchoolMember.students:
      if i.registration == registration:
        i.absences += 1

  def proof_affiliation(self,registration):
    """Função que mostra o comprovante de vínculo do professor"""
    print("\nComprovante de vínculo")
    for teacher in SchoolMember.teachers:
      if teacher.registration == registration:
        print(f"Nome: {teacher.name}")
        print(f"Matrícula: {teacher.registration}")
    print("O Professor está regularmente vinculado a essa instituição de ensino")

a0 = Student("Ana","1111")
SchoolMember.students.append(a0)
t2 = Teacher("1","Daniel", "1121")
t2.proof_affiliation("1121")


# Criar metodo salario
# Concertar a frequencia pra ficar mais facil pro professor