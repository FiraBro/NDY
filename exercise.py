products_on_sale = ['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4']


sale_prices=[100, 120, 135, 150]

quantities=[1000, 1500, 1300]

# for chair_type in products_on_sale:
#     for price in sale_prices:
#         for quantity in quantities:
#             print ([chair_type, price*quantity])


comp_list = [price * quantity for price in sale_prices for quantity in quantities]
print(comp_list)