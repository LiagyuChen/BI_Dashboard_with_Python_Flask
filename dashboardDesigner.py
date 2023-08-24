import pandas as pd
import math

from flask import Flask, render_template


df = pd.read_csv("data/dataset.csv")

# Overall Indicators
totalCost = math.ceil(df.cost.sum())
totalIncome = math.ceil(df.gross_income.sum())
totalQuantity = df.quantity.sum()

# Proportions
branches = df.branch.value_counts()
branchNames = branches.index.tolist()
branchValues = branches.values.tolist()

cities = df.city.value_counts()
cityNames = cities.index.tolist()
cityValues = cities.values.tolist()

custTypes = df.cust_type.value_counts()
custTypeNames = custTypes.index.tolist()
custTypeValues = custTypes.values.tolist()

genders = df.gender.value_counts()
genderNames = genders.index.tolist()
genderValues = genders.values.tolist()

types = df.groupby("type").quantity.sum()
typeNamesLong = types.index.tolist()
typeNames = [x.split(" ")[0] for x in typeNamesLong]
typeValues = types.values.tolist()

payments = df.payment.value_counts()
paymentNames = payments.index.tolist()
paymentValues = payments.values.tolist()

# Average cost from Normal and Member customers
avgNormalCost = round(df[df.cust_type == "Normal"].cost.mean(), 1)
avgMemberCost = round(df[df.cust_type == "Member"].cost.mean(), 1)

# Monthly gross_income
monthIncomes = df.groupby("month").gross_income.sum()
monthIncomeName = monthIncomes.index.tolist()
monthIncomeValue = monthIncomes.values.tolist()
monthIncomeValue = [round(x, 1) for x in monthIncomeValue]

# Rating proportion for each product type
df["rating_level"] = df.rating.astype(str).apply(lambda x : int(x[0]))
typeRatingLevels = df.groupby(["type", "rating_level"]).quantity.count()
typeRatingLevelNames = typeRatingLevels.index.tolist()
typeRatingLevelTypes = [i[0].split(" ")[0] for i in typeRatingLevelNames]
typeRatingLevelRatings = [i[1] for i in typeRatingLevelNames]
typeRatingLevelValues = typeRatingLevels.values.tolist()

# Cust_Type Purchase Quantity at Once
purchaseQuantity = df.groupby(["cust_type", "quantity"]).quantity.count()
purchaseQuantityNames = purchaseQuantity.index.tolist()
purchaseQuantityCustTypes = [i[0] for i in purchaseQuantityNames]
purchaseQuantityQuantities = [i[1] for i in purchaseQuantityNames]
purchaseQuantityValues = purchaseQuantity.values.tolist()

# Gender purchase quantity with different unit_price level
df["price_level"] = pd.cut(df.unit_price, bins = [0, 20, 40, 60, 80, 100], labels=["0-20", "20-40", "40-60", "60-80", "80-100"])
genderPrices = df.groupby(["gender", "price_level"]).quantity.sum()
genderPriceNames = genderPrices.index.tolist()
genderPriceGenders = [i[0] for i in genderPriceNames]
genderPriceLevels = [i[1] for i in genderPriceNames]
genderPriceValues = genderPrices.values.tolist()

# dayOfWeek_Hour Purchase Frequency
dayHours = df.groupby(["day_of_week", "hour"]).quantity.count()
dayHourNames = dayHours.index.tolist()
dayHourDays = [i[0] for i in dayHourNames]
dayHourHours = [i[1] for i in dayHourNames]
dayHourFreqs = dayHours.values.tolist()
# Deal with missing values
dayHourData = {
    'day_of_week': dayHourDays, 
    'hour': dayHourHours, 
    'value': dayHourFreqs
}
dayHourDF = pd.DataFrame(dayHourData).set_index(['day_of_week', 'hour'])
multiIndexDF = pd.MultiIndex.from_product([range(7), range(24)], names=['day_of_week', 'hour'])
dayHourDF = dayHourDF.reindex(multiIndexDF, fill_value=0)
dayHourFrequency = dayHourDF.value.values.tolist()
dayHourHourNames = list(range(24))
dayHourDayNames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# Send data to forend using flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/getData')
def get_data():
    data = {
        'totalCost': str(totalCost), 
        'totalIncome': str(totalIncome), 
        'totalQuantity': str(totalQuantity),
        'branchNames': branchNames, 
        'branchValues': branchValues,
        'cityNames': cityNames, 
        'cityValues': cityValues,
        'custTypeNames': custTypeNames, 
        'custTypeValues': custTypeValues,
        "genderNames": genderNames,
        "genderValues": genderValues,
        'typeNames': typeNames, 
        'typeValues': typeValues,
        'paymentNames': paymentNames, 
        'paymentValues': paymentValues,
        'avgNormalCost': avgNormalCost, 
        'avgMemberCost': avgMemberCost,
        'monthIncomeName': monthIncomeName, 
        'monthIncomeValue': monthIncomeValue,
        'typeRatingLevelTypes': typeRatingLevelTypes, 
        'typeRatingLevelRatings': typeRatingLevelRatings,
        'typeRatingLevelValues': typeRatingLevelValues, 
        'purchaseQuantityCustTypes': purchaseQuantityCustTypes,
        'purchaseQuantityQuantities': purchaseQuantityQuantities, 
        'purchaseQuantityValues': purchaseQuantityValues,
        'genderPriceGenders': genderPriceGenders, 
        'genderPriceLevels': genderPriceLevels,
        'genderPriceValues': genderPriceValues, 
        'dayHourDayNames': dayHourDayNames,
        'dayHourHourNames': dayHourHourNames, 
        'dayHourFrequency': dayHourFrequency
    }
    return data

if __name__ == '__main__':
    app.run(debug = True)

 
