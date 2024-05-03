## Порівняння трьох алгоритмів сортування: злиттям, вставками та Timsort

    measurements for array size (x1000 times): 5
    insertion_sort: 0.00027141700411448255
    merge_sort: 0.0018397500025457703
    timsort: 0.00015412500215461478
    
    measurements for array size (x1000 times): 10
    insertion_sort: 0.0004746670019812882
    merge_sort: 0.004359083002782427
    timsort: 0.00016687499737599865
    
    measurements for array size (x1000 times): 50
    insertion_sort: 0.0020724170026369393
    merge_sort: 0.037381540998467244
    timsort: 0.0002968339977087453
    
    measurements for array size (x1000 times): 100
    insertion_sort: 0.00414558299962664
    merge_sort: 0.05978608300210908
    timsort: 0.00048099999548867345
    
    measurements for array size (x1000 times): 1000
    insertion_sort: 0.0683259579964215
    merge_sort: 0.7515116249996936
    timsort: 0.003049708000617102
    
    measurements for array size (x1000 times): 2000
    insertion_sort: 0.16195429200161016
    merge_sort: 1.631620666004892
    timsort: 0.008698250007000752
    
    measurements for array size (x1000 times): 5000
    insertion_sort: 0.6022181669977726
    merge_sort: 4.575305625003239
    timsort: 0.01889800000208197

![alt text](https://github.com/bingooo1337/goit-algo-hw-04/blob/main/img/img1.png?raw=true)
![alt text](https://github.com/bingooo1337/goit-algo-hw-04/blob/main/img/img2.png?raw=true)

З попередніх вимірювань видно, що на великих масивах алгоритми сортування мають значні відмінності у часі виконання:

- Для малих масивів (5, 10) алгоритм сортування вставками показує непоганий результат.
- На великих масивах помітно перевагу алгоритму Timsort над іншими. Час виконання Timsort набагато менший, ніж у інших алгоритмів.

Це підтверджує теоретичні оцінки складності алгоритмів:

- Складність сортування вставками - O(n^2), тому він працює добре на невеликих масивах, але зростає дуже швидко зі збільшенням розміру вхідного масиву.
- Складність сортування злиттям - O(n log n), що робить його більш ефективним для великих масивів порівняно з сортуванням вставками.
- Timsort поєднує обидва алгоритми, використовуючи сортування злиттям для обробки великих підмасивів та сортування вставками для малих підмасивів, що робить його ефективним на різних розмірах масивів.

### Отже, саме поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, особливо на великих масивах даних. Це пояснює чому програмісти у більшості випадків використовують вбудовані алгоритми сортування, які базуються на Timsort, замість написання власних реалізацій.