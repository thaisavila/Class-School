from membroEscola import SchoolMember
from aluno import Student
from professor import Teacher 

a1 = Student("Ana","1111")
a2 = Student("Bruno","2222")
a3 = Student("Carla","1212")
a4 = Student("Diego","4321")
a5 = Student("Eva","5678")
a6 = Student("Fábio","8765")
t1 = Teacher("A","Daniel","3333")
t2 = Teacher("A","Helena","4444")
SchoolMember.students.extend([a1, a2, a3, a4, a5, a6])
SchoolMember.teachers.extend([t1, t2])

def menu_principal():
  while True:
    print("=== Menu do Curso ===")
    print("Você é...")
    print("1. Aluno")
    print("2. Professor")
    print("3. Sair")

    choice = input("Escolha uma opção (1-3): ")  

    if choice == '1':
      menu_aluno()
    elif choice == '2':
      menu_professor()  
    else:
      print("Saindo do sistema... Até mais!")
      return

def menu_aluno():
  print("\n=== Menu do Aluno ===")
  registration = input("Digite sua matrícula: ")

  while True:
    print("\n=== Menu do Aluno ===")
    print("1. Ver comprovante de matrícula")
    print("2. Ver média final")
    print("3. Ver status acadêmico")
    print("4. Ver turma")
    print("5. Voltar ao menu principal")
    print("6. Sair do sistema")

    choice = input("Escolha uma opção (1-6): ")

    if choice == '1':
      print("\n=== Comprovante de Matrícula ===")

        
      a1.proof_affiliation(name, "student")      
    elif choice == '2':
      pass
    elif choice == '3':
      pass
    elif choice == '4':
      return
    else:
      print("Opção inválida. Tente novamente.") 

def menu_professor():
  while True:
    print("\n=== Menu do Professor ===")
    print("1. Lançar nota")
    print("2. Lançar presença")
    print("3. Lançar falta")
    print("4. Ver comprovante de vínculo")
    print("5. Ver turma")
    print("6. Voltar ao menu principal")
    print("7. Sair do sistema")

    choice = input("Escolha uma opção (1-7): ")

    if choice == '1':
      print("\n=== Lançar Nota ===")
      student = input("Digite a matrícula do aluno: ")
      grade = float(input("Digite a nota a ser lançada: "))
      t1.release_grade(student, grade)

    elif choice == '2':
      print("\n=== Lançar Presença ===")
      registration = input("Digite a matrícula do aluno: ")
      t1.launch_present(registration)
      
    elif choice == '3':
      print("\n=== Lançar Falta ===")
      registration = input("Digite a matrícula do aluno: ")
      t1.launch_absences(registration)
      
    elif choice == '4':
      print("\n=== Ver Comprovante de Vínculo ===")
      registration = input("Digite sua matrícula: ")
      t1.proof_affiliation(registration)
    
    elif choice == '5':
      print("\n=== Turma ===")
      t1.view_class()
    elif choice == '6':
      print("Voltando ao menu principal...")
      return
    else:
      print("Opção inválida. Tente novamente.")


#menu_principal()
#menu_professor()
menu_aluno()
# NÃO ESQUECER DE COLOCAR PRA VER AS MÉDIAS DOS ALUNOS