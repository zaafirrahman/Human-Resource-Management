# Halsey Premium Plan

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
  if timesaved < 0 :
    timesaved = 0
  total_ts = output * timesaved
  incentive = total_ts * 0.5 * nrph
  wpw = rphg + incentive
  print(f'Time saved / unit : {timesaved}')
  print(f'Total time saved : {total_ts}')
  print(f'Rate / hour guaranteed : {rphg}')
  print(f'Incentive : {incentive}')
  print(f'Wages / week : {wpw}')
  each += 1
