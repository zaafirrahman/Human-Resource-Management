# Taylor's Differential Piece Rate Plan

nrph = float(input('Normal rate / hour : '))
sopw = float(input('Standard ouput / week (unit) : '))
stpu = float(input('Standard time / unit (hour) : '))
worker = int(input('Quantity of worker/s : '))

rphg = nrph * stpu * sopw # Rate / hour guaranteed

for each in range(worker) :
  print(f'\nWorker {each+1} :')
  output = float(input('Output / week (unit) : '))
  if output < sopw :
    rate = 15
  else :
    rate = 20
  wpw = output * rate
  print(f'Rate : {rate}')
  print(f'Wages / week : {wpw}')
  each += 1
