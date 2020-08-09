import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('data.csv')

mobile_brand_list = df['Mobile Brand'].to_list()
avg_rating_list = df['Average Rating'].to_list()

mobile_brand_mean = statistics.mean(mobile_brand_list)
avg_rating_mean = statistics.mean(avg_rating_list)

mobile_brand_median = statistics.median(mobile_brand_list)
avg_rating_median = statistics.median(avg_rating_list)

mobile_brand_mode = statistics.mode(mobile_brand_list)
avg_rating_mode = statistics.mode(avg_rating_list)

mobile_brand_std_deviation = statistics.stdev(mobile_brand_list)
avg_rating_std_deviation = statistics.stdev(avg_rating_list)

print('mean,median,mode is {},{},{} respectively'.format(mobile_brand_mean,mobile_brand_median,mobile_brand_mode))
print('mean,median,mode is {},{},{} respectively'.format(avg_rating_mean,avg_rating_median,avg_rating_mode))

mobile_brand_first_std_deviation_start,mobile_brand_first_std_deviation_end = mobile_brand_mean-mobile_brand_std_deviation,mobile_brand_mean+mobile_brand_std_deviation
mobile_brand_second_std_deviation_start,mobile_brand_second_std_deviation_end = mobile_brand_mean-(2*mobile_brand_std_deviation),mobile_brand_mean+(2*mobile_brand_std_deviation)
mobile_brand_third_std_deviation_start,mobile_brand_third_std_deviation_end = mobile_brand_mean-(3*mobile_brand_std_deviation),mobile_brand_mean+(3*mobile_brand_std_deviation)

avg_rating_first_std_deviation_start,avg_rating_first_std_deviation_end = avg_rating_mean-avg_rating_std_deviation,avg_rating_mean+avg_rating_std_deviation
avg_rating_second_std_deviation_start,avg_rating_second_std_deviation_end = avg_rating_mean-(2*avg_rating_std_deviation),avg_rating_mean+(2*avg_rating_std_deviation)
avg_rating_third_std_deviation_start,avg_rating_third_std_deviation_end = avg_rating_mean-(3*avg_rating_std_deviation),avg_rating_mean+(3*avg_rating_std_deviation)

mobile_brand_list_of_data_within_1_std_deviation = [result for result in mobile_brand_list if result>mobile_brand_first_std_deviation_start and result<mobile_brand_first_std_deviation_end]
mobile_brand_list_of_data_within_2_std_deviation = [result for result in mobile_brand_list if result>mobile_brand_second_std_deviation_start and result<mobile_brand_second_std_deviation_end]
mobile_brand_list_of_data_within_3_std_deviation = [result for result in mobile_brand_list if result>mobile_brand_third_std_deviation_start and result<mobile_brand_third_std_deviation_end]

avg_rating_list_of_data_within_1_std_deviation = [result for result in avg_rating_list if result>avg_rating_first_std_deviation_start and result<avg_rating_first_std_deviation_end]
avg_rating_list_of_data_within_2_std_deviation = [result for result in avg_rating_list if result>avg_rating_second_std_deviation_start and result<avg_rating_second_std_deviation_end]
avg_rating_list_of_data_within_3_std_deviation = [result for result in avg_rating_list if result>avg_rating_third_std_deviation_start and result<avg_rating_third_std_deviation_end]

print('{}% of data for mobile brands lies within first standard deviation'.format(len(mobile_brand_list_of_data_within_1_std_deviation)*100.0/len(mobile_brand_list)))
print('{}% of data for mobile brands lies within second standard deviation'.format(len(mobile_brand_list_of_data_within_2_std_deviation)*100.0/len(mobile_brand_list)))
print('{}% of data for mobile brands lies within third standard deviation'.format(len(mobile_brand_list_of_data_within_3_std_deviation)*100.0/len(mobile_brand_list)))

print('{}% of data for average rating lies within first standard deviation'.format(len(avg_rating_list_of_data_within_1_std_deviation)*100.0/len(avg_rating_list)))
print('{}% of data for average rating lies within second standard deviation'.format(len(avg_rating_list_of_data_within_2_std_deviation)*100.0/len(avg_rating_list)))
print('{}% of data for average rating lies within third standard deviation'.format(len(avg_rating_list_of_data_within_3_std_deviation)*100.0/len(avg_rating_list)))


fig = ff.create_distplot([df['Mobile Brand'].tolist()],['Mobile Brand'],show_hist=False)
fig.show()

fig = ff.create_distplot([df['Average Rating'].tolist()],['Mobile Brand'],show_hist=False)
fig.show()

