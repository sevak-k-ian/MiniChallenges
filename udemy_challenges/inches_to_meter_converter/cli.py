#############################################
"""
GET FEET/INCHES AND CONVERT IT INTO METERS
The user will input in the IDE :
- 5 12
- Need to understand the input in order to correctly convert it into meters
Info → The distance d in meters (m) is equal 
to the distance d in feet (ft) times 0.3048 + the distance d in inches (in) times 0.0254:
"""
#############################################
import functions

def convert_into_meters() -> None :
    feet, inch = functions.parse_user_input()
    result : float = functions.converter(feet=feet, inch=inch)
    print(f'You provided me {feet} feets & {inch} inches to convert into meters.'
          f'The result is: {result}m.')



if __name__ == "__main__" :
    convert_into_meters()
