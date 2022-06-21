# To know the price of a ticket
x = float(input("What's you trip's distance? Km:"))
a = x * 0.5
b = x * 0.45
if x <= 200:
    print('Your trip has {:.1f} Km, so you will pay 50 cents per Km \n Your trip is R$:{:.2f} Reais'.format(x, a))
else:
    print('Your trip has {:.1f} Km, so you will pay 45 cents per Km \n Your trip is R$:{:.2f} Reais'.format(x, b))
print('Have a good trip!')
