import streamlit as st
import mysql.connector
import pandas as pd
import plotly.graph_objects as go

# Function to execute SQL query and display results based on user selection
def execute_query(option, option2):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root',
        database='project'
    )
    cursor = mydb.cursor()

    # Mapping quarters to their respective year and quarter values
    quarters_mapping = {
        '2018 Q1': ('2018', '1'),
        '2018 Q2': ('2018', '2'),
        '2018 Q3': ('2018', '3'),
        '2018 Q4': ('2018', '4'),
        '2019 Q1': ('2019', '1'),
        '2019 Q2': ('2019', '2'),
        '2019 Q3': ('2019', '3'),
        '2019 Q4': ('2019', '4'),
        '2020 Q1': ('2020', '1'),
        '2020 Q2': ('2020', '2'),
        '2020 Q3': ('2020', '3'),
        '2020 Q4': ('2020', '4'),
        '2021 Q1': ('2021', '1'),
        '2021 Q2': ('2021', '2'),
        '2021 Q3': ('2021', '3'),
        '2021 Q4': ('2021', '4'),
        '2022 Q1': ('2022', '1'),
        '2022 Q2': ('2022', '2'),
        '2022 Q3': ('2022', '3'),
        '2022 Q4': ('2022', '4'),
        '2023 Q1': ('2023', '1'),
        '2023 Q2': ('2023', '2'),
        '2023 Q3': ('2023', '3'),
        '2023 Q4': ('2023', '4'),
        '2024 Q1': ('2024', '1')
    }

    year, quarter = quarters_mapping[option2]

    query = f"""select state, sum(Transaction_count) as Transaction_count, sum(transaction_amount) as Transaction_Value 
                from project.map_Transaction
                where year = '{year}' and quater = '{quarter}'
                group by State;"""
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['State', 'Total_Transaction_count', 'Transaction_Value'])


    query1 = f"""select state, sum(Transaction_count) as Transaction_Count, sum(transaction_amount) as Transaction_Value 
                from project.Aggregated_Transaction
                where year = '{year}' and quarter = '{quarter}'
                group by State;"""
    cursor.execute(query1)
    results1 = cursor.fetchall()
    df1 = pd.DataFrame(results1, columns=['State', 'Total_Transaction_count', 'Transaction_Value'])

    st.sidebar.header(":blue-background[Transactions]")
    trans_count = df1['Total_Transaction_count'].sum()
    trans_value = df1['Transaction_Value'].sum()
    st.sidebar.write("Total Transaction count")
    st.sidebar.write(trans_count)
    st.sidebar.write("Total Transaction Value")
    st.sidebar.write(trans_value)
    st.sidebar.subheader("Category")

    query2 = f"""SELECT Transaction_type as Transaction_type, SUM(Transaction_amount) as Transaction_amount
                 FROM Aggregated_Transaction
                 WHERE year = '{year}' AND quarter = '{quarter}'
                 GROUP BY Transaction_type;"""
    cursor.execute(query2)
    results2 = cursor.fetchall()
    df2 = pd.DataFrame(results2, columns=['Transaction_type', 'Transaction_amount'])
    for index, row in df2.iterrows():
        st.sidebar.write(f"{row['Transaction_type']}\t{row['Transaction_amount']}")

    st.sidebar.subheader("TOP 10")

    if st.sidebar.button("State"):
        query3 = f"""select state as state, sum(Transaction_amount) as Transacation_amount 
                    from project.top_transaction
                    WHERE year = '{year}' AND quater = '{quarter}'
                    Group by state
                    order by Transacation_amount desc
                    Limit 10;"""
        cursor.execute(query3)
        results3 = cursor.fetchall()
        df3 = pd.DataFrame(results3, columns=['state', 'Transaction_amount'])
        for index, row in df3.iterrows():
            st.sidebar.write(f"{row['state']}\t{row['Transaction_amount']}")

    if st.sidebar.button("District"):
        query4 = f"""select District_Name as District, sum(Transaction_amount) as Transacation_amount 
                    from project.top_transaction
                    WHERE year = '{year}' AND quater = '{quarter}'
                    Group by District_Name
                    order by Transacation_amount desc
                    Limit 10;"""
        cursor.execute(query4)
        results4 = cursor.fetchall()
        df4 = pd.DataFrame(results4, columns=['District', 'Transaction_amount'])
        for index, row in df4.iterrows():
            st.sidebar.write(f"{row['District']}\t{row['Transaction_amount']}")

    # Prepare text for tooltip
    tooltip_text = [f"State: {state}<br>Total Transaction Count: {count}<br>Transaction Value: {value:,.2f}"
                    for state, count, value in zip(df['State'], df['Total_Transaction_count'], df['Transaction_Value'])]

    fig = go.Figure(data=go.Choropleth(
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locationmode='geojson-id',
        locations=df['State'],
        z=df['Total_Transaction_count'],  # Use raw count for coloring

        autocolorscale=True,  # Let Plotly choose the color scale automatically
        colorscale='Reds',  # Use the Reds color scale

        colorbar=dict(
            title={'text': "Transaction Count"},
            thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',
            tick0=0,
            dtick=20000,
            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        ),
        hovertext=tooltip_text,  # Add tooltip text
        hoverinfo="text+z"
    ))

    fig.update_geos(
        visible=False,
        projection=dict(
            type='conic conformal',
            parallels=[12.472944444, 35.172805555556],
            rotation={'lat': 24, 'lon': 80}
        ),
        lonaxis={'range': [68, 98]},
        lataxis={'range': [6, 38]}
    )

    fig.update_layout(
        title=dict(
            text="Transaction Count in India by State",
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=1,
            pad={'b': 10}
        ),
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=550,
        width=550
    )

    st.plotly_chart(fig)

# User data

# Function to execute SQL query and display results based on user selection
def execute_query1(option, option2):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root',
        database='project'
    )
    cursor = mydb.cursor()

    # Mapping quarters to their respective year and quarter values
    quarters_mapping = {
        '2018 Q1': ('2018', '1'),
        '2018 Q2': ('2018', '2'),
        '2018 Q3': ('2018', '3'),
        '2018 Q4': ('2018', '4'),
        '2019 Q1': ('2019', '1'),
        '2019 Q2': ('2019', '2'),
        '2019 Q3': ('2019', '3'),
        '2019 Q4': ('2019', '4'),
        '2020 Q1': ('2020', '1'),
        '2020 Q2': ('2020', '2'),
        '2020 Q3': ('2020', '3'),
        '2020 Q4': ('2020', '4'),
        '2021 Q1': ('2021', '1'),
        '2021 Q2': ('2021', '2'),
        '2021 Q3': ('2021', '3'),
        '2021 Q4': ('2021', '4'),
        '2022 Q1': ('2022', '1'),
        '2022 Q2': ('2022', '2'),
        '2022 Q3': ('2022', '3'),
        '2022 Q4': ('2022', '4'),
        '2023 Q1': ('2023', '1'),
        '2023 Q2': ('2023', '2'),
        '2023 Q3': ('2023', '3'),
        '2023 Q4': ('2023', '4'),
        '2024 Q1': ('2024', '1')
    }

    year, quarter = quarters_mapping[option2]

    query = f"""select state, sum(registered_users) as Registered_user, sum(Count_App_Opens) as Count_App_Opens  
                from project.Map_User
                where year = '{year}' and quater = '{quarter}'
                group by State;"""
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['State', 'Registered_user', 'Count_App_Opens'])


    query1 = f"""select state, sum(registered_users) as Registered_user, sum(Count_App_Opens) as Count_App_Opens 
                from project.Aggregated_User
                where year = '{year}' and quarter = '{quarter}'
                group by State;"""
    cursor.execute(query1)
    results1 = cursor.fetchall()
    df1 = pd.DataFrame(results1, columns=['State', 'Registered_user', 'Count_App_Opens'])

    st.sidebar.header(":blue-background[Users]")
    trans_count = df1['Registered_user'].sum()
    trans_value = df1['Count_App_Opens'].sum()
    st.sidebar.write("Registered PhonePe User")
    st.sidebar.write(trans_count)
    st.sidebar.write("App open in this Quater")
    st.sidebar.write(trans_value)
    st.sidebar.subheader("Based On Brand PhonePe Users")

    query2 = f"""SELECT Brand as Brand, SUM(Brand_Count) as Brand_count
                 FROM Aggregated_User
                 WHERE year = '{year}' AND quarter = '{quarter}'
                 GROUP BY Brand;"""
    cursor.execute(query2)
    results2 = cursor.fetchall()
    df2 = pd.DataFrame(results2, columns=['Brand', 'Brand_count'])
    for index, row in df2.iterrows():
        st.sidebar.write(f"{row['Brand']}\t{row['Brand_count']}")

    st.sidebar.subheader("TOP 10 State and District Users")
    if st.sidebar.button("State"):
        query3 = f"""select state as state, sum(Registered_Users) as Registered_users 
                    from project.top_User
                    WHERE year = '{year}' AND quater = '{quarter}'
                    Group by state
                    order by Registered_Users desc
                    Limit 10;"""
        cursor.execute(query3)
        results3 = cursor.fetchall()
        df3 = pd.DataFrame(results3, columns=['state', 'Registered_users'])
        for index, row in df3.iterrows():
            st.sidebar.write(f"{row['state']}\t{row['Registered_users']}")

    if st.sidebar.button("District"):
        query4 = f"""select District_Name as District, sum(Registered_Users) as Registered_users
                    from project.top_User
                    WHERE year = '{year}' AND quater = '{quarter}'
                    Group by District_Name
                    order by Registered_users desc
                    Limit 10;"""
        cursor.execute(query4)
        results4 = cursor.fetchall()
        df4 = pd.DataFrame(results4, columns=['District', 'Registered_users'])
        for index, row in df4.iterrows():
            st.sidebar.write(f"{row['District']}\t{row['Registered_users']}")

    # Prepare text for tooltip
    tooltip_text = [f"State: {state}<br>Registered User: {count}<br>App Opened: {value}"
                    for state, count, value in zip(df['State'], df['Registered_user'], df['Count_App_Opens'])]

    fig = go.Figure(data=go.Choropleth(
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locationmode='geojson-id',
        locations=df['State'],
        z=df['Registered_user'],  # Use raw count for coloring

        autocolorscale=True,  # Let Plotly choose the color scale automatically
        colorscale='Reds',  # Use the Reds color scale

        colorbar=dict(
            title={'text': "Registered User"},
            thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',
            tick0=0,
            dtick=20000,
            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        ),
        hovertext=tooltip_text,  # Add tooltip text
        hoverinfo="text+z"
    ))

    fig.update_geos(
        visible=False,
        projection=dict(
            type='conic conformal',
            parallels=[12.472944444, 35.172805555556],
            rotation={'lat': 24, 'lon': 80}
        ),
        lonaxis={'range': [68, 98]},
        lataxis={'range': [6, 38]}
    )

    fig.update_layout(
        title=dict(
            text="Registered User in India by State",
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=1,
            pad={'b': 10}
        ),
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=550,
        width=550
    )

    st.plotly_chart(fig)

# Insurance data

# Function to execute SQL query and display results based on user selection
def execute_query2(option, option2):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root',
        database='project'
    )
    cursor = mydb.cursor()

    # Mapping quarters to their respective year and quarter values
    quarters_mapping = {
        '2018 Q1': ('2018', '1'),
        '2018 Q2': ('2018', '2'),
        '2018 Q3': ('2018', '3'),
        '2018 Q4': ('2018', '4'),
        '2019 Q1': ('2019', '1'),
        '2019 Q2': ('2019', '2'),
        '2019 Q3': ('2019', '3'),
        '2019 Q4': ('2019', '4'),
        '2020 Q1': ('2020', '1'),
        '2020 Q2': ('2020', '2'),
        '2020 Q3': ('2020', '3'),
        '2020 Q4': ('2020', '4'),
        '2021 Q1': ('2021', '1'),
        '2021 Q2': ('2021', '2'),
        '2021 Q3': ('2021', '3'),
        '2021 Q4': ('2021', '4'),
        '2022 Q1': ('2022', '1'),
        '2022 Q2': ('2022', '2'),
        '2022 Q3': ('2022', '3'),
        '2022 Q4': ('2022', '4'),
        '2023 Q1': ('2023', '1'),
        '2023 Q2': ('2023', '2'),
        '2023 Q3': ('2023', '3'),
        '2023 Q4': ('2023', '4'),
        '2024 Q1': ('2024', '1')
    }

    year, quarter = quarters_mapping[option2]

    if int(year) < 2020 or (int(year) == 2020 and int(quarter) < 2):
        st.write("No data available")
        return

    query = f"""select state, sum(Insurance_Count) as Total_Insurance, sum(Insurance_value) as Insurance_value  
                from project.Map_insurance
                where year = '{year}' and quater = '{quarter}'
                group by State;"""
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['State', 'Insurance_Count', 'Insurance_value'])


    query1 = f"""select state, sum(Transactions_Count) as Insurance_count, sum(Transaction_Value) as Insurance_value
                from project.Aggregated_insurance
                where year = '{year}' and quater = '{quarter}'
                group by State;"""
    cursor.execute(query1)
    results1 = cursor.fetchall()
    df1 = pd.DataFrame(results1, columns=['State', 'Insurance_count', 'Insurance_value'])

    st.sidebar.header(":blue-background[Insurance]")
    trans_count = df1['Insurance_count'].sum()
    trans_value = df1['Insurance_value'].sum()
    st.sidebar.write("No. of People Registered Insurance")
    st.sidebar.write(trans_count)
    st.sidebar.write("Insurance Value in this Quater")
    st.sidebar.write(trans_value)
    st.sidebar.subheader("TOP 10 State and District By Insurance Value")
    
    if st.sidebar.button("state"):

        query3 = f"""select state as state, sum(Insurance_value) as Insurance_value
                    from project.Top_insurance
                    WHERE year = '{year}' AND quater = '{quarter}'
                    Group by state
                    order by Insurance_value desc
                    Limit 10;"""
        cursor.execute(query3)
        results3 = cursor.fetchall()
        df3 = pd.DataFrame(results3, columns=['state', 'Insurance_value'])
        for index, row in df3.iterrows():
            st.sidebar.write(f"{row['state']}\t{row['Insurance_value']}")

    if st.sidebar.button("District"):
        query4 = f"""select District_Name as District, sum(Insurance_value) as Insurance_value
                    from project.Top_insurance
                    WHERE year = '{year}' AND quater = '{quarter}'
                    Group by District_Name
                    order by Insurance_value desc
                    Limit 10;"""
        cursor.execute(query4)
        results4 = cursor.fetchall()
        df4 = pd.DataFrame(results4, columns=['District', 'Insurance_value'])
        for index, row in df4.iterrows():
            st.sidebar.write(f"{row['District']}\t{row['Insurance_value']}")

    # Prepare text for tooltip
    tooltip_text = [f"State: {state}<br>Insurance_Count: {count}<br>Insurance_value: {value}"
                    for state, count, value in zip(df['State'], df['Insurance_Count'], df['Insurance_value'])]

    fig = go.Figure(data=go.Choropleth(
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locationmode='geojson-id',
        locations=df['State'],
        z=df['Insurance_Count'],  # Use raw count for coloring

        autocolorscale=True,  # Let Plotly choose the color scale automatically
        colorscale='Reds',  # Use the Reds color scale

        colorbar=dict(
            title={'text': "Insurance Count"},
            thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',
            tick0=0,
            dtick=20000,
            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        ),
        hovertext=tooltip_text,  # Add tooltip text
        hoverinfo="text+z"
    ))

    fig.update_geos(
        visible=False,
        projection=dict(
            type='conic conformal',
            parallels=[12.472944444, 35.172805555556],
            rotation={'lat': 24, 'lon': 80}
        ),
        lonaxis={'range': [68, 98]},
        lataxis={'range': [6, 38]}
    )

    fig.update_layout(
        title=dict(
            text="No of Insurance taken in India by State",
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=1,
            pad={'b': 10}
        ),
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=550,
        width=550
    )

    st.plotly_chart(fig)


option, option2 = st.sidebar.columns([1, 1])  # Split the sidebar into two columns

option = option.selectbox(
    "Please select",
    ("Transaction", "User","Insurance"),
    index=None
)

option2 = option2.selectbox(
    "Select Quarter",
    ("2018 Q1", "2018 Q2", "2018 Q3", "2018 Q4",
     "2019 Q1", "2019 Q2", "2019 Q3", "2019 Q4",
     "2020 Q1", "2020 Q2", "2020 Q3", "2020 Q4",
     "2021 Q1", "2021 Q2", "2021 Q3", "2021 Q4",
     "2022 Q1", "2022 Q2", "2022 Q3", "2022 Q4",
     "2023 Q1", "2023 Q2", "2023 Q3", "2023 Q4",
     "2024 Q1"
     ),
    index=None,
    help="Choose an option"
)


if option=="Transaction" and option2:
    execute_query(option, option2)
elif option=="User" and option2:
    execute_query1(option,option2)
elif option=="Insurance" and option2:
    execute_query2(option,option2)    
