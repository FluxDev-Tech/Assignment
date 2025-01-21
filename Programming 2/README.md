 
Python 

#ito yung mga pagpipilian natin kung ano ang gusto natin i-calculate
print("1. Addition: ")
print("2. Subtraction: ")
print("3. Multiplication: ")
print("4. Division: ")
#ito yung mga pagpipilian natin kung ano ang gusto natin i-calculate: Ito ay isang komento. Hindi ito bahagi ng code na isasagawa ng computer. Ginagamit ito para magbigay ng paliwanag sa code para sa mga tao na nagbabasa nito.
print("1. Addition: "), print("2. Subtraction: "), Ang print() ay isang function na nagpapakita ng text sa screen natin. Ipinapakita nito ang mga pagpipilian para sa user: Addition, Subtraction, Multiplication, at Division.
Python

chooseoption = int(input("Choose An Option Provided Above: "))
input("Choose An Option Provided Above: "): Ang input() ay isang function na kumukuha ng input/text mula sa user. Ipinapakita nito ang text na "Choose An Option Provided Above:" sa screen at hinihintay ang ging input ng user. Ang input na ito ay laging isang string (text).
int(...): Ang int() ay isang function na kino-convert ang isang value sa isang integer (Whole Number). Kaya, ang input ng user (na string) ay kino-convert sa isang integer at inilalagay sa variable na chooseoption. Halimbawa, kung ang user ay nag-input ng "1", ang chooseoption ay magiging 1.
Python

result = 0  # ito yung viriable natin na nagtatago ng calculate natin
result = 0: Dito, gumagawa tayo ng isang variable na tinatawag na result at binibigyan ito ng initial value na 0. Ang variable na ito ang magtatago ng result ng calculation natin.
Python

# print the first and second number
if chooseoption in (1, 2, 3, 4):
    number1 = float(input("Enter The First Number: "))
    number2 = float(input("Enter The Second Number: "))
if chooseoption in (1, 2, 3, 4):: Ito ay isang conditional statement. ginasuri sini kung ang value ng chooseoption ay nasa loob ng tuple (1, 2, 3, 4). Ibig sabihin, ginasuri sini kung ang pinili ng user ay isa sa mga valid na option.
number1 = float(input("Enter The First Number: ")) at number2 = float(input("Enter The Second Number: ")): Kung valid ang chooseoption, hihingi tayo ng code ng dalawang numero mula sa user. Ang float() ay ginagamit para i-convert ang input sa isang floating-point number (numero na may decimal).
Python

    if chooseoption == 1:    
        result = number1 + number2
    elif chooseoption == 2:
        result = number1 - number2
    elif chooseoption == 3:
        result = number1 * number2
    elif chooseoption == 4:
        if number2 != 0:
            result = number1 / number2
        else:
            print("Error: Division by zero is not allowed.") #dito kung nag print ka nang false na number lalabas dyn ang error division
            result = None

ang if,elif,else yan yung tinatawag na control flow statement na gumagawa ng conditional execution na nagsasagawa ng tamang option base sa value ng chooseoption.
Kung chooseoption ay 1, gagawin ang addition.
Kung chooseoption ay 2, gagawin ang subtraction.
Kung chooseoption ay 3, gagawin ang multiplication.
Kung chooseoption ay 4, gagawin ang division. Dito, may karagdagang akong binutang para maiwasan ang division by zero error. Kung ang number2 ay 0, magpi-print ng error message at itatakda ang result sa None.
Python

    else:
        print("Invalid Option Chosen")  # if wala sa statement ang numbers mo

Ang else naman na ito ay para sa unang if chooseoption sa loob ng tuple (1, 2, 3, 4):. Kung ang chooseoption ay hindi 1, 2, 3, o 4, ipi-print nito ang "Invalid Option Chosen".
Python

    # if calculate is true  
    if result is not None:
        print("The Result of the Operation is:", result)

if result is not None: ginasuri namn nito kung ang result ay hindi None. Ito ay para siguraduhing  walang error na nangyari sa code naton (tulad ng division by zero) bago i-print ang resulta.
print("The Result of the Operation is:", result): Ipi-print namn nito ang resulta ng option kung walang error ang ging code naton.
Sa madaling salita, ang code natin ay isang simpleng calculator na kumukuha ng input mula sa user para sa gustong option at dalawang numero,
at pagkatapos ay kinakalkula at ipinapakita ang resulta. Mayroon din itong error handling para sa invalid na input at division by zero.