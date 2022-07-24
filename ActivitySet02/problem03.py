def get_cs():
    cs = input('enter a string: ')
    return cs


def cs_to_lst(cs):
    cs = cs.split(';')
    lst = []
    for i in cs:
        a = i.split('=')
        a = tuple(a)
        lst.append(a)
    return lst


def main():
    cs = get_cs()
    lst = cs_to_lst(cs)
    print(lst)


if __name__ == '__main__':
    main()
    
