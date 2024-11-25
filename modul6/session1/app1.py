class Product:

    def __init__(self, name=None, price=None, stock=None):
        if name and price and stock:
            pass
        else:
            self.name, self.price, self.stock = input("Give (name, price, stock) for product:").split(',')

    def __repr__(self):
        return (f"{self.__class__.__name__}: ({self.name},{self.price},{self.stock})")

    def __str__(self):
        return (f"Nume: {self.name} \n"
                f"Pret: {self.price} \n"
                f"Stoc: {self.stock} \n"
                f"{40 * '-'}")


class Category:

    def __init__(self, name: str):
        self.category_name = name
        self.products = []

    def add_product(self):
        # product = input("give product:")
        product = Product()
        self.products.append(product)

    def __str__(self):
        return f"--- {self.category_name.capitalize()}"


class Shop:
    main_menu_message = 'Bun venit la magazinul Pycharm'
    main_menu_dict = {1: "Category", 2: "Produse", 3: "Iesire"}
    product_menu_dict = {1: "Adaugare", 2: "Vizualizare", 3: "Iesire la meniul principal"}
    categories = [Category('pantofi'), Category('haine')]

    def products_menu(self):
        # code here
        while True:
            print(40 * '=' + '\n' + Product.__name__.upper().center(40, '=') + '\n' + 40 * '=')
            for key, value in self.product_menu_dict.items():
                print(f'\t{key}: {value}')
            selection = input('Introduceti optiunea:')
            if selection == '1':
                category = input("Introduceti numele categoriei:")
                product = input("Introduceti numele produsului")
                price = input("Introduceti pretul produsului")
                stock = input("Introduceti stocul produsului")
                for cat in self.categories:
                    if cat.category_name == category:
                        cat.products.append(Product(product, price, stock))
            elif selection == '2':
                print(self.categories)
            elif selection == '3':
                break

    def run(self):
        while True:
            print(self.main_menu_message)
            for key, value in self.main_menu_dict.items():
                print(f'\t{key}: {value}')
            selection = input('Alegeti optiunea:')
            if selection == '1':
                print(40 * '=' + '\n' + Category.__name__.upper().center(40, '=') + '\n' + 40 * '=')
                for category in self.categories:
                    print(category)
            elif selection == '2':
                self.products_menu()
