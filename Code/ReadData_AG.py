import json,pandas as pd
"""#import pandas as pd
fname = "../../Data/yelp_academic_dataset_business.json"
unformated_data = list()
with open(fname,encoding="utf-8") as f:
    line = f.readlines()
    unformated_data.append(line)
data_list = list()
unformated_data = unformated_data[0]
for _dict in unformated_data:
    data_list.append(_dict)
print(data_list[1])

business=pd.DataFrame.from_dict(list(iter(data_list).iteritems()), orient='columns', dtype=None)
print(business)
#pd.dataframe(data_list)"""

#Reading Business Data
business=pd.DataFrame.from_csv("../../Data/yelp_academic_dataset_business.csv")
business.drop(['type','postal_code','latitude','longitude','review_count','attributes','address','is_open','hours','stars'],inplace=True,axis=1)
business.index.name='neighborhood'
business.reset_index(inplace=True)
business.drop(business.columns[[0]],inplace=True,axis=1)
business=business.loc[business['state']=='NC']
#print(business)

#Reading Review Data
review=pd.DataFrame.from_csv("../../Data/review.csv")
#business.drop(['type','postal_code','latitude','longitude','review_count','attributes','address','is_open','hours'],inplace=True,axis=1)
#business.index.name='reviewid'
#business.reset_index(inplace=True)
#business.drop(business.columns[[0,4,5,6,7,8,9,10]],inplace=True,axis=1)
#print(review)

br=business.merge(review,on='business_id',how='inner')
user_mapping = {}
user_mapping_code = 0
business_mapping = {}
business_mapping_code = 0
for i in range(br.shape[0]):
    if br.loc[i,'stars']>=3:
        br.loc[i,'stars_m']=br.loc[i,'stars']+(0.1*br.loc[i,'funny']+.6*br.loc[i,'useful']+0.3*br.loc[i,'cool'])/(br.loc[i,'funny']+br.loc[i,'useful']+br.loc[i,'cool']+1)
    else:
        br.loc[i,'stars_m']=br.loc[i,'stars']-(0.1*br.loc[i,'funny']+.6*br.loc[i,'useful']+0.3*br.loc[i,'cool'])/(br.loc[i,'funny']+br.loc[i,'useful']+br.loc[i,'cool']+1)
#br['stars']=[br['stars']+(0.1*br['funny']+.6*br['useful']+0.3*br['cool'])/(br['funny']+br['useful']+br['cool']+1) if br['stars']>=3 else br['stars']-(0.1*br['funny']+.6*br['useful']+0.3*br['cool'])/(br['funny']+br['useful']+br['cool']+1) for x in df['stars']]
    user_name=br.loc[i,'user_id']
    if(user_name not in user_mapping.keys()):
        user_mapping_code += 1
        user_mapping[user_name] = user_mapping_code
    br.loc[i,'user_code'] = user_mapping[user_name]

    business_name = br.loc[i,'business_id']
    if(business_name not in business_mapping.keys()):
        business_mapping_code += 1
        business_mapping[business_name] = business_mapping_code
    br.loc[i,'business_code'] = business_mapping[business_name]

br.to_csv("../../Data/merged_BR3.csv")
