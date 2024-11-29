import pandas as pd
import plotly.express as px

# __ name mangeled way to avoid naming conflicts

# self = this butin cpp


class Utilities:
    __instance = None

    @staticmethod
    def GetInstance():
        if Utilities.__instance is None:
            Utilities.__instance = Utilities()
        return Utilities.__instance

    def __init__(self):  # intializer is the equivelance of constructor in c++
        if Utilities.__instance != None:
            raise Exception("Singleton Class")
        else:
            self.__df = pd.read_csv("cleaned_hotel_bookings.csv")

    def ReadCSV(self):
        return self.__df

    def ProcessFullDate(self):
        self.__df["full_date"] = pd.to_datetime(
            self.__df["full_date"], errors="coerce", format="mixed", dayfirst=True
        )

    def ProcessHasChildren(self):
        self.__df = self.__df["has_children"] = (self.__df["children"] > 0) | (
            self.__df["babies"] > 0
        )

    def ProcessTotalStay(self):
        df["total_stay_of_guest"] = (
            df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
        )

    def QuickCleansing(self):

        self.__df.dropna(how="all", axis=0, inplace=True)
        self.__df.dropna(how="all", axis=1, inplace=True)
        self.__df.drop_duplicates(inplace=True)
        self.ProcessFullDate()
        self.ProcessHasChildren()
        self.ProcessTotalStay()


util = Utilities.GetInstance()
df = util.ReadCSV()
util.QuickCleansing()

print(df.columns)

print(df["full_date"])















class BookingTrendsandCustomerBehavior:

    def cancellations_trends_graph(EndMonth: int = 12, EndYear: int = 2017):
        # [start_month , start_year , end_month , end_year] #Deprecated Approach
        print(
            f"year sample{df["full_date"][0].year} only month {df["full_date"][0].month}"
        )

        cancellations_per_date = (
            df.groupby(
                [
                    pd.Grouper(key="full_date", freq="ME")
                ]  # this way isn't working anymore I found that it works only when the year and month in seperate columns and I don't know why for now ?!      [df["full_date"].year, df["full_date"].month]
            )["is_canceled"]
            .sum()
            .reset_index()
        )
        print(cancellations_per_date.columns)

        cancellations_per_date.columns = ["month_year", "total_cancellations"]

        start_period = pd.Timestamp(month=1, year=2015, day=1)
        print(start_period)
        print(cancellations_per_date.index)
        end_period = pd.Timestamp(month=EndMonth, year=EndYear, day=28)
        cancellations_per_date = cancellations_per_date[
            (cancellations_per_date["month_year"] >= start_period)
            & (cancellations_per_date["month_year"] <= end_period)
        ]
        cancellations_per_date["month_year"] = cancellations_per_date[
            "month_year"
        ].dt.strftime("%m/%Y")

        fig = px.line(
            cancellations_per_date,
            x="month_year",
            y="total_cancellations",
            # color_discrete_map="GnBU"
            title="Cancellation Trends",
            labels={
                "total_cancellations": "Cancellations Count",
                "month_year": "Date Month/Year",
            },
            color_discrete_sequence=px.colors.sequential.haline,
            template="simple_white",
        )
        # fig.show()
        return fig

    # cancellations_trends_graph()

    def lead_times_per_hotel():
        fig = px.box(
            df,
            x="hotel",
            y="lead_time",
            color="hotel",
            title="Lead Time Comparison: City vs. Resort Hotels",
            color_discrete_sequence=px.colors.sequential.Aggrnyl,
            template="simple_white",
        )
        # fig.show()
        return fig

    # lead_times_per_hotel()

    def Cancellations_vs_guests_types():
        cancellation_rates = (
            df.groupby("is_repeated_guest")["is_canceled"].mean().round(2).reset_index()
        )

        cancellation_rates["guest_type"] = cancellation_rates["is_repeated_guest"].map(
            {False: "First Time Guset", True: "Repeatd Guest"}
        )  # Apply mapping to 'is_repeated_guest'
        fig = px.bar(
            cancellation_rates,
            x="guest_type",
            y="is_canceled",
            title="Cancellation Rates by Guest Type",
            labels={"is_canceled": "Cancellation Rate", "guest_type": "Guest Type"},
            color_discrete_sequence=px.colors.sequential.Aggrnyl,
            color="guest_type",
            template="simple_white",
        )
        # fig.show()
        return fig

    # Cancellations_vs_guests_types()

    def cancellations_vs_market_segment():
        df2 = df[df["is_canceled"]]
        cancellation_rates_per_market_segment = (
            df2.groupby("market_segment")["is_canceled"].count().round(2).reset_index()
        )
        arranged_cancellation_rates_per_market_segment = (
            cancellation_rates_per_market_segment.sort_values(
                "is_canceled", ascending=False
            )
        )
        fig = px.bar(
            arranged_cancellation_rates_per_market_segment,
            x="market_segment",
            y="is_canceled",
            color="market_segment",
            labels={
                "is_canceled": "Cancellation Rates",
                "market_segment": "Market Segment",
            },
            title="cancellation_rates_per_market_segment",
            color_discrete_sequence=px.colors.sequential.Aggrnyl,
            template="simple_white",
        )
        # fig.show()
        return fig

    # cancellations_vs_market_segment()

    def relation_of_requests_vs_cancellations():
        fig = px.scatter(
            df,
            x="total_of_special_requests",
            y="is_canceled",
            title="Correlation between Special Requests and Cancellations",
            labels={
                "total_of_special_requests": "Total Special Requests",
                "is_canceled": "Booking Cancelled (True/False)",
            },
            color="is_canceled",  # Color points by cancellation status
            color_discrete_sequence=[
                "#FFF4B7",
                "#006A67",
            ],  # px.colors.sequential.Bluyl
            # color_discrete_map={"True":"#006A67" , "False":"#FFF4B7"}
            template="simple_white",
        )
        # fig.show()
        return fig

        # relation_of_requests_vs_cancellations()

    def cancelation_trends_per_season():
        df_cancelled_true_only = df[df["is_canceled"]]
        cancellation_rates_vs_season = (
            df_cancelled_true_only.groupby("arrival_season")["is_canceled"]
            .count()
            .round(2)
            .reset_index()
        )
        cancellation_rates_vs_season_arranged = (
            cancellation_rates_vs_season.sort_values("is_canceled", ascending=False)
        )
        fig = px.bar(
            cancellation_rates_vs_season_arranged,
            x="arrival_season",
            y="is_canceled",
            color="arrival_season",
            title="seasons with higher booking cancellations?",
            labels={"is_canceled": "Cancellation Counts", "arrival_season": "Season"},
            # color_continuous_scale="GnBU",
            color_discrete_sequence=px.colors.sequential.Aggrnyl,
            template="simple_white",
        )
        # fig.show()
        return fig

    # cancelation_trens_per_season()


class CustomerDemographicsandPreferences:

    def frequent_reserved_and_assigned_rooms():
        room_types_count = (
            df.groupby(["assigned_room_type", "reserved_room_type"])
            .size()
            .reset_index(name="count")
        )

        room_types_pivot = room_types_count.pivot_table(  # transforming data from long format into wide formal for suitable visualization
            index="assigned_room_type",
            columns="reserved_room_type",
            values="count",
            aggfunc="sum",
            fill_value=0,  # Fill NaNs with 0
        )

        fig = px.imshow(
            room_types_pivot,
            labels=dict(
                x="Reserved Room Type",
                y="Assigned Room Type",
                color="Count of Reservations",
            ),
            title="Heatmap of Assigned vs. Reserved Room Types",
            color_continuous_scale="Brwnyl",  # Cividis, Plasma, etc
            template="seaborn",
        )

        # fig.show()
        return fig

    def meal_prefrences_vs_countries():
        grouped_countries_with_meals = (
            df.groupby(["country", "meal"]).size().reset_index(name="count")
        )

        countries_with_meals_pivot = grouped_countries_with_meals.pivot_table(  # transforming data from long format into wide formal for suitable visualization
            index="country",
            columns="meal",
            values="count",
            aggfunc="sum",
            fill_value=0,  # Fill NaNs with 0
        )

        countries_with_meals_pivot["total_meal_counts"] = (
            countries_with_meals_pivot.sum(axis=1)
        )

        top_10_countries_pivot = countries_with_meals_pivot.sort_values(
            by="total_meal_counts", ascending=False
        ).head(10)

        fig = px.bar(
            top_10_countries_pivot,
            labels={
                "country": "Country",
            },
            title="Top 10 Countries & Their Meals Prefrences",
            orientation="v",
            color_discrete_sequence=px.colors.sequential.Brwnyl,
            template="simple_white",
        )
        # fig.show()
        return fig

    def average_stay_per_hotels():

        fig = px.box(
            df,
            x="hotel",  # City vs. Resort
            y="total_stay_of_guest",  # Total length of stay
            color="hotel",  # Color by hotel type
            title="average stay periods city vs resort",
            labels={"total_stay": "Total Nights Stayed", "hotel": "Hotel Type"},
            color_discrete_sequence=px.colors.sequential.Brwnyl,
            template="simple_white",
        )

        # fig.show()
        return fig

    def relation_of_cancelation_rates_and_siblings():
        cancellation_rates_children = df.groupby("has_children")["is_canceled"].mean()

        fig = px.bar(
            cancellation_rates_children,
            x=cancellation_rates_children.index,
            y="is_canceled",
            title="Cancellation by Presence of Children & Babies",
            labels={
                "is_canceled": "Cancellation Rate",
                "has_children": "Has Children/Babies",
            },
            color=cancellation_rates_children.index,
            color_discrete_sequence=px.colors.sequential.Brwnyl,
            template="simple_white",
        )
        fig.update_xaxes(
            tickmode="array",
            tickvals=[False, True],
            ticktext=["No Chils or Babies", "Has Childs or Babies"],
        )

        # fig.show()
        return fig

    def types_of_customers_vs_requiring_parking_rates():
        client_types_vs_parking_spaces = (
            df.groupby("customer_type")["required_car_parking_spaces"]
            .mean()
            .reset_index()
        )

        client_types_vs_parking_spaces_df = client_types_vs_parking_spaces.sort_values(
            "required_car_parking_spaces", ascending=False
        )
        fig = px.bar(
            client_types_vs_parking_spaces_df,
            x="customer_type",
            y="required_car_parking_spaces",
            color="customer_type",
            title="How Frequent Each Customer Type Requires a Parking Place?",
            labels={
                "required_car_parking_spaces": "AverageRequired Parkking Spaces",
                "index": "Customer Type",
            },
            color_discrete_sequence=px.colors.sequential.Brwnyl,
            template="simple_white",
        )

        fig.update_xaxes(
            tickmode="array",
            tickvals=[0, 1, 2, 3],
            ticktext=["Contract", "Group", "Transient", "Transient-Party"],
        )

        # fig.show()
        return fig


# Deprecated Versions of Methods

# def cancellations_trends_graph(start_and_end_date:list):

#         # df["arrival_date_year"] = pd.to_datetime(
#         #     df["arrival_date_year"], format="mixed"
#         # )

#         # print(f"full date year sample{df["arrival_date_year"][0]} only year {df["arrival_date_year"][0].year}")

#         # df["arrival_date_month"] = pd.to_datetime(
#         #     df["arrival_date_month"], format="mixed"
#         # )

#         # print(f"full date month sample{df["arrival_date_month"][0]} only month {df["arrival_date_month"][0].month}")

#         # df = df.mask(int(df["arrival_date_year"].dt.year) == TargettedYear and int(df["arrival_date_month"].dt.month) == TrgettedMonth)

#         print(
#             f"year sample{df["full_date"][0].year} only month {df["full_date"][0].month}"
#         )

#         cancellations_per_date = (
#             df.groupby(
#                 [
#                     pd.Grouper(key="full_date", freq="ME")
#                 ]  # this way isn't working anymore I found that it works only when the year and month in seperate columns and I don't know why for now ?!      [df["full_date"].year, df["full_date"].month]
#             )["is_canceled"]
#             .sum()
#             .reset_index()
#         )
#         print(cancellations_per_date.columns)

#         cancellations_per_date.columns = ["month_year", "total_cancellations"]
#         cancellations_per_date["month_year"] = cancellations_per_date["month_year"].dt.strftime("%m/%Y")
#         fig = px.line(
#             cancellations_per_date,
#             x="month_year",
#             y="total_cancellations",
#             # color_discrete_map="GnBU"
#             title="Cancellation Trends",
#             labels={
#                 "total_cancellations": "Cancellations Count",
#                 "month_year": "Date Month/Year",
#             },
#             color_discrete_sequence=px.colors.sequential.haline,
#             template="simple_white",
#         )
#         # fig.show()
#         return fig
