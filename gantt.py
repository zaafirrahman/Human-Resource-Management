# Gantt Task and Bonus Plan

nrph = float(input('Normal rate / hour : '))
sopw = float(input('Standard ouput / week (unit) : '))
stpu = float(input('Standard time / unit (hour) : '))
worker = int(input('Quantity of worker/s : '))

rphg = nrph * stpu * sopw # Rate / hour guaranteed

for each in range(worker) :
  print(f'\nWorker {each+1} :')
  output = float(input('Output / week (unit) : '))
  timestdrt = output * 10
  if output < sopw :
    wa = rphg
    incentive = 0
  else :
    wa = nrph * timestdrt
    incentive = 0.2 * wa
  wpw = wa + incentive
  rpu = wpw / output
  print(f'Time standard allowed : {timestdrt}')
  print(f'Wages allowed : {wa}')
  print(f'Incentive : {incentive}')
  print(f'Wages / week : {wpw}')
  print(f'Rate / unit : {rpu}')
  each += 1
