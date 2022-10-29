def delete(list_, index=None):
    copy_list = list_.copy()
    if index is None or index > (len(copy_list)-1):
        new_list = copy_list[:len(copy_list)-1]
        return new_list
    else:
        first_half = copy_list[:index]
        second_half = copy_list[index+1:]
        new_list = first_half + second_half
        return new_list



print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
