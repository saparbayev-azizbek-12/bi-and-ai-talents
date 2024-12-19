def convert_far_to_cel(F):
    C = F * 9/5 + 32
    print(f'{F} degrees F = {C:.2f} degrees C')
def convert_cel_to_far(C):
    F = (C - 32) * 5/9
    print(f'{C} degrees C = {F:.2f} degrees F')

f = int(input('Enter a temperature in degrees F: '))
convert_cel_to_far(f)
c = int(input('Enter a temperature in degrees C: '))
convert_far_to_cel(c)