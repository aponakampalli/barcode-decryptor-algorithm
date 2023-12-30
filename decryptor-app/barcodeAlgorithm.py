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
    chunk = chunk[1:-1]
    key = '^!%'
    
    if len(chunk) > 0:
        first = chunk[0]
        first = first.replace('!','')
        first = first.replace('^','')
        first = first.replace('%','')
        decoded.append(first)

    for x in range(1, len(chunk)):
        nums = chunk[x]
        block = ''
        for y in range(0, len(nums)):
            char = nums[y]
            if char in key:
                if char == '^':
                    decoded[x-1] = decoded[x - 1][::-1]
                if char == '%':
                    allVal = [*decoded[x-1]]
                    decrypt = [encryptPairs[val] for val in allVal]
                    decoded[x - 1] = ''.join(decrypt)
                if char == '!':
                    block += decoded[x - 1]
            else:
                block += char
        decoded.append(block)
    return ''.join(decoded)


def allBarcode(series):
    return [barcodeAlgorithm(barcode) for barcode in series]

if __name__ == '__main__': 
    challenge = ["#12#34!#59^#67%#",
        "#0%#1%#2%#3%#4%#5%#6%#7%#8%#9%#", 
        '##1#3#9%4^481%3^64#3#6#2^58%6%6%619!6!86^0#6%3137!8!55^5#1#6#19#']
    print(allBarcode(challenge))
    #['1221430867', '0246802469']
    #'#^0   #1  #1528^12!9%7    #4  #48494!3%23^088^8%1     #1%7251%27^70%7 #596!17348  #044842!8   #3!0%9089!02893511#'