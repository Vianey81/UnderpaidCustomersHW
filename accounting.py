def customer_expectation(customer_name,customer_melons,customer_paid):
    melon_cost = 1.00
    customer_expected = customer_melons * melon_cost
    if customer_expected > customer_paid:
        print customer_name, "paid {:.2f}, expected {:.2f}".format(
            customer_paid, customer_expected)
        print "{} has underpaid for their melons.".format(customer_name)

    elif customer_expected < customer_paid:
        print customer_name, "paid {:.2f}, expected {:.2f}".format(
            customer_paid, customer_expected)
        print "{} has overpaid for their melons.".format(customer_name)
        
the_file = open('customer-orders.txt')

for line in (the_file):
        line = line.rstrip()
        line = line.split('|')

        customer_name = line[1]
        customer_melons = line[2]
        customer_paid = line[3]
        customer_expectation(customer_name,int(customer_melons),float(customer_paid))

the_file.close()
