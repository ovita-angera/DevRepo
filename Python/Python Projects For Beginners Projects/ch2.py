# a receipt printing program
# 
def main():
    # create a product name and its corresponding price
    p1_name, p1_price = "Maize", 139.75
    p2_name, p2_price = "Peas", 389.47
    p3_name, p3_price = "Beans", 79.99

    # create a company name and information
    company_name = "Quickmart supermarket"
    company_address = "277 Ngoingwa St."
    company_city = "Thika, Kiambu"

    # declare the ending message
    message = "Thanks for shopping with us today!"

    # create a top border
    print("*"*50)

    # display the company information
    print("*\t\t{}\t\t *".format(company_name).title())
    print("*\t\t{}\t\t *".format(company_address))
    print("*\t\t{}\t\t\t *".format(company_city))

    # print a line between sections
    print("="*50)

    # display the product information
    print("*\tProduct Name\tProduct Price\t\t *")

    # a print statement for each product
    print("*\t{}\t\t${}\t\t\t *".format(p1_name.title(), p1_price))
    print("*\t{}\t\t${}\t\t\t *".format(p2_name.title(), p2_price))
    print("*\t{}\t\t${}\t\t\t *".format(p3_name.title(), p3_price))

    # a line between sections
    print("="*50)

    # displaying the total amount due by the client
    print("*\t\t\tTotal\t\t\t *")

    # calculate the total
    total = p1_price + p2_price + p3_price
    print("*\t\t\t${}\t\t\t *".format(total))

    # print a line between sections
    print("="*50)

    # display the ending message
    print("*" + " "*48 + "*" + "\n*\t{}\t *\n".format(message) + "*" + " "*48 + "*")

    # display the bottom border
    print("*"*50)
    
if __name__ == "__main__":
    main()