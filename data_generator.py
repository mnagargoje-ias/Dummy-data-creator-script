import random
import pandas as pd
import datetime

def random_date():
    start = datetime.date(2023, 1, 1)
    end = datetime.date(2023, 2, 1)
    
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def get_data():
    params = {}
    params['average_in_view_time'] = random.random()*10
    params['campaign_id'] = random.randint(1, 10000)
    params['publisher_id'] = random.randint(1, 10000)
    params['placement_id'] = random.randint(1, 10000)
    params['device_type'] = random.choice(["mobile", "desktop", "console", "unknown"])
    params['measurement_source_type'] = random.choice(["IAS", "PMI"])
    params['media_type'] = random.choice(['display', 'video'])
    params['team_id'] = random.choice([23797])
    params['media_type_id'] = random.choice([121,221,212,122,222,921,131,132])
    params['quality_impression'] = random.choice([True, False])
    params['hit_date'] = random_date()
    params['in_view_passed_imps'] = random.choice([0, 1])
    params['not_in_view_passed_imps'] = 1 if params['in_view_passed_imps']==0 else 0
    #params['in_view_passed_imps'] = random.randint(1,50)
    #params['not_in_view_passed_imps'] = random.randint(1,50)
    #params['gross_ias_imps'] = random.randint(0, 50)
    #params['gross_pm_imps'] = random.randint(0, 50) if params['gross_ias_imps']==0 else 0
    #params['gross_pm_yt_bs_imps'] = random.randint(0, 50) if params['gross_pm_imps']==0 else 0
    #params['gross_pm_yt_imps'] = random.randint(0, 50) if params['gross_pm_yt_bs_imps']==0 else 0
    #params['pm_yt_bs_viewability_common_givt_imps'] = random.randint(0, 50) if params['gross_pm_yt_imps']==0 else 0
    #params['non_compliant_ads'] = random.randint(0, 50) if params['pm_yt_bs_viewability_common_givt_imps']==0 else 0

    return params

schema = {}
for i in get_data():
    schema[i] = []
print(schema)

df = pd.DataFrame(schema)

#Total number of records
n = 10000 

for i in range(n):
    df.loc[len(df)]=get_data()

#writes into the file
df.to_csv('snowflake_sample_raw9.csv', index=False)
