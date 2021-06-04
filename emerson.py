# Emerson Efficiency Plan

nrph = float(input('Normal rate / hour : '))
sopw = float(input('Standard ouput / week (unit) : '))
stpu = float(input('Standard time / unit (hour) : '))
worker = int(input('Quantity of worker/s : '))

rphg = nrph * stpu * sopw # Rate / hour guaranteed

for each in range(worker) :
  print(f'\nWorker {each+1} :')
  output = float(input('Output / week (unit) : '))
  efficiency = (output / sopw) * 100
  if efficiency < 67 :
    pbonus = 0
  elif 100 > efficiency >= 67 :
    pbonus = 100 - efficiency
  else :
    pbonus = efficiency - 100 + 20
  incentive = (pbonus/100) * rphg
  wpw = rphg + incentive
  print(f'Efficiency : {efficiency}')
  print(f'Percentage of bonus on wages : {pbonus}')
  print(f'Rate / hour guaranteed : {rphg}')
  print(f'Incentive : {incentive}')
  print(f'Wages / week : {wpw}')
  each += 1
