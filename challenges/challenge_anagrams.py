# considerando que o requisito exige que se atinja a complexidade O(n log n)
# baseado na aula 2.3 pode -se utilizar Merge sort.
# merge e merge_sort obtidos através da aula 2.3
# disponivel em :
# https://github.com/tryber/sd-025-b-live-lectures/blob/lecture/cs/2.3/sort/merge_sort.py
# referencia IndexError:
# https://bobbyhadz.com/blog/python-indexerror-list-assignment-index-out-of-range#:~:text=The%20Python%20%22IndexError%3A%20list%20assignment,of%20the%20list%2C%20e.g.%20my_list.

def merge(left, right):
    merged = []
    left_p, right_p = 0, 0

    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            merged.append(left[left_p])
            left_p += 1
        else:
            merged.append(right[right_p])
            right_p += 1

    while left_p < len(left):
        merged.append(left[left_p])
        left_p += 1

    while right_p < len(right):
        merged.append(right[right_p])
        right_p += 1

    return merged


def merge_sort(info):
    if len(info) <= 1:
        return info

    mid = len(info) // 2
    left, right = merge_sort(info[:mid]), merge_sort(info[mid:])
    return merge(left, right)


def is_anagram(first_string, second_string):
    if (
        not first_string
        or not second_string
        or first_string == ''
        or second_string == ''
    ):
        return (first_string, second_string, False)

    f_string = list(first_string.lower())
    s_string = list(second_string.lower())

    mix_one = "".join(merge_sort(f_string))
    mix_two = "".join(merge_sort(s_string))

    return (mix_one, mix_two, mix_one == mix_two)
