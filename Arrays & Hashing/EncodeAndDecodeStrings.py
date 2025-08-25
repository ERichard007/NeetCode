class Solution:

    def encode(self, strs: list[str]) -> str:
        newString = str()
        for word in strs:
            for char in word:
                newString += str(ord(char))
                newString += "*"
            newString += " "
        return newString

    def decode(self, s: str) -> list[str]:
        myList = []
        newString = str()
        decodeString = str()

        for char in s:
            if char == "*":
                decodeString += chr(int(newString))
                newString = str()
            elif char == " ":
                myList.append(decodeString)
                decodeString = str()
            else:
                newString += char

        return myList
    
    def encode2(self, strs: list[str]) -> str:
        newString = str()

        for word in strs:
            newString += str(len(word)) + "#" + word

        return newString

    def decode2(self, s: str) -> list[str]:
        decodedList = []
        num = str()
        i = 0

        while i < len(s):
            char = s[i]

            num = str()
            while (char != "#"):
                num += char
                i+=1
                char = s[i]

            num = int(num)

            cut = i+1
            decodedList.append(s[cut:cut+num])

            i = cut + num
            
        return decodedList



myList = ["neet","co#de","love","you"]
mySolution = Solution()

encodedList = mySolution.encode(myList)
decodedList = mySolution.decode(encodedList)

encodedList2 = mySolution.encode2(myList)
decodedList2 = mySolution.decode2(encodedList2)


print(myList)
print(encodedList)
print(decodedList)
print(encodedList2)
print(decodedList2)