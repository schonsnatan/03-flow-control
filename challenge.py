#WIP
CONSTANTE_BONUS = 1000

#Request the name for the user:

nameCheck = True
salCheck = True
bonusCheck = True

while nameCheck:
    try:
        name = input("Type your name: ")
        if len(name)==0:
            raise ValueError("Please provide a name")
        elif any(char.isdigit() for char in name):
            raise ValueError("Your name must have only letters")
        elif name.isspace():
            raise ValueError("Please type something")
        else:
            print("Olá,",name)
            nameCheck = False
    except ValueError as e:
        print(f"Error: {e}. Please take a look into the instructions.")

#Request the salary:
while salCheck:
    try:
        sal = float(input("Informe seu salario: "))
        if sal<=0:
            raise ValueError("Inform a positive and non-zero value")
        else:
            salCheck = False
    except ValueError as e:
        print(f"Error: {e}. Please take a look into the instructions.")

while bonusCheck:
    #Request the bonus value:
    try:
        bonus = float(input("Digite o seu bonus: "))
        if bonus < 0:
            raise ValueError("Inform a positive bonus.")
        else:
            bonusCheck = False
    except ValueError as e:
        print(f"Error: {e}. Please take a look into the instructions.")


#Print the informations for the user:
final_bonus = CONSTANTE_BONUS + sal * bonus
kpi = (sal + final_bonus) / 1000

print(f"Your KPI is: {kpi:.2f}")
print(f"{name}, your salary is ${sal:.2f} and your final bonus is ${final_bonus:.2f}")