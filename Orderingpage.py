#   ____  _____  _____  ______ _____  _____ _   _  _____     _____        _____ ______ 
#  / __ \|  __ \|  __ \|  ____|  __ \|_   _| \ | |/ ____|   |  __ \ /\   / ____|  ____|
# | |  | | |__) | |  | | |__  | |__) | | | |  \| | |  __    | |__) /  \ | |  __| |__   
# | |  | |  _  /| |  | |  __| |  _  /  | | | . ` | | |_ |   |  ___/ /\ \| | |_ |  __|  
# | |__| | | \ \| |__| | |____| | \ \ _| |_| |\  | |__| |   | |  / ____ \ |__| | |____ 
#  \____/|_|  \_\_____/|______|_|  \_\_____|_| \_|\_____|   |_| /_/    \_\_____|______|

from pyscript import display, document, window

#----------------------------------------------------------#
#            CUSTOMER ORDER CHOICE AND QUANTITY            #
#----------------------------------------------------------#

icecream_value = 0 # These are the initial values of the quantities.
cake_value = 0
milkshake_value = 0
yogurt_value = 0
pudding_value = 0

def increaseicecream(e):
    global icecream_value # Global allows a function affect variables created outside the function.
    if icecream_value < 10:
        icecream_value += 1
    display(icecream_value, target="icecreamquantity", append=False) # Append replaces the existing element instead of just adding the new value next to the previous one.

def decreaseicecream(e):
    global icecream_value
    if icecream_value > 0:
        icecream_value -= 1
    display(icecream_value, target="icecreamquantity", append=False)

def increasecake(e):
    global cake_value
    if cake_value < 10:
        cake_value += 1
    display(cake_value, target="cakequantity", append=False)

def decreasecake(e):
    global cake_value
    if cake_value > 0:
        cake_value -= 1
    display(cake_value, target="cakequantity", append=False)

def increasemilkshake(e):
    global milkshake_value
    if milkshake_value < 10:
        milkshake_value += 1
    display(milkshake_value, target="milkshakequantity", append=False)

def decreasemilkshake(e):
    global milkshake_value
    if milkshake_value > 0:
        milkshake_value -= 1
    display(milkshake_value, target="milkshakequantity", append=False)

def increaseyogurt(e):
    global yogurt_value
    if yogurt_value < 10:
        yogurt_value += 1
    display(yogurt_value, target="yogurtquantity", append=False)

def decreaseyogurt(e):
    global yogurt_value
    if yogurt_value > 0:
        yogurt_value -= 1
    display(yogurt_value, target="yogurtquantity", append=False)

def increasepudding(e):
    global pudding_value
    if pudding_value < 10:
        pudding_value += 1
    display(pudding_value, target="puddingquantity", append=False)

def decreasepudding(e):
    global pudding_value
    if pudding_value > 0:
        pudding_value -= 1
    display(pudding_value, target="puddingquantity", append=False)

#----------------------------------------------------------#
#                      ORDER SUMMARY                       #
#----------------------------------------------------------#

def view_details(e):
    cakeprice = cake_value * 187.0
    icecreamprice = icecream_value * 70.0
    milkshakeprice = milkshake_value * 59.0
    yogurtprice = yogurt_value * 87.0
    puddingprice = pudding_value * 105.0
    customerN = document.getElementById('customer').value
    customerA = document.getElementById('address').value
    customerC = document.getElementById('customercontact').value

    notaxprice = cakeprice + icecreamprice + milkshakeprice + yogurtprice + puddingprice

    if notaxprice == 0:
        display("Please select item/s !", target="totalpricevalue", append=False)
    else:
        totalprice = round((notaxprice + ((0.6 / notaxprice) * 100)), 2)
        display(f'Your total is {totalprice}', target="totalpricevalue", append=False)

    if customerN == '' :
        display("Please complete the form !", target="customerdetails", append=False)
    if customerA == '' :
        display("Please complete the form !", target="customerdetails", append=False)
    if customerC == '' :
        display("Please complete the form !", target="customerdetails", append=False)
    else:
        display(f'Please confirm details: order for {customerN} to {customerA}. If neccessary, we will contact {customerC}', target="customerdetails", append=False)

    button = document.getElementById("placeorderbtn")
    if notaxprice == 0:
        button.setAttribute("disabled", True)
    if customerN == '' :
        button.setAttribute("disabled", True)
    if customerA == '' :
        button.setAttribute("disabled", True)
    if customerC == '' :
        button.setAttribute("disabled", True)
    else:
        button.removeAttribute("disabled")

def place_order(e):
    window.location.reload()