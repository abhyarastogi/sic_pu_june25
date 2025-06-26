total_land_acres = 80
acres_per_segment = 80/5

tomato_total_tonne = (10*acres_per_segment*0.3)+(12*acres_per_segment*0.7)
tomato_total_kg = tomato_total_tonne * 1000
tomato_sales = 7 * tomato_total_kg

potato_total_tonne = 10 * acres_per_segment
potato_total_kg = potato_total_tonne * 1000
potato_sales = 20 * potato_total_kg

cabbage_total_tonne = 14 * acres_per_segment
cabbage_total_kg = cabbage_total_tonne * 1000
cabbage_sales = 24 * cabbage_total_kg

sunflower_total_tonne = 0.7 * acres_per_segment
sunflower_total_kg = sunflower_total_tonne * 1000
sunflower_sales = 200 * sunflower_total_kg

sugarcane_total_tonne = 45 * acres_per_segment
sugarcane_sales = 4000 * sugarcane_total_tonne

overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
print(('Overall sales achieved by Mahesh through 80acres land was {}Rs').format(overall_sales))
chemicalfree_sales_11_months = tomato_sales + potato_sales + cabbage_sales + sunflower_sales
print(('Chemical free sales at the end of 11 months is {}Rs').format(chemicalfree_sales_11_months))
