from classes.request import Request
from function.main import main
from classes.initiation.store import store
from classes.initiation.shop import shop


while True:
    print("=" * 100)
    a = input(f"Напишите запрос\n")
    if a == 'end':
        break

    request = Request(a)
    main(request, shop, store)
