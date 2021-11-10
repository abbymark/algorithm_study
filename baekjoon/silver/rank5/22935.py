n = int(input())

def convert(num):
  # breakpoint()
  count = (num - 15) // 14

  if num < 16:
    binary = bin(num)[2:]
    binary = binary.rjust(4, '0')

    print(binary.replace('0', 'V').replace('1', '딸기'))
  elif count % 2 == 0:
    rest = (num - 15)  % 14
    binary = bin(15 - rest)[2:]
    binary = binary.rjust(4, '0')

    print(binary.replace('0', 'V').replace('1', '딸기'))
  elif count % 2 == 1:
    rest = (num - 15) % 14
    binary = bin(rest + 1)[2:]
    binary = binary.rjust(4, '0')

    print(binary.replace('0', 'V').replace('1', '딸기'))

for i in range(n):
  convert(int(input()))