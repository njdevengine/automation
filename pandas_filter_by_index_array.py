s_d = [0,4,8,12,16]
o_d = [1,5,9,13,17]
c_d = [2,6,10,14,18]
f_d = [3,7,11,15,19]

all_reps = list(weekly.index)

for i in range(len(all_reps)):
  subs_date = list(weekly.loc[all_reps[i]][s_d])
  offer_date = list(weekly.loc[all_reps[i]][o_d])
  crd_date = list(weekly.loc[all_reps[i]][c_d])
  fund_date = list(weekly.loc[all_reps[i]][f_d])
