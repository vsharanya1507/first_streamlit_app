import streamlit
streamlit.title('My Moms New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥗 kale , spinach and Rocket smoothie')
streamlit.text('🐔Hard boiled free range egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas 
#my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#streamlit.dataframe(my_fruit_list)
# let's put a pick list here so they can pick the fruit they want to include
##streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
blh = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
pd = pandas.DataFrame(blh)
default_fruit_list = ["Avocado", "Strawberries"]
df = streamlit.dataframe(blh)
try:
        # // This does not work `
        # // per the documentation on teh Lesson 3 `
        # streamlit.multiselect("Pick some fruits, or eat some Floating Rocks.", list(bleh.index),['Avocado','Strawberries']) `
        # assert set(default_fruit_list).issubset(bleh.columns) `
        # // explicit list cast from single column required, set in var or in code `streamlit.dataframe(blh) `

        df.multiselect("Pick some fruits.", list(blh['Fruit']), default_fruit_list)

except Exception as o:
        
        print(o) 

finally:
        
        print("Now download them and put them in your Head; if you consumed Silicon Fruits, you are in need of " "Chelation Therapy.") 

    # streamlit.multiselect("Pick some fruits, or eat some Floating Rocks.", bleh.set_index('Fruit'))

except Exception as f: 
    import this
    print(f)
