Лабораторын ажил: FP Snake Game

## Зорилго

1. PyGame ашиглан тоглоомын үндсэн элементүүдийг модульчлан зохион байгуулах.
2. Functional Programming (FP) зарчмуудыг ашиглах: pure functions, map, filter, reduce.
3. Snake Game-ын логикийг функцийг ашиглаж бичих.


## 🔗 Хэрэгтэй линк

- [PyGame Documentation](https://www.pygame.org/docs/)
- [Python `map`, `filter`, `reduce`](https://docs.python.org/3/library/functions.html)



## Мөрдөх дүрмүүд

1. **Pure functions** ашиглах (global variable-гүй, side-effect багатай)
2. **Higher-order functions**: map, filter, reduce ашиглах
3. **Modular code**: Тоглоомын логик тус бүрт зориулсан функц тусдаа байх
4. **Коммент бичих**: Функц бүрийн дотор юу хийхийг мөр мөрөөр тайлбарлах
5. **Snake болон Food-ийн байрлалыг list/tuple-д хадгалах**
6. **Collision болон food check**-ийг тусдаа функцээр шийдэх

map()

List эсвэл iterable-д агуулагдах элемент бүрт function хэрэглэх, шинэ list үүсгэх+

Жишээ: list(map(lambda x: x\*\*2, [1,2,3])) # [1,4,9]

filter()

List эсвэл iterable-д агуулагдах элементийг тодорхой нөхцөлөөр шүүх, шинэ list үүсгэх

Жишээ: list(filter(lambda x: x%2==0, [1,2,3,4])) # [2,4]

reduce()

List эсвэл iterable-ийн элементүүдийг нэг утганд нэгтгэх

Жишээ: from functools import reduce
reduce(lambda acc, x: acc+x, [1,2,3], 0) # 6

random модуль

Санамсаргүй утга үүсгэх

Snake Game-д хоолны байрлалд ашиглана

Жишээ: import random
random.randrange(0, 600, 20) # 0,20,...580

import random
random.randrange(0, 600, 20) # 0,20,...580