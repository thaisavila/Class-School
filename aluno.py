from membroEscola import SchoolMember

class Student(SchoolMember):
  def __init__(self, name, registration,role= "student", presents=0, absences=0, grades=[]):
    super().__init__(name, registration, role)
    self.presents = presents   # Presença
    self.absences = absences   # Faltas
    self.grades = grades       # Notas
    
  def final_average(self):
    """Função para calcular a média final do aluno"""
    media = sum(self.grades)/len(self.grades)
    print(f"Sua média final é: {media}")
  
  def proof_affiliation(self, registration:int):
    """Função para visualizar comprovante de matrículas"""
    print("\nComprovante de matrícula")
    for student in SchoolMember.students:
      if student.registration == registration:
        print(f"Nome: {student.name}")
        print(f"Matrícula: {student.registration}")
    print("O estudante está regularmente matrículado nessa instituição de ensino")

  def academic_status(self):
    """Função para visualizar se o aluno está aprovado ou reprovado com base na frequência e notas"""
    print("Status do aluno")
    print(f"Presenças: {self.presents}")
    print(f"Faltas: {self.absences}")
    media = sum(self.grades)/len(self.grades)
    print(f"Média final: {media}") # Depois chamar a final_average aqui
    if media<7:
      print("Status: REPROVADO")
      print("Obs: Sua média precisa ser maior ou igual a 7")
    elif self.absences*4>self.presents:
      print("REPROVADO")
      print("Obs: Você precisa de no mínimo 25% de presença nas aulas")
    else:
      print("APROVADO")



# Implementar para ver notas