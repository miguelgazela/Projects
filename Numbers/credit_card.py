def main():
    credit_card_num = list(raw_input("Credit card #: "))
    checksum_nums = [int(v) * 2 for i, v in enumerate(credit_card_num) if i % 2 == 0]
    checksum = 0

    for i, v in enumerate(credit_card_num):
        checksum += (i % 2 != 0 and int(credit_card_num[i]) or 0)

    for v in checksum_nums:
        if v >= 10:
            q, r = divmod(v, 10)
            checksum += q + r
        else:
            checksum += v

    if checksum % 10 == 0: print "The credit card number is valid."
    else: print "The credit card number is not valid!"


if __name__ == "__main__":
    main()
