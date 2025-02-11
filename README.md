#Predicted RMR Formula:
=IF(B8="FEMALE",(10*C10)+(6.25*C9)-(5*C7)-161,(10*C10)+(6.25*C9)-(5*C7)+5)

Where: 
B8 is Gender (Male or Female)
C10 is Body Mass in Kilograms (Note that 1 kilogram is 2.204 lbs)
C9 is Height in Centimeters (Note that 1 inch is 2.53 centimeters)
C7 is Age in years

Activity Status Multipliers:

Sedentary - 1.1 * Predicted RMR 
Light Active - 1.2 * Predicted RMR
Active - 1.3 * Predicted RMR
Labour Intensive - 1.4 * Predicted RMR

Activity Descriptors:
Sedentary - 2-5k steps per day
Light Active - 5-8k steps per day
Active - 8-12k steps per day
Labour Intensive - >12k steps per day

Predicted Total Daily Energy Expenditure Formula:

=(B18*B19+B22)

Where:

B18 is Predicted RMR
B19 is Activity Status Multiplier
B22 is Average Calories Expended Daily from Exercise (Note that this is calculated by multiplying the number of workouts per week by the average calories expended per workout divided by 7)

Multiplier Goal Coefficients:

Fat Loss: Multiply Predicted Total Daily Energy Expenditure by 0.8
Muscle Gain: Multiply Predicted Total Daily Energy Expenditure by 1.1
Maintenance: Multiply Predicted Total Daily Energy Expenditure by 1

Target Avg. Daily Energy Intake (kcal)is the product of predicted total daily energy expenditure and the multiplier goal coefficient.
Energy Availability is Target Avg. Daily Energy Intake divided by kilograms of fat-free mass.

Protein Target
Advisable to target a protein intake in grams per kilograms of fat-free mass per day of between 0.8-1.6
It could default to 1.2 g/kg/day but having a dropdown to self-select between this range would be good with annotation that lower intake slightly increases risk for fat-free mass loss during a fat loss emphasis and a higher intake than 1.2g/kg per day displaces other macronutrients but better ensures muscle mass defense and gain.

Once selected by user, multiply coefficient by fat-free mass in kilograms. Then, multiply the grams of protein by 4 where there are 4kcal/gram of protein. 
Subtract this value from the Target Average Daily Energy Intake calculated previously for remaining balance to determine fat and carbohydrate allotment.

Fat Target
An intake not less than 20% of the total daily energy target or 0.3 g/lb of bodyweight (0.6g/kg)
The upper bound could be 40% of the total daily energy target or 0.6g/lb of bodyweight (1.2g/kg)

Carbohydrate Target
The remaining calories could be allocated to carbohydrates by summing the calories from selected protein and fat, subtracting from the daily target, and then dividing by 4 where 1 gram of carbohydrate contains 4kcal/g.

Fiber could default to 14g/1000kcal
Base Fluid Intake could default to 40 ml/kg/day


The table presented showing all targets could be ranges like the following:
	
Target Energy Range (kcal):	+ or - 5% of value calculated rounded to the nearest 5
Protein (grams): + or - 5% of value calculated rounded to the nearest 5g
Fat (grams): + or - 5% of value calculated rounded to the nearest 5g	
Carbs (grams): + or - 5% of value calculated rounded to the nearest 5g			
Fiber (grams): + or - 2g of value calculated			
Fluid (ounces):	+ or - 5 oz of value calculated	

