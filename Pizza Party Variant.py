
import math

def pizza_party():
    while True:
        people = input("How many people at this party?")
        slices = input("How many slices will each person want?")
        try:
            #Convert the inputs into integer values
            ppl = int(people)
            s = int(slices)
            #Calculate the total number of slices desired
            total = ppl * s
            #Recommend small pie based on total number of slices
            if total <= 6:
                #Recommend Small
                lo = 6 - total
                if lo == 1:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 small pizza at Pequod's\nwith {lo} slice left over.")
                else:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 small pizza at Pequod's\nwith {lo} slices left over.")
            elif total <= 8:
                #Recommend Medium
                lo = 8 - total
                if lo == 1:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 medium pizza at Pequod's\nwith {lo} slice left over.")
                else:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 medium pizza at Pequod's\nwith {lo} slices left over.")
            elif total <= 10:
                #Recommend Large
                lo = 10 - total
                if lo == 1:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 large pizza at Pequod's\nwith {lo} slice left over.")
                else:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 large pizza at Pequod's\nwith {lo} slices left over.")
            elif total <= 12:
                #Recommend Extra Large
                lo = 12 - total
                if lo == 1:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 extra large pizza at Pequod's\nwith {lo} slice left over.")
                else:
                    print(f"For your party you'll need {total} slices,\nthis can be covered by 1 extra large pizza at Pequod's\nwith {lo} slices left over.")
            else:
                #Recommend Multiple Pies if total is too high
                pies = total/12
                XLpies = math.floor(pies)
                lo = total%12
                #Determine recommendation based off the number of left over slices
                if lo == 0:
                    print(f"{XLpies} Extra Large Pies will be just right!")
                elif lo <= 6:
                    if lo == 1:
                        print(f"You'll need {XLpies} Extra Large Pizzas\nand 1 small pizza(to cover the {lo} left over slice)")
                    else:
                        print(f"You'll need {XLpies} Extra Large Pizzas\nand 1 small pizza(to cover the {lo} left over slices)")
                elif lo <= 8:
                    print(f"You'll need {XLpies} Extra Large Pizzas\nand 1 medium pizza(to cover the {lo} left over slices)")
                elif lo <= 10:
                    print(f"You'll need {XLpies} Extra Large Pizzas\nand 1 large pizza(to cover the {lo} left over slices)")
                       
        except ValueError:
            print("Must Enter Numeric Values for People & Slices")


pizza_party()
