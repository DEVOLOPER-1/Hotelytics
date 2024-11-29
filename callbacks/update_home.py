from dash import Input, Output
from graphs import (
    BookingTrendsandCustomerBehavior as BTCB,
    CustomerDemographicsandPreferences as CDP,
)


def register_callbacks(app):
    # @app.callback(
    #     Output("tabs_container", "active_tab"),
    #     [Input("navigation_through_tabs", "active_page")],
    # )

    @app.callback(
        Output("Cancelation_trands_graph", "figure"),
        [Input("YearSlider", "value"), Input("MonthSlider", "value")],
    )
    def UpdateCancelationTrendsGraph(YearSlider: int, MonthSlider: int):
        #  [1, 2015, 12, 2017]
        return BTCB.cancellations_trends_graph(MonthSlider, YearSlider)

    def switch_tab(active_page):
        if active_page == 1:
            return "Booking Trends and Customer Behavior"

        elif active_page == 2:
            return "Customer Demographics and Preferences"

        else:
            return "Booking Trends and Customer Behavior"
