# Rowan Premium Plan

nrph = float(input('Normal rate / hour : '))
sopw = float(input('Standard ouput / week (unit) : '))
stpu = float(input('Standard time / unit (hour) : '))
worker = int(input('Quantity of worker/s : '))

rphg = nrph * stpu * sopw # Rate / hour guaranteed

for each in range(worker) :
  print(f'\nWorker {each+1} :')
  output = float(input('Output / week (unit) : '))
  timetaken = float(input('Time taken / unit : '))
  timesaved = stpu - timetaken
  ttpu = (timetaken / 10) * 100
  tspu = 100 - ttpu
  if tspu < 0 :
    tspu = 0
  incentive = ((100 + tspu) * nrph) / 100
  wpw = sopw * stpu * incentive
  print(f'Time saved / unit : {timesaved}')
  print(f'Percentage of time taken / unit : {ttpu}')
  print(f'Percentage of time saved / unit : {tspu}')
  print(f'Rate / hour guaranteed : {rphg}')
  print(f'Incentive : {incentive}')
  print(f'Wages / week : {wpw}')
  each += 1
