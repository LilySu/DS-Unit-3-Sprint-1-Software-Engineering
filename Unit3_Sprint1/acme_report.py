            
    def generate_products(num_products):
        firstnamelist = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        lastnamelist = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        names = []
        prices = []
        weights = []
        flammabilities = []
        for i in range (0, num_products):
            name = random.choice(firstnamelist) + ' ' + random.choice(lastnamelist)
            price = random.randint(5, 100)
            weight = random.randint(5, 100)
            flammability = random.uniform(0, 2.5)
            names.append(name)
            prices.append(price)
            weights.append(weight)
            flammabilities.append(flammability)
    
     def inventory_report(generate_products):
        firstTimeNameInList = set()
        uniqueNames = []
        for i in names:
            if i not in firstTimeNameInList:
                uniqueNames.append(i)
                firstTimeNameInList.add(i)
        products = {}
        for i in range(len(names)):
            products[names[i]] = prices[i], weights[i], flammabilities[i]
        print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
        print('Unique product names: {}'.format(len(uniqueNames)))
        print('Average price {}'.format(mean(prices)))
        print('Average weight {}'.format(mean(weights)))
        print('Average flammability:{}'.format(mean(flammabilities)))    


    if __name__ == '__main__':
         inventory_report(generate_products(30))