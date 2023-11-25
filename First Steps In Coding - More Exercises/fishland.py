mackerel_kg_price = float(input())
sprinkle_kg_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())


bonito_kg_price = ((60 / 100) * mackerel_kg_price) + mackerel_kg_price
bonito_total_price = bonito_kg_price * bonito_kg
safrid_kg_price = ((80 / 100) * sprinkle_kg_price) + sprinkle_kg_price
safrid_total_price = safrid_kg_price * safrid_kg
mussels_price = mussels_kg * 7.50

all_price = bonito_total_price + safrid_total_price + mussels_price

print(f"{all_price:.2f}")