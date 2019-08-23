# Primeiro exercício 

# As respostas das questões 1 e 2 sao respectivamentes:
# 2 Metros e Letra (D)

# A partir deste ponto, está descrito a solucao do problema proposto.



Data = input("Digitalize os comando variando entre F ou V. \n")   # The input, the commands to robot.
Data = Data.upper()      # put all the string in UPPER.


while "TF" in Data:                   # here im using 'while' because if you try to use 'if', the loop is not gonna happen, so, use while for the loop in the string.
    Data = Data.replace("TF","")

while "FT" in Data:
    Data = Data.replace("FT","")

if len(Data) > 0:

    if 'F' in Data:                # the code is identifying if the result is positive or negative.
        x = '-'
    else:
        x = '+'

    print("O resultado foi {} {} passos em relação à posição inicial do robô.".format(len(Data),x))   # print the output

if len(Data) < 0:      # if len == 0, the robot stay in the same position, it doesn't matter if the robot moved, the machine has returned to the start position.
    print("O robô permance na posição inicial.")

    # The first steps in the code is making the way to cancel the 'F' and 'T' and if the 'Len' still other than 0, the code identify if signal is positive or negative.
