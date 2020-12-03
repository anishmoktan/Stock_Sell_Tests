port= {
  'AAPL': {
            "2020-11-16":[1,100],
            "2020-11-17":[2,100],
            "2020-11-18":[3,100],
            "2020-11-19":[4,100],
            "2020-11-18":[2,100],
            "2020-11-19":[1,100],
            "2020-11-20":[5,100]
          },
  'TSLA': {
            "2020-11-16":[1,100],
            "2020-11-17":[2,100],
            "2020-11-18":[3,100],
            "2020-11-19":[4,100]
          },
  'HOME':
          {
            "2020-11-16":[1,100],
            "2020-11-17":[2,100],
            "2020-11-18":[3,100],
            "2020-11-19":[4,100],
            "2020-11-18":[3,100],
            "2020-11-19":[4,100]
          }
  'CITI':
          {
            "2020-11-16":[1,100],
            "2020-11-17":[2,100],
            "2020-11-18":[3,100],
            "2020-11-19":[4,100]
          }
  }

def update_port(portfolio,date_today):
  updated_port={}
  for stock in portfolio:
    print(stock)
    access = portfolio[stock]
    quant=0

    for date in access:
      quant= quant + access[date][0]
    
    updated_port[stock]= {date_today:[quant,300]}

  return updated_port

    #   updated[stock]={date_today:x}

updated_portfolio= update_port(port,"Nov20")
#print(update_port(port,"Nov20"))
print(port)
print('\n Updated portfolio')
print(updated_portfolio)

def roi(raw_port,updated_port):
  total_raw_worth= 0
  total_updated_worth = 0

  for stock in raw_port:
    for date in raw_port[stock]:
      total_raw_worth= total_raw_worth +raw_port[stock][date][0] * raw_port[stock][date][1]
  for stock in updated_port:
    for date in updated_port[stock]:
      total_updated_worth= total_updated_worth +updated_port[stock][date][0] * updated_port[stock][date][1]
  
  return{"raw_total" : total_raw_worth,
         "updated_total" : total_updated_worth,
         "ROI" : (total_updated_worth-total_raw_worth)/total_raw_worth}

print(roi(port,updated_portfolio))

if (roi(port,updated_portfolio)["raw"]) == 2100:
  print("ALMAOAO")
