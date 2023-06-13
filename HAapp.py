import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import datetime
from PIL import Image
import datetime

# Load the data into a DataFrame
data1 = pd.read_csv("data.csv")


st.set_page_config(
    layout="wide",
)

# Set the background color to blue
background_color = "#0000FF"
color_css = f"body {{ background-color: {background_color}; }}"
st.markdown(f'<style>{color_css}</style>', unsafe_allow_html=True)

section = st.sidebar.selectbox("Select a section", ["Home", "Overview", "Data Exploration and Analysis"])


# overview section
if section == "Overview":
    # Set page title
    st.markdown("<h1 style='color: darkblue; font-size: 32px;'> ✅Overview about Covid-19 and the Data </h1>", unsafe_allow_html=True)

    import streamlit as st

    def main():
        # First Column
        st.markdown("## 1-What is the coronavirus that causes COVID-19?😷")
        st.markdown("Coronaviruses are a large family of viruses and are known to cause illness ranging from the common cold to more severe diseases. For most cases, illness is mild and the person recovers by himself/herself.")
        st.markdown("The coronavirus causing COVID-19 is a new strain of coronavirus identified as the cause of an outbreak of respiratory illness first detected in Wuhan, China.")
        st.markdown("Symptoms can include:")
        st.markdown("- Fever")
        st.markdown("- Cough")
        st.markdown("- Shortness of breath")
        st.markdown("- Sore throat")
        st.markdown("To date, there is no specific antiviral treatment. The medical care provided is mainly to relieve and treat symptoms.")
        st.markdown("There is currently no vaccine to protect against COVID-19.")

        # Second Column
        st.markdown("## 2-How does the coronavirus causing COVID-19 spread?🤧")
        st.markdown("**Direct:**")
        st.markdown("Via respiratory droplets produced when an infected person coughs or sneezes.")
        st.markdown("The virus is also present in the saliva.")
        st.markdown("Cover your cough or sneeze with a tissue, then throw the tissue immediately in the trash. If tissues are not available cough/sneeze into your upper arm.")
        st.markdown("If you present respiratory infection symptoms (cough, fever, shortness of breath, sore throat), seek medical care as soon as possible.")
        st.markdown("Do not share utensils or personal items like toothbrush, hairbrush, cups, etc.")
        st.markdown("**Indirect:**")
        st.markdown("By touching a surface or object that has the virus on it and then touching your mouth, nose, or eyes.")
        st.markdown("The virus can remain infective for up to 12 hours on inert material.")

        # Third Column
        st.markdown("## 3-In case you have to travel to an affected country, please take the following precautions 🤒")
        st.markdown("The Ministry of Public Health advises people to avoid traveling to infected countries unless it is absolutely necessary.")
        st.markdown("- Avoid close contact with people who have symptoms of a respiratory infection.")
        st.markdown("- Avoid consumption of raw or undercooked animal products (meat, eggs).")
        st.markdown("- Wash your hands often with soap and water. If soap and water are not readily available, use an alcohol-based hand sanitizer (concentrated >50% alcohol).")
        st.markdown("- Avoid contact with animals (alive or deceased) or visiting live animal markets, wet markets, or animal product markets.")
        st.markdown("- Avoid crowded places. In case it is essential to be present there, wear a facemask.")

    if __name__ == '__main__':
        main()
     
    import streamlit as st

    def main():
        st.markdown("## You can access the full dashboard by ECDC here 👇🏻")
        if st.button("Click me"):
            url = "https://vaccinetracker.ecdc.europa.eu/public/extensions/COVID-19/vaccine-tracker.html#uptake-tab"
            new_tab = f'<a target="_blank" href="{url}">Click me</a>'
            st.markdown(new_tab, unsafe_allow_html=True)

    if __name__ == "__main__":
        main()


        st.markdown("## About the Data 👩🏻‍💻")
        st.markdown("European Centre for Disease Prevention and Control Data")
        st.write("An agency of the European Union")
        st.write("Data source: [ECDC](https://www.ecdc.europa.eu/en/data/downloadable-datasets)")
        import webbrowser
        
        import streamlit as st

        # Dataset 1: 14-day notification rate of new COVID-19 cases and deaths
        st.markdown("## 14-day Notification Rate of COVID-19 Cases and Deaths🕵🏻 ")
        st.write("From 1 June 2020 till 1 Jun 2023, this dataset contains weekly data on 14-day notification rate of new COVID-19 cases and deaths reported by EU/EEA Member States.")
        st.write("The dataset includes the following features: country, country_code, continent, population, indicator, weekly_count, year_week, rate_14_day, cumulative_count, source note.")

        # Dataset 2: Hospital and ICU admission rates and current occupancy for COVID-19
        st.markdown("## Hospital and ICU Admission Rates for COVID-19 📉")
        st.write("From 1 June 2020 till 1 Jun 2023, this dataset provides information about hospitalization and Intensive Care Unit (ICU) admission rates and current occupancy for COVID-19 by date and country.")
        st.write("The dataset includes the following features: country, indicator, date, year_week, value, source.")

        # Dataset 3: COVID-19 vaccination in the EU/EEA
        st.markdown("## COVID-19 Vaccination in the EU/EEA 💉")
        st.write("From 1 June 2020 till 1 Jun 2023, this dataset contains information on COVID-19 vaccination in the EU/EEA. The data are presented in the Vaccine Tracker and collected through The European Surveillance System (TESSy).")
        st.write("The dataset includes the following features: YearWeekISO, ReportingCountry, Denominator, NumberDosesReceived, FirstDose, SecondDose, Region, TargetGroup, Vaccine, Population.")

        # Additional notes or explanations
        st.markdown("## Additional Notes 📋 ")
        st.write("Please note that the datasets may have missing values in some columns or unknown regions in certain datasets. These datasets have been cleaned to handle such limitations.")
        st.write("The data has no duplicates, and outliers have been addressed during preprocessing.")

# Home section
if section == "Home":
    # Set page title
    st.markdown("<h1 style='color: darkblue; font-size: 30 px;'> Welcome to the COVID-19 Impact and Response Dashboard: Evaluating Healthcare Capacity and Vaccination Efforts in the EU/EEA Region 🔬🧪 </h1>", unsafe_allow_html=True)
   
   
    # Load and display the photo
    
    photo = Image.open("vacc.jpg")
    st.image(photo, caption="The latest news, data and analysis on the European’s pandemic response.", use_column_width=True)
    st.markdown("<h2 style='color: blue; font-size: 22px;'>European Centre for Disease Prevention and Control</h2>", unsafe_allow_html=True)
   
    # Add some text or description if needed
    st.write("By Hanine Charanek")

# Section 1: Data Exploration and Analysis
if section == "Data Exploration and Analysis":
    page = st.sidebar.selectbox("Select a page", ["Data on 14-day notification rate of new COVID-19 cases and deaths", "Data on COVID-19 vaccination in the EU/EEA","Data on hospital and ICU admission rates and current occupancy for COVID-19"])

    # Page 1: Data on 14-day notification rate of new COVID-19 cases and deaths
    if page == "Data on 14-day notification rate of new COVID-19 cases and deaths":
        st.markdown("<h1 style='font-size: 28px; color: darkblue;'> 🦠 14-day notification rate of new COVID-19 cases and deaths</h1>", unsafe_allow_html=True)
       
       
        # Define the file path
       

        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv("data.csv")
       
        # Define the available countries
        available_countries = data['country'].unique()
        available_countries = ['All Countries'] + list(available_countries)

        # Top-level filter for country selection
        selected_country = st.selectbox('Select a country', available_countries)

        # Filter the data based on the selected country
        filtered_data = data if selected_country == 'All Countries' else data[data['country'] == selected_country]

        # Calculate the total deaths and cases
        total_deaths = filtered_data[filtered_data['indicator'] == 'deaths']['weekly_count'].sum()
        total_cases = filtered_data[filtered_data['indicator'] == 'cases']['weekly_count'].sum()

        # Display the total count of deaths and cases side by side
        col1, col2 = st.columns(2)
        col1.metric(label="Total Deaths", value=total_deaths)
        col2.metric(label="Total Cases", value=total_cases)

        # Choropleth Map and Heatmap side by side
        col3, col4 = st.columns(2)

        # Choropleth Map
        with col3:
            st.markdown("<h2 style='font-size: 24px;'>Cumulative Count of Deaths by Country</h2>", unsafe_allow_html=True)

            # Group the data by country and calculate the cumulative count of deaths
            grouped_data = filtered_data[filtered_data['indicator'] == 'deaths'].groupby('country')['cumulative_count'].max().reset_index()

            # Create the Choropleth Map
            fig_choropleth = px.choropleth(grouped_data, locations='country', locationmode='country names',
                                        color='cumulative_count', hover_name='country',
                                        title='Cumulative Count of Deaths by Country',
                                        color_continuous_scale='Reds')

            # Customize the layout
            fig_choropleth.update_layout(geo=dict(showframe=False, showcoastlines=False))

            # Display the Choropleth Map
            st.plotly_chart(fig_choropleth)

        # Heatmap
        with col4:
            st.markdown("<h2 style='font-size: 24px;'>Heatmap of 14-Day Notification Rate of New Cases</h2>", unsafe_allow_html=True)

            # Filter the data for cases and convert rate_14_day to numeric
            cases_df = filtered_data[filtered_data['indicator'] == 'cases']
            cases_df['rate_14_day'] = pd.to_numeric(cases_df['rate_14_day'], errors='coerce')

            # Pivot the data to create the Heatmap
            pivot_df = cases_df.pivot(index='year_week', columns='country', values='rate_14_day')

            if selected_country == 'All Countries':
                filtered_df_heatmap = pivot_df
            else:
                filtered_df_heatmap = pivot_df[[selected_country]]

            plt.figure(figsize=(12, 8))
            sns.heatmap(filtered_df_heatmap.transpose(), cmap='YlOrRd', linewidths=0.5)
            plt.xlabel('Year-Week')
            plt.ylabel('Country')
            plt.title('Heatmap of 14-Day Notification Rate of New Cases')

            # Display the Heatmap
            st.pyplot(plt.gcf())

        # Stacked Area Chart and Line Chart side by side
        col5, col6 = st.columns(2)

        # Stacked Area Chart
        with col5:
            st.markdown("<h2 style='font-size: 24px;'>Total cases per Country over the Years</h2>", unsafe_allow_html=True)

            # Filter the data by continent and indicator
            europe_df = filtered_data[(filtered_data['continent'] == 'Europe') & (filtered_data['indicator'] == 'cases')]

            # Get unique European countries
            europe_countries = europe_df['country'].unique()

            # Select countries for the line chart
            selected_countries_line = st.multiselect('Select European countries', europe_countries, default=europe_countries[:5], key='line_chart_countries')

            if selected_countries_line:
                filtered_df_line = europe_df[europe_df['country'].isin(selected_countries_line)]

                # Convert year_week to datetime format
                filtered_df_line['year_week'] = pd.to_datetime(filtered_df_line['year_week'] + '-1', format='%Y-%W-%w')

                fig_line, ax = plt.subplots(figsize=(12, 8))
                for country in selected_countries_line:
                    country_df = filtered_df_line[filtered_df_line['country'] == country]
                    ax.plot(country_df['year_week'].dt.year, country_df['cumulative_count'], label=country)

                ax.set_title('Line Chart of COVID-19 Cases')
                ax.set_xlabel('Year')
                ax.set_ylabel('Cumulative Count of Cases')
                ax.legend()
                plt.xticks(rotation=45)

                # Display the Line Chart
                st.pyplot(fig_line)

        # Line Chart
        with col6:
            st.markdown("<h2 style='font-size: 24px;'>Total Deaths per Country over the Years</h2>", unsafe_allow_html=True)

            # Group the data by country and year
            grouped_data_line = filtered_data[filtered_data['indicator'] == 'deaths'].groupby(['country', filtered_data['year_week'].str[:4]])['weekly_count'].sum().reset_index()
            grouped_data_line.rename(columns={'year_week': 'year', 'weekly_count': 'total_deaths'}, inplace=True)

            # Get the list of available countries
            countries_line = grouped_data_line['country'].unique()
            countries_line = ['All Countries'] + list(countries_line)

            # Get user input for country selection
            selected_country_line = st.selectbox("Select a country or choose 'All Countries' to view all countries", countries_line)

            # Set up the plot
            fig_line, ax = plt.subplots(figsize=(12, 8))

            # Plot the line chart for the selected country(s)
            if selected_country_line == 'All Countries':
                for country in countries_line[1:]:
                    country_data = grouped_data_line[grouped_data_line['country'] == country]
                    ax.plot(country_data['year'], country_data['total_deaths'], marker='o', label=country)
            else:
                country_data = grouped_data_line[grouped_data_line['country'] == selected_country_line]
                ax.plot(country_data['year'], country_data['total_deaths'], marker='o', label=selected_country_line)

            ax.set_xlabel('Year')
            ax.set_ylabel('Total Deaths')
            ax.set_title('Total Deaths per Country over the Years')
            ax.legend()
            plt.xticks(rotation=45)

            # Display the Line Chart
            st.pyplot(fig_line)

       # Page 2: Data on COVID-19 vaccination in the EU/EEA
    elif page == "Data on COVID-19 vaccination in the EU/EEA":
        st.markdown("<h1 style='font-size: 28px; color: darkblue;'>🧪 COVID-19 vaccination in the EU/EEA</h1>", unsafe_allow_html=True)
       
         
        import zipfile
        import pandas as pd

        zip_file_path = 'data (3).zip'
        csv_file_name = 'data (3).csv'

        # Extract the CSV file from the ZIP archive
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extract(csv_file_name)

        # Read the extracted CSV file using pandas
        data_path = csv_file_name
        vaccine_df = pd.read_csv(data_path)

        # Now you can work with the DataFrame `df` containing your CSV data
        # For example, you can print the first few rows
        print(vaccine_df.head())

        def generate_visuals(vaccine_df):
        # Convert relevant columns to numeric types
           
            numeric_cols = ['FirstDose', 'SecondDose', 'Population']
            vaccine_df[numeric_cols] = vaccine_df[numeric_cols].apply(pd.to_numeric)

            # Filter data based on user-selected region and target group
            st.sidebar.markdown("<h3 style='font-size: 16px;'>Vaccine Administered Doses - Figure 1,2</h3>", unsafe_allow_html=True)
            region_filter = st.sidebar.selectbox("Filter by Region", vaccine_df['Region'].unique())
            target_group_filter = st.sidebar.selectbox("Filter by Target Group", vaccine_df['TargetGroup'].unique())

            filtered_data = vaccine_df.copy()
            if region_filter:
                filtered_data = filtered_data[filtered_data['Region'] == region_filter]
            if target_group_filter:
                filtered_data = filtered_data[filtered_data['TargetGroup'] == target_group_filter]

            # Visual 1: Pie Chart of Distribution of Vaccine Doses Administered
           
            vaccine_counts = filtered_data.groupby('Vaccine')[['FirstDose', 'SecondDose']].sum().reset_index()

            # Create two columns for the visuals
            col1, col2 = st.columns(2)

            # Pie Chart
            with col1:
                st.markdown("<h2 style='font-size: 24px;'>Distribution of Vaccine Doses Administered </h2>", unsafe_allow_html=True)
                fig, ax1 = plt.subplots(figsize=(6, 6))  # Adjust the figsize here
                ax1.pie(vaccine_counts['FirstDose'], labels=vaccine_counts['Vaccine'], autopct='%1.1f%%')
                ax1.axis('equal')
                st.pyplot(fig)

            # Line Chart
            with col2:
                st.markdown("<h2 style='font-size: 24px;'>Cumulative Number of Doses Administered by Week </h2>", unsafe_allow_html=True)
                grouped_data = filtered_data.groupby('YearWeekISO')[['FirstDose', 'SecondDose', 'Population']].sum().reset_index()

                fig, ax2 = plt.subplots(figsize=(15, 6))
                for v in vaccine_counts['Vaccine']:
                    vaccine_data = grouped_data.copy()
                    vaccine_data['Vaccine'] = v
                    vaccine_data['CumulativeVaccineUptake'] = (vaccine_data['FirstDose'] + vaccine_data['SecondDose']) / vaccine_data['Population'] * 100
                    ax2.plot(vaccine_data['YearWeekISO'], vaccine_data['CumulativeVaccineUptake'], label=v)

                ax2.set_xlabel('Week')
                ax2.set_ylabel('Cumulative Vaccine Uptake %')
                ax2.legend()
                st.pyplot(fig)

        generate_visuals(vaccine_df)



        def visualize_data():
            # Read the data from the CSV file
            import zipfile
            import pandas as pd

            zip_file_path = 'data (3).zip'
            csv_file_name = 'data (3).csv'

            # Extract the CSV file from the ZIP archive
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extract(csv_file_name)

            # Read the extracted CSV file using pandas
            data_path = csv_file_name
            vaccine_df = pd.read_csv(data_path)

            # Group the data by target group and calculate the sum of doses administered
            grouped_df = vaccine_df.groupby('TargetGroup')[['FirstDose', 'SecondDose']].sum().reset_index()

            # Define the target groups and corresponding colors
            target_groups = ['HCW', 'LTCF', 'Age0_4', 'Age5_9', 'Age10_14', 'Age15_17', 'Age18_24', 'Age25_49', 'Age50_59', 'Age60_69', 'Age70_79', 'Age80+']
            colors = ['blue', 'green', 'orange', 'purple', 'pink', 'cyan', 'brown', 'red', 'gray', 'magenta', 'yellow', 'lightblue']

            # Create a bar chart
           
            fig1, ax1 = plt.subplots(figsize=(12, 8))
            ax1.bar(grouped_df['TargetGroup'], grouped_df['FirstDose'], label='First Dose', color=colors[0])
            ax1.bar(grouped_df['TargetGroup'], grouped_df['SecondDose'], bottom=grouped_df['FirstDose'], label='Second Dose', color=colors[1])

            # Set the title and labels
            ax1.set_xlabel('Target Group')
            ax1.set_ylabel('Number of Doses')

            # Set the x-axis tick labels
            ax1.set_xticklabels(grouped_df['TargetGroup'], rotation=45)

            # Add a legend
            ax1.legend()

            # Filter the data based on user-selected region and target group
            st.sidebar.markdown("<h3 style='font-size: 16px;'>Cumulative Vaccine Uptake Percentage by Region and Target Group - Figure 4</h3>", unsafe_allow_html=True)


            region = st.sidebar.selectbox('Select Region', vaccine_df['Region'].unique())
            target_group = st.sidebar.selectbox('Select Target Group', vaccine_df['TargetGroup'].unique())
            filtered_df = vaccine_df[(vaccine_df['Region'] == region) & (vaccine_df['TargetGroup'] == target_group)]

            # Group the filtered data by YearWeekISO and Vaccine and calculate the cumulative vaccine uptake percentage
            grouped_df = filtered_df.groupby(['YearWeekISO', 'Vaccine']).sum().reset_index()
            grouped_df['CumulativeUptake'] = grouped_df.groupby(['Vaccine'])['SecondDose'].cumsum() / grouped_df.groupby(['Vaccine'])['Denominator'].cumsum() * 100

            # Create a list of unique vaccines
            vaccines = grouped_df['Vaccine'].unique()

            # Create the line chart
           
            fig2, ax2 = plt.subplots(figsize=(10, 6))

            # Plot the lines for each vaccine
            for vaccine in vaccines:
                # Filter the grouped data for the current vaccine
                vaccine_data = grouped_df[grouped_df['Vaccine'] == vaccine]

                # Plot the cumulative uptake percentage
                ax2.plot(vaccine_data['YearWeekISO'], vaccine_data['CumulativeUptake'], label=vaccine)

            # Set the title and labels
            ax2.set_xlabel('YearWeekISO')
            ax2.set_ylabel('Cumulative Uptake Percentage')

            # Add a legend
            ax2.legend()

            # Display the figures side by side using Streamlit
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<h2 style='font-size: 24px;'>Number of Doses Administered by Target Group </h2>", unsafe_allow_html=True)
                st.pyplot(fig1)
            with col2:
                st.markdown("<h2 style='font-size: 24px;'>Cumulative Vaccine Uptake Percentage by Region and Target Group </h2>", unsafe_allow_html=True)
                st.pyplot(fig2)

        # Run the function to display the plots
        visualize_data()

        import numpy as np
        import seaborn as sns

        # Filter the data by region
        regions = vaccine_df["Region"].unique()
        st.sidebar.markdown("<h3 style='font-size: 16px;'> Evaluating The Government Efforts Filters- Figure 5,6,7</h3>", unsafe_allow_html=True)
        selected_region = st.sidebar.selectbox("Select Region", regions, key="region_selector")

        # Filter the data based on the selected region
        filtered_data = vaccine_df[vaccine_df["Region"] == selected_region]

        # Create a scatter plot
        fig7, ax = plt.subplots()
       
        ax.scatter(filtered_data["NumberDosesReceived"], filtered_data["Population"])
        ax.set_xlabel("Number of Doses Received")
        ax.set_ylabel("Population")

        # Create a stacked bar chart
        fig, ax = plt.subplots()
       
        region_data = filtered_data.groupby("Region")["NumberDosesReceived"].sum()
        region_data.plot(kind="bar", stacked=True, ax=ax)
        ax.set_xlabel("Region")
        ax.set_ylabel("Number of Doses Received")

        # Pivot the data to create a matrix of counts
        heatmap_data = filtered_data.pivot_table(index="TargetGroup", columns="Vaccine", values="NumberDosesReceived", aggfunc=np.sum)

        # Create a heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".0f")
       
        plt.xlabel("Vaccine")
        plt.ylabel("Age Group")

        # Display the plots side by side using Streamlit
        col1, col2, col3 = st.columns(3)
        with col1:
                st.markdown("<h2 style='font-size: 24px;'>Vaccination Efforts vs. Population </h2>", unsafe_allow_html=True)
                st.pyplot(fig7)
        with col2:
                st.markdown("<h2 style='font-size: 24px;'>Distribution of Vaccine Doses for {}</h2>".format(selected_region), unsafe_allow_html=True)
                st.pyplot(fig)
        with col3:
                st.markdown("<h2 style='font-size: 24px;'>Number of Doses Received by Age Groups and Vaccine Types </h2>", unsafe_allow_html=True)
                st.pyplot(plt)
       
       
     # Page 3: Data on hospital and ICU admission rates and current occupancy for COVID-19
    elif page == "Data on hospital and ICU admission rates and current occupancy for COVID-19":
        st.markdown("<h1 style='font-size: 28px; color: darkblue;'> 👩🏻‍⚕️ Hospital and ICU admission rates and current occupancy for COVID-19</h1>", unsafe_allow_html=True)
        @st.cache  # Add caching to improve performance
        def load_data():
    # Read the data from the CSV file
            
            data = pd.read_csv('data1.csv')
            return data

        def visualize_data(data, country, indicator):
            if country == 'All':
                # Filter the data for the specified indicator
                filtered_data = data[data['indicator'] == indicator]
            else:
                # Filter the data for a specific country and indicator
                filtered_data = data[(data['country'] == country) & (data['indicator'] == indicator)]

            # Convert the date column to datetime format
            filtered_data['date'] = pd.to_datetime(filtered_data['date'])

            # Group the data by country and iterate over each group
            grouped_data = filtered_data.groupby('country')

            fig, ax = plt.subplots(figsize=(10, 6))
            for group_name, group_data in grouped_data:
                ax.plot(group_data['date'], group_data['value'], label=group_name)

            ax.set_xlabel('Date')
            ax.set_ylabel('Number of Patients')
            ax.grid(True)
            ax.legend()  # Add legend to differentiate countries

            return fig

        def main():
            # Load the data
            data = load_data()

            # Get unique countries and add 'All' option
            countries = data['country'].unique().tolist()
            countries.insert(0, 'All')

            # Specify the country and indicator
            country = st.selectbox('Select Country', countries)
            indicator = 'Daily hospital occupancy'  # or 'Daily ICU occupancy'

            # Visualize the data
            fig = visualize_data(data, country, indicator)

            # Display the plot using Streamlit
            container1 = st.container()
            with container1:
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("<h2 style='font-size: 24px;'>Daily Hospital Occupancy by Country</h2>", unsafe_allow_html=True)
                    st.pyplot(fig)

                with col2:
                    st.markdown("<h2 style='font-size: 24px;'>Cumulative Daily Occupancy Rate by Country</h2>", unsafe_allow_html=True)
                    # Create the choropleth map
                    filtered_data = data[(data['indicator'] == indicator) & (data['country'].isin(countries))]
                    grouped_data = filtered_data.groupby('country')['value'].cumsum()
                    filtered_data['cumulative_value'] = grouped_data

                    choropleth_fig = px.choropleth(filtered_data, locations='country', locationmode='country names',
                                                color='cumulative_value', color_continuous_scale='YlOrRd',
                                                labels={'cumulative_value': 'Cumulative Occupancy Rate'},
                                                hover_name='country', hover_data=['date', 'value'])

                    st.plotly_chart(choropleth_fig, use_container_width=True)

        if __name__ == '__main__':
            st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable the warning
            main()

        @st.cache  # Add caching to improve performance
        def load_data():
            # Modify the data path to the location of the CSV file
         
            
            # Read the data from the CSV file
            data = pd.read_csv('new_data.csv')
            return data

        def main():
            # Load the data
            data = load_data()

            # Filter the data for the desired indicators (weekly new hospital admissions or new ICU admissions)
            indicator1 = 'Weekly new hospital admissions per 100k'  # or 'Weekly new ICU admissions per 100k'
            filtered_data1 = data[data['indicator'] == indicator1]

            # Group the data by country, year_week and calculate the average value for each group
            grouped_data1 = filtered_data1.groupby(['country', 'year_week'])['value'].mean().reset_index()

            # Sort the data in descending order
            grouped_data1 = grouped_data1.sort_values('value', ascending=False)

            # Allow the user to select a year_week for filtering
            st.sidebar.markdown("<h3 style='font-size: 16px;'> Weekly new hospital admissions per 100k </h3>", unsafe_allow_html=True)
            selected_year_week = st.sidebar.selectbox('Select a year_week', grouped_data1['year_week'].unique())

            # Filter the data based on the selected year_week
            filtered_data1_year_week = grouped_data1[grouped_data1['year_week'] == selected_year_week]

            # Plot the bar chart for indicator1
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.bar(filtered_data1_year_week['country'], filtered_data1_year_week['value'])
            ax1.set_title(f'{indicator1} in {selected_year_week}')
            ax1.set_xlabel('Country')
            ax1.set_ylabel(f'{indicator1}')
            ax1.set_xticklabels(filtered_data1_year_week['country'], rotation=45)
            ax1.grid(True)

            # Filter the data for the desired indicators (daily hospital occupancy or daily ICU occupancy)
            indicator2 = 'Daily hospital occupancy'  # or 'Daily ICU occupancy'
            filtered_data2 = data[data['indicator'] == indicator2]

            # Group the data by country, year_week and calculate the cumulative sum of occupancy for each group
            grouped_data2 = filtered_data2.groupby(['country', 'year_week'])['value'].sum().reset_index()

            # Pivot the data to create a matrix with year_week as index, countries as columns, and occupancy values as values
            pivoted_data = grouped_data2.pivot(index='year_week', columns='country', values='value')

            # Calculate the cumulative sum of occupancy for each country
            cumulative_data = pivoted_data.cumsum(axis=0)

            # Allow the user to select a country for the stacked area chart
            selected_country2 = st.selectbox('Select a country', cumulative_data.columns)

            # Display the visuals side by side using Streamlit
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<h2 style='font-size: 24px;'>Weekly new hospital admissions per 100k </h2>", unsafe_allow_html=True)
                st.pyplot(fig1)

            with col2:
                st.markdown("<h2 style='font-size: 24px;'>Cumulative Daily Hospital Occupancy in Countries </h2>", unsafe_allow_html=True)
                fig2_country, ax2_country = plt.subplots(figsize=(12, 8))
                ax2_country.plot(cumulative_data.index, cumulative_data[selected_country2], label=selected_country2)
                ax2_country.set_title(f'Cumulative {indicator2} in {selected_country2}')
                ax2_country.set_xlabel('Year_Week')
                ax2_country.set_ylabel('Cumulative Occupancy')
                ax2_country.legend(loc='upper left')
                ax2_country.set_xticklabels(cumulative_data.index, rotation=45)
                st.pyplot(fig2_country)

        if __name__ == '__main__':
            st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable the warning
            main()


