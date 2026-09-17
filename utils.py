class utils:

    def reversed( num : int) -> int:
        str_num = str(num)
        reversed_str_num = str_num[::-1]
        if num < 0:
            reversed_str_num  = "-" + reversed_str_num[:-1]
        return int(reversed_str_num)

    def formatter(num : int) -> tuple[str, str]:
        num_oct : int; num_bin : int
        str_oct : str; str_bin : str

        num_oct = num; num_bin = num
        str_oct = "" ; str_bin = ""

        while (num_oct != 0):
            rem = num_oct % 8
            str_oct = str(rem) + str_oct
            num_oct = num_oct // 8

        while (num_bin != 0):
                    rem = num_bin % 2
                    str_bin = str(rem) + str_bin
                    num_bin = num_bin // 2

        return str_bin, str_oct
