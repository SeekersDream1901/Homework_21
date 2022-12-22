def main(request, shop, store):
    if request.from_() == 'склад' and request.to() == 'магазин':
        try:
            if shop.get_free_space() >= request.amount() and shop.unique_items_count() <= shop.capacity:
                store.remove(request.product(), request.amount())
                shop.add(request.product(), request.amount())
                print(f"Нужное количество есть на складе")
                print(f"Курьер забрал {request.amount()} {request.product()} со склад")
                print(f"Курьер везет {request.amount()} {request.product()} со склад в магазин")
                print(f"Курьер доставил {request.amount()} {request.product()} в магазин")
                print(f"\nВ склад хранится:\n")
                for item in store.get_items():
                    print(f"{store.items[item]} {item}")
                print(f"\nВ магазин хранится:\n")
                for item in shop.get_items():
                    print(f"{shop.items[item]} {item}")
            else:
                print("В магазин недостаточно места, попобуйте что то другое")
        except Exception as e:
            print(e)

    elif request.from_() == 'магазин' and request.to() == 'склад':
        try:
            if store.get_free_space() >= request.amount():
                shop.remove(request.product(), request.amount())
                store.add(request.product(), request.amount())
                print(f"Нужное количество есть в магазин")
                print(f"Курьер забрал {request.amount()} {request.product()} из магазина")
                print(f"Курьер везет {request.amount()} {request.product()} из магазина на склад")
                print(f"Курьер доставил {request.amount()} {request.product()} на склад")
                print(f"\nВ магазин хранится:\n")
                for item in shop.get_items():
                    print(f"{shop.items[item]} {item}")
                print(f"\nВ склад хранится:\n")
                for item in store.get_items():
                    print(f"{store.items[item]} {item}")
            else:
                print("На складе недостаточно места, попобуйте что то другое")
        except Exception as e:
            print(e)

    else:
        print("Ничего не понятно, повторите запрос.")
