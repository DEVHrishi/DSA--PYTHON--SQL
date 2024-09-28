def max_product(arr):
    arr_len = len(arr)
    if arr_len < 2:
        print('No pair exist')
        return 
    
    x = arr[0]; y = arr[1]

    for i in range(0, arr_len):
        for j in range(i+1, arr_len):
            if (arr[i]*arr[j] > x*y):
                x = arr[i]; y = arr[j]
    
    return x, y

arr = [1, 2, 3, 4, 7, 0, 8, 4]
print('Original array:',arr)
print('Maximum product pair is:', max_product(arr))


