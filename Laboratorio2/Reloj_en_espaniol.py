from datetime import datetime

def time_to_text(hour, minute):
    if (hour > 12):
        hour -= 12
    if (minute > 37):
        hour += 1
    match hour:
        case 1:
            texto = 'la una '
        case 2:
            texto = 'las dos '
        case 3:
            texto = 'las tres '
        case 4:
            texto = 'las cuatro '
        case 5:
            texto = 'las cinco '
        case 6:
            texto = 'las seis '
        case 7:
            texto = 'las siete '
        case 8:
            texto = 'las ocho '
        case 9:
            texto = 'las nueve '
        case 10:
            texto = 'las diez '
        case 11:
            texto = 'las once '
        case 12:
            texto = 'las doce '
    match minute:
        case 58 | 59 | 0 | 1 | 2:
            texto += 'en punto'
        case 3 | 4 | 5 | 6 | 7:
            texto += 'y cinco'
        case 8 | 9 | 10 | 11 | 12:
            texto += 'y diez'
        case 13 | 14 | 15 | 16 | 17:
            texto += 'y cuarto'
        case 18 | 19 | 20 | 21 | 22:
            texto += 'y veinte'
        case 23 | 24 | 25 | 26 | 27:
            texto += 'y veinticinco'
        case 28 | 29 | 30 | 31 | 31:
            texto += 'y media'
        case 33 | 34 | 35 | 36 | 37:
            texto += 'y treintaicinco'
        case 38 | 39 | 40 | 41 | 42:
            texto += 'menos viente'
        case 43 | 44 | 45 | 46 | 47:
            texto += 'menos cuarto'
        case 48 | 49 | 50 | 51 | 52:
            texto += 'menos diez'
        case 53 | 54 | 55 | 56 | 57:
            texto += 'menos cinco'
    return texto        

current = input("Ingrese una hora en formato hora:minutos : ")
if (current == ""):
    current = datetime.now()
    hour = current.hour
    minute = current.minute
else:
    current = current.split(":")
    hour = current[0]
    minute = current[1]
texto = time_to_text(int(hour), int(minute))
print(f'{hour}:{minute} Son {texto}')