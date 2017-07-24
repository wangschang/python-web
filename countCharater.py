
import pprint
import collections


def main():

    file_input =  raw_input('File Name: ')
    #print(file_input)
    with open(file_input, 'r') as info:
        #print(info.read())
        count = collections.Counter(info.read().upper())

    value = pprint.pformat(count)
    print(value)


if __name__ == "__main__":
    main()
