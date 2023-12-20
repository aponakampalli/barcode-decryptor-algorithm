def barcodeAlgorithm(barcode):
    encryptPairs = {
    '0': '0',
    '1': '2',
    '2': '4',
    '3': '6',
    '4': '8',
    '5': '0',
    '6': '2',
    '7': '4',
    '8': '6',
    '9': '8'
    }
    decoded = []
    chunk = barcode.split('#')
    chunk = [nums for nums in chunk if nums]

    for x in range(0, len(chunk)):
        nums = chunk[x]
        if x > 0 and '!' in nums:
            decoded.append(nums.replace('!','') + decoded[x - 1])
        elif x > 0 and '^' in nums:
            decoded.append(nums.replace('^',''))
            decoded[x-1] = decoded[x - 1][::-1]
        elif x > 0 and '%' in nums:
            decoded.append(nums.replace('%',''))
            allVal = [*decoded[x-1]]
            decrypt = [encryptPairs[val] for val in allVal]
            decoded[x - 1] = ''.join(decrypt)
        else:
            if x == 0 and (('%' or '^' or '!') in nums):
                nums = nums.replace('!','')
                nums = nums.replace('^','')
                nums = nums.replace('%','')
                decoded.append(nums)
            else:
                decoded.append(nums)
        print(decoded)


    return ''.join(decoded)

def allBarcode(series):
    return [barcodeAlgorithm(barcode) for barcode in series]

if __name__ == '__main__': 
    challenge = ["#12#34!#59^#67%#",
        "#0%#1%#2%#3%#4%#5%#6%#7%#8%#9%#"]
    print(allBarcode(challenge))
    #['1221430867', '0246802469']