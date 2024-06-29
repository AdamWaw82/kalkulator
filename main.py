import logging

logging.basicConfig(level=logging.DEBUG)

def validate_value( value ):
    # próbowałem 
    # str(value).isdigit()
    # str(value).isnumeric()
    # str(value).isdecimal()
    # ale i tak jak podałem zeminnoprzecinkową wartość to zwracał że to nie liczba :/
    # więc skończyłem tak: 

    try:
        fl_repr = float(value)
        return True
    except:
        return False

def get_user_values(user_choice: int):
    values = []
    index = 1
    if user_choice not in [2,4]:
        logging.info("!!! Podanie pustej wartości wykonuje działanie !!!")

    while True:
        value = input(f"Podaj składnik {index}: ")

        if value == "":
            break

        if validate_value(value):
            values.append(float(value))
            index += 1
        else:
            logging.info(f"Podana wartość nie jest liczbą: {value}")

        if user_choice in [2,4] and len(values) == 2:
           break

    if len(values) < 2:
        logging.info(f"Musisz podać przynajmniej 2 liczby do wykonania działania")

    operations = {
        1: dodawanie,
        2: odejmowanie,
        3: mnozenie,
        4: dzielenie
    }

    if user_choice in operations:
        result = operations[user_choice](values)
        logging.info(f"Wynik działania to: {result}")
    


def operation_informator(value_list):
    oper = ""
    for elem in value_list:
        oper += f"{elem} i "
    return oper[:-3]

def dodawanie(value_list: list):
    logging.info( f"Dodaję {operation_informator(value_list)}" )
    return sum(value_list)

def odejmowanie(value_list):
    logging.info( f"Odejmuje {operation_informator(value_list)}" )
    result = value_list[0]
    for value in value_list[1:]:
        result -= value
    return result

def mnozenie(value_list):
    logging.info( f"Mnożę {operation_informator(value_list)}" )

    result = value_list[0]
    for value in value_list[1:]:
        result *= value
    return result

def dzielenie(value_list):
    logging.info( f"Dzielę {operation_informator(value_list)}" )

    result = value_list[0]
    for value in value_list[1:]:
        if value > 0:
            result /= value
        else:
            logging.error(f"Pamiętaj holero nie dziel przez 0")
            exit()
    return result

if __name__ == "__main__":
    
    user_choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: \r\n")
    if user_choice.isnumeric() and int(user_choice) in range(1, 5):
        get_user_values( int(user_choice) )
    else:
        logging.info(f"Dokonałeś/aś błędnego wyboru: {user_choice}")