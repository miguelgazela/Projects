credit_card = "4261500027050504"

ind_nums = list(credit_card)
checksum_nums = ind_nums[::2]
other_nums = ind_nums[1::2]

# convert strings to int
for i in range(len(checksum_nums)):
    checksum_nums[i] = int(checksum_nums[i])

for i in range(len(other_nums)):
    other_nums[i] = int(other_nums[i])

for i in range(len(checksum_nums)):
    num = checksum_nums[i]
    res = checksum_nums[i] * 2

    if res >= 10:
        q, r = divmod(num, 10)
        checksum_nums.append(q)
        checksum_nums.append(r)
        del checksum_nums[i]
    else:
        checksum_nums[i] = res

print checksum_nums
print other_nums