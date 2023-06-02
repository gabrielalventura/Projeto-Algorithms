def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# condição de parada word = null ou empty
# retorno chama a função se movendo em direção ao centro,
#  um para a direta e um para a esquerda;
