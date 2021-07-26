import math

def pizza_party():
    while True:
        people = input("How many People? ")
        pizzas = input("How many Pizzas? ")
        slices = input("How many slices per Pizza? ") 
        try: 
            #Convert the inputs into integer values
            ppl = int(people)
            pz = int(pizzas)
            s = int(slices)
            #Total number of slices
            ts = s * pz
            print(f"{ts} slices in total")
            #Available slices for each person
            spp = math.floor(ts / ppl)
            if spp == 1:
                #modifies the output for if there is 1 slice per person
                print(f"To start, there will be {spp} slice per person")
            elif ts < ppl:
                #Handles for if there are too many people
                print(f"There are more people than slices")
            else:
                print(f"To start, there will be {spp} slices per person")
            #Left Over Slices
            lo = ts - (spp * ppl)
            if ts < ppl:
                print("time to make a tough decision")
            else:
                #Handle singular vs. Plural in the output statement
                if lo ==1:
                    print(f"{lo} slice will be left over")
                else:
                    print(f"{lo} slices will be left over")
          
        except ValueError:
            print("Must Enter Numeric Values for People, Slices, and Pizzas")  


pizza_party()
